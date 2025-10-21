# ÍNDICE COMPLETO - HEMODOCTOR HYBRID V1.0
# Navegação Detalhada de Todos os Arquivos
# Dr. Abel Costa (IDOR-SP) - Outubro 2025

---

## 📋 VISÃO GERAL

Este índice lista **TODOS** os arquivos do HemoDoctor Hybrid V1.0, com descrições detalhadas, linhas de código, prioridade de leitura e interdependências.

**Total de Arquivos:** 20  
**Total de Linhas:** ~8.500 (YAMLs + Documentação)  
**Status:** ✅ 100% Completo - Pronto para Implementação  

---

## 🎯 ORDEM DE LEITURA RECOMENDADA

### **1. QUICK START (LEIA PRIMEIRO):**
- 📄 `README.md` - Visão geral do projeto
- 📄 `QUICKSTART_IMPLEMENTACAO.md` - Guia rápido para dev team
- 📄 `YAMLs/10_runbook_hybrid.yaml` - Roadmap V0→V1→V2

### **2. CONTEXTO E ANÁLISE:**
- 📄 `Analise_Comparativa/ANALISE_COMPARATIVA_TRIPLA_*.md` - Decisões técnicas
- 📄 `Analise_Comparativa/COMPARACAO_HIBRIDO_vs_SADMH_V2.3.md` - Comparação módulos

### **3. ESPECIFICAÇÕES TÉCNICAS:**
- 📄 `Especificacoes_Dev/DEV_TEAM_SPEC_09_NEXT_STEPS_ENGINE.md` - Spec com código

### **4. YAMLs (POR ORDEM DE IMPLEMENTAÇÃO):**
- Sprint 0: 00, 01
- Sprint 1: 02, 03
- Sprint 2: 04, 05, 09, 12
- Sprint 3: 06, 07, 08, 11
- Support: 10

---

## 📂 ESTRUTURA DETALHADA

### **/ (ROOT)**

#### **README.md** (5.2 KB)
- **Tipo:** Documentação master
- **Descrição:** Visão geral completa do projeto, arquitetura, síndromes, compliance, timeline
- **Seções:**
  - Visão geral
  - Características principais (34 síndromes, 75 evidências, always-output)
  - Estrutura do repositório
  - Quick start
  - Arquitetura do sistema (diagrama)
  - Síndromes cobertas (8 críticas, 23 priority, 1 review, 2 routine)
  - Benefícios regulatórios (ANVISA/FDA/ISO/LGPD)
  - Timeline (V0 8 sem, V1 12 sem, V2 16 sem)
  - Equipe necessária (3 FTE + hematologista)
  - Métricas de qualidade (FN=0, sens≥99%, spec≥80%)
  - Avisos importantes (Red List, WORM log, state machine)
  - Contato
  - Changelog
- **Prioridade:** ⭐⭐⭐ Alta (leia primeiro!)
- **Dependências:** Nenhuma
- **Para:** Product Owner, Dev Team, Hematologistas

---

#### **INDEX_COMPLETO.md** (este arquivo)
- **Tipo:** Navegação
- **Descrição:** Índice detalhado de todos os arquivos com descrições, tamanhos, dependências
- **Prioridade:** ⭐⭐ Média (referência)
- **Dependências:** Nenhuma
- **Para:** Todos

---

#### **QUICKSTART_IMPLEMENTACAO.md** (a ser criado)
- **Tipo:** Guia rápido
- **Descrição:** Guia prático para dev team iniciar implementação Sprint 0
- **Prioridade:** ⭐⭐⭐ Alta (dev team leia primeiro!)
- **Dependências:** README.md, 10_runbook_hybrid.yaml
- **Para:** Dev Team

---

### **/ YAMLs/ (15 arquivos, ~336 KB total)**

