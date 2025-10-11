# REORGANIZATION EXECUTION PLAN - HemoDoctor Repository v2.0
**Date:** 2025-10-11 16:30 BRT
**Version:** 1.0
**Status:** READY FOR EXECUTION
**Script:** `reorganize_repository_v2.0.sh`

---

## EXECUTIVE SUMMARY

This document provides step-by-step instructions for executing the HemoDoctor repository reorganization. The process is **safe, reversible, and validated** with full backup and rollback capability.

**Duration:** 1-2 hours
**Risk:** LOW (full backup, validation, rollback plan)
**Impact:** HIGH (permanent improvement to repository usability)

---

## PRE-EXECUTION CHECKLIST

### ✅ Documentation Review

- [ ] Read `REPOSITORY_ANALYSIS_DETAILED_20251011.md` (32 KB)
- [ ] Read `REPOSITORY_ORGANIZATION_PROPOSAL_20251011.md` (28 KB)
- [ ] Understand proposed structure
- [ ] Review migration mapping
- [ ] Understand rollback plan

### ✅ System Readiness

- [ ] Verify disk space: `df -h /Users/abelcosta/Documents/HemoDoctor/`
  - **Minimum required:** 500 MB free (440 MB existing + backup overhead)

- [ ] Verify no active processes using repository:
  ```bash
  lsof +D /Users/abelcosta/Documents/HemoDoctor/docs/ | grep -v "COMMAND"
  ```
  - **Expected:** No active processes (or only Finder/Spotlight)

- [ ] Close any open files in IDEs (VS Code, PyCharm, etc.)

- [ ] Current working directory backed up recently?
  - **Last backup:** Check `~/n8n_backups/` for recent backups

### ✅ Decision Points Resolved

- [ ] **BMAD-METHOD (165 MB):** Keep in-repo or symlink?
  - **Default:** Keep in-repo at `01_REFERENCE/BMAD-METHOD/`
  - **If changed:** Manually edit script line 215

- [ ] **Execution timing:** Proceed now or schedule?
  - **Recommended:** Now (end of workday, no active sessions)

- [ ] **Approval obtained:** Abel reviewed and approved proposal?
  - **Signature:** _______________________________

---

## EXECUTION PHASES

### PHASE 1: DRY-RUN VERIFICATION (10 minutes)

**Purpose:** Preview all planned changes without modifying files

#### 1.1 Navigate to Repository

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/
pwd
# Should output: /Users/abelcosta/Documents/HemoDoctor/docs
```

#### 1.2 Verify Script Exists and is Executable

```bash
ls -lh reorganize_repository_v2.0.sh
# Should show: -rwxr-xr-x ... reorganize_repository_v2.0.sh

# If not executable:
chmod +x reorganize_repository_v2.0.sh
```

#### 1.3 Run Dry-Run

```bash
./reorganize_repository_v2.0.sh --dry-run | tee dry_run_output_20251011.txt
```

**What to look for:**
- ✅ All planned moves listed
- ✅ No error messages
- ✅ Expected file counts match
- ✅ Backup would be created
- ✅ Directory structure would be created

**Review output:**
```bash
less dry_run_output_20251011.txt
# Press 'q' to quit
```

**Decision point:**
- If dry-run looks good → Proceed to Phase 2
- If errors/concerns → Stop and investigate

---

### PHASE 2: BACKUP CREATION (10 minutes)

**Purpose:** Create full backup before any changes

#### 2.1 Manual Backup Verification (Before Script)

```bash
cd /Users/abelcosta/Documents/HemoDoctor/

# Check available space
df -h .
# Need at least 450 MB free

# Check current docs size
du -sh docs/
# Should be ~440 MB
```

#### 2.2 Create Additional Safety Backup (Optional but Recommended)

```bash
# Create timestamped backup
timestamp=$(date +"%Y%m%d_%H%M%S")
tar -czf "docs_manual_backup_${timestamp}.tar.gz" docs/

