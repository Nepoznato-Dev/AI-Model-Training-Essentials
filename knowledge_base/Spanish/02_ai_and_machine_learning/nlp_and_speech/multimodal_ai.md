---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [multimodal, ai, ai-and-machine-learning]
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
# IA multimodal
Los sistemas de IA multimodal procesan y combinan información de múltiples tipos de datos (texto, imágenes, audio, video y más) simultáneamente. Mientras que los sistemas de IA anteriores eran típicamente de una sola modalidad (solo texto, solo imágenes), los sistemas modernos más capaces son multimodales. GPT-4V lee imágenes y texto juntos; Gemini procesa texto, imágenes, audio y vídeo de forma nativa; y sistemas como Sora generan videos a partir de descripciones de texto. Este archivo cubre cómo funciona la IA multimodal, las arquitecturas detrás de ella y por qué la combinación de modalidades es tan poderosa.
---

## ¿Por qué multimodal?
| Beneficio | Descripción | Ejemplo |
|---------|-------------|---------|
| **Comprensión más rica** | Diferentes modalidades proporcionan información complementaria | Un vídeo transmite movimiento, sonido y contexto que el texto por sí solo no puede |
| **Mejor generalización** | El aprendizaje entre modalidades crea representaciones más sólidas | Un modelo que ha visto imágenes y descripciones de texto de "gato" entiende mejor el concepto |
| **Interacción más natural** | Los humanos se comunican a través de múltiples canales | Asistentes de voz que ven lo que estás señalando |
| **Transferencia intermodal** | El conocimiento de una modalidad ayuda con otra | La comprensión de imágenes mejora la generación de texto y viceversa |
---

## Arquitecturas principales
### Modelos visión-lenguaje (VLM)
Modelos que procesan tanto imágenes como texto juntos.
| Arquitectura | Cómo funciona | Ejemplos |
|-------------|-------------|---------|
| **Codificador doble** | Codificadores separados para imagen y texto; combinar en una etapa posterior | RECORTAR, ALINEAR |
| **Codificador Fusion** | Los tokens de imagen y texto se entrelazan y procesan juntos | Flamenco, Géminis |
| **Atención cruzada** | Los tokens de texto atienden a las características de la imagen (o viceversa) | Flamenco, CoCa |
| **Tokenizador unificado** | Las imágenes se convierten en tokens y se procesan junto con tokens de texto | Géminis, Camaleón |
### Cómo funcionan los modelos visión-lenguaje
| Paso | Descripción |
|------|-------------|
| **1. Codificar imagen** | Un codificador de visión (ViT, SigLIP) convierte la imagen en un conjunto de vectores de características |
| **2. Codificar texto** | Un codificador de idioma procesa los tokens de texto |
| **3. Modalidades de fusibles** | Las características de la imagen se proyectan en el espacio de incrustación del modelo de lenguaje |
| **4. Generar** | El modelo de lenguaje produce texto condicionado a la entrada de texto y de imagen |
### Modelos clave visión-lenguaje
| Modelo | Desarrollador | Arquitectura | Característica notable |
|-------|-----------|-------------|-----------------|
| **CLIP** | Abierta AI | Codificador dual (ViT + codificador de texto) | Clasificación de imágenes de disparo cero mediante texto |
| **LLaVA** | Código abierto | Codificador visual LLaMA + CLIP | VLM de código abierto; comunidad fuerte |
| **GPT-4V/4o** | Abierta AI | Multimodal unificado | Procesa texto, imágenes y audio juntos |
| **Géminis** | Google DeepMind | Nativamente multimodal desde la formación | Construido para multimodal desde cero |
| **Claude** | Antrópico | Visión + texto | Fuerte en comprensión de documentos y gráficos |
| **Qwen-VL** | Alibaba | VLM de peso abierto | Competitivo con modelos cerrados |
| **PasanteVL** | Código abierto | Codificador de visión multiescala | Fuerte opción de código abierto |
---

