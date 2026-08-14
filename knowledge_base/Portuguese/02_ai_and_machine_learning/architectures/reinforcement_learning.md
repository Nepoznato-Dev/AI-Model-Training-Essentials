---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [reinforcement, learning, ai-and-machine-learning]
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

# Aprendizagem por Reforço
O aprendizado por reforço (RL) é como as máquinas aprendem a tomar sequências de decisões por tentativa e erro. Ao contrário da aprendizagem supervisionada, onde a resposta correta é fornecida para cada exemplo, a RL dá ao agente apenas um sinal de recompensa – e o agente deve descobrir quais ações levam aos melhores resultados ao longo do tempo. É a abordagem por trás do AlphaGo, do controle robótico, da IA ​​de jogos e - principalmente - do RLHF, a técnica usada para alinhar grandes modelos modernos de linguagem com as preferências humanas.
---

## Conceitos Básicos
RL enquadra a tomada de decisão como um ciclo entre um **agente** e um **ambiente**.
| Componente | Função | Exemplo |
|-----------|------|--------|
| **Agente** | O tomador de decisão | Um programa de xadrez, um robô, um modelo de linguagem |
| **Meio Ambiente** | O mundo com o qual o agente interage | O tabuleiro de xadrez, um armazém, uma conversa |
| **Estado** | A situação atual | Posição do tabuleiro, leituras de sensores do robô, histórico de bate-papo |
| **Ação** | O que o agente pode fazer | Mova uma peça, vire à esquerda, gere uma ficha |
| **Recompensa** | Sinal de feedback (número escalar) | +1 para vitória, -1 para falha, pontuação de preferência humana |
| **Política** | Estratégia mapeando estados para ações | “Se o rei estiver ameaçado, mova-o” |
| **Função de valor** | Recompensa cumulativa esperada de um estado | “Esta posição no conselho vale cerca de +3 pontos” |
### O ciclo RL
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

O objetivo do agente é maximizar a **recompensa cumulativa** ao longo do tempo, e não apenas a recompensa imediata. Isto é o que torna a RL fundamentalmente diferente da aprendizagem supervisionada.
---

## Principais diferenças de outros paradigmas de aprendizagem
| Aspecto | Aprendizagem Supervisionada | Aprendizagem não supervisionada | Aprendizagem por Reforço |
|--------|-------------------|---------------------|----------------------|
| **Sinal** | Etiquetas corretas para cada exemplo | Sem rótulos; encontrar estrutura | Recompensa escalar, muitas vezes atrasada |
| **Comentários** | Imediato | Nenhum | Atrasado e escasso |
| **Sequência** | Cada exemplo é independente | Cada exemplo é independente | Ações afetam estados futuros |
| **Meta** | Minimizar o erro de previsão | Descubra padrões | Maximizar a recompensa cumulativa |
---

