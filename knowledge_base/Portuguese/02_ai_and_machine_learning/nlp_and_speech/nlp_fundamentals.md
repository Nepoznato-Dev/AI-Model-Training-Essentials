---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [nlp, ai-and-machine-learning]
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

# Fundamentos da PNL
Processamento de Linguagem Natural (PNL) é o campo que ensina máquinas a compreender, gerar e trabalhar com a linguagem humana. Ele alimenta mecanismos de pesquisa, chatbots, sistemas de tradução, análise de sentimento e grandes modelos de linguagem (LLMs) que transformaram a IA desde 2020. Este arquivo cobre a evolução das técnicas clássicas às modernas arquiteturas baseadas em Transformer.
---

## Pré-processamento de texto
O texto bruto é confuso. Antes que um modelo possa usá-lo, ele precisa ser limpo e estruturado.
| Etapa | O que faz | Exemplo |
|------|-------------|---------|
| **Tokenização** | Dividir o texto em tokens (palavras, subpalavras ou caracteres) | "Eu amo PNL" →`["I", "love", "NLP"]`|
| **Minúsculas** | Converter para minúsculas | "Olá" → "olá" |
| **Pare a remoção de palavras** | Remover palavras comuns (o, é, em) | "o gato sentou" → "o gato sentou" |
| **Decadência** | Cortar terminações de palavras (bruto) | "executando" → "executando" |
| **Lematização** | Reduzir para a forma de dicionário (com reconhecimento de contexto) | “melhor” → “bom” |
| **Normalização** | Corrigir codificação, remover caracteres especiais, expandir contrações | "não" → "não" |
Os modelos modernos do Transformer geralmente ignoram a remoção e a lematização de palavras de parada – eles aprendem esses padrões a partir dos dados.
---

## Representação de texto
As máquinas precisam de números, não de palavras. A forma como representamos o texto como vetores é fundamental.
### Abordagens Clássicas
| Método | Descrição | Limitação |
|--------|-------------|-----------|
| **Codificação One-Hot** | Cada palavra é uma posição única em um enorme vetor | Escasso; sem significado semântico |
| **Saco de Palavras (BoW)** | Contar frequências de palavras; ignorar ordem | Perde totalmente a ordem das palavras |
| **TF-IDF** | Ponderar palavras por frequência no documento × raridade no corpus | Ainda ignora ordem e contexto |
### Incorporações de palavras
Os embeddings mapeiam palavras em vetores densos onde palavras semelhantes estão próximas umas das outras.
| Modelo | Ideia-chave |
|-------|----------|
| **Word2Vec** (2013) | Prever palavra do contexto (CBOW) ou contexto da palavra (Skip-gram) |
| **Luva** (2014) | Estatísticas globais de coocorrência → vetores densos |
| **FastText** (2016) | Word2Vec + informações de subpalavras (lida melhor com palavras raras) |
O famoso exemplo:`king - man + woman ≈ queen`. Os embeddings capturam relacionamentos semânticos.
**Limitação**: os embeddings clássicos atribuem um vetor por palavra, portanto não podem lidar com polissemia (palavras com múltiplos significados). “Banco” em “banco do rio” e “conta bancária” obtém o mesmo vetor.
---

## Modelos de sequência
Antes dos Transformers, a abordagem padrão da PNL era processar o texto sequencialmente.
| Arquitetura | Como funciona | Força | Fraqueza |
|------------|-------------|----------|----------|
| **RNN** | Processe os tokens um de cada vez; manter o estado oculto | Lida com entrada de comprimento variável | Gradientes desaparecendo; não é possível capturar dependências longas |
| **LSTM** | RNN com portas (esquecer, entrada, saída) para controlar o fluxo de informações | Melhor em dependências de longo alcance | Ainda sequencial; lento para treinar |
| **GRU** | LSTM simplificado (menos portões) | Mais rápido que LSTM; desempenho semelhante | Mesmas limitações fundamentais |
Esses modelos processam texto da esquerda para a direita, o que significa que são lentos para treinar (não podem paralelizar) e lutam com dependências de longo alcance.
---

## O Mecanismo de Atenção
A atenção permite que um modelo observe todas as posições em uma sequência simultaneamente e decida quais são mais relevantes para a previsão atual.
### Principais insights
Em vez de comprimir uma frase inteira em um único estado oculto (como fazem os RNNs), a atenção calcula uma soma ponderada de todos os estados ocultos, onde os pesos são aprendidos.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Componente | Função |
|-----------|------|
| **Consulta (Q)** | O que estou procurando? |
| **Chave (K)** | O que eu contenho? |
| **Valor (V)** | Que informações eu forneço? |
| **√d_k** | Fator de escala para evitar grandes produtos escalares |
---

