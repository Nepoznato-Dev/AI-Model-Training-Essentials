# Engenharia de Prompts

Engenharia de prompts é a prática de projetar, refinar e otimizar prompts de entrada para obter a melhor saída possível de um modelo de linguagem. É ao mesmo tempo uma arte e uma ciência, e constitui a principal interface para controlar o comportamento de LLMs sem recorrer a fine-tuning.

---

## Princípios Fundamentais

### Clareza e Especificidade
Um prompt claro não deixa espaço para ambiguidades. Especifique exatamente o que você quer, incluindo formato, extensão e perspectiva.

**Vago:**
> "Fale sobre Python."

**Específico:**
> "Explique o Global Interpreter Lock (GIL) do Python. Descreva seu impacto em multithreading, apresente uma alternativa contornando o problema e mantenha sua resposta com menos de 200 palavras."

### Forneça Contexto
Os modelos têm melhor desempenho quando conhecem o papel, o público e o objetivo.

**Sem contexto:**
> "Escreva uma função para ordenar uma lista."

**Com contexto:**
> "Você é um desenvolvedor Python sênior. Escreva uma função para ordenar uma lista de dicionários por uma chave fornecida. Use type hints e trate casos extremos. O público-alvo são desenvolvedores juniores."

### Use Instruções Positivas
Diga ao modelo o que fazer, e não o que evitar. "Não inclua jargões" é mais fraco do que "Use uma linguagem simples, acessível a uma criança de 10 anos."

---

## Estruturas de Prompt

### Papéis de System / User / Assistant
A maioria das APIs de LLM oferece suporte a uma estrutura de múltiplas interações:

- **Mensagem de sistema**: Define o comportamento, a persona e as restrições do modelo (permanece durante toda a sessão).
- **Mensagem do usuário**: A consulta ou instrução atual.
- **Mensagem do assistente**: As respostas anteriores do modelo (usadas para continuidade).

**Exemplo (estilo da API da OpenAI):**
System: You are a helpful coding assistant. You reply with concise code examples and brief explanations. Never provide unsafe code.
User: Write a Python function to download a file from a URL.

### Few-Shot Prompting
Forneça 2–3 exemplos do formato de entrada e saída desejado antes de pedir que o modelo execute a tarefa. Isso ensina o padrão.

**Exemplo:**
User: Convert these sentences to passive voice:
Input: The cat chased the mouse.
Output: The mouse was chased by the cat.
Input: The chef cooked the meal.
Output: The meal was cooked by the chef.
Input: The storm destroyed the house.
Output: (model completes)

### Cadeia de Pensamento (CoT)
Incentive o modelo a mostrar seu raciocínio passo a passo. Isso melhora a precisão em tarefas de aritmética, lógica e múltiplas etapas.

**Sem CoT:**
> "Quanto é 24 × 37?"

**Com CoT:**
> "Calcule 24 × 37. Mostre seu raciocínio passo a passo."

O modelo produzirá etapas intermediárias, reduzindo erros aritméticos.

### Saídas Estruturadas
Solicite um formato específico, como JSON, YAML ou tabelas em markdown, para tornar o parsing confiável.
User: Liste três vantagens e três desvantagens de microsserviços. Retorne apenas um objeto JSON válido com as chaves "pros" e "cons", cada uma contendo um array de strings.

---

## Técnicas Avançadas

### Autoconsistência
Gere várias respostas para o mesmo prompt (com temperature > 0) e use votação majoritária para a resposta final. Isso é especialmente eficaz para tarefas de raciocínio.

### Tree-of-Thoughts
Explore múltiplos caminhos de raciocínio em paralelo, avalie cada um e escolha o melhor. Esta é uma técnica de nível de pesquisa, mas pode ser aproximada pedindo ao modelo que "explore soluções alternativas".

