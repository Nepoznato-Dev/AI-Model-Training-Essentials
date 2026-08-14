<!--
---
# Metadata
title: "Machine Learning Project Failures"
description: "Data leakage, expectation mismatches, deployment failures, model decay"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, project, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Falhas em projetos de aprendizado de máquina
Os projetos de aprendizado de máquina falham em um ritmo alarmante – estimativas da indústria sugerem que 60-85% dos projetos de ML nunca chegam à produção. As falhas geralmente não estão nos algoritmos; eles estão no processo, nos dados, nas expectativas e no contexto organizacional. Compreender por que os projetos de ML falham é essencial para qualquer pessoa que construa sistemas de ML, porque os modos de falha são previsíveis e em grande parte evitáveis.
---

## Por que os projetos de ML falham
### Categorias de falha
| Categoria | Parcela de Falhas | Descrição |
|----------|------------------|------------|
| **Problemas de dados** | ~30% | Os dados são insuficientes, tendenciosos, obsoletos ou inacessíveis |
| **Definição do problema** | ~20% | O problema do ML não corresponde à necessidade do negócio |
| **Incompatibilidade de expectativas** | ~15% | As partes interessadas esperam magia; a realidade é a melhoria incremental |
| **Falha na implantação** | ~15% | Modelo funciona em notebooks, mas não pode ser produzido |
| ** questões organizacionais** | ~10% | Nenhuma propriedade clara; a equipe carece de habilidades; sem apoio executivo |
| **Desempenho do modelo** | ~10% | O modelo não atinge a precisão exigida ou generaliza mal |
---

## Falhas relacionadas a dados
### Problemas comuns de dados
| Problema | Descrição | Exemplo |
|---------|-------------|---------|
| **Dados insuficientes** | Exemplos insuficientes para aprender padrões significativos | Treinamento de modelo de detecção de fraude em 500 transações |
| **Qualidade da etiqueta** | Os rótulos de treinamento estão errados, inconsistentes ou subjetivos | Imagens médicas rotuladas por não especialistas; rótulos de sentimento com baixa concordância entre avaliadores |
| **Vazamento de dados** | Informações do futuro ou destino vazam em recursos | Usando o resultado da rotatividade de clientes como um recurso; incluindo dados de teste no treinamento |
| **Viés de seleção** | Os dados de treinamento não representam a população de implantação | Treinar um modelo médico com base em dados de um hospital; implantação nacional |
| **Desvio de conceito** | A relação entre recursos e destino muda ao longo do tempo | O comportamento do consumidor muda após uma pandemia; modelo treinado em dados pré-pandemia |
| **Incompatibilidade de recursos** | Os recursos disponíveis durante o treinamento diferem daqueles disponíveis na produção | Treinamento com etiquetas manuais; produção utiliza rótulos automatizados com distribuição diferenciada |
| **Desequilíbrio de classes** | As classes-alvo são altamente distorcidas | 99% negativo, 1% positivo; modelo aprende a prever sempre o negativo |
### O problema de vazamento de dados
| Tipo | Descrição | Exemplo |
|------|-------------|---------|
| **Vazamento alvo** | Um recurso só fica disponível depois que o alvo ocorre | “Resultado do tratamento” usado como recurso para prever “sucesso do tratamento” |
| **Contaminação em teste de trem** | Dados de testes influenciam treinamento | Dimensionamento com estatísticas globais (inclui dados de teste); aumento de dados que vaza |
| **Viés de amostragem** | Treinamento e produção utilizam amostragem diferente | Treinamento sobre tráfego web; implantando no tráfego de aplicativos móveis |
| **Vazamento de pré-processamento** | A etapa de pré-processamento usa informações do conjunto de dados completo | Imputação de valores em falta à média global (inclui dados de teste) |
---

## Falhas na definição do problema
### Padrões de desalinhamento
| Padrão | Descrição | Consequência |
|---------|-------------|-------------|
| **Resolvendo o problema errado** | Necessidades de negócios X; equipe constrói Y | Modelo é tecnicamente bom, mas inútil |
| **ML quando as regras seriam suficientes** | O problema possui regras determinísticas; ML adiciona complexidade | Excesso de engenharia; mais difícil de manter; menos interpretável |
| **ML quando os dados não existem** | Problema requer dados que não foram coletados | O projeto não pode ser iniciado; meses desperdiçados em viabilidade |
| **Meta de precisão sem contexto de negócios** | “Precisamos de 95% de precisão” – mas o que isso significa para o negócio? | Modelo atende à precisão, mas não resolve o problema do negócio |
| **Ignorando o custo dos erros** | Falsos positivos e falsos negativos têm custos diferentes | Modelo otimiza métrica errada |
| **Sem linha de base** | Sem comparação com a abordagem existente | Não consigo dizer se o ML é realmente melhor do que uma simples heurística |
---

