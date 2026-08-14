---
# Metadata
title: "Machine Learning Evaluation and Workflow"
description: "ML pipelines, metrics, best practices"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [ml, evaluation, workflow, ai-and-machine-learning]
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

# Avaliação e fluxo de trabalho de aprendizado de máquina
Um guia prático para o ciclo de vida do ML — desde o enquadramento do problema até o monitoramento da produção — com foco em métricas, validação e depuração.
---

## O fluxo de trabalho de ML (CRISP-ML)
1. **Compreensão do Negócio**: Defina o objetivo e os critérios de sucesso.
2. **Compreensão dos dados**: explore os dados disponíveis e identifique problemas de qualidade.
3. **Preparação de dados**: limpe, transforme e divida dados.
4. **Modelagem**: treine modelos e ajuste hiperparâmetros.
5. **Avaliação**: avalie o desempenho em relação às métricas.
6. **Implantação**: forneça o modelo em produção.
7. **Monitoramento**: rastreie desvios, desempenho e anomalias.
Este é um ciclo iterativo – você revisitará as etapas anteriores com base nos resultados da avaliação.
---

## Divisão de dados
### Treinamento / Validação / Divisão de Teste
- **Conjunto de treinamento** (~70%): usado para ajustar os parâmetros do modelo.
- **Conjunto de validação** (~15%): usado para ajustar hiperparâmetros e selecionar variantes de modelo.
- **Conjunto de testes** (~15%): usado apenas uma vez no final para estimar o desempenho da generalização.
**Importante:** O conjunto de teste deve ser mantido completamente intacto até a avaliação final para evitar vazamento de dados.
### Validação cruzada (k-fold)
Para conjuntos de dados pequenos, use validação cruzada k-fold: divida os dados em k dobras, treine em k-1, valide no restante e repita k vezes. Média do desempenho. k=5 ou k=10 é comum.
### Divisão estratificada
Para classificação com classes desequilibradas, use divisões estratificadas para preservar as proporções das classes em cada subconjunto.
### Divisão baseada em tempo
Para dados de série temporal, divida cronologicamente (treine no passado, teste no futuro) em vez de aleatoriamente.
---

## Métricas de avaliação
### Métricas de Classificação
| Métrica | O que mede | Melhor usado para |
|--------|------------------|---------------|
| **Precisão** | (TP + TN) / (TP + TN + FP + FN) | Conjuntos de dados balanceados |
| **Precisão** | TP/(TP + FP) | Quando falsos positivos são caros (por exemplo, detecção de spam) |
| **Lembrar** | TP/(TP+FN) | Quando os falsos negativos são dispendiosos (por exemplo, rastreio do cancro) |
| **Pontuação F1** | Média harmônica de precisão e recall | Conjuntos de dados desequilibrados, métrica de número único |
| **AUC-ROC** | Área sob a curva ROC; compensação entre TPR e FPR | Desempenho geral do classificador independente do limiar |
| **AUC-PR** | Área sob a curva Precision-Recall | Conjuntos de dados altamente desequilibrados |
**Definições:**
- TP = Verdadeiro Positivo
- TN = Verdadeiro Negativo
- FP = Falso Positivo (erro Tipo I)
- FN = Falso Negativo (erro Tipo II)
### Métricas de regressão
| Métrica | O que mede | Sensibilidade a valores discrepantes |
|--------|------------------|--------------------------|
| **MSE** (erro quadrático médio) | Diferença quadrática média | Alto |
| **RMSE** (raiz do erro quadrático médio) | Raiz quadrada do MSE (mesmas unidades do alvo) | Alto |
| **MAE** (erro médio absoluto) | Diferença média absoluta | Baixo |
| **R²** (Coeficiente de Determinação) | Proporção de variância explicada | Nenhum diretamente, mas sensível a valores discrepantes indiretamente |
### Métricas de classificação e recuperação
- **Precision@k**: fração de itens relevantes entre as k principais recomendações.
- **Recall@k**: fração de todos os itens relevantes que aparecem no top-k.
- **NDCG** (ganho cumulativo com desconto normalizado): contabiliza a relevância da posição.
- **Taxa de acerto**: se um item relevante aparece no top-k.
### Métricas Gerativas / LLM
- **Perplexidade**: quão "surpreso" o modelo fica com um texto retido (quanto menor, melhor).
- **BLEU**: sobreposição de n-gramas com traduções de referência (focado na precisão).
- **ROUGE**: Sobreposição orientada para recordação para resumo.
- **BERTScore**: Similaridade semântica usando embeddings contextuais (mais robusto que BLEU).
- **METEOR**: Alinha-se aos sinônimos e radicais do WordNet.
---

