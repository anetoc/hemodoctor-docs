# HemoDoctor Hybrid V1.0 - Custom Agent Skills

Custom Claude Code Agent Skills para o projeto HemoDoctor Hybrid V1.0.

## Visão Geral

Este diretório contém **9 Skills customizadas** que fornecem expertise especializada para trabalhar com o sistema de apoio à decisão clínica HemoDoctor:

### Core Skills (4)
1. **YAML Validation** - Validar arquivos YAML de configuração
2. **Evidence Engine** - Trabalhar com as 75 regras de evidência
3. **Test Suite** - Criar e executar testes (pytest)
4. **Documentation** - Manter documentação técnica regulatória

### Advanced Skills (5)
5. **HemoDoctor Validator** - Validação completa multi-arquivo + compliance
6. **Code Helper** - Gerar boilerplate (parsers, testes, CSV processors)
7. **Next Steps Debugger** - Debug e teste de triggers (módulo 09)
8. **YAML DAG Visualizer** - Diagramas Mermaid de decision trees
9. **Clinical Test Generator** - Gerar casos de teste sintéticos com ground truth

## Como as Skills Funcionam

Skills são carregadas automaticamente pelo Claude Code quando relevantes. Cada Skill:

- **Metadata (sempre carregada)**: Nome e descrição no frontmatter YAML
- **Instructions (carregada quando trigada)**: Corpo do SKILL.md
- **Resources (carregadas conforme necessário)**: Scripts, referências, exemplos

### Progressive Disclosure

Claude carrega conteúdo em estágios:
1. Startup: Metadata de todas as skills (~100 tokens cada)
2. Triggered: Instruções do SKILL.md quando relevante (~5k tokens)
3. As needed: Arquivos referenciados e scripts executados

Isso significa que você pode ter muitas Skills instaladas sem penalidade de contexto.

---

## Core Skills

### 1. YAML Validation

**Trigger:** Quando trabalhando com YAMLs no diretório `YAMLs/`, validando sintaxe, ou troubleshooting erros YAML.

**Capabilities:**
- Valida sintaxe YAML de todos os 15 módulos
- Verifica estrutura e campos obrigatórios
- Cross-references entre arquivos
- Scripts: `validate_yaml.py`, `validate_all.py`

**Quick use:**
```bash
python .claude/skills/yaml-validation/scripts/validate_all.py
```

---

### 2. Evidence Engine

**Trigger:** Quando implementando avaliação de evidências, testando lógica de evidências, ou debugando detecção de síndromes.

**Capabilities:**
- Trabalha com as 75 evidências atômicas (E-XXX)
- Safe expression evaluation (simpleeval)
- Handling missing data gracefully
- Testing evidence logic
- Scripts: `list_evidences.py`, `test_evidence.py`

**Quick use:**
```bash
python .claude/skills/evidence-engine/scripts/list_evidences.py --category critical_gates
python .claude/skills/evidence-engine/scripts/test_evidence.py E-ANC-CRIT --anc=0.3
```

---

### 3. Test Suite

**Trigger:** Quando implementando testes Sprint 0, debugando falhas de teste, ou validando requisitos Red List (FN=0).

**Capabilities:**
- Pytest-based testing framework
- Sprint 0 test requirements (20 casos mínimo)
- Red List validation (FN=0 obrigatório)
- Coverage targets (≥80% line, ≥70% branch)
- Test templates e patterns

**Quick use:**
```bash
pytest -v                      # Run all tests
pytest -v -m redlist          # Run Red List tests only
pytest --cov=. --cov-report=html  # Coverage report
```

---

### 4. Documentation

**Trigger:** Quando atualizando specs, criando relatórios técnicos, ou preparando documentos de submissão.

**Capabilities:**
- Standards ANVISA RDC 657/2022
- Standards FDA 21 CFR Part 11
- Standards ISO 13485:2016
- Templates regulatórios
- Docstring patterns
- Versioning (semantic)

**Quick use:**
- Ver SKILL.md para templates de test reports, technical notes, etc.

---

## Advanced Skills

### 5. HemoDoctor Validator

**Trigger:** Quando validando YAMLs, verificando compliance regulatório, ou preparando para deployment.

