---
# Metadata
title: "Artificial Intelligence"
description: "AI overview, ML, deep learning, LLMs, ethics"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [artificial, intelligence, ai-and-machine-learning]
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

# Inteligencia artificial
La inteligencia artificial es el intento de construir máquinas que puedan hacer cosas que requerirían inteligencia si un humano las hiciera: reconocer rostros, comprender el habla, tomar decisiones, escribir textos, jugar, conducir automóviles, diagnosticar enfermedades. El campo es tan antiguo como la propia informática: Alan Turing preguntaba: "¿Pueden pensar las máquinas?". en 1950, pero la reciente explosión de capacidades (década de 2020) ha convertido a la IA en una de las tecnologías más importantes y controvertidas de la historia de la humanidad.
---

## Una breve historia
La IA ha pasado por ciclos de exageración y decepción durante décadas. Comprender esta historia le ayudará a comprender por qué la gente está al mismo tiempo entusiasmada y escéptica.
| Época | Qué pasó | Resultado |
|-----|---------------|---------|
| **Décadas de 1950 y 1960** | Optimismo temprano. Prueba de Turing propuesta (1950). La Conferencia de Dartmouth acuña "Inteligencia Artificial" (1956). Programas iniciales como ELIZA (chatbot) y SHRDLU (comprensión de idiomas). | Emoción: "¡Tendremos AGI en una generación!" |
| **Década de 1970** | Primer invierno de IA. Las limitaciones de los primeros enfoques se vuelven claras. La financiación se agota. | Decepción: promesas incumplidas |
| **Década de 1980** | Auge de los sistemas expertos: programas basados ​​en reglas que codificaban el conocimiento humano especializado. El proyecto de Quinta Generación de Japón. | Emoción nuevamente: inversiones corporativas en IA |
| **1987-1993** | Segundo invierno de IA. Los sistemas expertos resultan frágiles y costosos de mantener. | Decepción otra vez |
| **Década de 2000** | El aprendizaje automático gana terreno. Más datos disponibles (internet). Los métodos estadísticos reemplazan las reglas codificadas a mano. | Progreso constante |
| **2012+** | Revolución del aprendizaje profundo. AlexNet gana el concurso ImageNet utilizando GPU. Las redes neuronales empiezan a superar a los métodos tradicionales en visión, habla y lenguaje. | Transformación rápida |
| **2017** | El artículo "La atención es todo lo que necesita" presenta la arquitectura Transformer. | Fundación para todo lo que sigue |
| **2020-2026** | Modelos de lenguajes grandes (GPT-3, GPT-4, Claude, Gemini, LLaMA). La IA genera texto, código, imágenes y vídeos. La adopción empresarial se acelera. | La IA pasa a formar parte de la vida cotidiana |
---

## Cómo funciona la IA moderna
### Aprendizaje automático: aprender de los datos
En lugar de programar reglas explícitas, el aprendizaje automático alimenta datos a algoritmos que encuentran patrones por sí solos.
| Tipo | Cómo funciona | Ejemplo |
|------|-------------|---------|
| **Aprendizaje supervisado** | Entrene con ejemplos etiquetados (entrada → salida correcta) | Detección de spam: envíe miles de correos electrónicos etiquetados como "spam" o "no spam" |
| **Aprendizaje no supervisado** | Encuentre patrones en datos sin etiquetar | Segmentación de clientes: agrupar clientes similares sin predefinir los grupos |
| **Aprendizaje por refuerzo** | Agente aprende por prueba y error, recibiendo recompensas o penalizaciones | IA de juego: prueba movimientos, consigue puntos por ganar, aprende qué estrategias funcionan |
### Aprendizaje profundo: redes neuronales
El aprendizaje profundo utiliza redes neuronales artificiales: capas de operaciones matemáticas simples que, combinadas, pueden aprender patrones increíblemente complejos. Lo "profundo" se refiere al número de capas.
Arquitecturas clave:
| Arquitectura | Mejor en | Uso en el mundo real |
|-------------|---------|----------------|
| **CNN** (Red neuronal convolucional) | Imagen y datos espaciales | Reconocimiento facial, imágenes médicas, vehículos autónomos |
| **RNN/LSTM** | Datos secuenciales (series temporales) | Reconocimiento de voz, generación de música (reemplazado en gran medida por Transformers) |
| **Transformador** | Todo: texto, imágenes, audio, código | GPT, Claude, Gemini, BERT, DALL-E: la arquitectura dominante |
| **GAN** (Red generativa de confrontación) | Generando datos realistas | Síntesis de imágenes, transferencia de estilo (parcialmente reemplazada por modelos de difusión) |
| **Modelos de difusión** | Generación de imágenes/vídeos de alta calidad | Difusión estable, DALL-E 3, Midjourney, Sora |
### Modelos de lenguajes grandes (LLM)
Los LLM son modelos basados ​​en Transformer entrenados en enormes cantidades de texto. Aprenden a predecir la siguiente ficha (pieza de palabra) en una secuencia, lo que resulta requerir comprensión de gramática, hechos, razonamiento e incluso algo parecido a "conocimiento".
| Modelo | Desarrollador | Característica notable |
|-------|-----------|-----------------|
| **GPT-4 / GPT-4o** | Abierta AI | Multimodal (texto + imágenes); razonamiento fuerte |
| **Claude** | Antrópico | Centrarse en la seguridad y la utilidad; ventanas de contexto largas |
| **Géminis** | Google DeepMind | Nativamente multimodal; integrado con los servicios de Google |
| **LLaMA / Llama 3** | Meta | Peso abierto; se puede ejecutar localmente; gran comunidad |
| **Mistral** | Mistral IA | Modelos abiertos eficientes competitivos con otros mucho más grandes |
**Proceso de formación**:
1. **Preentrenamiento**: aprenda de datos de texto masivos (prediciendo los próximos tokens). Aquí es donde el modelo adquiere "conocimiento".
2. **Ajustes**: Capacítese en tareas específicas o con preferencias humanas.
3. **RLHF** (Aprendizaje reforzado a partir de la retroalimentación humana): los humanos califican los resultados del modelo; el modelo aprende a producir productos que los humanos prefieren.
Las **ventanas de contexto** (la cantidad de texto que el modelo puede procesar a la vez) han aumentado de tokens 4K (primeros GPT-3) a más de 1 millón de tokens en los modelos 2026.
---

