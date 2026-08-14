---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [ml, engineering, mlops, ai-and-machine-learning]
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

# Engenharia de ML e MLOps
Construir um modelo de aprendizado de máquina é apenas metade da batalha. Colocá-lo em produção, mantê-lo funcionando de maneira confiável, monitorar desvios e iterá-lo - é aí que entram a engenharia de ML e MLOps. Este arquivo cobre todo o ciclo de vida, do experimento ao sistema de produção.
---

## O ciclo de vida do ML
| Fase | Descrição | Principais atividades |
|-------|------------|---------------|
| **1. Definição do Problema** | Enquadre o problema de negócios como uma tarefa de ML | Definir métricas, restrições, critérios de sucesso |
| **2. Coleta de dados** | Coletar e rotular dados de treinamento | ETL, rotulagem, aumento |
| **3. Experimentação** | Treinar e avaliar modelos | Engenharia de recursos, ajuste de hiperparâmetros |
| **4. Seleção de modelo** | Escolha o melhor modelo | Compare métricas, avalie compensações |
| **5. Implantação** | Envie o modelo para produção | Servindo infraestrutura, API, lote |
| **6. Monitoramento** | Fique atento à deriva e à degradação | Desvio de dados, desvio de conceito, desempenho |
| **7. Reciclagem** | Atualizar o modelo com novos dados | Requalificação programada ou desencadeada |
A maior parte do valor (e dificuldade) está nas fases 5–7. Um modelo sentado em um notebook Jupyter não cria valor comercial.
---

## Padrões de exibição de modelo
| Padrão | Descrição | Latência | Caso de uso |
|---------|-------------|---------|----------|
| **Inferência de lote** | Executar modelo em um lote de dados de acordo com uma programação | Horas | Recomendações diárias, pontuação de fraude |
| **Inferência on-line** | Previsão em tempo real por solicitação | Milissegundos | Classificação de pesquisa, classificação em tempo real |
| **Inferência de streaming** | Processar previsões em um fluxo de dados | Segundos | Detecção de anomalias, processamento de eventos |
### Servindo Infraestrutura
| Ferramenta | Tipo | Melhor para |
|------|------|----------|
| **Exibição do TensorFlow** | Servidor modelo | Modelos TensorFlow |
| **TorchServe** | Servidor modelo | Modelos PyTorch |
| **Servidor de Inferência Triton** | Multiestrutura | Inferência de GPU, múltiplas estruturas |
| **vLLM** | Serviço LLM | Inferência LLM de alto rendimento |
| **BentoML** | Serviço unificado | Implantação independente de estrutura |
| **Seldon** | Nativo de K8s | Implantação do modelo Kubernetes |
| **Ray Serve** | Serviço escalável | Grandes modelos, inferência distribuída |
---

## Registros de Modelos
Um registro de modelo é um armazenamento centralizado para gerenciar modelos de ML — suas versões, metadados, métricas e status de implantação.
| Capacidade | Descrição |
|-----------|------------|
| **Versionamento** | Rastreie cada versão do modelo com ID exclusivo |
| **Metadados** | Dados de treinamento, hiperparâmetros, métricas, autor |
| **Transições de palco** | Mova os modelos pelos estágios: Preparação → Produção → Arquivado |
| **Linhagem** | Rastrear quais dados e códigos produziram cada modelo |
| Ferramenta | Descrição |
|------|-------------|
| **MLfluxo** | Código aberto; registro de modelo + rastreamento de experimento |
| **Pesos e preconceitos (W&B)** | Comercial; rastreamento de experimentos + registro de modelo |
| **DVC** | Versionamento de dados e modelos com Git |
| **Azure ML/SageMaker** | Gerenciamento de modelos nativos da nuvem |
---

## Acompanhamento de experimentos
Cada experimento de ML deve ser rastreado: quais dados foram usados, quais hiperparâmetros, quais métricas resultaram.
| Ferramenta | Principais recursos |
|------|-------------|
| **MLfluxo** | Código aberto, auto-hospedado, rastreia parâmetros/métricas/artefatos |
| **W&B** | UI rica, varreduras, controle de versão de artefatos, relatórios |
| **Netuno** | Armazenamento de metadados para MLOps |
| **TensorBoard** | Integrado ao TensorFlow; visualizar curvas de treinamento |
### O que rastrear
| Categoria | Exemplos |
|----------|---------|
| **Parâmetros** | Taxa de aprendizagem, tamanho do lote, arquitetura do modelo, número de épocas |
| **Métricas** | Precisão, perda, F1, AUC-ROC (por época e final) |
| **Artefatos** | Pesos de modelos, matrizes de confusão, amostras de predição |
| **Dados** | Versão do conjunto de dados, proporções de divisão, etapas de pré-processamento |
| **Meio Ambiente** | Versão Python, versões de biblioteca, hardware |
---

