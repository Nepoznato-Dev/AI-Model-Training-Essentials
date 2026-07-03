# Glossário de Tecnologia

Um glossário de referência que cobre modelos de AI, hardware, benchmarks e conceitos centrais
no cenário moderno de AI e computação.

---

## Modelos de Linguagem e Assistentes de AI

### ChatGPT
ChatGPT é um chatbot de AI desenvolvido pela OpenAI, lançado pela primeira vez em novembro de 2022.
Ele é baseado na série GPT de large language models (LLMs). O ChatGPT é um
produto de AI para consumidores com um dos crescimentos mais rápidos da história, alcançando 100 milhões de
usuários em dois meses após o lançamento. Ele oferece conversação baseada em texto, geração de código,
resumos e escrita criativa. Os planos pagos dão acesso a modelos
mais poderosos, como GPT-4 e GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT é uma família de large language models criada pela OpenAI. A arquitetura
usa um Transformer somente com decoder, treinado com o objetivo de prever o próximo token em
massivos corpora de texto. As principais versões incluem GPT-2 (2019, 1,5B de parâmetros, notável
pela publicidade de "too dangerous to release"), GPT-3 (2020, 175B de parâmetros, amplamente
usado via API), GPT-3.5 (a base do ChatGPT original) e GPT-4
(2023, multimodal, com desempenho próximo ao de especialistas humanos em muitos benchmarks).

### Claude
Claude é um assistente de AI desenvolvido pela Anthropic. O nome é uma homenagem a Claude
Shannon, fundador da teoria da informação. A Anthropic foi fundada por ex-pesquisadores da
OpenAI e tem foco em "constitutional AI" — uma técnica para tornar
os modelos mais seguros, treinando-os para seguir um conjunto de princípios. Os modelos Claude
(Claude 1, 2, 3 Haiku / Sonnet / Opus) são conhecidos por suas longas janelas de contexto (até
200.000 tokens), raciocínio sofisticado e menor produção de conteúdo nocivo em comparação com
LLMs de base.

### Gemini
Gemini é a família de modelos multimodais de AI do Google DeepMind, anunciada em
dezembro de 2023. Gemini é nativamente multimodal — treinado desde o início com
texto, imagens, áudio e vídeo simultaneamente, ao contrário de modelos anteriores que tiveram
modalidades adicionadas via fine-tuning. As versões incluem Gemini Nano (on-device),
Gemini Flash (rápido, econômico) e Gemini Ultra (maior capacidade).
Gemini impulsiona o chatbot de AI do Google, Bard (renomeado para Gemini), e os Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini é um small language model (SLM) desenvolvido pela Microsoft com 3,8B
parâmetros. Foi lançado em abril de 2024. Ao contrário da maioria dos modelos grandes, o Phi-3-mini
foi treinado em um conjunto de dados cuidadosamente selecionado, de "qualidade de livro didático" — uma técnica
pioneira da Microsoft Research — que prioriza a qualidade dos dados em vez do volume bruto.
Apesar de ser muito menor que GPT-4 ou Claude 3 Opus, o Phi-3-mini iguala ou
supera modelos várias vezes maiores em benchmarks de raciocínio, como MMLU e
HumanEval. Ele suporta uma janela de contexto de 4k tokens em sua variante base e de 128k
na variante de longo contexto. O Phi-3-mini pode rodar em uma única GPU de consumo
ou até on-device em um smartphone moderno com RAM suficiente.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) é uma família de modelos com open weights
lançada pela Meta. O Llama 2 (2023) foi lançado para uso em pesquisa e uso comercial
com tamanhos que vão de 7B a 70B parâmetros. O Llama 3 (2024) melhorou
significativamente o desempenho, com modelos de 8B a 70B (e depois 400B+).
Como os pesos podem ser baixados publicamente, os modelos Llama são a base
para um grande ecossistema de variantes com fine-tuning (Mistral, Alpaca, Vicuna etc.)
e são amplamente usados em implantações locais/privadas de AI.