# Verify backup created
ls -lh "docs_manual_backup_${timestamp}.tar.gz"
# Should show ~150-200 MB (compressed)
```

**Result:** Two backups will exist:
1. Manual backup: `docs_manual_backup_YYYYMMDD_HHMMSS.tar.gz`
2. Script backup: `docs_backup_20251011_pre_reorg.tar.gz` (created in Phase 3)

---

### PHASE 3: EXECUTE REORGANIZATION (30 minutes)

**Purpose:** Run reorganization script with full backup

#### 3.1 Final Verification

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/

# Verify we're in correct location
pwd

# Verify script exists
ls -lh reorganize_repository_v2.0.sh

# Verify no uncommitted work (if git repo)
git status 2>/dev/null || echo "Not a git repo"
```

#### 3.2 Execute Script (WITH BACKUP)

```bash
# Run with verbose output
./reorganize_repository_v2.0.sh -v | tee reorganization_output_20251011.txt
```

**Expected output flow:**
```
🚀 HemoDoctor Repository Reorganization v2.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📦 Step 1: Creating Full Backup
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ℹ Creating backup at: /Users/abelcosta/Documents/HemoDoctor/docs_backup_20251011_pre_reorg.tar.gz
ℹ This may take a few minutes for 440 MB...
✓ Backup created: docs_backup_20251011_pre_reorg.tar.gz (150M)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📁 Step 2: Creating New Directory Structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Create 01_REFERENCE/
✓ Create 02_AGENTS/reports/
✓ Create 02_AGENTS/ceo-consultant/
✓ Create 03_SCRIPTS/migration/
...

[... continues through all 12 steps ...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📊 Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Repository reorganization complete!
```

#### 3.3 Monitor Execution

**What to watch for:**
- ✅ Backup step completes first (should show backup size)
- ✅ No error messages (red ✗ symbols)
- ✅ Each step shows green checkmarks (✓)
- ✅ Validation step confirms file counts

**If errors occur:**
- Script will exit automatically
- See "EMERGENCY ROLLBACK" section below

#### 3.4 Review Output Log

```bash
# After completion, review full log
less reorganization_output_20251011.txt

# Search for errors
grep -i "error\|failed\|✗" reorganization_output_20251011.txt

# Expected: No results (or only "error handling" context)
```

---

### PHASE 4: VALIDATION (20 minutes)

**Purpose:** Verify reorganization completed successfully

#### 4.1 File Count Validation

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/

# Total files (should be ~23,480, may be less due to deleted .DS_Store)
find . -type f | wc -l
# Expected: 23,400-23,480

# Verify no files lost (compare to backup)
# Original count was 23,480, deleted .DS_Store (38) + zip (1) = ~23,441
```

#### 4.2 Structure Validation

```bash
# Check new structure exists
ls -la

# Expected output:
# drwxr-xr-x   7 abelcosta  staff   224 Oct 11 16:30 00_WORKING
# drwxr-xr-x   4 abelcosta  staff   128 Oct 11 16:30 01_REFERENCE
# drwxr-xr-x   5 abelcosta  staff   160 Oct 11 16:30 02_AGENTS
# drwxr-xr-x   4 abelcosta  staff   128 Oct 11 16:30 03_SCRIPTS
# drwxr-xr-x   2 abelcosta  staff    64 Oct 11 16:30 04_ARCHIVE
# drwxr-xr-x   4 abelcosta  staff   128 Oct 11 16:30 99_TEMP
# -rw-r--r--   1 abelcosta  staff  25KB Oct 11 16:30 CLAUDE.md

# Count root items (should be ~10)
ls -la | wc -l
# Expected: 10-13 (including hidden files like .DS_Store, .git)
```

#### 4.3 Critical Path Testing

**CEP Documents:**
```bash
ls 00_WORKING/01_SUBMISSAO_CEP/PROTOCOLO/
# Expected: PROJ-001, PROJ-002 files

ls 00_WORKING/01_SUBMISSAO_CEP/CONSENTIMENTO/
# Expected: OPT-OUT, TCLE files
```

**ANVISA Documents:**
```bash
ls 00_WORKING/02_SUBMISSAO_ANVISA/00_CORE_DOCUMENTS/ | head -10
# Expected: SRS-001, SDD-001, RMP-001, CER-001, etc.