**Capabilities:**
- Validação completa multi-arquivo (evidences + syndromes + triggers)
- Consistency checker (cross-file references)
- Coverage checker (34 syndromes → 34 triggers)
- Regulatory compliance (ANVISA/FDA)
- Scripts: `validate_yaml.py`, `consistency_checker.py`, `coverage_checker.py`

**Quick use:**
```bash
# Validar arquivo único
python .claude/skills/hemodoctor-validator/scripts/validate_yaml.py YAMLs/03_syndromes_hybrid.yaml

# Verificar coverage de triggers
python .claude/skills/hemodoctor-validator/scripts/coverage_checker.py \
  YAMLs/03_syndromes_hybrid.yaml YAMLs/09_next_steps_engine_hybrid.yaml

# Verificar consistência cross-file
python .claude/skills/hemodoctor-validator/scripts/consistency_checker.py \
  YAMLs/02_evidence_hybrid.yaml YAMLs/03_syndromes_hybrid.yaml
```

---

### 6. Code Helper

**Trigger:** Quando gerando boilerplate, escrevendo testes, ou automatizando tarefas repetitivas.

**Capabilities:**
- Gera YAML parsers (load/save/validate)
- Gera pytest templates (fixtures, edge cases)
- Gera CSV processors (CSV ↔ JSON)
- Gera batch processors (processar múltiplos arquivos)
- Calcula estatísticas de datasets
- Script: `code_helper.py`

**Quick use:**
```bash
# Gerar YAML parser
python .claude/skills/code-helper/scripts/code_helper.py yaml-parser my_parser.py

# Gerar pytest template
python .claude/skills/code-helper/scripts/code_helper.py pytest test_module.py

# Gerar CSV processor
python .claude/skills/code-helper/scripts/code_helper.py csv-processor process_csv.py
```

---

### 7. Next Steps Debugger

**Trigger:** Quando desenvolvendo triggers, debugando next_steps_engine, ou testando coverage de triggers.

**Capabilities:**
- Testa triggers do módulo 09 (next_steps_engine)
- Simula casos clínicos
- Detecta dead code (triggers que nunca disparam)
- Valida sintaxe de expressões 'when'
- Regression testing
- Script: `debug_next_steps.py`

**Quick use:**
```bash
# Testar triggers com arquivo de casos
python .claude/skills/next-steps-debugger/scripts/debug_next_steps.py test \
  YAMLs/09_next_steps_engine_hybrid.yaml test_cases.json --verbose

# Simular caso único
python .claude/skills/next-steps-debugger/scripts/debug_next_steps.py simulate \
  YAMLs/09_next_steps_engine_hybrid.yaml --hb=9.5 --sex=F --mcv=72 --ferritin=8

# Verificar sintaxe de triggers
python .claude/skills/next-steps-debugger/scripts/debug_next_steps.py check \
  YAMLs/09_next_steps_engine_hybrid.yaml
```

---

### 8. YAML DAG Visualizer

**Trigger:** Quando criando documentação, visualizando decision trees, ou preparando submissões regulatórias.

**Capabilities:**
- Gera diagramas Mermaid DAG
- Visualiza evidências → síndromes
- Filtra por síndrome específica
- Filtra por nível de criticality
- Gera diagramas de dependências de módulos
- Exports para Markdown
- Script: `visualize_dag.py`

**Quick use:**
```bash
# DAG completo (75 evidências → 34 síndromes)
python .claude/skills/yaml-dag-visualizer/scripts/visualize_dag.py full \
  YAMLs/02_evidence_hybrid.yaml YAMLs/03_syndromes_hybrid.yaml dag_full.md

# DAG de síndrome específica (IDA)
python .claude/skills/yaml-dag-visualizer/scripts/visualize_dag.py syndrome \
  YAMLs/02_evidence_hybrid.yaml YAMLs/03_syndromes_hybrid.yaml S-IDA ida_dag.md

# DAG de síndromes críticas
python .claude/skills/yaml-dag-visualizer/scripts/visualize_dag.py priority \
  YAMLs/02_evidence_hybrid.yaml YAMLs/03_syndromes_hybrid.yaml critical critical_dag.md

# Dependências de módulos
python .claude/skills/yaml-dag-visualizer/scripts/visualize_dag.py modules module_deps.md
```