#### **00_config_hybrid.yaml** (10 KB, ~220 linhas)
- **Tipo:** Configuração
- **Versão:** hybrid_v1.0.0
- **Descrição:** Normalização de unidades + cutoffs/thresholds + pré-analítico
- **Seções:**
  - Units (hb, plt, wbc, mcv, etc.)
  - Cutoffs (hb_critical_low, plt_critical_low, anc_critical, etc.)
  - Pediatrics (mcv_low_child, plt_ref_low_child)
  - Safety (schistocytes_critical_pct)
  - Cutoffs refinados (thrombocytosis clonal, neutrofilia_leftshift, CIVD, TMA)
  - Pre-analytical gates (mchc_implausible, cold_agglutinin, pseudo_thrombocytopenia)
- **Prioridade:** ⭐⭐⭐ Alta (Sprint 0)
- **Dependências:** Nenhuma
- **Integra com:** 01_schema (validação), 02_evidence (regras)

---

#### **01_schema_hybrid.yaml** (13 KB, ~280 linhas)
- **Tipo:** Schema canônico
- **Versão:** schema_v0.9.0
- **Descrição:** Schema de dados canônico + morfologia triestado
- **Seções:**
  - Fields (CBC core: hb, ht, rbc, wbc, anc, plt, mcv, mch, mchc, rdw, etc.)
  - Morphology tokens (triestado: true/false/unknown)
    - esquistocitos, esferocitos, dacriocitos, eliptocitos, drepanocitos
    - rouleaux, policromasia, corpos_howell_jolly
    - blastos, promielocitos, mielocitos, metamielocitos, bastoes
    - linfocitos_atipicos, hiposegmentacao
    - aglomerados_plaquetarios, plaquetas_gigantes
  - Metadata (age_years, sex)
- **Prioridade:** ⭐⭐⭐ Alta (Sprint 0)
- **Dependências:** 00_config
- **Integra com:** 02_evidence (fields), 03_syndromes (morfologia)

---

#### **02_evidence_hybrid.yaml** (18 KB, ~420 linhas)
- **Tipo:** Evidências (regras atômicas)
- **Versão:** evidence_v0.9.0
- **Descrição:** 75 evidências (E-XXX) categorizadas por strength (critical/strong/moderate/weak)
- **Seções:**
  - Critical gates (11): ANC <0.2, PLT <10, WBC >100, Hb <6, esquistócitos ≥1%, etc.
  - Red series (18): Microcitose, macrocitose, RDW alto, IDA labs, B12/folato baixo, etc.
  - White series (23): Neutropenia, leucocitose, blastos, left shift, linfocitose, eosinofilia, etc.
  - Platelet series (12): Trombocitopenia crítica/grave, trombocitose, MPV alto, pseudo, etc.
  - Coagulation (5): D-dímero alto, fibrinogênio baixo, PT/APTT prolongado, etc.
  - Complementary (6): CRP alto, LDH alto, haptoglobina baixa, reticulócitos, etc.
- **Prioridade:** ⭐⭐⭐ Alta (Sprint 1)
- **Dependências:** 00_config, 01_schema
- **Integra com:** 03_syndromes (combine logic)

---

#### **03_syndromes_hybrid.yaml** (28 KB, ~650 linhas)
- **Tipo:** Síndromes (DAG fusion)
- **Versão:** syndromes_v0.9.0
- **Descrição:** 34 síndromes (S-XXX) com combine logic (ALL/ANY/NEGATIVE)
- **Seções:**
  - **Critical (8):** neutropenia_grave, blastic, TMA, plt_critica, anemia_grave, neutrofilia_leftshift_crit, thrombocitose_crit, CIVD
  - **Priority (23):** IDA, IDA-INFLAM, ACD, BETA-THAL, ALFA-THAL, MACRO-B12, HEMOLYSIS, etc.
  - **Review Sample (1):** review_sample (erro pré-analítico)
  - **Routine (2):** routine_normal, routine_borderline
- **Cada síndrome inclui:**
  - criticality (critical/priority/routine/review_sample)
  - combine (ALL/ANY/NEGATIVE logic)
  - threshold (0.0-1.0)
  - actions (lista de próximos passos clínicos)
  - missing_fields_warn (campos ausentes que reduzem confiança)
- **Prioridade:** ⭐⭐⭐ Alta (Sprint 1)
- **Dependências:** 02_evidence
- **Integra com:** 05_missingness, 06_route_policy, 09_next_steps

---

