---
# Metadata
title: "Data Science and Analytics"
description: "Data processing, ML, big data, BI"
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
tags: [data, science, analytics, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Ciencia de datos y análisis
La ciencia de datos es la disciplina de convertir datos sin procesar en información procesable. Se encuentra en la intersección de la estadística, la informática y la experiencia en el campo, y se ha vuelto esencial en todos los sectores, desde las finanzas hasta la atención médica. Este archivo recorre los conceptos, herramientas y flujos de trabajo principales que todo profesional debería conocer.
---

## El proceso de ciencia de datos
La mayoría de los proyectos siguen alguna variación de **CRISP-DM**, el ciclo de vida estándar de la industria:
| Fase | Qué pasa | Hora típica |
|-------|-------------|--------------|
| **Comprensión empresarial** | Definir objetivos, métricas de éxito y limitaciones | 10-15% |
| **Comprensión de datos** | Recopile, explore y perfile los datos | 10-15% |
| **Preparación de datos** | Limpiar, transformar y diseñar funciones | ~50–60% |
| **Modelado** | Seleccionar y entrenar modelos | 10-15% |
| **Evaluación** | Evaluar el desempeño frente a los objetivos comerciales | 5-10% |
| **Implementación** | Enviar el modelo a producción | 5-10% |
Se estima ampliamente que la preparación de datos, particularmente la limpieza de datos, consume alrededor del 80% del tiempo de un científico de datos.
---

## Tipos de datos de un vistazo
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Estructurado** | Organizado en filas y columnas | Tablas SQL, hojas de cálculo |
| **Sin estructura** | Sin formato predefinido | Texto, imágenes, audio, vídeo |
| **Semiestructurado** | Alguna organización pero flexible | JSON, XML, HTML |
| **Serie temporal** | Datos secuenciales indexados por tiempo | Precios de acciones, lecturas de sensores |
| **Espacial** | Basado en ubicación geográfica o | Coordenadas GPS, datos de mapas |
| **Gráfico** | Nodos y aristas que representan relaciones | Redes sociales, gráficos de conocimiento |
---

## Fundamentos de estadística
### Estadística descriptiva versus inferencial
Las estadísticas descriptivas resumen lo que *tienes*; Las estadísticas inferenciales le permiten sacar conclusiones sobre lo que *no* tiene (la población en general).
| Concepto | Ideas clave |
|---------|-----------|
| **Tendencia central** | Media (sensible a valores atípicos), mediana (robusta), moda (más frecuente) |
| **Dispersión** | Rango, varianza, desviación estándar, rango intercuartil |
| **Forma de distribución** | Asimetría (asimetría), curtosis (pesadez de la cola) |
| **Prueba de hipótesis** | Hipótesis nula versus alternativa, valores p, nivel de significancia (α) |
| **Intervalos de confianza** | Rango que probablemente contenga el verdadero parámetro de población |
| **Errores tipo I/Tipo II** | Falso positivo (rechazando un verdadero nulo) / falso negativo (faltando un efecto real) |
### Pruebas estadísticas comunes
| Prueba | Cuándo utilizar |
|------|-------------|
| **prueba t** | Comparar medias entre dos grupos |
| **ANOVA** | Comparar medias en tres o más grupos |
| **Chi-cuadrado** | Prueba de independencia de variables categóricas |
| **Mann-Whitney U** | Alternativa no paramétrica a la prueba t (sin supuesto de normalidad) |
| **Correlación de Pearson** | Relación lineal entre dos variables continuas |
| **Correlación de lancero** | Relación monótona (basada en rangos, más sólida) |
### Distribuciones de probabilidad que vale la pena conocer
| Distribución | Caso de uso |
|-------------|----------|
| **Normal** | Fenómenos naturales, errores de medición: la clásica curva de campana |
| **Binomio** | Recuentos de éxito/fracaso (lanzamientos de moneda, tasas de conversión) |
| **Poisson** | Recuento de eventos en un intervalo fijo (llamadas por hora, defectos por lote) |
| **Exponencial** | Tiempo entre eventos (tiempos de espera, intervalos de falla) |
| **Distribución t** | Muestras pequeñas o varianza poblacional desconocida |
| **Chi-cuadrado** | Análisis de datos categóricos, pruebas de bondad de ajuste |
---

## Recopilación y almacenamiento de datos
### De dónde provienen los datos
Los datos del mundo real provienen de muchas fuentes: bases de datos relacionales, API (REST, GraphQL), archivos planos (CSV, JSON, Parquet), plataformas de transmisión (Kafka, Kinesis), encuestas y repositorios públicos (Kaggle, portales gubernamentales). El formato que recibe determina gran parte de su estrategia de preprocesamiento.
### Conceptos de almacenamiento de datos
| Concepto | Descripción |
|---------|-------------|
| **ETL** | Extraer → Transformar → Cargar: enfoque tradicional de canalización |
| **ELT** | Extraer → Cargar → Transformar: enfoque moderno en la nube (carga sin procesar, transformación en el almacén) |
| **Lago de datos** | Datos sin procesar almacenados en formato nativo (esquema en lectura) |
| **Almacén de datos** | Datos estructurados y procesados ​​optimizados para el análisis (esquema en escritura) |
| **Centro de datos** | Un subconjunto de un almacén, con ámbito de un departamento o dominio |
| **Esquema de estrellas** | Mesa central de hechos rodeada de tablas de dimensiones |
| **Esquema de copo de nieve** | Tablas de dimensiones normalizadas (menos redundancia, más uniones) |
### Tipos de bases de datos
| Tipo | Ejemplos | Mejor para |
|------|----------|----------|
| **Relacional (SQL)** | PostgreSQL, MySQL, Oracle | Datos estructurados, transacciones ACID |
| **Documento** | MongoDB, CouchDB | Esquemas flexibles, datos tipo JSON |
| **Valor clave** | Redis, DynamoDB | Almacenamiento en caché, sesiones, búsquedas simples |
| **Columna-Familia** | Casandra, HBase | Cargas de trabajo con mucha escritura, series temporales |
| **Gráfico** | Neo4j, Amazonas Neptuno | Relaciones, redes sociales |
| **Series temporales** | InfluxDB, escala de tiempoDB | Métricas de IoT, seguimiento |
| **Vector** | Piña, Milvus | Incorporación de almacenamiento para búsqueda de ML/AI |
---

## Preprocesamiento de datos e ingeniería de funciones
### Lista de verificación de limpieza
Todo conjunto de datos real tiene problemas. Aquí está la limpieza estándar:
| Problema | Enfoque |
|-------|----------|
| **Valores faltantes** | Imputación (media, mediana, predicción) o eliminación si es escasa |
| **Valores atípicos** | Detectar mediante IQR o puntuación Z; tratar con tapado o transformación |
| **Duplicados** | Identificar y eliminar |
| **Inconsistencias** | Estandarizar formatos, corregir errores tipográficos, normalizar unidades |
### Técnicas de transformación
| Técnica | Qué hace |
|-----------|-------------|
| **Normalización** | Escala los valores al rango 0–1 |
| **Estandarización** | Puntuación Z: media = 0, estándar = 1 |
| **Codificación one-hot** | Convierte categorías a columnas binarias |
| **Codificación de etiquetas** | Asigna etiquetas de números enteros a categorías |
| **Transformación de registro** | Reduce el sesgo a la derecha en los datos |
| **Agrupación** | Agrupa valores continuos en grupos discretos |
### Ingeniería de funciones
La ingeniería de características suele ser la diferencia entre un modelo mediocre y uno excelente. Las técnicas clave incluyen:
- **Creación de funciones**: derivar nuevas columnas a partir de las existentes (por ejemplo,`age_group`de `age`).
- **Selección de características**: métodos de filtrado (correlación), métodos de envoltura (eliminación recursiva), métodos integrados (LASSO, importancia del árbol).
- **Reducción de dimensionalidad**: PCA para lineal, t-SNE o UMAP para visualización.
- **Términos de interacción**: combinación de funciones de forma multiplicativa para capturar efectos conjuntos.
---

## Análisis de datos exploratorios (EDA)
EDA es donde desarrolla la intuición sobre sus datos antes de modelarlos. El objetivo es detectar patrones, anomalías y relaciones.
### Elegir el gráfico correcto
| Tipo de gráfico | Mejor para |
|-----------|----------|
| **Histograma** | Distribución de una sola variable |
| **Gráfico de caja** | Resumen de cinco números, detección de valores atípicos |
| **Gráfico de dispersión** | Relación entre dos variables continuas |
| **Mapa de calor** | Matrices de correlación, visualización de densidad |
| **Gráfico de barras** | Comparando categorías |
| **Gráfico de líneas** | Tendencias a lo largo del tiempo |
| **Trama de violín** | Densidad de distribución + resumen del diagrama de caja |
| **Gráfico de pares** | Resumen rápido de todos los pares de variables |
### La pila EDA de Python
| Biblioteca | Rol |
|---------|------|
| **pandas** | Manipulación y análisis de datos |
| **numeroso** | Computación numérica |
| **matplotlib** | Trazado de cimientos |
| **nacido en el mar** | Visualización estadística (construida en matplotlib) |
| **trama** | Visualizaciones interactivas basadas en web |
| **especie** | Informática científica y estadística |
---

## Aprendizaje automático en ciencia de datos
### Aprendizaje supervisado de un vistazo
| Tarea | Algoritmos |
|------|-----------|
| **Regresión** (predecir un número) | Lineal, Ridge/LASSO, Árbol de decisión, Bosque aleatorio, Aumento de gradiente (XGBoost, LightGBM) |
| **Clasificación** (predecir una categoría) | Regresión logística, k-NN, Naive Bayes, SVM, árboles de decisión, bosque aleatorio, redes neuronales |
### Aprendizaje no supervisado de un vistazo
| Tarea | Algoritmos |
|------|-----------|
| **Agrupación** | k-medias, jerárquicos, DBSCAN, modelos de mezcla gaussiana |
| **Reducción de dimensionalidad** | PCA, t-SNE, UMAP, codificadores automáticos |
| **Reglas de la Asociación** | A priori, FP-Crecimiento |
### Evaluación del modelo
| Tipo de métrica | Métricas clave |
|-------------|-------------|
| **Clasificación** | Exactitud, precisión, recuperación, puntuación F1, ROC-AUC, matriz de confusión |
| **Regresión** | MAE, MSE, RMSE, R², R² ajustado |
| **Validación** | validación cruzada de k veces, estratificada, división de series temporales |
| **Sintonización** | Búsqueda en cuadrícula, búsqueda aleatoria, optimización bayesiana |
---

## Tecnologías de Big Data
Cuando los conjuntos de datos exceden lo que una sola máquina puede manejar, la computación distribuida entra en escena.
| Marco | Fuerza |
|-----------|----------|
| **Apache Chispa** | Procesamiento en memoria; Spark SQL, transmisión, MLlib, GraphX ​​|
| **ApacheHadoop** | MapReduce + HDFS: la pila de big data original |
| **Apache Flink** | Procesamiento de flujo de baja latencia |
| **Haz Apache** | Modelo unificado por lotes y streaming |
### Plataformas de datos en la nube
| Proveedor | Servicios clave |
|----------|-------------|
| **AWS** | S3, EMR, corrimiento al rojo, SageMaker, pegamento |
| **Google Nube** | BigQuery, Dataproc, plataforma AI, almacenamiento en la nube |
| **Azul** | Synapse Analytics, Databricks, aprendizaje automático, lago de datos |
| **Copo de nieve** | Almacén de datos nativo de la nube (independiente del proveedor) |
### Orquestación de canalizaciones
| Herramienta | Notas |
|------|-------|
| **Flujo de aire Apache** | Estándar de la industria; DAG basados ​​en Python |
| **Prefecto** | Alternativa moderna con API más limpia |
| **Dagster** | Orquestación centrada en activos |
| **dbt** | Transformación de datos por primera vez en SQL en el almacén |
---

## Inteligencia empresarial y análisis
### Herramientas de BI comparadas
| Herramienta | Tipo | Fuerza |
|------|------|----------|
| **Cuadro** | Comercial | Análisis visual enriquecido, arrastrar y soltar |
| **PowerBI** | Comercial (Microsoft) | Integración profunda de Office/Azure |
| **Mirador** | Comercial (Google) | Exploración de datos, modelado LookML |
| **Metabase** | Código abierto | Fácil configuración, SQL nativo |
| **Superconjunto** | Código abierto (Apache) | Escalable, SQL primero |
### Principios de diseño del panel
Los buenos paneles siguen algunas reglas: conozca a su audiencia, elija la visualización adecuada para cada métrica, use el color de manera estratégica (no decorativa), mantenga escalas consistentes y habilite la interactividad (filtros, desgloses). El rendimiento también importa: nadie espera por un panel lento.
### Categorías de KPI comunes
| Categoría | Ejemplos |
|----------|---------|
| **Financiero** | Ingresos, margen de beneficio, ROI, valor de vida del cliente |
| **Cliente** | Costo de adquisición (CAC), tasa de abandono, NPS, puntuación de satisfacción |
| **Operativo** | Tasas de eficiencia, tiempo de ciclo, tasas de defectos |
| **Mercadotecnia** | Tasa de conversión, tasa de clics, ROAS, atribución |
| **Producto** | Usuarios activos diarios, participación, retención, adopción de funciones |
---

## Análisis avanzado
| Enfoque | Técnicas | Cuándo utilizar |
|----------|-----------|-------------|
| **Predictivo** | Series temporales (ARIMA, Prophet, LSTM), modelización de riesgos, predicción de abandono | Previsión de valores futuros |
| **Prescriptivo** | Programación lineal, simulación Monte Carlo, pruebas A/B, bandidos con múltiples brazos | Optimización de decisiones |
| **Análisis de texto** | Tokenización, análisis de sentimientos, modelado de temas (LDA), NER, incrustaciones de palabras (Word2Vec, BERT) | Extraer información del texto |
---

## Ética y gobernanza de datos
### Regulaciones de privacidad
| Reglamento | Alcance |
|-----------|-------|
| **RGPD** | interesados ​​de la UE; derecho de supresión, consentimiento, portabilidad de datos |
| **CCPA** | Consumidores de California; darse de baja de las ventas de datos |
| **HIPAA** | Datos sanitarios de EE. UU.; estrictas reglas de confidencialidad |
### Dimensiones de calidad de datos
| Dimensión | Pregunta |
|-----------|----------|
| **Precisión** | ¿Los datos son correctos? |
| **Integridad** | ¿Falta algo? |
| **Consistencia** | ¿Están de acuerdo las fuentes? |
| **Puntualidad** | ¿Es actual? |
| **Validez** | ¿Se ajusta a los formatos esperados? |
| **Singularidad** | ¿Hay duplicados? |
### Sesgo y equidad
El sesgo puede aparecer en cualquier etapa: sesgo de muestreo (datos no representativos), sesgo de medición (instrumentos defectuosos) o sesgo algorítmico (predicciones discriminatorias). Las estrategias de mitigación incluyen el preprocesamiento (arreglar los datos), el procesamiento interno (restringir el modelo) y el posprocesamiento (ajustar los resultados). Las métricas de equidad como la paridad demográfica y la igualdad de oportunidades ayudan a cuantificar el problema.
---

## Trayectorias profesionales
| Rol | Enfoque |
|------|-------|
| **Analista de datos** | Análisis descriptivos, paneles de control, informes |
| **Científico de datos** | Modelado estadístico, ML, análisis avanzado |
| **Ingeniero de aprendizaje automático** | Sistemas de producción de ML, implementación de modelos, MLOps |
| **Ingeniero de datos** | Canalizaciones de datos, infraestructura, ETL |
| **Gerente de Análisis** | Liderazgo de equipos, estrategia, gestión de stakeholders |
| **Investigador científico** | Nuevos algoritmos, publicaciones |
---

## Tendencias emergentes
- **AutoML**: creación automatizada de canalizaciones y selección de modelos.
- **MLOps**: Prácticas de DevOps aplicadas a la gestión del ciclo de vida de ML.
- **Tiendas de funciones**: gestión de funciones centralizada para su reutilización entre equipos.
- **Data Mesh**: arquitectura de datos descentralizada y propiedad del dominio.
- **LLM e IA generativa**: modelos de lenguaje grandes que transforman flujos de trabajo de texto, código e imágenes.
- **Edge Analytics**: procesamiento de datos en el dispositivo en lugar de en la nube.
- **Inferencia causal**: ir más allá de la correlación para comprender la causa y el efecto reales.
- **Aprendizaje federado**: modelos de entrenamiento a través de datos descentralizados sin moverlos.
- **IA responsable**: la ética, la explicabilidad y la transparencia se convierten en requisitos estándar.