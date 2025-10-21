# 🎯 SLIDES: Briefing Dev Team HemoDoctor v2.3.1

**Formato:** Markdown → Exportar para slides (Marp, reveal.js, Google Slides)  
**Duração:** 60 minutos  
**Audiência:** Backend Engineers, QA, Arquiteto

---

## SLIDE 1: Título

```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║      BRIEFING: HemoDoctor Hybrid v2.3.1           ║
║          Sistema de Apoio à Decisão Clínica       ║
║                                                   ║
║              IDOR-SP • Outubro 2025               ║
║                                                   ║
╚═══════════════════════════════════════════════════╝

                Dr. Abel Costa
         AI Medical Device Specialist

                19/10/2025 • 60 min
```

---

## SLIDE 2: Agenda

### 📋 AGENDA (60 min)

| Tempo | Tópico |
|-------|--------|
| **00-10 min** | Visão Geral e Contexto |
| **10-25 min** | Arquitetura Técnica (YAMLs) |
| **25-40 min** | Correções Críticas e CDSS |
| **40-50 min** | Roadmap de Implementação |
| **50-60 min** | Q&A e Próximos Passos |

---

## SLIDE 3: O que é HemoDoctor?

### Sistema de Apoio à Decisão Clínica (CDSS)

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  CBC Input   │ ───▶ │  HemoDoctor  │ ───▶ │  Card Output │
│  (41 campos) │      │   v2.3.1     │      │ (não-diagn.) │
└──────────────┘      └──────────────┘      └──────────────┘
```

**Objetivo:**
- Detectar **35 síndromes hematológicas**
- **FN críticos = 0** (Red List)
- Microcopy **não-diagnóstica** (ANVISA/FDA)

**Público-alvo:**
- Médicos generalistas (não-hematologistas)
- Pronto-socorro, UTI, ambulatórios

---

## SLIDE 4: Contexto da Versão v2.3.1

### Evolução do Sistema

| Versão | Data | Status |
|--------|------|--------|
| **v1.0.0** | Out 2025 | ❌ 3 erros críticos |
| **v2.3.1** | Out 2025 | ✅ Erros corrigidos |

### v1.0.0 → v2.3.1

| Métrica | v1.0.0 | v2.3.1 | Delta |
|---------|--------|--------|-------|
| **Síndromes** | 34 | 35 | +1 (S-ACD) |
| **Evidências** | 75 | 79 | +4 |
| **Erros Críticos** | ❌ 3 | ✅ 0 | -3 |
| **Módulos CDSS** | 0 | 2 | +2 |
| **Triggers Críticos** | 48 | 54 | +6 |

---

## SLIDE 5: OS 3 ERROS CRÍTICOS

### ❌ Bugs Descobertos na Validação Externa

1. **S-PV (Policitemia Vera)**
   - ❌ Detectava **ANEMIA** (Hb baixo)
   - ✅ Corrigido: **ERITROCITOSE** (Hb alto)

2. **S-ERITROCITOSE-SECUNDARIA**
   - ❌ Detectava **ANEMIA** (Hb baixo)
   - ✅ Corrigido: **ERITROCITOSE** (Hb alto)

3. **S-PANCYTOPENIA**
   - ❌ Detectava **LEUCOCITOSE** (WBC alto)
   - ✅ Corrigido: **LEUCOPENIA** (WBC baixo)

**Impacto:** Falsos Negativos em casos críticos

---

## SLIDE 6: Correção 1 - S-PV

### ANTES (v1.0.0) ❌

```yaml
- id: S-PV
  combine:
    all: [E-HB-CRIT-LOW]  # ❌ ANEMIA!
```

### DEPOIS (v2.3.1) ✅

```yaml
- id: S-PV
  combine:
    any: [E-HB-HIGH, E-HCT-HIGH]  # ✅ ERITROCITOSE
  negative: [E-CRP-HIGH]
```

**Caso de Teste:**
```
Hb: 19.5 g/dL (M), Ht: 55%
v1.0.0: ❌ Não detecta S-PV
v2.3.1: ✅ Detecta S-PV (C1 ou C2)
```

---

## SLIDE 7: Correção 2 - S-PANCYTOPENIA

### ANTES (v1.0.0) ❌

```yaml
- id: S-PANCYTOPENIA
  combine:
    all: [E-HB-CRIT-LOW, E-PLT-LOW]
    any: [E-ANC-CRIT, E-WBC-HIGH]  # ❌ LEUCOCITOSE!
