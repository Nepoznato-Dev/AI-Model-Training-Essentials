# Avaliação e fluxo de trabalho de aprendizado de máquina

Um guia prático para o ciclo de vida de ML — da definição do problema ao monitoramento em produção — com foco em métricas, validação e depuração.

---

## O fluxo de trabalho de ML (CRISP-ML)

1. **Entendimento do negócio**: Defina o objetivo e os critérios de sucesso.
2. **Entendimento dos dados**: Explore os dados disponíveis e identifique problemas de qualidade.
3. **Preparação dos dados**: Limpe, transforme e divida os dados.
4. **Modelagem**: Treine modelos e ajuste hiperparâmetros.
5. **Avaliação**: Meça o desempenho com base nas métricas.
6. **Implantação**: Coloque o modelo em produção.
7. **Monitoramento**: Acompanhe drift, desempenho e anomalias.

Este é um ciclo iterativo — você revisitará etapas anteriores com base nos resultados da avaliação.

---

## Divisão dos dados

### Divisão entre treino / validação / teste
- **Conjunto de treino** (~70%): Usado para ajustar os parâmetros do modelo.
- **Conjunto de validação** (~15%): Usado para ajustar hiperparâmetros e selecionar variantes do modelo.
- **Conjunto de teste** (~15%): Usado apenas uma vez, no final, para estimar o desempenho de generalização.

**Importante:** O conjunto de teste deve permanecer completamente intocado até a avaliação final para evitar vazamento de dados.

### Validação cruzada (k-fold)
Para conjuntos de dados pequenos, use validação cruzada k-fold: divida os dados em k partes, treine em k-1, valide na parte restante e repita k vezes. Tire a média do desempenho. k=5 ou k=10 é comum.

### Divisão estratificada
Para classificação com classes desbalanceadas, use divisões estratificadas para preservar as proporções de classes em cada subconjunto.

### Divisão baseada em tempo
Para dados de séries temporais, divida cronologicamente (treino no passado, teste no futuro) em vez de aleatoriamente.

---

## Métricas de avaliação

### Métricas de classificação

| Métrica | O que mede | Melhor uso |
|--------|------------------|---------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Conjuntos de dados balanceados |
| **Precision** | TP / (TP + FP) | Quando falsos positivos são custosos (ex.: detecção de spam) |
| **Recall** | TP / (TP + FN) | Quando falsos negativos são custosos (ex.: triagem de câncer) |
| **F1-score** | Média harmônica entre precision e recall | Conjuntos de dados desbalanceados, métrica resumida em um único número |
| **AUC-ROC** | Área sob a curva ROC; equilíbrio entre TPR e FPR | Desempenho geral do classificador, independente do limiar |
| **AUC-PR** | Área sob a curva Precision-Recall | Conjuntos de dados fortemente desbalanceados |

**Definições:**
- TP = True Positive
- TN = True Negative
- FP = False Positive (erro do Tipo I)
- FN = False Negative (erro do Tipo II)

### Métricas de regressão

| Métrica | O que mede | Sensibilidade a outliers |
|--------|------------------|--------------------------|
| **MSE** (Mean Squared Error) | Diferença quadrática média | Alta |
| **RMSE** (Root Mean Squared Error) | Raiz quadrada do MSE (mesmas unidades do alvo) | Alta |
| **MAE** (Mean Absolute Error) | Diferença absoluta média | Baixa |
| **R²** (Coefficient of Determination) | Proporção da variância explicada | Nenhuma diretamente, mas sensível a outliers indiretamente |

### Métricas de ranking e recuperação
- **Precision@k**: Fração de itens relevantes entre as top-k recomendações.
- **Recall@k**: Fração de todos os itens relevantes que aparecem no top-k.
- **NDCG** (Normalised Discounted Cumulative Gain): Leva em conta a relevância da posição.
- **Hit Rate**: Indica se um item relevante aparece no top-k.

### Métricas generativas / para LLMs
- **Perplexity**: O quanto o modelo fica "surpreso" com um texto fora do conjunto de treino (quanto menor, melhor).
- **BLEU**: Sobreposição de n-gramas com traduções de referência (foco em precisão).
- **ROUGE**: Sobreposição orientada a recall para sumarização.
- **BERTScore**: Similaridade semântica usando embeddings contextuais (mais robusta que BLEU).
- **METEOR**: Faz alinhamento com sinônimos e radicais do WordNet.

---

## Armadilhas na avaliação

### Vazamento de dados
Ocorre quando informações do conjunto de teste influenciam o treinamento sem querer.
- **Prevenção:** Nunca use dados de teste para engenharia de atributos, normalização ou ajuste de hiperparâmetros.
- **Detecção:** Se o modelo obtiver resultados suspeitamente altos, desconfie de vazamento.

### Overfitting
O modelo tem bom desempenho nos dados de treino, mas vai mal na validação/teste.
- **Mitigação:** Use regularização, early stopping, simplifique a arquitetura ou colete mais dados.