## Estratégias de implantação de modelo
| Estratégia | Como funciona | Risco |
|----------|-------------|------|
| **Implantação de sombra** | O novo modelo funciona ao lado do antigo; previsões comparadas, mas não veiculadas | Risco zero; valida antes de entrar no ar |
| **Lançamento Canário** | Encaminhar pequena % do tráfego para o novo modelo; aumentar gradualmente | Baixo risco; reversão rápida |
| **Teste A/B** | Divida os usuários entre antigos e novos; compare métricas de negócios | Mede o impacto real |
| **Azul-Verde** | Dois ambientes idênticos; mudar todo o tráfego de uma vez | Reversão instantânea; custo duplo durante a transição |
| **Sinalizadores de recursos** | Ativar/desativar modelo por segmento de usuário | Controle refinado |
---

## Monitoramento de sistemas de ML
Os sistemas de ML precisam de mais monitoramento do que o software tradicional porque os próprios dados podem mudar.
### Tipos de deriva
| Tipo de deriva | O que muda | Exemplo |
|-----------|-------------|---------|
| **Desvio de dados** | Mudanças na distribuição de insumos | Mudança na demografia do cliente após uma campanha de marketing |
| **Desvio de conceito** | Relação entre alterações nas entradas e nas saídas | O comportamento do consumidor muda durante uma recessão |
| **Desvio de etiqueta** | Alterações na distribuição alvo | Taxa de fraude aumenta de 1% para 5% |
### O que monitorar
| Categoria | Métricas |
|----------|---------|
| **Desempenho do modelo** | Exatidão, precisão, recuperação, F1, AUC (em comparação com a linha de base) |
| **Qualidade dos dados** | Valores ausentes, distribuições de recursos, valores discrepantes |
| **Detecção de deriva** | Testes estatísticos (teste KS, PSI, divergência KL) |
| **Infraestrutura** | Latência, rendimento, utilização de GPU, memória |
| **Métricas de negócios** | Taxa de conversão, impacto na receita, satisfação do usuário |
### Ferramentas de monitoramento
| Ferramenta | Tipo |
|------|------|
| **Evidentemente IA** | Desvio de dados de código aberto e monitoramento de desempenho de modelo |
| **Grafana** | Visualização do painel (funciona com Prometheus) |
| **PorquêLabs** | Plataforma de observabilidade de dados |
| **Arize** | Observabilidade de ML e análise de causa raiz |
| **Prometeu + Grafana** | Métricas de infraestrutura e aplicação |
---

## Treinamento reproduzível
Reprodutibilidade significa que você pode executar novamente um experimento e obter o mesmo resultado. É essencial para depuração, auditoria e conformidade.
### Requisitos
| Requisito | Como conseguir isso |
|------------|--------|
| **Controle de versão de dados** | DVC, Delta Lake ou instantâneos de conjunto de dados com hashes |
| **Controle de versão de código** | Git para todos os códigos de treinamento |
| **Fixação de ambiente** | `requirements.txt`,`conda env`, imagens Docker com versões exatas |
| **Configuração de sementes** | Corrigir sementes aleatórias para numpy, torch, tensorflow |
| **Gerenciamento de configuração** | Configurações Hydra, OmegaConf ou YAML para todos os hiperparâmetros |
| **Rastreamento de artefatos** | MLflow ou W&B para registrar todos os experimentos |
---

## Inferência de escala
Quando um modelo precisa atender milhões de solicitações por dia, o desempenho é importante.
| Técnica | Descrição |
|-----------|------------|
| **Lotes** | Agrupe várias solicitações em um único encaminhamento |
| **Quantização** | Reduza a precisão do modelo (FP32 → INT8 ou INT4) para inferência mais rápida |
| **Modelo de Destilação** | Treine um modelo menor para imitar um modelo maior |
| **Poda** | Remova pesos ou neurônios sem importância |
| **Cache** | Armazenar em cache previsões frequentes para evitar recomputação |
| **Otimização de GPU** | TensorRT, tempo de execução ONNX, atenção flash |
| **Escalonamento horizontal** | Execute várias réplicas de modelo atrás de um balanceador de carga |
---

## Sinalizadores de recursos para ML
Os sinalizadores de recursos permitem controlar qual versão do modelo atende quais usuários, sem reimplantar.
| Caso de uso | Descrição |
|----------|------------|
| **Lançamento gradual** | Servir novo modelo para 5% dos usuários e depois aumentar |
| **Interruptor de desligamento** | Reverter instantaneamente para o modelo anterior se forem detectados problemas |
| **Baseado em segmento** | Diferentes modelos para diferentes segmentos de usuários |
| **Experimentação** | Variantes do modelo de teste A/B com métricas de negócios |
Ferramentas: LaunchDarkly, Unleash, Flagsmith ou sinalizadores de recursos simples baseados em banco de dados.
---

## A curva de maturidade MLOps
| Nível | Características |
|-------|----------------|
| **Nível 0 — Manual** | Treinamento manual, implantação manual, sem monitoramento |
| **Nível 1 — Experimentação** | Acompanhamento de experimentos, registro de modelo, CI básico |
| **Nível 2 — Automação** | Retreinamento automatizado, CI/CD para modelos, testes automatizados |
| **Nível 3 — Pipeline completo** | Pipeline automatizado ponta a ponta com monitoramento, detecção de desvios e retreinamento automático |
A maioria das organizações está em algum lugar entre o Nível 0 e o Nível 1. O objetivo é o Nível 2–3, onde o ciclo de vida do ML é automatizado e auto-recuperável.