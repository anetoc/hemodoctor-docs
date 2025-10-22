"""
Sprint 4: Red List FN=0 Validation Tests

CRITICAL REQUIREMENT: FN=0 for ALL 8 critical syndromes
If FN > 0 detected → HALT and request tuning

UPDATED v2.5.0: S-APL removed from Red List (not implemented in YAMLs)
Decision: OPTION A approved by Dr. Abel Costa

Test Structure:
- 240 parametrized tests (one per case - 8 syndromes × 30 cases)
- 1 metrics computation test
- Total: 241 tests

Success Criteria:
- FN = 0 for all 8 critical syndromes
- Sensitivity = 100% for all 8 critical
- Pass rate = 100% (241/241 tests)
"""

import pytest
import json
from pathlib import Path
from typing import Dict, List

from hemodoctor.api.pipeline import analyze_cbc


# Load critical cases
CRITICAL_CASES_FILE = Path(__file__).parent.parent.parent / "data" / "red_list" / "critical_cases.json"

with open(CRITICAL_CASES_FILE, 'r') as f:
    CRITICAL_CASES = json.load(f)

print(f"\n✅ Loaded {len(CRITICAL_CASES)} Red List cases from {CRITICAL_CASES_FILE}")


# =============================================================================
# PARAMETRIZED TESTS (270 tests - one per case)
# =============================================================================

@pytest.mark.parametrize("case", CRITICAL_CASES)
def test_red_list_fn_zero(case):
    """
    Test FN=0 for critical syndromes (MANDATORY)

    This is the REGULATORY GATE:
    - FN=0 is NON-NEGOTIABLE
    - If ANY case fails, Sprint 4 FAILS
    - Tuning sprint (+1 week) required if FN > 0
    """
    case_id = case["case_id"]
    expected = case["expected_syndrome"]

    # Prepare CBC data
    cbc_data = {k: v for k, v in case.items() if k not in [
        "case_id", "expected_syndrome", "expected_evidences",
        "expected_next_steps", "criticality", "fn_allowed", "notes"
    ]}

    # Run pipeline
    result = analyze_cbc(cbc_data)

    # CRITICAL ASSERTION: FN=0 MANDATORY
    assert expected in result["top_syndromes"], \
        f"❌ FN DETECTED! Case {case_id}: Expected {expected}, got {result['top_syndromes']}\n" \
        f"   CBC: WBC={case.get('wbc')}, ANC={case.get('anc')}, Hb={case.get('hb')}, PLT={case.get('plt')}\n" \
        f"   Notes: {case.get('notes')}\n" \
        f"   THIS IS A REGULATORY BLOCKER - HALT SPRINT 4!"

    # Critical syndrome MUST be prioritized (first in list)
    assert result["top_syndromes"][0] == expected, \
        f"⚠️ Critical not prioritized: {result['top_syndromes']} (expected {expected} first)\n" \
        f"   Case {case_id}\n" \
        f"   This may indicate incorrect precedence in 06_route_policy_hybrid.yaml"


# =============================================================================
# METRICS COMPUTATION TEST
# =============================================================================

