# Engenharia de Prompts

Engenharia de prompts é a prática de projetar, refinar e otimizar prompts de entrada para obter a melhor saída possível de um modelo de linguagem. Ela é ao mesmo tempo uma arte e uma ciência, e é a principal interface para controlar o comportamento de LLMs sem recorrer a fine-tuning.

---

## Princípios Fundamentais

### Clareza e Especificidade
Um prompt claro não deixa espaço para ambiguidade. Especifique exatamente o que você quer, incluindo formato, extensão e perspectiva.

**Vago:**
> "Fale sobre Python."

**Específico:**
> "Explique o Global Interpreter Lock (GIL) do Python. Descreva seu impacto em multithreading, dê uma alternativa contornando a limitação e mantenha sua resposta com menos de 200 palavras."

### Forneça Contexto
Os modelos têm melhor desempenho quando conhecem o papel, o público e o objetivo.

**Sem contexto:**
> "Escreva uma função para ordenar uma lista."

**Com contexto:**
> "Você é um desenvolvedor Python sênior. Escreva uma função para ordenar uma lista de dicionários por uma chave específica. Use type hints e trate edge cases. O público são desenvolvedores júnior."

### Use Instruções Positivas
Diga ao modelo o que fazer, não apenas o que evitar. "Não use jargão" é mais fraco do que "Use linguagem simples, acessível a uma criança de 10 anos".

---

## Estruturas de Prompt

### Papéis de System / User / Assistant
A maioria das APIs de LLM oferece suporte a uma estrutura multi-turn:

- **System message**: Define o comportamento, a persona e as restrições do modelo (persistem durante toda a sessão).
- **User message**: A consulta ou instrução atual.
- **Assistant message**: As respostas anteriores do modelo (usadas para continuidade).

**Exemplo (estilo OpenAI API):**
System: Você é um assistente útil de programação. Responda com exemplos de código concisos e explicações breves. Nunca forneça código inseguro.
User: Escreva uma função em Python para baixar um arquivo a partir de uma URL.

### Few-Shot Prompting
Forneça 2–3 exemplos do formato desejado de entrada e saída antes de pedir ao modelo para executar a tarefa. Isso ensina o padrão.

**Exemplo:**
User: Converta estas frases para a voz passiva:
Input: O gato perseguiu o rato.
Output: O rato foi perseguido pelo gato.
Input: O chef cozinhou a refeição.
Output: A refeição foi cozinhada pelo chef.
Input: A tempestade destruiu a casa.
Output: (o modelo completa)

### Chain-of-Thought (CoT)
Incentive o modelo a mostrar o raciocínio passo a passo. Isso melhora a precisão em tarefas de aritmética, lógica e múltiplas etapas.

**Sem CoT:**
> "Quanto é 24 × 37?"

**Com CoT:**
> "Calcule 24 × 37. Mostre seu raciocínio passo a passo."

O modelo produzirá etapas intermediárias, reduzindo erros aritméticos.

### Saídas Estruturadas
Solicite um formato específico, como JSON, YAML ou tabelas em markdown, para tornar o parsing confiável.
User: Liste três prós e três contras de microservices. Retorne apenas um objeto JSON válido com as chaves "pros" e "cons", cada uma sendo um array de strings.

---

## Técnicas Avançadas

### Autoconsistência
Gere múltiplas respostas para o mesmo prompt (com temperatura > 0) e faça uma votação majoritária para a resposta final. Isso é especialmente eficaz para tarefas de raciocínio.

### Tree-of-Thoughts
Explore múltiplos caminhos de raciocínio em paralelo, avalie cada um e escolha o melhor. Esta é uma técnica de nível de pesquisa, mas pode ser aproximada pedindo ao modelo que "explore soluções alternativas".

### ReAct (Reasoning + Acting)
Permita que o modelo intercale raciocínio com chamadas de ferramentas. Ele pode pensar, agir (por exemplo, pesquisar na web, executar código) e depois pensar novamente com base no resultado.