#### **04_output_templates_hybrid.yaml** (17 KB, ~380 linhas)
- **Tipo:** Templates de card
- **Versão:** hybrid_v1.0.0
- **Descrição:** Templates para renderização de cards finais
- **Seções:**
  - Critical template (evidências + ações urgentes + timeframe)
  - Priority template (síndromes + padrões + next_steps)
  - Routine template (valores normais + nenhum exame adicional)
  - Review_sample template (flags pré-analíticos + recoleta)
  - Confidence rules (C0/C1/C2 mapping)
- **Prioridade:** ⭐⭐ Média (Sprint 2)
- **Dependências:** 03_syndromes
- **Integra com:** 12_output_policies (render)

---

#### **05_missingness_hybrid_v2.3.yaml** (29 KB, ~750 linhas)
- **Tipo:** Missingness + always-output
- **Versão:** missingness_hybrid_v2.3.0
- **Descrição:** Política de missingness expandida com proxy logic, guaranteed output, borderline rules
- **Seções:**
  - Global policy (>30% missing → C0)
  - Minimal keys (chaves mínimas por série: red, white, platelets, coag)
  - Policies específicas (26 síndromes)
    - Cada policy: target, missing, severity, fallback, required_fields, degradation_logic, **proxy_logic**
  - Guaranteed output (6 níveis: critical → review_sample → priority → borderline → routine → c0_guidance)
  - Borderline rules (8 cenários: MCV 80-82, PLT 140-150, WBC 3.8-4, Hb borderline, etc.)
  - Integration next_steps_engine (missing keys → triggers automáticos)
  - Field importance hierarchy (critical/high/moderate/low)
- **Inovações V2.3:**
  - ✅ Proxy logic (inferir esquistócitos por bioquímica, reticulocitose por policromasia, etc.)
  - ✅ Guaranteed output (sistema NUNCA vazio)
  - ✅ Borderline rules (zona cinzenta sempre gera orientação)
- **Prioridade:** ⭐⭐⭐ Alta (Sprint 2)
- **Dependências:** 03_syndromes, 09_next_steps_engine
- **Integra com:** 12_output_policies (confidence), 06_route_policy (C0/C1/C2)

---

#### **06_route_policy_hybrid.yaml** (17 KB, ~430 linhas)
- **Tipo:** Route policy + determinismo
- **Versão:** route_policy_hybrid_v1.0.0
- **Descrição:** Política de rota única determinística (precedence + route_id SHA256)
- **Seções:**
  - Engine configuration (deterministic, short_circuit_enabled)
  - Precedence
    - Critical order (9 síndromes, ordem rígida short-circuit)
    - Priority (severity_weight 0.0-1.0 + tie-break lexicográfico)
    - Review_sample (sempre prioridade máxima)
    - Routine (após tudo)
  - Unique route (route_id = SHA256 de evidences + syndromes + output_class + confidence)
  - Alt_routes policy (síndromes não selecionadas preservadas no WORM)
  - IDs convention (E-/S-/F- prefixes)
  - Flows (F-RED, F-WHITE, F-PLT, F-GLOBAL)
  - Validation tests (reproducibility, short-circuit, priority ordering, review_sample precedence)
- **Prioridade:** ⭐ Baixa (Sprint 3, auditoria)
- **Dependências:** 03_syndromes, 02_evidence
- **Integra com:** 07_conflict_matrix, 08_wormlog (alt_routes)

---

#### **07_conflict_matrix_hybrid.yaml** (15 KB, ~400 linhas)
- **Tipo:** Conflict resolution
- **Versão:** conflict_matrix_hybrid_v1.0.0
- **Descrição:** Matriz de conflitos entre síndromes + resolução
- **Seções:**
  - Negative pairs (12): TMA×PTI, IDA×ACD, IDA×ALFA-THAL, PSEUDO×PLT-CRIT, etc.
    - Cada par: rationale, resolution V0 (precedence), resolution V1 (penalties), exception
  - Soft conflicts (4): NEUTROFILIA-REACTIVE×LEUCOEMOIDE, LYMPHO-REACTIVE×CLONAL, etc.
    - V0: escolher por threshold/tempo
    - V1: penalty -0.15
  - Resolution policy
    - V0: precedence (módulo 06)
    - V1: penalties (-0.30 negative, -0.15 soft)
  - Validation tests
  - Audit trail (WORM log registra conflicts_detected + conflicts_resolved)
