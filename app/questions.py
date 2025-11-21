# Rótulos
DOMAIN_LABELS_PT = {
    "programacao": "Programação",
    "infraestrutura": "Infraestrutura",
    "seguranca": "Segurança",
    "dados": "Dados",
    "design": "Design",
    "games": "Games",
}

PERSONA_LABELS_PT = {
    "analista": "Analista (Dados/IA)",
    "construtor": "Construtor (Infra/Sec)",
    "inovador": "Inovador (Criação/Programação)",
    "comunicador": "Comunicador (UX/Produto)",
}

DOMAIN_PERSONA = {
    "programacao": "inovador",
    "infraestrutura": "construtor",
    "seguranca": "construtor",
    "dados": "analista",
    "design": "comunicador",
    "games": "inovador",
}

# 25 por domínio = 150 total
DOMAIN_COUNTS = {
    "programacao": 25,
    "infraestrutura": 25,
    "seguranca": 25,
    "dados": 25,
    "design": 25,
    "games": 25,
}

DOMAIN_ITEMS = {
    "programacao": [
        "Eu me animo em criar algo do zero que funcione na tela.",
        "Gosto de resolver quebra-cabeças lógicos passo a passo.",
        "Sinto satisfação em automatizar tarefas repetitivas.",
        "Curto transformar ideias em funcionalidades concretas.",
        "Tenho paciência para tentar diferentes soluções quando algo não funciona.",
        "Gosto de melhorar algo para ficar mais rápido e eficiente.",
        "Acho divertido organizar um problema em pequenas partes.",
        "Gosto de ver testes passando e sentir que tudo está no lugar.",
        "Prefiro atividades que exigem lógica e criatividade ao mesmo tempo.",
        "Me interesso em entender por que um erro aconteceu e corrigi-lo.",
        "Gosto de estruturar meu trabalho em pequenas funções bem definidas.",
        "Curto revisar meu próprio trabalho e melhorar a qualidade dele.",
        "Me empolgo com desafios que pedem persistência.",
        "Gosto de seguir padrões e boas práticas quando crio algo.",
        "Sinto prazer em ver algo que construí funcionando para outras pessoas.",
        "Gosto de explicar como uma solução foi estruturada.",
        "Tenho interesse em aprender diferentes formas de resolver o mesmo problema.",
        "Gosto de combinar diferentes peças para formar um sistema completo.",
        "Me atrai a ideia de deixar um projeto bem organizado.",
        "Tenho curiosidade em comparar abordagens para um mesmo desafio.",
        "Gosto de transformar regras em passos claros e executáveis.",
        "Me agrada desmontar soluções grandes e montar de novo de forma melhor.",
        "Curto criar pequenos projetos para praticar e aprender.",
        "Gosto de comparar soluções e escolher a mais simples.",
        "Me anima ver progresso constante em tarefas longas."
    ],
    "infraestrutura": [
        "Gosto de garantir que serviços estejam sempre disponíveis para todos.",
        "Me agrada entender como várias partes se conectam nos bastidores.",
        "Curto investigar problemas de conexão e disponibilidade.",
        "Gosto de planejar como um sistema pode crescer sem quebrar.",
        "Prefiro rotinas com padronização e documentação clara.",
        "Me sinto bem criando rotinas que tornam operações mais estáveis.",
        "Gosto de acompanhar indicadores de saúde de um sistema.",
        "Tenho paciência para descobrir a causa raiz de falhas.",
        "Curto trabalhar com ambientes que exigem confiabilidade.",
        "Gosto de pensar em como recuperar um serviço rapidamente após um problema.",
        "Me interesso por organizar rotinas de cópias de segurança.",
        "Curto lidar com linha de comando e sistemas operacionais.",
        "Gosto de prever capacidade para evitar gargalos.",
        "Curto padronizar formas de instalar e publicar serviços.",
        "Gosto de tornar o trabalho repetitivo automatizado.",
        "Me preocupo em manter custos e recursos sob controle.",
        "Curto separar ambientes de testes e produção para evitar riscos.",
        "Gosto de criar checklists e seguir procedimentos para estabilidade.",
        "Sinto satisfação quando tudo roda sem surpresas.",
        "Curto diagnosticar lentidão e melhorar o desempenho.",
        "Gosto de organizar um plano de mudança com etapas seguras.",
        "Curto medir consumo para evitar desperdícios.",
        "Gosto de padronizar nomes e estruturas para facilitar suporte.",
        "Me anima quando um sistema volta rápido após falha.",
        "Prefiro rotinas previsíveis e confiáveis a improvisos."
    ],
    "seguranca": [
        "Tenho curiosidade sobre como alguém poderia burlar um sistema.",
        "Gosto de pensar em formas de proteger contas e informações.",
        "Me interesso em seguir regras e políticas para manter tudo seguro.",
        "Curto procurar pontos fracos antes que outras pessoas os encontrem.",
        "Gosto de investigar sinais de atividades suspeitas.",
        "Me preocupo com privacidade e uso correto de informações.",
        "Curto analisar riscos e propor medidas de proteção.",
        "Gosto de revisar acessos e garantir que só o necessário está liberado.",
        "Tenho interesse em criar hábitos seguros no dia a dia.",
        "Curto simular cenários de ataque para aprender a defender.",
        "Gosto de documentar orientações para evitar incidentes.",
        "Me atento aos detalhes quando se trata de proteção.",
        "Curto avaliar o impacto de um problema e como responder rapidamente.",
        "Gosto de pensar em segurança desde o início de um projeto.",
        "Me interesso em checar se regras e controles estão funcionando.",
        "Curto ensinar outras pessoas a usar a tecnologia com segurança.",
        "Gosto de manter auditorias organizadas para comprovar conformidade.",
        "Me atrai investigar a origem de um incidente.",
        "Curto comparar alternativas de proteção e escolher a mais adequada.",
        "Gosto de revisar regularmente se há pontos de melhoria na proteção.",
        "Gosto de verificar se as pessoas têm apenas o acesso necessário.",
        "Me interessa mapear o que é mais crítico para proteger primeiro.",
        "Curto revisar configurações em busca de brechas.",
        "Gosto de criar checklists para evitar erros humanos.",
        "Me anima reduzir riscos de forma prática e contínua."
    ],
    "dados": [
        "Gosto de descobrir padrões e histórias escondidas em números.",
        "Me interesso por criar gráficos que expliquem uma situação.",
        "Curto responder perguntas usando evidências e dados.",
        "Gosto de organizar informações bagunçadas até fazerem sentido.",
        "Tenho curiosidade em testar hipóteses e ver o que os dados mostram.",
        "Curto medir impacto e comparar resultados de antes e depois.",
        "Gosto de explicar descobertas de forma simples para qualquer pessoa.",
        "Me agrada trabalhar com tabelas e planilhas.",
        "Curto explorar diferentes formas de visualizar um mesmo conjunto de dados.",
        "Gosto de buscar a causa principal por trás de um comportamento.",
        "Tenho interesse em aprender como máquinas podem reconhecer padrões.",
        "Curto avaliar a qualidade das informações antes de tomar decisões.",
        "Gosto de transformar perguntas vagas em métricas claras.",
        "Me interesso por processos para coletar e organizar informações.",
        "Curto experimentar modelos e comparar desempenho.",
        "Gosto de avaliar riscos e incertezas usando probabilidades.",
        "Me anima trabalhar com dados do mundo real, mesmo que imperfeitos.",
        "Curto acompanhar indicadores ao longo do tempo.",
        "Gosto de ver quando uma análise muda uma decisão importante.",
        "Tenho paciência para revisar dados até ter confiança no resultado.",
        "Curto criar resumos que mostram o essencial sem exageros.",
        "Gosto de validar dados antes de confiar neles.",
        "Me anima converter perguntas abertas em análises objetivas.",
        "Curto separar sinal de ruído em informações confusas.",
        "Gosto de escolher gráficos que comuniquem a mensagem com clareza."
    ],
    "design": [
        "Gosto de entender a necessidade das pessoas antes de propor soluções.",
        "Me agrada criar telas bonitas e fáceis de usar.",
        "Curto transformar ideias em protótipos rápidos para testar.",
        "Gosto de escrever textos curtos e claros dentro de uma interface.",
        "Me interesso por manter consistência visual entre diferentes telas.",
        "Curto garantir que qualquer pessoa consiga usar, inclusive com limitações.",
        "Gosto de observar como as pessoas interagem e aprender com isso.",
        "Me anima organizar componentes reutilizáveis para ganhar velocidade.",
        "Curto alinhar estética e funcionalidade no mesmo projeto.",
        "Gosto de validar ideias com testes simples e feedback real.",
        "Me interesso por tipografia e uso de espaço em tela.",
        "Curto pensar no primeiro contato do usuário com o produto.",
        "Gosto de simplificar fluxos complexos em passos claros.",
        "Me agrada documentar decisões para outras pessoas seguirem.",
        "Curto criar experiências consistentes em diferentes dispositivos.",
        "Gosto de equilibrar requisitos do negócio e necessidades do usuário.",
        "Me interesso por tornar interfaces inclusivas e acessíveis.",
        "Curto organizar bibliotecas visuais e guias de estilo.",
        "Gosto de dar nomes claros para botões e seções.",
        "Me anima ver pessoas usando o que eu desenhei.",
        "Gosto de criar padrões visuais que outras pessoas possam reutilizar.",
        "Me anima reduzir cliques e passos desnecessários.",
        "Curto identificar pontos de atrito e simplificar.",
        "Gosto de ajustar espaçamentos e alinhamentos para dar conforto.",
        "Me interesso por escrever mensagens de erro empáticas e úteis."
    ],
    "games": [
        "Gosto de imaginar mecânicas de jogo e regras divertidas.",
        "Me agrada pensar em desafios que evoluem de forma justa.",
        "Curto prototipar rapidamente uma ideia e testar com amigos.",
        "Gosto de criar histórias, personagens e mundos.",
        "Me interesso por equilibrar dificuldade e sensação de progresso.",
        "Curto ajustar elementos para que o jogo seja fluido.",
        "Gosto de pensar em comportamentos de personagens controlados pelo computador.",
        "Me anima criar efeitos visuais e sonoros que aumentam a imersão.",
        "Curto coletar feedback de jogadores e melhorar a experiência.",
        "Gosto de pensar em como jogar com outras pessoas online ou localmente.",
        "Me interesso por recompensas e sistemas de progressão.",
        "Curto planejar fases e caminhos alternativos.",
        "Gosto de otimizar para que o jogo rode bem em diferentes dispositivos.",
        "Me anima publicar algo e ver outras pessoas jogando.",
        "Curto manter e balancear o jogo após o lançamento.",
        "Gosto de estudar por que certos jogos prendem a atenção.",
        "Me interesso por pequenos projetos criativos feitos em pouco tempo.",
        "Curto organizar recursos de arte, som e lógica para ficarem leves.",
        "Gosto de combinar narrativa e mecânicas para criar emoções.",
        "Me agrada trabalhar em equipe para dar vida a um jogo.",
        "Gosto de testar jogabilidade até ficar natural.",
        "Me anima criar desafios que ensinam as regras jogando.",
        "Curto equilibrar sorte e habilidade para manter a graça.",
        "Gosto de pensar em recompensas que motivam sem exageros.",
        "Me interesso por construir comunidades em torno de um jogo."
    ],
}

def _make_questions():
    questions = []
    next_id = 1
    for domain, n in DOMAIN_COUNTS.items():
        items = DOMAIN_ITEMS[domain]
        if len(items) < n:
            raise ValueError(f"Domínio {domain} precisa de pelo menos {n} afirmações; tem {len(items)}.")
        for i in range(n):
            text = items[i]
            questions.append({
                "id": next_id,
                "text": text,
                "domain": domain,
                "persona": DOMAIN_PERSONA[domain],
            })
            next_id += 1
    assert len(questions) == 150, f"Esperado 150 perguntas, obtido {len(questions)}"
    return questions

QUESTIONS = _make_questions()