---

### 9. Clinical Test Generator

**Trigger:** Quando gerando casos de teste, criando Red List, ou preparando datasets de validação.

**Capabilities:**
- Gera casos sintéticos de CBC com ground truth
- Cria Red List (40+ casos por síndrome crítica)
- Gera validation sets balanceados (500+ casos)
- Cria missing-data scenarios
- Gera borderline cases
- Exports para JSON/CSV/YAML
- Script: `generate_test_cases.py`

**Quick use:**
```bash
# Gerar Red List (320 casos críticos)
python .claude/skills/clinical-test-generator/scripts/generate_test_cases.py \
  red-list 40 red_list.json

# Gerar validation set (500 casos balanceados)
python .claude/skills/clinical-test-generator/scripts/generate_test_cases.py \
  validation 500 validation_set.csv

# Gerar casos com missing data
python .claude/skills/clinical-test-generator/scripts/generate_test_cases.py \
  missing-data 100 missing_cases.json

# Gerar casos borderline
python .claude/skills/clinical-test-generator/scripts/generate_test_cases.py \
  borderline 50 borderline_cases.yaml
```

---

## Estrutura de Diretórios

```
.claude/skills/
├── README.md                          # Este arquivo
│
├── yaml-validation/                   # Core Skill 1
│   ├── SKILL.md
│   └── scripts/
│       ├── validate_yaml.py
│       └── validate_all.py
│
├── evidence-engine/                   # Core Skill 2
│   ├── SKILL.md
│   └── scripts/
│       ├── list_evidences.py
│       └── test_evidence.py
│
├── test-suite/                        # Core Skill 3
│   └── SKILL.md
│
├── documentation/                     # Core Skill 4
│   └── SKILL.md
│
├── hemodoctor-validator/              # Advanced Skill 5
│   ├── SKILL.md
│   ├── references/
│   │   └── quick_reference.md
│   └── scripts/
│       ├── validate_yaml.py
│       ├── consistency_checker.py
│       └── coverage_checker.py
│
├── code-helper/                       # Advanced Skill 6
│   ├── SKILL.md
│   └── scripts/
│       └── code_helper.py
│
├── next-steps-debugger/               # Advanced Skill 7
│   ├── SKILL.md
│   └── scripts/
│       └── debug_next_steps.py
│
├── yaml-dag-visualizer/               # Advanced Skill 8
│   ├── SKILL.md
│   └── scripts/
│       └── visualize_dag.py
│
└── clinical-test-generator/           # Advanced Skill 9
    ├── SKILL.md
    ├── references/
    │   └── clinical_patterns.md
    └── scripts/
        └── generate_test_cases.py
```

---

## Usando as Skills

### Método 1: Implícito (Recomendado)

Claude automaticamente detecta e usa Skills relevantes:

```
Você: "Valide todos os arquivos YAML do projeto"
Claude: [Usa HemoDoctor Validator Skill automaticamente]
```

```
Você: "Gere 40 casos de TMA para o Red List"
Claude: [Usa Clinical Test Generator Skill automaticamente]
```

```
Você: "Crie um diagrama mostrando as evidências da síndrome S-IDA"
Claude: [Usa YAML DAG Visualizer Skill automaticamente]
```

### Método 2: Explícito

Você pode referenciar Skills diretamente:

```
Você: "Use a HemoDoctor Validator Skill para verificar consistência entre evidences e syndromes"
```

### Método 3: Scripts Diretos

Execute scripts manualmente quando preferir:

```bash
cd /Users/abelcosta/Documents/HemoDoctor/docs/HEMODOCTOR_HIBRIDO_V1.0

# Validação completa
python .claude/skills/hemodoctor-validator/scripts/validate_yaml.py YAMLs/

# Gerar código
python .claude/skills/code-helper/scripts/code_helper.py pytest test_new.py

# Debug triggers
python .claude/skills/next-steps-debugger/scripts/debug_next_steps.py check YAMLs/09_next_steps_engine_hybrid.yaml

# Visualizar DAG
python .claude/skills/yaml-dag-visualizer/scripts/visualize_dag.py full YAMLs/02_evidence_hybrid.yaml YAMLs/03_syndromes_hybrid.yaml dag.md

# Gerar testes
python .claude/skills/clinical-test-generator/scripts/generate_test_cases.py red-list 40 red_list.json
```

