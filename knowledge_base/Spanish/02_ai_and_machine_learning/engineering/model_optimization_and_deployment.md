---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
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
tags: [model, optimization, deployment, ai-and-machine-learning]
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
# Optimización e implementación del modelo
Entrenar un modelo de IA de gran tamaño es un logro significativo, pero implementarlo de manera eficiente es donde se requiere la mayor parte del esfuerzo de ingeniería. Un modelo que tarda 10 segundos en responder o requiere ocho GPU A100 no es práctico para la mayoría de las aplicaciones del mundo real. La optimización de modelos es el proceso de hacer modelos más pequeños, más rápidos y más rentables, manteniendo al mismo tiempo una calidad aceptable. Este archivo cubre la cuantificación, la poda, la destilación y las herramientas prácticas para implementar modelos en producción.
---

## ¿Por qué optimizar?
| Preocupación | Impacto |
|---------|--------|
| **Latencia** | Los usuarios esperan respuestas en menos de 1 segundo; cada 100 ms adicionales pierde compromiso |
| **Costo** | La inferencia de GPU es costosa; un modelo de 70 mil millones cuesta ~0,05-0,15 dólares por 1 millón de tokens en hardware en la nube |
| **Memoria** | Un modelo 7B en FP32 necesita 28 GB de VRAM; la mayoría de las GPU de consumo tienen entre 8 y 24 GB |
| **Energía** | El funcionamiento de modelos grandes consume una cantidad significativa de electricidad; importantes para dispositivos móviles y de vanguardia |
| **Escala** | Servir a millones de usuarios requiere modelos que se ajusten al hardware disponible |
---

## Cuantización
La cuantificación reduce la precisión de los pesos del modelo desde punto flotante de 32 bits (FP32) a formatos más pequeños como INT8, INT4 o incluso inferiores.
### Formatos de precisión
| Formato | Bits por peso | Memoria para modelo 7B | Calidad |
|--------|----------------|--------------------|---------|
| **FP32** | 32 | 28GB | Línea de base (precisión total) |
| **FP16 / BF16** | 16 | 14 GB | Casi idéntico a FP32 |
| **INT8** | 8 | 7 GB | Pérdida de calidad muy pequeña |
| **INT4** | 4 | 3,5 GB | Pérdida moderada de calidad; todavía utilizable |
| **INT3/INT2** | 3-2 | 2,6-1,75 GB | Pérdida significativa de calidad; etapa de investigación |
### Métodos de cuantificación
| Método | Cuando sucede | Cómo funciona | Calidad |
|--------|----------------|--------------|---------|
| **Cuantificación post-entrenamiento (PTQ)** | Una vez finalizado el entrenamiento | Calibre el modelo en un pequeño conjunto de datos; encontrar escalas óptimas | Bueno para INT8; se degrada en INT4 |
| **GPTQ** | Después del entrenamiento | Cuantización INT4 compatible con GPU utilizando información aproximada de segundo orden | Buena calidad en INT4 |
| **AWQ** (Cuantificación de peso basada en la activación) | Después del entrenamiento | Proteger los pesos destacados en función de las magnitudes de activación | Mejor que GPTQ en INT4 |
| **GGUF** (formato llama.cpp) | Después del entrenamiento | Cuantización compatible con la CPU; precisión mixta por capa | Optimizado para inferencia de CPU |
| **Entrenamiento consciente de la cuantificación (QAT)** | Durante el entrenamiento | Simule la cuantificación durante el entrenamiento para que el modelo aprenda a afrontar la situación. La mejor calidad; requiere reentrenamiento |
### Impacto práctico
| Modelo | Tamaño FP16 | Tamaño INT4 | Aceleración | Pérdida de calidad |
|-------|-----------|-----------|---------|-------------|
| **LLAMA 7B** | 14 GB | 3,5 GB | 2-4x | ~1-2% en los puntos de referencia |
| **LLAMA 70B** | 140 GB | 35GB | 2-3x | ~2-3% en los puntos de referencia |
---