ls 00_WORKING/02_SUBMISSAO_ANVISA/01_ANNEXOS/
# Expected: CER-001 annexes (B, D, E)
```

**Agent Reports:**
```bash
ls 02_AGENTS/reports/
# Expected: RELATORIO_*_AGENTES*.md files (7 files)

ls 02_AGENTS/HEMODOCTOR_AGENTES/
# Expected: 13 agent definition files
```

**Scripts:**
```bash
ls 03_SCRIPTS/migration/
# Expected: migrate_p0_files.sh, migrate_p1_files.sh

ls 03_SCRIPTS/validation/
# Expected: validate_p0.sh, validate_p1.sh

ls 03_SCRIPTS/analysis/
# Expected: analyze_*.js, compare_*.py
```

**Session Summaries:**
```bash
ls 00_WORKING/06_SESSION_SUMMARIES/
# Expected: 9+ session summary/report files
```

#### 4.4 Size Validation

```bash
# Repository size (should be ~391 MB, down from 440 MB)
du -sh .
# Expected: 380-400 MB (49 MB zip deleted)

# Breakdown by folder
du -sh */ | sort -hr
# Expected order: 01_REFERENCE (248 MB), 00_WORKING (140 MB), ...
```

#### 4.5 Content Spot Checks

**Verify key files still readable:**
```bash
# Check CLAUDE.md (should still have full content)
wc -l CLAUDE.md
# Expected: 700-800 lines

# Check SRS (should have full content)
wc -l 00_WORKING/02_SUBMISSAO_ANVISA/00_CORE_DOCUMENTS/SRS-001*.md
# Expected: 700+ lines

# Check backlog
wc -l 00_WORKING/BACKLOG_UNIFIED.md
# Expected: 1,500+ lines (85 KB file)
```

#### 4.6 Backup Verification

```bash
cd /Users/abelcosta/Documents/HemoDoctor/

# Verify backup exists
ls -lh docs_backup_20251011_pre_reorg.tar.gz
# Expected: ~150-200 MB (compressed from 440 MB)

# Test backup integrity
tar -tzf docs_backup_20251011_pre_reorg.tar.gz | head -20
# Expected: List of files from original structure
```

---

### PHASE 5: DOCUMENTATION UPDATE (30 minutes)

**Purpose:** Update paths in documentation

#### 5.1 Update CLAUDE.md

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/

# Create backup of current CLAUDE.md
cp CLAUDE.md CLAUDE.md.backup_pre_update

# Edit CLAUDE.md (use your preferred editor)
nano CLAUDE.md  # or: vim, code, etc.
```

**Changes to make in CLAUDE.md:**

1. **Update "REPOSITORY STRUCTURE" section:**
   - Replace `HEMODOCTOR_CONSOLIDADO_v2.0_20251010/` → `00_WORKING/`

2. **Update "QUICK REFERENCE" section:**
   ```markdown
   # OLD:
   /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/

   # NEW:
   /Users/abelcosta/Documents/HemoDoctor/docs/00_WORKING/
   ```

3. **Add reorganization note at top:**
   ```markdown
   ## 🎉 REPOSITORY REORGANIZED (2025-10-11)

   **New structure:** Numbered folders (00_WORKING, 01_REFERENCE, 02_AGENTS, etc.)
   **Old structure:** `HEMODOCTOR_CONSOLIDADO_v2.0_20251010/` → `00_WORKING/`
   **Backup:** `docs_backup_20251011_pre_reorg.tar.gz` (if rollback needed)

   See `README.md` for navigation guide.
   ```

4. **Update "COMMANDS" section:**
   ```bash
   # OLD:
   cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_CONSOLIDADO_v2.0_20251010

   # NEW:
   cd /Users/abelcosta/Documents/HemoDoctor/docs/00_WORKING
   ```

