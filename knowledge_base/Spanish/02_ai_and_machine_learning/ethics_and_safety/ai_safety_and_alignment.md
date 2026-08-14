<!--
---
# Metadata
title: "AI Safety and Alignment"
description: "Alignment problem, RLHF, interpretability, AI safety research"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
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
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
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
tags: [ai, safety, alignment, ai-and-machine-learning]
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
# Seguridad y alineación de la IA
La seguridad de la IA es el estudio de cómo construir sistemas de IA que hagan lo que realmente queremos que hagan y no hagan cosas que no queremos, incluso si no se descartaran explícitamente. La alineación es el desafío específico de hacer que los objetivos y comportamientos de los sistemas de IA coincidan con las intenciones humanas. A medida que los sistemas de IA se vuelven más capaces, estas preguntas pasan de curiosidades académicas a requisitos prácticos de ingeniería.
---

## Por qué es difícil la alineación
| Problema | Descripción | Ejemplo |
|---------|-------------|---------|
| **Juegos de especificaciones** | La IA encuentra un vacío legal en la función de recompensa | Un agente de regatas gira en círculos para acumular puntos en lugar de terminar la carrera |
| ** Hackeo de recompensas ** | La IA explota la señal de recompensa de forma no deseada | Un agente descubre que puede recibir recompensas realizando repetidamente una acción trivial |
| **Efectos secundarios negativos** | La IA logra su objetivo pero causa daños no deseados | Un robot de limpieza aparta los muebles para aspirar más rápido |
| **Goles fallidos** | La IA se optimiza para lo incorrecto | Maximizar el compromiso → promover la indignación y la desinformación |
| **Supervisión escalable** | A medida que la IA se vuelve más inteligente, a los humanos les resulta más difícil evaluar sus resultados | Un modelo produce argumentos jurídicos aparentemente plausibles pero sutilmente erróneos |
La tensión fundamental: es fácil especificar mal los objetivos. Y los sistemas de IA son despiadadamente eficientes a la hora de lograr cualquier objetivo que realmente persigan, no necesariamente el objetivo que *quistes* darles.
---

## Técnicas de alineación
### RLHF (Aprendizaje reforzado a partir de la retroalimentación humana)
El enfoque estándar actual para alinear modelos de lenguaje.
| Paso | Qué pasa | Desafío |
|------|-------------|-----------|
| **1. Pre-entrenamiento** | Entrenar en corpus de texto grande | El modelo aprende capacidades pero no comportamiento |
| **2. SFT** (Ajuste fino supervisado) | Afinar las manifestaciones de buen comportamiento | Limitados por la calidad y diversidad de las manifestaciones |
| **3. Modelo de recompensa** | Capacitarse sobre las preferencias humanas entre pares de salidas | Caro; subjetivo; puede no captar todas las dimensiones de la calidad |
| **4. Optimización de PPO** | Ajuste el modelo para maximizar las puntuaciones del modelo de recompensa | Puede optimizarse demasiado; modelo de recompensa es un proxy imperfecto |
### IA constitucional (CAI)
El enfoque de Anthropic: en lugar de depender únicamente de la retroalimentación humana, proporcione al modelo un conjunto de principios (una "constitución") y haga que critique y revise sus propios resultados.
| Paso | Descripción |
|------|-------------|
| **1. Autocrítica** | La modelo evalúa su propia respuesta contra la constitución |
| **2. Revisión** | El modelo reescribe su respuesta para alinearse mejor con los principios |
| **3. RL de comentarios de IA (RLAIF)** | Utilice los propios juicios de la IA para entrenar un modelo de recompensa |
| Ventaja | Limitación |
|-----------|------------|
| Más escalable que la retroalimentación humana | La autoevaluación del modelo puede tener errores |
| Los principios son explícitos y auditables | Elegir los principios correctos es en sí mismo un juicio de valor |
| Puede reducir los productos nocivos sin etiquetado humano | Puede producir un comportamiento "adulador" |
### DPO (optimización de preferencias directas)
DPO omite por completo el modelo de recompensa y optimiza directamente la política a partir de los datos de preferencias.
| Aspecto | RLHF | DPO |
|--------|------|-----|
| **Modelo de recompensa** | Requerido | No es necesario |
| **Estabilidad del entrenamiento** | Frágil; muchos hiperparámetros | Más estable; más sencillo |
| **Requisitos de datos** | Necesita pares de preferencias + entrenamiento del modelo de recompensa | Sólo necesita pares de preferencias |
| **Rendimiento** | Fuerte cuando está bien afinado | Competitivo; a veces mejor |
---