## Lo que la IA puede y no puede hacer
### Capacidades actuales
| Tarea | Rendimiento | Limitaciones |
|------|-------------|-------------|
| **Generación de texto** | Excelente: coherente, contextual y estilísticamente variada | Puede alucinar (generar información falsa con seguridad) |
| **Generación de código** | Muy bueno para patrones comunes; puede escribir programas completos | Luchas con arquitecturas novedosas; puede introducir errores sutiles |
| **Generación de imágenes** | Fotorrealista; estilos artísticos; edición | Las manos y el texto aún son imperfectos; lucha con el razonamiento espacial preciso |
| **Traducción** | Casi humano para los principales pares de idiomas | Los idiomas de bajos recursos son menos precisos; se puede perder el matiz cultural |
| **Reconocimiento de voz** | Casi humano en audio limpio | Lucha con acentos fuertes y ruido de fondo |
| **Razonamiento** | Mejorando rápidamente; puede resolver muchos problemas lógicos | Fracasa en problemas nuevos que requieren una comprensión genuina |
| **Matemáticas** | Bueno en problemas estándar | Comete errores en pruebas novedosas; no reemplaza la verificación formal |
| **Planificación y uso de herramientas** | Emergentes (agentes) | Sigue siendo poco fiable para tareas complejas de varios pasos sin supervisión humana |
### Lo que la IA no puede hacer (a partir de 2026)
- **Entiende verdaderamente** cualquier cosa como lo hacen los humanos: procesa patrones, no significados.
- **Garantizar la exactitud de los hechos**: las alucinaciones siguen siendo un problema sin resolver
- **Reemplazar el juicio humano** en decisiones de alto riesgo sin supervisión
- **Generalizar perfectamente** a dominios muy diferentes de los datos de entrenamiento
- **Operar de forma autónoma** en entornos físicos impredecibles (la robótica todavía es difícil)
---

## Ética y seguridad de la IA
La IA no es neutral. Refleja los datos con los que se capacitó, las elecciones de sus desarrolladores y los incentivos de las organizaciones que lo implementan.
### Preocupaciones clave
| Problema | Qué pasa | Ejemplo |
|-------|-------------|---------|
| **Sesgo** | Los sistemas de IA reproducen y amplifican los sesgos en los datos de entrenamiento | Algoritmos de contratación que favorecen a los candidatos masculinos; reconocimiento facial con mayores tasas de error para pieles más oscuras |
| **Privacidad** | IA entrenada con datos personales; capacidades de vigilancia | Formación sobre obras protegidas por derechos de autor; reconocimiento facial en espacios públicos |
| **Mal uso** | Deepfakes, desinformación, phishing automatizado | Vídeos falsos de políticos generados por IA; llamadas fraudulentas automatizadas |
| **Desplazamiento laboral** | Automatización de tareas anteriormente realizadas por humanos | Creación de contenidos, atención al cliente, entrada de datos, algo de programación |
| **Alineación** | Garantizar que los objetivos de la IA coincidan con los valores humanos | Una IA a la que se le pide "maximizar la producción de clips" podría convertir toda la materia en clips |
| **Riesgo existencial** | Preocupación teórica por el futuro AGI | Debate entre investigadores: algunos lo consideran urgente, otros prematuro |
### ¿Quién trabaja en seguridad?
- **Anthropic**: fundado por antiguos investigadores de OpenAI centrados específicamente en la seguridad de la IA.
- **DeepMind Safety** — equipo de investigación dentro de Google DeepMind
- **MIRI** (Instituto de Investigación de Inteligencia Artificial) — investigación teórica sobre seguridad
- **ARC** (Centro de investigación de IA): investigación empírica de seguridad
- **Organismos gubernamentales**: Ley de IA de la UE (2026), órdenes ejecutivas de EE. UU., marcos internacionales
---

