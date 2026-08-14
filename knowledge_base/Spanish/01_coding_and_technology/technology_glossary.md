<!--
---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Glosario de tecnología
Un glosario de referencia que cubre modelos de IA, hardware, puntos de referencia y conceptos básicos.
en el panorama moderno de la IA y la informática.
---

## Asistentes y modelos de lenguaje de IA
### ChatGPT
ChatGPT es un chatbot de IA desarrollado por OpenAI, lanzado por primera vez en noviembre de 2022.
Está impulsado por la serie GPT de modelos de lenguajes grandes (LLM). ChatGPT es uno
de los productos de IA de consumo de más rápido crecimiento en la historia, alcanzando los 100 millones
usuarios dentro de los dos meses posteriores al lanzamiento. Admite conversación basada en texto, código
generación, resumen y escritura creativa. Los niveles pagos brindan acceso a
Modelos más potentes como GPT-4 y GPT-4o.
### GPT (Transformador generativo preentrenado)
GPT es una familia de grandes modelos de lenguaje creados por OpenAI. la arquitectura
utiliza un transformador solo decodificador entrenado con un objetivo de predicción del siguiente token en
corpus de texto masivos. Las versiones clave incluyen GPT-2 (2019, 1.5B de parámetros, notable
para publicidad "demasiado peligrosa para publicar"), GPT-3 (2020, parámetros 175B, ampliamente
utilizado a través de la API), GPT-3.5 (la columna vertebral del ChatGPT original) y GPT-4
(2023, multimodal, desempeño cercano al nivel de experto humano en muchos puntos de referencia).
### Claudio
Claude es un asistente de inteligencia artificial desarrollado por Anthropic. Lleva el nombre de Claude.
Shannon, el fundador de la teoría de la información. Anthropic fue fundada por el ex
Investigadores de OpenAI y se centra en la "IA constitucional", una técnica para hacer
modelos más seguros entrenándolos para que sigan un conjunto de principios. modelos claude
(Claude 1, 2, 3 Haiku / Sonnet / Opus) son conocidos por ventanas de contexto largas (hasta
a 200.000 tokens), razonamiento matizado y producción dañina reducida en comparación con
LLM de referencia.
### Géminis
Gemini es la familia de modelos de IA multimodal de Google DeepMind, anunciada en
Diciembre de 2023. Gemini es nativamente multimodal: está entrenado desde cero en
texto, imágenes, audio y video simultáneamente, a diferencia de los modelos anteriores que tenían
Modalidades añadidas mediante ajustes. Las versiones incluyen Gemini Nano (en el dispositivo),
Gemini Flash (rápido, rentable) y Gemini Ultra (máxima capacidad).
Gemini impulsa el chatbot de IA de Google, Bard (rebautizado como Gemini) y la IA de búsqueda de Google
Resúmenes.
### Phi-3-mini
Phi-3-mini es un modelo de lenguaje pequeño (SLM) desarrollado por Microsoft con 3.8B
parámetros. Fue lanzado en abril de 2024. A diferencia de la mayoría de los modelos grandes, Phi-3-mini
fue capacitado en un conjunto de datos cuidadosamente seleccionado con "calidad de libro de texto", una técnica
iniciado por Microsoft Research, que prioriza la calidad de los datos sobre el volumen sin procesar.
A pesar de ser mucho más pequeño que GPT-4 o Claude 3 Opus, los fósforos Phi-3-mini o
supera a los modelos varias veces más grandes en puntos de referencia de razonamiento como MMLU y
Evaluación Humana. Admite una ventana de contexto de token de 4k en su variante base y una de 128k
ventana en la variante de contexto largo. Phi-3-mini puede ejecutarse en una única GPU de consumo
o incluso en el dispositivo de un teléfono inteligente moderno con suficiente RAM.
### Llama (Meta IA)
Llama (Large Language Model Meta AI) es una familia de modelos de peso abierto
publicado por Meta. Llama 2 (2023) fue lanzado para investigación y uso comercial
con tamaños que van desde 7B a 70B parámetros. Llama 3 (2024) mejorada
rendimiento significativamente, con modelos que van desde 8B a 70B (y posteriormente 400B+).
Debido a que los pesos se pueden descargar públicamente, los modelos Llama son la base
para un gran ecosistema de variantes afinadas (Mistral, Alpaca, Vicuña, etc.)
y se utilizan ampliamente para implementaciones de IA locales/privadas.
###Mistral
Mistral AI es una empresa francesa de inteligencia artificial que desarrolla LLM abiertos y propietarios.
Mistral 7B (2023) demostró que un modelo de parámetros 7B puede igualar el
rendimiento de modelos mucho más grandes utilizando técnicas eficientes como el deslizamiento
atención de ventana y atención de consultas agrupadas. Mixtral 8x7B (2023) es una mezcla-
modelo de expertos: enruta cada token a un subconjunto de 8 redes de expertos,
logrando un rendimiento de nivel GPT-3.5 y siendo computacionalmente más barato.
Los modelos de Mistral son totalmente abiertos y pueden funcionar localmente.
---

