#!/usr/bin/env node

const fs = require('fs');

// Load agent data
const data = JSON.parse(fs.readFileSync('RELATORIO_ANALISE_AGENTES_HEMODOCTOR.json', 'utf8'));

// Create command map: command -> [agents that have it]
const commandMap = {};

data.agents.forEach(agent => {
  agent.commands.forEach(cmd => {
    if (!commandMap[cmd]) {
      commandMap[cmd] = [];
    }
    commandMap[cmd].push(agent.name);
  });
});

// Find duplicates
const duplicates = {};
const unique = {};

Object.entries(commandMap).forEach(([cmd, agents]) => {
  if (agents.length > 1) {
    duplicates[cmd] = agents;
  } else {
    unique[cmd] = agents[0];
  }
});

// Statistics
const totalCommands = Object.keys(commandMap).length;
const duplicateCount = Object.keys(duplicates).length;
const uniqueCount = Object.keys(unique).length;
const duplicateInstances = Object.values(duplicates).reduce((sum, agents) => sum + agents.length, 0);

console.log('# 🔍 ANÁLISE DE DUPLICAÇÃO DE COMANDOS\n');
console.log(`## 📊 ESTATÍSTICAS\n`);
console.log(`| Métrica | Valor |`);
console.log(`|---------|-------|`);
console.log(`| **Total de Comandos Únicos** | ${totalCommands} |`);
console.log(`| **Comandos Duplicados** | ${duplicateCount} (${(duplicateCount/totalCommands*100).toFixed(1)}%) |`);
console.log(`| **Comandos Únicos** | ${uniqueCount} (${(uniqueCount/totalCommands*100).toFixed(1)}%) |`);
console.log(`| **Total de Instâncias** | ${data.summary.totalCommands} |`);
console.log(`| **Instâncias Duplicadas** | ${duplicateInstances - duplicateCount} |`);
console.log(`| **Taxa de Redundância** | ${((duplicateInstances - duplicateCount) / data.summary.totalCommands * 100).toFixed(1)}% |`);

console.log(`\n---\n`);
console.log(`## 🔄 COMANDOS DUPLICADOS (${duplicateCount})\n`);

Object.entries(duplicates).sort((a, b) => b[1].length - a[1].length).forEach(([cmd, agents]) => {
  console.log(`### **${cmd}** (${agents.length} agentes)`);
  agents.forEach(agent => {
    console.log(`- ${agent}`);
  });
  console.log('');
});

console.log(`---\n`);
console.log(`## ✅ COMANDOS ÚNICOS (${uniqueCount})\n`);

// Group by agent
const agentCommands = {};
Object.entries(unique).forEach(([cmd, agent]) => {
  if (!agentCommands[agent]) {
    agentCommands[agent] = [];
  }
  agentCommands[agent].push(cmd);
});

Object.entries(agentCommands).sort((a, b) => b[1].length - a[1].length).forEach(([agent, cmds]) => {
  console.log(`### **${agent}** (${cmds.length} únicos)`);
  cmds.forEach(cmd => console.log(`- ${cmd}`));
  console.log('');
});

// Semantic analysis
console.log(`---\n`);
console.log(`## 🎯 ANÁLISE SEMÂNTICA\n`);

const semanticGroups = {
  'sample-size': ['sample-size calculation', 'statistical power'],
  'gap-analysis': ['gap identification', 'compliance gaps'],
  'crf-design': ['case report forms design'],
  'interim-analysis': ['interim analysis planning'],
  'submission-package': ['submission package assembly', 'submission package complete', 'cep-submission-package'],
};

console.log('### **Funções Semanticamente Relacionadas:**\n');
Object.entries(semanticGroups).forEach(([concept, related]) => {
  const relatedCommands = Object.keys(commandMap).filter(cmd =>
    related.some(r => cmd.toLowerCase().includes(r.toLowerCase()))
  );
  if (relatedCommands.length > 0) {
    console.log(`**${concept}:**`);
    relatedCommands.forEach(cmd => {
      console.log(`- ${cmd}: ${commandMap[cmd].join(', ')}`);
    });
    console.log('');
  }
});

// Recommendations
console.log(`---\n`);
console.log(`## 💡 RECOMENDAÇÕES\n`);

console.log(`### **1. Duplicações Legítimas (Manter):**\n`);
console.log(`Comandos onde a duplicação faz sentido (expertise diferente):\n`);
Object.entries(duplicates).forEach(([cmd, agents]) => {
  if (agents.length === 2) {
    console.log(`- **${cmd}**: Especialidades complementares`);
  }
});

console.log(`\n### **2. Duplicações para Revisar:**\n`);
console.log(`Comandos com >2 implementações (possível consolidação):\n`);
Object.entries(duplicates).forEach(([cmd, agents]) => {
  if (agents.length > 2) {
    console.log(`- **${cmd}**: ${agents.length} agentes (${agents.join(', ')})`);
  }
});

console.log(`\n### **3. Comandos para Padronizar:**\n`);
console.log(`Comandos similares com nomes diferentes:\n`);
const similarCommands = [
  ['/submission-package', '/submission-package-complete', '/cep-submission-package'],
  ['/gap-analysis', '/external-gap-identification', '/gap-detection'],
  ['/clinical-protocol', '/protocol-create'],
];

similarCommands.forEach(group => {
  console.log(`- ${group.join(' ≈ ')}`);
  group.forEach(cmd => {
    if (commandMap[cmd]) {
      console.log(`  - ${cmd}: ${commandMap[cmd].join(', ')}`);
    }
  });
  console.log('');
});