def test_compute_red_list_metrics():
    """
    Compute FN/FP/TP/TN for all 8 critical syndromes (v2.5.0 - S-APL removed)

    Saves metrics to: results/red_list_metrics.json

    GATE CRITERIA:
    - FN = 0 for ALL 8 syndromes
    - Sensitivity = 100% for ALL 8 syndromes
    - Specificity ≥ 80% overall
    """
    results = []

    # Run all 240 cases (8 syndromes × 30 cases)
    for case in CRITICAL_CASES:
        case_id = case["case_id"]
        expected = case["expected_syndrome"]

        # Prepare CBC data
        cbc_data = {k: v for k, v in case.items() if k not in [
            "case_id", "expected_syndrome", "expected_evidences",
            "expected_next_steps", "criticality", "fn_allowed", "notes"
        ]}

        # Run pipeline
        result = analyze_cbc(cbc_data)

        # Solution 2: Multiple critical syndromes supported
        # Check if expected syndrome is IN top_syndromes (not just position [0])
        top_syndromes = result["top_syndromes"]
        predicted = expected if expected in top_syndromes else (top_syndromes[0] if top_syndromes else None)

        results.append({
            "case_id": case_id,
            "expected": expected,
            "predicted": predicted,
            "all_syndromes": result["top_syndromes"],
            "notes": case.get("notes", "")
        })

    # Compute per-syndrome metrics (8 critical syndromes - S-APL removed in v2.5.0)
    syndrome_list = [
        "S-NEUTROPENIA-GRAVE",
        "S-BLASTIC-SYNDROME",
        "S-TMA",
        "S-PLT-CRITICA",
        "S-ANEMIA-GRAVE",
        "S-NEUTROFILIA-LEFTSHIFT-CRIT",
        "S-THROMBOCITOSE-CRIT",
        "S-CIVD"
        # S-APL removed (not implemented in YAMLs - approved by Dr. Abel)
    ]

    metrics = {}
    for syndrome in syndrome_list:
        tp = sum(1 for r in results if r["expected"] == syndrome and r["predicted"] == syndrome)
        fn = sum(1 for r in results if r["expected"] == syndrome and r["predicted"] != syndrome)
        fp = sum(1 for r in results if r["expected"] != syndrome and r["predicted"] == syndrome)
        tn = sum(1 for r in results if r["expected"] != syndrome and r["predicted"] != syndrome)

        total_positive = tp + fn
        total_negative = fp + tn

        sensitivity = tp / total_positive if total_positive > 0 else 0
        specificity = tn / total_negative if total_negative > 0 else 0
        ppv = tp / (tp + fp) if (tp + fp) > 0 else 0
        npv = tn / (tn + fn) if (tn + fn) > 0 else 0

        metrics[syndrome] = {
            "tp": tp,
            "fn": fn,
            "fp": fp,
            "tn": tn,
            "sensitivity": round(sensitivity, 4),
            "specificity": round(specificity, 4),
            "ppv": round(ppv, 4),
            "npv": round(npv, 4),
            "total_cases": total_positive
        }

    # Save metrics to JSON
    results_dir = Path(__file__).parent.parent.parent / "results"
    results_dir.mkdir(exist_ok=True)

    metrics_file = results_dir / "red_list_metrics.json"
    with open(metrics_file, 'w') as f:
        json.dump(metrics, f, indent=2)

    print(f"\n✅ Metrics saved to {metrics_file}")

    # Print summary
    print("\n" + "="*80)
    print("RED LIST VALIDATION METRICS (SPRINT 4)")
    print("="*80)
    print(f"{'Syndrome':<35} {'TP':>4} {'FN':>4} {'FP':>4} {'Sens':>6} {'Spec':>6} {'Status':>10}")
    print("-"*80)

    all_fn_zero = True
    all_sens_100 = True

    for syndrome, m in metrics.items():
        status = "✅ PASS" if m["fn"] == 0 else "❌ FAIL"
        if m["fn"] > 0:
            all_fn_zero = False
        if m["sensitivity"] < 1.0:
            all_sens_100 = False

        print(f"{syndrome:<35} {m['tp']:>4} {m['fn']:>4} {m['fp']:>4} "
              f"{m['sensitivity']:>6.1%} {m['specificity']:>6.1%} {status:>10}")

    print("-"*80)

    # Overall metrics
    total_tp = sum(m["tp"] for m in metrics.values())
    total_fn = sum(m["fn"] for m in metrics.values())
    total_fp = sum(m["fp"] for m in metrics.values())

    overall_sensitivity = total_tp / (total_tp + total_fn) if (total_tp + total_fn) > 0 else 0
    overall_specificity = sum(m["specificity"] for m in metrics.values()) / len(metrics)

    print(f"{'OVERALL':<35} {total_tp:>4} {total_fn:>4} {total_fp:>4} "
          f"{overall_sensitivity:>6.1%} {overall_specificity:>6.1%}")
    print("="*80)

    # CRITICAL ASSERTIONS: FN=0 GATE
    for syndrome, m in metrics.items():
        assert m["fn"] == 0, \
            f"\n❌ GATE FAILED: FN > 0 for {syndrome}\n" \
            f"   False Negatives: {m['fn']}\n" \
            f"   Sensitivity: {m['sensitivity']:.1%}\n" \
            f"   Total cases: {m['total_cases']}\n\n" \
            f"   🚨 THIS IS A REGULATORY BLOCKER!\n" \
            f"   Action required:\n" \
            f"   1. HALT Sprint 4 execution\n" \
            f"   2. Root cause analysis (which evidence/syndrome failed?)\n" \
            f"   3. Tuning sprint (+1 week)\n" \
            f"   4. Re-run validation\n" \
            f"   5. Verify FN=0 before proceeding\n"

        assert m["sensitivity"] == 1.0, \
            f"\n❌ GATE FAILED: Sensitivity < 100% for {syndrome}\n" \
            f"   Sensitivity: {m['sensitivity']:.1%}\n" \
            f"   Expected: 100%\n"

    # Secondary metric: Specificity ≥ 80%
    assert overall_specificity >= 0.80, \
        f"⚠️ Overall specificity < 80%: {overall_specificity:.1%}"

    # Success message
    print("\n" + "="*80)
    print("🎉 FN=0 GATE PASSED FOR ALL CRITICAL SYNDROMES!")
    print("="*80)
    print(f"   Total cases: {len(results)}")
    print(f"   Syndromes: {len(syndrome_list)}")
    print(f"   FN total: {total_fn} (ZERO ✅)")
    print(f"   Sensitivity: {overall_sensitivity:.1%} (100% ✅)")
    print(f"   Specificity: {overall_specificity:.1%} ({'>= 80%' if overall_specificity >= 0.80 else '< 80%'})")
    print("="*80)
    print("\n✅ APPROVED FOR ANVISA SUBMISSION (30 Nov 2025)")
    print("="*80 + "\n")

    return metrics