**Automated find/replace:**
```bash
# Preview changes
grep -n "HEMODOCTOR_CONSOLIDADO_v2.0_20251010" CLAUDE.md

# Replace (macOS sed)
sed -i '.backup' 's/HEMODOCTOR_CONSOLIDADO_v2.0_20251010/00_WORKING/g' CLAUDE.md

# Verify changes
diff CLAUDE.md.backup CLAUDE.md
```

#### 5.2 Create Root README.md

```bash
cat > README.md << 'EOF'
# HemoDoctor v3.x - SaMD Class III Documentation Repository

**Last Updated:** 2025-10-11 (Reorganized v2.0)
**Primary Directory:** `00_WORKING/`
**Total Size:** ~391 MB, 23,400+ files

---

## 🎯 QUICK START

**For new agents/team members:**
1. Read [`CLAUDE.md`](CLAUDE.md) (master context, 15 min)
2. Navigate to [`00_WORKING/`](00_WORKING/) (active work)
3. Check priorities in [`00_WORKING/BACKLOG_UNIFIED.md`](00_WORKING/BACKLOG_UNIFIED.md)

**For submissions:**
- **CEP (Ethics):** `00_WORKING/01_SUBMISSAO_CEP/`
- **ANVISA (Regulatory):** `00_WORKING/02_SUBMISSAO_ANVISA/`

---

## 📂 REPOSITORY STRUCTURE

```
/docs/
├── README.md                    ← You are here
├── CLAUDE.md                    ← Master context (START HERE)
├── .gitignore                   ← Git exclusions
│
├── 00_WORKING/                  ⭐ PRIMARY - Active work
│   ├── 00_GOVERNANCE/           Version control, policies
│   ├── 01_SUBMISSAO_CEP/        Ethics committee submission
│   ├── 02_SUBMISSAO_ANVISA/     Regulatory submission
│   ├── 03_DESENVOLVIMENTO/      Development (code, tests, specs)
│   ├── 04_ANALISES_ESTRATEGICAS/ Strategic planning
│   ├── 05_MASTER_DOCUMENTATION/ Master docs, context handoffs
│   ├── 06_SESSION_SUMMARIES/    Session reports
│   ├── BACKLOG_UNIFIED.md       Unified backlog (85 KB)
│   └── CHANGELOG_MASTER.md      Master changelog
│
├── 01_REFERENCE/                📚 REFERENCE - Source materials
│   ├── AUTHORITATIVE_BASELINE/  Official source documents (43 files)
│   ├── HEMODOCTOR_REFERENCIAS/  Clinical articles, presentations
│   └── BMAD-METHOD/             Methodology reference (165 MB)
│
├── 02_AGENTS/                   🤖 AGENTS - Agent ecosystem
│   ├── HEMODOCTOR_AGENTES/      13 agent definitions
│   ├── reports/                 Agent analysis reports (7 files)
│   ├── ceo-consultant/          CEO consultant agent (7 files)
│   ├── DASHBOARD_AGENTES_HEMODOCTOR.html
│   └── RELATORIO_ANALISE_AGENTES_HEMODOCTOR.json
│
├── 03_SCRIPTS/                  ⚙️ SCRIPTS - Automation
│   ├── migration/               Migration scripts (2 files)
│   ├── validation/              Validation scripts (2 files)
│   └── analysis/                Analysis scripts (4 files)
│
├── 04_ARCHIVE/                  📦 ARCHIVE - Legacy (empty)
│   └── README_ARCHIVE.md
│
└── 99_TEMP/                     🗑️ TEMP - Scratch space (git-ignored)
    ├── downloads/
    └── scratch/
```

---

## 🚀 COMMON OPERATIONS

### Navigate to Working Directory
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/00_WORKING
```

### Find CEP Documents
```bash
cd 00_WORKING/01_SUBMISSAO_CEP/
ls PROTOCOLO/           # Study protocols
ls CONSENTIMENTO/       # Consent forms
ls CRFs/                # Case report forms
```

### Find ANVISA Documents
```bash
cd 00_WORKING/02_SUBMISSAO_ANVISA/
ls 00_CORE_DOCUMENTS/   # SRS, SDD, RMP, CER, etc.
ls 01_ANNEXOS/          # CER annexes
```