## Modelos de audio y voz
### Reconocimiento de voz (ASR)
| Modelo | Arquitectura | Característica notable |
|-------|-------------|-----------------|
| **Susurro** (OpenAI) | Transformador codificador-decodificador | Capacitado con 680.000 horas de audio multilingüe; robusto |
| **Conformador** | Convolución + autoatención | Combina características locales y globales |
| **wav2vec 2.0** | Autosupervisado | Aprende del discurso sin etiquetar |
| **USM** (Google) | Modelo de habla universal | 2 millones de horas de datos etiquetados; Más de 300 idiomas |
### Texto a voz (TTS)
| Modelo | Enfoque | Característica notable |
|-------|----------|-----------------|
| **VALL-E** (Microsoft) | Códec neuronal | Clonación de voz a partir de una muestra de 3 segundos |
| **Ladrar** (Suno) | Basado en transformador | Plurilingüe; incluye sonidos que no son del habla |
| **ElevenLabs** | Comercial | Clonación de voz de alta calidad |
| **ChatTTS** | Código abierto | Discurso conversacional con prosodia natural |
| **Discurso de pez** | Código abierto | Plurilingüe; inferencia rápida |
### Comprensión de audio
| Modelo | Capacidad |
|-------|-----------|
| **AudioLDM** | Generación de efectos de sonido a partir de texto |
| **MusicGen** (Meta) | Generación de texto a música |
| **Qwen-Audio** | Comprensión de audio (habla, música, sonidos ambientales) |
| **SALMÓN** | Comprensión del habla, audio, lenguaje, música y ruido |
---

## Modelos de vídeo
El vídeo combina imágenes, audio, texto y tiempo, lo que lo convierte en la modalidad más compleja.
| Modelo | Tipo | Capacidad |
|-------|------|-------------|
| **Sora** (OpenAI) | Texto a vídeo | Hasta 1080p; entiende la física |
| **Géminis** | Comprensión de vídeo | Puede analizar videos largos con audio |
| **Video-LLaVA** | Vídeo + texto | Comprensión de vídeo de código abierto |
| **Pista Gen-3** | Texto/imagen a vídeo | Generación de vídeos comerciales |
| **Kling** | Texto a vídeo | Generación de vídeos de formato largo |
### Video de comprensión de los desafíos
| Desafío | Descripción |
|-----------|-------------|
| **Razonamiento temporal** | Comprender los acontecimientos que se desarrollan a lo largo del tiempo |
| **Contexto largo** | Los vídeos pueden durar horas; procesar todos los fotogramas es caro |
| **Sincronización audiovisual** | Conectando lo dicho con lo mostrado |
| **Causalidad** | Comprensión de causa y efecto en secuencias de vídeo |
---

## Recuperación multimodal
Encontrar contenido relevante en diferentes modalidades.
| Tarea | Descripción | Ejemplo |
|------|-------------|---------|
| **Texto → Imagen** | Buscar imágenes que coincidan con una consulta de texto | Busque "puesta de sol sobre las montañas" en una biblioteca de fotos |
| **Imagen → Texto** | Buscar texto relevante para una imagen | Generando títulos para imágenes |
| **Texto → Audio** | Encuentra sonidos que coincidan con una descripción | Diseño de sonido: "pasos sobre grava" |
| **Imagen → Imagen** | Encuentra imágenes visualmente similares | Búsqueda de productos por imagen |
### CLIP para recuperación multimodal
El espacio de incrustación compartido de CLIP permite la recuperación intermodal sin disparos:
| Paso | Descripción |
|------|-------------|
| 1 | Codifica todas las imágenes con el codificador de visión |
| 2 | Codifique la consulta de texto con el codificador de texto |
| 3 | Calcular la similitud del coseno entre la incrustación de texto y todas las incrustaciones de imágenes |
| 4 | Devuelve las imágenes con mayor similitud |
Esto funciona sin ningún tipo de capacitación específica para la tarea, una propiedad llamada capacidad de **disparo cero**.
---

