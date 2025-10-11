# Contribuindo para o HemoDoctor

## 🏥 Sobre o Projeto

HemoDoctor é um projeto de documentação técnica e regulatória para dispositivos médicos SaMD (Software as a Medical Device) focado em oncologia hematológica.

## ⚠️ Importante

Este projeto contém documentação regulatória crítica para submissões à ANVISA e FDA. Qualquer contribuição deve seguir rigorosamente os padrões de qualidade e conformidade regulatória.

## 🔐 Política de Contribuições

### Quem Pode Contribuir

Devido à natureza regulatória crítica deste projeto, contribuições são limitadas a:

1. **Membros da Equipe IDOR-SP**: Desenvolvedores e pesquisadores autorizados
2. **Especialistas Regulatórios**: Com credenciais verificadas
3. **Consultores Aprovados**: Mediante acordo formal

### Tipos de Contribuições Aceitas

#### ✅ Contribuições Bem-Vindas
- Correções de erros tipográficos ou gramaticais
- Melhorias na documentação técnica
- Atualizações de conformidade regulatória
- Adição de referências científicas
- Melhorias em scripts de automação

#### ❌ Contribuições Não Aceitas
- Alterações em documentos oficiais versionados sem aprovação
- Modificações em especificações técnicas (SRS, SDD, etc.)
- Mudanças em matrizes de rastreabilidade sem validação
- Alterações em relatórios clínicos (CER)

## 📝 Processo de Contribuição

### 1. Fork e Clone

```bash
# Fork o repositório através do GitHub
# Clone seu fork
git clone https://github.com/SEU_USUARIO/hemodoctor-docs.git
cd hemodoctor-docs
```

### 2. Crie uma Branch

```bash
# Use nomenclatura descritiva
git checkout -b feature/descricao-da-melhoria
# ou
git checkout -b fix/correcao-especifica
# ou
git checkout -b docs/atualizacao-documentacao
```

### 3. Faça Suas Alterações

- Mantenha commits pequenos e focados
- Siga os padrões de nomenclatura existentes
- Não modifique arquivos em `AUTHORITATIVE_BASELINE/` sem autorização
- Teste scripts antes de submeter

### 4. Commit com Mensagem Descritiva

```bash
git add .
git commit -m "tipo: descrição clara da alteração

- Detalhe 1
- Detalhe 2
- Justificativa regulatória (se aplicável)"
```

Tipos de commit:
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `refactor`: Refatoração de código
- `test`: Adição de testes
- `chore`: Tarefas de manutenção

### 5. Push e Pull Request

```bash
git push origin sua-branch
```

Crie um Pull Request no GitHub com:
- **Título claro**: Descreva a mudança sucintamente
- **Descrição detalhada**: 
  - O que foi alterado
  - Por que foi alterado
  - Impacto regulatório (se houver)
  - Referências (normas, documentos)
- **Checklist**: Confirme que seguiu todos os padrões

## 📋 Checklist de PR

Antes de submeter um PR, verifique:

- [ ] Código/documentação segue os padrões existentes
- [ ] Nenhum arquivo sensível foi incluído
- [ ] Commits são claros e descritivos
- [ ] Documentação foi atualizada (se necessário)
- [ ] Scripts foram testados
- [ ] Não há conflitos com a branch main
- [ ] Impacto regulatório foi avaliado

## 🔍 Revisão de Código

Todos os PRs passam por:

1. **Revisão Técnica**: Validação de qualidade do código/documentação
2. **Revisão Regulatória**: Conformidade com normas ANVISA/FDA
3. **Validação de Rastreabilidade**: Impacto em documentos rastreados
4. **Aprovação Final**: Por pelo menos um maintainer

## 📚 Padrões de Documentação

### Nomenclatura de Arquivos

```
[TIPO]-[NUM]_[Descrição]_v[X.Y]_[STATUS].ext

Exemplos:
- SRS-001_Software_Requirements_v2.2_OFICIAL.md
- TRC-001_Traceability_Matrix_v2.1_OFICIAL.csv
- RMP-001_Risk_Management_Plan_v1.0_OFICIAL.md
```

### Versionamento

- **Major (X.0)**: Mudanças significativas de estrutura
- **Minor (X.Y)**: Atualizações de conteúdo
- **Status**: DRAFT, REVIEW, OFICIAL, DEPRECATED

## 🛡️ Segurança

### Dados Sensíveis

**NUNCA** inclua nos commits:
- Dados de pacientes
- Credenciais ou tokens
- Informações proprietárias não autorizadas
- Resultados clínicos identificáveis

### Relatar Vulnerabilidades

Se encontrar uma vulnerabilidade de segurança:
1. **NÃO** abra uma issue pública
2. Envie um email para: [seguranca@idor.org]
3. Aguarde resposta antes de divulgar

## 🤝 Código de Conduta

### Nossos Padrões

- Seja respeitoso e profissional
- Aceite críticas construtivas
- Foque no que é melhor para o projeto
- Mantenha confidencialidade quando necessário

### Comportamentos Inaceitáveis

- Linguagem ofensiva ou discriminatória
- Assédio de qualquer tipo
- Divulgação de informações confidenciais
- Conduta antiética ou não profissional

## 📞 Contato

Para questões sobre contribuições:
- **Issues**: Use para discussões técnicas
- **Email**: [hemodoctor@idor.org]
- **Equipe**: Veja AUTHORITATIVE_BASELINE/README_FINAL.md

## 📄 Licença

Ao contribuir, você concorda que suas contribuições serão licenciadas sob os mesmos termos do projeto.

---

**Agradecemos seu interesse em contribuir para o HemoDoctor!**

Juntos podemos melhorar o suporte à decisão clínica em oncologia hematológica.

