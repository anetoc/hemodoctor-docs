#!/bin/bash
################################################################################
# HemoDoctor Repository Reorganization Script v2.0
# Date: 2025-10-11
# Purpose: Reorganize documentation repository for clarity and maintainability
# Author: Repository Organization Specialist (Claude Code Agent)
#
# IMPORTANT: Creates full backup before making any changes
# Rollback: Restore from docs_backup_20251011_pre_reorg.tar.gz
################################################################################

set -euo pipefail  # Exit on error, undefined variables, pipe failures

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
BASE_DIR="/Users/abelcosta/Documents/HemoDoctor/docs"
BACKUP_DIR="/Users/abelcosta/Documents/HemoDoctor"
BACKUP_NAME="docs_backup_20251011_pre_reorg.tar.gz"
DRY_RUN=false
VERBOSE=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        -v|--verbose)
            VERBOSE=true
            shift
            ;;
        -h|--help)
            echo "Usage: $0 [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  --dry-run    Show what would be done without making changes"
            echo "  -v, --verbose Enable verbose output"
            echo "  -h, --help    Show this help message"
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Logging functions
log_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

log_success() {
    echo -e "${GREEN}✓${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

log_step() {
    echo -e "\n${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}  $1${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

# Execute command (respects dry-run mode)
execute() {
    local cmd="$1"
    local description="$2"

    if [ "$VERBOSE" = true ]; then
        log_info "$description"
        log_info "Command: $cmd"
    fi

    if [ "$DRY_RUN" = true ]; then
        echo "[DRY-RUN] $cmd"
    else
        eval "$cmd"
        if [ $? -eq 0 ]; then
            [ "$VERBOSE" = true ] && log_success "$description"
        else
            log_error "Failed: $description"
            exit 1
        fi
    fi
}

# Main script
main() {
    log_step "🚀 HemoDoctor Repository Reorganization v2.0"

    if [ "$DRY_RUN" = true ]; then
        log_warning "DRY-RUN MODE: No changes will be made"
    fi

    # Verify we're in the correct directory
    if [ ! -d "$BASE_DIR" ]; then
        log_error "Directory not found: $BASE_DIR"
        exit 1
    fi

    cd "$BASE_DIR"
    log_info "Working directory: $(pwd)"

    # ========================================================================
    # STEP 1: BACKUP
    # ========================================================================
    log_step "📦 Step 1: Creating Full Backup"

    if [ "$DRY_RUN" = false ]; then
        log_info "Creating backup at: $BACKUP_DIR/$BACKUP_NAME"
        log_info "This may take a few minutes for 440 MB..."

        cd "$BACKUP_DIR"
        tar -czf "$BACKUP_NAME" docs/ 2>/dev/null || {
            log_error "Backup failed!"
            exit 1
        }

        # Verify backup
        if [ -f "$BACKUP_NAME" ]; then
            backup_size=$(du -h "$BACKUP_NAME" | cut -f1)
            log_success "Backup created: $BACKUP_NAME ($backup_size)"
        else
            log_error "Backup file not created!"
            exit 1
        fi

        cd "$BASE_DIR"
    else
        echo "[DRY-RUN] Would create: $BACKUP_DIR/$BACKUP_NAME"
    fi

    # ========================================================================
    # STEP 2: CREATE NEW DIRECTORY STRUCTURE
    # ========================================================================
    log_step "📁 Step 2: Creating New Directory Structure"

    execute "mkdir -p 01_REFERENCE" "Create 01_REFERENCE/"
    execute "mkdir -p 02_AGENTS/reports" "Create 02_AGENTS/reports/"
    execute "mkdir -p 02_AGENTS/ceo-consultant" "Create 02_AGENTS/ceo-consultant/"
    execute "mkdir -p 03_SCRIPTS/migration" "Create 03_SCRIPTS/migration/"
    execute "mkdir -p 03_SCRIPTS/validation" "Create 03_SCRIPTS/validation/"
    execute "mkdir -p 03_SCRIPTS/analysis" "Create 03_SCRIPTS/analysis/"
    execute "mkdir -p 04_ARCHIVE" "Create 04_ARCHIVE/"
    execute "mkdir -p 99_TEMP/downloads" "Create 99_TEMP/downloads/"
    execute "mkdir -p 99_TEMP/scratch" "Create 99_TEMP/scratch/"

    log_success "New directory structure created"

    # ========================================================================
    # STEP 3: RENAME CONSOLIDADO → 00_WORKING
    # ========================================================================
    log_step "🔄 Step 3: Rename CONSOLIDADO → 00_WORKING"

    if [ -d "HEMODOCTOR_CONSOLIDADO_v2.0_20251010" ]; then
        execute "mv 'HEMODOCTOR_CONSOLIDADO_v2.0_20251010' '00_WORKING'" \
                "Rename HEMODOCTOR_CONSOLIDADO_v2.0_20251010 → 00_WORKING"
        log_success "CONSOLIDADO renamed to 00_WORKING"
    else
        log_warning "HEMODOCTOR_CONSOLIDADO_v2.0_20251010 not found (may already be renamed)"
    fi

    # ========================================================================
    # STEP 4: CREATE SESSION_SUMMARIES SUBFOLDER
    # ========================================================================
    log_step "📂 Step 4: Create SESSION_SUMMARIES Subfolder"

    execute "mkdir -p 00_WORKING/06_SESSION_SUMMARIES" \
            "Create 00_WORKING/06_SESSION_SUMMARIES/"

    # ========================================================================
    # STEP 5: MOVE REFERENCE MATERIALS
    # ========================================================================
    log_step "📚 Step 5: Move Reference Materials"

    if [ -d "AUTHORITATIVE_BASELINE" ]; then
        execute "mv 'AUTHORITATIVE_BASELINE' '01_REFERENCE/'" \
                "Move AUTHORITATIVE_BASELINE → 01_REFERENCE/"
    fi

    if [ -f "AUTHORITATIVE_BASELINE.md" ]; then
        execute "mv 'AUTHORITATIVE_BASELINE.md' '01_REFERENCE/AUTHORITATIVE_BASELINE/README_BASELINE.md'" \
                "Move AUTHORITATIVE_BASELINE.md → README_BASELINE.md"
    fi

    if [ -d "HEMODOCTOR_REFERENCIAS" ]; then
        execute "mv 'HEMODOCTOR_REFERENCIAS' '01_REFERENCE/'" \
                "Move HEMODOCTOR_REFERENCIAS → 01_REFERENCE/"
    fi

    if [ -d "BMAD-METHOD" ]; then
        log_warning "BMAD-METHOD (165 MB) - Choose action:"
        log_warning "  1. Move to 01_REFERENCE/ (default)"
        log_warning "  2. Create symlink (manual intervention needed)"
        execute "mv 'BMAD-METHOD' '01_REFERENCE/'" \
                "Move BMAD-METHOD → 01_REFERENCE/"
    fi

    log_success "Reference materials organized"

    # ========================================================================
    # STEP 6: MOVE AGENT SYSTEM FILES
    # ========================================================================
    log_step "🤖 Step 6: Move Agent System Files"

    # Main agent directory
    if [ -d "HEMODOCTOR_AGENTES" ]; then
        execute "mv 'HEMODOCTOR_AGENTES' '02_AGENTS/'" \
                "Move HEMODOCTOR_AGENTES → 02_AGENTS/"
    fi

    # Agent dashboard and JSON
    [ -f "DASHBOARD_AGENTES_HEMODOCTOR.html" ] && \
        execute "mv 'DASHBOARD_AGENTES_HEMODOCTOR.html' '02_AGENTS/'" \
                "Move DASHBOARD_AGENTES_HEMODOCTOR.html"

    [ -f "RELATORIO_ANALISE_AGENTES_HEMODOCTOR.json" ] && \
        execute "mv 'RELATORIO_ANALISE_AGENTES_HEMODOCTOR.json' '02_AGENTS/'" \
                "Move RELATORIO_ANALISE_AGENTES_HEMODOCTOR.json"

    # Agent reports
    for file in RELATORIO_*AGENTES*.md RELATORIO_AUDITORIA*.md RELATORIO_FINAL_AGENT*.md \
                RELATORIO_2_AGENTES*.md RELATORIO_FINAL_INTEGRACAO*.md \
                RELATORIO_IMPLEMENTACAO_OPCOES*.md RELATORIO_ORGANIZACAO*.md; do
        if [ -f "$file" ]; then
            execute "mv '$file' '02_AGENTS/reports/'" "Move $file"
        fi
    done

    # CEO consultant files
    for file in ceo-consultant-agent-spec.md CEO_CONSULTANT_*.md INDEX_CEO_CONSULTANT*.md \
                QUICK_START_CEO_CONSULTANT.md README_CEO_CONSULTANT.md install-ceo-consultant.sh; do
        if [ -f "$file" ]; then
            execute "mv '$file' '02_AGENTS/ceo-consultant/'" "Move $file"
        fi
    done

    log_success "Agent system files organized"

    # ========================================================================
    # STEP 7: MOVE SCRIPTS
    # ========================================================================
    log_step "⚙️ Step 7: Move Scripts"

    # Migration scripts
    [ -f "migrate_p0_files.sh" ] && \
        execute "mv 'migrate_p0_files.sh' '03_SCRIPTS/migration/'" \
                "Move migrate_p0_files.sh"

    [ -f "migrate_p1_files.sh" ] && \
        execute "mv 'migrate_p1_files.sh' '03_SCRIPTS/migration/'" \
                "Move migrate_p1_files.sh"

    # Validation scripts
    [ -f "validate_p0.sh" ] && \
        execute "mv 'validate_p0.sh' '03_SCRIPTS/validation/'" \
                "Move validate_p0.sh"

    [ -f "validate_p1.sh" ] && \
        execute "mv 'validate_p1.sh' '03_SCRIPTS/validation/'" \
                "Move validate_p1.sh"

    # Analysis scripts
    for file in analyze_*.js compare_*.py; do
        if [ -f "$file" ]; then
            execute "mv '$file' '03_SCRIPTS/analysis/'" "Move $file"
        fi
    done

    log_success "Scripts organized"

    # ========================================================================
    # STEP 8: MOVE SESSION SUMMARIES
    # ========================================================================
    log_step "📝 Step 8: Move Session Summaries"

    for file in REPOSITORY_ANALYSIS_SUMMARY*.md PLANO_CONSOLIDACAO*.md \
                INDEX_COMPARACAO*.md RESUMO_EXECUTIVO_COMPARACAO*.md \
                RELATORIO_COMPARACAO*.md ANALISE_CONHECIMENTO*.md \
                ANALISE_DUPLICACAO*.md MIGRATION_COMPARISON*.txt LEIAME_COMPARACAO*.txt; do
        if [ -f "$file" ]; then
            execute "mv '$file' '00_WORKING/06_SESSION_SUMMARIES/'" "Move $file"
        fi
    done

    # Move session summary from 00_WORKING root if exists
    if [ -f "00_WORKING/SESSION_SUMMARY_COMPLETE_20251011.md" ]; then
        execute "mv '00_WORKING/SESSION_SUMMARY_COMPLETE_20251011.md' '00_WORKING/06_SESSION_SUMMARIES/'" \
                "Move SESSION_SUMMARY_COMPLETE_20251011.md"
    fi

    log_success "Session summaries organized"

    # ========================================================================
    # STEP 9: CLEANUP WITHIN 00_WORKING
    # ========================================================================
    log_step "🧹 Step 9: Cleanup Within 00_WORKING"

    # Remove duplicate backlog
    if [ -f "00_WORKING/BACKLOG_UNIFICADO.md" ]; then
        execute "rm '00_WORKING/BACKLOG_UNIFICADO.md'" \
                "Delete duplicate BACKLOG_UNIFICADO.md"
    fi

    # Rename extended backlog
    if [ -f "00_WORKING/UNIFIED_BACKLOG_EXTENDED_v1.0.md" ]; then
        execute "mv '00_WORKING/UNIFIED_BACKLOG_EXTENDED_v1.0.md' '00_WORKING/BACKLOG_UNIFIED.md'" \
                "Rename UNIFIED_BACKLOG_EXTENDED_v1.0.md → BACKLOG_UNIFIED.md"
    fi

    log_success "00_WORKING cleaned up"

    # ========================================================================
    # STEP 10: DELETE REDUNDANT FILES
    # ========================================================================
    log_step "🗑️ Step 10: Delete Redundant Files"

    # Delete zip file (can regenerate)
    if [ -f "HEMODOCTOR_CONSOLIDADO_v2.0_20251010.zip" ]; then
        execute "rm 'HEMODOCTOR_CONSOLIDADO_v2.0_20251010.zip'" \
                "Delete HEMODOCTOR_CONSOLIDADO_v2.0_20251010.zip (49 MB)"
    fi

    # Delete .DS_Store files
    if [ "$DRY_RUN" = false ]; then
        log_info "Removing all .DS_Store files..."
        find . -name ".DS_Store" -delete 2>/dev/null || true
        log_success "Removed .DS_Store files"
    else
        echo "[DRY-RUN] Would delete all .DS_Store files"
    fi

    log_success "Redundant files deleted"

    # ========================================================================
    # STEP 11: VALIDATION
    # ========================================================================
    log_step "✅ Step 11: Validation"

    if [ "$DRY_RUN" = false ]; then
        # Count files
        total_files=$(find . -type f 2>/dev/null | wc -l | tr -d ' ')
        log_info "Total files: $total_files (expected: ~23,480)"

        # Check directory structure
        log_info "Verifying new structure..."
        for dir in "00_WORKING" "01_REFERENCE" "02_AGENTS" "03_SCRIPTS" "04_ARCHIVE" "99_TEMP"; do
            if [ -d "$dir" ]; then
                log_success "$dir/ exists"
            else
                log_error "$dir/ NOT FOUND!"
            fi
        done

        # Check critical paths
        log_info "Checking critical paths..."
        [ -d "00_WORKING/01_SUBMISSAO_CEP" ] && log_success "CEP docs accessible"
        [ -d "00_WORKING/02_SUBMISSAO_ANVISA" ] && log_success "ANVISA docs accessible"
        [ -d "02_AGENTS/reports" ] && log_success "Agent reports accessible"
        [ -d "03_SCRIPTS/migration" ] && log_success "Scripts accessible"

        # Repository size
        repo_size=$(du -sh . 2>/dev/null | cut -f1)
        log_info "Repository size: $repo_size (expected: ~391 MB)"
    else
        echo "[DRY-RUN] Would validate file counts and structure"
    fi

    log_success "Validation complete"

    # ========================================================================
    # STEP 12: SUMMARY
    # ========================================================================
    log_step "📊 Summary"

    if [ "$DRY_RUN" = false ]; then
        log_success "✨ Repository reorganization complete!"
        echo ""
        log_info "New structure:"
        echo ""
        tree -L 1 -d 2>/dev/null || ls -la | grep "^d"
        echo ""
        log_info "Next steps:"
        echo "  1. Review new structure: ls -la"
        echo "  2. Test critical paths (CEP, ANVISA, agents)"
        echo "  3. Update CLAUDE.md with new paths"
        echo "  4. Create README.md files"
        echo ""
        log_info "Backup location: $BACKUP_DIR/$BACKUP_NAME"
        echo ""
        log_warning "If problems occur, rollback with:"
        echo "  cd $BACKUP_DIR"
        echo "  rm -rf docs/"
        echo "  tar -xzf $BACKUP_NAME"
    else
        log_info "Dry-run complete. Review planned changes above."
        log_info "To execute, run without --dry-run flag."
    fi
}

# Run main function
main "$@"

# Exit successfully
exit 0
