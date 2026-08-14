---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
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
    changes: "Moved to architectures/ subfolder; added subcategory field"
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
tags: [recommendation, systems, ai-and-machine-learning]
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

# Sistemas de recomendación
Los sistemas de recomendación predicen lo que un usuario querrá ver, comprar o interactuar a continuación. Impulsan el contenido de las redes sociales, las sugerencias de productos en los sitios de comercio electrónico, las selecciones de películas en las plataformas de transmisión y los resultados de búsqueda. A pesar de ser invisibles para la mayoría de los usuarios, se encuentran entre los sistemas de inteligencia artificial de mayor impacto comercial del mundo: Netflix estima que su motor de recomendación ahorra más de mil millones de dólares al año al reducir la rotación de suscriptores.
---

## Por qué las recomendaciones son difíciles
| Desafío | Descripción |
|-----------|-------------|
| **Escala** | Millones de usuarios × millones de elementos = miles de millones de pares posibles |
| **Escasez** | Cada usuario ha interactuado con una pequeña fracción de los elementos disponibles |
| **Arranque en frío** | Los nuevos usuarios y los nuevos elementos no tienen historial de interacción |
| **Preferencias dinámicas** | Los gustos de los usuarios cambian con el tiempo |
| **Más allá de la precisión** | Las recomendaciones también deben ser diversas, novedosas y fortuitas |
| **Objetivos comerciales** | Maximizar el compromiso ≠ maximizar el bienestar del usuario |
---

## Enfoques básicos
### Filtrado colaborativo
La idea: si los usuarios A y B estuvieron de acuerdo en el pasado, probablemente estarán de acuerdo en el futuro.
| Tipo | Cómo funciona | Ejemplo |
|------|-------------|---------|
| **Basado en el usuario** | Encuentra usuarios similares; recomendar lo que les gustó | "A los usuarios a los que les gustó esto también les gustó..." |
| **Basado en artículos** | Encuentra artículos similares a los que ya le gustan al usuario | "Porque viste..." |
| **Factorización matricial** | Descomponer la matriz de interacción usuario-elemento en factores latentes | SVD, ALS (mínimos cuadrados alternos) |
| Fuerza | Debilidad |
|----------|----------|
| No es necesario comprender los elementos en sí | Problema de arranque en frío: no puedo recomendar artículos nuevos |
| Capta preferencias implícitas y complejas | Requiere muchos datos de interacción |
| Funciona en cualquier tipo de contenido | Sesgo de popularidad: recomienda artículos que ya son populares |
### Filtrado basado en contenido
Recomiende artículos similares a los que ya le gustan al usuario, según las características del artículo.
| Tipo de característica | Ejemplo |
|-------------|---------|
| **Texto** | Género, descripción, palabras clave, reparto |
| **Audio** | Tempo, género, estado de ánimo (para música) |
| **Visual** | Paleta de colores, estilo (para imágenes/moda) |
| **Metadatos** | Precio, marca, categoría |
| Fuerza | Debilidad |
|----------|----------|
| No hay arranque en frío para los artículos (se conocen las características) | No puedo recomendar artículos que no sean del gusto actual del usuario |
| Funciona con menos datos de interacción | Requiere una buena ingeniería de funciones |
| Explicable ("recomendado porque es similar a X") | Menos casualidad |
### Enfoques híbridos
La mayoría de los sistemas de producción combinan métodos colaborativos y basados ​​en contenidos.
| Estrategia híbrida | Descripción |
|----------|-------------|
| **Ponderado** | Combina puntuaciones de múltiples modelos |
| **Cambiar** | Utilice contenido para nuevos usuarios y colaborativo para los ya establecidos |
| **Cascada** | Utilice primero un modelo simple y luego refine con uno complejo |
| **Combinación de funciones** | Fusionar funciones colaborativas y de contenido en un solo modelo |
| **Metaaprendizaje** | Aprenda a combinar diferentes recomendadores |
---

