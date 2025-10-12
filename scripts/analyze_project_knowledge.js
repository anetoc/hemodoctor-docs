#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Load agent data
const data = JSON.parse(fs.readFileSync('RELATORIO_ANALISE_AGENTES_HEMODOCTOR.json', 'utf8'));

const agentsDir = 'HEMODOCTOR_AGENTES';

// Keywords to search for project knowledge
const projectKeywords = {
  projectName: ['HemoDoctor', 'hemodoctor', 'HEMODOCTOR'],
  deviceType: ['SaMD', 'Software as Medical Device', 'CBC', 'Complete Blood Count', 'Class III'],
  regulatory: ['ANVISA', 'RDC 751', 'RDC 657', 'FDA 510(k)', 'IEC 62304', 'ISO 14971'],
  clinicalContext: ['hematology', 'hematologia', 'pediatric', 'pediátrico', 'severity', 'CATEGORIA'],
  documentation: ['CLAUDE.md', 'CONSOLIDADO', 'master documentation', '01_SUBMISSAO_CEP', '02_SUBMISSAO_ANVISA'],
  otherAgents: ['@anvisa-regulatory', '@clinical-evidence', '@biostatistics', '@cep-protocol', 'orchestrator', 'orchestration'],
  backlog: ['TODO', 'backlog', 'task', 'tarefa', 'P0', 'P1', 'priority'],
};

console.log('# 🔍 ANÁLISE DE CONHECIMENTO DO PROJETO\n');
console.log('**Análise:** Verificando se cada agente conhece o contexto do projeto HemoDoctor\n');
console.log('---\n');

const results = {};

data.agents.forEach(agent => {
  const agentPath = path.join(agentsDir, agent.name);
  const claudePath = path.join(agentPath, 'CLAUDE.md');

  results[agent.name] = {
    hasClaudeMd: false,
    fileSize: 0,
    knowledge: {},
    score: 0,
    maxScore: 0,
  };

  if (!fs.existsSync(claudePath)) {
    console.log(`### ❌ **${agent.name}**\n`);
    console.log(`- **CLAUDE.md:** Não encontrado\n`);
    return;
  }

  results[agent.name].hasClaudeMd = true;
  const content = fs.readFileSync(claudePath, 'utf8');
  results[agent.name].fileSize = (content.length / 1024).toFixed(1);

  // Check for each keyword category
  Object.entries(projectKeywords).forEach(([category, keywords]) => {
    const matches = keywords.filter(kw =>
      content.toLowerCase().includes(kw.toLowerCase())
    );
    results[agent.name].knowledge[category] = {
      found: matches.length > 0,
      matches: matches,
      count: matches.length,
    };
    results[agent.name].maxScore += 1;
    if (matches.length > 0) {
      results[agent.name].score += 1;
    }
  });
});

// Summary statistics
const totalAgents = data.agents.length;
const agentsWithClaudeMd = Object.values(results).filter(r => r.hasClaudeMd).length;
const avgScore = Object.values(results).reduce((sum, r) => sum + r.score, 0) / totalAgents;
const avgKnowledgePercent = (avgScore / 7) * 100; // 7 categories

console.log(`## 📊 RESUMO GERAL\n`);
console.log(`| Métrica | Valor |`);
console.log(`|---------|-------|`);
console.log(`| **Total de Agentes** | ${totalAgents} |`);
console.log(`| **Agentes com CLAUDE.md** | ${agentsWithClaudeMd} (${(agentsWithClaudeMd/totalAgents*100).toFixed(0)}%) |`);
console.log(`| **Pontuação Média** | ${avgScore.toFixed(1)}/7 (${avgKnowledgePercent.toFixed(0)}%) |`);
console.log(`\n---\n`);

// Detailed results
console.log(`## 🔍 ANÁLISE DETALHADA POR AGENTE\n`);

Object.entries(results).sort((a, b) => b[1].score - a[1].score).forEach(([agentName, result]) => {
  if (!result.hasClaudeMd) {
    console.log(`### ❌ **${agentName}**\n`);
    console.log(`- **Status:** CLAUDE.md não encontrado\n`);
    return;
  }

  const scorePercent = (result.score / result.maxScore * 100).toFixed(0);
  const emoji = scorePercent >= 80 ? '🟢' : scorePercent >= 50 ? '🟡' : '🔴';

  console.log(`### ${emoji} **${agentName}** (${result.score}/${result.maxScore} - ${scorePercent}%)\n`);
  console.log(`- **Arquivo:** CLAUDE.md (${result.fileSize} KB)\n`);

  Object.entries(result.knowledge).forEach(([category, data]) => {
    const status = data.found ? '✅' : '❌';
    console.log(`- **${category}:** ${status} ${data.found ? `(${data.count} menções)` : ''}`);
    if (data.found && data.matches.length > 0 && data.matches.length <= 3) {
      console.log(`  - ${data.matches.join(', ')}`);
    }
  });
  console.log('');
});