### Run Scripts
```bash
cd 03_SCRIPTS/
bash migration/migrate_p0_files.sh
bash validation/validate_p0.sh
```

---

## 📊 REPOSITORY METRICS

| Metric | Value |
|--------|-------|
| **Total Size** | ~391 MB |
| **Total Files** | 23,400+ |
| **Root Items** | 10 (was 43 before reorg) |
| **Primary Work** | 00_WORKING/ (140 MB, 7,722 files) |
| **Reference** | 01_REFERENCE/ (248 MB, 15,664 files) |
| **Agents** | 02_AGENTS/ (1.7 MB, 65 files) |
| **Last Reorg** | 2025-10-11 v2.0 |

---

## 🔄 RECENT CHANGES

**2025-10-11 - Repository Reorganization v2.0:**
- Renamed `HEMODOCTOR_CONSOLIDADO_v2.0_20251010/` → `00_WORKING/`
- Organized 34 root files into logical categories
- Created numbered folder structure (00_, 01_, 02_, etc.)
- Removed redundant zip file (49 MB)
- 77% reduction in root complexity (43 → 10 items)

**2025-10-10 - Consolidation Complete:**
- Merged 6 legacy versions into single CONSOLIDADO directory
- P0/P1/P2 corrections (11/11 tasks complete)
- ANVISA package: 60% → 90% complete

---

## 📚 KEY DOCUMENTS

**Master Context:**
- [`CLAUDE.md`](CLAUDE.md) - Master context for agents (25 KB)

**Strategic:**
- [`00_WORKING/BACKLOG_UNIFIED.md`](00_WORKING/BACKLOG_UNIFIED.md) - Unified backlog (85 KB)
- [`00_WORKING/CHANGELOG_MASTER.md`](00_WORKING/CHANGELOG_MASTER.md) - Master changelog

**Technical:**
- [`00_WORKING/05_MASTER_DOCUMENTATION/MASTER_TECHNICAL_SPECIFICATIONS_v1.0.md`](00_WORKING/05_MASTER_DOCUMENTATION/MASTER_TECHNICAL_SPECIFICATIONS_v1.0.md)

**Analysis:**
- [`REPOSITORY_ANALYSIS_DETAILED_20251011.md`](00_WORKING/06_SESSION_SUMMARIES/REPOSITORY_ANALYSIS_DETAILED_20251011.md)
- [`REPOSITORY_ORGANIZATION_PROPOSAL_20251011.md`](00_WORKING/06_SESSION_SUMMARIES/REPOSITORY_ORGANIZATION_PROPOSAL_20251011.md)

---

## 🔒 BACKUP & ROLLBACK

**Backup location:** `/Users/abelcosta/Documents/HemoDoctor/docs_backup_20251011_pre_reorg.tar.gz`

**Rollback (if needed):**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/
rm -rf docs/
tar -xzf docs_backup_20251011_pre_reorg.tar.gz
```

**Time to rollback:** <5 minutes

---

## 👥 CONTACTS

**Project Lead:** Abel Costa
**Email:** abel.costa@hemodoctor.com.br

---

**Repository Version:** 2.0 (Reorganized 2025-10-11)
**Documentation:** Complete
**Status:** ✅ Operational
EOF

echo "✅ README.md created"
```

#### 5.3 Create Subdirectory READMEs

