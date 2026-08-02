# Inteligência Artificial

## O que é Inteligência Artificial?

Inteligência Artificial (IA) refere-se à simulação da inteligência humana em máquinas programadas para pensar, aprender e resolver problemas. Sistemas de IA podem executar tarefas que normalmente exigem inteligência humana, como reconhecer fala, tomar decisões, traduzir idiomas e identificar objetos em imagens. O termo foi cunhado por John McCarthy em 1956, na Conferência de Dartmouth, amplamente considerada o evento fundador da IA como campo de estudo.

A IA moderna é amplamente dividida em IA Restrita (também chamada de IA Fraca), projetada para tarefas específicas, e a teórica Inteligência Artificial Geral (AGI), que igualaria ou superaria a capacidade cognitiva humana em todos os domínios. Todos os sistemas de IA atuais são IA Restrita.

## História da IA

A história da IA abrange quase oito décadas. As primeiras bases teóricas foram estabelecidas por Alan Turing, cujo artigo de 1950, "Computing Machinery and Intelligence", introduziu o Teste de Turing — uma medida da capacidade de uma máquina exibir comportamento inteligente indistinguível do de um ser humano. A Conferência de Dartmouth de 1956 estabeleceu formalmente a IA como disciplina acadêmica.

As décadas de 1950–1970 viram programas iniciais otimistas como ELIZA (um chatbot simples) e LISP (uma linguagem de programação criada para IA). Os "invernos da IA" das décadas de 1970 e 1980 foram períodos de redução de financiamento e interesse após expectativas não atendidas. Um ressurgimento nos anos 1980 veio com os sistemas especialistas — programas baseados em regras que codificavam conhecimento humano especializado. Os anos 2000 trouxeram avanços em aprendizado de máquina impulsionados pela internet e pelo crescimento dos conjuntos de dados. Os anos 2010 testemunharam a ascensão do aprendizado profundo, transformando visão computacional, processamento de linguagem natural (NLP) e aprendizado por reforço.

## Aprendizado de Máquina

Aprendizado de Máquina (ML) é um subconjunto da IA que permite aos sistemas aprender com dados sem serem explicitamente programados. As principais categorias de ML incluem:

**Aprendizado Supervisionado**: O modelo é treinado com pares de entrada e saída rotulados. Exemplos incluem detecção de spam e classificação de imagens. Os algoritmos incluem regressão linear, árvores de decisão, máquinas de vetores de suporte e redes neurais.

**Aprendizado Não Supervisionado**: O modelo encontra padrões em dados não rotulados. Exemplos incluem segmentação de clientes e detecção de anomalias. Os algoritmos incluem agrupamento k-means e análise de componentes principais (PCA).

**Aprendizado por Reforço**: Um agente aprende interagindo com um ambiente, recebendo recompensas ou penalidades. É usado em IA para jogos (AlphaGo, AlphaZero), robótica e sistemas de recomendação.

**Aprendizado Semi-Supervisionado e Auto-Supervisionado**: Combinam pequenas quantidades de dados rotulados com grandes conjuntos de dados não rotulados. Os modelos GPT usam uma abordagem auto-supervisionada durante o pré-treinamento.

## Aprendizado Profundo

Aprendizado Profundo é um subconjunto do aprendizado de máquina que utiliza redes neurais artificiais com muitas camadas (redes profundas). Inspiradas de forma aproximada na estrutura neural do cérebro, essas redes aprendem representações hierárquicas dos dados. O aprendizado profundo impulsiona:

- **Visão Computacional**: Reconhecimento de imagens, detecção de objetos, imagens médicas
- **Processamento de Linguagem Natural**: Tradução automática, análise de sentimento, resposta a perguntas
- **Reconhecimento de Fala**: Assistentes de voz como Siri, Alexa, Google Assistant
- **IA Generativa**: Geração de imagens (DALL-E, Stable Diffusion), geração de texto (GPT)

As principais arquiteturas de aprendizado profundo incluem redes neurais convolucionais (CNNs) para imagens, redes neurais recorrentes (RNNs) e LSTMs para sequências, transformers para linguagem e redes adversariais generativas (GANs) para síntese.

## Modelos de Linguagem de Grande Escala (LLMs)

Modelos de Linguagem de Grande Escala (LLMs) são sistemas de IA treinados com enormes quantidades de dados textuais para compreender e gerar linguagem humana. Eles são baseados na arquitetura Transformer, introduzida no artigo de 2017 "Attention is All You Need", de Vaswani et al. Os LLMs preveem o próximo token (parte de palavra) em uma sequência, o que lhes permite gerar texto coerente, responder perguntas, escrever código e realizar tarefas de raciocínio.