## IA en la práctica: industria por industria
| Industria | Solicitud | Madurez |
|----------|-------------|----------|
| **Cuidado de la salud** | Diagnosticar el cáncer a partir de imágenes; descubrimiento de fármacos (AlphaFold); predecir los resultados de los pacientes | Implementado y en expansión |
| **Finanzas** | Detección de fraude, comercio algorítmico, calificación crediticia, robo-advisors | Ampliamente desplegado |
| **Transporte** | Vehículos autónomos (Waymo, Tesla Autopilot); optimización de rutas | Parcialmente desplegado; autonomía total aún limitada |
| **Educación** | Aprendizaje personalizado; tutoría de IA; calificación automatizada | Creciendo rápidamente |
| **Campos creativos** | Generación de imágenes (Midjourney, DALL-E); música; asistencia en escritura; finalización del código | Transformando los flujos de trabajo ahora |
| **Ciberseguridad** | Detección de amenazas; identificación de anomalías; tanto ataques como defensas | Carrera armamentista en marcha |
| **Legal** | Análisis de contratos; revisión de documentos; investigación jurídica | Ser adoptado; preocupaciones sobre la precisión |
| **Agricultura** | Monitoreo de cultivos vía satélite/dron; pulverización de precisión; predicción de rendimiento | Creciendo |
| **Fabricación** | Inspección de calidad; mantenimiento predictivo; optimización de la cadena de suministro | Ampliamente desplegado |
---

## Robótica e IA incorporada
La robótica combina la IA con máquinas físicas. A pesar de décadas de progreso, la interacción física con el mundo sigue siendo mucho más difícil que la inteligencia digital.
- **Atlas de Boston Dynamics**: movimiento bípedo avanzado; parkour; tareas de almacén
- **Robots industriales** (ABB, FANUC, KUKA): automatizan la fabricación; soldadura; asamblea
- **Robots quirúrgicos** (Sistema da Vinci): cirugía mínimamente invasiva con una precisión que va más allá de las manos humanas
- **Robots domésticos** (Roomba): sencillo pero comercialmente exitoso
- **Robots humanoides** (Tesla Optimus, Figura AI) — emergentes; Las tareas físicas de propósito general siguen siendo muy difíciles.
La brecha entre la IA digital (que ha logrado enormes avances) y la IA física (que lucha con la destreza, el equilibrio y los entornos impredecibles) es uno de los grandes desafíos del campo.
---

## Tendencias actuales (década de 2020)
| Tendencia | ¿Qué está pasando?
|-------|-------------------|
| **IA multimodal** | Sistemas que procesan texto, imágenes, audio y vídeo juntos (GPT-4V, Gemini) |
| **Agentes** | LLM que pueden usar herramientas, navegar por la web, escribir código y realizar acciones de varios pasos |
| **Modelos de peso abierto** | LLaMA de Meta y otros democratizando el acceso a grandes modelos |
| **IA en el dispositivo** | Ejecución de modelos localmente en teléfonos y portátiles (Apple Intelligence, Qualcomm NPU) |
| **Reglamento de IA** | Ley de IA de la UE (2026): primera ley integral sobre IA; clasificación de sistemas por nivel de riesgo |
| **IA en la ciencia** | Plegamiento de proteínas (AlphaFold), descubrimiento de materiales, modelización climática, pruebas matemáticas |
| **Modelos de lenguajes pequeños** | Modelos eficientes que funcionan con hardware de consumo; calidad acercándose a modelos más grandes |
---

## Resumen
La IA es el desarrollo tecnológico más significativo del siglo XXI hasta el momento. No es magia: es una coincidencia de patrones a escala, posible gracias a datos masivos, hardware potente y arquitecturas inteligentes. Lo que lo hace transformador es que la comparación de patrones, si se hace lo suficientemente bien, puede replicar muchas tareas que antes requerían inteligencia humana. Los desafíos son igualmente significativos: alucinaciones, prejuicios, desplazamiento laboral, uso indebido y la pregunta abierta de si el camino desde la IA estrecha hacia la inteligencia general es corto o increíblemente largo. Lo que está claro es que la IA remodelará todas las industrias, todas las profesiones y todos los aspectos de la vida diaria. Comprender cómo funciona (y qué no puede hacer) es esencial para navegar el mundo que estamos construyendo.