## Enfoques modernos de aprendizaje profundo
### Modelos de dos torres
La arquitectura dominante para recomendaciones a gran escala (utilizada por YouTube, Pinterest, Spotify).
| Componente | Rol |
|-----------|--------------|
| **Torre de usuarios** | Red neuronal que codifica las características y el historial del usuario en una inserción |
| **Torre de artículos** | Red neuronal que codifica características de elementos en una incrustación |
| **Similitud** | Producto escalar o similitud de coseno entre incrustaciones de usuario y elemento |
| Paso | Descripción |
|------|-------------|
| 1 | Entrene ambas torres para producir incrustaciones similares para pares de usuarios-elementos que interactúan |
| 2 | En el momento de la publicación, calcule previamente las incrustaciones de elementos |
| 3 | Para una solicitud de usuario, calcule la incrustación de usuario |
| 4 | Utilice la búsqueda aproximada del vecino más cercano (ANN) para encontrar los elementos más similares |
### Modelos de secuencia para recomendaciones
El comportamiento del usuario es secuencial: lo que vio ayer influye en lo que verá hoy.
| Modelo | Enfoque |
|-------|----------|
| **GRU4Rec** | Modelo basado en GRU para recomendaciones basadas en sesiones |
| **SASRec** | Recomendador secuencial basado en autoatención |
| **BERT4Rec** | Transformador Bidireccional para recomendaciones secuenciales |
| **YouTube DNN** | Red neuronal profunda que trata el historial de reproducciones como una secuencia |
### Recuperación vs Clasificación
Los sistemas modernos dividen las recomendaciones en dos etapas:
| Etapa | Propósito | Método |
|-------|---------|--------|
| **Recuperación (generación de candidatos)** | Reducir millones de elementos a ~1000 candidatos | Modelo de dos torres; búsqueda de RNA; rápido pero aproximado |
| **Ranking (puntuación)** | Puntuar y ordenar con precisión a los candidatos | Modelo profundo con muchas características; más lento pero preciso |
| **Reclasificación** | Adaptarse a la diversidad, las reglas comerciales y la frescura | Bandidos contextuales; optimización de restricciones |
---

## Métricas de evaluación
| Métrica | Qué mide | Cuándo utilizar |
|--------|-----------------|-------------|
| **Precisión@K** | Fracción de recomendaciones top-K que son relevantes | Cuando te importa la precisión de las mejores selecciones |
| **Recordar@K** | Fracción de elementos relevantes encontrados en top-K | Cuando te preocupas por no perderte buenos artículos |
| **NDCG** (Ganancia acumulada descontada normalizada) | Calidad de clasificación; recompensas que suben los elementos relevantes | Cuando el orden de clasificación importa |
| **MAP** (Precisión media media) | Precisión media entre todos los usuarios | Calidad de la clasificación general |
| **Tasa de aciertos@K** | Si al menos un elemento relevante aparece en top-K | Escenarios de relevancia binaria |
| **Cobertura** | Fracción de artículos recomendados | Diversidad y equidad |
| **Serendipia** | Recomendaciones inesperadas pero relevantes | Satisfacción del usuario |
---

## El problema del arranque en frío
| Escenario | Desafío | Soluciones |
|----------|-----------|-----------|
| **Nuevo usuario** | Sin historial de interacción | Utilice datos demográficos; mostrar artículos populares; utilizar señales contextuales (ubicación, dispositivo, hora) |
| **Nuevo artículo** | Nadie ha interactuado con él todavía | Utilice funciones de contenido; estrategias de exploración-explotación; algoritmos bandidos |
| **Nuevo sistema** | Ningún dato | Transferir el aprendizaje de dominios similares; seleccionar contenido inicial |
---

## Exploración vs Explotación
| Estrategia | Descripción | Compensación |
|----------|-------------|-----------|
| **ε-codicioso** | Mostrar elementos aleatorios con probabilidad ε | Simple pero ineficiente |
| **Muestreo de Thompson** | Muestra de la distribución posterior de la calidad del artículo | De principios; buenas propiedades teóricas |
| **Límite superior de confianza (UCB)** | Prefiere elementos con alta incertidumbre | Buen equilibrio de exploración y explotación |
| **Bandidos contextuales** | Exploración condicionada al contexto del usuario | Más eficiente que la exploración a ciegas |
| **Inyección de diversidad** | Incluir deliberadamente elementos diversos o novedosos | Simple; puede reducir el compromiso a corto plazo |
---