**Estrutura do prompt:**
Você tem acesso a uma calculadora e a um mecanismo de busca. Em cada etapa, produza:
Thought: (seu raciocínio)
Action: (nome da ferramenta, entrada)
Observation: (saída da ferramenta)
... continue até chegar à resposta final.

### Atribuição de Persona
Atribua uma persona específica para enquadrar a resposta.

**Exemplos:**
- "Você é um desenvolvedor do kernel Linux explicando gerenciamento de memória para um recém-formado."
- "Você é um nutricionista amigável dando conselhos gerais a um cliente."
- "Você é um crítico de tecnologia cínico analisando um novo gadget."

---

## Ajuste de Parâmetros

- **Temperature** (0.0 – 1.0+): Controla a aleatoriedade. Menor = mais determinístico; maior = mais criativo. Use 0.0–0.3 para respostas factuais; 0.7–1.0 para escrita criativa.
- **Top-p** (nucleus sampling): Corta a massa de probabilidade em um determinado limite cumulativo. 0.9 significa que o modelo amostra a partir dos 90% tokens mais prováveis. Em geral, ajuste temperatura ou top-p, não ambos.
- **Max tokens**: Define o tamanho máximo da saída. Lembre-se de reservar espaço para a resposta dentro da janela de contexto.
- **Frequency penalty**: Reduz a repetição dos mesmos tokens.
- **Presence penalty**: Incentiva o modelo a introduzir novos tópicos.

---

## Problemas Comuns e Correções

| Problema | Causa provável | Correção |
|---------|--------------|-----|
| O modelo ignora partes do prompt | Prompt muito longo ou sobrecarregado | Encurte; coloque a instrução mais importante no final |
| A saída é verbosa demais | Não há restrição de tamanho | Adicione "Limite a 3 frases" ou defina max_tokens |
| A saída é curta demais | Restrições excessivas | Adicione "Explique em detalhes" ou reduza a temperatura |
| Alucinações factuais | Contexto insuficiente ou pergunta ambígua | Adicione "Se não tiver certeza, diga 'não sei'" e forneça um contexto de RAG |
| Formatação inconsistente | Não há instrução explícita de formato | Peça JSON, tabela em markdown ou lista com marcadores |
| O modelo responde no idioma errado | Não há instrução de idioma | Declare explicitamente "Responda em inglês" (ou no idioma desejado) |

---

## Templates de Prompt para Tarefas Comuns

### Sumarização
Resuma o texto a seguir em 3 bullet points. Foque nos principais argumentos e evite detalhes.

Texto: [insira o texto]


### Geração de Código
Escreva uma função em [linguagem] que [faça X].
Requisitos:

Use type hints.

Inclua uma docstring.

Trate os seguintes edge cases: [lista].

Não use bibliotecas externas, a menos que isso seja especificado.


### Explicação
Explique [conceito] para um [leigo / estudante universitário / criança]. Use uma analogia quando apropriado.

### Brainstorming
Gere 10 ideias para [tópico]. Para cada ideia, dê uma descrição de uma frase e um possível desafio.

text

### Classificação
Classifique o seguinte feedback de cliente como [positivo, neutro, negativo].
Forneça uma pontuação de confiança (0-100) e um motivo breve.

Feedback: [insira o texto]

### Tradução com Estilo
Traduza o texto a seguir do inglês para o espanhol. Use um tom informal adequado para uma publicação em redes sociais.
Texto: [insira o texto]

---

## Avaliação de Prompts

Trate prompts como código: versione, teste e itere.

- **Faça testes A/B** com diferentes variantes de prompt em um conjunto separado de consultas.
- **Meça o sucesso** por meio de avaliação humana ou métricas automatizadas (ex.: exact match, BLEU, pontuação personalizada).
- **Mantenha um registro de prompts** (um arquivo de texto simples ou planilha) com o prompt, a versão e o desempenho observado.

---