LLMs de destaque incluem:
- **Série GPT** (OpenAI): GPT-3, GPT-4 e sucessores — amplamente usados para conversa e código
- **Claude** (Anthropic): Focado em segurança e utilidade
- **Gemini** (Google DeepMind): Multimodal, integrando texto, imagens e código
- **LLaMA / Llama 3** (Meta): Modelos com pesos abertos para pesquisa e implantação local
- **Mistral** (Mistral AI): Modelos abertos eficientes e competitivos com LLMs muito maiores

Os LLMs são treinados em duas etapas: pré-treinamento (não supervisionado em grandes corpus de texto) e ajuste fino (supervisionado ou por aprendizado por reforço a partir de feedback humano, RLHF). Janelas de contexto descrevem quanto texto um LLM pode processar de uma só vez, variando de 4 mil tokens (GPT-3 inicial) a mais de 1 milhão de tokens nos modelos mais avançados de 2026.

## Ética e Segurança em IA

A IA levanta questões éticas importantes, incluindo viés, privacidade, deslocamento de empregos e o risco de uso indevido. O viés algorítmico ocorre quando os dados de treinamento refletem desigualdades históricas, fazendo com que sistemas de IA produzam resultados discriminatórios. Sistemas de reconhecimento facial mostraram taxas de erro mais altas para pessoas de pele mais escura. Algoritmos de contratação já demonstraram favorecer candidatos homens.

A segurança em IA é o campo dedicado a garantir que sistemas de IA se comportem como pretendido, sem causar danos não intencionais. As principais preocupações incluem:
- **Alinhamento**: Garantir que os objetivos da IA correspondam aos valores humanos
- **Interpretabilidade / Explicabilidade**: Entender por que uma IA tomou uma decisão (crítico em medicina, direito e finanças)
- **Uso indevido**: Deepfakes gerados por IA, desinformação, ciberataques
- **Risco existencial**: Preocupação teórica de que uma futura AGI possa perseguir objetivos desalinhados com a sobrevivência humana

Organizações que trabalham com segurança em IA incluem a equipe de Safety da OpenAI, a Anthropic (fundada por ex-pesquisadores de segurança da OpenAI), a equipe de segurança da DeepMind e institutos independentes como MIRI e ARC.

## IA na Sociedade

A IA está transformando quase todos os setores:

- **Saúde**: A IA auxilia no diagnóstico de câncer a partir de imagens médicas, na previsão de desfechos de pacientes, na aceleração da descoberta de medicamentos (o AlphaFold resolveu a previsão da estrutura de dobramento de proteínas) e na personalização de planos de tratamento.
- **Finanças**: Detecção de fraudes, negociação algorítmica, pontuação de crédito e robo-advisors usam modelos de ML.
- **Transporte**: Veículos autônomos usam visão computacional, lidar e aprendizado por reforço. Tesla Autopilot, Waymo e Cruise estão entre os principais esforços.
- **Educação**: Plataformas de aprendizagem personalizada adaptam o conteúdo ao ritmo e ao estilo de aprendizagem de cada estudante.
- **Campos criativos**: A IA gera música, arte e escrita; ferramentas como Midjourney, DALL-E e GitHub Copilot mudaram os fluxos de trabalho criativos.
- **Cibersegurança**: A IA detecta anomalias, identifica ameaças e potencializa tanto ataques quanto defesas.

## Robótica e IA Incorporada

A robótica combina IA com máquinas físicas. Robôs modernos usam percepção (câmeras, lidar), planejamento e controle para navegar e manipular ambientes. O Atlas, da Boston Dynamics, demonstra movimento bípede avançado. Robôs industriais de empresas como ABB e FANUC automatizam a manufatura. Robôs domésticos (Roomba) e robôs cirúrgicos (da Vinci System) aplicam IA em contextos cotidianos e médicos. A pesquisa em IA incorporada concentra-se em agentes que aprendem habilidades físicas por meio da interação com o mundo, reduzindo a distância entre ambientes simulados e reais.

## Tendências Atuais em IA (anos 2020)

- **IA multimodal**: Sistemas que processam texto, imagens, áudio e vídeo em conjunto (GPT-4V, Gemini)
- **Agentes e IA agêntica**: LLMs que podem usar ferramentas, navegar na web, escrever código e realizar ações em múltiplas etapas (Operator da OpenAI, Computer Use da Anthropic)
- **Modelos com pesos abertos**: O LLaMA da Meta democratizou o acesso a grandes modelos para pesquisadores
- **IA no dispositivo**: Execução local de modelos de IA em celulares e laptops sem conectividade com a nuvem (Apple Intelligence, NPUs da Qualcomm)
- **Regulação da IA**: O EU AI Act (2026) é a primeira lei abrangente de IA do mundo, classificando sistemas de IA por nível de risco
