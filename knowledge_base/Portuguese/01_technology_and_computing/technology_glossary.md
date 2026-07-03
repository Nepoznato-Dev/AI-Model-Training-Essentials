# Glossário de Tecnologia

Um glossário de referência que abrange modelos de IA, hardware, benchmarks e
conceitos centrais no cenário moderno de IA e computação.

---

## Modelos de Linguagem e Assistentes de IA

### ChatGPT
ChatGPT é um chatbot de IA desenvolvido pela OpenAI, lançado pela primeira vez
em novembro de 2022. Ele é impulsionado pela série GPT de grandes modelos de
linguagem (LLMs). O ChatGPT é um dos produtos de IA para consumidores com
crescimento mais rápido da história, alcançando 100 milhões de usuários em até
dois meses após o lançamento. Ele oferece conversação baseada em texto, geração
de código, sumarização e escrita criativa. Os planos pagos dão acesso a modelos
mais poderosos, como GPT-4 e GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT é uma família de grandes modelos de linguagem criada pela OpenAI. A
arquitetura usa um Transformer somente decodificador treinado com o objetivo de
previsão do próximo token sobre corpora massivos de texto. As principais
versões incluem GPT-2 (2019, 1,5B parâmetros, notável pela publicidade de
"muito perigoso para ser lançado"), GPT-3 (2020, 175B parâmetros, amplamente
usado via API), GPT-3.5 (a base do ChatGPT original) e GPT-4 (2023,
multimodal, com desempenho próximo ao nível de especialistas humanos em muitos
benchmarks).

### Claude
Claude é um assistente de IA desenvolvido pela Anthropic. Seu nome é uma
homenagem a Claude Shannon, fundador da teoria da informação. A Anthropic foi
fundada por ex-pesquisadores da OpenAI e foca em "IA constitucional" — uma
técnica para tornar os modelos mais seguros, treinando-os para seguir um
conjunto de princípios. Os modelos Claude (Claude 1, 2, 3 Haiku / Sonnet /
Opus) são conhecidos por suas longas janelas de contexto (até 200.000 tokens),
raciocínio refinado e menor geração de conteúdo nocivo em comparação com LLMs
de base.

### Gemini
Gemini é a família de modelos multimodais de IA do Google DeepMind, anunciada
em dezembro de 2023. O Gemini é nativamente multimodal — treinado desde o
início com texto, imagens, áudio e vídeo simultaneamente, ao contrário de
modelos anteriores que tiveram modalidades adicionadas via fine-tuning. As
versões incluem Gemini Nano (no dispositivo), Gemini Flash (rápido e com boa
relação custo-benefício) e Gemini Ultra (de maior capacidade). O Gemini
alimenta o chatbot de IA do Google, Bard (renomeado para Gemini), e os AI
Overviews da Busca Google.

### Phi-3-mini
Phi-3-mini é um pequeno modelo de linguagem (SLM) desenvolvido pela Microsoft
com 3,8B parâmetros. Foi lançado em abril de 2024. Ao contrário da maioria dos
grandes modelos, o Phi-3-mini foi treinado em um conjunto de dados
cuidadosamente curado de "qualidade de livro didático" — uma técnica
pioneirada pela Microsoft Research — que prioriza a qualidade dos dados em vez
do volume bruto. Apesar de ser muito menor que GPT-4 ou Claude 3 Opus, o
Phi-3-mini iguala ou supera modelos várias vezes maiores em benchmarks de
raciocínio, como MMLU e HumanEval. Ele suporta uma janela de contexto de 4k
tokens em sua variante base e uma janela de 128k na variante de contexto longo.
O Phi-3-mini pode rodar em uma única GPU de consumidor ou até mesmo
no dispositivo em um smartphone moderno com RAM suficiente.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) é uma família de modelos com pesos abertos
lançada pela Meta. O Llama 2 (2023) foi disponibilizado para pesquisa e uso
comercial em tamanhos que variam de 7B a 70B parâmetros. O Llama 3 (2024)
melhorou significativamente o desempenho, com modelos variando de 8B a 70B (e
posteriormente 400B+). Como os pesos podem ser baixados publicamente, os
modelos Llama formam a base de um grande ecossistema de variantes ajustadas
(Mistral, Alpaca, Vicuna etc.) e são amplamente usados em implantações locais
ou privadas de IA.

