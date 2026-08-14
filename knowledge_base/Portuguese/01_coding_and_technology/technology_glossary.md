<!--
---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Glossário de tecnologia
Um glossário de referência que abrange modelos de IA, hardware, benchmarks e conceitos básicos
no cenário moderno de IA e computação.
---

## Modelos e assistentes de linguagem de IA
### Bate-papoGPT
ChatGPT é um chatbot de IA desenvolvido pela OpenAI, lançado pela primeira vez em novembro de 2022.
Ele é alimentado pela série GPT de modelos de linguagem grande (LLMs). ChatGPT é um
dos produtos de IA de consumo que mais crescem na história, atingindo 100 milhões
usuários dentro de dois meses após o lançamento. Suporta conversação baseada em texto, código
geração, resumo e escrita criativa. Os níveis pagos fornecem acesso a
modelos mais poderosos, como GPT-4 e GPT-4o.
### GPT (Transformador Gerativo Pré-treinado)
GPT é uma família de grandes modelos de linguagem criados pela OpenAI. A arquitetura
usa um Transformer somente decodificador treinado com um objetivo de previsão do próximo token em
corpora de texto massivo. As principais versões incluem GPT-2 (2019, parâmetros 1,5B, notável
para publicidade "muito perigosa para liberar"), GPT-3 (2020, parâmetros 175B, amplamente
usado por meio da API), GPT-3.5 (a espinha dorsal do ChatGPT original) e GPT-4
(2023, multimodal, desempenho próximo do nível de perito humano em muitos parâmetros de referência).
### Cláudio
Claude é um assistente de IA desenvolvido pela Anthropic. Tem o nome de Claude
Shannon, o fundador da teoria da informação. A Antrópica foi fundada pelo ex-
Pesquisadores da OpenAI e concentra-se na "IA constitucional" - uma técnica para fazer
modelos mais seguros, treinando-os para seguir um conjunto de princípios. Modelos Claude
(Claude 1, 2, 3 Haiku/Soneto/Opus) são conhecidos por longas janelas de contexto (até
para 200.000 tokens), raciocínio matizado e redução da produção prejudicial em comparação com
LLMs básicos.
### Gêmeos
Gemini é a família de modelos de IA multimodais do Google DeepMind, anunciada em
Dezembro de 2023. Gêmeos é nativamente multimodal – treinado desde o início
texto, imagens, áudio e vídeo simultaneamente, ao contrário dos modelos anteriores que tinham
modalidades adicionadas via ajuste fino. As versões incluem Gemini Nano (no dispositivo),
Gemini Flash (rápido e econômico) e Gemini Ultra (maior capacidade).
Gemini alimenta o chatbot Bard de IA do Google (renomeado Gemini) e a IA de Pesquisa do Google
Visão geral.
### Phi-3-mini
Phi-3-mini é um modelo de linguagem pequena (SLM) desenvolvido pela Microsoft com 3,8B
parâmetros. Foi lançado em abril de 2024. Ao contrário da maioria dos modelos grandes, Phi-3-mini
foi treinado em um conjunto de dados cuidadosamente selecionado com "qualidade de livro didático" - uma técnica
pioneiro da Microsoft Research — que prioriza a qualidade dos dados em detrimento do volume bruto.
Apesar de ser muito menor que GPT-4 ou Claude 3 Opus, Phi-3-mini corresponde ou
supera modelos várias vezes maiores em benchmarks de raciocínio como MMLU e
Avaliação Humana. Ele suporta uma janela de contexto de token de 4k em sua variante base e uma janela de contexto de token de 128k
janela na variante de contexto longo. Phi-3-mini pode ser executado em uma única GPU de consumidor
ou mesmo no dispositivo, em um smartphone moderno com RAM suficiente.
### Lhama (Meta AI)
Llama (Large Language Model Meta AI) é uma família de modelos de peso aberto
lançado pela Meta. Llama 2 (2023) foi lançado para pesquisa e uso comercial
com tamanhos variando de parâmetros 7B a 70B. Lhama 3 (2024) melhorado
desempenho significativamente, com modelos variando de 8B a 70B (e posteriormente 400B+).
Como os pesos podem ser baixados publicamente, os modelos Llama são a base
para um grande ecossistema de variantes ajustadas (Mistral, Alpaca, Vicuna, etc.)
e são amplamente utilizados para implantações de IA locais/privadas.
###Mistral
Mistral AI é uma empresa francesa de IA que desenvolve LLMs abertos e proprietários.
Mistral 7B (2023) demonstrou que um modelo de parâmetro 7B pode corresponder ao
desempenho de modelos muito maiores usando técnicas eficientes, como deslizamento
atenção de janela e atenção de consulta agrupada. Mixtral 8x7B (2023) é uma mistura-
modelo de especialistas - ele roteia cada token para um subconjunto de 8 redes especializadas,
alcançar desempenho de nível GPT-3.5 e ao mesmo tempo ser computacionalmente mais barato.
Os modelos da Mistral são totalmente abertos e podem ser executados localmente.
---