### ReAct (Reasoning + Acting)
Permita que o modelo intercale raciocínio com chamadas de ferramentas. Ele pode pensar, depois agir (por exemplo, pesquisar na web, executar código) e então pensar novamente com base no resultado.

**Estrutura do prompt:**
You have access to a calculator and a search engine. For each step, output:
Thought: (your reasoning)
Action: (tool name, input)
Observation: (tool output)
... continue until you have the final answer.

### Atribuição de Persona
Atribua uma persona específica para orientar a resposta.

**Exemplos:**
- "Você é um desenvolvedor do kernel Linux explicando gerenciamento de memória para um recém-formado."
- "Você é um nutricionista amigável dando conselhos gerais a um cliente."
- "Você é um crítico de tecnologia cínico avaliando um novo gadget."

---

## Ajuste de Parâmetros

- **Temperature** (0.0 – 1.0+): Controla a aleatoriedade. Menor = mais determinístico, maior = mais criativo. Use 0.0–0.3 para respostas factuais; 0.7–1.0 para escrita criativa.
- **Top-p** (nucleus sampling): Corta a massa de probabilidade em um determinado limite cumulativo. 0.9 significa que o modelo amostra a partir dos 90% tokens mais prováveis. Em geral, ajuste temperature ou top-p, não ambos.
- **Max tokens**: Define o comprimento máximo da saída. Lembre-se de reservar espaço para a resposta dentro da janela de contexto.
- **Frequency penalty**: Reduz a repetição dos mesmos tokens.
- **Presence penalty**: Incentiva o modelo a introduzir novos tópicos.

---

## Armadilhas Comuns e Correções

| Problema | Causa provável | Correção |
|---------|--------------|-----|
| O modelo ignora partes do prompt | Prompt longo demais ou sobrecarregado | Encurte; coloque a instrução mais importante no final |
| A saída é verbosa demais | Não há restrição de tamanho | Adicione "Limite a 3 frases" ou defina max_tokens |
| A saída é breve demais | Restrições excessivas | Adicione "Explique em detalhes" ou reduza a temperature |
| Alucinações factuais | Contexto insuficiente ou pergunta ambígua | Adicione "Se não tiver certeza, diga 'não sei'" e forneça um contexto RAG |
| Formatação inconsistente | Não há instrução explícita de formato | Peça JSON, tabela em markdown ou lista com marcadores |
| O modelo responde no idioma errado | Não há instrução de idioma | Declare explicitamente "Responda em português" (ou no idioma desejado) |

---

## Modelos de Prompt para Tarefas Comuns

### Sumarização
Resuma o texto a seguir em 3 bullet points. Foque nos argumentos principais e evite detalhes.

Text: [insert text]


### Geração de Código
Escreva uma função em [linguagem] que [faça X].
Requisitos:

Use type hints.

Inclua uma docstring.

Trate os casos extremos: [lista].

Não use bibliotecas externas, a menos que especificado.


### Explicação
Explique [conceito] para um [leigo / estudante universitário / criança]. Use uma analogia quando apropriado.

### Brainstorming
Gere 10 ideias para [tópico]. Para cada ideia, forneça uma descrição de uma frase e um possível desafio.

texto

### Classificação
Classifique o seguinte feedback de cliente como [positivo, neutro, negativo].
Forneça uma pontuação de confiança (0-100) e uma justificativa breve.

Feedback: [insert text]

### Tradução com Estilo
Traduza o texto a seguir do inglês para o espanhol. Use um tom informal adequado para uma publicação em rede social.
Text: [insert text]

---

## Avaliação de Prompts

Trate prompts como código: versiona, teste e itere.

- **Faça testes A/B** com diferentes variantes de prompt em um conjunto separado de consultas.
- **Meça o sucesso** por meio de avaliação humana ou métricas automatizadas (por exemplo, exact match, BLEU, pontuação personalizada).
- **Mantenha um registro de prompts** (um arquivo de texto simples ou uma planilha) com o prompt, a versão e o desempenho observado.

---