## Falhas nas expectativas
### O ciclo de hype em projetos de ML
| Fase | Descrição | Risco |
|-------|-------------|------|
| **Excitação** | "A IA resolverá tudo!" | Muito promissor; falta de recursos |
| **Prova de conceito** | Modelo funciona com dados limpos em notebooks | Falsa confiança; "funciona!" |
| **Verificação da realidade** | Os dados de produção são confusos; desempenho cai | Desapontamento; “ML não funciona” |
| **Marcha da Morte** | Equipe tenta forçar a produção | Dívida técnica; esgotamento |
| **Abandono ou implantação silenciosa** | Projeto cancelado ou implantado sem monitoramento | Investimento desperdiçado |
### Gerenciando Expectativas
| Estratégia | Descrição |
|----------|------------|
| **Comece com uma linha de base** | Compare com a abordagem mais simples possível (regras; desempenho humano) |
| **Definir métricas de sucesso antecipadamente** | Métricas de negócios (receita; economia de custos) e não apenas métricas de ML (precisão; F1) |
| **Exploração de caixa de tempo** | Dê à equipe de 2 a 4 semanas para avaliar a viabilidade antes de se comprometer |
| **Mostre o que o ML não pode fazer** | Seja honesto sobre as limitações; definir expectativas realistas |
| **Iterar incrementalmente** | Implante primeiro um modelo simples; melhorar iterativamente |
| **Quantificar o custo dos erros** | Traduzir o desempenho do modelo em impacto nos negócios |
---

## Falhas de implantação
### Por que os modelos não chegam à produção
| Problema | Descrição | Solução |
|--------|-------------|----------|
| **Caderno para lacuna de produção** | O código funciona no Jupyter, mas não está pronto para produção | Práticas de MLOps; CI/CD para ML; revisão de código |
| **Requisitos de latência** | A inferência do modelo é muito lenta para uso em tempo real | Otimização do modelo; quantização; cache |
| **Escalabilidade** | O modelo não consegue lidar com o tráfego de produção | Processamento em lote; escala horizontal; modelo servindo infraestrutura |
| **Lacunas de monitoramento** | Não há como detectar quando o modelo se degrada | Monitoramento de desvio de dados; monitoramento de desempenho; alertando |
| **Gerenciamento de dependências** | Os ambientes de treinamento e serviço diferem | Contentorização; ambientes reproduzíveis |
| **Sem plano de reversão** | Não é possível reverter para o modelo anterior quando o novo modelo falha | Cadastro de modelo; versionamento; reversão automatizada |
### Decadência do modelo
| Tipo | Descrição | Detecção |
|------|-------------|-----------|
| **Desvio de dados** | Mudança nas distribuições de recursos de entrada | Monitore estatísticas de recursos; Divergência KL; PSI |
| **Desvio de conceito** | Relação entre recursos e mudanças de destino | Monitore a precisão das previsões ao longo do tempo |
| **Desvio de rótulo** | Definição ou distribuição das alterações alvo | Rastrear distribuições de rótulos; correlação de métricas de negócios |
| **Alterações iniciais** | Fonte de dados altera formato, tempo ou qualidade | Validação de esquema; monitoramento de frescor |
---

## Falhas Organizacionais
| Falha | Descrição | Prevenção |
|---------|-------------|------------|
| **Sem propriedade clara** | Ninguém é responsável pelo modelo em produção | Atribuir proprietários de modelos; definir RACI |
| **Equipes isoladas** | Os cientistas de dados constroem modelos; engenheiros implantam; ninguém se comunica | Equipes multifuncionais; objetivos compartilhados |
| **Sem maturidade de MLOps** | Nenhum registro de modelo; sem CI/CD; sem monitoramento | Investir em infraestrutura MLOps de forma incremental |
| **Cronogramas irrealistas** | "Construa um sistema de ML de produção em 2 semanas" | Exploração de caixa de tempo; iterar; comunicar complexidade |
| **Falta de experiência no domínio** | A equipe de ML não entende o problema do negócio | Incorporar especialistas de domínio em equipes de ML |
| **Sem quadro de avaliação** | Não sei dizer se o modelo está funcionando em produção | Definir métricas de negócios; configurar painéis; revisões regulares |
---

## Lições aprendidas
### A lista de verificação do projeto de ML
| Fase | Pergunta-chave |
|-------|------------|
| **Definição do problema** | Isso é realmente um problema de ML? Qual é a linha de base? Como é o sucesso? |
| **Avaliação de dados** | Temos dados suficientes? É representativo? Os rótulos são confiáveis? |
| **Viabilidade** | Podemos construir um protótipo funcional em 2 a 4 semanas? Quais são os riscos? |
| **Desenvolvimento** | Há vazamento de dados? Estamos usando a métrica de avaliação correta? |
| **Pré-produção** | Funciona com dados de produção? É rápido o suficiente? É monitorado? |
| **Implantação** | Podemos reverter? Quem está de plantão? O que acontece quando ele se degrada? |
| **Pós-implantação** | Estamos monitorando a deriva? As métricas de negócios são monitoradas? Existe um plano de reciclagem? |
---

## Resumo
Os projetos de ML falham não porque os algoritmos sejam muito difíceis, mas porque o processo em torno deles está quebrado. Problemas de dados – dados insuficientes, rótulos inadequados, vazamentos, desvios – são responsáveis ​​pela maior parte das falhas. Falhas na definição de problemas – resolver o problema errado, usar ML quando as regras seriam suficientes, ignorar o custo dos erros – desperdiçam meses de esforço. Falhas nas expectativas – promessas excessivas, entregas insuficientes e não gerenciamento das partes interessadas – destroem a confiança organizacional no ML. Falhas na implantação (lacunas entre o notebook e a produção, problemas de latência, falta de monitoramento) significam que os modelos que funcionam no desenvolvimento nunca criam valor na produção. Falhas organizacionais – sem propriedade, equipes isoladas, sem MLOps – tornam estruturalmente impossível o sucesso. O antídoto é a prática disciplinada: comece com uma linha de base; exploração de caixa de tempo; validar os dados rigorosamente; verifique se há vazamento; definir métricas de negócios; implantar de forma incremental; monitorar continuamente; e iterar. As melhores equipes de ML gastam mais tempo em dados e processos do que em modelos.