## Armadilhas de avaliação
### Vazamento de dados
Ocorre quando as informações do conjunto de testes influenciam inadvertidamente o treinamento.
- **Prevenir:** Nunca use dados de teste para engenharia de recursos, normalização ou ajuste de hiperparâmetros.
- **Detectar:** Se a pontuação do seu modelo for suspeitamente alta, suspeite de vazamento.
### Sobreajuste
O modelo tem um bom desempenho em dados de treinamento, mas fraco em validação/teste.
- **Mitigar:** Use regularização, interrupção antecipada, simplifique a arquitetura ou colete mais dados.
### Subajuste
O modelo tem um desempenho ruim tanto no treinamento quanto na validação.
- **Mitigar:** Use um modelo mais complexo, adicione recursos ou reduza a regularização.
### Dados desequilibrados
- **Mitigar:** Use pesos de classe, sobreamostragem (SMOTE), subamostragem ou use métricas apropriadas (F1, AUC-PR) em vez de precisão.
### Deriva Temporal (Deriva de Conceito)
A relação entre recursos e destino muda com o tempo.
- **Mitigar:** Treine novamente periodicamente, monitore o desempenho e use algoritmos de detecção de desvios.
---

## Ajuste de hiperparâmetros
- **Pesquisa em grade**: teste exaustivamente todas as combinações de um conjunto predefinido de hiperparâmetros. Simples, mas computacionalmente caro.
- **Pesquisa aleatória**: Amostra de combinações aleatórias de distribuições. Mais eficiente do que a pesquisa em grade para espaços de alta dimensão.
- **Otimização Bayesiana**: Constrói um modelo probabilístico da função objetivo e seleciona hiperparâmetros de forma inteligente. Bibliotecas: Optuna, Hyperopt, scikit-optimise.
- **Ajuste automatizado**: Use ferramentas como Optuna, Ray Tune ou Weights & Biases Sweeps para ajuste distribuído.
**Intervalos de pesquisa sugeridos para hiperparâmetros comuns:**
| Parâmetro | Intervalo sugerido (escala logarítmica) |
|-----------|----------------------------|
| Taxa de aprendizagem | 1e-5 a 1e-1 |
| Tamanho do lote | 16, 32, 64, 128, 256 |
| Número de camadas (NN) | 2 a 6 |
| Número de neurônios (NN) | 32 a 1024 |
| Regularização (L2) | 1e-6 a 1e-2 |
| Profundidade da árvore (XGBoost) | 3 a 12 |
---

## Seleção e validação de modelo
1. **Modelo de linha de base**: comece com uma heurística simples ou um modelo simples (por exemplo, regressão logística, preditor de média) para estabelecer um limite inferior.
2. **Modelos candidatos**: Treine múltiplas famílias de modelos (por exemplo, Random Forest, XGBoost, Neural Network).
3. **Validação cruzada** de cada candidato no conjunto de validação.
4. **Compare métricas** (com intervalos de confiança) e selecione o melhor candidato.
5. **Avaliação final** no conjunto de testes resistidos.
6. **Análise de erros**: veja exemplos em que o modelo errou. Identifique padrões (por exemplo, classes raras, entradas ambíguas) e alimente insights na preparação de dados ou na engenharia de recursos.
---

## Implantação e monitoramento
### Padrões de veiculação
- **Inferência em lote**: processe grandes volumes de dados off-line (por exemplo, recomendações noturnas).
- **Inferência on-line**: previsões em tempo real via API (por exemplo, pontuação de crédito, detecção de fraudes).
- **Inferência de streaming**: orientada por eventos, em tempo real e com baixa latência (por exemplo, alertas de sensores IoT).
### Monitoramento de modelo
- **Monitoramento de desempenho**: Rastreie a precisão/F1 ao longo do tempo em dados ao vivo (quando a verdade do terreno estiver disponível).
- **Desvio de dados**: Monitore mudanças nas distribuições de recursos de entrada (por exemplo, usando PSI – Índice de Estabilidade Populacional).
- **Desvio de conceito**: Monitore mudanças na relação entre entradas e saídas.
- **Desvio de previsão**: acompanhe a distribuição dos resultados previstos.
- **Latência e taxa de transferência**: Garanta que os SLAs (Acordos de Nível de Serviço) sejam cumpridos.
### Registro e alerta
- Registrar todas as solicitações e respostas de previsão (com anonimato).
- Definir alertas para:
  - Queda significativa no desempenho.
  - Alta porcentagem de entradas ausentes ou inválidas.
  - Resultados do modelo fora dos limites esperados.
### Controle de versão e registro do modelo
- Use um registro de modelo (por exemplo, MLflow, Weights & Biases, Sagemaker Model Registry) para armazenar e versão de modelos, metadados e resultados de avaliação.
- Armazene o código de treinamento e a versão dos dados (via DVC ou Git LFS) junto com o modelo.
---

## Lista de verificação prática do fluxo de trabalho
- [ ] Problema enquadrado e métrica de sucesso definida.
- [ ] Exploração de dados realizada (missing values, outliers, distribuição).
- [ ] Divisão de treinamento/validação/teste criada (estratificada se necessário).
- [ ] Modelo de base estabelecido.
- [ ] Modelos candidatos treinados e validados.
- [] Hiperparâmetros ajustados.
- [ ] Melhor modelo selecionado via validação cruzada.
- [ ] Avaliação final no conjunto de testes.
- [ ] Análise de erros realizada.
- [ ] Plano de implantação pronto (infraestrutura de atendimento).
- [ ] Configuração do painel de monitoramento.
- [ ] Documentação (cartão de dados, cartão modelo) preenchida.