#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * HemoDoctor Agent Analyzer
 * Analisa os agentes HemoDoctor (formato commands.json + CLAUDE.md)
 * Adaptado do BMAD AgentAnalyzer
 */

class HemoDoctorAgentAnalyzer {
  constructor(agentsDir) {
    this.agentsDir = agentsDir;
    this.agents = [];
  }

  /**
   * Analisa um agente individual
   */
  async analyzeAgent(agentName) {
    const agentPath = path.join(this.agentsDir, agentName);
    const commandsPath = path.join(agentPath, 'commands.json');
    const claudePath = path.join(agentPath, 'CLAUDE.md');

    const profile = {
      name: agentName,
      hasCommands: false,
      hasClaude: false,
      commands: [],
      commandCount: 0,
      expertise: [],
      capabilities: [],
      installed: false,
    };

    // Check if commands.json exists
    if (fs.existsSync(commandsPath)) {
      profile.hasCommands = true;
      const commandsData = JSON.parse(fs.readFileSync(commandsPath, 'utf8'));

      if (commandsData.commands) {
        profile.commands = Object.keys(commandsData.commands);
        profile.commandCount = profile.commands.length;
      }
    }

    // Check if CLAUDE.md exists
    if (fs.existsSync(claudePath)) {
      profile.hasClaude = true;
      const claudeContent = fs.readFileSync(claudePath, 'utf8');

      // Extract expertise areas
      const expertiseMatch = claudeContent.match(/## CORE EXPERTISE(.*?)##/s);
      if (expertiseMatch) {
        const lines = expertiseMatch[1].split('\n').filter(l => l.trim().startsWith('-'));
        profile.expertise = lines.map(l => l.replace(/^-\s*\*\*/, '').replace(/\*\*:.*/, '').trim());
      }

      // Extract capabilities
      const capabilitiesMatch = claudeContent.match(/## CAPABILITIES & TOOLS(.*?)##/s);
      if (capabilitiesMatch) {
        profile.capabilities = capabilitiesMatch[1]
          .match(/\*\*[A-Z-]+[0-9-]+\*\*:/g)
          ?.map(m => m.replace(/\*\*/g, '').replace(':', '')) || [];
      }
    }

    // Check if installed in ~/.claude/agents/
    const installedPath = path.join(process.env.HOME, '.claude', 'agents', agentName);
    profile.installed = fs.existsSync(installedPath);

    return profile;
  }

  /**
   * Analisa todos os agentes
   */
  async analyzeAll() {
    const entries = fs.readdirSync(this.agentsDir, { withFileTypes: true });

    for (const entry of entries) {
      if (entry.isDirectory() && !entry.name.startsWith('.') && !entry.name.startsWith('00_')) {
        // Skip docs/ folder
        if (entry.name === 'docs') continue;

        try {
          const profile = await this.analyzeAgent(entry.name);
          this.agents.push(profile);
        } catch (error) {
          console.error(`Error analyzing ${entry.name}:`, error.message);
        }
      }
    }

    return this.agents;
  }

  /**
   * Gera relatório em Markdown
   */
  generateReport() {
    const totalAgents = this.agents.length;
    const installedAgents = this.agents.filter(a => a.installed).length;
    const totalCommands = this.agents.reduce((sum, a) => sum + a.commandCount, 0);

    let report = `# 🤖 RELATÓRIO DE ANÁLISE - AGENTES HEMODOCTOR\n\n`;
    report += `**Data:** ${new Date().toISOString().split('T')[0]}\n`;
    report += `**Analisador:** HemoDoctorAgentAnalyzer (adaptado de BMAD)\n\n`;
    report += `---\n\n`;

    report += `## 📊 RESUMO EXECUTIVO\n\n`;
    report += `| Métrica | Valor |\n`;
    report += `|---------|-------|\n`;
    report += `| **Total de Agentes** | ${totalAgents} |\n`;
    report += `| **Agentes Instalados** | ${installedAgents} (${Math.round(installedAgents/totalAgents*100)}%) |\n`;
    report += `| **Total de Comandos** | ${totalCommands} |\n`;
    report += `| **Média Comandos/Agente** | ${(totalCommands/totalAgents).toFixed(1)} |\n\n`;

    report += `---\n\n`;
    report += `## 🔍 AGENTES DETALHADOS\n\n`;

    for (const agent of this.agents) {
      report += `### **${agent.name.replace(/-/g, ' ').toUpperCase()}**\n\n`;
      report += `| Atributo | Valor |\n`;
      report += `|----------|-------|\n`;
      report += `| **Status** | ${agent.installed ? '✅ Instalado' : '⏳ Não instalado'} |\n`;
      report += `| **Comandos** | ${agent.commandCount} |\n`;
      report += `| **CLAUDE.md** | ${agent.hasClaude ? '✅' : '❌'} |\n`;
      report += `| **commands.json** | ${agent.hasCommands ? '✅' : '❌'} |\n\n`;

      if (agent.commands.length > 0) {
        report += `**Comandos disponíveis:**\n`;
        for (const cmd of agent.commands) {
          report += `- \`${cmd}\`\n`;
        }
        report += `\n`;
      }

      if (agent.expertise.length > 0) {
        report += `**Expertise:**\n`;
        for (const exp of agent.expertise.slice(0, 3)) {
          report += `- ${exp}\n`;
        }
        report += `\n`;
      }

      if (agent.capabilities.length > 0) {
        report += `**Capacidades:**\n`;
        for (const cap of agent.capabilities.slice(0, 5)) {
          report += `- ${cap}\n`;
        }
        report += `\n`;
      }

      report += `---\n\n`;
    }

    report += `## 📋 MATRIZ DE COMANDOS\n\n`;
    report += `| Agente | Comandos | Status |\n`;
    report += `|--------|----------|--------|\n`;
    for (const agent of this.agents) {
      const status = agent.installed ? '✅' : '⏳';
      report += `| **${agent.name}** | ${agent.commandCount} | ${status} |\n`;
    }
    report += `\n`;

    report += `---\n\n`;
    report += `## 🎯 RECOMENDAÇÕES\n\n`;

    const notInstalled = this.agents.filter(a => !a.installed);
    if (notInstalled.length > 0) {
      report += `### **Agentes não instalados (${notInstalled.length}):**\n\n`;
      for (const agent of notInstalled) {
        report += `- **${agent.name}**: ${agent.commandCount} comandos disponíveis\n`;
      }
      report += `\n**Ação:** Instalar em \`~/.claude/agents/\`\n\n`;
    }

    const withoutCommands = this.agents.filter(a => a.commandCount === 0);
    if (withoutCommands.length > 0) {
      report += `### **Agentes sem comandos (${withoutCommands.length}):**\n\n`;
      for (const agent of withoutCommands) {
        report += `- **${agent.name}**: Criar commands.json\n`;
      }
      report += `\n`;
    }

    report += `---\n\n`;
    report += `**Análise completa!** 🎉\n`;
    report += `**Total analisado:** ${totalAgents} agentes, ${totalCommands} comandos\n`;

    return report;
  }

  /**
   * Gera relatório em JSON
   */
  generateJSON() {
    return {
      metadata: {
        timestamp: new Date().toISOString(),
        analyzer: 'HemoDoctorAgentAnalyzer',
        version: '1.0',
      },
      summary: {
        totalAgents: this.agents.length,
        installedAgents: this.agents.filter(a => a.installed).length,
        totalCommands: this.agents.reduce((sum, a) => sum + a.commandCount, 0),
        avgCommandsPerAgent: this.agents.reduce((sum, a) => sum + a.commandCount, 0) / this.agents.length,
      },
      agents: this.agents,
    };
  }
}

// Main execution
async function main() {
  const agentsDir = process.argv[2] || './HEMODOCTOR_AGENTES';

  console.log('🔍 HemoDoctor Agent Analyzer\n');
  console.log(`📂 Analisando: ${agentsDir}\n`);

  const analyzer = new HemoDoctorAgentAnalyzer(agentsDir);

  await analyzer.analyzeAll();

  const report = analyzer.generateReport();
  const json = analyzer.generateJSON();

  // Write Markdown report
  const reportPath = './RELATORIO_ANALISE_AGENTES_HEMODOCTOR.md';
  fs.writeFileSync(reportPath, report);
  console.log(`✅ Relatório Markdown: ${reportPath}`);

  // Write JSON report
  const jsonPath = './RELATORIO_ANALISE_AGENTES_HEMODOCTOR.json';
  fs.writeFileSync(jsonPath, JSON.stringify(json, null, 2));
  console.log(`✅ Relatório JSON: ${jsonPath}`);

  console.log(`\n📊 Resumo:`);
  console.log(`   Total de agentes: ${json.summary.totalAgents}`);
  console.log(`   Agentes instalados: ${json.summary.installedAgents}`);
  console.log(`   Total de comandos: ${json.summary.totalCommands}`);
  console.log(`\n🎉 Análise completa!\n`);
}

if (require.main === module) {
  main().catch(console.error);
}

module.exports = { HemoDoctorAgentAnalyzer };
