# PMS-001 — Plano de Pós-Mercado & Tecnovigilância (v1.1)
**Data:** 2025-09-18 00:19

[ANCHOR:PMS_PLAN]
## 1. Plano e Objetivos
Monitorar segurança, desempenho, calibração e equidade no mundo real. Integra o estudo ITS como PMCF.

[ANCHOR:PMS_SOURCES]
## 2. Fontes de Dados
Reclamações/incidentes, pesquisas, literatura, **reports_sap** (T2–T5/F1–F3), logs operacionais (06_ops.csv).

[ANCHOR:PMS_METRICS]
## 3. Métricas e Limiares
Sensibilidade, especificidade, **ECE/Brier**, AUC/AP; alarmes por subgrupo (site/sexo/idade/analisador) conforme limiar.

[ANCHOR:PMS_PMCF]
## 4. PMCF (RWE)
PROJ-001/002: Séries temporais interrompidas com o HemoDoctor no fluxo, desfecho primário: redução do TTD.

[ANCHOR:PMS_FAIRNESS]
## 5. Equidade
Auditoria contínua (T2 por subgrupo); CAPA caso Δmétrica exceda limiar.

[ANCHOR:PMS_PSUR]
## 6. PSUR
Relatório anual para Classe III: síntese de segurança/desempenho/ações corretivas.

[ANCHOR:PMS_CAPA]
## 7. CAPA
Fluxo de investigação, ação corretiva e verificação de eficácia vinculado à matriz de riscos.

[ANCHOR:PMS_TRACE]
## 8. Rastreabilidade
Âncoras para IFU (limitações/uso), SRS (NFR/FR), TEC-002 (riscos), REG-001 (pós-mercado), AUD-001 (matriz).