```

### DEPOIS (v2.3.1) ✅

```yaml
- id: S-PANCYTOPENIA
  combine:
    all: [E-ANEMIA, E-PLT-LOW, E-WBC-LOW]  # ✅ LEUCOPENIA
```

**Caso de Teste:**
```
Hb: 8.0 g/dL, WBC: 2.5×10⁹/L, PLT: 80×10⁹/L
v1.0.0: ❌ Não detecta S-PANCYTOPENIA
v2.3.1: ✅ Detecta S-PANCYTOPENIA (C1)
```

---

## SLIDE 8: Nova Síndrome - S-ACD

### S-ACD (Anemia da Doença Crônica/Inflamatória)

```yaml
- id: S-ACD
  criticality: priority
  combine:
    all: [E-ANEMIA]
    any: [E-FERRITIN-HIGH-100, E-CRP-HIGH]
  negative: [E-HBA2-HIGH, E-HEMOLYSIS-PATTERN]
  threshold: 0.7
```

**Clínica:**
- Anemia + ferritina alta (≥100) OU CRP alto
- Exclui talassemia e hemólise
- Tratamento: Condição inflamatória de base

**Total de síndromes:** 34 → **35** ✨

---

## SLIDE 9: Arquitetura Técnica

### Pipeline Completo

```python
┌────────────────────────────────────────────────────┐
│                                                    │
│  Input (CBC) → Normalizador → Evidence Engine →   │
│                                                    │
│  Syndrome Engine → Missingness Handler →          │
│                                                    │
│  Route Policy → Next Steps → Output Templates →   │
│                                                    │
│  WORM Log → Card Final (JSON/HTML/Markdown)       │
│                                                    │
└────────────────────────────────────────────────────┘
```

**14 Módulos YAML → Código Python**

---

## SLIDE 10: Stack Tecnológico

### Componentes Core

| Camada | Tecnologia |
|--------|-----------|
| **Backend** | Python 3.11+, FastAPI |
| **Validação** | Pydantic v2 |
| **ML** | PyTorch 2.0+ (sem scikit-learn!) |
| **Database** | PostgreSQL 15 (TimescaleDB) |
| **Cache** | Redis (opcional) |
| **Security** | HMAC-SHA256, KMS |
| **Observability** | Prometheus, Grafana, structlog |
| **Testing** | pytest, pytest-cov, httpx |

**Sem scikit-learn:** Usar torch.nn + numpy/sympy

---

## SLIDE 11: 14 Módulos YAML

| # | YAML | Propósito | Linhas |
|---|------|-----------|--------|
| **00** | config_hybrid.yaml | Cutoffs, unidades | 150 |
| **01** | schema_hybrid.yaml | 41 campos CBC | 200 |
| **02** | evidence_hybrid.yaml | 79 evidências | 800 |
| **03** | syndromes_hybrid.yaml | 35 síndromes | 1200 |
| **04** | output_templates_hybrid.yaml | Microcopy CDSS | 400 |
| **05** | missingness_hybrid_v2.3.yaml | Proxy logic | 300 |
| **06** | route_logic_hybrid.yaml | Routing policy | 250 |
| **08** | wormlog_hybrid.yaml | Auditoria | 150 |
| **09** | next_steps_engine_hybrid.yaml | 54 triggers | 600 |
| **10** | runbook_hybrid.yaml | Calibration | 200 |
| **11** | case_state_hybrid.yaml | State machine | 180 |
| **12** | output_policies_hybrid.yaml | Card selection | 220 |
| **12-CDSS** | output_policies_cdss.yaml | Gating CDSS | 180 |

**Total:** ~4,830 linhas de especificação

---

## SLIDE 12: CDSS - Microcopy Segura

### Módulo 04: Output Templates

**Propósito:** NUNCA usar linguagem diagnóstica

**Verbos PERMITIDOS:**
- ✅ "padrão compatível com"
- ✅ "sugere"
- ✅ "pode representar"
- ✅ "considerar"
- ✅ "recomenda-se"

**Verbos PROIBIDOS:**
- ❌ "diagnóstico de"
- ❌ "confirma"
- ❌ "tem (doença)"
- ❌ "é (doença)"

**Exemplo:**
```
❌ "Diagnóstico de anemia ferropriva"
✅ "Padrão compatível com anemia ferropriva (C1)"
```

---

## SLIDE 13: Gating Inteligente

### Módulo 12-CDSS: Próximos Passos

**Problema:** Sistema sugeria exames avançados antes dos básicos

**Solução:** Gating rules

```yaml
gating:
  - name: anemia_workup
    if: "S-IDA OR S-ACD OR S-MACRO-B12-FOLATE"
    require_first: ["Ferritina", "TSat", "CRP", "B12", "Folato"]
