<!--
---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Inferência Causal
A inferência causal é a ciência que determina se uma coisa realmente causa outra – e não apenas se elas estão correlacionadas. A correlação informa que duas variáveis ​​se movem juntas. A causalidade lhe diz que mudar um mudará o outro. Esta distinção é extremamente importante na medicina (este medicamento funciona?), na política (esta intervenção reduz a pobreza?), nos negócios (esta campanha publicitária aumenta as vendas?) e na ciência (este mecanismo explica o fenómeno?).
---

## Correlação vs Causalidade
| Conceito | Descrição | Exemplo |
|---------|-------------|---------|
| **Correlação** | Duas variáveis ​​se movem juntas | Vendas de sorvete e mortes por afogamento aumentam no verão |
| **Causalidade** | Uma variável afeta diretamente outra | Fumar causa câncer de pulmão |
| **Confundido** | Uma terceira variável causa ambos | Clima quente causa venda de sorvete e natação (e afogamento) |
| **Causalidade reversa** | O efeito realmente causa a suposta causa | As pessoas compram suplementos de saúde porque estão doentes, e não o contrário |
| **Correlação espúria** | Relacionamento coincidente | Consumo per capita de queijo se correlaciona com mortes por emaranhamento de lençóis |
---

## A Estrutura de Resultados Potenciais
### Modelo Causal Rubin
| Conceito | Descrição |
|--------|-------------|
| **Resultados potenciais** | Para cada unidade, há um resultado se tratado Y(1) e um resultado se não tratado Y(0) |
| **Efeito do tratamento** | A diferença: Y(1) - Y(0) para uma determinada unidade |
| **Problema fundamental** | Nunca podemos observar Y(1) e Y(0) para a mesma unidade — só podemos ver um |
| **Efeito médio do tratamento (ATE)** | A média dos efeitos do tratamento individual na população |
| **Contrafactual** | O resultado não observado — o que teria acontecido na outra condição |
### Principais suposições
| Suposição | Significado | Como satisfazer |
|-----------|--------|----------------|
| **Ignorabilidade (inconfundibilidade)** | A atribuição do tratamento é independente dos resultados potenciais, dadas as covariáveis ​​observadas | Randomização; medir todos os fatores de confusão |
| **Positividade (sobreposição)** | Cada unidade tem probabilidade diferente de zero de receber qualquer um dos tratamentos | Verifique a sobreposição de covariáveis ​​entre grupos |
| **SUTVA** (suposição de valor de tratamento unitário estável) | O tratamento de uma unidade não afeta o resultado de outra; tratamento é consistente | Nenhuma interferência; não há versões ocultas de tratamento |
| **Consistência** | O resultado observado é igual ao resultado potencial do tratamento recebido | Tratamento bem definido |
---

