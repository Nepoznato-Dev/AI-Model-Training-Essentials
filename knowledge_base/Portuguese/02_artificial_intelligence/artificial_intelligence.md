# Inteligência Artificial

## O que é Inteligência Artificial?

Inteligência Artificial (IA) refere-se à simulação da inteligência humana em máquinas programadas para pensar, aprender e resolver problemas. Sistemas de IA podem executar tarefas que normalmente exigem inteligência humana, como reconhecer fala, tomar decisões, traduzir idiomas e identificar objetos em imagens. O termo foi cunhado por John McCarthy em 1956 na Conferência de Dartmouth, amplamente considerada o evento fundador da IA como campo de estudo.

A IA moderna é amplamente dividida em IA Restrita (também chamada de IA Fraca), projetada para tarefas específicas, e a teórica Inteligência Artificial Geral (AGI), que igualaria ou superaria a capacidade cognitiva humana em todos os domínios. Todos os sistemas de IA atuais são IA Restrita.

## História da IA

A história da IA abrange quase oito décadas. Os primeiros fundamentos teóricos foram estabelecidos por Alan Turing, cujo artigo de 1950, "Computing Machinery and Intelligence", apresentou o Teste de Turing — uma medida da capacidade de uma máquina de exibir um comportamento inteligente indistinguível do de um ser humano. A Conferência de Dartmouth de 1956 estabeleceu formalmente a IA como uma disciplina acadêmica.

As décadas de 1950 a 1970 viram programas iniciais otimistas como ELIZA (um chatbot simples) e LISP (uma linguagem de programação projetada para IA). Os "invernos da IA" das décadas de 1970 e 1980 foram períodos de redução de financiamento e interesse após expectativas não atendidas. Um ressurgimento nos anos 1980 veio com os sistemas especialistas — programas baseados em regras que codificavam conhecimento humano especializado. Os anos 2000 trouxeram avanços em aprendizado de máquina impulsionados pela internet e por conjuntos de dados crescentes. A década de 2010 marcou a ascensão do deep learning, transformando visão computacional, processamento de linguagem natural (NLP) e aprendizado por reforço.

## Aprendizado de Máquina

Aprendizado de Máquina (ML) é um subconjunto da IA que permite que sistemas aprendam com dados sem serem explicitamente programados. As principais categorias de ML incluem:

**Aprendizado Supervisionado**: O modelo é treinado com pares rotulados de entrada e saída. Exemplos incluem detecção de spam e classificação de imagens. Os algoritmos incluem regressão linear, árvores de decisão, support vector machines e redes neurais.

**Aprendizado Não Supervisionado**: O modelo encontra padrões em dados não rotulados. Exemplos incluem segmentação de clientes e detecção de anomalias. Os algoritmos incluem clustering k-means e análise de componentes principais (PCA).

**Aprendizado por Reforço**: Um agente aprende ao interagir com um ambiente, recebendo recompensas ou penalidades. É usado em IA para jogos (AlphaGo, AlphaZero), robótica e sistemas de recomendação.

**Aprendizado Semissupervisionado e Autossupervisionado**: Combina pequenas quantidades de dados rotulados com grandes conjuntos de dados não rotulados. Modelos GPT usam uma abordagem autossupervisionada durante o pré-treinamento.

## Deep Learning

Deep Learning é um subconjunto do aprendizado de máquina que usa redes neurais artificiais com muitas camadas (redes profundas). Inspiradas de forma livre na estrutura neural do cérebro, essas redes aprendem representações hierárquicas dos dados. O deep learning impulsiona:

- **Visão Computacional**: Reconhecimento de imagens, detecção de objetos, imagens médicas
- **Processamento de Linguagem Natural**: Tradução automática, análise de sentimento, resposta a perguntas
- **Reconhecimento de Fala**: Assistentes de voz como Siri, Alexa e Google Assistant
- **IA Generativa**: Geração de imagens (DALL-E, Stable Diffusion), geração de texto (GPT)

As principais arquiteturas de deep learning incluem redes neurais convolucionais (CNNs) para imagens, redes neurais recorrentes (RNNs) e LSTMs para sequências, transformers para linguagem e generative adversarial networks (GANs) para síntese.

## Large Language Models (LLMs)

Large Language Models (LLMs) são sistemas de IA treinados em enormes volumes de dados textuais para compreender e gerar linguagem humana. Eles se baseiam na arquitetura Transformer, apresentada no artigo de 2017 "Attention is All You Need", de Vaswani et al. Os LLMs preveem o próximo token (parte de palavra) em uma sequência, o que lhes permite gerar texto coerente, responder perguntas, escrever código e realizar tarefas de raciocínio.

