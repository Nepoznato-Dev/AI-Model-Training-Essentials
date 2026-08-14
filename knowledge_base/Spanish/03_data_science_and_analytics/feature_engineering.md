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
# Ingeniería de funciones
La ingeniería de características es el proceso de transformar datos sin procesar en representaciones que hacen que los modelos de aprendizaje automático sean más efectivos. A menudo se describe como el paso más importante en el proceso de aprendizaje automático: las características que le brinda a un modelo importan más que el algoritmo que elija. Un modelo simple con características bien diseñadas normalmente superará a un modelo complejo con entradas sin procesar y sin procesar. El arte radica en comprender tanto el dominio como los datos lo suficientemente bien como para crear señales de las que el modelo pueda aprender.
---

## Por qué es importante la ingeniería de funciones
| factor | Impacto |
|--------|--------|
| **Calidad de la señal** | Mejores características = patrones más claros para que el modelo los aprenda |
| **Simplicidad del modelo** | Las buenas características permiten que los modelos más simples funcionen bien; menos necesidad de arquitecturas complejas |
| **Velocidad de entrenamiento** | Las características relevantes y bien escaladas convergen más rápido |
| **Generalización** | Las funciones basadas en el dominio ayudan a los modelos a trabajar con datos invisibles |
| **Interpretabilidad** | Las características significativas son más fáciles de explicar a las partes interesadas |
---

## Tipos de transformaciones de funciones
### Transformaciones numéricas
| Transformación | Fórmula / Descripción | Cuándo utilizar |
|---------------|----------------------|-------------|
| **Transformación de registro** | iniciar sesión(x) o iniciar sesión(x + 1) | Distribuciones sesgadas a la derecha; valores monetarios |
| **Raíz cuadrada** | raíz cuadrada (x) | Sesgo moderado; contar datos |
| **Caja-Cox** | Transformación paramétrica que encuentra la mejor transformación de potencia | Hacer que los datos se distribuyan de forma más normal |
| **Yeo-Johnson** | Como Box-Cox pero maneja valores negativos | Datos sesgados con valores negativos |
| **Estandarización** | (x - media) / estándar | Funciones con diferentes escalas; algoritmos asumiendo normalidad |
| **Escalado mínimo-máximo** | (x - mín) / (máx - mín) | Funciones delimitadoras a [0, 1]; valores de píxeles de la imagen |
| **Escalado robusto** | (x - mediana) / RIQ | Datos con valores atípicos |
| **Agrupación** | Convertir continuo a categórico | Relaciones no lineales; árboles de decisión |
| **Características polinómicas** | x², x³, x₁×x₂ | Capturar relaciones no lineales en modelos lineales |
### Codificaciones categóricas
| Codificación | Descripción | Cuándo utilizar |
|----------|-------------|-------------|
| **Codificación one-hot** | Crea una columna binaria para cada categoría | Categorías de baja cardinalidad; los modelos basados ​​en árboles se manejan de forma nativa |
| **Codificación de etiquetas** | Asignar un número entero a cada categoría | Categorías ordinales; modelos basados ​​en árboles |
| **Codificación de destino** | Reemplace categoría con media de variable objetivo | Categorías de alta cardinalidad; evitar el sobreajuste con suavizado |
| **Codificación de frecuencia** | Reemplazar categoría con su recuento o frecuencia | Cuando la frecuencia en sí es informativa |
| **Codificación binaria** | Convertir categorías codificadas en números enteros a dígitos binarios | Alta cardinalidad; reduce la dimensionalidad frente a one-hot |
| **Incrustar** | Aprenda la representación de vectores densos | Cardinalidad muy alta; PNL; sistemas de recomendación |
| **Codificación hash** | Categorías hash para un número fijo de funciones | Cardinalidad muy alta; aprendizaje en línea |
### Funciones de fecha y hora
| Característica | Descripción |
|---------|-------------|
| **Hora del día** | Capta patrones diarios (hora punta, noche) |
| **Día de la semana** | Efectos entre semana y fin de semana |
| **Mes/trimestre** | Patrones estacionales |
| **Es fin de semana** | Bandera binaria para el fin de semana |
| **Es feriado** | Bandera binaria para días festivos |
| **Tiempo desde el evento** | Días desde la última compra; horas desde el último inicio de sesión |
| **Codificación cíclica** | sin(2π × hora / 24), cos(2π × hora / 24) — preserva la naturaleza circular del tiempo |
---

## Manejo de valores faltantes
| Estrategia | Descripción | Cuándo utilizar |
|----------|-------------|-------------|
| **Eliminar filas** | Eliminar filas con valores faltantes | Los datos que faltan son una pequeña fracción; MCAR (falta completamente al azar) |
| **Eliminar columnas** | Eliminar funciones con demasiados valores faltantes | La característica prácticamente falta; no importante |
| **Imputación media/mediana** | Complete con la media o mediana de la característica | Simple; conserva la media pero reduce la varianza |
| **Imputación de modo** | Complete categórico con el valor más frecuente | Características categóricas |
| **Imputación KNN** | Utilice k vecinos más cercanos para estimar el valor faltante | Cuando instancias similares ayudan a predecir el valor faltante |
| **Imputación basada en modelos** | Entrenar un modelo para predecir valores faltantes | Más preciso; computacionalmente caro |
| **Falta indicador** | Agregue una columna binaria que marque la falta | Cuando la propia ausencia es informativa |
| **Interpolación** | Rellenar con valores interpolados (lineal, spline) | Series de tiempo; datos ordenados |
---