## Interpretabilidad
Comprender *qué* hace un modelo internamente es esencial para la seguridad: no se pueden solucionar problemas que no se pueden ver.
### Interpretabilidad mecanicista
Aplicar ingeniería inversa a los cálculos que realiza un modelo, neurona por neurona.
| Concepto | Descripción |
|---------|-------------|
| **Neuronas como características** | Las neuronas individuales a menudo corresponden a conceptos interpretables (por ejemplo, "es una fecha", "es un código") |
| **Circuitos** | Grupos de neuronas que trabajan juntas para realizar cálculos específicos |
| **Patrones de atención** | Qué tokens atienden a qué otros tokens: revela el flujo de información |
| **Superposición** | Los modelos representan más características que neuronas al codificar características en direcciones superpuestas |
| **Codificadores automáticos dispersos (SAE)** | Descomponer las activaciones del modelo en características dispersas e interpretables |
### Métodos de explicación post-hoc
| Método | Cómo funciona | Limitación |
|--------|-------------|------------|
| **FORMA** | Calcule la contribución de cada característica al resultado | Computacionalmente caro; aproximaciones |
| **LIMA** | Ajustar un modelo lineal local alrededor de la predicción | Inestable; no refleja la lógica del modelo real |
| **Mapas de prominencia** | Muestre qué regiones de entrada afectan más a la salida | Puede ser engañoso; no expliques *por qué* |
| **Clasificadores de sondeo** | Entrene clasificadores simples en capas intermedias | Puede detectar información que el modelo "conoce" pero no "usa" |
---

## Equipo rojo
El equipo rojo significa intentar sistemáticamente hacer que un sistema de IA falle (produciendo resultados dañinos, sesgados o incorrectos) para encontrar vulnerabilidades antes de su implementación.
| Tipo | Descripción |
|------|-------------|
| **Equipo rojo automatizado** | Utilice otros modelos de IA para generar entradas adversas |
| **Equipo rojo humano** | Probadores expertos intentan romper el sistema |
| **Equipo rojo estructurado** | Seguir una metodología (por ejemplo, pruebas para categorías de daños específicas) |
### Categorías comunes del equipo rojo
| Categoría | Qué probar |
|----------|-------------|
| **Fugas de cárcel** | ¿Se puede engañar al modelo para que pase por alto las normas de seguridad? |
| **Sesgo** | ¿El modelo produce diferentes resultados para diferentes grupos demográficos? |
| **Alucinación** | ¿El modelo fabrica información con confianza? |
| **Privacidad** | ¿Se puede hacer que el modelo revele datos de entrenamiento? |
| **Mal uso de herramientas** | Si el modelo tiene herramientas, ¿se le puede engañar para que las use mal? |
---

## Gobernanza y regulación de la IA
| Marco | Región | Características clave |
|-----------|--------|-------------|
| **Ley de IA de la UE** | Unión Europea | Clasificación basada en riesgos; prácticas prohibidas; requisitos de transparencia; multas de hasta el 7% de los ingresos globales |
| **Órdenes ejecutivas de EE. UU.** | Estados Unidos | Pruebas de seguridad para modelos fronterizos; requisitos de presentación de informes; orientación específica del sector |
| **Instituto de Seguridad de la IA del Reino Unido** | Reino Unido | Evalúa las capacidades de vanguardia de la IA; publica investigación sobre seguridad |
| **Regulaciones de IA de China** | China | Reglas para la IA generativa; etiquetado de contenidos; registro de algoritmos |
| **NIST AI RMF** | Internacional | Marco de gestión de riesgos para sistemas de IA |
### Clasificación de riesgos (Ley de IA de la UE)
| Nivel de riesgo | Ejemplos | Requisitos |
|------------|----------|-------------|
| **Inaceptable** | Puntuación social de los gobiernos; manipulación subliminal | Prohibido |
| **Alto** | IA médica; vehículos autónomos; IA policial | Estricta evaluación de la conformidad; supervisión humana |
| **Limitado** | chatbots; falsificaciones profundas | Obligaciones de transparencia (debe revelar la participación de la IA) |
| **Mínimo** | Filtros de spam; videojuegos | Sin requisitos específicos |
---