```

**Exemplo:**
```
❌ Sugerir "Medula óssea" sem "Ferritina"
✅ "PRIMEIRO: Ferritina, TSat, CRP"
```

**Benefício:** Custo-efetividade, segurança

---

## SLIDE 14: Roadmap - 4 Semanas

### Timeline de Implementação

```
Semana 1       Semana 2-3     Semana 4       Semana 5
───────────────────────────────────────────────────────
[Sprint 0]     [Sprint 1-2]   [Sprint 3]     [Sprint 4]
   Setup    →   Core Engines → Output+Audit → Calibration
   Parser       Syndrome       WORM Log       Retrospect
   Evidence     Next Steps     Red List       Performance
```

**Entregas:**
- **Semana 1:** Parser YAML + Evidence engine
- **Semana 2-3:** Syndrome engine + Next steps
- **Semana 4:** CDSS + WORM log + Red List
- **Semana 5:** Calibration + Retrospectiva 500 casos

---

## SLIDE 15: Sprint 0 (Semana 1)

### Setup + Parser

**Tasks:**
- [ ] Repo setup (Git, Docker, CI/CD)
- [ ] YAML Parser (Pydantic models)
- [ ] Normalizer (41 campos CBC)
- [ ] Evidence Engine básico (10 evidências)
- [ ] Testes unitários (coverage ≥60%)

**Entregável:** Pipeline parcial (Input → Evidences)

**Equipe:**
- 2 Backend Engineers (full-time)
- 1 QA Engineer (full-time)
- Dr. Abel Costa (part-time, 10h/semana)

---

## SLIDE 16: Sprint 1-2 (Semanas 2-3)

### Engines Core

**Tasks:**
- [ ] Syndrome Engine (35 síndromes)
- [ ] Missingness Handler (Always-output)
- [ ] Route Policy (critical > priority > routine)
- [ ] Next Steps Engine (54 triggers + gating)
- [ ] Testes de integração (50 casos)

**Entregável:** Pipeline end-to-end (sem WORM log)

**Milestone:** Sistema detecta 35 síndromes

---

## SLIDE 17: Sprint 3 (Semana 4)

### Output + Auditoria

**Tasks:**
- [ ] Output Templates (Markdown/HTML/JSON)
- [ ] Output Policies (card selection + gating)
- [ ] WORM Log (append-only + HMAC)
- [ ] Case State (state machine)
- [ ] **Red List validation (240 casos FN=0)** ⚠️

**Entregável:** Sistema completo funcional

**Crítico:** FN críticos = 0 obrigatório

---

## SLIDE 18: Sprint 4 (Semana 5)

### Calibration + Performance

**Tasks:**
- [ ] Retrospectiva 500 casos IDOR-SP
- [ ] Platt Calibration (torch.nn)
- [ ] Performance tuning (P99 <5s)
- [ ] Documentação técnica
- [ ] IFU Draft

**Entregável:** Sistema production-ready

**Métricas:**
- Sensibilidade/especificidade
- Alert burden (<50/1000)
- ECE <0.05

---

## SLIDE 19: Red List - Crítico

### 240 Casos Críticos (FN = 0)

**Propósito:** Garantir zero falsos negativos em casos graves

**Categorias:**
- TMA (microangiopatia trombótica)
- Neutropenia grave (ANC <0.5)
- Leucostase (WBC ≥100)
- APL suspeita (promielócitos + coagulopatia)
- Trombocitopenia grave (PLT <20)

**CI/CD:** Teste bloqueante (merge impedido se falhar)

**Prioridade:** MÁXIMA ⚠️

---

## SLIDE 20: WORM Log - Auditoria

### Write Once Read Many

**Estrutura:**
```json
{
  "event_id": "uuid4",
  "case_id_hash": "sha256:...",
  "route_id": "sha256:...",
  "fired_evidences": ["E-HB-HIGH", "E-HCT-HIGH"],
  "top_syndromes": [{"id": "S-PV", "confidence": "C1"}],
  "engine_versions": "v2.3.1",
  "config_hash": "sha256:...",
  "hmac_signature": "hmac_sha256:..."
}
```

**Garantias:**
- Append-only (nunca update/delete)
- HMAC impede adulteração
- Hash chain detecta remoção
- Retenção: 90 dias (LGPD)

---

## SLIDE 21: Exemplo Prático - PV

### Caso de Teste

**Input:**
```json
{
  "age_years": 55,
  "sex": "M",
  "hb": 19.5,
  "ht": 55,
  "wbc": 12.0,
  "plt": 450
}
```

**Processamento:**
1. Evidence Engine: `E-HB-HIGH`, `E-HCT-HIGH` → TRUE
2. Syndrome Engine: `S-PV` → C1 (score 0.75)
3. Next Steps: "Repetir CBC", "JAK2/CALR/MPL", "EPO sérica"
4. Output: Card PRIORIDADE

**v1.0.0:** ❌ Não detectaria  
**v2.3.1:** ✅ Detecta corretamente

---

## SLIDE 22: Exemplo Output - PV

### Card Gerado

```
┌─────────────────────────────────────────────────┐
│ PRIORIDADE — Eritrocitose — PV a considerar     │
├─────────────────────────────────────────────────┤
│                                                 │
│ Hipótese: **Policitemia Vera (C1)** — padrão   │
│ compatível (Hb/Ht altos).                       │
│                                                 │
│ **Por quê:** Hb 19.5 g/dL (M), Ht 55%.         │
│                                                 │
│ **Próximos passos:**                            │
│   1) Repetir CBC; confirmar persistência        │
│   2) JAK2/CALR/MPL                              │
│   3) EPO sérica (quando disponível)             │
│                                                 │
│ *CDSS de apoio à decisão. Não substitui         │
│  julgamento clínico. Resultado não é            │
│  diagnóstico.*                                  │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## SLIDE 23: Critérios de Sucesso