### Mistral
Mistral AI é uma empresa francesa de IA que desenvolve LLMs abertos e
proprietários. O Mistral 7B (2023) demonstrou que um modelo de 7B parâmetros
pode igualar o desempenho de modelos muito maiores usando técnicas eficientes,
como sliding window attention e grouped-query attention. O Mixtral 8x7B (2024)
é um modelo mixture-of-experts — ele direciona cada token para um subconjunto
de 8 redes especialistas, alcançando desempenho de nível GPT-3.5 com menor
custo computacional. Os modelos da Mistral têm pesos totalmente abertos e podem
ser executados localmente.

---

## Hardware de GPU e Placas Gráficas

### GPU (Graphics Processing Unit)
Uma GPU é um processador projetado para computação massivamente paralela.
Originalmente criada para renderização de gráficos 3D, a GPU tornou-se
essencial para treinamento e inferência de IA/ML porque consegue realizar
milhares de operações de ponto flutuante simultaneamente usando milhares de
pequenos núcleos. Os dois principais fabricantes de GPU para IA são NVIDIA e
AMD.

### NVIDIA GeForce RTX Series
A série RTX (Ray Tracing Texel eXtreme) é a linha de GPUs para consumidores da
NVIDIA. As gerações RTX 30xx (Ampere, 2020) e RTX 40xx (Ada Lovelace, 2022)
incluem Tensor Cores dedicados à aceleração de operações de IA. A VRAM (memória
de vídeo) é crítica para executar modelos de IA localmente — uma GPU de 8GB
pode lidar com modelos de 7B parâmetros em quantização de 4 bits; uma GPU de
24GB pode lidar com modelos de 70B em 4 bits.

### NVIDIA A-Series and H-Series (Data Centre)
A A100 (Ampere, 2020) e a H100 (Hopper, 2022) são os aceleradores profissionais
de IA da NVIDIA. Uma H100 tem até 80GB de memória HBM3 e é o hardware padrão
por trás da maior parte do treinamento de LLMs em larga escala hoje. Essas GPUs
custam entre US$ 25.000 e US$ 40.000 cada, mas oferecem de 10 a 30 vezes o
throughput de IA das placas RTX para consumidores.

### AMD Radeon RX Series
A linha de GPUs para consumidores da AMD. A RX 7900 XTX (2022) tem 24GB de VRAM
e pode executar LLMs locais via ROCm (a pilha de computação para GPU da AMD).
As GPUs da AMD, em geral, têm menos suporte do que as da NVIDIA nos frameworks
de IA, embora esse suporte esteja melhorando.

### Intel Arc
Intel Arc é a linha de GPUs dedicadas da Intel, lançada a partir de 2022. As
GPUs Arc suportam XeSS (a técnica de superamostragem da Intel) e têm suporte
limitado, mas crescente, para tarefas de inferência de IA via os frameworks
OpenVINO e IPEX-LLM.

### Intel ARK (ark.intel.com)
ARK é o banco de dados oficial de especificações de produtos da Intel em
ark.intel.com. Ele fornece especificações técnicas detalhadas de todos os
produtos CPU, GPU, FPGA e NUC da Intel, incluindo contagem de núcleos,
frequências de clock, TDP, tipos de memória compatíveis e recursos de conjunto
de instruções. Quando você ouve "consulte o ARK para ver as especificações",
isso significa visitar esse banco de dados para obter informações confiáveis
sobre hardware.

---

## Benchmarks de Desempenho em IA

### MMLU (Massive Multitask Language Understanding)
MMLU é um benchmark que testa o conhecimento de LLMs em 57 disciplinas
acadêmicas, incluindo matemática, história, direito, medicina e ciência da
computação. Ele consiste em questões de múltipla escolha extraídas de exames
reais de nível universitário. Uma pontuação de 70% corresponde aproximadamente
ao nível de um estudante universitário de graduação; GPT-4 e Claude 3 pontuam
acima de 86%. O Phi-3-mini pontua em torno de 70%, apesar de seu pequeno
tamanho.

### HumanEval
HumanEval é o benchmark da OpenAI para geração de código. Ele consiste em 164
problemas de programação em Python com casos de teste automatizados. Os modelos
são medidos por pass@k — a probabilidade de que pelo menos uma entre k soluções
geradas passe em todos os testes. O GPT-4 pontua cerca de ~87% (pass@1); um
modelo 7B bem ajustado pode chegar a ~50–60%.

