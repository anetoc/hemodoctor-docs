# Alt Routes Feature Design v2.6.0

**Date:** 2025-10-22
**Status:** Design Phase
**Priority:** P3 (Feature)
**Estimated Effort:** 4 hours

---

## 1. Executive Summary

Alternative routing (alt_routes) provides alternative syndrome interpretations when clinical findings match multiple diagnostic criteria but precedence rules select only one for display. This feature enables complete clinical decision traceability by preserving all plausible diagnostic pathways.

**Key Benefits:**
- **Audit Trail:** Shows "path not taken" for regulatory compliance
- **Clinical Transparency:** Explains why syndrome X was chosen over syndrome Y
- **Retrospective Analysis:** Identifies syndrome co-occurrence patterns
- **Debugging:** Helps understand precedence rule outcomes

---

## 2. Requirements Analysis

### 2.1 Functional Requirements

**FR-1: Alternative Route Generation**
- System SHALL generate alt_routes for syndromes that match evidence but are not selected
- Alt_routes SHALL exclude syndromes already in top_syndromes
- Alt_routes SHALL be sorted by clinical confidence (highest first)

**FR-2: Precedence Integration**
- Alt_routes SHALL respect existing precedence rules (06_route_policy_hybrid.yaml)
- Critical syndromes that short-circuit SHALL have empty alt_routes
- Priority syndromes SHALL show other priority syndromes as alt_routes

**FR-3: Conflict Resolution Audit**
- Alt_routes SHALL include conflict resolution metadata (from 07_conflict_matrix_hybrid.yaml)
- System SHALL explain why each alt_route was not selected (precedence reason)

**FR-4: Determinism**
- Same CBC input SHALL always produce same alt_routes (deterministic)
- Route_id computation SHALL include alt_routes in hash
- WORM log SHALL preserve alt_routes for audit trail

### 2.2 Non-Functional Requirements

**NFR-1: Performance**
- Alt_routes generation SHALL add <5ms to pipeline latency
- Target: Total latency remains <10ms avg (current: 2.5ms)

**NFR-2: Memory**
- Alt_routes SHALL add <2MB memory per case
- Max alt_routes per case: 10 syndromes (reasonable limit)

**NFR-3: Backward Compatibility**
- Existing tests SHALL continue passing (no regressions)
- Pipeline API SHALL remain compatible (alt_routes is additive field)

---

## 3. Architecture Design

### 3.1 Data Structures

```python
# Alt Route Entry (one alternative syndrome)
class AltRoute:
    """
    Represents one alternative diagnostic route.

    Attributes:
        syndrome_id: Syndrome ID (e.g., "S-IDA")
        criticality: Criticality level (critical/priority/routine)
        confidence: Clinical confidence score (0.0-1.0)
        suppression_reason: Why this route was not selected
        conflict_with: Syndrome ID it conflicted with (if applicable)
    """
    syndrome_id: str
    criticality: str
    confidence: float  # 0.0-1.0 (based on evidence strength)
    suppression_reason: str
    conflict_with: Optional[str]

# Pipeline Result (extended)
result = {
    "top_syndromes": ["S-TMA"],  # Selected syndrome(s)
    "alt_routes": [  # NEW FIELD
        {
            "syndrome_id": "S-PTI",
            "criticality": "priority",
            "confidence": 0.75,
            "suppression_reason": "Precedence: S-TMA (critical) > S-PTI (priority)",
            "conflict_with": "S-TMA"
        }
    ],
    # ... existing fields ...
}
```

### 3.2 Algorithm Flow