// Category analysis
console.log(`---\n`);
console.log(`## 📊 ANÁLISE POR CATEGORIA\n`);

const categoryStats = {};
Object.keys(projectKeywords).forEach(category => {
  categoryStats[category] = {
    agentsWithKnowledge: 0,
    totalMentions: 0,
  };
  Object.values(results).forEach(result => {
    if (result.knowledge[category]?.found) {
      categoryStats[category].agentsWithKnowledge++;
      categoryStats[category].totalMentions += result.knowledge[category].count;
    }
  });
});

console.log(`| Categoria | Agentes com Conhecimento | % | Total Menções |`);
console.log(`|-----------|--------------------------|---|---------------|`);
Object.entries(categoryStats).sort((a, b) => b[1].agentsWithKnowledge - a[1].agentsWithKnowledge).forEach(([category, stats]) => {
  const percent = (stats.agentsWithKnowledge / totalAgents * 100).toFixed(0);
  console.log(`| **${category}** | ${stats.agentsWithKnowledge}/${totalAgents} | ${percent}% | ${stats.totalMentions} |`);
});

console.log(`\n---\n`);
console.log(`## 💡 RECOMENDAÇÕES\n`);

// Find agents with low scores
const lowScoreAgents = Object.entries(results)
  .filter(([_, r]) => r.hasClaudeMd && r.score < 4)
  .sort((a, b) => a[1].score - b[1].score);

console.log(`### **1. Agentes com Baixo Conhecimento do Projeto (< 4/7):**\n`);
if (lowScoreAgents.length === 0) {
  console.log(`✅ Todos os agentes têm conhecimento adequado (≥4/7)!\n`);
} else {
  lowScoreAgents.forEach(([name, result]) => {
    console.log(`- **${name}**: ${result.score}/7 (${(result.score/7*100).toFixed(0)}%)`);
    const missing = Object.entries(result.knowledge)
      .filter(([_, data]) => !data.found)
      .map(([cat, _]) => cat);
    console.log(`  - **Faltam:** ${missing.join(', ')}`);
  });
  console.log('');
}

// Check for orchestrator
const hasOrchestrator = Object.entries(results).some(([name, result]) =>
  name.includes('orchestrator') || name.includes('project-manager')
);

console.log(`### **2. Agente Orquestrador:**\n`);
if (hasOrchestrator) {
  console.log(`✅ Encontrado agente orquestrador/project-manager\n`);
} else {
  console.log(`❌ **CRÍTICO:** Nenhum agente orquestrador/project-manager encontrado!\n`);
  console.log(`**Ação requerida:** Criar agente @hemodoctor-orchestrator com:\n`);
  console.log(`- Conhecimento completo do projeto (7/7 categorias)`);
  console.log(`- Conhecimento de todos os 12 agentes e seus comandos`);
  console.log(`- Capacidade de coordenação multi-agente`);
  console.log(`- Gestão de backlog unificado`);
  console.log(`- Protocolo de cold start para novas sessões\n`);
}

// Check inter-agent knowledge
const agentsKnowingOthers = Object.values(results).filter(r =>
  r.knowledge.otherAgents?.found
).length;

console.log(`### **3. Conhecimento Inter-Agentes:**\n`);
console.log(`- **Agentes que conhecem outros agentes:** ${agentsKnowingOthers}/${totalAgents} (${(agentsKnowingOthers/totalAgents*100).toFixed(0)}%)\n`);
if (agentsKnowingOthers < totalAgents * 0.8) {
  console.log(`⚠️ **Baixo nível de conhecimento inter-agentes!**\n`);
  console.log(`**Recomendação:** Adicionar seção "## OTHER AGENTS" em todos os CLAUDE.md\n`);
}

// Check backlog awareness
const agentsWithBacklog = Object.values(results).filter(r =>
  r.knowledge.backlog?.found
).length;

console.log(`### **4. Consciência de Backlog:**\n`);
console.log(`- **Agentes que conhecem sistema de backlog:** ${agentsWithBacklog}/${totalAgents} (${(agentsWithBacklog/totalAgents*100).toFixed(0)}%)\n`);
if (agentsWithBacklog < totalAgents * 0.5) {
  console.log(`⚠️ **Sistema de backlog não está bem estabelecido!**\n`);
  console.log(`**Recomendação:** Criar sistema unificado de TODO list/backlog\n`);
}

console.log(`---\n`);
console.log(`\n**Análise completa!**\n`);