### Métricas por Sprint

| Sprint | Critério | Target |
|--------|----------|--------|
| **0** | Parser YAML | 10/14 OK |
| **0** | Evidence engine | 10/79 OK |
| **0** | Coverage | ≥60% |
| **1-2** | Syndrome engine | 35/35 OK |
| **1-2** | Next steps | 54/54 OK |
| **1-2** | Pipeline E2E | 50 casos OK |
| **3** | **Red List FN** | **0/240** ⚠️ |
| **3** | WORM log | Funcional |
| **4** | Retrospectiva | 500 casos |
| **4** | Calibration ECE | <0.05 |
| **4** | Performance P99 | <5s |

---

## SLIDE 24: Q&A Antecipado

### Perguntas Frequentes

**P1:** Por que não usar scikit-learn?  
**R:** Requisito do runbook v2.3.1 (reduzir dependências)

**P2:** Como garantir FN críticos = 0?  
**R:** Red List + CI/CD blocking

**P3:** Como funciona o WORM log?  
**R:** Append-only JSONL + HMAC + Hash chain

**P4:** Como testar localmente?  
**R:** Docker Compose

**P5:** Qual a prioridade de implementação?  
**R:** Red List primeiro (crítico)

---

## SLIDE 25: Material de Apoio

### Documentação para Devs

**Leitura OBRIGATÓRIA (2h):**

1. `GUIA_COMPLETO_POS_IMPLEMENTACAO_v2.3.1.md` (20 min)
2. `RELATORIO_IMPLEMENTACAO_v2.3.1_FINAL.md` (15 min)
3. `RELATORIO_MODULOS_CDSS_v2.3.1.md` (10 min)
4. **YAMLs** (1 hora):
   - `00_config_hybrid.yaml`
   - `02_evidence_hybrid.yaml`
   - `03_syndromes_hybrid.yaml`
   - `09_next_steps_engine_hybrid.yaml`

**Quick Start:**
- `DEVELOPER_QUICKSTART_v2.3.1.md` (código pronto)

---

## SLIDE 26: Próximos Passos Imediatos

### Após este Briefing (Hoje)

1. ✅ **Acesso ao Repositório**
   - Todos os devs clonarem repo
   - Verificar acesso aos YAMLs

2. ✅ **Leitura Obrigatória** (2h)
   - Guia completo
   - Relatórios técnicos
   - YAMLs principais

3. ✅ **Setup Local** (1h)
   - Docker + Docker Compose
   - Python 3.11+, Poetry
   - VSCode/PyCharm

