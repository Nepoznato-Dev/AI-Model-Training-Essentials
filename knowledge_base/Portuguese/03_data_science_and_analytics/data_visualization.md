<!--
---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
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
tags: [data, visualization, data-science-and-analytics]
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

-->
# Visualização de dados
Um gráfico bem desenhado pode revelar padrões que as tabelas de números escondem. Um projeto mal projetado pode enganar, confundir ou entediar. A visualização de dados é a arte de transformar dados em histórias visuais que informam decisões. Este arquivo cobre a seleção de gráficos, princípios de design, erros comuns e as ferramentas que tornam tudo isso possível.
---

## Escolhendo o gráfico certo
A decisão mais importante em qualquer visualização é escolher o tipo de gráfico certo para seus dados e mensagens.
### Guia de seleção de gráficos
| Seu objetivo | Melhores tipos de gráfico |
|-----------|-----------------|
| **Comparar categorias** | Gráfico de barras, gráfico de barras agrupadas |
| **Mostrar alterações ao longo do tempo** | Gráfico de linhas, gráfico de áreas |
| **Mostrar distribuição** | Histograma, gráfico de caixa, gráfico de violino |
| **Mostrar relacionamento** | Gráfico de dispersão, gráfico de bolhas |
| **Mostrar composição** | Barra empilhada, gráfico de pizza (fatias limitadas), mapa de árvore |
| **Mostrar correlação** | Gráfico de dispersão, mapa de calor, gráfico de pares |
| **Mostrar classificação** | Gráfico de barras horizontais |
| **Mostrar padrões geográficos** | Mapa coroplético, mapa de pontos |
| **Mostrar parte do todo ao longo do tempo** | Gráfico de áreas empilhadas |
### Quando usar cada gráfico
| Gráfico | Pontos fortes | Evite quando |
|-------|-----------|-----------|
| **Barra** | Comparações claras entre categorias | Muitas categorias (>15) |
| **Linha** | Tendências ao longo do tempo; dados contínuos | Os dados não são sequenciais |
| **Dispersão** | Relações entre duas variáveis ​​| Muitos pontos sobrepostos |
| **Histograma** | Forma de distribuição de uma variável | Amostras pequenas (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |
---

## Princípios de Design
### Ideias Centrais de Tufte
Os princípios de Edward Tufte continuam sendo o padrão ouro para visualização de dados:
| Princípio | Descrição |
|-----------|------------|
| **Maximizar a proporção de tinta de dados** | Cada gota de tinta deve transmitir dados. Remova todo o resto. |
| **Elimine o lixo gráfico** | Sem efeitos 3D, gradientes gratuitos ou elementos decorativos. |
| **Mostrar os dados** | Não distorça, esconda ou escolha a dedo. Deixe os dados falarem. |
| **Pequenos múltiplos** | Use pequenos gráficos repetidos para comparação entre categorias. |
| **Minigráficos** | Gráficos minúsculos do tamanho de palavras para dados de tendências embutidos. |
### Regras práticas de design
| Regra | Por que |
|------|-----|
| **Iniciar eixo y em zero** (para gráficos de barras) | Caso contrário você exagerará as diferenças |
| **Etiquete diretamente** | Coloque rótulos nas linhas/barras em vez de usar legenda quando possível |
| **Use cores propositalmente** | Destaque o que importa; use cinza para contexto |
| **Mantenha a simplicidade** | Uma mensagem por gráfico; não sobrecarregue |
| **Use escalas consistentes** | Ao comparar gráficos, mantenha os eixos iguais |
| **Peça de forma significativa** | Classifique as barras por valor (não em ordem alfabética), a menos que haja uma ordem natural |
| **Forneça contexto** | Adicione benchmarks, metas ou médias históricas |
### Diretrizes de cores
| Caso de uso | Abordagem |
|----------|----------|
| **Categórico** | Tons distintos (azul, laranja, verde, vermelho) — máx. 7–8 categorias |
| **Sequencial** | Claro a escuro de uma tonalidade (azul claro → azul escuro) |
| **Divergente** | Gradiente de dois tons para dados com um ponto médio significativo (vermelho ← branco → azul) |
| **Acessibilidade** | Teste com simuladores daltônicos; não confie apenas na cor (adicione rótulos ou padrões) |
---

## Contação de histórias com dados
Um gráfico sem narrativa é apenas uma imagem. Contar histórias transforma dados em insights.
### A Estrutura de Contação de Histórias
1. **Contexto**: Qual é a situação? O que o público já sabe?
2. **Conflito**: Qual é o problema, a surpresa ou a tensão nos dados?
3. **Resolução**: o que o público deve fazer com esse insight?
### Dicas Práticas
| Dica | Descrição |
|-----|-------------|
| **Lidere com insights** | Dê um título ao gráfico com o resultado, não com os dados ("A receita cresceu 30%" e não "Receita por trimestre") |
| **Anote os pontos principais** | Adicione textos explicativos para eventos importantes ou momentos decisivos |
| **Use divulgação progressiva** | Mostre um gráfico de cada vez; construa a história passo a passo |
| **Destaque o que importa** | Use cor ou tamanho para chamar a atenção para o principal ponto de dados |
| **Forneça um "e daí?"** | Cada gráfico deve responder a uma pergunta ou solicitar uma ação |
---

## Erros Comuns
| Erro | Por que é ruim | Correção |
|--------|-------------|-----|
| **Eixo y truncado** | Exagera pequenas diferenças | Comece do zero para gráficos de barras |
| **Intervalo de tempo de colheita** | Engana sobre tendências | Mostrar gama completa disponível |
| **Muitas cores** | Sobrecarrega o espectador | Limite a 5–7; use cinza para contexto |
| **Eixos y duplos** | Implica correlação que pode não existir | Use dois gráficos separados |
| **Gráficos 3D** | Distorce proporções | Sempre use 2D |
| **Gráficos circulares com mais de 10 fatias** | Impossível comparar | Use um gráfico de barras |
| **Rótulos ausentes** | O visualizador não consegue entender o gráfico | Sempre rotule eixos, títulos e unidades |
| **Gráficos de áreas enganosos** | As áreas empilhadas distorcem a percepção de séries individuais | Use gráficos de linhas ou pequenos múltiplos |
---

## Ferramentas
###Píton
| Biblioteca | Força |
|--------|----------|
| **matplotlib** | Fundação da plotagem Python; totalmente personalizável |
| **Nascido no mar** | Visualização estatística; belos padrões; construído em matplotlib |
| **enredo** | Gráficos interativos baseados na web; painéis |
| **altar** | Gramática declarativa de gráficos (Vega-Lite) |
| **bokeh** | Visualização interativa para navegadores |
###JavaScript/Web
| Biblioteca | Força |
|--------|----------|
| **D3.js** | Flexibilidade máxima; curva de aprendizado íngreme |
| **Gráfico.js** | Gráficos simples e responsivos |
| **Recargas** | Gráficos fáceis de reagir |
| **Gráfico Observável** | Gramática gráfica leve e expressiva |
### Ferramentas sem código/BI
| Ferramenta | Tipo |
|------|------|
| **Quadro** | Análise visual padrão do setor |
| **Power BI** | Ecossistema Microsoft; BI empresarial |
| **Olhador** | Google Nuvem; exploração de dados |
| **Metabase** | Código aberto; configuração simples |
| **Superconjunto Apache** | Código aberto; Nativo de SQL |
---

## Design do painel
Um painel é uma coleção de visualizações que juntas contam uma história completa sobre um processo, sistema ou negócio.
### Tipos de painel
| Tipo | Público | Finalidade |
|------|----------|--------|
| **Estratégico** | Executivos | KPIs de alto nível; tendências de longo prazo |
| **Operacional** | Gerentes | Monitoramento em tempo real; operações diárias |
| **Analítico** | Analistas | Exploração profunda; filtragem, detalhamento |
### Lista de verificação de projeto
- **Conheça seu público**: quais decisões eles tomarão neste painel?
- **Regra dos 5 segundos**: A conclusão principal pode ser compreendida em 5 segundos?
- **Layout**: métricas mais importantes no canto superior esquerdo (onde os olhos vão primeiro).
- **Limite de tipos de gráfico**: no máximo 3 a 4 tipos por painel para maior consistência.
- **Interativo por padrão**: filtros, seletores de intervalo de datas, detalhamentos.
- **Desempenho**: painéis que levam mais de 5 segundos para carregar não são usados.
- **Dispositivos móveis**: considere um design responsivo se os usuários precisarem dele em qualquer lugar.
---

## Resumo
Uma boa visualização de dados envolve clareza, honestidade e impacto. Escolha o gráfico certo para seus dados. Remova tudo o que não serve à mensagem. Use cores e anotações para orientar o visualizador. E sempre, sempre deixe os dados contarem a história – e não o contrário.