### HellaSwag
HellaSwag é um benchmark de raciocínio de senso comum. Os modelos recebem uma
frase descrevendo uma atividade cotidiana e devem escolher a continuação mais
provável entre quatro opções. As opções incorretas são especialmente projetadas
para parecer plausíveis, mas estarem sutilmente erradas. O benchmark testa se
um modelo tem compreensão fundamentada de situações físicas e sociais.

### ARC (AI2 Reasoning Challenge)
ARC é um benchmark do Allen Institute for AI. Ele consiste em perguntas de
ciências do ensino fundamental, divididas nos conjuntos "Easy" e "Challenge". O
conjunto Challenge contém perguntas com as quais métodos baseados em recuperação
e modelos estatísticos simples têm dificuldade, exigindo raciocínio em várias
etapas.

---

## Conceitos Fundamentais de IA/ML

### RAG (Retrieval-Augmented Generation)
RAG é uma técnica que combina um sistema de recuperação (normalmente um banco de
dados vetorial) com um modelo de linguagem. Em vez de depender apenas do
conhecimento paramétrico do modelo, o RAG primeiro recupera documentos
relevantes de uma base de conhecimento externa e então os inclui no contexto do
modelo. Isso permite que o modelo responda a perguntas sobre informações
atualizadas ou específicas de um domínio sem necessidade de retreinamento. O
Potato.ai usa uma forma de RAG — ele recupera informações de sua KB e inclui os
resultados no contexto antes de gerar uma resposta.

### Fine-tuning
Fine-tuning é o processo de continuar treinando um modelo pré-treinado em um
conjunto de dados menor e específico de domínio. Isso adapta os pesos do modelo
para uma tarefa ou domínio particular. Por exemplo, um LLM base pode passar por
fine-tuning em prontuários médicos para criar um assistente de perguntas e
respostas médicas. Fine-tuning é computacionalmente caro, mas muito mais barato
do que treinar do zero.

### Quantisation
Quantisation reduz a precisão numérica dos pesos do modelo (por exemplo, de
float de 32 bits para inteiro de 4 bits). Isso reduz drasticamente o uso de
memória — um modelo de 7B em precisão de 16 bits requer ~14GB de VRAM; o mesmo
modelo em 4 bits (formato GGUF) requer ~4GB. A quantização normalmente causa
uma pequena, porém aceitável, degradação de precisão e é a principal técnica
que permite que modelos grandes rodem em hardware de consumidor ou até em
dispositivos móveis.

### Context Window
A janela de contexto é o número máximo de tokens que um modelo pode processar de
uma só vez, incluindo tanto o prompt quanto a resposta gerada. O GPT-3.5 tinha
uma janela de 4.096 tokens; GPT-4 Turbo e Claude 3 suportam 128.000 tokens; o
Gemini 1.5 Pro suporta 1.000.000 de tokens. Uma janela de contexto maior
permite que o modelo "veja" mais de uma conversa ou documento ao mesmo tempo,
melhorando a coerência em interações longas.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF é a técnica de treinamento que transforma um modelo de linguagem base (que
simplesmente prevê o próximo token) em um assistente que segue instruções e se
comporta de forma útil. Avaliadores humanos pontuam as saídas do modelo, um
modelo de recompensa é treinado com base nessas preferências, e então o modelo
de linguagem é otimizado em relação a esse modelo de recompensa usando
aprendizado por reforço. ChatGPT, Claude e Gemini usam variantes de RLHF ou
técnicas de alinhamento semelhantes (por exemplo, Constitutional AI e Direct
Preference Optimisation).

### Transformer Architecture
O Transformer é a arquitetura de rede neural subjacente a todos os LLMs
modernos. Introduzido no artigo de 2017 "Attention Is All You Need", de Vaswani
et al., ele usa mecanismos de self-attention para processar todos os tokens em
paralelo, em vez de sequencialmente. Transformers somente codificador (BERT)
são usados para tarefas de compreensão; Transformers somente decodificador
(GPT, Llama, Mistral) são usados para tarefas de geração; Transformers
codificador-decodificador (T5, BART) são usados para tradução e sumarização.

### Embeddings and Vector Databases
Embeddings são representações numéricas densas de texto (ou imagens) produzidas
por uma rede neural. Textos semanticamente semelhantes têm embeddings próximos
no espaço vetorial. Bancos de dados vetoriais (ChromaDB, Pinecone, Weaviate,
Qdrant) armazenam esses embeddings e oferecem busca rápida aproximada por
vizinhos mais próximos. Eles são a base de armazenamento dos sistemas RAG,
incluindo a camada de memória fria do Potato.ai.