```
Input: CBC data
  ↓
1. Evaluate 79 evidences (unchanged)
  ↓
2. Detect ALL syndromes (modified)
   - Collect ALL true syndromes (don't short-circuit yet)
   - Sort by precedence (critical → priority → review → routine)
  ↓
3. Apply precedence selection (NEW)
   - top_syndromes = first N by precedence
   - remaining_syndromes = all other true syndromes
  ↓
4. Generate alt_routes (NEW)
   - For each syndrome in remaining_syndromes:
     - Compute confidence score
     - Determine suppression_reason
     - Check conflict_matrix
     - Create AltRoute entry
   - Sort by confidence (highest first)
   - Limit to max_alt_routes (10)
  ↓
5. Compute route_id (modified)
   - Include alt_routes in hash for determinism
  ↓
6. WORM log (modified)
   - Persist alt_routes for audit trail
  ↓
Output: result with alt_routes
```

### 3.3 Confidence Scoring

Confidence score for alt_routes is computed based on evidence strength:

```python
def compute_alt_route_confidence(syndrome: SyndromeResult, evidences: List[EvidenceResult]) -> float:
    """
    Compute confidence score for alternative route.

    Logic:
        - Start with base score: 1.0
        - For each required evidence (from combine logic):
            - If present with strength "strong": +0.0 (no penalty)
            - If present with strength "moderate": -0.1
            - If present with strength "weak": -0.2
            - If missing: -0.3
        - Clamp to [0.0, 1.0]

    Example:
        S-PTI requires: [E-PLT-LOW, E-ISOLATED-THROMBO]
        - E-PLT-LOW: present, strong
        - E-ISOLATED-THROMBO: present, moderate
        → Confidence = 1.0 - 0.1 = 0.90
    """
```

### 3.4 Suppression Reasons

Taxonomy of suppression reasons:

1. **Precedence (Critical > Priority):** "Precedence: S-TMA (critical) > S-PTI (priority)"
2. **Precedence (Critical Order):** "Precedence: S-NEUTROPENIA-GRAVE (critical #1) > S-TMA (critical #3)"
3. **Precedence (Priority Order):** "Precedence: S-CML (severity_weight 0.95) > S-IDA (0.80)"
4. **Conflict (Negative Pair):** "Conflict: S-TMA excludes S-PTI (negative pair)"
5. **Conflict (Soft):** "Conflict: S-IDA reduces S-ALFA-THAL confidence (soft conflict)"
6. **Review Sample:** "Precedence: S-REVIEW-SAMPLE blocks all other results"

---

## 4. Implementation Plan

### 4.1 Phase 1: Modify detect_syndromes() (1 hour)

**File:** `src/hemodoctor/engines/syndrome.py`

**Changes:**
1. Modify `detect_syndromes()` to collect ALL true syndromes (not just top N)
2. Return tuple: `(top_syndromes, all_syndromes)`
3. Apply precedence logic to separate top vs alt

**Code:**
```python
def detect_syndromes(
    evidences: List[EvidenceResult],
    yaml_parser: YAMLParser
) -> Tuple[List[SyndromeResult], List[SyndromeResult]]:
    """
    Detect syndromes and separate into top vs alternative routes.

    Returns:
        Tuple of (top_syndromes, all_syndromes)
    """
    # Step 1: Collect ALL true syndromes
    all_syndromes = []
    for syndrome_def in syndrome_defs:
        if is_syndrome_present(syndrome_def, present_ids):
            syndrome = SyndromeResult(...)
            all_syndromes.append(syndrome)

    # Step 2: Sort by precedence
    all_syndromes.sort(key=lambda s: ...)

    # Step 3: Apply short-circuit logic
    top_syndromes = apply_precedence(all_syndromes)

    return top_syndromes, all_syndromes
```

### 4.2 Phase 2: Add generate_alt_routes() (1 hour)

**File:** `src/hemodoctor/engines/syndrome.py` (new function)

