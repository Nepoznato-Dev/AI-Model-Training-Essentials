---
# Metadata
title: "Prompt Engineering"
description: "Prompt techniques and strategies"
category: "AI and Machine Learning"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [prompt, engineering, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Engenharia imediata
A engenharia de prompts é a prática de projetar, refinar e otimizar prompts de entrada para obter o melhor resultado possível de um modelo de linguagem. É uma arte e uma ciência e é a interface principal para controlar o comportamento do LLM sem ajustes finos.
---

## Princípios Fundamentais
### Clareza e Especificidade
Uma solicitação clara não deixa espaço para ambigüidades. Especifique exatamente o que você deseja, incluindo formato, comprimento e perspectiva.
**Vago:**
> "Conte-me sobre Python."
**Específico:**
> "Explique o Global Interpreter Lock (GIL) do Python. Descreva seu impacto no multithreading, forneça uma solução alternativa e mantenha sua resposta com menos de 200 palavras."
### Fornecer contexto
Os modelos têm melhor desempenho quando conhecem a função, o público e o objetivo.
**Sem contexto:**
> "Escreva uma função para classificar uma lista."
**Com contexto:**
> "Você é um desenvolvedor Python sênior. Escreva uma função para classificar uma lista de dicionários por uma determinada chave. Use dicas de tipo e lide com casos extremos. O público são desenvolvedores juniores."
### Use instruções positivas
Diga ao modelo o que fazer, não o que evitar. “Não inclua jargões” é mais fraco do que “Use uma linguagem simples e acessível a uma criança de 10 anos”.
---

## Estruturas de prompt
### Sistema/Usuário/Funções de assistente
A maioria das APIs LLM suportam uma estrutura multiturno:
- **Mensagem do sistema**: Define o comportamento, a personalidade e as restrições do modelo (persiste durante toda a sessão).
- **Mensagem do usuário**: A consulta ou instrução atual.
- **Mensagem do assistente**: as respostas anteriores do modelo (usadas para continuidade).
**Exemplo (estilo API OpenAI):**
Sistema: Você é um assistente de codificação útil. Você responde com exemplos de código concisos e breves explicações. Nunca forneça código inseguro.
Usuário: escreva uma função Python para baixar um arquivo de uma URL.
### Solicitação de poucas fotos
Forneça 2–3 exemplos do formato de entrada-saída desejado antes de pedir ao modelo para executar a tarefa. Isso ensina o padrão.
**Exemplo:**
Usuário: Converta estas frases para voz passiva:
Entrada: O gato perseguiu o rato.
Saída: O rato foi perseguido pelo gato.
Entrada: O chef preparou a refeição.
Resultado: A refeição foi preparada pelo chef.
Entrada: A tempestade destruiu a casa.
Saída: (modelo concluído)
### Cadeia de Pensamento (CoT)
Incentive o modelo a mostrar seu raciocínio passo a passo. Isso melhora a precisão em tarefas aritméticas, lógicas e de várias etapas.
**Sem CoT:**
> "O que é 24 × 37?"
**Com CoT:**
> "Calcule 24 × 37. Mostre seu raciocínio passo a passo."
O modelo produzirá etapas intermediárias, reduzindo erros aritméticos.
### Resultados Estruturados
Solicite um formato específico como JSON, YAML ou tabelas de descontos para tornar a análise confiável.
Usuário: liste três prós e três contras dos microsserviços. Retorne apenas um objeto JSON válido com chaves "prós" e "contras", cada uma com uma matriz de strings.
---

## Técnicas Avançadas
### Autoconsistência
Gere múltiplas respostas para o mesmo prompt (com temperatura > 0) e vote por maioria na resposta final. Isto é especialmente eficaz para tarefas de raciocínio.
### Árvore dos Pensamentos
Explore vários caminhos de raciocínio em paralelo, avalie cada um e escolha o melhor. Esta é uma técnica de pesquisa, mas pode ser aproximada pedindo ao modelo para “explorar soluções alternativas”.
### ReAct (raciocínio + atuação)
Deixe o modelo intercalar o raciocínio com as chamadas de ferramentas. Ele pode pensar e depois agir (por exemplo, pesquisar na web, executar código) e depois pensar novamente com base no resultado.
**Estrutura de prompt:**
Você tem acesso a uma calculadora e a um mecanismo de busca. Para cada etapa, produza:
Pensamento: (seu raciocínio)
Ação: (nome da ferramenta, entrada)
Observação: (saída da ferramenta)
... continue até ter a resposta final.
### Atribuição de Personagem
Atribua uma persona específica para enquadrar a resposta.
**Exemplos:**
- "Você é um desenvolvedor de kernel Linux explicando gerenciamento de memória para um recém-formado."
- “Você é uma nutricionista simpática que dá conselhos gerais a um cliente.”
- "Você é um crítico de tecnologia cínico analisando um novo gadget."
---

## Ajuste de parâmetros
- **Temperatura** (0,0 – 1,0+): Controla a aleatoriedade. Inferior = mais determinístico, superior = mais criativo. Use 0,0–0,3 para respostas factuais; 0,7–1,0 para escrita criativa.
- **Top-p** (amostragem de núcleo): Corta a massa de probabilidade em um determinado limite cumulativo. 0,9 significa que o modelo mostra os 90% principais tokens prováveis. Normalmente ajuste a temperatura ou o top-p, não ambos.
- **Max tokens**: Define o comprimento máximo de saída. Lembre-se de reservar espaço para a resposta na janela de contexto.
- **Penalidade de frequência**: Reduz a repetição dos mesmos tokens.
- **Penalidade de presença**: incentiva o modelo a introduzir novos tópicos.
---

## Armadilhas e soluções comuns
| Problema | Causa provável | Correção |
|--------|-------------|-----|
| Modelo ignora partes do prompt | Prompt muito longo ou sobrecarregado | Encurtar; coloque a instrução mais importante no final |
| A saída é muito detalhada | Sem restrição de comprimento | Adicione "Limite a 3 frases" ou defina max_tokens |
| A saída é muito concisa | Excessivamente restritivo | Adicione "Explicar em detalhes" ou diminua a temperatura |
| Alucinações factuais | Contexto insuficiente ou pergunta ambígua | Adicione "Se não tiver certeza, diga 'Não sei'" e forneça um contexto RAG |
| Formatação inconsistente | Nenhuma instrução de formato explícita | Solicite JSON, tabela de descontos ou lista com marcadores |
| Modelo responde em linguagem errada | Sem instrução linguística | Indique explicitamente "Responder em inglês" (ou no idioma de destino) |
---

## Modelos de prompt para tarefas comuns
### Resumo
Resuma o texto a seguir em 3 marcadores. Concentre-se nos argumentos principais e evite detalhes.
Texto: [inserir texto]

### Geração de código
Escreva uma função [linguagem] que [faça X].
Requisitos:
Use dicas de tipo.
Incluir um documento.
Lidar com casos extremos: [lista].
Não use bibliotecas externas, a menos que especificado.

### Explicação
Explique [conceito] para um [não especialista/estudante universitário/criança]. Use uma analogia quando apropriado.
### Brainstorming
Gere 10 ideias para [tópico]. Para cada ideia, forneça uma descrição de uma frase e um desafio potencial.
texto
### Classificação
Classifique o seguinte feedback do cliente como [positivo, neutro, negativo].
Forneça uma pontuação de confiança (0-100) e um breve motivo.
Feedback: [inserir texto]
### Tradução com estilo
Traduza o seguinte texto em inglês para espanhol. Use um tom informal adequado para uma postagem nas redes sociais.
Texto: [inserir texto]
---

## Avaliação de prompts
Trate os prompts como código: crie versões deles, teste-os e repita.
- **Teste A/B** diferentes variantes de prompt em um conjunto retido de consultas.
- **Meça o sucesso** por meio de avaliação humana ou métricas automatizadas (por exemplo, correspondência exata, BLEU, pontuação personalizada).
- **Mantenha um registro de prompt** (um arquivo de texto simples ou planilha) com o prompt, versão e desempenho observado.
---