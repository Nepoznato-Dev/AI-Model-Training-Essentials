# Avaliação e Workflow de Machine Learning

Um guia prático do ciclo de vida de ML — da definição do problema ao monitoramento em produção — com foco em métricas, validação e depuração.

---

## O Workflow de ML (CRISP-ML)

1. **Entendimento do Negócio**: Defina o objetivo e os critérios de sucesso.
2. **Entendimento dos Dados**: Explore os dados disponíveis e identifique problemas de qualidade.
3. **Preparação dos Dados**: Limpe, transforme e divida os dados.
4. **Modelagem**: Treine modelos e ajuste hiperparâmetros.
5. **Avaliação**: Meça o desempenho com base nas métricas.
6. **Implantação**: Coloque o modelo em produção.
7. **Monitoramento**: Acompanhe drift, desempenho e anomalias.

Este é um ciclo iterativo — você revisitará etapas anteriores com base nos resultados da avaliação.

---

## Divisão de Dados

### Divisão entre Treino / Validação / Teste
- **Conjunto de treino** (~70%): Usado para ajustar os parâmetros do modelo.
- **Conjunto de validação** (~15%): Usado para ajustar hiperparâmetros e selecionar variantes do modelo.
- **Conjunto de teste** (~15%): Usado apenas uma vez, no final, para estimar a capacidade de generalização.

**Importante:** O conjunto de teste deve permanecer completamente intocado até a avaliação final para evitar data leakage.

### Cross-Validation (k-fold)
Para conjuntos de dados pequenos, use validação cruzada k-fold: divida os dados em k partes, treine em k-1, valide na parte restante e repita k vezes. Tire a média do desempenho. k=5 ou k=10 é comum.

### Divisão Estratificada
Para classificação com classes desbalanceadas, use divisões estratificadas para preservar as proporções das classes em cada subconjunto.

### Divisão Baseada em Tempo
Para dados de séries temporais, faça a divisão em ordem cronológica (treino no passado, teste no futuro), em vez de aleatoriamente.

---

## Métricas de Avaliação

### Métricas de Classificação

| Métrica | O que mede | Melhor uso |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Conjuntos de dados balanceados |
| **Precision** | TP / (TP + FP) | Quando falsos positivos têm alto custo (ex.: detecção de spam) |
| **Recall** | TP / (TP + FN) | Quando falsos negativos têm alto custo (ex.: rastreamento de câncer) |
| **F1-score** | Média harmônica entre precision e recall | Conjuntos de dados desbalanceados, métrica de valor único |
| **AUC-ROC** | Área sob a curva ROC; equilíbrio entre TPR e FPR | Desempenho geral do classificador independentemente do threshold |
| **AUC-PR** | Área sob a curva Precision-Recall | Conjuntos de dados altamente desbalanceados |

**Definições:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (erro do Tipo I)
- FN = False Negative (erro do Tipo II)

### Métricas de Regressão

| Métrica | O que mede | Sensibilidade a outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Diferença quadrática média | Alta |
| **RMSE** (Root Mean Squared Error) | Raiz quadrada do MSE (mesmas unidades do alvo) | Alta |
| **MAE** (Mean Absolute Error) | Diferença absoluta média | Baixa |
| **R²** (Coefficient of Determination) | Proporção da variância explicada | Nenhuma diretamente, mas sensível a outliers de forma indireta |

### Métricas de Ranking e Recuperação
- **Precision@k**: Fração de itens relevantes entre as top-k recomendações.
- **Recall@k**: Fração de todos os itens relevantes que aparecem no top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Considera a relevância em função da posição.
- **Hit Rate**: Indica se um item relevante aparece no top-k.

### Métricas Generativas / para LLMs
- **Perplexity**: O quanto o modelo fica "surpreso" com um texto separado para avaliação (quanto menor, melhor).
- **BLEU**: Sobreposição de n-gramas com traduções de referência (foco em precision).
- **ROUGE**: Sobreposição orientada a recall para sumarização.
- **BERTScore**: Similaridade semântica usando embeddings contextuais (mais robusto que BLEU).
- **METEOR**: Alinha sinônimos e radicais com base no WordNet.

---

## Armadilhas na Avaliação

### Data Leakage
Ocorre quando informações do conjunto de teste influenciam inadvertidamente o treinamento.
- **Prevenir:** Nunca use dados de teste para feature engineering, normalização ou ajuste de hiperparâmetros.
- **Detectar:** Se o modelo apresentar pontuação suspeitosamente alta, suspeite de leakage.

### Overfitting
O modelo vai bem nos dados de treino, mas mal em validação/teste.
- **Mitigar:** Use regularização, early stopping, simplifique a arquitetura ou colete mais dados.

