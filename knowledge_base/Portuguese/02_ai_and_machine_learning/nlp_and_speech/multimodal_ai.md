---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [multimodal, ai, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# IA multimodal
Os sistemas multimodais de IA processam e combinam informações de vários tipos de dados – texto, imagens, áudio, vídeo e muito mais – simultaneamente. Embora os sistemas de IA anteriores fossem tipicamente de modalidade única (somente texto, somente imagem), os sistemas modernos mais capazes são multimodais. GPT-4V lê imagens e texto juntos; Gemini processa texto, imagens, áudio e vídeo nativamente; e sistemas como o Sora geram vídeos a partir de descrições de texto. Este arquivo aborda como funciona a IA multimodal, as arquiteturas por trás dela e por que a combinação de modalidades é tão poderosa.
---

## Por que multimodal?
| Benefício | Descrição | Exemplo |
|---------|-------------|---------|
| **Entendimento mais rico** | Diferentes modalidades fornecem informações complementares | Um vídeo transmite movimento, som e contexto que o texto sozinho não consegue |
| **Melhor generalização** | A aprendizagem entre modalidades cria representações mais robustas | Um modelo que viu imagens e descrições de texto de “gato” entende melhor o conceito |
| **Interação mais natural** | Os humanos se comunicam através de múltiplos canais | Assistentes de voz que veem o que você está apontando |
| **Transferência intermodal** | Conhecimento de uma modalidade ajuda em outra | A compreensão da imagem melhora a geração de texto e vice-versa |
---

## Arquiteturas principais
### Modelos de Visão-Linguagem (VLMs)
Modelos que processam imagens e texto juntos.
| Arquitetura | Como funciona | Exemplos |
|---------|-------------|---------|
| **Codificador duplo** | Codificadores separados para imagem e texto; combinar numa fase posterior | CLIPE, ALINHE |
| **Codificador de fusão** | Tokens de imagem e texto são intercalados e processados ​​juntos | Flamingo, Gêmeos |
| **Atenção cruzada** | Os tokens de texto atendem aos recursos da imagem (ou vice-versa) | Flamingo, CoCa |
| **Tokenizador unificado** | As imagens são convertidas em tokens e processadas juntamente com tokens de texto | Gêmeos, Camaleão |
### Como funcionam os modelos de visão-linguagem
| Etapa | Descrição |
|------|-------------|
| **1. Codificar imagem** | Um codificador de visão (ViT, SigLIP) converte a imagem em um conjunto de vetores de características |
| **2. Codificar texto** | Um codificador de linguagem processa os tokens de texto |
| **3. Modalidades de fusíveis** | Os recursos da imagem são projetados no espaço de incorporação do modelo de linguagem |
| **4. Gerar** | O modelo de linguagem produz texto condicionado a entradas de imagem e texto |
### Principais modelos de linguagem de visão
| Modelo | Desenvolvedor | Arquitetura | Recurso notável |
|-------|-----------|-------------|-----------------|
| **CLIP** | OpenAI | Codificador duplo (codificador ViT + texto) | Classificação de imagem zero-shot via texto |
| **LLaVA** | Código aberto | Codificador visual LLaMA + CLIP | VLM de código aberto; comunidade forte |
| **GPT-4V/4o** | OpenAI | Multimodal unificado | Processa texto, imagens e áudio juntos |
| **Gêmeos** | Google DeepMind | Nativamente multimodal de treinamento | Construído para multimodal desde o início |
| **Cláudio** | Antrópico | Visão + texto | Forte na compreensão de documentos e gráficos |
| **Qwen-VL** | Alibaba | VLM de peso aberto | Competitivo com modelos fechados |
| **EstagiárioVL** | Código aberto | Codificador de visão multiescala | Opção forte de código aberto |
---

## Modelos de áudio e fala
### Reconhecimento de fala (ASR)
| Modelo | Arquitetura | Recurso notável |
|-------|-------------|-----------------|
| **Sussurro** (OpenAI) | Transformador codificador-decodificador | Treinado em 680 mil horas de áudio multilíngue; robusto |
| **Conformador** | Convolução + autoatenção | Combina recursos locais e globais |
| **wav2vec 2.0** | Auto-supervisionado | Aprende com a fala não rotulada |
| **USM** (Google) | Modelo de fala universal | 2 milhões de horas de dados rotulados; Mais de 300 idiomas |
### Conversão de texto para fala (TTS)
| Modelo | Abordagem | Recurso notável |
|-------|----------|-----------------|
| **VALL-E** (Microsoft) | Codec neural | Clonagem de voz a partir de amostra de 3 segundos |
| **Latido** (Suno) | Baseado em transformador | Multilíngue; inclui sons não falados |
| **OnzeLabs** | Comercial | Clonagem de voz de alta qualidade |
| **Bate-papoTTS** | Código aberto | Discurso conversacional com prosódia natural |
| **Discurso de Peixe** | Código aberto | Multilíngue; inferência rápida |
### Compreensão de áudio
| Modelo | Capacidade |
|-------|-----------|
| **ÁudioLDM** | Geração de efeitos sonoros a partir de texto |
| **MusicGen** (Meta) | Geração de texto para música |
| **Qwen-Áudio** | Compreensão de áudio (fala, música, sons ambientais) |
| **SALMONN** | Compreensão de fala, áudio, linguagem, música e ruído |
---

## Modelos de vídeo
O vídeo combina imagens, áudio, texto e tempo – tornando-o a modalidade mais complexa.
| Modelo | Tipo | Capacidade |
|-------|------|-------------|
| **Sora** (OpenAI) | Texto para vídeo | Até 1080p; entende de física |
| **Gêmeos** | Compreensão do vídeo | Pode analisar vídeos longos com áudio |
| **Vídeo-LLaVA** | Vídeo + texto | Compreensão de vídeo de código aberto |
| **Pista Gen-3** | Texto/imagem para vídeo | Geração de vídeo comercial |
| **Kling** | Texto para vídeo | Geração de vídeo de formato longo |
### Desafios de compreensão de vídeo
| Desafio | Descrição |
|-----------|------------|
| **Raciocínio temporal** | Compreender os acontecimentos que se desenrolam ao longo do tempo |
| **Contexto longo** | Os vídeos podem durar horas; processar todos os frames é caro |
| **Sincronização audiovisual** | Conectando o que é dito com o que é mostrado |
| **Causalidade** | Compreendendo causa e efeito em sequências de vídeo |
---

## Recuperação Cross-Modal
Encontrar conteúdo relevante em diferentes modalidades.
| Tarefa | Descrição | Exemplo |
|------|-------------|---------|
| **Texto → Imagem** | Encontre imagens que correspondam a uma consulta de texto | Pesquise "pôr do sol sobre as montanhas" em uma biblioteca de fotos |
| **Imagem → Texto** | Encontre texto relevante para uma imagem | Gerando legendas para imagens |
| **Texto → Áudio** | Encontre sons que correspondam a uma descrição | Design de som: “passos no cascalho” |
| **Imagem → Imagem** | Encontre imagens visualmente semelhantes | Pesquisa de produtos por imagem |
### CLIP para recuperação intermodal
O espaço de incorporação compartilhado do CLIP permite a recuperação cross-modal de disparo zero:
| Etapa | Descrição |
|------|-------------|
| 1 | Codifique todas as imagens com o codificador de visão |
| 2 | Codifique a consulta de texto com o codificador de texto |
| 3 | Calcular a similaridade de cosseno entre a incorporação de texto e todas as incorporações de imagens |
| 4 | Retorne as imagens com maior similaridade |
Isso funciona sem qualquer treinamento específico de tarefa — uma propriedade chamada capacidade **zero-shot**.
---

## IA incorporada
A IA incorporada combina percepção multimodal com ação física.
| Sistema | Modalidade | Aplicação |
|--------|----------|------------|
| **RT-2** (Google) | Visão + linguagem → ações do robô | Controle de robô de uso geral a partir de instruções de texto |
| **Outubro** | Política de robôs de código aberto | Treinado em diversos dados de robôs |
| **Tesla Optimus** | Visão + linguagem → tarefas físicas | Robô humanóide para tarefas gerais |
| **Figura 01** | Visão + linguagem + fala | Robô humanóide com capacidade de conversação |
### Desafios na IA incorporada
| Desafio | Por que é difícil |
|-----------|--------------|
| **Lacuna entre Sim e Real** | A simulação não captura perfeitamente a física do mundo real |
| **Destreza** | O controle motor fino (mãos, dedos) é extremamente difícil |
| **Segurança** | Robôs físicos podem causar danos reais |
| **Processamento em tempo real** | Deve perceber, decidir e agir em milissegundos |
| **Generalização** | Um robô treinado para pegar copos vermelhos pode falhar nos azuis |
---

## Dados e treinamento
### Dados de treinamento multimodal
| Conjunto de dados | Modalidades | Tamanho |
|--------|-----------|------|
| **LAION-5B** | Pares imagem-texto | 5,85 bilhões de pares |
| **DataComp** | Imagem-texto com curadoria | Referência para design de conjunto de dados |
| **WIT** (Wikipédia) | Imagem-texto da Wikipedia | 11,5 milhões de pares |
| **Como fazer 100 milhões** | Vídeo-texto (vídeos de instruções) | 100 milhões de clipes |
| **LibriSpeech** | Discurso-texto | 1.000 horas de inglês |
| **Voz Comum** | Discurso-texto | Multilíngue; contribuição da comunidade |
### Estratégias de treinamento
| Estratégia | Descrição | Quando usar |
|----------|-------------|-------------|
| **Treinamento conjunto** | Treinar em todas as modalidades simultaneamente | Quando você alinhou os dados multimodais |
| **Aprendizagem curricular** | Comece com exemplos fáceis; aumentar a dificuldade | Melhora a convergência |
| **Aprendizagem contrastiva** | Aprenda a combinar pares relacionados entre modalidades (estilo CLIP) | Construindo representações compartilhadas |
| **Ajuste de instruções** | Treinar em pares multimodais instrução-resposta | Fazendo modelos seguirem instruções multimodais |
---

## Avaliação
| Referência | Modalidades | O que testa |
|-----------|-----------|---------------|
| **MMLU** | Texto | Conhecimento em 57 disciplinas |
| **MMMU** | Texto + imagens | Raciocínio de nível universitário com diagramas |
| **MathVista** | Texto + imagens | Raciocínio matemático com dados visuais |
| **Vídeo-MME** | Texto + vídeo | Compreensão de vídeo e raciocínio temporal |
| ** CAPACETE ** | Texto + áudio | Avaliação multimodal de longo contexto |
| **Banco SWE** | Texto + código | Tarefas de engenharia de software do mundo real |
---

## Resumo
A IA multimodal representa a mudança de modelos de propósito único para sistemas que percebem e raciocinam em todas as formas de dados. Modelos de linguagem visual como GPT-4V e Gemini podem compreender imagens e texto juntos; modelos de fala como Whisper e VALL-E controlam áudio; os modelos de vídeo estão começando a processar toda a complexidade das imagens em movimento com som. A tendência é clara: os sistemas de IA mais capazes do futuro serão nativamente multimodais, processando todos os tipos de informação simultaneamente. Os desafios — alinhamento de dados, custo computacional, avaliação e implantação incorporada — são significativos, mas o progresso em 2024–2026 foi rápido.