**Code:**
```python
def generate_alt_routes(
    top_syndromes: List[SyndromeResult],
    all_syndromes: List[SyndromeResult],
    evidences: List[EvidenceResult],
    yaml_parser: YAMLParser,
    max_alt_routes: int = 10
) -> List[Dict[str, Any]]:
    """
    Generate alternative routes from syndromes not selected.

    Args:
        top_syndromes: Selected syndromes (displayed to user)
        all_syndromes: All true syndromes (before precedence)
        evidences: Evidence results (for confidence scoring)
        yaml_parser: YAML parser instance
        max_alt_routes: Max number of alt_routes to return

    Returns:
        List of alt_route dicts, sorted by confidence
    """
    top_ids = {s.id for s in top_syndromes}
    alt_routes = []

    for syndrome in all_syndromes:
        if syndrome.id in top_ids:
            continue  # Skip syndromes already in top

        # Compute confidence
        confidence = compute_alt_route_confidence(syndrome, evidences)

        # Determine suppression reason
        suppression_reason = determine_suppression_reason(
            syndrome, top_syndromes, yaml_parser
        )

        # Check conflict
        conflict_with = check_conflict(syndrome, top_syndromes, yaml_parser)

        alt_routes.append({
            "syndrome_id": syndrome.id,
            "criticality": syndrome.criticality,
            "confidence": confidence,
            "suppression_reason": suppression_reason,
            "conflict_with": conflict_with,
        })

    # Sort by confidence (highest first)
    alt_routes.sort(key=lambda r: -r["confidence"])

    # Limit to max
    return alt_routes[:max_alt_routes]
```

### 4.3 Phase 3: Integrate with pipeline.py (30 min)

**File:** `src/hemodoctor/api/pipeline.py`

**Changes:**
1. Call `generate_alt_routes()` after syndrome detection
2. Add `alt_routes` field to result dict
3. Update `compute_route_id()` to include alt_routes

**Code:**
```python
def analyze_cbc(cbc_data: Dict[str, Any]) -> Dict[str, Any]:
    # ... existing code ...

    # 5. Syndromes (35 syndromes, short-circuit on critical)
    top_syndromes, all_syndromes = detect_syndromes(evidences, yaml_parser)

    # 5b. Alt Routes (NEW)
    alt_routes = generate_alt_routes(top_syndromes, all_syndromes, evidences, yaml_parser)

    # ... existing code ...

    result = {
        "top_syndromes": [s.id for s in top_syndromes],
        "alt_routes": alt_routes,  # NEW FIELD
        # ... existing fields ...
    }

    return result
```

### 4.4 Phase 4: Update route_id computation (30 min)

**File:** `src/hemodoctor/api/pipeline.py`

**Changes:**
1. Include alt_routes in route_id hash for determinism

**Code:**
```python
def compute_route_id(
    evidences: List,
    syndromes: List,
    alt_routes: List[Dict]  # NEW PARAMETER
) -> str:
    """Compute deterministic SHA256 hash including alt_routes."""
    # ... existing evidence/syndrome logic ...

    # Add alt_routes (sorted for determinism)
    alt_route_ids = sorted([r["syndrome_id"] for r in alt_routes])

    route_data = {
        "evidences": present_evidence_ids,
        "syndromes": syndrome_ids,
        "alt_routes": alt_route_ids,  # NEW
    }

    # ... hash computation ...
```

### 4.5 Phase 5: Enable tests (30 min)

**File:** `tests/audit/test_routing_audit.py`

**Changes:**
1. Remove `@pytest.mark.skip` from 9 tests
2. Implement test bodies based on expected behavior

**Example:**
```python
def test_alt_routes_field_exists():
    """Test alt_routes field exists in result."""
    cbc = {"hb": 15.0, "wbc": 8.0, "plt": 250, "age_years": 30, "sex": "M"}
    result = analyze_cbc(cbc)

    assert "alt_routes" in result
    assert isinstance(result["alt_routes"], list)

def test_alt_routes_empty_for_normal():
    """Test alt_routes is empty for normal CBC."""
    cbc = {"hb": 15.0, "wbc": 8.0, "plt": 250, "age_years": 30, "sex": "M"}
    result = analyze_cbc(cbc)

    # Normal CBC → S-INCONCLUSIVO only
    assert len(result["alt_routes"]) == 0

def test_alt_routes_contains_excluded_syndromes():
    """Test alt_routes contains syndromes excluded by precedence."""
    cbc = {
        "hb": 7.0,
        "plt": 25,
        "ldh": 980,
        "morphology": {"esquistocitos": True},
        "age_years": 30,
        "sex": "M"
    }
    result = analyze_cbc(cbc)

    # Both S-TMA (critical) and S-ANEMIA-GRAVE (critical) detected
    # S-TMA has precedence (line 3 vs line 5)
    assert "S-TMA" in result["top_syndromes"]

    # S-ANEMIA-GRAVE should be in alt_routes
    alt_route_ids = [r["syndrome_id"] for r in result["alt_routes"]]
    assert "S-ANEMIA-GRAVE" in alt_route_ids
```

