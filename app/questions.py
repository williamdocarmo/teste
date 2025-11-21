# Rótulos de categorias (PT)
DOMAIN_LABELS_PT = {
    "programacao": "Programação",
    "infraestrutura": "Infraestrutura",
    "seguranca": "Segurança",
    "dados": "Dados",
    "design": "Design",
    "games": "Games",
}

PERSONA_LABELS_PT = {
    "analista": "Analista (tendência a Dados/IA)",
    "construtor": "Construtor (Infra/Sec)",
    "inovador": "Inovador (Programação/Games)",
    "comunicador": "Comunicador (UX/Produto)",
}

# Mapeamento de persona dominante por domínio
DOMAIN_PERSONA = {
    "programacao": "inovador",
    "infraestrutura": "construtor",
    "seguranca": "construtor",
    "dados": "analista",
    "design": "comunicador",
    "games": "inovador",
}

# Alocação alvo de perguntas por domínio (soma = 100)
DOMAIN_COUNTS = {
    "programacao": 17,
    "infraestrutura": 17,
    "seguranca": 17,
    "dados": 17,
    "design": 16,
    "games": 16,
}

# Tópicos por domínio (>= número desejado)
DOMAIN_TOPICS = {
    "programacao": [
        "transformar ideias em aplicativos ou sites",
        "resolver desafios lógicos com código",
        "aprender frameworks web (React, Vue, Angular)",
        "aprender frameworks backend (Django, Spring, .NET)",
        "integrar APIs REST e GraphQL",
        "automatizar tarefas com scripts",
        "escrever testes automatizados e praticar TDD",
        "adotar boas práticas de código limpo",
        "versionar projetos com Git e GitHub",
        "otimizar performance de aplicações",
        "modelar bancos de dados para aplicações",
        "programação orientada a objetos (POO)",
        "conceitos de programação funcional",
        "arquitetura de software (hexagonal, microserviços)",
        "escrever documentação técnica clara",
        "participar de code reviews e pair programming",
        "construir CLIs e utilitários de linha de comando",
        "arquitetar APIs escaláveis",
        "aprender testes de integração e contrato",
        "automatizar builds e releases"
    ],
    "infraestrutura": [
        "dominar sistemas operacionais, especialmente Linux",
        "operar serviços de nuvem (AWS/Azure/GCP)",
        "configurar redes, DNS e firewalls",
        "trabalhar com containers (Docker)",
        "orquestrar serviços com Kubernetes",
        "provisionar com Terraform (IaC)",
        "automatizar com Ansible",
        "observabilidade: logs, métricas e traces",
        "monitorar disponibilidade e custos",
        "planejar escalabilidade e alta disponibilidade",
        "backup e recuperação de desastres (DR)",
        "armazenamento e file systems",
        "balanceadores de carga e proxies reversos",
        "padronizar pipelines CI/CD",
        "políticas de segurança e conformidade na nuvem",
        "autenticação/SSO e federação",
        "gestão de identidades e permissões (IAM)",
        "otimizar custos (FinOps)",
        "infra como código reutilizável (módulos)",
        "planejamento de capacidade"
    ],
    "seguranca": [
        "ethical hacking e pensamento ofensivo",
        "políticas de identidade e acesso (IAM)",
        "conformidade e políticas de segurança",
        "testes de penetração e análise de vulnerabilidades",
        "resposta a incidentes (IR)",
        "acompanhar CVEs, exploits e patches",
        "criptografia aplicada no dia a dia",
        "modelagem de ameaças (threat modeling)",
        "security by design em projetos",
        "segurança de APIs e microserviços",
        "segurança em cloud (CSPM, CWPP, CIEM)",
        "análise de logs de segurança e SIEM",
        "hardening de sistemas e endpoints",
        "detecção e resposta (EDR/XDR)",
        "campanhas de phishing e awareness",
        "princípios de Zero Trust",
        "segurança de containers e Kubernetes",
        "segurança de dados (DLP, classificação)",
        "segurança em pipelines CI/CD",
        "gestão de vulnerabilidades contínua"
    ],
    "dados": [
        "analisar dados para apoiar decisões",
        "escrever consultas SQL eficazes",
        "criar visualizações e dashboards",
        "aplicar machine learning clássico (scikit-learn)",
        "engenharia de dados e pipelines ETL/ELT",
        "limpar e preparar dados (data wrangling)",
        "experimentação e testes A/B",
        "definir métricas e KPIs",
        "data storytelling e comunicação",
        "big data em nuvem (BigQuery, Redshift, Databricks)",
        "trabalhar com notebooks (Jupyter)",
        "feature engineering e seleção de variáveis",
        "introdução a MLOps",
        "governança e qualidade de dados",
        "modelos preditivos aplicados ao negócio",
        "estatística aplicada para análise",
        "IA generativa com LLMs e embeddings",
        "coleta e ingestão de dados em tempo real (streaming)",
        "privacidade e compliance de dados",
        "documentação de dados (data catalog)"
    ],
    "design": [
        "pesquisa com usuários (UX research)",
        "UI design e hierarquia visual",
        "prototipação com Figma",
        "microcopy e UX writing",
        "design systems e componentes",
        "acessibilidade (a11y)",
        "testes de usabilidade",
        "wireframes de baixa fidelidade",
        "arquitetura da informação e navegação",
        "heurísticas de Nielsen e boas práticas",
        "motion design leve",
        "design responsivo (mobile-first)",
        "handoff para desenvolvimento",
        "métricas de UX (NPS, SUS)",
        "definição de personas e jornadas",
        "design de onboarding e empty states",
        "mapas de calor e análise comportamental",
        "design inclusivo e internacionalização",
        "bibliotecas de ícones e tipografia",
        "documentação de guidelines"
    ],
    "games": [
        "criar jogos e mecânicas envolventes",
        "usar a engine Unity",
        "usar a engine Unreal",
        "level design e balanceamento",
        "programar física, IA e comportamento de NPCs",
        "otimização gráfica e FPS",
        "trilha sonora e efeitos de áudio",
        "publicação e monetização de jogos",
        "roteiros e narrativa interativa",
        "multiplayer e redes para jogos",
        "economia de jogo (currencies, progressão)",
        "ferramentas e editores internos (tools)",
        "shaders e pipelines gráficos",
        "game analytics e telemetria",
        "prototipagem rápida (game jams)",
        "UX de jogos e acessibilidade",
        "mercado de games e tendências",
        "portabilidade para consoles e mobile",
        "otimização de build e assets",
        "suporte pós-lançamento e balanceamento contínuo"
    ],
}

# Frases-base para variar a redação
PREFIXES = [
    "Tenho interesse em {}.",
    "Gosto de {}.",
    "Me motiva {}.",
    "Quero aprender mais sobre {}.",
    "Tenho curiosidade em {}.",
    "Aprecio {}.",
    "Me atrai {}.",
    "Pretendo praticar {}.",
]

def _make_questions():
    questions = []
    next_id = 1
    for domain, count in DOMAIN_COUNTS.items():
        topics = DOMAIN_TOPICS[domain]
        if len(topics) < count:
            raise ValueError(f"Domínio '{domain}' precisa de pelo menos {count} tópicos; tem {len(topics)}.")
        # usar primeiros 'count' tópicos
        for i in range(count):
            topic = topics[i]
            prefix = PREFIXES[i % len(PREFIXES)]
            text = prefix.format(topic)
            questions.append({
                "id": next_id,
                "text": text[0].upper() + text[1:],  # capitalizar
                "domain": domain,
                "persona": DOMAIN_PERSONA[domain],
            })
            next_id += 1
    # garantir 100 perguntas
    assert len(questions) == 100, f"Esperado 100 perguntas, obtido {len(questions)}"
    return questions

QUESTIONS = _make_questions()
