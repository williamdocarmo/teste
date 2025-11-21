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

# Tópicos por domínio (sem jargões; >= número desejado)
DOMAIN_TOPICS = {
    "programacao": [
        "quebrar problemas grandes em passos menores",
        "criar soluções usando raciocínio lógico",
        "automatizar tarefas repetitivas do dia a dia",
        "transformar uma ideia em algo funcional",
        "persistir até encontrar e corrigir um erro",
        "pesquisar e testar caminhos diferentes para resolver algo",
        "organizar instruções de forma clara para outras pessoas entenderem",
        "aprender novas formas de pensar e resolver problemas",
        "construir pequenas ferramentas para facilitar a rotina",
        "estruturar soluções que possam ser reaproveitadas",
        "pensar em eficiência e fazer mais com menos recursos",
        "manter um estilo claro e consistente nas soluções",
        "colaborar revisando o trabalho de outras pessoas",
        "verificar se uma solução continua funcionando após mudanças",
        "documentar o funcionamento de uma solução",
        "traduzir regras do negócio em regras lógicas",
        "integrar partes diferentes de um sistema",
        "projetar soluções que sejam fáceis de manter",
        "lidar bem com ambiguidade até chegar a uma resposta",
        "refatorar soluções para ficarem mais simples",
    ],
    "infraestrutura": [
        "garantir que serviços fiquem disponíveis o tempo todo",
        "planejar capacidade e crescimento com antecedência",
        "padronizar processos para reduzir erros",
        "observar sinais de saúde e desempenho de serviços",
        "organizar quem pode acessar o quê",
        "resolver incidentes de forma rápida e calma",
        "criar rotinas de cópia e recuperação de informações",
        "otimizar custos de operação sem perder qualidade",
        "preparar ambientes de teste e de produção",
        "automatizar instalações e configurações repetitivas",
        "mapear dependências entre serviços e equipes",
        "trabalhar com registros e monitoramento para entender problemas",
        "atualizar sistemas sem interromper quem usa",
        "pensar em soluções que suportem alto uso",
        "lidar com limitações de tempo e recursos",
        "preparar documentação operacional objetiva",
        "reduzir riscos humanos com automação e padrões",
        "separar ambientes para evitar impactos indesejados",
        "facilitar diagnósticos com bons registros",
        "garantir que mudanças passem por etapas de validação",
    ],
    "seguranca": [
        "imaginar como algo pode falhar ou ser abusado",
        "identificar riscos antes que se tornem problemas",
        "definir regras e controles para reduzir riscos",
        "investigar sinais que indicam incidentes",
        "proteger informações sensíveis e confidenciais",
        "avaliar impacto e probabilidade para priorizar ações",
        "criar hábitos e treinamentos de segurança para pessoas",
        "revisar mudanças com olhar crítico",
        "manter sigilo e ética em situações sensíveis",
        "pensar em camadas de defesa e redundância",
        "responder a incidentes de forma coordenada",
        "analisar comportamentos fora do padrão",
        "preparar checklists e evidências para auditorias",
        "acompanhar notícias e tendências de riscos",
        "garantir acesso apenas ao necessário",
        "incluir segurança desde o início de um projeto",
        "registrar decisões importantes para referência futura",
        "propor melhorias contínuas baseadas em lições aprendidas",
        "questionar suposições que possam abrir brechas",
        "priorizar correções com base em risco real",
    ],
    "dados": [
        "gostar de trabalhar com números e informações",
        "encontrar padrões em grandes quantidades de dados",
        "fazer perguntas e medir as respostas",
        "transformar dados em gráficos e resumos claros",
        "validar se uma conclusão é confiável",
        "testar hipóteses e comparar resultados",
        "comparar cenários para tomar decisões",
        "contar histórias a partir de informações",
        "reunir dados de fontes diferentes",
        "definir métricas com nomes e regras bem claras",
        "cuidar da qualidade e consistência das informações",
        "investigar causas de variações inesperadas",
        "revisar detalhes com atenção e paciência",
        "usar dados para orientar prioridades",
        "estimar resultados futuros com base no passado",
        "documentar a origem dos dados e quem os usa",
        "respeitar privacidade e regras ao analisar informações",
        "simplificar análises complexas para públicos não técnicos",
        "construir painéis que comunicam o essencial",
        "apoiar decisões de negócio com evidências",
    ],
    "design": [
        "entender necessidades reais das pessoas usuárias",
        "valorizar estética simples e funcional",
        "prototipar ideias rapidamente no papel ou ferramenta",
        "organizar telas e fluxos de forma clara",
        "escrever textos curtos que orientam",
        "testar com pessoas e melhorar a cada ciclo",
        "manter consistência visual entre telas",
        "pensar em acessibilidade para diferentes públicos",
        "adaptar a experiência para celular e computador",
        "usar feedback de pessoas usuárias como principal guia",
        "desenhar jornadas do início ao fim",
        "colaborar com produto e engenharia",
        "criar componentes reutilizáveis",
        "priorizar clareza sobre decoração",
        "medir satisfação e esforço das pessoas usuárias",
        "explicar decisões de design com argumentos simples",
        "reduzir atrito em tarefas repetidas",
        "evitar sobrecarga de informação nas telas",
        "definir hierarquia visual para orientar a leitura",
        "pensar no estado vazio e mensagens de erro",
    ],
    "games": [
        "imaginar regras e mecânicas divertidas",
        "equilibrar dificuldade e progressão",
        "criar experiências que prendem atenção",
        "experimentar protótipos rapidamente",
        "ajustar feedbacks visuais e sonoros",
        "pensar em histórias e personagens marcantes",
        "analisar por que um jogo é divertido",
        "buscar sensação de fluidez durante a experiência",
        "trabalhar com ideias abstratas e criatividade",
        "equilibrar risco e recompensa para motivar",
        "projetar níveis interessantes",
        "considerar experiências para jogar junto",
        "planejar novidades por temporadas ou eventos",
        "acompanhar tendências do mercado de jogos",
        "pensar em monetização justa e ética",
        "lidar com comunidade e feedback após o lançamento",
        "refinar controles para que sejam naturais",
        "criar desafios que ensinam sem frustrar",
        "medir engajamento e melhorar com base nos dados",
        "inovar em mecânicas mesmo com limitações",
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