### Mistral
Mistral AI é uma empresa francesa de AI que desenvolve LLMs abertos e proprietários.
O Mistral 7B (2023) demonstrou que um modelo de 7B parâmetros pode igualar o
desempenho de modelos muito maiores usando técnicas eficientes, como sliding
window attention e grouped-query attention. O Mixtral 8x7B (2024) é um modelo mixture-
of-experts — ele encaminha cada token para um subconjunto de 8 redes especialistas,
alcançando desempenho de nível GPT-3.5 com custo computacional menor.
Os modelos da Mistral têm open weights e podem ser executados localmente.

---

## Hardware de GPU e Placas Gráficas

### GPU (Graphics Processing Unit)
Uma GPU é um processador projetado para computação massivamente paralela. Originalmente
criada para renderizar gráficos 3D, a GPU se tornou essencial para treinamento
e inferência de AI/ML porque consegue executar milhares de operações de ponto flutuante
simultaneamente usando milhares de pequenos núcleos. Os dois principais fabricantes de GPU
para AI são NVIDIA e AMD.

### Série NVIDIA GeForce RTX
A série RTX (Ray Tracing Texel eXtreme) é a linha de GPUs de consumo da NVIDIA. As gerações RTX
30xx (Ampere, 2020) e RTX 40xx (Ada Lovelace, 2022) incluem
Tensor Cores dedicados para acelerar operações de AI. VRAM (video RAM) é
crítica para executar modelos de AI localmente — uma GPU de 8GB pode lidar com modelos de 7B
parâmetros em quantização de 4 bits; uma GPU de 24GB pode lidar com modelos de 70B em 4 bits.

### Séries NVIDIA A e H (Data Center)
A A100 (Ampere, 2020) e a H100 (Hopper, 2022) são os aceleradores profissionais de AI
da NVIDIA. Uma H100 tem até 80GB de memória HBM3 e é o hardware padrão
por trás da maior parte do treinamento de LLMs em larga escala atualmente. Essas GPUs custam de US$ 25.000 a
US$ 40.000 cada, mas oferecem de 10 a 30× o throughput de AI das placas RTX de consumo.

### Série AMD Radeon RX
É a linha de GPUs de consumo da AMD. A RX 7900 XTX (2022) tem 24GB de VRAM e pode executar
LLMs locais via ROCm (a stack de computação para GPU da AMD). As GPUs da AMD em geral têm menos
suporte que as da NVIDIA em frameworks de AI, embora o suporte esteja melhorando.

### Intel Arc
Intel Arc é a linha de GPUs dedicadas da Intel, lançada a partir de 2022. As GPUs Arc
suportam XeSS (super-sampling da Intel) e têm suporte limitado, porém crescente,
para tarefas de inferência de AI via os frameworks OpenVINO e IPEX-LLM.

### ARK Intel (ark.intel.com)
ARK é o banco de dados oficial de especificações de produtos da Intel em ark.intel.com. Ele
fornece especificações técnicas detalhadas de todos os produtos Intel CPU, GPU, FPGA e
NUC, incluindo número de núcleos, velocidades de clock, TDP, tipos de memória suportados
e recursos do conjunto de instruções. Quando alguém diz "consulte o ARK para ver as especificações",
isso significa visitar esse banco de dados para obter informações autoritativas sobre hardware.

---

## Benchmarks de Desempenho em AI

### MMLU (Massive Multitask Language Understanding)
MMLU é um benchmark que testa o conhecimento de LLMs em 57 disciplinas acadêmicas, incluindo
matemática, história, direito, medicina e ciência da computação. Ele consiste em
questões de múltipla escolha extraídas de provas universitárias reais. Uma pontuação de
70% corresponde aproximadamente ao nível de um estudante universitário; GPT-4 e Claude 3 pontuam acima de 86%.
Phi-3-mini pontua em torno de 70%, apesar do tamanho reduzido.

### HumanEval
HumanEval é o benchmark da OpenAI para geração de código. Ele consiste em 164 problemas de
programação em Python com casos de teste automatizados. Os modelos são medidos por
pass@k — a probabilidade de que pelo menos uma entre k soluções geradas passe em todos os
testes. GPT-4 pontua ~87% (pass@1); um modelo 7B bem ajustado pode chegar a ~50–60%.

### HellaSwag
HellaSwag é um benchmark de raciocínio de senso comum. Os modelos recebem uma frase
descrevendo uma atividade cotidiana e precisam escolher a continuação mais provável entre
quatro opções. As opções incorretas são projetadas especificamente para parecer plausíveis,
mas sutilmente erradas. Ele testa se o modelo tem uma compreensão fundamentada de situações físicas
e sociais.