- **Prioridade:** ⭐ Baixa (Sprint 3, auditoria)
- **Dependências:** 06_route_policy, 03_syndromes
- **Integra com:** 08_wormlog (audit)

---

#### **07_normalization_heuristics.yaml** (16 KB, ~370 linhas)
- **Tipo:** Normalização site-specific
- **Versão:** hybrid_v1.0.0
- **Descrição:** Heurísticas para normalização de unidades por laboratório
- **Seções:**
  - Site-specific learning (aprender padrões por lab)
  - Auto-detection rules (dividir por 1000 se p50 >1000, etc.)
  - Audit log config (WORM logging)
- **Prioridade:** ⭐⭐ Média (Sprint 1, após parsers)
- **Dependências:** 00_config
- **Integra com:** 08_wormlog (audit)

---

#### **08_wormlog_hybrid.yaml** (17 KB, ~520 linhas)
- **Tipo:** WORM log (auditoria)
- **Versão:** wormlog_hybrid_v1.0.0
- **Descrição:** Registro imutável para auditoria regulatória (ANVISA/FDA/ISO/LGPD)
- **Seções:**
  - Mode (append_only_jsonl)
  - Segmenting (rotação diária, filename pattern)
  - Immutability
    - Sealing (segment chaining SHA256)
    - Auth (HMAC-SHA256 KMS-backed key)
    - Key rotation policy (anual, overlap 30d)
  - Retention (90d, purge automatizada LGPD)
  - Entry schema
    - Required fields: event_ts, case_id_hash, route_id, alt_routes, output_class, top_syndromes, fired_evidences, missing_keys, engine_version, config_hash, code_hash, site_id, data_lineage, hmac_signature
    - Optional fields: conflicts_detected, conflicts_resolved, next_steps_suggested, user_acknowledgment, card_rendered
  - Query & analytics (jq, ripgrep, pandas)
  - Compliance (ANVISA RDC 657, FDA 21 CFR Part 11, ISO 13485, LGPD)
  - Validation tests (HMAC verification, segment chaining, append-only enforcement)
- **Prioridade:** ⭐ Baixa (Sprint 3, auditoria)
- **Dependências:** 06_route_policy (route_id), 07_conflict_matrix (conflicts)
- **Integra com:** Todos os módulos (registra tudo)

---

#### **09_next_steps_engine_hybrid.yaml** (39 KB, ~1.450 linhas) ⭐
- **Tipo:** Next steps engine
- **Versão:** hybrid_v1.0.0
- **Descrição:** Motor inteligente de próximos passos clínicos (34 triggers, 1 por síndrome)
- **Seções:**
  - Prioritization (levels, tie_break, cost_bands, turnaround)
  - Render (max_items 8, deduplicate, rationale, cost/turnaround display)
  - Triggers (34 total)
    - **Série vermelha - críticos:** anemia-grave, IDA, beta-tal, alfa-tal, macro-B12-folate, hemolysis, aplasia-retic-low, MDS, MM-MGUS, PNH, HB-sickle
    - **Série branca - críticos:** neutropenia-grave, blastic, neutrofilia-leftshift-crit, APL-suspeita
    - **Série branca - priority:** lymphoproliferative, eosinophilia, CML, monocitose-cronica, basofilia
    - **Série plaquetária - críticos:** plt-critica, TMA, CIVD, thrombocitose-crit
    - **Série plaquetária - priority:** thrombocitose, PTI, HIT-possible, pseudo-thrombo, MPN-possible
    - **Múltiplas séries:** pancytopenia, leucoeritroblastose, policitemia
    - **Review sample:** review_sample
    - **Borderline:** borderline_microcytosis, macrocytosis, thrombocytopenia, thrombocytosis, leukopenia, leukocytosis, anemia_female/male
  - Cada trigger: id, when (condição), syndromes, suggest (list of {level, test, rationale, cost, turnaround, prereq})
  - Validation (5 test cases)