## Hardware GPU e placas gráficas
### GPU (Unidade de Processamento Gráfico)
Uma GPU é um processador projetado para computação massivamente paralela. Originalmente
construídas para renderizar gráficos 3D, as GPUs se tornaram essenciais para o treinamento de IA/ML
e inferência porque podem realizar milhares de operações de ponto flutuante
simultaneamente usando milhares de pequenos núcleos. Os dois principais fabricantes de GPU
para IA são NVIDIA e AMD.
### Série NVIDIA GeForce RTX
A série RTX (Ray Tracing Texel eXtreme) é a linha de GPUs de consumo da NVIDIA. RTX
As gerações 30xx (Ampere, 2020) e RTX 40xx (Ada Lovelace, 2022) incluem
Tensor Cores dedicados para acelerar operações de IA. VRAM (RAM de vídeo) é
crítico para executar modelos de IA localmente – uma GPU de 8 GB pode lidar com parâmetros de 7B
modelos em quantização de 4 bits; uma GPU de 24 GB pode lidar com modelos 70B em 4 bits.
### NVIDIA Série A e Série H (Data Center)
O A100 (Ampere, 2020) e o H100 (Hopper, 2022) são IA profissionais da NVIDIA
aceleradores. Um H100 tem até 80 GB de memória HBM3 e é o padrão
hardware por trás da maioria dos treinamentos LLM em larga escala atualmente. Essas GPUs custam US$ 25.000–
US$ 40.000 cada, mas oferecem de 10 a 30 vezes o rendimento de IA dos cartões RTX de consumo.
### Série AMD Radeon RX
Linha de GPU de consumo da AMD. O RX 7900 XTX (2022) tem 24 GB de VRAM e pode rodar
LLMs locais via ROCm (pilha de computação GPU da AMD). GPUs AMD geralmente são menos
bem suportado do que a NVIDIA para estruturas de IA, embora o suporte esteja melhorando.
### Arco Intel
Intel Arc é a linha de produtos de GPU discreta da Intel, lançada a partir de 2022. Arc
GPUs suportam XeSS (superamostragem da Intel) e têm suporte limitado, mas crescente
para tarefas de inferência de IA por meio de estruturas OpenVINO e IPEX-LLM.
### ARK Intel (ark.intel.com)
ARK é o banco de dados oficial de especificações de produtos da Intel em ark.intel.com. Isso
fornece especificações técnicas detalhadas para cada CPU, GPU, FPGA e
Produto NUC, incluindo contagens de núcleos, velocidades de clock, TDP, tipos de memória suportados,
e recursos do conjunto de instruções. Quando você ouve "verifique as especificações do ARK", significa
visitando esse banco de dados para obter informações oficiais de hardware.
---

## Benchmarks de desempenho de IA
### MMLU (compreensão massiva de linguagem multitarefa)
MMLU é uma referência que testa o conhecimento LLM em 57 disciplinas acadêmicas, incluindo
matemática, história, direito, medicina e ciência da computação. Consiste em
questões de múltipla escolha extraídas de exames reais de nível universitário. Uma pontuação de
70% é aproximadamente um nível de graduação humano; GPT-4 e Claude 3 pontuam acima de 86%.
Phi-3-mini pontua em torno de 70%, apesar de seu tamanho pequeno.
### Avaliação Humana
HumanEval é a referência da OpenAI para geração de código. Consiste em 164 Python
problemas de programação com casos de teste automatizados. Os modelos são medidos em
pass@k — a probabilidade de que pelo menos uma das k soluções geradas passe em todas
testes. Pontuações GPT-4 ~87% (aprovado@1); um modelo 7B bem ajustado pode atingir aproximadamente 50–60%.
### HellaSwag
HellaSwag é uma referência de raciocínio de bom senso. Os modelos recebem uma frase
descrevendo uma atividade mundana e deve escolher a continuação mais provável
quatro opções. As opções incorretas são especialmente projetadas para serem plausíveis, mas
sutilmente errado. Ele testa se um modelo tem uma compreensão fundamentada da física
e situações sociais.
### ARC (desafio de raciocínio AI2)
ARC é uma referência do Allen Institute for AI. É composto por ensino fundamental
questões científicas, divididas em conjuntos "Fácil" e "Desafio". O desafio definido
contém questões que métodos baseados em recuperação e modelos estatísticos simples
luta, exigindo raciocínio em várias etapas.
---