## Selección de funciones
### Métodos de filtrado
| Método | Descripción |
|--------|-------------|
| **Correlación** | Eliminar características altamente correlacionadas entre sí |
| **Umbral de variación** | Eliminar funciones con variación cercana a cero |
| **Información mutua** | Mida la información que cada característica proporciona sobre el objetivo |
| **Chi cuadrado** | Prueba de independencia entre características categóricas y objetivo |
| **Prueba ANOVA F** | Pruebe si las medias de las características numéricas difieren entre las clases de destino |
### Métodos de envoltura
| Método | Descripción |
|--------|-------------|
| **Selección hacia adelante** | Empiece vacío; agregue la mejor característica una a la vez |
| **Eliminación hacia atrás** | Comience con todos; eliminar la peor característica una a la vez |
| **Eliminación de funciones recursivas (RFE)** | Entrenar repetidamente el modelo; eliminar las características menos importantes |
### Métodos integrados
| Método | Descripción |
|--------|-------------|
| **Regularización L1 (Lasso)** | Reduce los pesos de características irrelevantes a cero |
| **Importancia basada en árboles** | Utilice la importancia de las características de los modelos de árbol |
| **Valores SHAP** | Mida la contribución de cada característica a las predicciones |
---

## Ingeniería de funciones específicas del dominio
### Funciones de texto
| Característica | Descripción |
|---------|-------------|
| **TF-IDF** | Frecuencia de términos ponderada por la frecuencia inversa de los documentos |
| **Incrustaciones de palabras** | Vectores densos que capturan significado semántico (Word2Vec, GloVe) |
| **N-gramas de caracteres** | Capture patrones de subpalabras; útil para errores tipográficos y morfología |
| **Estadísticas de texto** | Longitud; recuento de palabras; recuento de sentencias; longitud media de palabra |
| **Puntuaciones de legibilidad** | Flesch-Kincaid; Índice de niebla disparada |
### Funciones de series temporales
| Característica | Descripción |
|---------|-------------|
| **Funciones de retraso** | Valores anteriores: y(t-1), y(t-7), y(t-30) |
| **Estadísticas móviles** | Media, estándar, mínima, máxima en una ventana |
| **Diferencia** | y(t) - y(t-1); captura tendencia |
| **Diferencia estacional** | y(t) - y(t-12) para datos mensuales con estacionalidad anual |
| **Términos de Fourier** | Términos de seno y coseno para patrones estacionales |
### Funciones de imagen (pre-aprendizaje profundo)
| Característica | Descripción |
|---------|-------------|
| **HOG** (Histograma de gradientes orientados) | Distribución de direcciones de los bordes |
| **LBP** (Patrones binarios locales) | Descripción de la textura |
| **SIFT** (Transformación de características invariantes de escala) | Descriptores de puntos clave |
| **Histogramas de color** | Distribución de colores en la imagen |
---

## Mejores prácticas de ingeniería de funciones
| Práctica | Descripción |
|----------|-------------|
| **Evitar la fuga de datos** | Nunca utilice información del futuro o del conjunto de prueba para crear funciones |
| **Documente todo** | Registre qué transformaciones se aplicaron y por qué |
| **Versiona tus características** | Realice un seguimiento de los cambios de funciones junto con los cambios de modelo |
| **Validar con y sin** | Pruebe si una nueva característica realmente mejora el rendimiento del modelo |
| **Mantenlo reproducible** | Los procesos de ingeniería de características deben ser deterministas y repetibles |
| **Supervisar la deriva de funciones** | Las distribuciones de funciones pueden cambiar con el tiempo; supervisar y reciclar |
---

## Resumen
La ingeniería de funciones es donde el conocimiento del dominio se encuentra con el aprendizaje automático. Es el proceso de transformar datos sin procesar (desordenados, incompletos, de alta dimensión) en representaciones limpias e informativas de las que los modelos pueden aprender. Las transformaciones numéricas manejan la inclinación y la escala. Las codificaciones categóricas convierten etiquetas en números que los modelos pueden usar. Las características de fecha capturan patrones temporales. Las estrategias de valor perdido manejan datos incompletos. La selección de funciones elimina el ruido y la redundancia. Los mejores ingenieros de funciones piensan como detectives: preguntan qué señales deberían estar presentes en los datos, dónde podrían estar ocultas esas señales y cómo extraerlas de una manera que sea honesta (sin fuga de datos), reproducible y robusta para cambiar con el tiempo.