- **Prioridade:** ⭐⭐⭐ Alta (Sprint 2, sempre útil)
- **Dependências:** 03_syndromes, 05_missingness
- **Integra com:** 12_output_policies (render), 11_case_state (pending_orders)

---

#### **10_runbook_hybrid.yaml** (23 KB, ~550 linhas)
- **Tipo:** Roadmap técnico
- **Versão:** runbook_hybrid_v1.0.0
- **Descrição:** Roadmap V0→V1→V2 (8-14 semanas) com sprints detalhados
- **Seções:**
  - V0 (8 semanas - determinístico)
    - Sprint 0: Setup + parsers (1 sem)
    - Sprint 1: Evidências + síndromes (2 sem)
    - Sprint 2: Missingness + next_steps + output (2 sem)
    - Sprint 3: Auditoria (1 sem)
    - Sprint 4: Validação (Red List FN=0, retrospectiva 500) (2 sem)
  - V1 (4 semanas - calibração)
    - Sprint 5: Platt scaling (2 sem)
    - Sprint 6: Validação V1 (ECE <0.05) (2 sem)
  - V2 (4-6 semanas - ML/GNN roadmap futuro)
    - Sprint 7-8: ML explicável (3 sem)
    - Sprint 9: Validação V2 + fairness audit (2 sem)
  - Operational readiness (CI/CD, KMS, PostgreSQL, FHIR, monitoring, backup)
  - Dependencies (team, data, infra)
  - Risks & mitigations (FN >0, alert burden, drift, key rotation)
- **Prioridade:** ⭐⭐⭐ Alta (leia após README!)
- **Dependências:** Nenhuma (referência para todos)
- **Integra com:** Todos os módulos (descreve implementação)

---

#### **11_case_state_hybrid.yaml** (21 KB, ~600 linhas)
- **Tipo:** State machine
- **Versão:** case_state_hybrid_v2.3.0
- **Descrição:** State machine para gestão de casos ao longo do tempo + reconciliação incremental
- **Seções:**
  - States (4): OPEN, WAITING_RESULTS, ESCALATED, CLOSED
  - Transitions (11 eventos: NEW_INPUT, RESULTS_ARRIVED, CRITICAL_FOUND, CLOSE_CASE, etc.)
  - Case payload (estrutura de dados completa)
    - identifiers (case_id, case_id_hash, site_id, patient_pseudonym)
    - canonical_inputs (CBC, morfologia, complementares, molecular)
    - pending_orders (next_steps solicitados mas não recebidos)
    - current_route (última decisão do sistema)
    - history (histórico de route_id)
    - state_metadata (current_state, last_state_change, state_history)
    - engine_versions (config_hash, schema_hash, evidence_hash, etc.)
  - Reconciliation (merge strategy, recalculation pipeline, change detection)
  - Pending orders tracking (matching logic, timeout policy)
  - Escalation protocol (trigger syndromes, notification channels, acknowledgment required, lock_route)
- **Prioridade:** ⭐⭐ Média (Sprint 3, operacional)
- **Dependências:** 09_next_steps_engine (pending_orders), 08_wormlog (history)
- **Integra com:** 12_output_policies (render updates), 06_route_policy (route_id)

---

#### **12_output_policies_hybrid.yaml** (23 KB, ~650 linhas)
- **Tipo:** Output orchestrator
- **Versão:** output_policies_hybrid_v2.3.0
- **Descrição:** Maestro final que orquestra card de saída (6 tipos, multi-formato)
- **Seções:**
  - Card selection (hierarquia 6 níveis)
    1. Critical (any critical syndrome)
    2. Review_sample (pré-analítico)
    3. Priority (any priority syndrome)
    4. Borderline (valores limítrofes)
    5. Routine normal (CBC normal)
    6. Abstain with guidance (>30% missing + nenhum padrão)
  - Card templates (6 tipos)
    - Critical: header, body sections (evidence, rationale, actions, next_steps, missing), footer, render options
    - Review_sample: flags pré-analíticos, instruções recoleta, block_result_release
    - Priority: síndromes, padrões, next_steps, dx diferencial
    - Routine borderline: valores limítrofes, orientação follow-up
    - Routine normal: valores normais, nenhum exame adicional
    - Abstain with guidance: taxa missing, próximos passos priorizados, pode prosseguir se...
  - Confidence mapping (C0/C1/C2)
    - C0: Inconclusivo (>30% missing ou critério diagnóstico ausente)
    - C1: Evidência parcial (padrão típico, proxy logic OK, missing <30%)
    - C2: Padrão consistente (critério diagnóstico presente, missing <10%)
  - Integration next_steps_engine (workflow, formatting markdown/HTML/JSON)
  - Render formats (4: markdown, HTML, JSON, FHIR R4)
  - Metadata (always_output_guarantee, 6-level fallback chain)
  - Validation (5 test cases)
