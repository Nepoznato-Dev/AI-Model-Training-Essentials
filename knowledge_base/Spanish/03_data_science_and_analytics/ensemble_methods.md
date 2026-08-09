---
# Metadatos
título: "Métodos de conjunto"
descripción: "Embolsado, impulso, apilamiento, votación, bosques aleatorios, XGBoost"
categoría: "Ciencia y análisis de datos"
versión: "1.0.0"
estado: "activo"
# Contribución
autores:
  - nombre: "Equipo de formación del modelo de IA"
    correo electrónico: ""
    rol: "autor_original"
colaboradores: []
registro de cambios:
  - versión: "1.0.0"
    fecha: "2026-08-05"
    autor: "Equipo de formación del modelo de IA"
    cambios: "Se agregaron metadatos de temas frontales de YAML para el seguimiento de los contribuyentes"
# Revisión
creado: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
review_by: "Equipo de la base de conocimientos de análisis y ciencia de datos"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [conjunto, métodos, ciencia-y-análisis-de-datos]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "7 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Métodos de conjunto
Los métodos conjuntos combinan múltiples modelos de aprendizaje automático para producir mejores predicciones que las que cualquier modelo podría lograr por sí solo. La intuición es sencilla: si tiene varios modelos, cada uno de los cuales es algo preciso pero comete errores diferentes, la combinación de sus predicciones anulará los errores individuales y producirá un resultado más sólido. Los conjuntos están detrás de la mayoría de las soluciones de aprendizaje automático competitivas y siguen siendo algunas de las técnicas más confiables en los sistemas de producción.
---

## Por qué funcionan los conjuntos
| Principio | Descripción |
|-----------|-------------|
| **Sabiduría de las multitudes** | Múltiples estimaciones imperfectas, promediadas, son mejores que cualquier estimación única |
| **Compensación entre sesgo y varianza** | Los conjuntos pueden reducir la variación (ensacado) o el sesgo (impulso) sin sacrificar al otro |
| **Diversidad de errores** | Si los modelos cometen diferentes errores, combinarlos anula los errores individuales |
| **Suavizado de límites de decisión** | Varios modelos crean una superficie de decisión más sólida que un solo modelo |
---

## Embolsado (agregación Bootstrap)
### Cómo funciona
| Paso | Descripción |
|------|-------------|
| **1. Muestreo de arranque** | Extraer múltiples muestras aleatorias (con reemplazo) de los datos de entrenamiento |
| **2. Modelos de base de tren** | Entrene un modelo en cada muestra de arranque (normalmente árboles de decisión) |
| **3. Agregado** | Para regresión: predicciones promedio. Para clasificación: voto mayoritario |
### Características clave
| Característica | Descripción |
|---------------|-------------|
| **Reduce la variación** | El promedio suaviza las fluctuaciones de los modelos individuales |
| **Entrenamiento paralelo** | Cada modelo base es independiente; se puede entrenar simultáneamente |
| **Evaluación fuera de bolsa** | Cada muestra queda fuera de algunas muestras de arranque; utilizarlos para la validación |
| **Decorrelación** | La selección aleatoria de características en cada división reduce la correlación entre árboles |
### Bosque aleatorio
| Aspecto | Descripción |
|--------|-------------|
| **Alumno base** | Árboles de decisión |
| **Adición de clave** | En cada división, considere solo un subconjunto aleatorio de características (normalmente sqrt(n_features)) |
| **Por qué funciona** | La selección aleatoria de características descorrela los árboles, haciendo que el conjunto sea más robusto |
| **Hiperparámetros** | Número de árboles; profundidad máxima; muestras mínimas por hoja; características máximas |
| **Fortalezas** | Maneja datos de alta dimensión; robusto a los valores atípicos; proporciona importancia a la característica |
| **Debilidades** | Menos interpretable que árboles individuales; puede sobreadaptarse en tareas de regresión ruidosas |
---

## Impulsando
### Cómo funciona
| Paso | Descripción |
|------|-------------|
| **1. Tren primer modelo** | Entrene un modelo base (a menudo un árbol/"tocón" poco profundo) con los datos |
| **2. Identificar errores** | Encuentre en qué casos el modelo se equivocó |
| **3. Tren siguiente modelo** | Entrenar un nuevo modelo centrado en los errores (reponderado o ajustado residual) |
| **4. Combinar secuencialmente** | Cada nuevo modelo corrige los errores acumulados de todos los modelos anteriores |
| **5. Repetir** | Continuar durante un número específico de rondas |
### Algoritmos de impulso
| Algoritmo | Función de pérdida | Característica clave |
|-----------|--------------|-------------|
| **AdaBoost** | Exponencial | Se vuelven a ponderar las instancias mal clasificadas; simple; sensible al ruido |
| **Impulso de gradiente** | Cualquier pérdida diferenciable | Se ajusta a residuos (gradiente de pérdida); más flexibles |
| **XGBoost** | Aumento de gradiente regularizado | regularización L1/L2; gradientes de segundo orden; optimización de hardware |
| **LightGBM** | Muestreo unilateral basado en gradientes | Crecimiento foliar; basado en histograma; rápido en grandes conjuntos de datos |
| **CatBoost** | Impulso ordenado | Maneja características categóricas de forma nativa; reduce el sobreajuste |
### Impulsar versus embolsar
| Dimensión | Ensacado | Impulsando |
|-----------|---------|----------|
| **Entrenamiento** | Paralelo | Secuencial |
| **Enfoque** | Reduce la variación | Reduce el sesgo |
| **Modelos básicos** | Alta variación, bajo sesgo (árboles profundos) | Baja variación, alto sesgo (árboles poco profundos/tocones) |
| **Combinación** | Peso igual | Ponderado por rendimiento |
| **Sobreajuste** | Menos propenso | Puede sobreajustarse si hay demasiadas rondas |
| **Sensibilidad al ruido** | Robusto | Sensible a datos ruidosos |
---