## Métodos para Inferência Causal
### Métodos Experimentais
| Método | Descrição | Força | Limitação |
|--------|-------------|----------|------------|
| **Ensaio controlado randomizado (ECR)** | Atribuir aleatoriamente unidades para tratamento ou controle | Padrão ouro; elimina confusão | Caro; às vezes antiético; não pode generalizar |
| **Teste A/B** | RCT num contexto empresarial/tecnológico | Simples; rigoroso | Métricas de curto prazo; efeitos de novidade; interferência |
| **Experiências de retorno** | Tratamento alternativo ao longo de períodos de tempo | Lida com interferências em mercados | Requer ambiente estável |
### Métodos Quase Experimentais
| Método | Descrição | Suposição principal |
|--------|-------------|----------------|
| **Diferença em diferenças (DiD)** | Compare a mudança nos resultados entre os grupos tratados e de controle ao longo do tempo | Tendências paralelas: grupos teriam seguido a mesma trajetória sem tratamento |
| **Descontinuidade de regressão (RD)** | Compare as unidades logo acima e logo abaixo do ponto de corte do tratamento | As unidades próximas do ponto de corte são comparáveis ​​(como se fossem aleatórias) |
| **Variáveis ​​instrumentais (IV)** | Use uma variável que afete o tratamento, mas não o resultado, exceto através do tratamento | O instrumento está correlacionado com o tratamento; afeta o resultado apenas através do tratamento |
| **Controle sintético** | Construir uma combinação ponderada de unidades de controle para corresponder à unidade tratada | O controle sintético representa com precisão o cenário contrafactual da unidade tratada |
| **Correspondência de pontuação de propensão** | Corresponder unidades tratadas e unidades de controlo com probabilidades de tratamento semelhantes | Todos os fatores de confusão são medidos e incluídos no modelo de propensão |
### Diferença em diferenças (visualizada)
| Período | Grupo Tratado | Grupo de Controle | Diferença |
|--------|-------------|---------------|------------|
| **Pré-tratamento** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Pós-tratamento** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **Estimativa DiD** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Gráficos Acíclicos Direcionados (DAGs)
DAGs são ferramentas visuais para codificar suposições causais e identificar fatores de confusão.
### Estruturas Básicas
| Estrutura | Padrão | Implicação |
|-----------|---------|------------|
| **Corrente** | A → B → C | A e C estão associados através de B; controlar para B bloqueia o caminho |
| **Garfo** | A ← B → C | A e C são confundidos por B; controlar para B bloqueia o caminho |
| **Colisor** | A → B ← C | A e C são independentes; controlar para B abre o caminho (cria associação espúria) |
### Regras para DAGs
| Regra | Descrição |
|------|-------------|
| **Critério backdoor** | Para estimar o efeito causal de X em Y, bloqueie todos os caminhos de backdoor (caminhos com uma seta para X) condicionando as variáveis ​​apropriadas |
| **Critério da porta da frente** | Se os caminhos dos backdoors não puderem ser bloqueados, use mediadores: estime X → M → Y em dois estágios |
| **Não condicione colisores** | Controlar um efeito comum abre um caminho espúrio |
| **Não condicione descendentes de colisores** | O mesmo problema do condicionamento no próprio colisor |
---

## Armadilhas Comuns
| Armadilha | Descrição | Exemplo |
|---------|-------------|---------|
| **Viés de variável omitida** | Falha no controle de um fator de confusão | Estimando a educação → rendimentos sem controlar a capacidade |
| **Excesso de controle** | Condicionamento em mediador ou colisor | Controle do cargo ao estimar a escolaridade → rendimentos |
| **Viés de seleção** | Condicionamento sobre uma variável afetada pelo tratamento | Analisando apenas pessoas empregadas quando estudam formação → salários |
| **Viés de tempo imortal** | Classificação incorreta do tempo-pessoa em estudos de coorte | Os pacientes devem sobreviver o tempo suficiente para receber tratamento |
| **Regressão à média** | Valores extremos tendem a aproximar-se da média | Pacientes doentes melhoram após tratamento independentemente |
| **Viés pós-tratamento** | Condicionamento em variáveis ​​que ocorrem após o tratamento | Controle de eventos adversos ao estimar a eficácia do medicamento |
---

## Ferramentas e bibliotecas
| Ferramenta | Idioma | Descrição |
|------|----------|------------|
| **DoPorquê** | Pitão | Biblioteca da Microsoft; Inferência causal baseada em DAG |
| **MLCausal** | Pitão | Biblioteca da Uber para modelagem de elevação e ML causal |
| **EconML** | Pitão | Double ML, florestas causais, variáveis ​​instrumentais |
| **modelos lineares** | Pitão | IV, modelos de dados em painel, DiD |
| **Combinação** | R | Correspondência de pontuação de propensão |
| **dagitty** | R/teia | Análise DAG; identificar conjuntos de ajuste |
| **Impacto Causal** | R/Python | Séries temporais estruturais bayesianas para inferência causal |
---

## Resumo
A inferência causal consiste em ir além do “o que aconteceu” para “o que teria acontecido se as coisas fossem diferentes”. O desafio fundamental é que nunca podemos observar os resultados tratados e não tratados para a mesma unidade – falta sempre o contrafactual. Experimentos randomizados resolvem isso tornando comparáveis ​​os grupos de tratamento e controle. Quando a aleatorização não é possível, métodos quase experimentais — DiD, descontinuidade de regressão, variáveis ​​instrumentais, controlo sintético — tentam reconstruir o contrafactual a partir de dados observacionais. Os DAGs ajudam a tornar as suposições explícitas e a identificar as variáveis ​​certas a serem controladas. A habilidade principal é pensar cuidadosamente sobre o processo de geração de dados: o que causa o quê, o que é um fator de confusão, o que é um colisor e o que teria acontecido na alternativa.