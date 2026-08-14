<!--
---
# Metadata
title: "Behavioural Economics and Decision Science"
description: "Cognitive biases, prospect theory, heuristics, nudges, choice architecture"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [behavioural, economics, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Economía del comportamiento y ciencia de la decisión
La economía del comportamiento estudia cómo las personas realmente toman decisiones, no cómo las tomarían los agentes racionales. La economía tradicional supone que las personas son racionales, egoístas y buenas procesando información. Décadas de investigación realizadas por Kahneman, Tversky, Thaler y otros han demostrado que esto es tremendamente inexacto. Las personas utilizan atajos mentales, se dejan influenciar por un contexto irrelevante, sobrevaloran la información reciente y cometen errores sistemáticamente predecibles. Comprender estos patrones es esencial para diseñar mejores productos, políticas, organizaciones y decisiones personales.
---

## Dos sistemas de pensamiento
| Sistema | Características | Velocidad | Esfuerzo | Ejemplo |
|--------|----------------|-------|--------|---------|
| **Sistema 1** | Automático; intuitivo; emocional | Rápido | Bajo | Leer expresiones faciales; conduciendo por una ruta familiar |
| **Sistema 2** | Adrede; analítico; lógico | Lento | Alto | Resolver un problema matemático; comparación de especificaciones de productos |
**Información clave**: la mayoría de las decisiones las toma el Sistema 1. El Sistema 2 es vago y solo interviene cuando el Sistema 1 está perplejo. Esto significa que la mayoría de nuestras decisiones son intuitivas, no racionales, y construimos racionalizaciones a posteriori.
---

## Sesgos cognitivos
### Sesgos de juicio
| Sesgo | Descripción | Ejemplo |
|------|-------------|---------|
| **Anclaje** | Confiar demasiado en la primera información encontrada | Negociaciones salariales: el primer número mencionado ancla la discusión |
| **Heurística de disponibilidad** | Juzgar la probabilidad por la facilidad con la que se nos ocurren ejemplos | Se sobreestima el riesgo de accidentes aéreos porque los accidentes se informan ampliamente |
| **Representatividad** | Juzgar la probabilidad por similitud con un estereotipo | Suponiendo que una persona tranquila es un bibliotecario y no un agricultor (ignorando las tarifas base) |
| **Efecto de marco** | Las decisiones cambian según cómo se presentan las opciones | Una "tasa de supervivencia del 90%" se siente mejor que una "tasa de mortalidad del 10%" |
| **Sesgo retrospectivo** | "Lo supe desde el principio": ver los acontecimientos pasados ​​como predecibles | Después de una caída del mercado, la gente afirma que era obvio |
| **Efecto Dunning-Kruger** | Las personas con baja capacidad sobreestiman su capacidad; expertos subestiman los suyos | Los inversores novatos confían en poder ganarle al mercado |
### Sesgos de decisión
| Sesgo | Descripción | Ejemplo |
|------|-------------|---------|
| **Aversión a las pérdidas** | Las pérdidas se sienten aproximadamente dos veces más dolorosas que las ganancias equivalentes que se sienten bien | Mantener las acciones perdedoras demasiado tiempo; evitando riesgos necesarios |
| **Sesgo de status quo** | Prefiriendo el estado actual de las cosas | No cambiar a un mejor plan de salud o fondo de pensiones |
| **Efecto dotación** | Sobrevalorar lo que ya posees | Pidiendo más por vender una taza de lo que pagaría por comprarla |
| **Falacia del costo hundido** | Continuar debido a la inversión pasada, no al valor futuro | Terminar un mal libro porque ya has leído la mitad |
| **Sesgo de confirmación** | Buscando información que confirme las creencias existentes | Leer únicamente fuentes de noticias que coincidan con sus puntos de vista |
| **Sesgo presente (descuento hiperbólico)** | Sobreponderación de las recompensas inmediatas frente a las futuras | Procrastinar; ahorro insuficiente para la jubilación |
| **Efecto de tendencia** | Hacer algo porque otros lo hacen | Comprar activos durante una burbuja |
| **Efecto señuelo** | Agregar una opción inferior para que otra opción se vea mejor | Tres niveles de precios donde existe la opción intermedia para que la superior parezca razonable |
---

## Heurística
| Heurística | Descripción | Cuando ayuda | Cuando falla |
|-----------|-------------|---------------|---------------|
| **Reconocimiento** | Elige lo que reconoces | Decisiones rápidas en ámbitos familiares | Se pasan por alto opciones desconocidas pero mejores |
| **Toma lo mejor** | Elija según la señal más importante | Cuando domina un factor | Cuando varios factores importan por igual |
| **Satisfactorio** | Elija la primera opción que cumpla con los criterios mínimos | Cuando los costos de búsqueda son altos | Conformarse con lo "suficientemente bueno" cuando existe algo mejor |
| **Eliminación por aspectos** | Eliminar opciones un atributo a la vez | Al comparar muchas opciones | El orden de los atributos cambia el resultado |
| **Heurística del afecto** | Tomar decisiones basadas en las emociones | Evaluación rápida de amenazas | Las respuestas emocionales anulan los datos |
---

## Teoría de la perspectiva
La alternativa de Kahneman y Tversky a la teoría de la utilidad esperada:
| Principio | Descripción |
|-----------|-------------|
| **Dependencia de referencia** | La gente evalúa los resultados en relación con un punto de referencia (normalmente el status quo), no en términos absolutos |
| **Aversión a las pérdidas** | Las pérdidas representan aproximadamente el doble que las ganancias equivalentes |
| **Sensibilidad decreciente** | La diferencia entre $100 y $200 parece mayor que entre $1100 y $1200 |
| **Ponderación de probabilidad** | La gente sobrepondera las probabilidades pequeñas y subestima las grandes |
### La función de valor
| Región | Forma | Comportamiento |
|--------|-------|-----------|
| **Ganancias** | Cóncavo (aversión al riesgo) | Prefiera $500 seguros a un 50% de probabilidad de $1,000 |
| **Pérdidas** | Convexo (búsqueda de riesgos) | Prefiere un 50% de posibilidades de perder $1000 a una pérdida segura de $500 |
| **El dominio de pérdida es mayor** | Aversión a las pérdidas | Perder $500 duele más que ganar $500 se siente bien |
---

## Teoría del empujón
### Principios de arquitectura de elección
| Principio | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Opciones predeterminadas** | La gente tiende a aceptar los valores predeterminados | La donación voluntaria de órganos aumenta drásticamente las tasas de donación |
| **Simplificación** | Reducir la complejidad; hazlo fácil | Autoinscripción en planes de pensiones |
| **Prueba social** | La gente sigue lo que hacen los demás | "9 de cada 10 huéspedes reutilizan sus toallas" |
| **Prominencia** | Haga que la información importante destaque | Las calorías cuentan en los menús; etiquetas energéticas en electrodomésticos |
| **Dispositivos de compromiso** | Bloquear el comportamiento futuro | Transferencias automáticas de ahorro; compromiso previo de ejercicio |
| **Tiempo** | Cuando preguntas asuntos | Inscribirse en una pensión el día de pago, no a final de mes |
### Empujar frente a lodo
| Concepto | Descripción | Ejemplo |
|---------|-------------|---------|
| **Empujar** | Haciendo más fácil hacer lo correcto | Inscripción predeterminada; formularios simplificados |
| **Lodos** | Fricción excesiva que impide tomar buenas decisiones | Formas burocráticas; procesos de cancelación ocultos |
| **Auditoría de lodos** | Identificar y eliminar fricciones innecesarias | Contar cuántos clics/pasos se necesitan para completar una tarea |
---

## Aplicaciones
### En los negocios
| Solicitud | Perspectiva conductual | Resultado |
|-------------|-------------------|--------|
| **Precios** | Anclaje; efecto señuelo | Precios de tres niveles; opción premium impulsa las ventas de nivel medio |
| **Mercadotecnia** | Escasez; prueba social | "Sólo quedan 2 en stock"; Etiquetas "más vendidas" |
| **Diseño de producto** | Opciones predeterminadas; fricción | Opciones preseleccionadas; compra con un clic |
| **Negociación** | Enmarcado; anclaje | Primera oferta ancla la negociación |
| **Comportamiento de los empleados** | Normas sociales; compromiso | Metas públicas; reconocimiento entre pares |
### En Políticas Públicas
| Solicitud | Perspectiva conductual | Ejemplo |
|-------------|-------------------|---------|
| **Cumplimiento fiscal** | Prueba social | "9 de cada 10 personas en tu zona pagan sus impuestos a tiempo" |
| **Salud** | Valores predeterminados; compromiso | Optar por no donar órganos; programación automática de citas |
| **Ahorros** | Sesgo presente; valores predeterminados | Autoinscripción en planes de jubilación; ahorrar-más-mañana |
| **Energía** | Comparación social; prominencia | Comparando el uso de energía con los vecinos |
| **Educación** | Simplificación; empujones | Formularios FAFSA simplificados; recordatorios de mensajes de texto |
---

## Limitaciones y críticas
| Crítica | Descripción |
|-----------|-------------|
| **Crisis de replicación** | Algunos hallazgos clásicos (por ejemplo, el agotamiento del ego) no han logrado replicarse |
| **Tamaños del efecto** | Algunos empujones tienen pequeños efectos que pueden no justificar los costos de implementación |
| **Preocupaciones éticas** | ¿Quién decide cuál es la elección "correcta"? Paternalismo versus autonomía |
| **Dependencia del contexto** | Los sesgos son más fuertes en algunos contextos que en otros; los hallazgos de laboratorio pueden no generalizarse |
| **Simplificación excesiva** | El comportamiento humano es complejo; los sesgos no lo explican todo |
| **Efectos contraproducentes** | Algunos empujones pueden desencadenar reactancia o reducir la motivación intrínseca |
---

## Resumen
La economía del comportamiento revela que la toma de decisiones humana es sistemáticamente diferente del modelo del agente racional. El Sistema 1 (rápido, intuitivo) domina el Sistema 2 (lento, analítico). Los sesgos cognitivos (anclaje, disponibilidad, aversión a las pérdidas, sesgo del status quo) son predecibles y generalizados. La teoría de las perspectivas muestra que las personas evalúan los resultados en relación con puntos de referencia, son reacias a las pérdidas y tienen una sensibilidad cada vez menor a los cambios. La teoría del empujón utiliza estos conocimientos para diseñar arquitecturas de elección que ayuden a las personas a tomar mejores decisiones sin restringir la libertad. Las aplicaciones abarcan negocios (precios, marketing, diseño de productos) y políticas públicas (cumplimiento fiscal, ahorros, salud). Pero el campo tiene limitaciones: fallas de replicación, tamaños de efecto pequeños y cuestiones éticas sobre el paternalismo. La conclusión práctica es diseñar sistemas que tengan en cuenta cómo se comportan realmente las personas, no cómo desearíamos que lo hicieran.