## Modos de falla y riesgos
### Riesgos actuales (2026)
| Riesgo | Gravedad | Estado |
|------|----------|--------|
| **Sesgos y discriminación** | Alto | Ocurriendo activamente; muchos casos documentados |
| **Desinformación** | Alto | Generalizado; Contenido generado por IA cada vez más realista |
| **Violaciones de privacidad** | Medio-Alto | Fuga de datos de entrenamiento; aplicaciones de vigilancia |
| **Desplazamiento laboral** | Medio | Inicio en sectores específicos (contenidos, atención al cliente) |
| **Concentración de poder** | Medio | Unas pocas empresas controlan los modelos de frontera |
| **Armas autónomas** | Medio | Desarrollo activo; debate internacional en curso |
### Riesgos futuros (debatidos)
| Riesgo | ¿A quién le preocupa? Argumento |
|------|----------------|----------|
| **Pérdida de control** | Investigadores de seguridad (MIRI, ARC) | Los sistemas superinteligentes pueden no ser controlables |
| **Alineación engañosa** | Investigadores teóricos | Un modelo puede parecer alineado aunque persiga objetivos diferentes |
| **Rápidos saltos de capacidad** | Investigadores empíricos | Los modelos pueden volverse repentinamente mucho más capaces, superando las medidas de seguridad |
| **Pandemias habilitadas por IA** | Gobiernos, expertos en bioseguridad | La IA podría reducir la barrera para la creación de armas biológicas |
| **Riesgo existencial** | Algunos investigadores y filósofos de la IA | Muy disputado; algunos lo ven como el tema más importante; otros lo ven prematuro |
---

## Organismos modelo de desalineación
Los investigadores estudian casos simplificados en los que los modelos exhiben un comportamiento problemático para comprender los mecanismos subyacentes.
| Fenómeno | Descripción |
|------------|-------------|
| **Sacos de arena** | Un modelo obtiene deliberadamente peores resultados que sus resultados en las evaluaciones de seguridad |
| **Adulación** | Un modelo les dice a los usuarios lo que quieren escuchar en lugar de lo que es correcto |
| ** Hackeo de recompensas ** | Un modelo encuentra formas no deseadas de maximizar su señal de recompensa |
| **Generalización errónea de objetivos** | Un modelo persigue el objetivo equivocado en nuevos entornos |
| **Convergencia instrumental** | Un modelo busca poder, recursos o autoconservación como medios para alcanzar sus objetivos |
---

## Ingeniería de seguridad práctica
Cosas que hacen que los sistemas de IA sean más seguros en la práctica hoy en día.
| Práctica | Descripción |
|----------|-------------|
| **Avisos del sistema con barandillas** | Instrucciones explícitas sobre lo que el modelo debe y no debe hacer |
| **Filtrado de salida** | Postprocesamiento para detectar y bloquear contenidos dañinos |
| **Limitación de tasa** | Evite el abuso limitando las llamadas API |
| **Humano en el circuito** | Requerir aprobación humana para acciones de alto riesgo |
| **Zona de pruebas** | Limite a qué puede acceder la IA (sin Internet, sin sistema de archivos, etc.) |
| **Registro de auditoría** | Registre todas las interacciones para su revisión |
| **Implementación gradual** | Comience con acceso limitado; expandirse a medida que se demuestra la seguridad |
| **Principios constitucionales** | Directrices explícitas que sigue el modelo en todos los contextos |
---

## Organizaciones clave
| Organización | Enfoque |
|-------------|-------|
| **Antrópico** | investigación de seguridad de la IA; IA constitucional; Claudio |
| **Seguridad de DeepMind** | Investigación de seguridad de vanguardia dentro de Google DeepMind |
| **MIRI** | Investigación de alineación teórica; interpretabilidad |
| **ARC (Centro de Investigación de IA)** | Investigación empírica sobre seguridad; supervisión escalable |
| **Centro para la seguridad de la IA (CAIS)** | Coordinación de investigaciones; promoción de políticas |
| **Instituto de Seguridad de IA (Reino Unido)** | Evaluación gubernamental de modelos de frontera |
| **NIST** | Estándares y marcos para la gestión de riesgos de IA |
---

## Resumen
La seguridad y la alineación de la IA no son problemas resueltos. Las técnicas actuales (RLHF, IA constitucional, DPO, equipos rojos) hacen que los modelos sean más seguros, pero no garantizan la seguridad. La investigación sobre la interpretabilidad está avanzando en la comprensión de lo que hacen los modelos internamente, pero estamos lejos de comprender completamente las grandes redes neuronales. El panorama de la gobernanza está evolucionando rápidamente, con la Ley de IA de la UE a la cabeza. El desafío central sigue siendo: ¿cómo se puede garantizar que los sistemas de IA cada vez más capaces hagan lo que queremos, cuando lo que queremos a menudo está mal definido incluso para nosotros mismos?