---

## SLIDE 27: Segunda-Feira (Sprint 0 Kickoff)

### Planning Sprint 0

**Manhã (9h-12h):**
- Planning Sprint 0 (2h)
  - Divisão de tasks
  - Definition of Done
  - Estimativas

**Tarde (14h-18h):**
- Spike Técnico (4h)
  - Parser YAML → Pydantic
  - Evidence engine POC
  - Teste 5 evidências

**Daily Standup:** 15 min/dia (9h15)

---

## SLIDE 28: Recursos Necessários

### Equipe

| Papel | Alocação | Duração |
|-------|----------|---------|
| Backend Engineer 1 | Full-time | 4 semanas |
| Backend Engineer 2 | Full-time | 4 semanas |
| QA Engineer | Full-time | 4 semanas |
| Dr. Abel Costa | Part-time (10h/sem) | 4 semanas |

### Infra

- Docker + Docker Compose
- PostgreSQL 15 (8GB RAM, 100GB storage)
- Redis (opcional, cache)
- GitHub Actions (CI/CD)

### Dados

- 240 casos Red List
- 500 casos retrospectivos IDOR-SP
- 100 casos prospectivos (opcional)

---

## SLIDE 29: Contatos

### Equipe do Projeto

| Nome | Papel | Contato |
|------|-------|---------|
| **Dr. Abel Costa** | Hematologista IDOR-SP | abel@idor.org |
| **AI Medical Device** | Arquiteto Sistema | (contexto) |
| **Backend Lead** | Dev Team Lead | (fornecer) |
| **QA Lead** | Quality Assurance | (fornecer) |

**Repositório:** (fornecer URL)  
**Branch:** `feature/hemodoctor-hibrido-v1.0`  
**Commit:** `92662f0` (feat v2.3.1 + CDSS)

---

## SLIDE 30: Conclusão

```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║     HemoDoctor Hybrid v2.3.1 + CDSS               ║
║                                                   ║
║  ✅ 35 síndromes, 79 evidências                   ║
║  ✅ 3 erros críticos CORRIGIDOS                   ║
║  ✅ Microcopy segura não-diagnóstica              ║
║  ✅ Pipeline completo especificado                ║
║  ✅ Roadmap 4 semanas definido                    ║
║                                                   ║
║     🚀 PRONTO PARA IMPLEMENTAÇÃO 🚀               ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

**Next Meeting:** Sprint 0 Planning (Segunda-feira, 9h)

**Perguntas?**

---

## SLIDE 31: Obrigado!

```
           ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄
           █ ▄▄▄ █  ▀  ▄▀▄█▀
           █ ███ █  ▄▀▀▀▄▀▀▄
           █▄▄▄▄▄█  █▀▀▀█▀▄▀
           ▄▄▄  ▄▄▄▄▄▀▀▄▄▀▄▀
           █▄██▀▄▄▄▀▄▄▄▀▀ ▀█
           ▄▄▄▄▄▄▄  ▀▄█▀▀▄▀█
           █ ▄▄▄ █  ▀▀█▄▀ ▀▄
           █ ███ █  ██▄▀ ▄▄▄
           █▄▄▄▄▄█  █▀█▀▄▄▄█
```

**QR Code:** Documentação completa

**Contato:** abel@idor.org  
**Repo:** (fornecer link)

---

**FIM DOS SLIDES**

---

## NOTAS PARA APRESENTADOR

### Slide 1-5 (10 min) - Contexto
- Falar brevemente sobre IDOR-SP
- Explicar motivação do CDSS
- Enfatizar os 3 erros críticos

### Slide 6-14 (15 min) - Arquitetura
- Demonstrar correção PV (antes/depois)
- Mostrar YAML real no editor
- Explicar pipeline end-to-end

### Slide 15-18 (10 min) - Roadmap
- Ser claro sobre expectativas por sprint
- Enfatizar Red List (FN=0) como crítico
- Mostrar timeline visual

### Slide 19-22 (10 min) - Detalhes Técnicos
- Demonstrar WORM log
- Rodar exemplo de teste PV
- Mostrar output card real

### Slide 23-30 (10 min) - Fechamento
- Revisar critérios de sucesso
- Responder perguntas
- Definir próximos passos

### Slides 31 (5 min) - Buffer
- Q&A adicional
- Networking
- Setup de acesso

**Total:** 60 minutos