## Conceitos básicos de IA/ML
### RAG (geração aumentada de recuperação)
RAG é uma técnica que combina um sistema de recuperação (normalmente um vetor
banco de dados) com um modelo de linguagem. Em vez de confiar apenas no modelo
conhecimento paramétrico, o RAG primeiro recupera documentos relevantes de um
base de conhecimento e, em seguida, inclui-os no contexto do modelo. Isto permite que
modelo para responder perguntas sobre informações atualizadas ou específicas do domínio
sem reciclagem. Potato.ai usa uma forma de RAG – ele recupera de seu KB
e inclui os resultados no contexto antes de gerar uma resposta.
### Ajuste fino
O ajuste fino é o processo de continuar a treinar um modelo pré-treinado em um
conjunto de dados menor e específico do domínio. Isto adapta os pesos do modelo para um
tarefa ou domínio específico. Por exemplo, um LLM básico pode ser ajustado em
registros médicos para criar um assistente médico de perguntas e respostas. O ajuste fino é
computacionalmente caro, mas muito mais barato do que treinar do zero.
### Quantização
A quantização reduz a precisão numérica dos pesos do modelo (por exemplo, de 32 bits
float para inteiro de 4 bits). Isso reduz drasticamente o consumo de memória – um modelo 7B
na precisão de 16 bits requer ~ 14 GB de VRAM; o mesmo modelo em 4 bits (formato GGUF)
requer ~ 4 GB. A quantização normalmente causa uma precisão pequena, mas aceitável
degradação e é a principal técnica que permite que grandes modelos sejam executados no consumidor
hardware ou até mesmo dispositivos móveis.
### Janela de contexto
A janela de contexto é o número máximo de tokens que um modelo pode processar de uma vez,
incluindo o prompt e a resposta gerada. GPT-3.5 tinha um token de 4.096
janela; GPT-4 Turbo e Claude 3 suportam 128.000 tokens; Gêmeos 1.5 Pró
suporta 1.000.000 de tokens. Uma janela de contexto maior permite que o modelo "veja"
mais uma conversa ou documento de uma só vez, melhorando a coerência ao longo do tempo
trocas.
### RLHF (Aprendizagem por Reforço com Feedback Humano)
RLHF é a técnica de treinamento que transforma um modelo de linguagem base (que
simplesmente prevê o próximo token) em um assistente que segue instruções e
se comporta de maneira prestativa. Os avaliadores humanos pontuam os resultados do modelo, um modelo de recompensa é treinado
em suas preferências, e o modelo de linguagem é então otimizado contra isso
modelo de recompensa usando aprendizagem por reforço. ChatGPT, Claude e Gemini usam
variantes de RLHF ou técnicas de alinhamento semelhantes (por exemplo, IA Constitucional,
Otimização de preferência direta).
### Arquitetura do Transformador
O Transformer é a arquitetura de rede neural subjacente a todos os LLMs modernos.
Introduzido no artigo de 2017 "Attention Is All You Need" de Vaswani et al.,
usa mecanismos de autoatenção para processar todos os tokens em paralelo, em vez de
sequencialmente. Transformadores somente de codificador (BERT) são usados ​​para tarefas de compreensão;
Transformadores somente decodificadores (GPT, Llama, Mistral) são usados ​​para tarefas de geração;
Os transformadores codificador-decodificador (T5, BART) são usados ​​para tradução e resumo.
### Incorporações e bancos de dados vetoriais
Embeddings são representações numéricas densas de texto (ou imagens) produzidas por
uma rede neural. Textos semanticamente semelhantes têm incorporações próximas em
espaço vetorial. Armazenamento de bancos de dados vetoriais (ChromaDB, Pinecone, Weaviate, Qdrant)
essas incorporações e suportam pesquisa rápida e aproximada do vizinho mais próximo. Eles são
a espinha dorsal de armazenamento dos sistemas RAG, incluindo a camada de memória fria do Potato.ai.