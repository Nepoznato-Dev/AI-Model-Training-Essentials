<!--
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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to engineering/ subfolder; added subcategory field"
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

-->
# Ingeniería ML y MLOps
Construir un modelo de aprendizaje automático es sólo la mitad de la batalla. Ponerlo en producción, mantenerlo funcionando de manera confiable, monitorear la desviación e iterarlo: ahí es donde entran en juego la ingeniería de aprendizaje automático y MLOps. Este archivo cubre el ciclo de vida completo desde el experimento hasta el sistema de producción.
---

## El ciclo de vida del aprendizaje automático
| Fase | Descripción | Actividades clave |
|-------|-------------|---------------|
| **1. Definición del problema** | Enmarcar el problema empresarial como una tarea de ML | Definir métricas, restricciones, criterios de éxito |
| **2. Recopilación de datos** | Recopilar y etiquetar datos de entrenamiento | ETL, etiquetado, aumento |
| **3. Experimentación** | Entrenar y evaluar modelos | Ingeniería de funciones, ajuste de hiperparámetros |
| **4. Selección de modelo** | Elige el mejor modelo | Comparar métricas, evaluar compensaciones |
| **5. Implementación** | Enviar el modelo a producción | Infraestructura de servicio, API, lotes |
| **6. Monitoreo** | Esté atento a la deriva y la degradación | Deriva de datos, deriva de conceptos, rendimiento |
| **7. Reciclaje** | Actualizar el modelo con nuevos datos | Reentrenamiento programado o iniciado |
La mayor parte del valor (y la dificultad) se encuentra en las fases 5 a 7. Un modelo sentado en una computadora portátil Jupyter no crea valor comercial.
---

## Patrones de publicación de modelos
| Patrón | Descripción | Latencia | Caso de uso |
|---------|-------------|---------|----------|
| **Inferencia por lotes** | Ejecutar el modelo en un lote de datos según un cronograma | Horas | Recomendaciones diarias, puntuación de fraude |
| **Inferencia en línea** | Predicción en tiempo real por solicitud | Milisegundos | Ranking de búsqueda, clasificación en tiempo real |
| **Inferencia de transmisión** | Procesar predicciones en un flujo de datos | Segundos | Detección de anomalías, procesamiento de eventos |
### Infraestructura de servicio
| Herramienta | Tipo | Mejor para |
|------|------|----------|
| **Servicio de TensorFlow** | Servidor de modelos | Modelos TensorFlow |
| **Servicio de antorcha** | Servidor de modelos | Modelos PyTorch |
| **Servidor de inferencia Triton** | Marco múltiple | Inferencia de GPU, múltiples marcos |
| **vLLM** | Servicio de LLM | Inferencia LLM de alto rendimiento |
| **BentoML** | Servicio unificado | Implementación independiente del marco |
| **Seldon** | K8s-nativo | Implementación del modelo Kubernetes |
| **Servicio de rayos** | Servicio escalable | Grandes modelos, inferencia distribuida |
---

## Registros de modelos
Un registro de modelos es un almacén centralizado para administrar modelos de aprendizaje automático: sus versiones, metadatos, métricas y estado de implementación.
| Capacidad | Descripción |
|-----------|-------------|
| **Versionamiento** | Realice un seguimiento de cada versión del modelo con una identificación única |
| **Metadatos** | Datos de entrenamiento, hiperparámetros, métricas, autor |
| **Transiciones de escenario** | Mover modelos a través de etapas: Puesta en escena → Producción → Archivado |
| **Linaje** | Rastree qué datos y códigos produjeron cada modelo |
| Herramienta | Descripción |
|------|-------------|
| **flujo ML** | Código abierto; registro de modelos + seguimiento de experimentos |
| **Pesos y sesgos (W&B)** | Comercial; seguimiento de experimentos + registro de modelos |
| **DVC** | Versionado de datos y modelos con Git |
| **Azure ML/SageMaker** | Gestión de modelos nativos de la nube |
---

## Seguimiento de experimentos
Se debe realizar un seguimiento de cada experimento de ML: qué datos se utilizaron, qué hiperparámetros, qué métricas resultaron.
| Herramienta | Características clave |
|------|-------------|
| **flujo ML** | Código abierto, autohospedado, rastrea parámetros/métricas/artefactos |
| **D&B** | Interfaz de usuario enriquecida, barridos, control de versiones de artefactos, informes |
| **Neptuno** | Almacén de metadatos para MLOps |
| **Tablero Tensor** | Integrado en TensorFlow; visualizar curvas de entrenamiento |
### Qué rastrear
| Categoría | Ejemplos |
|----------|---------|
| **Parámetros** | Tasa de aprendizaje, tamaño de lote, arquitectura del modelo, número de épocas |
| **Métricas** | Precisión, pérdida, F1, AUC-ROC (por época y final) |
| **Artefactos** | Pesos de modelos, matrices de confusión, muestras de predicción |
| **Datos** | Versión del conjunto de datos, proporciones de división, pasos de preprocesamiento |
| **Medio ambiente** | Versión de Python, versiones de biblioteca, hardware |
---