### Underfitting
O modelo tem desempenho ruim tanto em treino quanto em validação.
- **Mitigar:** Use um modelo mais complexo, adicione features ou reduza a regularização.

### Dados Desbalanceados
- **Mitigar:** Use pesos de classe, oversampling (SMOTE), undersampling ou métricas apropriadas (F1, AUC-PR) em vez de accuracy.

### Temporal Drift (Concept Drift)
A relação entre features e alvo muda ao longo do tempo.
- **Mitigar:** Retreine periodicamente, monitore o desempenho e use algoritmos de detecção de drift.

---

## Ajuste de Hiperparâmetros

- **Grid Search**: Testa exaustivamente todas as combinações de um conjunto predefinido de hiperparâmetros. Simples, porém computacionalmente caro.
- **Random Search**: Amostra combinações aleatórias a partir de distribuições. Mais eficiente que grid search em espaços de alta dimensionalidade.
- **Bayesian Optimisation**: Constrói um modelo probabilístico da função objetivo e seleciona hiperparâmetros de forma inteligente. Bibliotecas: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use ferramentas como Optuna, Ray Tune ou Weights & Biases Sweeps para ajuste distribuído.

**Faixas sugeridas para hiperparâmetros comuns:**

| Parameter | Suggested range (log-scale) |
|-----------|-----------------------------|
| Learning rate | 1e-5 to 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Number of layers (NN) | 2 to 6 |
| Number of neurons (NN) | 32 to 1024 |
| Regularisation (L2) | 1e-6 to 1e-2 |
| Tree depth (XGBoost) | 3 to 12 |

---

## Seleção e Validação de Modelos

1. **Modelo de baseline**: Comece com uma heurística simples ou um modelo simples (ex.: regressão logística, preditor da média) para estabelecer um limite inferior.
2. **Modelos candidatos**: Treine múltiplas famílias de modelos (ex.: Random Forest, XGBoost, Neural Network).
3. **Faça cross-validation** de cada candidato no conjunto de validação.
4. **Compare as métricas** (com intervalos de confiança) e selecione o melhor candidato.
5. **Avaliação final** no conjunto de teste separado.
6. **Análise de erros**: Observe exemplos em que o modelo erra. Identifique padrões (ex.: classes raras, entradas ambíguas) e retroalimente esses insights para a preparação de dados ou o feature engineering.

---

## Implantação e Monitoramento

### Padrões de Serving
- **Batch inference**: Processa grandes volumes de dados offline (ex.: recomendações noturnas).
- **Online inference**: Predições em tempo real via API (ex.: credit scoring, detecção de fraude).
- **Streaming inference**: Orientada a eventos, em tempo real e com baixa latência (ex.: alertas de sensores IoT).

### Monitoramento de Modelos
- **Monitoramento de desempenho**: Acompanhe accuracy/F1 ao longo do tempo em dados reais (quando houver ground truth disponível).
- **Data drift**: Monitore mudanças nas distribuições das features de entrada (ex.: usando PSI – Population Stability Index).
- **Concept drift**: Monitore mudanças na relação entre entradas e saídas.
- **Prediction drift**: Acompanhe a distribuição das saídas previstas.
- **Latência e throughput**: Garanta o cumprimento dos SLAs (Service Level Agreements).

### Logging e Alertas
- Registre todas as requisições e respostas de predição (com anonimização).
- Configure alertas para:
  - Queda significativa de desempenho.
  - Alta porcentagem de entradas ausentes ou inválidas.
  - Saídas do modelo fora dos limites esperados.

### Versionamento e Registry de Modelos
- Use um model registry (ex.: MLflow, Weights & Biases, Sagemaker Model Registry) para armazenar e versionar modelos, metadados e resultados de avaliação.
- Armazene o código de treinamento e a versão dos dados (via DVC ou Git LFS) junto com o modelo.

---

## Checklist Prático de Workflow

- [ ] Problema definido e métrica de sucesso estabelecida.
- [ ] Exploração de dados realizada (valores ausentes, outliers, distribuição).
- [ ] Divisão treino/validação/teste criada (estratificada, se necessário).
- [ ] Modelo de baseline estabelecido.
- [ ] Modelos candidatos treinados e validados.
- [ ] Hiperparâmetros ajustados.
- [ ] Melhor modelo selecionado via cross-validation.
- [ ] Avaliação final no conjunto de teste.
- [ ] Análise de erros realizada.
- [ ] Plano de implantação pronto (infraestrutura de serving).
- [ ] Dashboard de monitoramento configurado.
- [ ] Documentação (data card, model card) concluída.