---

## 5. Test Coverage

### 5.1 Unit Tests (9 total)

All in `tests/audit/test_routing_audit.py`:

1. ✅ `test_alt_routes_field_exists()` - Field presence
2. ✅ `test_alt_routes_empty_for_normal()` - Empty for normal CBC
3. ✅ `test_alt_routes_contains_excluded_syndromes()` - Precedence exclusions
4. ✅ `test_alt_routes_audit_trail()` - Conflict resolution metadata
5. ✅ `test_alt_routes_max_count()` - Max limit enforced
6. ✅ `test_route_id_includes_alt_routes()` - Determinism (already passing)
7. ✅ `test_alt_routes_not_duplicated()` - No duplication with top_syndromes
8. ✅ `test_alt_routes_sorted_by_confidence()` - Sorted order
9. ✅ `test_alt_routes_empty_for_critical()` - Empty for critical short-circuit
10. ✅ `test_alt_routes_traceability()` - Traceability exists (already passing)

### 5.2 Integration Tests

**Scenario 1: TMA vs PTI (negative pair)**
```
Input: PLT=25, esquistocitos=true, LDH=980
Expected:
  - top_syndromes: ["S-TMA"]
  - alt_routes: [
      {
        "syndrome_id": "S-PTI",
        "confidence": 0.70,
        "suppression_reason": "Precedence: S-TMA (critical) > S-PTI (priority)",
        "conflict_with": "S-TMA"
      }
    ]
```

**Scenario 2: Multiple critical syndromes**
```
Input: ANC=0.3, PLT=8, Hb=6.0
Expected:
  - top_syndromes: ["S-NEUTROPENIA-GRAVE", "S-PLT-CRITICA", "S-ANEMIA-GRAVE"]
    (all critical, co-occurrence allowed per Solution 2)
  - alt_routes: [] (critical syndromes have empty alt_routes)
```

**Scenario 3: IDA vs Alfa-Thal (soft conflict)**
```
Input: MCV=72, ferritin=35, RBC=5.8
Expected:
  - top_syndromes: ["S-ALFA-THAL"]
  - alt_routes: [
      {
        "syndrome_id": "S-IDA",
        "confidence": 0.60,
        "suppression_reason": "Conflict: S-ALFA-THAL (ferritin normal + RBC high)",
        "conflict_with": "S-ALFA-THAL"
      }
    ]
```

---

## 6. Performance Analysis

### 6.1 Computational Complexity

**Before (without alt_routes):**
- Evidence evaluation: O(79) = O(N_evidences)
- Syndrome detection: O(35) = O(N_syndromes)
- Precedence sort: O(35 log 35) = O(N_syndromes log N_syndromes)
- **Total: O(N_evidences + N_syndromes log N_syndromes)**

**After (with alt_routes):**
- Evidence evaluation: O(79) [unchanged]
- Syndrome detection: O(35) [unchanged]
- Precedence sort: O(35 log 35) [unchanged]
- **Alt routes generation: O(35) = O(N_syndromes)** [NEW]
  - Confidence scoring: O(1) per syndrome
  - Conflict check: O(1) per syndrome (hash lookup)
  - Sort alt_routes: O(10 log 10) ≈ O(1) (max 10 alt_routes)