## Sesgo y equidad
| Tipo de sesgo | Descripción | Impacto |
|-----------|-------------|--------|
| **Sesgo de popularidad** | Los artículos populares se recomiendan cada vez más y se vuelven más populares | Los artículos de cola larga están desatendidos |
| **Sesgo de selección** | Los modelos aprenden de las interacciones observadas, no de todas las posibles | Sesgado hacia usuarios activos |
| **Sesgo de posición** | Los elementos que se muestran en posiciones más altas obtienen más clics independientemente de la calidad | Refuerza primeras posiciones |
| **Sesgo de exposición** | Los elementos que se han mostrado reciben más señal de entrenamiento | Bucle de retroalimentación |
| **Sesgo demográfico** | Las recomendaciones difieren entre grupos demográficos de manera injusta | Discriminación; mala experiencia para algunos grupos |
### Estrategias de mitigación
| Estrategia | Descripción |
|----------|-------------|
| **Ponderación de propensión inversa** | Artículos populares para bajar de peso en el entrenamiento |
| **Capas de eliminación de sesgos** | Agregar un componente desestabilizador al modelo |
| **Restricciones de equidad** | Añadir restricciones para garantizar un trato equitativo |
| **Recomendaciones diversas** | Optimice explícitamente la diversidad junto con la relevancia |
| **Auditoría y seguimiento** | Verifique periódicamente las recomendaciones para detectar sesgos entre grupos |
---

## Ejemplos de la industria
| Empresa | Sistema | Enfoque |
|---------|--------|----------|
| **Netflix** | Recomendaciones de películas/TV | Recuperación de dos torres + clasificación profunda + bandidos contextuales para obras de arte |
| **YouTube** | Recomendaciones de vídeos | Red neuronal profunda para generación de candidatos; modelo de clasificación separado |
| **Spotify** | Recomendaciones musicales | Filtrado colaborativo + PNL en listas de reproducción + análisis de audio |
| **Amazonía** | Recomendaciones de productos | Filtrado colaborativo de elemento a elemento; personalizado a escala |
| **TikTok** | Vídeo breve | Aprendizaje por refuerzo; fuerte énfasis en la exploración |
| **Pinterest** | Recomendaciones visuales | Modelo de dos torres; similitud visual |
---

## Herramientas y marcos
| Herramienta | Propósito |
|------|---------|
| **Recomendadores de TensorFlow (TFRS)** | Modelos de dos torres, recuperación, clasificación |
| **PyTorch RecSys** | Modelos de recomendación orientados a la investigación |
| **Sorpresa** | Filtrado colaborativo clásico (SVD, NMF, KNN) |
| **Implícito** | Filtrado colaborativo rápido para comentarios implícitos (ALS, BPR) |
| **Faiss** (Meta) | Búsqueda aproximada del vecino más cercano a escala |
| **Milvus / Piña / Weaviate** | Bases de datos vectoriales para búsqueda de similitudes |
| **Recbol** | Biblioteca completa de investigación de recomendaciones |
| **Merlín** (NVIDIA) | Canal de recomendaciones acelerado por GPU |
---

## Resumen
Los sistemas de recomendación se encuentran entre las aplicaciones de IA de mayor impacto en la industria. El campo ha evolucionado desde un simple filtrado colaborativo hasta arquitecturas de aprendizaje profundo que combinan el historial del usuario, el contenido del elemento, las señales contextuales y los objetivos comerciales. Los sistemas modernos utilizan un proceso de recuperación, clasificación y reclasificación, con modelos de dos torres para una generación rápida de candidatos y modelos profundos para una puntuación precisa. Los desafíos (arranque en frío, sesgo, exploración y equilibrio de la satisfacción del usuario con los objetivos comerciales) siguen siendo áreas activas de investigación e ingeniería.