**Quick creation script:**
```bash
# Create README_WORKING.md
cat > 00_WORKING/README_WORKING.md << 'EOF'
# 00_WORKING - Primary Working Directory

**Purpose:** Active work for CEP, ANVISA, development, and strategic planning
**Size:** 140 MB, 7,722 files
**Status:** ✅ Operational

## Subdirectories

- **00_GOVERNANCE/** - Version control, policies (2 files)
- **01_SUBMISSAO_CEP/** - Ethics committee (31 files, 97% complete)
- **02_SUBMISSAO_ANVISA/** - Regulatory (107 files, 90% complete)
- **03_DESENVOLVIMENTO/** - Development (7,543 files)
- **04_ANALISES_ESTRATEGICAS/** - Strategic (18 files)
- **05_MASTER_DOCUMENTATION/** - Master docs (11 files)
- **06_SESSION_SUMMARIES/** - Session reports (9+ files)

## Root Files

- **BACKLOG_UNIFIED.md** - Unified backlog (85 KB, 1,500+ lines)
- **CHANGELOG_MASTER.md** - Master changelog

## Last Updated

2025-10-11
EOF

# Create README_REFERENCE.md
cat > 01_REFERENCE/README_REFERENCE.md << 'EOF'
# 01_REFERENCE - Reference Materials

**Purpose:** Source materials, articles, methodology
**Size:** 248 MB, 15,664 files

## Contents

- **AUTHORITATIVE_BASELINE/** - Official source documents (43 files, 1.3 MB)
- **HEMODOCTOR_REFERENCIAS/** - Clinical articles, presentations (7 files, 83 MB)
- **BMAD-METHOD/** - Methodology reference (15,587 files, 165 MB)

## Last Updated

2025-10-11
EOF

# Create README_AGENTS.md
cat > 02_AGENTS/README_AGENTS.md << 'EOF'
# 02_AGENTS - Agent Ecosystem

**Purpose:** Agent definitions, reports, dashboards
**Size:** 1.7 MB, 65 files

## Contents

- **HEMODOCTOR_AGENTES/** - 13 agent definitions (installed in ~/.claude/agents/)
- **reports/** - Agent analysis reports (7 files)
- **ceo-consultant/** - CEO consultant agent (7 files)
- **DASHBOARD_AGENTES_HEMODOCTOR.html** - Agent dashboard
- **RELATORIO_ANALISE_AGENTES_HEMODOCTOR.json** - Agent analysis data

## Agents

1. @anvisa-regulatory-specialist
2. @clinical-evidence-specialist
3. @software-architecture-specialist
4. @risk-management-specialist
5. @quality-systems-specialist
6. @traceability-specialist
7. @regulatory-review-specialist
8. @hematology-technical-specialist
9. @documentation-finalization-specialist
10. @external-regulatory-consultant
11. @biostatistics-specialist
12. @cep-protocol-specialist
13. @ceo-consultant

## Last Updated

2025-10-11
EOF

# Create README_SCRIPTS.md
cat > 03_SCRIPTS/README_SCRIPTS.md << 'EOF'
# 03_SCRIPTS - Automation Scripts

**Purpose:** Migration, validation, analysis scripts
**Size:** <1 MB, 9 files

## Contents

- **migration/** - migrate_p0_files.sh, migrate_p1_files.sh
- **validation/** - validate_p0.sh, validate_p1.sh
- **analysis/** - analyze_*.js, compare_*.py

## Usage

```bash
cd 03_SCRIPTS/

# Migration
bash migration/migrate_p0_files.sh

# Validation
bash validation/validate_p0.sh

# Analysis
node analysis/analyze_hemodoctor_agents.js
```

## Last Updated

2025-10-11
EOF

echo "✅ Subdirectory READMEs created"
```

---

### PHASE 6: FINAL VERIFICATION (10 minutes)

**Purpose:** End-to-end testing

#### 6.1 Agent Access Simulation

```bash
# Simulate new agent reading context
cd /Users/abelcosta/Documents/HemoDoctor/docs/

# Read CLAUDE.md (should reference new paths)
grep "00_WORKING" CLAUDE.md | head -5
# Expected: Should find references to 00_WORKING/

# Navigate per CLAUDE.md instructions
cd 00_WORKING/
ls -la
# Expected: Should see 01_SUBMISSAO_CEP/, 02_SUBMISSAO_ANVISA/, etc.
```

#### 6.2 Critical Workflow Testing

**CEP workflow:**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/

# Navigate to CEP
cd 00_WORKING/01_SUBMISSAO_CEP/

# Check protocol
ls PROTOCOLO/
cat PROTOCOLO/PROJ-001*.md | head -20
# Expected: Protocol content visible

