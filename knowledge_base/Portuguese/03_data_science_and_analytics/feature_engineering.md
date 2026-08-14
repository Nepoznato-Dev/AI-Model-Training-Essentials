<!--
---
# Metadata
title: "Feature Engineering"
description: "Transformations, encodings, feature selection, dimensionality reduction"
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
tags: [feature, engineering, data-science-and-analytics]
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
# Engenharia de recursos
A engenharia de recursos é o processo de transformar dados brutos em representações que tornam os modelos de aprendizado de máquina mais eficazes. Muitas vezes é descrito como a etapa mais importante no pipeline de ML – os recursos que você fornece a um modelo são mais importantes do que o algoritmo que você escolhe. Um modelo simples com recursos bem elaborados normalmente superará um modelo complexo com entradas brutas e não processadas. A arte reside em compreender o domínio e os dados suficientemente bem para criar sinais com os quais o modelo possa aprender.
---

## Por que a engenharia de recursos é importante
| Fator | Impacto |
|--------|--------|
| **Qualidade do sinal** | Melhores recursos = padrões mais claros para o modelo aprender |
| **Simplicidade do modelo** | Bons recursos permitem que modelos mais simples tenham um bom desempenho; menor necessidade de arquiteturas complexas |
| **Velocidade de treinamento** | Recursos relevantes e bem dimensionados convergem mais rapidamente |
| **Generalização** | Recursos informados por domínio ajudam os modelos a trabalhar com dados invisíveis |
| **Interpretabilidade** | Recursos significativos são mais fáceis de explicar às partes interessadas |
---

## Tipos de transformações de recursos
### Transformações Numéricas
| Transformação | Fórmula / Descrição | Quando usar |
|---------------|----------------------|------------|
| **Transformação de log** | log(x) ou log(x + 1) | Distribuições distorcidas à direita; valores monetários |
| **Raiz quadrada** | quadrado(x) | Inclinação moderada; contar dados |
| **Caixa-Cox** | Transformada paramétrica que encontra a melhor transformação de potência | Tornando os dados distribuídos de forma mais normal |
| **Yeo Johnson** | Como Box-Cox, mas lida com valores negativos | Dados distorcidos com valores negativos |
| **Padronização** | (x - média) / padrão | Recursos com diferentes escalas; algoritmos assumindo normalidade |
| **Escalonamento mínimo-máximo** | (x - min) / (máx - min) | Limitando recursos para [0, 1]; valores de pixel da imagem |
| **Escalonamento robusto** | (x - mediana) / AIQ | Dados com valores discrepantes |
| **Binning** | Converter contínuo em categórico | Relações não lineares; árvores de decisão |
| **Recursos polinomiais** | x², x³, x₁×x₂ | Capturando relacionamentos não lineares em modelos lineares |
### Codificações Categóricas
| Codificação | Descrição | Quando usar |
|----------|-------------|-------------|
| **Codificação one-hot** | Crie uma coluna binária para cada categoria | Categorias de baixa cardinalidade; modelos baseados em árvore lidam nativamente |
| **Codificação de etiqueta** | Atribuir número inteiro a cada categoria | Categorias ordinais; modelos baseados em árvore |
| **Codificação de destino** | Substituir categoria pela média da variável alvo | Categorias de alta cardinalidade; evite overfitting com suavização |
| **Codificação de frequência** | Substitua a categoria pela sua contagem ou frequência | Quando a própria frequência é informativa |
| **Codificação binária** | Converter categorias codificadas por números inteiros em dígitos binários | Alta cardinalidade; reduz dimensionalidade vs one-hot |
| **Incorporação** | Aprenda representação vetorial densa | Cardinalidade muito alta; PNL; sistemas de recomendação |
| **Codificação hash** | Categorias de hash para um número fixo de recursos | Cardinalidade muito alta; aprendizagem on-line |
### Recursos de data e hora
| Recurso | Descrição |
|--------|-------------|
| **Hora do dia** | Captura padrões diários (hora do rush, período noturno) |
| **Dia da semana** | Efeitos durante a semana vs fim de semana |
| **Mês/trimestre** | Padrões sazonais |
| **É fim de semana** | Bandeira binária para fim de semana |
| **É feriado** | Bandeira binária para feriados |
| **Tempo desde o evento** | Dias desde a última compra; horas desde o último login |
| **Codificação cíclica** | sin(2π × hora / 24), cos(2π × hora / 24) — preserva a natureza circular do tempo |
---