## A Arquitetura do Transformador
O Transformer (Vaswani et al., 2017 - "Attention Is All You Need") substituiu inteiramente a recorrência pela atenção. É a base de praticamente toda a PNL moderna.
### Arquitetura
| Componente | Descrição |
|-----------|------------|
| **Codificador** | Lê o texto de entrada; produz representações contextuais |
| **Decodificador** | Gera texto de saída; atende à saída do codificador |
| **Autoatenção** | Cada token atende todos os outros tokens na mesma sequência |
| **Atenção de múltiplas cabeças** | Execute vários cabeçotes de atenção em paralelo; capturar diferentes relacionamentos |
| **Codificação posicional** | Injetar informações de posição (já que não há recorrência) |
| **Rede Feed-Forward** | Aplicado a cada posição de forma independente |
| **Normalização de camadas** | Estabilizar o treinamento |
| **Conexões residuais** | Ignorar conexões para fluxo gradiente |
### Somente codificador, Somente decodificador, Codificador-Decodificador
| Variante | Arquitetura | Melhor para | Exemplos |
|---------|---------|----------|---------|
| **Somente codificador** | Compreende texto | Classificação, NER, análise de sentimento | BERT, RoBERTa, DeBERTa |
| **Somente decodificador** | Gera texto | Modelos de linguagem, chatbots, geração de código | GPT-3/4, LLaMA, Claude |
| **Codificador-Decodificador** | Transforma texto | Tradução, resumo | T5, BART, mBART |
---

## Principais famílias modelo
### Família BERT (somente codificador)
| Modelo | Recurso principal |
|-------|------------|
| **BERTO** (2018) | Modelo de linguagem mascarada + previsão da próxima frase |
| **RoBERTa** | NSP removido; treinou por mais tempo com mais dados |
| **ALBERTO** | Compartilhamento de parâmetros; pegada menor |
| **DeBERTa** | Atenção desembaraçada; NLU melhorado |
| **DistilBERT** | 40% menor, 60% mais rápido, mantém 97% do desempenho do BERT |
### Família GPT (somente decodificador)
| Modelo | Parâmetros | Notas |
|-------|-----------|-------|
| **GPT-2** | 1,5B | Modelos somente decodificadores mostrados podem gerar texto coerente |
| **GPT-3** | 175B | Aprendizagem rápida; solicitado em vez de ajustado |
| **GPT-3.5/GPT-4** | Não divulgado | Ajustado por instrução + RLHF; conversacional |
| **LLaMA** (Meta) | 7B-70B | Peso aberto; gerou o ecossistema LLM de código aberto |
| **Mistral / Mixtral** | 7B/8×7B (MoE) | Modelos abertos eficientes com forte desempenho |
---

## Principais tarefas de PNL
| Tarefa | Descrição | Modelo típico |
|------|-------------|-------------|
| **Classificação de texto** | Atribuir um rótulo ao texto (spam/não spam, positivo/negativo) | BERT, classificadores ajustados |
| **Reconhecimento de entidade nomeada (NER)** | Identifique pessoas, organizações, locais no texto | Camada BERT + CRF |
| **Análise de sentimento** | Determinar o tom emocional | BERT ajustado ou LLM zero-shot |
| **Tradução automática** | Traduzir entre idiomas | T5, mBART, MarianMT |
| **Resposta a perguntas** | Responda às perguntas de acordo com o contexto | BERT (extrativo), GPT (generativo) |
| **Resumo** | Condensar texto longo | T5, BART, GPT |
| **Geração de texto** | Produzir texto coerente | GPT-4, LLaMA, Claude |
---

## Ajuste fino versus solicitação
| Abordagem | Como funciona | Quando usar |
|----------|-------------|-------------|
| **Ajuste fino** | Atualize os pesos do modelo nos dados específicos da tarefa | Você rotulou os dados; precisam de desempenho máximo |
| **Solicitando** | Dê instruções ao modelo em linguagem natural | Prototipagem rápida; dados limitados; usando LLMs |
| **Poucos tiros** | Incluir exemplos no prompt | Quando você tem alguns exemplos, mas não o suficiente para fazer o ajuste fino |
| **LoRA/QLoRA** | Ajuste fino eficiente; atualizar pequenas matrizes de classificação baixa | Ajuste modelos grandes com memória GPU limitada |
---

## Ferramentas e Estruturas
| Ferramenta | Finalidade |
|------|---------|
| ** Abraçando Transformadores de Rosto ** | Modelos pré-treinados, tokenizadores, pipelines de ajuste fino |
| **espaCio** | Pipeline de PNL de nível de produção (tokenização, NER, POS, dependência) |
| **NLTK** | Educacional; algoritmos clássicos de PNL |
| **Gensim** | Modelagem de tópicos (LDA), incorporação de palavras (Word2Vec, Doc2Vec) |
| **LangChain/LlamaIndex** | Estruturas para construção de aplicativos baseados em LLM |
| **vLLM** | Serviço LLM de alto rendimento |
| **Tokenizadores (HF)** | Tokenização rápida (BPE, WordPiece, SentencePiece) |
---

## O cenário LLM
O cenário moderno da PNL é dominado por grandes modelos de linguagem:
| Categoria | Exemplos | Notas |
|----------|------------|-------|
| **Proprietário** | GPT-4, Claude, Gêmeos | Melhor desempenho; Apenas acesso à API |
| **Peso aberto** | LLaMA 3, Mistral, Qwen | Pesos disponíveis; executar localmente |
| **Código aberto** | Pítia, OPT | Totalmente aberto (dados, pesos, código) |
| **Multimodal** | GPT-4V, Gêmeos, LLaVA | Processar texto + imagens |
| **Especializado em código** | CodeLlama, StarCoder, DeepSeek Coder | Treinado em código |
| **Pequeno/Eficiente** | Phi-3, Gemma, TinyLlama | Forte desempenho em pequena escala |
O campo está se movendo rapidamente. O que é de vanguarda hoje pode ser substituído em meses. Os fundamentos – atenção, tokenização, ajuste fino, avaliação – permanecem estáveis.