## Poda
La poda elimina pesos o neuronas innecesarios de un modelo entrenado.
| Tipo | Descripción | Ventaja | Desafío |
|------|-------------|-----------|-----------|
| **Sin estructura** | Eliminar pesos individuales (puestos a cero) | Relaciones de compresión más altas | Requiere soporte de hardware escaso |
| **Estructurado** | Eliminar neuronas enteras, cabezas de atención o capas | Reduce directamente el tamaño del modelo | Puede perder más calidad |
| **Basado en magnitud** | Eliminar pesos con valores absolutos más pequeños | Simple; funciona bien | Puede perder pequeños pesos importantes |
| **Basado en importancia** | Eliminar ponderaciones en función de su contribución a la producción | Conservación de mejor calidad | Más caro de calcular |
### Tubería de poda
| Paso | Descripción |
|------|-------------|
| 1. Tren | Entrene el modelo completo normalmente |
| 2. Puntuación | Calcular puntuaciones de importancia para cada peso/neurona |
| 3. Podar | Elimina los elementos menos importantes |
| 4. Afinar | Vuelva a entrenar para recuperar la precisión perdida |
| 5. Repetir | Iterar poda y ajuste para una mayor compresión |
---

## Destilación del conocimiento
Entrenar un pequeño modelo de "estudiante" para imitar un modelo grande de "maestro".
| Componente | Rol |
|-----------|--------------|
| **Profesor** | Modelo grande y de alta calidad |
| **Estudiante** | Pequeño modelo que aprende del profesor |
| **Pérdida por destilación** | El estudiante intenta igualar la distribución de producción del profesor (etiquetas suaves) |
### Tipos de destilación
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Basado en Logit** | Estudiante coincide con las probabilidades de salida del profesor | Destilación original de Hinton |
| **Basado en funciones** | Estudiante coincide con las representaciones intermedias del profesor | FitNets |
| **Basado en relaciones** | Estudiante relaciona relaciones entre muestras | RKD (Destilación del conocimiento relacional) |
| **Sin datos** | No se necesitan datos de entrenamiento originales; utilizar la generación del profesor | DAFL, inversión profunda |
### Ejemplos de destilación notables
| Profesor | Estudiante | Resultado |
|---------|---------|--------|
| **GPT-4** | GPT-3.5-turbo (se rumorea) | Modelo más pequeño con gran parte de la calidad del GPT-4 |
| **BERT-Grande** | DistilBERT | 40% más pequeño, 60% más rápido, 97% del rendimiento de BERT |
| **LLAMA 70B** | LLaMA 7B (vía destilación) | Modelo pequeño de código abierto que se acerca a la calidad de un modelo grande |
---

## Optimizaciones específicas de LLM
### Optimización de caché KV
Los modelos de lenguaje grandes almacenan en caché los pares clave-valor de tokens anteriores para evitar un nuevo cálculo.
| Técnica | Descripción | Impacto |
|-----------|-------------|--------|
| **Atención multiconsulta (MQA)** | Todos los cabezales de atención comparten un par KV | Reduce la memoria; ligera pérdida de calidad |
| **Atención de consultas agrupadas (GQA)** | Grupos de cabezas comparten pares KV | Equilibrio entre MQA y atención estándar |
| **Atención ventana corredera** | Solo atiende a los últimos tokens W | Reduce el tamaño de la caché KV para contextos largos |
### Decodificación especulativa
| Paso | Descripción |
|------|-------------|
| 1 | Un pequeño modelo "borrador" genera K tokens rápidamente |
| 2 | El modelo grande verifica todos los K tokens en un solo pase hacia adelante |
| 3 | Los tokens aceptados se conservan; los rechazados se regeneran |
Resultado: aceleración de generación entre 2 y 3 veces sin pérdida de calidad (el modelo grande siempre tiene la última palabra).
### Atención relámpago
| Característica | Descripción |
|---------|-------------|
| **Problema** | La atención estándar requiere memoria O(n²) para la matriz de atención |
| **Solución** | Calcular la atención en bloques; nunca materializar la matriz completa en la memoria |
| **Resultado** | 2-4 veces más rápido; permite ventanas de contexto mucho más largas |
| **Variantes** | Flash Attention 2 (más rápido), FlashDecoding (optimizado para inferencia) |
---