---

## Workflows Recomendados

### Workflow 1: Desenvolvimento de Nova Síndrome

1. **Code Helper** → Gerar boilerplate YAML
2. **YAML Validation** → Validar sintaxe
3. **HemoDoctor Validator** → Verificar consistência
4. **YAML DAG Visualizer** → Visualizar decision tree
5. **Clinical Test Generator** → Criar casos de teste
6. **Test Suite** → Validar com pytest

### Workflow 2: Debug de Triggers

1. **Next Steps Debugger** → Verificar sintaxe de 'when'
2. **Next Steps Debugger** → Simular casos
3. **HemoDoctor Validator** → Verificar coverage (34 syndromes → 34 triggers)
4. **Clinical Test Generator** → Gerar edge cases
5. **Test Suite** → Regression testing

### Workflow 3: Preparação para Deployment

1. **HemoDoctor Validator** → Validação completa multi-arquivo
2. **HemoDoctor Validator** → Coverage checker (100%)
3. **Clinical Test Generator** → Red List (FN=0)
4. **Test Suite** → Testes completos (≥80% coverage)
5. **YAML DAG Visualizer** → Gerar documentação regulatória
6. **Documentation** → Atualizar specs técnicas

---

## Best Practices

### Para Claude

1. **Check memory first**: Sempre verifique `.claude/skills/` antes de tarefas
2. **Use scripts**: Scripts são mais confiáveis que código gerado
3. **Reference by path**: Use caminhos completos ao executar scripts
4. **Report results**: Mostre output dos scripts ao usuário
5. **Combine Skills**: Use múltiplas Skills em workflows

### Para Desenvolvedores

1. **Mantenha Skills atualizadas**: Update quando arquitetura mudar
2. **Teste scripts**: Valide que scripts funcionam antes de commitar
3. **Documente mudanças**: Update SKILL.md quando adicionar features
4. **Compartilhe learnings**: Adicione patterns descobertos
5. **Use workflows**: Combine múltiplas Skills para tarefas complexas

---

## Troubleshooting

**Skill não está sendo trigada:**
- Verifique que `description` no frontmatter é clara e específica
- Inclua keywords que Claude deve reconhecer
- Verifique que SKILL.md está no lugar correto

**Script falha ao executar:**
- Verifique permissões: `chmod +x script.py`
- Teste manualmente primeiro: `python script.py`
- Verifique que dependências estão instaladas

**Skill carrega mas não funciona:**
- Verifique sintaxe YAML do frontmatter
- Verifique que instruções são claras e concisas
- Adicione exemplos se Claude está confuso

---

## Recursos

**Documentação Skills:**
- [Anthropic Skills Guide](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills)
- [Skills Cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills)
- [Best Practices](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices)

**Projeto HemoDoctor:**
- [README.md](../README.md) - Project overview
- [CLAUDE.md](../CLAUDE.md) - AI context
- [INDEX_COMPLETO.md](../INDEX_COMPLETO.md) - Complete file index

---

## Estatísticas

**Total de Skills:** 9 (4 core + 5 advanced)

**Total de Scripts:** 13 executáveis

**Total de Arquivos:** 22 (9 SKILL.md + 13 scripts + 2 references + 1 README)

**Capabilities Totais:**
- 15 YAML validation capabilities
- 75 Evidence patterns
- 34 Syndrome logic handlers
- 34 Trigger debuggers
- Unlimited test case generation
- Unlimited diagram generation
- Complete regulatory compliance

---

## Licença

Estas Skills são específicas para o projeto HemoDoctor Hybrid V1.0 e devem ser usadas apenas neste contexto.

Ver `LICENSE.txt` em cada diretório de Skill para termos completos.

---

**Mantido por:** Dr. Abel Costa (IDOR-SP)
**Versão:** 2.0.0
**Data:** 19 de Outubro de 2025
**Skills:** 9 customizadas (4 core + 5 advanced)
**Scripts:** 13 executáveis de automação
**Status:** ✅ Production Ready