### ARC (AI2 Reasoning Challenge)
ARC é um benchmark do Allen Institute for AI. Ele consiste em questões de ciências
do ensino fundamental, divididas em conjuntos "Easy" e "Challenge". O conjunto Challenge
contém perguntas com as quais métodos baseados em recuperação e modelos estatísticos simples
têm dificuldade, exigindo raciocínio em várias etapas.

---

## Conceitos Fundamentais de AI/ML

### RAG (Retrieval-Augmented Generation)
RAG é uma técnica que combina um sistema de recuperação (normalmente um banco de dados
vetorial) com um language model. Em vez de depender apenas do conhecimento
paramétrico do modelo, o RAG primeiro recupera documentos relevantes de uma base de conhecimento
externa e depois os inclui no contexto do modelo. Isso permite que o
modelo responda perguntas sobre informações atualizadas ou específicas de um domínio
sem precisar de retreinamento. O Potato.ai usa uma forma de RAG — ele recupera da sua KB
e inclui os resultados no contexto antes de gerar uma resposta.

### Fine-tuning
Fine-tuning é o processo de continuar o treinamento de um modelo pré-treinado em um
conjunto de dados menor e específico de domínio. Isso adapta os pesos do modelo para uma
tarefa ou domínio específico. Por exemplo, um LLM base pode passar por fine-tuning em
prontuários médicos para criar um assistente de perguntas e respostas médicas. Fine-tuning é
computacionalmente caro, mas muito mais barato do que treinar do zero.

### Quantização
Quantização reduz a precisão numérica dos pesos do modelo (por exemplo, de float de 32 bits
para inteiro de 4 bits). Isso reduz drasticamente a pegada de memória — um modelo 7B
em precisão de 16 bits exige ~14GB de VRAM; o mesmo modelo em 4 bits (formato GGUF)
exige ~4GB. A quantização normalmente causa uma pequena, porém aceitável, perda de precisão
e é a principal técnica que permite que modelos grandes rodem em hardware de consumo
ou até em dispositivos móveis.

### Janela de Contexto
A janela de contexto é o número máximo de tokens que um modelo pode processar de uma só vez,
incluindo tanto o prompt quanto a resposta gerada. O GPT-3.5 tinha uma janela de 4.096 tokens;
GPT-4 Turbo e Claude 3 suportam 128.000 tokens; Gemini 1.5 Pro
suporta 1.000.000 de tokens. Uma janela de contexto maior permite que o modelo "veja"
mais de uma conversa ou documento ao mesmo tempo, melhorando a coerência em trocas longas.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF é a técnica de treinamento que transforma um language model base (que
simplesmente prevê o próximo token) em um assistente que segue instruções e
se comporta de forma útil. Avaliadores humanos pontuam as saídas do modelo, um reward model é treinado
com base nessas preferências, e o language model é então otimizado contra esse
reward model usando aprendizado por reforço. ChatGPT, Claude e Gemini usam
variantes de RLHF ou técnicas semelhantes de alinhamento (por exemplo, Constitutional AI,
Direct Preference Optimisation).

### Arquitetura Transformer
O Transformer é a arquitetura de rede neural subjacente a todos os LLMs modernos.
Apresentado no artigo de 2017 "Attention Is All You Need", de Vaswani et al., ele
usa mecanismos de self-attention para processar todos os tokens em paralelo, em vez de
sequencialmente. Transformers somente com encoder (BERT) são usados para tarefas de compreensão;
Transformers somente com decoder (GPT, Llama, Mistral) são usados para tarefas de geração;
Transformers encoder-decoder (T5, BART) são usados para tradução e sumarização.

### Embeddings e Bancos de Dados Vetoriais
Embeddings são representações numéricas densas de texto (ou imagens) produzidas por
uma rede neural. Textos semanticamente semelhantes têm embeddings próximos no
espaço vetorial. Bancos de dados vetoriais (ChromaDB, Pinecone, Weaviate, Qdrant) armazenam
esses embeddings e suportam busca aproximada rápida por vizinho mais próximo. Eles são
a base de armazenamento de sistemas RAG, incluindo a camada de cold memory do Potato.ai.