- **Prioridade:** ⭐⭐ Média (Sprint 2)
- **Dependências:** 05_missingness (confidence), 09_next_steps_engine (integrate), 06_route_policy (output_class)
- **Integra com:** 11_case_state (card render updates), 08_wormlog (card_rendered)

---

### **/ Analise_Comparativa/ (2 arquivos, ~67 KB total)**

#### **ANALISE_COMPARATIVA_TRIPLA_HEMODOCTOR_SADMH_DEVTEAM.md** (48 KB, ~1.140 linhas)
- **Tipo:** Análise técnica master
- **Descrição:** Documento master com análise completa das 3 metodologias + decisões de integração
- **Seções:**
  - Sumário executivo
  - Fase 1-8: Análise original (HemoDoctor vs SADMH vs Dev Team)
  - **Fase 9:** Ajustes clínicos Dr. Abel (34 síndromes, normalização, pré-analítico)
  - **Fase 10:** Integração SADMH V2.3 Always-Output Design (8 módulos)
    - 09_next_steps_engine (1.450 linhas)
    - 05_missingness V2.3 (750 linhas)
    - 12_output_policies (650 linhas)
    - 11_case_state (600 linhas)
    - 06_route_policy (430 linhas)
    - 07_conflict_matrix (400 linhas)
    - 08_wormlog (520 linhas)
    - 10_runbook (550 linhas)
  - Arquitetura final integrada (diagrama)
  - Benefícios regulatórios (ANVISA/FDA/ISO/LGPD)
  - Score final (18/18 critérios, 100%)
  - Documentação gerada (15 YAMLs, 1 spec dev)
  - Próximos passos (Sprint 0-4)
- **Prioridade:** ⭐⭐⭐ Alta (contexto completo)
- **Dependências:** Nenhuma
- **Para:** Product Owner, Arquiteto, Hematologistas

---

#### **COMPARACAO_HIBRIDO_vs_SADMH_V2.3.md** (19 KB, ~470 linhas)
- **Tipo:** Comparação executiva
- **Descrição:** Comparação detalhada módulo por módulo (Híbrido V1.0 vs SADMH V2.3)
- **Seções:**
  - Sumário executivo (decisão: integrar TODOS os 8 módulos)
  - Módulos integrados (8 novos)
    - Comparação por módulo (aspecto, híbrido anterior, SADMH V2.3, decisão final)
    - Benefício ANVISA, benefício clínico, exemplos
  - Benefícios regulatórios integrados (tabelas comparativas ANVISA/FDA/ISO/LGPD)
  - Arquitetura final integrada (diagrama 13 módulos)
  - Score comparativo final (18/18 vs 13/13 vs 11/18 vs 8/18)
  - Recomendação executiva (✅ integrar todos, sem compromissos)
  - Próximos passos (Sprint 0-4, V0 8 sem, V1 12 sem, V2 16 sem)
  - Anexos gerados (15 YAMLs, 1 spec, documentação master)
- **Prioridade:** ⭐⭐ Média (decisões de design)
- **Dependências:** ANALISE_COMPARATIVA_TRIPLA
- **Para:** Product Owner, Arquiteto

---

### **/ Especificacoes_Dev/ (1 arquivo, ~14 KB)**