LLMs notáveis incluem:
- **GPT series** (OpenAI): GPT-3, GPT-4 e sucessores — amplamente usados para chat e código
- **Claude** (Anthropic): Focado em segurança e utilidade
- **Gemini** (Google DeepMind): Multimodal, integrando texto, imagens e código
- **LLaMA / Llama 3** (Meta): Modelos open-weight para pesquisa e implantação local
- **Mistral** (Mistral AI): Modelos abertos eficientes, competitivos com LLMs muito maiores

Os LLMs são treinados em duas etapas: pré-treinamento (não supervisionado em grandes corpora de texto) e fine-tuning (supervisionado ou via aprendizado por reforço com feedback humano, RLHF). As janelas de contexto descrevem quanto texto um LLM consegue processar de uma vez, variando de 4K tokens (GPT-3 inicial) a mais de 1 milhão de tokens nos modelos mais avançados de 2024.

## Ética e Segurança em IA

A IA levanta importantes questões éticas, incluindo viés, privacidade, substituição de empregos e risco de uso indevido. O viés algorítmico ocorre quando os dados de treinamento refletem desigualdades históricas, levando sistemas de IA a produzir saídas discriminatórias. Sistemas de reconhecimento facial já demonstraram taxas de erro maiores para pessoas de pele mais escura. Algoritmos de contratação já foram identificados como favorecendo candidatos do sexo masculino.

A segurança em IA é o campo dedicado a garantir que sistemas de IA se comportem como o pretendido, sem causar danos não intencionais. Entre as principais preocupações estão:
- **Alinhamento**: Garantir que os objetivos da IA correspondam aos valores humanos
- **Interpretabilidade / Explicabilidade**: Entender por que uma IA tomou uma decisão (crítico em medicina, direito e finanças)
- **Uso indevido**: Deepfakes gerados por IA, desinformação, ciberataques
- **Risco existencial**: Preocupação teórica de que uma futura AGI possa perseguir objetivos desalinhados da sobrevivência humana

Entre as organizações que trabalham com segurança em IA estão a equipe de Safety da OpenAI, a Anthropic (fundada por ex-pesquisadores de segurança da OpenAI), a equipe de segurança da DeepMind e institutos independentes como MIRI e ARC.

## IA na Sociedade

A IA está transformando quase todos os setores:

- **Saúde**: A IA auxilia no diagnóstico de câncer a partir de imagens médicas, na previsão de desfechos de pacientes, na aceleração da descoberta de medicamentos (o AlphaFold resolveu a predição da estrutura de dobramento de proteínas) e na personalização de planos de tratamento.
- **Finanças**: Detecção de fraude, trading algorítmico, credit scoring e robo-advisors usam modelos de ML.
- **Transporte**: Veículos autônomos usam visão computacional, lidar e aprendizado por reforço. Tesla Autopilot, Waymo e Cruise estão entre os principais esforços.
- **Educação**: Plataformas de aprendizagem personalizada adaptam o conteúdo ao ritmo e ao estilo de aprendizagem de cada estudante.
- **Áreas criativas**: A IA gera música, arte e escrita; ferramentas como Midjourney, DALL-E e GitHub Copilot mudaram os fluxos de trabalho criativos.
- **Cibersegurança**: A IA detecta anomalias, identifica ameaças e impulsiona tanto ataques quanto defesas.

## Robótica e IA Incorporada

A robótica combina IA com máquinas físicas. Robôs modernos usam percepção (câmeras, lidar), planejamento e controle para navegar e manipular ambientes. O Atlas, da Boston Dynamics, demonstra movimento bípede avançado. Robôs industriais de empresas como ABB e FANUC automatizam a manufatura. Robôs domésticos (Roomba) e robôs cirúrgicos (da Vinci System) aplicam IA em contextos cotidianos e médicos. A pesquisa em IA incorporada concentra-se em agentes que aprendem habilidades físicas por meio da interação com o mundo, reduzindo a distância entre ambientes simulados e reais.

## Tendências Atuais em IA (anos 2020)

- **IA multimodal**: Sistemas que processam texto, imagens, áudio e vídeo em conjunto (GPT-4V, Gemini)
- **Agentes e IA agêntica**: LLMs que podem usar ferramentas, navegar na web, escrever código e executar ações em múltiplas etapas (Operator da OpenAI, Computer Use da Anthropic)
- **Modelos open-weight**: O LLaMA da Meta democratizou o acesso a grandes modelos para pesquisadores
- **IA on-device**: Execução local de modelos de IA em celulares e laptops sem conectividade com a nuvem (Apple Intelligence, NPUs da Qualcomm)
- **Regulação de IA**: O EU AI Act (2024) é a primeira lei abrangente de IA do mundo, classificando sistemas de IA por nível de risco