## Hardware GPU y tarjetas gráficas
### GPU (Unidad de procesamiento de gráficos)
Una GPU es un procesador diseñado para computación masivamente paralela. Originalmente
Creadas para renderizar gráficos 3D, las GPU se han vuelto esenciales para el entrenamiento de IA/ML
e inferencia porque pueden realizar miles de operaciones de punto flotante
utilizando simultáneamente miles de pequeños núcleos. Los dos principales fabricantes de GPU
para IA son NVIDIA y AMD.
### Serie NVIDIA GeForce RTX
La serie RTX (Ray Tracing Texel eXtreme) es la línea de GPU para consumidores de NVIDIA. RTX
Las generaciones 30xx (Ampere, 2020) y RTX 40xx (Ada Lovelace, 2022) incluyen
Tensor Cores dedicados para acelerar las operaciones de IA. VRAM (RAM de vídeo) es
fundamental para ejecutar modelos de IA localmente: una GPU de 8 GB puede manejar parámetros de 7 B
modelos en cuantificación de 4 bits; una GPU de 24 GB puede manejar modelos de 70 B en 4 bits.
### NVIDIA Serie A y Serie H (Centro de datos)
El A100 (Ampere, 2020) y el H100 (Hopper, 2022) son la IA profesional de NVIDIA
aceleradores. Un H100 tiene hasta 80 GB de memoria HBM3 y es el estándar
hardware detrás de la mayoría de la formación LLM a gran escala en la actualidad. Estas GPU cuestan 25.000 dólares.
$ 40,000 cada una, pero ofrecen entre 10 y 30 veces el rendimiento de IA de las tarjetas RTX de consumo.
### Serie AMD Radeon RX
Línea de GPU de consumo de AMD. La RX 7900 XTX (2022) tiene 24 GB de VRAM y puede ejecutar
LLM locales a través de ROCm (pila de computación GPU de AMD). Las GPU AMD son generalmente menos
tiene mejor soporte que NVIDIA para marcos de IA, aunque el soporte está mejorando.
### Arco Intel
Intel Arc es la línea de productos de GPU discreta de Intel, lanzada a partir de 2022. Arc
Las GPU son compatibles con XeSS (el supermuestreo de Intel) y tienen un soporte limitado pero creciente
para tareas de inferencia de IA a través de los marcos OpenVINO e IPEX-LLM.
### ARK Intel (ark.intel.com)
ARK es la base de datos oficial de especificaciones de productos de Intel en ark.intel.com. eso
proporciona especificaciones técnicas detalladas para cada CPU, GPU, FPGA y
Producto NUC, que incluye recuentos de núcleos, velocidades de reloj, TDP, tipos de memoria admitidos,
y características del conjunto de instrucciones. Cuando escuche "verifique las especificaciones de ARK", significa
visitar esa base de datos para obtener información autorizada sobre el hardware.
---

## Puntos de referencia de rendimiento de la IA
### MMLU (Comprensión masiva del lenguaje multitarea)
MMLU es un punto de referencia que evalúa el conocimiento de LLM en 57 materias académicas que incluyen
matemáticas, historia, derecho, medicina e informática. Consiste en
Preguntas de opción múltiple extraídas de exámenes reales de nivel universitario. una puntuación de
El 70% es aproximadamente un nivel universitario humano; GPT-4 y Claude 3 obtienen una puntuación superior al 86%.
Phi-3-mini obtiene una puntuación de alrededor del 70% a pesar de su pequeño tamaño.
### Evaluación Humana
HumanEval es el punto de referencia de OpenAI para la generación de código. Consta de 164 Python.
Problemas de programación con casos de prueba automatizados. Los modelos se miden en
pass@k: la probabilidad de que al menos una de las k soluciones generadas pase todas
pruebas. Puntuaciones de GPT-4 ~87% (aprobado@1); un modelo 7B bien ajustado puede alcanzar entre el 50% y el 60%.
### HellaSwag
HellaSwag es un punto de referencia de razonamiento de sentido común. A los modelos se les da una oración.
describir una actividad mundana y debe elegir la continuación más probable de
cuatro opciones. Las opciones incorrectas están especialmente diseñadas para ser plausibles, pero
sutilmente equivocado. Prueba si un modelo tiene una comprensión fundamentada de la física.
y situaciones sociales.
### ARC (Desafío de razonamiento AI2)
ARC es un referente del Instituto Allen de IA. Consta de escuela primaria
Preguntas científicas, divididas en conjuntos "fáciles" y "desafíos". El desafío establecido
contiene preguntas que métodos basados en la recuperación y modelos estadísticos simples
luchan, lo que requiere un razonamiento de varios pasos.
---