- **Total: O(N_evidences + N_syndromes log N_syndromes)** [SAME BIG-O]

**Conclusion:** No asymptotic complexity increase!

### 6.2 Latency Estimate

**Current pipeline latency:** 2.5ms avg

**Added latency (alt_routes):**
- Compute confidence: 35 syndromes × 0.01ms = 0.35ms
- Check conflicts: 35 syndromes × 0.01ms = 0.35ms
- Sort alt_routes: 10 × log(10) × 0.001ms = 0.03ms
- **Total added: ~0.73ms**

**New estimated latency:** 2.5ms + 0.73ms = **3.23ms avg**

**Target:** <10ms ✅ (32% of target, well within budget!)

### 6.3 Memory Impact

**Alt_route entry size:**
- syndrome_id: 20 bytes (string)
- criticality: 10 bytes (string)
- confidence: 8 bytes (float)
- suppression_reason: 100 bytes (string)
- conflict_with: 20 bytes (string)
- **Total per entry: ~158 bytes**

**Max alt_routes:** 10 entries
**Total added memory:** 158 bytes × 10 = **1.58 KB** ✅ (<<2MB target!)

---

## 7. WORM Log Integration

Alt_routes will be persisted in WORM log for audit trail:

```json
{
  "case_id": "CASE-12345",
  "route_id": "abc123...",
  "top_syndromes": ["S-TMA"],
  "alt_routes": [
    {
      "syndrome_id": "S-PTI",
      "confidence": 0.70,
      "suppression_reason": "Precedence: S-TMA (critical) > S-PTI (priority)",
      "conflict_with": "S-TMA"
    }
  ],
  "timestamp": "2025-10-22T15:30:00Z",
  "hmac": "def456..."
}
```

**HMAC computation:** Alt_routes included in HMAC for integrity verification.

---

## 8. Regulatory Compliance

### 8.1 ISO 13485:2016 (Traceability)

**§7.3.2 Design Outputs:**
- Alt_routes provides complete traceability of clinical decision-making
- Shows why certain diagnostic pathways were not selected
- Enables retrospective validation of precedence rules

### 8.2 ANVISA RDC 657/2022

**Audit Trail Requirement:**
- All clinical decisions must be auditable
- Alt_routes satisfies "path not taken" documentation
- Conflict resolution reasons provide transparency

### 8.3 FDA 21 CFR Part 11

**Electronic Records:**
- Alt_routes persisted in WORM log (immutable)
- HMAC ensures data integrity
- Deterministic route_id enables deduplication

### 8.4 LGPD (Data Privacy)

**Pseudonymization:**
- Alt_routes contain only syndrome IDs (no PHI)
- Confidence scores are aggregate metrics (no identifiable data)

---

## 9. Backward Compatibility

### 9.1 API Changes

**Pipeline result (BEFORE):**
```python
{
    "top_syndromes": ["S-TMA"],
    "evidences_present": ["E-PLT-CRIT-LOW"],
    "route_id": "abc123...",
    # ... other fields ...
}
```

**Pipeline result (AFTER):**
```python
{
    "top_syndromes": ["S-TMA"],
    "alt_routes": [  # NEW FIELD (additive, non-breaking)
        {"syndrome_id": "S-PTI", "confidence": 0.70, ...}
    ],
    "evidences_present": ["E-PLT-CRIT-LOW"],
    "route_id": "abc123...",  # Now includes alt_routes in hash
    # ... other fields ...
}
```

**Breaking changes:** NONE ✅
- New field `alt_routes` is additive
- Existing fields unchanged
- Clients can safely ignore `alt_routes` if not needed

### 9.2 Test Compatibility

**Existing tests (851 tests):**
- All tests check `top_syndromes` (unchanged)
- Route_id computation now includes alt_routes (deterministic, same behavior)
- No test should break

**New tests (9 tests):**
- Currently skipped (no breaking effect)
- Will be enabled after feature implementation

---