## Estrategias de implementación del modelo
| Estrategia | Cómo funciona | Riesgo |
|----------|-------------|------|
| **Despliegue de sombras** | El nuevo modelo corre al lado del antiguo; predicciones comparadas pero no cumplidas | Riesgo cero; valida antes de entrar en funcionamiento |
| **Lanzamiento en Canarias** | Dirigir un pequeño porcentaje del tráfico hacia el nuevo modelo; aumentar gradualmente | Bajo riesgo; retroceso rápido |
| **Pruebas A/B** | Dividir a los usuarios entre antiguos y nuevos; comparar métricas comerciales | Mide el impacto real |
| **Azul-Verde** | Dos ambientes idénticos; cambiar todo el tráfico a la vez | Reversión instantánea; doble costo durante la transición |
| **Banderas de funciones** | Activar/desactivar modelo por segmento de usuario | Control detallado |
---

## Monitoreo de sistemas de aprendizaje automático
Los sistemas de aprendizaje automático necesitan más monitoreo que el software tradicional porque los datos en sí pueden cambiar.
### Tipos de deriva
| Tipo de deriva | Qué cambia | Ejemplo |
|-----------|-------------|---------|
| **Deriva de datos** | Cambios en la distribución de insumos | La demografía de los clientes cambia después de una campaña de marketing |
| **Deriva conceptual** | Relación entre cambios de entrada y salida | El comportamiento del consumidor cambia durante una recesión |
| **Desviación de etiquetas** | Cambios en la distribución objetivo | Tasa de fraude aumenta del 1% al 5% |
### Qué monitorear
| Categoría | Métricas |
|----------|---------|
| **Rendimiento del modelo** | Exactitud, precisión, recuperación, F1, AUC (en comparación con el valor inicial) |
| **Calidad de los datos** | Valores faltantes, distribuciones de características, valores atípicos |
| **Detección de deriva** | Pruebas estadísticas (prueba KS, PSI, divergencia KL) |
| **Infraestructura** | Latencia, rendimiento, utilización de GPU, memoria |
| **Métricas comerciales** | Tasa de conversión, impacto en los ingresos, satisfacción del usuario |
### Herramientas de monitoreo
| Herramienta | Tipo |
|------|------|
| **Evidentemente IA** | Supervisión del rendimiento del modelo y deriva de datos de código abierto |
| **Gráfana** | Visualización del panel (funciona con Prometheus) |
| **Por quéLabs** | Plataforma de observabilidad de datos |
| **Arize** | Observabilidad de ML y análisis de causa raíz |
| **Prometeo + Grafana** | Métricas de infraestructura y aplicaciones |
---

## Entrenamiento reproducible
La reproducibilidad significa que puede volver a ejecutar un experimento y obtener el mismo resultado. Es esencial para la depuración, la auditoría y el cumplimiento.
### Requisitos
| Requisito | Cómo lograrlo |
|-------------|-------------------|
| **Versionado de datos** | Instantáneas de DVC, Delta Lake o conjuntos de datos con hashes |
| **Versionado de código** | Git para todo el código de entrenamiento |
| **Fijación del entorno** |  `requirements.txt`, `conda env`, imágenes de Docker con versiones exactas |
| **Ajuste de semillas** | Arreglar semillas aleatorias para numpy, torch, tensorflow |
| **Gestión de configuración** | Configuraciones Hydra, OmegaConf o YAML para todos los hiperparámetros |
| **Seguimiento de artefactos** | MLflow o W&B para registrar cada experimento |
---

## Inferencia de escala
Cuando un modelo necesita atender millones de solicitudes por día, el rendimiento importa.
| Técnica | Descripción |
|-----------|-------------|
| **Procesamiento por lotes** | Agrupe varias solicitudes en un único pase directo |
| **Cuantización** | Reduzca la precisión del modelo (FP32 → INT8 o INT4) para una inferencia más rápida |
| **Destilación modelo** | Entrena un modelo más pequeño para imitar uno más grande |
| **Poda** | Eliminar pesos o neuronas sin importancia |
| **Almacenamiento en caché** | Almacenar en caché las predicciones frecuentes para evitar un nuevo cálculo |
| **Optimización de GPU** | TensorRT, ONNX Runtime, Atención Flash |
| **Escala horizontal** | Ejecute varias réplicas de modelos detrás de un equilibrador de carga |
---

## Indicadores de funciones para ML
Los indicadores de funciones le permiten controlar qué versión del modelo sirve a qué usuarios, sin tener que volver a implementarlo.
| Caso de uso | Descripción |
|----------|-------------|
| **Implementación gradual** | Ofrezca un nuevo modelo al 5% de los usuarios y luego aumente |
| **Interruptor de apagado** | Vuelva instantáneamente al modelo anterior si se detectan problemas |
| **Basado en segmentos** | Diferentes modelos para diferentes segmentos de usuarios |
| **Experimentación** | Variantes del modelo de prueba A/B con métricas comerciales |
Herramientas: LaunchDarkly, Unleash, Flagsmith o indicadores de funciones simples respaldados por bases de datos.
---

## La curva de madurez de MLOps
| Nivel | Características |
|-------|----------------|
| **Nivel 0 — Manual** | Entrenamiento manual, implementación manual, sin monitoreo |
| **Nivel 1: Experimentación** | Seguimiento de experimentos, registro de modelos, CI básica |
| **Nivel 2: Automatización** | Reentrenamiento automatizado, CI/CD para modelos, pruebas automatizadas |
| **Nivel 3: proceso completo** | Tubería automatizada de extremo a extremo con monitoreo, detección de deriva y reentrenamiento automático |
La mayoría de las organizaciones se encuentran entre el nivel 0 y el nivel 1. El objetivo es el nivel 2-3, donde el ciclo de vida del aprendizaje automático es automatizado y autorreparable.