## Marcos de servicio
| Marco | Mejor para | Característica clave |
|-----------|----------|-------------|
| **vLLM** | Servicio de LLM | Atención paginada; procesamiento por lotes continuo; alto rendimiento |
| **TensorRT-LLM** | Inferencia de GPU NVIDIA | Máximo rendimiento en hardware NVIDIA |
| **llama.cpp** | Inferencia de CPU y GPU de consumo | Ejecuta modelos cuantificados en portátiles y teléfonos |
| **Ollama** | Modelo local en ejecución | Envoltorio fácil de usar para llama.cpp |
| **Servidor de inferencia Triton** | Servicio multimarco | Admite TensorFlow, PyTorch, ONNX, TensorRT |
| **Servicio de antorcha** | Servicio de modelo PyTorch | Integración nativa de PyTorch |
| **Tiempo de ejecución ONNX** | Inferencia multiplataforma | Ejecución optimizada en todo el hardware |
| **BentoML** | Despliegue de producción | Agnóstico del marco; se encarga de envasar y servir |
---

## Patrones de implementación
| Patrón | Descripción | Cuándo utilizar |
|---------|-------------|-------------|
| **Implementación perimetral** | Ejecute modelos en teléfonos, dispositivos IoT o hardware integrado | Baja latencia; desconectado; privacidad |
| **API en la nube** | Alojar modelos en GPU en la nube; servir a través de API | Computación máxima; pago por uso |
| **Híbrido** | Modelo pequeño en dispositivo; modelo grande en la nube | Lo mejor de ambos mundos |
| **Sin servidor** | Escalar a cero; paga solo cuando se usa | Tráfico esporádico; sensible a los costos |
| **Inferencia por lotes** | Procesar datos de forma masiva según un cronograma | Cuando no se necesita tiempo real |
---

## Evaluación comparativa
| Métrica | Qué mide |
|--------|-----------------|
| **Tokens por segundo** | Rendimiento de generación (cuanto más alto, mejor) |
| **Tiempo hasta el primer token (TTFT)** | Latencia antes de que aparezca el primer token de salida |
| **Latencia por solicitud** | Tiempo total desde la entrada hasta la salida completa |
| **Uso de memoria** | VRAM o RAM consumida durante la inferencia |
| **Rendimiento** | Solicitudes atendidas por segundo |
| **Costo por 1 millón de tokens** | Costo en dólares de procesar 1 millón de tokens |
---

## Consejos prácticos
- **Comience con la cuantificación.** La cuantificación INT4 (AWQ o GPTQ) ofrece la mejor relación calidad-tamaño. La mayoría de los modelos 7B funcionan cómodamente en una única GPU de consumo en INT4.
- **Utilice vLLM para la prestación de LLM.** Es la opción de código abierto más rápida para la inferencia de LLM de alto rendimiento.
- **Perfil antes de optimizar.** Mide dónde se invierte realmente el tiempo. A menudo es el ancho de banda de la memoria, no la computación, el cuello de botella.
- **Haga coincidir el modelo con la tarea.** Un modelo 7B está bien para la mayoría de las tareas. No uses 70B cuando 7B sea suficiente.
- **Considere la destilación.** Si necesita un modelo pequeño y rápido para la producción, destile a partir de un modelo más grande en lugar de entrenar desde cero.
- **Monitorear continuamente.** El rendimiento del modelo puede degradarse con el tiempo a medida que cambian las distribuciones de datos. Realice un seguimiento de las métricas de latencia, rendimiento y calidad.
---

## Resumen
La optimización del modelo es el puente entre la investigación y la producción. La cuantización reduce los modelos entre 4 y 8 veces con una pérdida de calidad mínima. La poda elimina el peso muerto. La destilación transfiere conocimientos de modelos grandes a pequeños. Los trucos de Flash Attention y KV-cache hacen que la inferencia sea más rápida. Juntas, estas técnicas convierten un modelo que requiere un centro de datos en uno que se ejecuta en una computadora portátil o un teléfono. El campo avanza rápidamente: lo que requirió ocho A100 el año pasado se ejecuta hoy en una GPU de consumo.