## Processos de Decisão Markov (MDPs)
MDPs são a estrutura matemática para RL. Eles assumem que o futuro depende apenas do estado atual, não da história de como você chegou lá (a **propriedade de Markov**).
| Componente | Notação | Significado |
|----------|----------|--------|
| **Estados** | S | Todas as situações possíveis em que o agente pode estar |
| **Ações** | Um | Todas as coisas que o agente pode fazer |
| **Função de transição** | P(s' \| s, a) | Probabilidade de alcançar os estados após a ação a nos estados |
| **Função de recompensa** | R(s, a, s') | Recompensa recebida pela transição |
| **Fator de desconto** | γ (gama) | Quanto avaliar as recompensas futuras versus as imediatas (0 a 1) |
O **retorno** (recompensa total com desconto) é:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Um fator de desconto alto (γ próximo de 1) significa que o agente tem visão de futuro. Um valor baixo significa que é míope.
---

## Algoritmos RL Clássicos
### Métodos Baseados em Valores
Eles aprendem quão bom é cada estado (ou par estado-ação).
| Algoritmo | Ideia-chave | Limitação |
|-----------|----------|------------|
| **Q-Learning** | Aprenda uma tabela de valores Q: Q(estado, ação) = recompensa esperada | Não se adapta a grandes espaços de estado |
| **Rede Q Profunda (DQN)** | Use uma rede neural para aproximar valores Q | Lida apenas com ações discretas; pode ser instável |
| **DQN duplo** | Corrigir o viés de superestimação do Q-learning | Ainda limitado a ações discretas |
Regra de atualização do Q-learning:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Métodos baseados em políticas
Estes aprendem diretamente a política (estratégia) sem estimar valores.
| Algoritmo | Ideia-chave | Vantagem |
|-----------|----------|-----------|
| **REFORÇAR** | Gradiente político de Monte Carlo; atualizar política em direção a bons resultados | Simples; trabalha com ações contínuas |
| **PPO** (Otimização de Política Proximal) | Corte atualizações de políticas para evitar mudanças grandes e desestabilizadoras | Estável; amplamente utilizado; bom padrão |
| **TRPO** | Método de região confiável para atualizações de políticas | Mais princípios do que PPO; mais difícil de implementar |
### Métodos Ator-Crítico
Combine o melhor de ambos: um **ator** (política) e um **crítico** (função de valor).
| Algoritmo | Ideia-chave |
|-----------|----------|
| **A2C/A3C** | Vantagem Ator-Crítico; usa estimativa de vantagem para reduzir variância |
| **SAC** (Ator-Crítico Suave) | Maximizar a recompensa mantendo a exploração (regularização da entropia) |
| **TD3** (DDPG duplo atrasado) | Abordar a superestimação em espaços de ação contínua |
---

## RLHF: Aprendizagem por Reforço com Feedback Humano
RLHF é a técnica que tornou o ChatGPT possível. Ele preenche a lacuna entre um modelo que pode prever texto e outro que produz resultados que os humanos realmente consideram úteis.
### As Três Etapas
| Etapa | O que acontece | Saída |
|------|------------|--------|
| **1. Afinação fina supervisionada (SFT)** | Ajustar um modelo pré-treinado em exemplos escritos por humanos de alta qualidade | Um modelo que segue razoavelmente bem as instruções |
| **2. Treinamento de modelo de recompensa** | Os humanos comparam pares de resultados do modelo; treinar um modelo para prever preferências humanas | Um modelo de recompensa que avalia a qualidade da produção |
| **3. Otimização RL** | Use PPO para ajustar o modelo SFT para maximizar as pontuações do modelo de recompensa | Um modelo alinhado às preferências humanas |
### Por que RLHF é importante
Sem RLHF, um modelo de linguagem é como um aluno que leu todos os livros, mas não sabe como se comportar durante uma conversa. Ele pode gerar texto, mas o texto pode ser inútil, tóxico ou perder totalmente o foco. RLHF ensina ao modelo *o que os humanos querem* - não apenas a aparência do texto.
### Variantes e Alternativas
| Método | Descrição | Vantagem |
|--------|-------------|-----------|
| **DPO** (Otimização de preferência direta) | Ignore o modelo de recompensa; otimizar diretamente a política a partir das preferências humanas | Mais simples; nenhum modelo de recompensa separado para treinar |
| **RLAIF** | Use IA (em vez de humanos) para gerar rótulos de preferência | Mais barato que a rotulagem humana |
| **IA Constitucional** | Use um conjunto de princípios para orientar o comportamento do modelo sem rótulos humanos | Mais escalável; Abordagem da Antrópica |
| **GRPO** (Otimização de Política Relativa de Grupo) | Comparar os resultados dentro de um grupo e não com um modelo separado | Usado no DeepSeek-R1; reduz necessidade de rede de valor |
---

## Exploração vs Exploração
Esta é a tensão central em RL. **Exploração** significa escolher ações que você sabe que funcionam bem. **Exploração** significa tentar coisas novas para descobrir estratégias potencialmente melhores.
| Estratégia | Como funciona | Compensação |
|----------|-------------|-----------|
| **ε-ganancioso** | Escolha a melhor ação na maioria das vezes; ação aleatória com probabilidade ε | Simples, mas ineficiente |
| **Exploração Boltzmann** | Escolha as ações probabilisticamente com base nos seus valores estimados | Mais suave que ε-ganancioso |
| **UCB** (Limite Superior de Confiança) | Prefere ações com elevada incerteza (otimismo face à incerteza) | Boas garantias teóricas |
| **Regularização de entropia** | Adicione bônus por visitar diversos estados (usado em SAC, PPO) | Incentiva a exploração natural |
---

## Aprendizado por reforço multiagente
Quando vários agentes aprendem simultaneamente, a dinâmica torna-se muito mais complexa.
| Cenário | Desafio | Exemplo |
|----------|-----------|--------|
| **Cooperativa** | Os agentes devem coordenar; atribuição de crédito é difícil | Times de futebol robóticos; redes de sensores distribuídas |
| **Competitivo** | Os oponentes se adaptam; o ambiente não é estacionário | IA de jogo (pôquer, StarCraft); cibersegurança |
| **Misto** | Alguns agentes cooperam, outros competem | Mercados de leilões; sistemas de tráfego |
| Algoritmo | Descrição |
|-----------|------------|
| **MADDPG** | Versão multiagente do DDPG; crítico centralizado, atores descentralizados |
| **MAPPO** | PPO multiagente; amplamente utilizado na prática |
| **Jogo automático** | Agentes treinam contra cópias de si mesmos (AlphaGo, AlphaStar) |
---

## Transferência Sim para Real
Treinar robôs no mundo real é lento e perigoso. Em vez disso, os agentes treinam em simulação e transferem para a realidade.
| Desafio | Solução |
|-----------|----------|
| **Lacuna de realidade** (simulação ≠ mundo real) | Randomização de domínio: variação dos parâmetros físicos durante o treinamento |
| **Ineficiência da amostra** | Use RL baseado em modelo ou treine em grandes simulações paralelas |
| **Segurança** | RL restrito: penalizar ações inseguras durante o treinamento |
| **Observabilidade parcial** | Treine com sensores barulhentos e observações atrasadas |
Empresas como Boston Dynamics e Tesla usam extensivamente a simulação, mas a lacuna entre o desempenho simulado e o desempenho físico continua sendo um dos maiores desafios da área.
---

## Ferramentas e Estruturas
| Ferramenta | Finalidade | Melhor para |
|------|---------|----------|
| **Linhas de base estáveis3** | Implementações limpas em Python de PPO, SAC, TD3, DQN | Aprendizagem e prototipagem |
| **RLlib** | Biblioteca RL escalável construída em Ray | Treinamento distribuído em grande escala |
| **LimparRL** | Implementações de arquivo único para pesquisa | Compreendendo profundamente os algoritmos |
| **Ginásio (OpenAI)** | Interface de ambiente padronizado | Definindo problemas de RL |
| **Isaac Gym / Isaac Lab** | Simulação de física acelerada por GPU | Robótica, da simulação para a realidade |
| **TRL** (Biblioteca Transformer RL) | RLHF, DPO, PPO para modelos de linguagem | Alinhando LLMs |
| **AbertoRLHF** | Estrutura RLHF distribuída | Treinamento de modelos grandes com RLHF |
---

## Dicas Práticas
- **Comece com PPO.** É o algoritmo de uso geral mais confiável. Se você não tiver certeza do que usar, o PPO é o padrão.
- **Normalize suas recompensas.** O escalonamento de recompensas afeta drasticamente a estabilidade do treinamento.
- **Use ambientes vetorizados.** A execução de muitos ambientes em paralelo (por exemplo, 8–64) estabiliza as estimativas de gradiente e acelera enormemente o treinamento.
- **Monitore a recompensa e a entropia.** Se a entropia cair para zero, seu agente parou de explorar e pode ficar preso em um ótimo local.
- **Modelar recompensas é uma arte.** Projetar a função de recompensa certa costuma ser a parte mais difícil. Recompensas escassas (apenas no final) tornam o aprendizado extremamente lento. Recompensas densas e bem definidas orientam o agente, mas podem introduzir comportamento não intencional.
- **RLHF é frágil.** Pequenas alterações no modelo de recompensa ou nos hiperparâmetros PPO podem causar grandes quedas de qualidade. O DPO é uma alternativa mais estável se você não precisar do pipeline RLHF completo.
---

## Resumo
A aprendizagem por reforço é o estudo de como os agentes aprendem a tomar decisões por meio da interação. Ele varia de algoritmos clássicos, como Q-learning, a métodos modernos de RL profundo, como PPO e SAC, e sustenta alguns dos avanços recentes mais importantes em IA – desde o jogo até o alinhamento do modelo de linguagem. O desafio central permanece o mesmo: como aprender o comportamento ideal quando o feedback é atrasado, escasso e barulhento? A resposta – tentativa e erro, guiada por matemática inteligente – acaba por ser uma das ideias mais poderosas de toda a inteligência artificial.