# Check consent forms
ls CONSENTIMENTO/
# Expected: OPT-OUT, TCLE files visible
```

**ANVISA workflow:**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/

# Navigate to ANVISA
cd 00_WORKING/02_SUBMISSAO_ANVISA/

# Check core documents
ls 00_CORE_DOCUMENTS/ | grep SRS
# Expected: SRS-001 files

# Check annexes
ls 01_ANNEXOS/ | grep ANNEX
# Expected: CER-001 annexes
```

**Agent workflow:**
```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/

# Navigate to agents
cd 02_AGENTS/

# Check reports
ls reports/
# Expected: 7 report files

# Check dashboard
open DASHBOARD_AGENTES_HEMODOCTOR.html
# Expected: Dashboard opens in browser
```

#### 6.3 Final Checklist

**Verification checklist:**
- [ ] File count correct (~23,400 files)
- [ ] Repository size correct (~391 MB)
- [ ] Root has ≤10 items
- [ ] 00_WORKING/ accessible
- [ ] 01_REFERENCE/ accessible
- [ ] 02_AGENTS/ accessible
- [ ] 03_SCRIPTS/ accessible
- [ ] CLAUDE.md updated with new paths
- [ ] README.md created and accurate
- [ ] Subdirectory READMEs created
- [ ] CEP documents accessible
- [ ] ANVISA documents accessible
- [ ] Agent reports accessible
- [ ] Scripts executable
- [ ] Backup exists and valid

**If ALL checked:** ✅ Reorganization successful!

---

## EMERGENCY ROLLBACK

**If problems occur during execution:**

### Immediate Stop (During Script Execution)

```bash
# Press Ctrl+C to stop script immediately

cd /Users/abelcosta/Documents/HemoDoctor/

# Restore from backup
rm -rf docs/
tar -xzf docs_backup_20251011_pre_reorg.tar.gz

# Verify restoration
cd docs/
ls -la
# Should see original structure with HEMODOCTOR_CONSOLIDADO_v2.0_20251010/

# Count files (should be ~23,480)
find . -type f | wc -l
```

**Time:** <5 minutes

### Post-Execution Rollback (If Issues Found After Completion)

```bash
cd /Users/abelcosta/Documents/HemoDoctor/

# Optional: Save new structure for analysis
tar -czf docs_reorg_failed_20251011.tar.gz docs/

# Restore from backup
rm -rf docs/
tar -xzf docs_backup_20251011_pre_reorg.tar.gz

# Verify
cd docs/
ls -la
find . -type f | wc -l
```

**Time:** 5-10 minutes

---

## POST-EXECUTION ACTIONS

### Immediate (Within 24 hours)

1. **Update external documentation** (if any):
   - Wiki references to old paths
   - Notion pages with old structure
   - Team communication channels

2. **Test with real agent session:**
   ```bash
   # Start Claude Code
   # Test: "Navigate to CEP documents"
   # Expected: Agent finds 00_WORKING/01_SUBMISSAO_CEP/ quickly
   ```

3. **Create completion report:**
   ```bash
   cat > REORGANIZATION_COMPLETE_20251011.txt << EOF
   Reorganization completed successfully: $(date)

   Statistics:
   - Files before: 23,480
   - Files after: $(find . -type f | wc -l)
   - Size before: 440 MB
   - Size after: $(du -sh . | cut -f1)
   - Root items before: 43
   - Root items after: $(ls -la | wc -l)

   Backups:
   - Script backup: docs_backup_20251011_pre_reorg.tar.gz
   - Manual backup: docs_manual_backup_*.tar.gz

   Status: ✅ COMPLETE
   EOF
   ```

### Short-term (Within 1 week)

4. **Implement .gitignore:**
   ```bash
   cd /Users/abelcosta/Documents/HemoDoctor/docs/

   cat > .gitignore << 'EOF'
   # macOS
   .DS_Store

   # Temporary
   99_TEMP/
   *.tmp
   *.temp

   # Archives
   *.zip
   *.tar
   *.tar.gz
   *.tgz

   # IDE
   .vscode/
   .idea/
   EOF
   ```

