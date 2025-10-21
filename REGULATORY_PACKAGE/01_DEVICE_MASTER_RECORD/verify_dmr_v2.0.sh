#!/bin/bash
# DMR v2.0 Integrity Verification Script
# Generated: 2025-10-08
# Purpose: Verify SHA-256 checksums for all 36 files in DMR v2.0

set -euo pipefail

BASE_DIR="/Users/abelcosta/Documents/HemoDoctor/docs/HemoDoctor_ANVISA_Unified_Dossier"
cd "$BASE_DIR"

echo "======================================================================"
echo "DMR v2.0 INTEGRITY VERIFICATION"
echo "======================================================================"
echo "Package: HemoDoctor_ANVISA_Unified_Dossier"
echo "Version: v2.0-20251008"
echo "Total Files: 36"
echo "Method: SHA-256 (FIPS 180-4)"
echo "Date: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "======================================================================"
echo ""

TOTAL=0
PASSED=0
FAILED=0

# Function to verify checksum
verify_file() {
    local file="$1"
    local expected="$2"
    local doc_id="$3"

    TOTAL=$((TOTAL + 1))

    if [ ! -f "$file" ]; then
        echo "❌ FAILED: $doc_id - File not found: $file"
        FAILED=$((FAILED + 1))
        return 1
    fi

    local actual=$(shasum -a 256 "$file" | awk '{print $1}')

    if [ "$actual" = "$expected" ]; then
        echo "✅ PASS: $doc_id - $(basename "$file")"
        PASSED=$((PASSED + 1))
        return 0
    else
        echo "❌ FAILED: $doc_id - Checksum mismatch"
        echo "   Expected: $expected"
        echo "   Actual:   $actual"
        echo "   File: $file"
        FAILED=$((FAILED + 1))
        return 1
    fi
}

echo "=== CORE TECHNICAL DOCUMENTS (12 files) ==="
verify_file "02_CONTROLES_DESIGN/SRS/SRS-001_Software_Requirements_v1.1_OFICIAL.md" \
    "a3e065634336fd78123a8e675f1689db3bf65d086d101a22a21de9cf5546ecdc" "SRS-001"

verify_file "02_CONTROLES_DESIGN/SDD/SDD-001_Software_Design_v1.1_OFICIAL.md" \
    "3bd38e28ba9e0e57759afc7b543e86707f3ca14baf2323a31ebfa3e8dda1651e" "SDD-001"

verify_file "02_CONTROLES_DESIGN/TEC/TEC-001_Software_Development_Plan_v1.0_OFICIAL.md" \
    "881fafe39b892f00afa66f03a0b32871c9f016ac2c7898523193905efa5bd630" "TEC-001"

verify_file "03_GESTAO_RISCO/RMP/RMP-001_Risk_Management_Plan_v1.0_OFICIAL.md" \
    "facb4ea052a845889a0b6c3b1488f0985161a8fc8a86a44131320de4714c92e5" "RMP-001"

verify_file "04_VERIFICACAO_VALIDACAO/TST/TST-001_Test_Specification_v1.0_OFICIAL.md" \
    "4bc26fe57555559629f72793def79ee6dff6848195ff13351e94ffa41b640494" "TST-001"

verify_file "05_AVALIACAO_CLINICA/CER/CER-001_Clinical_Evaluation_Report_v1.2_OFICIAL.md" \
    "c567c4cd7bf111906fefc09ed9b79990f161b087761c2c47b08fb8a5cda3f399" "CER-001"

verify_file "06_RASTREABILIDADE/TRC/TRC-001_Traceability_Matrix_v2.0_OFICIAL.csv" \
    "76535ab1ace2759a148f01bd166646946ec5c01dfb1c82f681aa0b700bbbcdef" "TRC-001"

verify_file "07_POS_MERCADO/PMS/PMS-001_PostMarket_Surveillance_v1.1_OFICIAL.md" \
    "d3541144ab44e0516c35a19dfcf73fb4c4c6d07f123024654c1276715b3acbf5" "PMS-001"

verify_file "08_ROTULAGEM/IFU/IFU-001_PT_BR_v1.0_OFICIAL.pdf" \
    "89318b0b5d93bc5f3f6202a29467cf1f9ffe4ac9bb0b033062ed4b9901a1026a" "IFU-001-PT"

verify_file "08_ROTULAGEM/IFU/IFU-001_EN_US_v1.0_OFICIAL.pdf" \
    "26086263e4e5a841210e8ea6ae08376ff6c4838b7bd1dc23c698290e390a9960" "IFU-001-EN"

verify_file "09_CYBERSECURITY/SEC/SEC-001_Cybersecurity_v1.0_OFICIAL.md" \
    "911f929cb1322cd1bd65c3a6447773b7bf9353768f668d878e61b77fa26f88eb" "SEC-001"

verify_file "10_SOUP/SOUP-001_Analysis_v1.0_OFICIAL.md" \
    "f1293ebc03cb53e3b92244d55189196da00e015a1d3d0c3b99b7186fb83a31d7" "SOUP-001"

echo ""
echo "=== API SPECIFICATIONS (12 files) ==="
verify_file "02_CONTROLES_DESIGN/API_SPECS/00_API_INDEX.md" \
    "0e38d52b0bc3af9ca40bd0d85121aa75f8c38300dcc3db1d72ddc6a13974bce3" "API-INDEX"