### Underfitting
O modelo apresenta baixo desempenho tanto no treino quanto na validação.
- **Mitigação:** Use um modelo mais complexo, adicione atributos ou reduza a regularização.

### Dados desbalanceados
- **Mitigação:** Use pesos de classe, oversampling (SMOTE), undersampling ou métricas apropriadas (F1, AUC-PR) em vez de accuracy.

### Drift temporal (Concept Drift)
A relação entre os atributos e o alvo muda ao longo do tempo.
- **Mitigação:** Reentreine periodicamente, monitore o desempenho e use algoritmos de detecção de drift.

---

## Ajuste de hiperparâmetros

- **Grid Search**: Testa exaustivamente todas as combinações de um conjunto predefinido de hiperparâmetros. Simples, mas computacionalmente caro.
- **Random Search**: Amostra combinações aleatórias a partir de distribuições. Mais eficiente que grid search em espaços de alta dimensionalidade.
- **Bayesian Optimisation**: Constrói um modelo probabilístico da função objetivo e seleciona hiperparâmetros de forma inteligente. Bibliotecas: Optuna, Hyperopt, scikit-optimise.
- **Automated Tuning**: Use ferramentas como Optuna, Ray Tune ou Weights & Biases Sweeps para ajuste distribuído.

**Faixas de busca sugeridas para hiperparâmetros comuns:**

| Parâmetro | Faixa sugerida (escala log) |
|-----------|-----------------------------|
| Learning rate | 1e-5 a 1e-1 |
| Batch size | 16, 32, 64, 128, 256 |
| Número de camadas (NN) | 2 a 6 |
| Número de neurônios (NN) | 32 a 1024 |
| Regularização (L2) | 1e-6 a 1e-2 |
| Profundidade da árvore (XGBoost) | 3 a 12 |

---

## Seleção e validação de modelos

1. **Modelo de baseline**: Comece com uma heurística simples ou um modelo simples (ex.: regressão logística, preditor da média) para estabelecer um limite inferior.
2. **Modelos candidatos**: Treine várias famílias de modelos (ex.: Random Forest, XGBoost, Rede Neural).
3. **Faça validação cruzada** de cada candidato no conjunto de validação.
4. **Compare métricas** (com intervalos de confiança) e selecione o melhor candidato.
5. **Avaliação final** no conjunto de teste separado.
6. **Análise de erros**: Observe exemplos em que o modelo erra. Identifique padrões (ex.: classes raras, entradas ambíguas) e leve esses insights de volta para a preparação dos dados ou a engenharia de atributos.

---

## Implantação e monitoramento

### Padrões de serving
- **Inferência em lote**: Processa grandes volumes de dados offline (ex.: recomendações noturnas).
- **Inferência online**: Predições em tempo real via API (ex.: score de crédito, detecção de fraude).
- **Inferência em streaming**: Orientada a eventos, em tempo real e com baixa latência (ex.: alertas de sensores IoT).

### Monitoramento do modelo
- **Monitoramento de desempenho**: Acompanhe accuracy/F1 ao longo do tempo em dados reais (quando o ground truth estiver disponível).
- **Data drift**: Monitore mudanças nas distribuições dos atributos de entrada (ex.: usando PSI – Population Stability Index).
- **Concept drift**: Monitore mudanças na relação entre entradas e saídas.
- **Prediction drift**: Acompanhe a distribuição das saídas previstas.
- **Latência e throughput**: Garanta que os SLAs (Service Level Agreements) sejam cumpridos.

### Logging e alertas
- Registre todas as requisições e respostas de predição (com anonimização).
- Configure alertas para:
  - Queda significativa de desempenho.
  - Alta porcentagem de entradas ausentes ou inválidas.
  - Saídas do modelo fora dos limites esperados.

### Versionamento e registry de modelos
- Use um model registry (ex.: MLflow, Weights & Biases, Sagemaker Model Registry) para armazenar e versionar modelos, metadados e resultados de avaliação.
- Armazene o código de treinamento e a versão dos dados (via DVC ou Git LFS) junto com o modelo.

---

## Checklist prático do fluxo de trabalho

- [ ] Problema definido e métrica de sucesso estabelecida.
- [ ] Exploração dos dados realizada (valores ausentes, outliers, distribuição).
- [ ] Divisão treino/validação/teste criada (estratificada, se necessário).
- [ ] Modelo de baseline estabelecido.
- [ ] Modelos candidatos treinados e validados.
- [ ] Hiperparâmetros ajustados.
- [ ] Melhor modelo selecionado por validação cruzada.
- [ ] Avaliação final no conjunto de teste.
- [ ] Análise de erros realizada.
- [ ] Plano de implantação pronto (infraestrutura de serving).
- [ ] Dashboard de monitoramento configurado.
- [ ] Documentação (data card, model card) concluída.