## Lidando com valores ausentes
| Estratégia | Descrição | Quando usar |
|----------|-------------|-------------|
| **Eliminar linhas** | Remover linhas com valores ausentes | Os dados faltantes são uma pequena fração; MCAR (ausente completamente ao acaso) |
| **Descartar colunas** | Remover recursos com muitos valores ausentes | O recurso está quase ausente; não é importante |
| **Imputação de média/mediana** | Preencha com a média ou mediana do recurso | Simples; preserva a média, mas reduz a variância |
| **Imputação de modo** | Preencha categórico com valor mais frequente | Características categóricas |
| **Imputação KNN** | Use k-vizinhos mais próximos para estimar o valor faltante | Quando instâncias semelhantes ajudam a prever o valor ausente |
| **Imputação baseada em modelo** | Treinar um modelo para prever valores ausentes | Mais preciso; computacionalmente caro |
| **Indicador ausente** | Adicionar uma coluna binária sinalizando falta | Quando a falta em si é informativa |
| **Interpolação** | Preencher com valores interpolados (linear, spline) | Séries temporais; dados encomendados |
---

## Seleção de recursos
### Métodos de filtro
| Método | Descrição |
|--------|------------|
| **Correlação** | Remover recursos altamente correlacionados entre si |
| **Limite de variação** | Remover recursos com variação próxima de zero |
| **Informação mútua** | Medir informações que cada recurso fornece sobre o alvo |
| **Qui-quadrado** | Testar a independência entre características categóricas e alvo |
| **Teste ANOVA F** | Testar se as médias das características numéricas diferem entre as classes alvo |
### Métodos de wrapper
| Método | Descrição |
|--------|------------|
| **Seleção direta** | Comece vazio; adicione o melhor recurso, um de cada vez |
| **Eliminação reversa** | Comece com todos; remova o pior recurso, um de cada vez |
| **Eliminação de recursos recursivos (RFE)** | Treine repetidamente o modelo; remover recursos menos importantes |
### Métodos incorporados
| Método | Descrição |
|--------|------------|
| **Regularização L1 (Lasso)** | Reduz os pesos dos recursos irrelevantes a zero |
| **Importância baseada em árvore** | Use a importância do recurso de modelos de árvore |
| **Valores SHAP** | Meça a contribuição de cada recurso para as previsões |
---

## Engenharia de recursos específicos de domínio
### Recursos de texto
| Recurso | Descrição |
|--------|-------------|
| **TF-IDF** | Frequência dos prazos ponderada pela frequência inversa do documento |
| **Incorporações de palavras** | Vetores densos que capturam significado semântico (Word2Vec, GloVe) |
| **N-gramas de caracteres** | Capture padrões de subpalavras; útil para erros de digitação e morfologia |
| **Estatísticas de texto** | Comprimento; contagem de palavras; contagem de sentenças; comprimento médio da palavra |
| **Pontuações de legibilidade** | Flesch-Kincaid; Índice de nevoeiro de tiro |
### Recursos de série temporal
| Recurso | Descrição |
|--------|-------------|
| **Recursos de atraso** | Valores anteriores: y(t-1), y(t-7), y(t-30) |
| **Estatísticas contínuas** | Média, padrão, mínimo, máximo em uma janela |
| **Diferença** | y(t) - y(t-1); captura tendência |
| **Diferença sazonal** | y(t) - y(t-12) para dados mensais com sazonalidade anual |
| **Termos de Fourier** | Termos de seno e cosseno para padrões sazonais |
### Recursos de imagem (pré-aprendizagem profunda)
| Recurso | Descrição |
|--------|-------------|
| **HOG** (histograma de gradientes orientados) | Distribuição das direções das bordas |
| **LBP** (padrões binários locais) | Descrição da textura |
| **SIFT** (transformação de recurso invariante em escala) | Descritores de pontos-chave |
| **Histogramas de cores** | Distribuição das cores na imagem |
---

## Práticas recomendadas de engenharia de recursos
| Prática | Descrição |
|----------|------------|
| **Evite vazamento de dados** | Nunca use informações do futuro ou do conjunto de testes para criar recursos |
| **Documente tudo** | Registre quais transformações foram aplicadas e por quê |
| **Versione seus recursos** | Rastreie alterações de recursos juntamente com alterações de modelo |
| **Validar com e sem** | Teste se um novo recurso realmente melhora o desempenho do modelo |
| **Mantenha-o reproduzível** | Os pipelines de engenharia de recursos devem ser determinísticos e repetíveis |
| **Desvio de recursos do monitor** | As distribuições de recursos podem mudar com o tempo; monitorar e reciclar |
---

## Resumo
A engenharia de recursos é onde o conhecimento do domínio encontra o aprendizado de máquina. É o processo de transformar dados brutos – confusos, incompletos e altamente dimensionais – em representações limpas e informativas com as quais os modelos podem aprender. As transformações numéricas controlam a inclinação e a escala. As codificações categóricas convertem rótulos em números que os modelos podem usar. Os recursos de data capturam padrões temporais. As estratégias de valor ausente lidam com dados incompletos. A seleção de recursos remove ruído e redundância. Os melhores engenheiros de recursos pensam como detetives: eles perguntam quais sinais devem estar presentes nos dados, onde esses sinais podem estar ocultos e como extraí-los de uma forma que seja honesta (sem vazamento de dados), reproduzível e robusta para mudar ao longo do tempo.