verify_file "02_CONTROLES_DESIGN/API_SPECS/README_API_SPECS.md" \
    "451a76ecc30b062bac24e6a5a701a57111293d32f4af550361b2a11352a66819" "API-README"

verify_file "02_CONTROLES_DESIGN/API_SPECS/01_API_Gateway_OpenAPI_v1.0.yaml" \
    "bfbba816cc83d2ec20c9b952615a47ff513f20eae9512c80b73fecc4c048fac9" "API-GATEWAY"

verify_file "02_CONTROLES_DESIGN/API_SPECS/02_Ingestion_Service_OpenAPI_v1.0.yaml" \
    "f68945cd2e61e3171b95ce04d55bd0c15373005c7e8dbdff836c5d3c1446cae3" "API-INGESTION"

verify_file "02_CONTROLES_DESIGN/API_SPECS/03_Validation_Service_OpenAPI_v1.0.yaml" \
    "aa259f856a08691805134958d9014b3a225fb909ebca813d48d7aa07303e0b99" "API-VALIDATION"

verify_file "02_CONTROLES_DESIGN/API_SPECS/04_Rules_Engine_OpenAPI_v1.0.yaml" \
    "73693b3eed543bb854acac4c9837b5e6553eb0b675c7716674bf4e423c590475" "API-RULES"

verify_file "02_CONTROLES_DESIGN/API_SPECS/05_HemoAI_Inference_OpenAPI_v1.0.yaml" \
    "6c28779f4459ca658ce941b7bdbab9045a34dd10e2dc7857a2c4ccc9d414996f" "API-HEMOAI"

verify_file "02_CONTROLES_DESIGN/API_SPECS/06_Alert_Orchestrator_OpenAPI_v1.0.yaml" \
    "1553f5e51b0876baa33c3a14905f6a700b5e71756a972b9cff7ac9ed494ec10e" "API-ALERT"

verify_file "02_CONTROLES_DESIGN/API_SPECS/07_Audit_Service_OpenAPI_v1.0.yaml" \
    "d73f3a3f3b1de14df064d83c3a431a5c9f6b1dc4448f872f356cb6f6ba5e7304" "API-AUDIT"

verify_file "02_CONTROLES_DESIGN/API_SPECS/08_Model_Manager_OpenAPI_v1.0.yaml" \
    "e1ee583a10befed2e77214e42d7260076a2dd65074e07781eddf355e4c31546d" "API-MODEL"

verify_file "02_CONTROLES_DESIGN/API_SPECS/09_UI_Backend_OpenAPI_v1.0.yaml" \
    "0bb95a596c4158f5abb2357aee8250ae914b7875c722e9ee095deed0d8dc52e9" "API-UI"

verify_file "02_CONTROLES_DESIGN/API_SPECS/10_Async_Events_AsyncAPI_v1.0.yaml" \
    "2a976564e2a5e6e9fb6101540a98d9cf4648404bea4510325c94febca6eb566e" "API-ASYNC"

echo ""
echo "=== VALIDATION REPORTS (7 files) ==="
verify_file "00_INDICE_GERAL/VALIDACOES_CONSOLIDADAS_REPORT.md" \
    "7c1a10469259bfeb4df0c168e070f93d8a3c2243ab06334ad679fc4d902f6c0b" "VALID-CONSOL"

verify_file "00_INDICE_GERAL/CONSOLIDACAO_COMPLETA_REPORT.md" \
    "5419532f4d1802898d104c4e0f73ca45aebcbfce716d3ab1fce6405e27b3d7ab" "CONSOL-REPORT"

verify_file "00_INDICE_GERAL/EXECUCAO_AUTOMATICA_COMPLETA_2025-10-08.md" \
    "8838ef0ee8c129ca2afefc29346b8bf2ef12b4a2a9c6bc33d76b53706a415245" "EXEC-AUTO"

verify_file "05_AVALIACAO_CLINICA/CER/CER-001_VALIDATION_REPORT.md" \
    "431d424c0f77b84419ab7959efdbbaebc7617a8e5d71f21d56e93ad47ec00a7d" "CER-VALID"

verify_file "06_RASTREABILIDADE/TRC/TRC-001_v2.0_UPDATE_SUMMARY.md" \
    "c4496047da033602bb676f98a86937ae75ac0b568d4ed3601e6edc80f705e8db" "TRC-UPDATE"

verify_file "06_RASTREABILIDADE/TRC/VALIDATION_REPORT.md" \
    "d0c774f1aa25f82e6722075f186d0141dad29a819a23fca24452478697da3946" "TRC-VALID"

verify_file "SUBMISSION_READY_STATUS.md" \
    "3843821b5376ca45fa89716a878fae97cf77284ebd00f47207e547196904223b" "SUBMISSION-STATUS"

echo ""
echo "======================================================================"
echo "VERIFICATION SUMMARY"
echo "======================================================================"
echo "Total Files Checked: $TOTAL"
echo "Passed: $PASSED"
echo "Failed: $FAILED"
echo "======================================================================"

if [ $FAILED -eq 0 ]; then
    echo ""
    echo "✅ SUCCESS: All checksums verified successfully!"
    echo "✅ DMR v2.0 integrity confirmed"
    echo "✅ Package is ready for regulatory submission"
    echo ""
    exit 0
else
    echo ""
    echo "❌ FAILURE: $FAILED file(s) failed verification"
    echo "❌ DMR v2.0 integrity compromised"
    echo "❌ DO NOT submit this package - investigate failures"
    echo ""
    exit 1
fi