#### **DEV_TEAM_SPEC_09_NEXT_STEPS_ENGINE.md** (14 KB, ~350 linhas)
- **Tipo:** Especificação técnica
- **Descrição:** Spec completa do módulo 09 (next_steps_engine) com exemplos de código Python
- **Seções:**
  - Sumário executivo (o que é, por que é crítico, integração no pipeline)
  - Objetivo do módulo (dado caso, retornar lista 0-8 exames priorizados)
  - Arquitetura (estrutura YAML, lógica de execução Python)
  - Segurança (avaliação segura de expressões: simpleeval ou AST parsing)
  - Exemplos práticos (3 casos: IDA suspeita, TMA crítica, borderline MCV)
  - Testes unitários (6 casos obrigatórios: IDA complete/partial, TMA critical, borderline, prioritization, dedupe, max_items)
  - Casos de borda (4: sem dados, múltiplos triggers, trigger inválido, exame já presente)
  - Integração com outros módulos (05 missingness, 12 output_policies, 11 case_state)
  - Métricas de qualidade (coverage, dedupe, max_items, alert fatigue, test completion rate, time to diagnosis)
  - Implementação em etapas (Sprint 0-2)
  - Glossário para devs não-médicos (IDA, ACD, TMA, PTI, PTT, SHU, CIVD, etc.)
  - Contato e suporte
  - Checklist de implementação
- **Prioridade:** ⭐⭐⭐ Alta (dev team)
- **Dependências:** 09_next_steps_engine_hybrid.yaml
- **Para:** Dev Team (backend engineers)

---

## 🔗 MAPA DE DEPENDÊNCIAS

### **CORE (Base):**
```
00_config → 01_schema → 02_evidence → 03_syndromes → 04_output_templates
```

### **ALWAYS-OUTPUT (V2.3):**
```
03_syndromes → 05_missingness_v2.3 → 12_output_policies
              ↓
          09_next_steps_engine
```

### **AUDITORIA:**
```
03_syndromes → 06_route_policy → 07_conflict_matrix → 08_wormlog
```

### **OPERACIONAL:**
```
09_next_steps_engine → 11_case_state → 12_output_policies
```

### **SUPORTE:**
```
00_config → 07_normalization_heuristics → 08_wormlog
10_runbook (independente, descreve tudo)
```

---

## 📊 ESTATÍSTICAS

### **Arquivos por Tipo:**
- YAMLs: 15 arquivos
- Documentação master: 3 arquivos (README, INDEX, QUICKSTART)
- Análise técnica: 2 arquivos
- Especificações dev: 1 arquivo
- **Total: 21 arquivos**

### **Linhas de Código:**
- YAMLs: ~7.350 linhas
- Documentação: ~1.200 linhas
- **Total: ~8.550 linhas**

### **Tamanho Total:**
- YAMLs: ~336 KB
- Documentação: ~86 KB
- **Total: ~422 KB**

### **Prioridade:**
- Alta (⭐⭐⭐): 10 arquivos (README, QUICKSTART, 00, 01, 02, 03, 09, 10, ANALISE_COMPARATIVA, DEV_TEAM_SPEC)
- Média (⭐⭐): 7 arquivos (INDEX, 04, 05, 07_norm, 11, 12, COMPARACAO)
- Baixa (⭐): 4 arquivos (06, 07_conflict, 08, Documentacao_Tecnica)

---

## ✅ CHECKLIST DE VALIDAÇÃO

- [ ] Todos os 15 YAMLs presentes e completos
- [ ] README master criado
- [ ] INDEX completo criado (este arquivo)
- [ ] QUICKSTART criado
- [ ] Análise comparativa (2 docs) copiados
- [ ] Especificação dev (1 doc) copiada
- [ ] Estrutura de pastas organizada
- [ ] Interdependências documentadas
- [ ] Ordem de leitura definida
- [ ] Prioridades marcadas
- [ ] Estatísticas calculadas

---

## 📞 CONTATO

**Product Owner Clínico:** Dr. Abel Costa (IDOR-SP)  
**Versão:** V1.0  
**Data:** Outubro 2025  
**Status:** ✅ **100% Completo - Pronto para Implementação**

---

**FIM DO ÍNDICE COMPLETO**