## Conceptos básicos de IA/ML
### RAG (Generación aumentada de recuperación)
RAG es una técnica que combina un sistema de recuperación (normalmente un vector
base de datos) con un modelo de lenguaje. En lugar de confiar únicamente en el modelo
conocimiento paramétrico, RAG primero recupera los documentos relevantes de un externo
base de conocimientos y luego los incluye en el contexto del modelo. Esto permite que el
modelo para responder preguntas sobre información actualizada o específica del dominio
sin reentrenamiento. Potato.ai utiliza una forma de RAG: se recupera de su KB
e incluye los resultados en el contexto antes de generar una respuesta.
### Ajuste fino
El ajuste es el proceso de continuar entrenando un modelo previamente entrenado en un
conjunto de datos más pequeño y específico de un dominio. Esto adapta los pesos del modelo para un
tarea o dominio particular. Por ejemplo, un LLM base podría ajustarse en
registros médicos para crear un asistente médico de preguntas y respuestas. El ajuste fino es
Computacionalmente costoso pero mucho más económico que entrenar desde cero.
### Cuantización
La cuantificación reduce la precisión numérica de los pesos del modelo (por ejemplo, de 32 bits
flotante a un entero de 4 bits). Esto reduce drásticamente el uso de memoria: un modelo 7B
en precisión de 16 bits requiere ~14 GB de VRAM; el mismo modelo en 4 bits (formato GGUF)
requiere ~4 GB. La cuantificación suele provocar una precisión pequeña pero aceptable
degradación y es la técnica principal que permite que modelos grandes se ejecuten en el consumidor.
hardware o incluso dispositivos móviles.
### Ventana de contexto
La ventana de contexto es la cantidad máxima de tokens que un modelo puede procesar a la vez,
incluyendo tanto el mensaje como la respuesta generada. GPT-3.5 tenía 4.096 tokens
ventana; GPT-4 Turbo y Claude 3 admiten 128.000 tokens; Géminis 1.5 Pro
admite 1.000.000 de tokens. Una ventana de contexto más grande permite que el modelo "vea"
más de una conversación o documento a la vez, mejorando la coherencia a largo plazo.
intercambios.
### RLHF (Aprendizaje reforzado a partir de la retroalimentación humana)
RLHF es la técnica de entrenamiento que transforma un modelo de lenguaje base (que
simplemente predice el siguiente token) en un asistente que sigue instrucciones y
se comporta servicialmente. Los evaluadores humanos califican los resultados del modelo y se entrena un modelo de recompensa
en sus preferencias, y el modelo de lenguaje se optimiza en función de esto
Modelo de recompensa mediante aprendizaje por refuerzo. ChatGPT, Claude y Gemini usan
variantes de RLHF o técnicas de alineación similares (por ejemplo, IA constitucional,
Optimización de preferencias directas).
### Arquitectura transformadora
Transformer es la arquitectura de red neuronal subyacente a todos los LLM modernos.
Introducido en el artículo de 2017 "La atención es todo lo que necesitas" de Vaswani et al.,
utiliza mecanismos de autoatención para procesar todos los tokens en paralelo en lugar de
secuencialmente. Los transformadores de solo codificador (BERT) se utilizan para comprender tareas;
Para tareas de generación se utilizan transformadores solo decodificadores (GPT, Llama, Mistral);
Los transformadores codificadores-decodificadores (T5, BART) se utilizan para la traducción y el resumen.
### Incrustaciones y bases de datos vectoriales
Las incrustaciones son representaciones numéricas densas de texto (o imágenes) producidas por
una red neuronal. Los textos semánticamente similares tienen incrustaciones cercanas.
espacio vectorial. Tienda de bases de datos vectoriales (ChromaDB, Pinecone, Weaviate, Qdrant)
estas incrustaciones y admiten una búsqueda rápida y aproximada del vecino más cercano. ellos son
la columna vertebral de almacenamiento de los sistemas RAG, incluida la capa de memoria fría de Potato.ai.