5. **Initialize git (if not already):**
   ```bash
   cd /Users/abelcosta/Documents/HemoDoctor/docs/

   git init
   git add .
   git commit -m "Repository reorganization v2.0 - 2025-10-11

   - Renamed HEMODOCTOR_CONSOLIDADO_v2.0_20251010/ → 00_WORKING/
   - Organized 34 root files into logical categories
   - Created numbered folder structure
   - 77% reduction in root complexity (43 → 10 items)
   - Added navigation READMEs
   "

   git tag reorg-v2.0-20251011
   ```

6. **Archive old backups (after 7-day safety period):**
   ```bash
   # After 7 days, if no issues:
   cd /Users/abelcosta/Documents/HemoDoctor/

   # Move backups to archive location
   mkdir -p backups_archive/
   mv docs_backup_*.tar.gz backups_archive/
   mv docs_manual_backup_*.tar.gz backups_archive/

   # Optional: compress archive
   tar -czf backups_archive_20251011.tar.gz backups_archive/
   rm -rf backups_archive/
   ```

---

## TROUBLESHOOTING

### Issue: Script fails during backup

**Symptom:** Error creating `docs_backup_20251011_pre_reorg.tar.gz`

**Cause:** Insufficient disk space

**Solution:**
```bash
# Check available space
df -h /Users/abelcosta/Documents/HemoDoctor/

# Free up space (delete old backups, temp files, etc.)
# Then re-run script
```

---

### Issue: "Permission denied" errors

**Symptom:** Cannot move files

**Cause:** Insufficient permissions or files in use

**Solution:**
```bash
# Close all IDEs and Finder windows

# Check what's using the files
lsof +D /Users/abelcosta/Documents/HemoDoctor/docs/

# Kill processes if needed (carefully!)
# Then re-run script
```

---

### Issue: File count doesn't match

**Symptom:** Validation shows different file count

**Cause:** .DS_Store deletion or zip removal

**Expected behavior:**
- Original: 23,480 files
- After reorg: ~23,441 files (deleted 38 .DS_Store + 1 zip)

**Verification:**
```bash
# Count difference
# Original - New = Deleted files
# Should be ~39 files (38 .DS_Store + 1 zip)
```

---

### Issue: BMAD-METHOD not found

**Symptom:** Can't find BMAD-METHOD after reorg

**Cause:** Moved to 01_REFERENCE/

**Solution:**
```bash
# Check new location
ls 01_REFERENCE/BMAD-METHOD/

# If not found, check backup
tar -tzf /Users/abelcosta/Documents/HemoDoctor/docs_backup_20251011_pre_reorg.tar.gz | grep BMAD-METHOD
```

---

## SUCCESS CRITERIA CHECKLIST

**Technical success:**
- [ ] All files preserved (zero loss)
- [ ] Repository size ~391 MB
- [ ] Root has ≤10 items
- [ ] All critical paths functional
- [ ] No broken symlinks or references

**Usability success:**
- [ ] New agent can navigate quickly (<30 seconds)
- [ ] CEP docs accessible in <5 seconds
- [ ] ANVISA docs accessible in <5 seconds
- [ ] README.md provides clear entry point
- [ ] CLAUDE.md updated correctly

**Team success:**
- [ ] Zero confusion during first use
- [ ] Positive feedback on clarity
- [ ] Reduced onboarding time

---

## CONTACTS & SUPPORT

**Questions during execution:**
- **Technical:** Review detailed analysis and proposal
- **Decision points:** See Section 13 in proposal document
- **Emergency:** Use rollback procedure immediately

**Post-execution issues:**
- Document issue in `00_WORKING/06_SESSION_SUMMARIES/`
- Tag with date and symptom
- Refer to troubleshooting section

---

## DOCUMENT HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-10-11 16:30 | Initial execution plan |

---

**Document Metadata:**
- **Created:** 2025-10-11 16:30 BRT
- **Version:** 1.0
- **Format:** Markdown
- **Size:** ~15 KB
- **Status:** ✅ READY FOR EXECUTION

---

**END OF EXECUTION PLAN**
