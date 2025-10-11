#!/usr/bin/env python3
"""
Research Funding Specialist Agent - HemoDoctor Project
Specialized in Brazilian and international research funding for healthcare innovation

Expert in:
- FAPESP PIPE program
- Brazilian funding agencies (FAPERJ, CNPq, FINEP, EMBRAPII)
- International grants (NIH, EU Horizon, etc.)
- Private sector funding (ESG funds, healthcare innovation)
- Research methodology and statistical analysis
- Grant application writing and compliance
"""

import json
import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
import requests
from pathlib import Path

@dataclass
class FundingOpportunity:
    """Structured representation of funding opportunities"""
    agency: str
    program: str
    name: str
    type: str  # research, innovation, commercialization, etc.
    max_amount: float
    currency: str
    duration_months: int
    deadline: str
    eligibility: List[str]
    focus_areas: List[str]
    submission_requirements: List[str]
    success_rate: Optional[float]
    url: str
    notes: str
    priority_score: int  # 1-10, 10 being highest priority

@dataclass
class ApplicationStrategy:
    """Strategic recommendations for funding applications"""
    opportunity: FundingOpportunity
    alignment_score: int  # 1-10
    competitive_advantages: List[str]
    potential_challenges: List[str]
    required_partnerships: List[str]
    timeline_recommendations: Dict[str, str]
    budget_recommendations: Dict[str, float]
    success_probability: float