# =============================================================================
# EVIDENCE VALIDATION (OPTIONAL)
# =============================================================================

@pytest.mark.parametrize("case", CRITICAL_CASES[:10])  # Sample 10 cases
def test_expected_evidences_present(case):
    """
    Verify expected evidences are detected

    This is NOT part of the FN=0 gate, but helps validate
    that the evidence engine is working correctly.
    """
    expected_evidences = case.get("expected_evidences", [])
    if not expected_evidences:
        pytest.skip("No expected evidences defined")

    # Prepare CBC data
    cbc_data = {k: v for k, v in case.items() if k not in [
        "case_id", "expected_syndrome", "expected_evidences",
        "expected_next_steps", "criticality", "fn_allowed", "notes"
    ]}

    # Run pipeline
    result = analyze_cbc(cbc_data)

    # Check evidences
    detected_evidences = [e["id"] for e in result.get("evidences", [])]

    for expected_ev in expected_evidences:
        assert expected_ev in detected_evidences, \
            f"Expected evidence {expected_ev} not detected in case {case['case_id']}\n" \
            f"   Detected: {detected_evidences}"


# =============================================================================
# NEXT STEPS VALIDATION (OPTIONAL)
# =============================================================================

@pytest.mark.parametrize("case", CRITICAL_CASES[:10])  # Sample 10 cases
def test_critical_next_steps_present(case):
    """
    Verify critical next steps are recommended

    This validates that the next_steps engine is providing
    appropriate clinical guidance for critical cases.
    """
    # Prepare CBC data
    cbc_data = {k: v for k, v in case.items() if k not in [
        "case_id", "expected_syndrome", "expected_evidences",
        "expected_next_steps", "criticality", "fn_allowed", "notes"
    ]}

    # Run pipeline
    result = analyze_cbc(cbc_data)

    # Check that next steps are present
    next_steps = result.get("next_steps", [])

    assert len(next_steps) > 0, \
        f"No next steps provided for critical case {case['case_id']}\n" \
        f"   Syndrome: {case['expected_syndrome']}\n" \
        f"   Critical cases MUST have next steps!"

    # Check that at least one next step is "urgent" level
    urgent_steps = [step for step in next_steps if step.get("level") == "urgent"]

    assert len(urgent_steps) > 0, \
        f"No URGENT next steps for critical case {case['case_id']}\n" \
        f"   Syndrome: {case['expected_syndrome']}\n" \
        f"   Critical syndromes require urgent recommendations!"
