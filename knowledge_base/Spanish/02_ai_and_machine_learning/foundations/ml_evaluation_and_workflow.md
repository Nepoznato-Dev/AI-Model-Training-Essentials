<!--
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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# Evaluación y flujo de trabajo del aprendizaje automático
Una guía práctica para el ciclo de vida del aprendizaje automático, desde la formulación de problemas hasta el monitoreo de la producción, con un enfoque en métricas, validación y depuración.
---

## El flujo de trabajo de ML (CRISP-ML)
1. **Entendimiento empresarial**: Definir el objetivo y los criterios de éxito.
2. **Comprensión de los datos**: explore los datos disponibles, identifique problemas de calidad.
3. **Preparación de datos**: Limpiar, transformar y dividir datos.
4. **Modelado**: entrene modelos, ajuste hiperparámetros.
5. **Evaluación**: Evalúe el desempeño frente a métricas.
6. **Implementación**: entrega el modelo en producción.
7. **Monitoreo**: realice un seguimiento de la deriva, el rendimiento y las anomalías.
Este es un ciclo iterativo: revisará los pasos anteriores según los resultados de la evaluación.
---

## División de datos
### Entrenamiento / Validación / Prueba dividida
- **Conjunto de entrenamiento** (~70%): Se utiliza para ajustar los parámetros del modelo.
- **Conjunto de validación** (~15%): se utiliza para ajustar hiperparámetros y seleccionar variantes de modelo.
- **Conjunto de prueba** (~15%): se usa solo una vez al final para estimar el rendimiento de la generalización.
**Importante:** El equipo de prueba debe mantenerse completamente intacto hasta la evaluación final para evitar la fuga de datos.
### Validación cruzada (k veces)
Para conjuntos de datos pequeños, utilice la validación cruzada de k veces: divida los datos en k veces, entrene en k-1, valide el resto y repita k veces. Promediar el rendimiento. k=5 o k=10 es común.
### División estratificada
Para la clasificación con clases desequilibradas, utilice divisiones estratificadas para preservar las proporciones de clase en cada subconjunto.
### División basada en el tiempo
Para los datos de series temporales, divídalos cronológicamente (entrenamiento en el pasado, prueba en el futuro) en lugar de aleatoriamente.
---

## Métricas de evaluación
### Métricas de clasificación
| Métrica | Qué mide | Mejor utilizado para |
|--------|------------------|---------------|
| **Precisión** | (TP + TN) / (TP + TN + FP + FN) | Conjuntos de datos equilibrados |
| **Precisión** | TP/(TP+FP) | Cuando los falsos positivos son costosos (por ejemplo, detección de spam) |
| **Recordar** | TP/(TP+FN) | Cuando los falsos negativos son costosos (por ejemplo, pruebas de detección del cáncer) |
| **Puntuación F1** | Media armónica de precisión y recuperación | Conjuntos de datos desequilibrados, métrica de un solo número |
| **AUC-ROC** | Área bajo la curva ROC; equilibrio entre TPR y FPR | Rendimiento del clasificador general independiente del umbral |
| **AUC-PR** | Área bajo la curva de recuperación de precisión | Conjuntos de datos altamente desequilibrados |
**Definiciones:**
- TP = Verdadero Positivo
- TN = Verdadero Negativo
- FP = Falso Positivo (error Tipo I)
- FN = Falso Negativo (error Tipo II)
### Métricas de regresión
| Métrica | Qué mide | Sensibilidad a los valores atípicos |
|--------|------------------|--------------------------|
| **MSE** (Error cuadrático medio) | Diferencia media al cuadrado | Alto |
| **RMSE** (Error cuadrático medio) | Raíz cuadrada de MSE (las mismas unidades que el objetivo) | Alto |
| **MAE** (Error medio absoluto) | Diferencia absoluta media | Bajo |
| **R²** (Coeficiente de Determinación) | Proporción de varianza explicada | Ninguno directamente, pero sensible indirectamente a los valores atípicos |
### Métricas de clasificación y recuperación
- **Precision@k**: fracción de elementos relevantes entre las k recomendaciones principales.
- **Recall@k**: Fracción de todos los elementos relevantes que aparecen en top-k.
- **NDCG** (Ganancia acumulada descontada normalizada): Cuentas por relevancia de la posición.
- **Tasa de aciertos**: si un elemento relevante aparece en el top-k.
### Métricas generativas / LLM
- **Perplejidad**: Qué tan "sorprendida" está la modelo por un texto extendido (cuanto más bajo, mejor).
- **BLEU**: superposición de n-gramas con traducciones de referencia (centradas en precisión).
- **ROUGE**: Superposición orientada al recuerdo para el resumen.
- **BERTScore**: Similitud semántica mediante incrustaciones contextuales (más robusta que BLEU).
- **METEOR**: Se alinea con sinónimos y raíces de WordNet.
---