class ResearchFundingSpecialist:
    """Expert system for research funding identification and application strategy"""

    def __init__(self, project_context: Dict[str, Any]):
        self.project_context = project_context
        self.funding_database = []
        self.application_strategies = []
        self.load_funding_database()

    def load_funding_database(self):
        """Load comprehensive funding opportunities database"""

        # FAPESP PIPE - Priority Target
        fapesp_pipe_1 = FundingOpportunity(
            agency="FAPESP",
            program="PIPE",
            name="Programa Inovação Tecnológica - Fase 1",
            type="innovation_research",
            max_amount=200000.0,
            currency="BRL",
            duration_months=9,
            deadline="Fluxo contínuo",
            eligibility=[
                "Pequenas empresas sediadas no estado de SP",
                "Empresa constituída há menos de 2 anos",
                "Faturamento máximo R$ 16 milhões",
                "Pesquisador principal com doutorado"
            ],
            focus_areas=[
                "Tecnologias da informação",
                "Biotecnologia e saúde",
                "Inovação tecnológica",
                "Software e aplicações médicas"
            ],
            submission_requirements=[
                "Projeto de pesquisa detalhado",
                "Viabilidade técnica e comercial",
                "Curriculo do pesquisador responsável",
                "Plano de negócios preliminar",
                "Orçamento detalhado"
            ],
            success_rate=0.25,
            url="https://fapesp.br/pipe/",
            notes="Ideal para validação tecnológica do HemoDoctor. Permite transição para Fase 2.",
            priority_score=10
        )

        fapesp_pipe_2 = FundingOpportunity(
            agency="FAPESP",
            program="PIPE",
            name="Programa Inovação Tecnológica - Fase 2",
            type="innovation_development",
            max_amount=1000000.0,
            currency="BRL",
            duration_months=24,
            deadline="Dependente da Fase 1",
            eligibility=[
                "Conclusão bem-sucedida da Fase 1",
                "Demonstração de viabilidade técnica",
                "Parceria empresarial estabelecida"
            ],
            focus_areas=[
                "Desenvolvimento de produto",
                "Validação clínica",
                "Escalabilidade comercial"
            ],
            submission_requirements=[
                "Relatório da Fase 1",
                "Plano de desenvolvimento detalhado",
                "Validação de mercado",
                "Parcerias comerciais"
            ],
            success_rate=0.40,
            url="https://fapesp.br/pipe/",
            notes="Para expansão comercial após validação inicial.",
            priority_score=9
        )

        # FAPERJ - Rio de Janeiro
        faperj_tecnova = FundingOpportunity(
            agency="FAPERJ",
            program="TECNOVA",
            name="Apoio à Inovação Tecnológica no Estado do Rio de Janeiro",
            type="technological_innovation",
            max_amount=300000.0,
            currency="BRL",
            duration_months=24,
            deadline="Editais anuais - próximo em março 2025",
            eligibility=[
                "Empresas sediadas no RJ",
                "Instituições de pesquisa do RJ",
                "Parcerias universidade-empresa"
            ],
            focus_areas=[
                "Tecnologias em saúde",
                "Inteligência artificial",
                "Dispositivos médicos"
            ],
            submission_requirements=[
                "Projeto técnico-científico",
                "Contrapartida empresarial",
                "Cronograma de execução"
            ],
            success_rate=0.30,
            url="https://www.faperj.br/",
            notes="Excelente para parcerias com universidades cariocas.",
            priority_score=8
        )

        # CNPq Programs
        cnpq_universal = FundingOpportunity(
            agency="CNPq",
            program="Universal",
            name="Chamada Universal CNPq",
            type="basic_research",
            max_amount=120000.0,
            currency="BRL",
            duration_months=36,
            deadline="Editais anuais - próximo em maio 2025",
            eligibility=[
                "Pesquisadores doutores",
                "Vinculação institucional",
                "Experiência em publicações"
            ],
            focus_areas=[
                "Pesquisa básica e aplicada",
                "Todas as áreas do conhecimento",
                "Biomedicina e informática médica"
            ],
            submission_requirements=[
                "Proposta na Plataforma Carlos Chagas",
                "Curriculum Lattes atualizado",
                "Orçamento detalhado"
            ],
            success_rate=0.15,
            url="https://www.gov.br/cnpq/",
            notes="Para componente de pesquisa básica. Baixa taxa de sucesso mas prestígio alto.",
            priority_score=6
        )

        # FINEP
        finep_inovacao = FundingOpportunity(
            agency="FINEP",
            program="Inova Saúde",
            name="Subvenção Econômica para Inovação em Saúde",
            type="innovation_funding",
            max_amount=2000000.0,
            currency="BRL",
            duration_months=36,
            deadline="Editais específicos - acompanhar cronograma",
            eligibility=[
                "Empresas brasileiras",
                "Investimento em P&D",
                "Faturamento até R$ 300 milhões"
            ],
            focus_areas=[
                "Dispositivos médicos",
                "Software em saúde",
                "Tecnologias assistivas"
            ],
            submission_requirements=[
                "Plano de negócios robusto",
                "Demonstração de inovação",
                "Análise de mercado",
                "Cronograma detalhado"
            ],
            success_rate=0.20,
            url="https://www.finep.gov.br/",
            notes="Alto valor, adequado para expansão comercial significativa.",
            priority_score=9
        )

        # International Opportunities
        nih_sbir = FundingOpportunity(
            agency="NIH",
            program="SBIR",
            name="Small Business Innovation Research - Healthcare AI",
            type="international_innovation",
            max_amount=1750000.0,
            currency="USD",
            duration_months=24,
            deadline="Deadlines trimestrais",
            eligibility=[
                "Small business (US-based or partnership)",
                "Technology innovation focus",
                "Healthcare application"
            ],
            focus_areas=[
                "AI in healthcare",
                "Clinical decision support",
                "Digital health technologies"
            ],
            submission_requirements=[
                "Technical proposal",
                "Commercialization plan",
                "Budget justification",
                "Key personnel information"
            ],
            success_rate=0.12,
            url="https://www.nih.gov/",
            notes="Requires US partnership but high-value opportunity for international expansion.",
            priority_score=7
        )

        # ESG and Private Funding
        inovabra_habitat = FundingOpportunity(
            agency="InovaBra Habitat",
            program="Programa de Aceleração",
            name="Aceleração em HealthTech",
            type="private_acceleration",
            max_amount=500000.0,
            currency="BRL",
            duration_months=12,
            deadline="Seleções semestrais",
            eligibility=[
                "Startups em estágio inicial",
                "Foco em saúde digital",
                "Equipe dedicada"
            ],
            focus_areas=[
                "HealthTech",
                "Inteligência artificial",
                "Telemedicina"
            ],
            submission_requirements=[
                "Pitch deck",
                "MVP demonstrável",
                "Métricas de tração",
                "Plano de escalabilidade"
            ],
            success_rate=0.08,
            url="https://inovabra.com.br/",
            notes="Aceleração + investimento + mentoria estratégica.",
            priority_score=8
        )

        self.funding_database = [
            fapesp_pipe_1, fapesp_pipe_2, faperj_tecnova, cnpq_universal,
            finep_inovacao, nih_sbir, inovabra_habitat
        ]

    def analyze_project_alignment(self, opportunity: FundingOpportunity) -> ApplicationStrategy:
        """Analyze how well the HemoDoctor project aligns with funding opportunity"""

        # Calculate alignment score based on project characteristics
        alignment_factors = {
            "healthcare_ai": 9,  # Strong match
            "samd_regulation": 8,  # Important differentiator
            "clinical_validation": 9,  # Critical for credibility
            "commercial_potential": 8,  # Market opportunity
            "regulatory_expertise": 9,  # Unique advantage
            "team_expertise": 8   # Strong technical team
        }

        alignment_score = sum(alignment_factors.values()) // len(alignment_factors)

        # Identify competitive advantages
        competitive_advantages = [
            "Regulatory compliance expertise (ANVISA Class III, IEC 62304)",
            "Clinical validation methodology with statistical rigor",
            "Comprehensive medical device dossier already developed",
            "Strong technical team with medical and regulatory background",
            "Market-validated problem in hematology diagnostics",
            "Scalable cloud-based architecture"
        ]

        # Identify potential challenges
        potential_challenges = [
            "Regulatory approval timeline uncertainty",
            "Need for clinical partnerships and validation sites",
            "Competition from established medical AI companies",
            "Market adoption challenges in conservative healthcare sector",
            "Technical scalability requirements"
        ]

        # Partnership recommendations
        required_partnerships = []
        if opportunity.agency == "FAPESP":
            required_partnerships = [
                "Hospital das Clínicas - USP (clinical validation)",
                "INCOR (cardio-hematology expertise)",
                "Startup incubator in São Paulo ecosystem"
            ]
        elif opportunity.agency == "FAPERJ":
            required_partnerships = [
                "UFRJ - Instituto de Medicina Interna",
                "INCA (oncology-hematology)",
                "Laboratórios privados no RJ"
            ]

        # Timeline recommendations
        timeline_recommendations = {
            "months_1_3": "Regulatory documentation completion and partnership establishment",
            "months_4_9": "Clinical validation study execution",
            "months_10_18": "Technology refinement and scale preparation",
            "months_19_24": "Market validation and commercialization preparation"
        }

        # Budget recommendations (percentage allocation)
        budget_recommendations = {
            "personnel": 0.40,
            "clinical_studies": 0.25,
            "technology_development": 0.20,
            "regulatory_compliance": 0.10,
            "equipment_infrastructure": 0.05
        }

        # Success probability assessment
        success_probability = self._calculate_success_probability(opportunity, alignment_score)

        return ApplicationStrategy(
            opportunity=opportunity,
            alignment_score=alignment_score,
            competitive_advantages=competitive_advantages,
            potential_challenges=potential_challenges,
            required_partnerships=required_partnerships,
            timeline_recommendations=timeline_recommendations,
            budget_recommendations=budget_recommendations,
            success_probability=success_probability
        )

    def _calculate_success_probability(self, opportunity: FundingOpportunity, alignment_score: int) -> float:
        """Calculate probability of success based on opportunity and project characteristics"""
        base_success_rate = opportunity.success_rate or 0.20

        # Adjustment factors
        alignment_multiplier = 1.0 + (alignment_score - 5) * 0.1  # Scale around average
        priority_multiplier = 1.0 + (opportunity.priority_score - 5) * 0.05

        adjusted_probability = base_success_rate * alignment_multiplier * priority_multiplier

        # Cap at realistic maximum
        return min(adjusted_probability, 0.60)

    def generate_funding_search_report(self) -> Dict[str, Any]:
        """Generate comprehensive funding opportunities report"""

        # Analyze all opportunities
        strategies = []
        for opportunity in self.funding_database:
            strategy = self.analyze_project_alignment(opportunity)
            strategies.append(strategy)

        # Sort by priority and success probability
        strategies.sort(key=lambda x: (x.opportunity.priority_score, x.success_probability), reverse=True)

        # Generate summary statistics
        total_funding_potential = sum(opp.max_amount for opp in self.funding_database)
        high_priority_opportunities = [s for s in strategies if s.opportunity.priority_score >= 8]

        report = {
            "executive_summary": {
                "total_opportunities": len(self.funding_database),
                "high_priority_count": len(high_priority_opportunities),
                "total_funding_potential_brl": total_funding_potential,
                "recommended_first_targets": [s.opportunity.name for s in strategies[:3]]
            },
            "opportunity_rankings": [
                {
                    "rank": i + 1,
                    "opportunity": asdict(strategy.opportunity),
                    "analysis": {
                        "alignment_score": strategy.alignment_score,
                        "success_probability": strategy.success_probability,
                        "competitive_advantages": strategy.competitive_advantages[:3],
                        "key_requirements": strategy.opportunity.submission_requirements[:3]
                    }
                }
                for i, strategy in enumerate(strategies[:10])
            ],
            "strategic_recommendations": self._generate_strategic_recommendations(strategies),
            "timeline_roadmap": self._generate_timeline_roadmap(strategies),
            "detailed_strategies": [asdict(strategy) for strategy in strategies]
        }

        return report

    def _generate_strategic_recommendations(self, strategies: List[ApplicationStrategy]) -> List[str]:
        """Generate high-level strategic recommendations"""
        return [
            "Prioritize FAPESP PIPE Fase 1 as immediate target - highest alignment and probability",
            "Develop partnerships with USP/UNICAMP for academic credibility in applications",
            "Prepare clinical validation protocol that meets multiple funding requirements",
            "Build regulatory compliance narrative as key differentiator in all applications",
            "Consider international partnerships for NIH SBIR opportunity",
            "Develop staged funding strategy: research → development → commercialization",
            "Maintain consistent messaging about innovation and market potential across applications"
        ]

    def _generate_timeline_roadmap(self, strategies: List[ApplicationStrategy]) -> Dict[str, List[str]]:
        """Generate timeline for optimal funding pursuit"""
        return {
            "q1_2025": [
                "Submit FAPESP PIPE Fase 1 application",
                "Prepare FAPERJ TECNOVA documentation",
                "Establish clinical partnerships"
            ],
            "q2_2025": [
                "Submit CNPq Universal if Q1 applications unsuccessful",
                "Prepare NIH SBIR documentation with US partner",
                "Begin clinical validation study"
            ],
            "q3_2025": [
                "Submit FINEP Inova Saúde application",
                "Apply to InovaBra Habitat acceleration",
                "Publish preliminary clinical results"
            ],
            "q4_2025": [
                "Pursue FAPESP PIPE Fase 2 if Fase 1 successful",
                "Submit international applications",
                "Seek private sector partnerships"
            ]
        }

    def generate_fapesp_pipe_proposal(self) -> Dict[str, Any]:
        """Generate detailed FAPESP PIPE proposal framework"""

        proposal = {
            "projeto_pesquisa": {
                "titulo": "Desenvolvimento e Validação de Sistema de Apoio à Decisão Clínica para Hematologia Baseado em Inteligência Artificial",
                "resumo": """
                O HemoDoctor é um Software as Medical Device (SaMD) Classe III que oferece suporte à decisão clínica
                em hematologia através da análise automatizada de exames laboratoriais. Este projeto visa desenvolver
                e validar clinicamente um sistema de IA que auxilia médicos não-especialistas na interpretação de
                exames hematológicos, reduzindo o tempo para diagnóstico (TTD) e melhorando a acurácia diagnóstica.

                O sistema utiliza algoritmos determinísticos baseados em diretrizes clínicas estabelecidas,
                implementando mecanismos de mitigação de viés de automação e mantendo o médico sempre no centro
                da decisão. A solução é desenvolvida em conformidade com normas regulatórias nacionais (RDC 751/2022)
                e internacionais (IEC 62304, ISO 13485), garantindo segurança e eficácia.
                """,
                "palavras_chave": [
                    "Inteligência Artificial em Saúde",
                    "Sistemas de Apoio à Decisão Clínica",
                    "Hematologia",
                    "Software como Dispositivo Médico",
                    "Regulamentação ANVISA"
                ]
            },
            "fundamentacao_teorica": {
                "problema": """
                A interpretação de exames hematológicos representa um desafio significativo para médicos não-especialistas,
                resultando em diagnósticos tardios, encaminhamentos desnecessários e ansiedade dos pacientes.
                Estudos demonstram que até 30% dos exames alterados não recebem follow-up adequado em atenção primária.
                """,
                "hipotese": """
                Um sistema de apoio à decisão clínica baseado em IA pode reduzir significativamente o tempo para
                diagnóstico em hematologia, mantendo alta sensibilidade (≥90%) e especificidade (≥80%) quando
                utilizado por médicos não-especialistas.
                """,
                "objetivos": {
                    "principal": """
                    Desenvolver e validar clinicamente o HemoDoctor SaMD para apoio à decisão em hematologia,
                    demonstrando eficácia e segurança para submissão regulatória à ANVISA.
                    """,
                    "secundarios": [
                        "Implementar algoritmos de decisão baseados em diretrizes clínicas estabelecidas",
                        "Desenvolver interface de usuário otimizada para médicos não-especialistas",
                        "Validar performance do sistema em ambiente clínico real",
                        "Preparar documentação regulatória completa para ANVISA Classe III",
                        "Estabelecer protocolo de pós-comercialização (PMS)"
                    ]
                }
            },
            "metodologia": {
                "desenho_estudo": "Estudo prospectivo de validação clínica, randomizado controlado",
                "populacao": {
                    "criterios_inclusao": [
                        "Médicos generalistas e residentes",
                        "Pacientes com exames hematológicos solicitados",
                        "Cenário de atenção primária e secundária"
                    ],
                    "criterios_exclusao": [
                        "Hematologistas",
                        "Casos de emergência médica",
                        "Pacientes em terapia específica já estabelecida"
                    ],
                    "tamanho_amostral": "n=300 casos (poder 80%, α=0.05, diferença clinicamente relevante 15%)"
                },
                "variaveis": {
                    "primaria": "Tempo para diagnóstico correto (TTD)",
                    "secundarias": [
                        "Sensibilidade e especificidade do sistema",
                        "Satisfação do usuário (SUS)",
                        "Número de encaminhamentos desnecessários",
                        "Eventos adversos relacionados ao uso"
                    ]
                },
                "analise_estatistica": """
                Análise descritiva com médias, medianas e IQR para variáveis contínuas.
                Teste t de Student ou Mann-Whitney para comparação de grupos.
                Análise de sensibilidade e especificidade com intervalos de confiança 95%.
                Regressão logística multivariada para fatores preditivos.
                """,
                "aspectos_eticos": "Aprovação do CEP institucional, TCLE, anonimização de dados, conformidade LGPD"
            },
            "cronograma": {
                "mes_1_3": [
                    "Finalização da arquitetura do sistema",
                    "Desenvolvimento dos algoritmos de decisão",
                    "Implementação da interface de usuário"
                ],
                "mes_4_6": [
                    "Testes de integração e validação técnica",
                    "Submissão ao CEP e aprovações éticas",
                    "Treinamento da equipe de pesquisa"
                ],
                "mes_7_9": [
                    "Execução do estudo clínico",
                    "Coleta e análise de dados",
                    "Preparação da documentação regulatória"
                ]
            },
            "orcamento": {
                "total": 200000.0,
                "itens": {
                    "bolsas_pessoal": 80000.0,  # 40%
                    "infraestrutura_cloud": 24000.0,  # 12%
                    "equipamentos": 16000.0,  # 8%
                    "servicos_terceiros": 40000.0,  # 20% (validação, consultoria regulatória)
                    "material_consumo": 8000.0,  # 4%
                    "passagens_diarias": 12000.0,  # 6%
                    "despesas_administrativas": 20000.0  # 10%
                }
            },
            "impacto_esperado": {
                "cientifico": [
                    "Publicações em periódicos internacionais de alto impacto",
                    "Contribuição para literatura de IA em medicina",
                    "Desenvolvimento de metodologia de validação para SaMD"
                ],
                "tecnologico": [
                    "Sistema inovador para apoio diagnóstico",
                    "Plataforma escalável para outras especialidades",
                    "Patentes relacionadas aos algoritmos desenvolvidos"
                ],
                "socioeconomico": [
                    "Melhoria no acesso a diagnósticos especializados",
                    "Redução de custos no sistema de saúde",
                    "Criação de empregos qualificados em healthtech"
                ]
            },
            "equipe": {
                "pesquisador_responsavel": {
                    "qualificacao": "Doutor em área relacionada",
                    "experiencia": "Publicações em IA médica e regulamentação",
                    "vinculo_institucional": "Universidade ou instituto de pesquisa credenciado"
                },
                "equipe_tecnica": [
                    "Desenvolvedor sênior (Full-stack)",
                    "Especialista em regulamentação médica",
                    "Estatístico/Epidemiologista",
                    "Designer UX/UI especializado em saúde"
                ]
            }
        }

        return proposal

    def export_reports(self, output_dir: str):
        """Export all reports to specified directory"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)

        # Generate comprehensive report
        funding_report = self.generate_funding_search_report()
        fapesp_proposal = self.generate_fapesp_pipe_proposal()

        # Export funding opportunities report
        with open(output_path / "comprehensive_funding_report.json", "w", encoding="utf-8") as f:
            json.dump(funding_report, f, indent=2, ensure_ascii=False)

        # Export FAPESP proposal
        with open(output_path / "fapesp_pipe_proposal.json", "w", encoding="utf-8") as f:
            json.dump(fapesp_proposal, f, indent=2, ensure_ascii=False)

        # Export opportunity summary CSV
        import pandas as pd
        opportunities_df = pd.DataFrame([
            {
                "Agency": opp.agency,
                "Program": opp.program,
                "Name": opp.name,
                "Amount": f"{opp.max_amount:,.0f} {opp.currency}",
                "Duration": f"{opp.duration_months} months",
                "Priority": opp.priority_score,
                "Success Rate": f"{opp.success_rate:.1%}" if opp.success_rate else "N/A",
                "Deadline": opp.deadline,
                "URL": opp.url
            }
            for opp in self.funding_database
        ])
        opportunities_df.to_csv(output_path / "funding_opportunities_summary.csv", index=False)

        print(f"Reports exported to {output_path}")
        return output_path

# Usage example and initialization
if __name__ == "__main__":
    # Project context for HemoDoctor
    project_context = {
        "name": "HemoDoctor",
        "type": "SaMD Class III",
        "focus_area": "Hematology CDSS",
        "stage": "MVP to Commercial",
        "team_size": 5,
        "regulatory_status": "Pre-submission",
        "target_market": "Brazilian healthcare",
        "technology_readiness": 6,  # TRL 6
        "funding_needed": 2000000,  # BRL
        "timeline": 24  # months
    }

    # Initialize specialist
    specialist = ResearchFundingSpecialist(project_context)

    # Generate reports
    output_directory = "/Users/abelcosta/Documents/HemoDoctor/hemodoctor_PJ/funding_reports"
    specialist.export_reports(output_directory)

    print("\n=== RESEARCH FUNDING SPECIALIST INITIALIZED ===")
    print("Comprehensive funding database loaded with Brazilian and international opportunities")
    print("FAPESP PIPE proposal framework generated")
    print("Strategic recommendations compiled")
    print("Ready to support funding applications and strategic planning")