## Apilamiento
### Cómo funciona
| Paso | Descripción |
|------|-------------|
| **1. Modelos de base de tren** | Entrene diversos modelos (por ejemplo, bosque aleatorio, SVM, red neuronal, aumento de gradiente) |
| **2. Generar predicciones** | Utilice predicciones fuera de pliegue (validación cruzada) como funciones de entrada |
| **3. Metamodelo de tren** | Entrenar un modelo de segundo nivel sobre las predicciones de los modelos base |
| **4. Predicción final** | Los modelos base predicen; metamodelo combina sus predicciones |
### Apilamiento de mejores prácticas
| Práctica | Razón |
|----------|--------|
| **Utilice diversos modelos base** | Diferentes algoritmos cometen errores diferentes; la diversidad es el punto |
| **Utilice validación cruzada para predicciones base** | Impide que el metamodelo aprenda a explotar los modelos base sobreajustados |
| **Mantenga el metamodelo simple** | Regresión logística o árbol poco profundo; los modelos básicos hacen el trabajo pesado |
| **Incluir características sin procesar en el metamodelo** | A veces también es útil darle al metamodelo acceso a las funciones originales |
---

## Votación y promedio
### Voto duro (clasificación)
| Modelo | Predicción |
|-------|-----------|
| Modelo A | Clase 1 |
| Modelo B | Clase 0 |
| Modelo C | Clase 1 |
| **Voto mayoritario** | **Clase 1** |
### Voto Blando (Clasificación)
| Modelo | P(Clase 0) | P(Clase 1) |
|-------|-----------|-----------|
| Modelo A | 0,3 | 0,7 |
| Modelo B | 0,6 | 0,4 |
| Modelo C | 0,4 | 0,6 |
| **Promedio** | **0,43** | **0,57** |
| **Predicción** | | **Clase 1** |
### Promedio ponderado
| Modelo | Peso | Predicción |
|-------|--------|-----------|
| Modelo A | 0,5 | 0,8 |
| Modelo B | 0,3 | 0,6 |
| Modelo C | 0,2 | 0,9 |
| **Promedio ponderado** | | 0,5×0,8 + 0,3×0,6 + 0,2×0,9 = 0,76 |
---

## Orientación práctica
### Cuándo usar qué conjunto
| Escenario | Método recomendado |
|----------|-------------------|
| **Línea de base rápida; datos tabulares** | Bosque aleatorio |
| **Precisión máxima; datos tabulares** | XGBoost/LightGBM/CatBoost |
| **Datos ruidosos** | Embolsado (el refuerzo sobrepasará el ruido) |
| **Se necesita interpretabilidad** | Modelo único o conjunto pequeño con características importantes |
| **Diversos tipos de modelos** | Apilar o votar |
| **Aprendizaje en línea** | Métodos de transmisión en conjunto; impulso adaptativo |
| **Datos desequilibrados** | Bosque aleatorio equilibrado; impulso sensible a los costos |
### Estrategias de diversidad conjunta
| Estrategia | Descripción |
|----------|-------------|
| **Diferentes algoritmos** | Combine modelos basados ​​en árboles, lineales y neuronales |
| **Diferentes características** | Entrenar modelos en diferentes subconjuntos de características |
| **Diferentes subconjuntos de datos** | Harpillera; submuestreo |
| **Diferentes hiperparámetros** | Mismo algoritmo con configuraciones variadas |
| **Diferentes períodos de tiempo** | Entrene en diferentes ventanas de tiempo |
---

## Resumen
Los métodos de conjunto funcionan porque combinan múltiples modelos imperfectos en un único predictor robusto. El embolsado (bosques aleatorios) reduce la varianza entrenando modelos en paralelo con muestras de arranque y promediando. Boosting (XGBoost, LightGBM, CatBoost) reduce el sesgo al entrenar modelos secuencialmente, cada uno corrigiendo los errores anteriores. El apilamiento utiliza un metamodelo para combinar diversos modelos base. La votación y el promedio son los conjuntos más simples. El hilo conductor es la diversidad: los conjuntos funcionan mejor cuando los modelos que los componen son individualmente razonables pero cometen errores diferentes. En la práctica, el aumento de gradiente en datos tabulares suele ser el enfoque único de mayor rendimiento, mientras que la acumulación de diversos modelos aumenta aún más la precisión en competiciones y aplicaciones de alto riesgo.