## IA incorporada
La IA incorporada combina la percepción multimodal con la acción física.
| Sistema | Modalidad | Solicitud |
|--------|----------|-------------|
| **RT-2** (Google) | Visión + lenguaje → acciones de robots | Control de robot de uso general a partir de instrucciones de texto |
| **Octubre** | Política de robots de código abierto | Capacitado con diversos datos de robots |
| **Tesla Optimus** | Visión + lenguaje → tareas físicas | Robot humanoide para tareas generales |
| **Figura 01** | Visión + lenguaje + habla | Robot humanoide con capacidad conversacional |
### Desafíos de la IA incorporada
| Desafío | Por qué es difícil |
|-----------|--------------|
| **Brecha entre simulación y real** | La simulación no captura perfectamente la física del mundo real |
| **Destreza** | El control de la motricidad fina (manos, dedos) es extremadamente difícil |
| **Seguridad** | Los robots físicos pueden causar daños reales |
| **Procesamiento en tiempo real** | Debe percibir, decidir y actuar en milisegundos |
| **Generalización** | Un robot entrenado para recoger vasos rojos puede fallar en los azules |
---

## Datos y formación
### Datos de entrenamiento multimodal
| Conjunto de datos | Modalidades | Tamaño |
|---------|-----------|------|
| **LAION-5B** | Pares imagen-texto | 5,85 mil millones de pares |
| **CompDatos** | Imagen-texto curado | Punto de referencia para el diseño de conjuntos de datos |
| **INGENIO** (Wikipedia) | Imagen-texto de Wikipedia | 11,5 millones de pares |
| **Cómo100M** | Vídeo-texto (vídeos instructivos) | 100 millones de vídeos |
| **LibriDiscurso** | Texto de voz | 1.000 horas de inglés |
| **Voz común** | Texto de voz | Plurilingüe; aportado por la comunidad |
### Estrategias de formación
| Estrategia | Descripción | Cuándo utilizar |
|----------|-------------|-------------|
| **Entrenamiento conjunto** | Entrena en todas las modalidades simultáneamente | Cuando haya alineado datos multimodales |
| **Aprendizaje curricular** | Comience con ejemplos sencillos; aumentar la dificultad | Mejora la convergencia |
| **Aprendizaje contrastante** | Aprenda a unir pares relacionados entre modalidades (estilo CLIP) | Construyendo representaciones compartidas |
| **Ajuste de instrucciones** | Capacitación en pares instrucción-respuesta multimodales | Hacer modelos sigue instrucciones multimodales |
---

## Evaluación
| Punto de referencia | Modalidades | Qué prueba |
|-----------|-----------|---------------|
| **MMLU** | Texto | Conocimiento en 57 temas |
| **MMMU** | Texto + imágenes | Razonamiento a nivel universitario con diagramas |
| **MathVista** | Texto + imágenes | Razonamiento matemático con datos visuales |
| **Video-MME** | Texto + vídeo | Comprensión del vídeo y razonamiento temporal |
| **CASCO** | Texto + audio | Evaluación multimodal de contexto largo |
| **SWE-banco** | Texto + código | Tareas de ingeniería de software del mundo real |
---

## Resumen
La IA multimodal representa el cambio de modelos de propósito único a sistemas que perciben y razonan en todas las formas de datos. Los modelos de lenguaje visual como GPT-4V y Gemini pueden comprender imágenes y texto juntos; modelos de voz como Whisper y VALL-E manejan audio; Los modelos de vídeo están empezando a procesar toda la complejidad de las imágenes en movimiento con sonido. La tendencia es clara: los sistemas de IA más capaces del futuro serán multimodales de forma nativa y procesarán todo tipo de información simultáneamente. Los desafíos (alineación de datos, costo computacional, evaluación e implementación incorporada) son importantes, pero el progreso en 2024-2026 ha sido rápido.