## Errores de la evaluación
### Fuga de datos
Ocurre cuando la información del conjunto de pruebas influye inadvertidamente en el entrenamiento.
- **Prevenir:** Nunca utilice datos de prueba para ingeniería de funciones, normalización o ajuste de hiperparámetros.
- **Detectar:** Si su modelo obtiene una puntuación sospechosamente alta, sospeche de una fuga.
### Sobreajuste
El modelo funciona bien con los datos de entrenamiento, pero tiene un rendimiento deficiente en la validación/prueba.
- **Mitigar:** Utilice la regularización, la detención anticipada, simplifique la arquitectura o recopile más datos.
### Falta de adaptación
El modelo funciona mal tanto en entrenamiento como en validación.
- **Mitigar:** Utilice un modelo más complejo, agregue funciones o reduzca la regularización.
### Datos desequilibrados
- **Mitigar:** Utilice ponderaciones de clase, sobremuestreo (SMOTE), submuestreo o utilice métricas apropiadas (F1, AUC-PR) en lugar de precisión.
### Deriva temporal (deriva conceptual)
La relación entre las características y el objetivo cambia con el tiempo.
- **Mitigar:** Vuelva a capacitarse periódicamente, supervise el rendimiento, utilice algoritmos de detección de deriva.
---

## Ajuste de hiperparámetros
- **Búsqueda de cuadrícula**: pruebe exhaustivamente todas las combinaciones de un conjunto predefinido de hiperparámetros. Simple pero computacionalmente costoso.
- **Búsqueda aleatoria**: muestra de combinaciones aleatorias de distribuciones. Más eficiente que la búsqueda en cuadrícula para espacios de alta dimensión.
- **Optimización bayesiana**: construye un modelo probabilístico de la función objetivo y selecciona hiperparámetros de forma inteligente. Bibliotecas: Optuna, Hyperopt, scikit-optimise.
- **Ajuste automatizado**: utilice herramientas como Optuna, Ray Tune o Weights & Biases Sweeps para realizar ajustes distribuidos.
**Rangos de búsqueda sugeridos para hiperparámetros comunes:**
| Parámetro | Rango sugerido (escala logarítmica) |
|-----------|-----------------------|
| Tasa de aprendizaje | 1e-5 a 1e-1 |
| Tamaño del lote | 16, 32, 64, 128, 256 |
| Número de capas (NN) | 2 a 6 |
| Número de neuronas (NN) | 32 a 1024 |
| Regularización (L2) | 1e-6 a 1e-2 |
| Profundidad del árbol (XGBoost) | 3 a 12 |
---

## Selección y validación del modelo
1. **Modelo de referencia**: comience con un modelo heurístico simple o simple (por ejemplo, regresión logística, predictor de media) para establecer un límite inferior.
2. **Modelos candidatos**: entrene varias familias de modelos (por ejemplo, Random Forest, XGBoost, Neural Network).
3. **Validación cruzada** de cada candidato en el conjunto de validación.
4. **Compare métricas** (con intervalos de confianza) y seleccione el mejor candidato.
5. **Evaluación final** en el conjunto de prueba retenido.
6. **Análisis de errores**: mire ejemplos en los que el modelo se equivoca. Identifique patrones (por ejemplo, clases raras, entradas ambiguas) y aporte información valiosa a la preparación de datos o la ingeniería de funciones.
---

## Implementación y monitoreo
### Patrones de servicio
- **Inferencia por lotes**: procese grandes volúmenes de datos sin conexión (por ejemplo, recomendaciones nocturnas).
- **Inferencia en línea**: predicciones en tiempo real a través de API (por ejemplo, calificación crediticia, detección de fraude).
- **Inferencia de transmisión**: basada en eventos, en tiempo real con baja latencia (por ejemplo, alertas de sensores de IoT).
### Monitoreo del modelo
- **Monitoreo de rendimiento**: realice un seguimiento de la precisión/F1 a lo largo del tiempo en datos en vivo (cuando la verdad sobre el terreno esté disponible).
- **Deriva de datos**: Supervise los cambios en las distribuciones de características de entrada (por ejemplo, utilizando PSI – Índice de estabilidad de la población).
- **Deriva de conceptos**: Monitorear cambios en la relación entre entradas y salidas.
- **Deriva de predicción**: realice un seguimiento de la distribución de los resultados previstos.
- **Latencia y rendimiento**: asegúrese de que se cumplan los SLA (acuerdos de nivel de servicio).
### Registro y alertas
- Registre todas las solicitudes y respuestas de predicción (con anonimización).
- Establecer alertas para:
  - Caída significativa del rendimiento.
  - Alto porcentaje de entradas faltantes o no válidas.
  - Modelar resultados fuera de los límites esperados.
### Control de versiones y registro del modelo
- Utilice un registro de modelos (por ejemplo, MLflow, Weights & Biases, Sagemaker Model Registry) para almacenar y versionar modelos, metadatos y resultados de evaluación.
- Almacene el código de entrenamiento y la versión de los datos (a través de DVC o Git LFS) junto con el modelo.
---

## Lista de verificación práctica del flujo de trabajo
- [ ] Problema enmarcado y métrica de éxito definida.
- [ ] Exploración de datos realizada (valores faltantes, valores atípicos, distribución).
- [] División de entrenamiento/validación/prueba creada (estratificada si es necesario).
- [ ] Modelo de línea base establecido.
- [ ] Modelos candidatos entrenados y validados.
- [] Hiperparámetros ajustados.
- [ ] Mejor modelo seleccionado mediante validación cruzada.
- [ ] Evaluación final en el set de prueba.
- [ ] Análisis de errores realizado.
- [ ] Plan de implementación listo (infraestructura de servicio).
- [ ] Configuración del panel de seguimiento.
- [ ] Documentación (ficha de datos, ficha de modelo) cumplimentada.