## 10. Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Performance regression (>10ms) | Low | Medium | Benchmark before/after, optimize confidence scoring |
| Memory leak (large alt_routes) | Low | High | Enforce max_alt_routes=10 limit |
| Route_id collision (hash changes) | Low | Critical | Include alt_routes in hash deterministically |
| Test failures (regression) | Medium | High | Run full 851 tests before commit |
| Conflict matrix bugs | Medium | Medium | Validate conflict_matrix logic with unit tests |

---

## 11. Success Criteria

**Must Have (Required for completion):**
- ✅ 9/9 alt_routes tests passing (no skips)
- ✅ No regressions (all 851 existing tests still pass)
- ✅ Feature documented in V2_6_0_ALT_ROUTES_SPEC.md
- ✅ BUG-020 closed in BUGS.md
- ✅ Performance <10ms (target: 3-4ms)
- ✅ Memory <2MB (target: <2KB)

**Should Have (Nice to have):**
- ✅ Example cases in documentation
- ✅ Conflict matrix validation tests
- ✅ WORM log integration verified

**Won't Have (Out of scope):**
- V1 probabilistic scoring (confidence uses simple heuristic)
- UI visualization of alt_routes (API only)
- Conflict penalty calibration (V1 feature)

---

## 12. Timeline

**Total Estimate:** 4 hours

| Phase | Duration | Status |
|-------|----------|--------|
| 1. Design (this doc) | 30 min | ✅ Complete |
| 2. Modify detect_syndromes() | 1 hour | Pending |
| 3. Add generate_alt_routes() | 1 hour | Pending |
| 4. Integrate with pipeline | 30 min | Pending |
| 5. Enable tests | 30 min | Pending |
| 6. Run full validation | 30 min | Pending |
| 7. Documentation | 30 min | Pending |

**Target Completion:** 2025-10-22 (same day)

---

## 13. Implementation Checklist

**Phase 1: Modify syndrome.py**
- [ ] Change `detect_syndromes()` signature to return tuple
- [ ] Collect ALL true syndromes (not just top)
- [ ] Apply precedence logic to separate top vs all
- [ ] Update unit tests for new signature

**Phase 2: Add alt_routes generation**
- [ ] Create `generate_alt_routes()` function
- [ ] Implement `compute_alt_route_confidence()`
- [ ] Implement `determine_suppression_reason()`
- [ ] Implement `check_conflict()`
- [ ] Add unit tests for each helper function

**Phase 3: Pipeline integration**
- [ ] Call `generate_alt_routes()` in `analyze_cbc()`
- [ ] Add `alt_routes` field to result dict
- [ ] Update `compute_route_id()` to include alt_routes
- [ ] Update WORM log to persist alt_routes

**Phase 4: Enable tests**
- [ ] Remove `@pytest.mark.skip` from 9 tests
- [ ] Implement test bodies
- [ ] Run 9 alt_routes tests (expect 9/9 passing)

**Phase 5: Validation**
- [ ] Run full test suite (expect 860/860 passing)
- [ ] Benchmark performance (expect <5ms added)
- [ ] Check memory usage (expect <2KB added)

**Phase 6: Documentation**
- [ ] Create V2_6_0_ALT_ROUTES_SPEC.md
- [ ] Update BUGS.md (close BUG-020)
- [ ] Add example cases to docs

---

## 14. References

**YAML Configurations:**
- `config/06_route_policy_hybrid.yaml` - Precedence rules
- `config/07_conflict_matrix_hybrid.yaml` - Conflict resolution

**Source Files:**
- `src/hemodoctor/engines/syndrome.py` - Syndrome detection
- `src/hemodoctor/api/pipeline.py` - Main pipeline
- `src/hemodoctor/engines/worm_log.py` - Audit trail

**Test Files:**
- `tests/audit/test_routing_audit.py` - 9 skipped tests

**Documentation:**
- `BUGS.md` - BUG-020 definition
- This file - Design specification

---

**END OF DESIGN DOCUMENT**
