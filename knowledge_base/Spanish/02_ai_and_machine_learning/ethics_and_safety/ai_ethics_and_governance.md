---
# Metadata
title: "AI Ethics and Governance"
description: "AI bias, fairness, accountability, regulation, governance frameworks"
category: "AI and Machine Learning"
subcategory: "Ethics and Safety"
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
    changes: "Moved to ethics_and_safety/ subfolder; added subcategory field"
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
tags: [ai, ethics, governance, ai-and-machine-learning]
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
# Ética y gobernanza de la IA
Los sistemas de IA no son neutrales. Reflejan los datos con los que fueron capacitados, los valores de sus creadores y los incentivos de las organizaciones que los implementan. La ética consiste en preguntarse no sólo "¿podemos construir esto?" pero "¿deberíamos?" La gobernanza consiste en crear estructuras (leyes, estándares, órganos de supervisión) que garanticen que la IA se desarrolle y utilice de manera responsable. Este archivo cubre las dimensiones éticas clave de la IA y los marcos de gobernanza que surgen para abordarlas.
---

## Principios éticos básicos para la IA
La mayoría de los marcos éticos de la IA convergen en un conjunto de principios compartidos.
| Principio | Lo que significa | Desafío |
|-----------|--------------|-----------|
| **Equidad** | La IA no debería discriminar a los grupos protegidos | Definir matemáticamente la justicia es difícil; diferentes definiciones de equidad pueden entrar en conflicto |
| **Transparencia** | Los usuarios deben saber cuándo interactúan con la IA y cómo funciona | La transparencia total puede permitir el juego; los sistemas propietarios se resisten a la divulgación |
| **Responsabilidad** | Alguien debe ser responsable cuando la IA causa daño | Difundir la responsabilidad entre desarrolladores, implementadores y usuarios |
| **Privacidad** | La IA debe respetar los datos personales y la autonomía | Los datos de entrenamiento a menudo incluyen información personal; conflicto de privacidad y utilidad |
| **Seguridad** | La IA no debería causar daño físico ni psicológico | La definición de daño depende del contexto; los casos extremos son impredecibles |
| **Supervisión humana** | Los humanos deberían mantener un control significativo | El sesgo de automatización significa que los humanos ceden ante la IA; supervisión se convierte en un visto bueno |
---

## Sesgo en los sistemas de IA
### De dónde viene el sesgo
| Fuente | Descripción | Ejemplo |
|--------|-------------|---------|
| **Datos de entrenamiento** | Sesgos históricos codificados en datos | Los datos de contratación reflejan discriminación pasada → el modelo discrimina |
| **Sesgo de etiqueta** | Los anotadores humanos imponen sus prejuicios | Currículums con nombres "femeninos" calificados más bajo por los anotadores |
| **Sesgo de selección** | Los datos no representan la población objetivo | Reconocimiento facial entrenado principalmente en rostros de piel clara |
| **Sesgo de medición** | Incluye proxy para atributos protegidos | El código postal se correlaciona con la raza |
| **Sesgo algorítmico** | La optimización amplifica los pequeños sesgos | Una pequeña brecha en los datos de entrenamiento se convierte en una gran brecha en las predicciones |
### Métricas de equidad
| Métrica | Definición | Cuándo utilizar |
|--------|-----------|-------------|
| **Paridad demográfica** | La tasa positiva es igual en todos los grupos | Cuando quieres resultados iguales |
| **Probabilidades igualadas** | La tasa de verdaderos positivos y la tasa de falsos positivos son iguales en todos los grupos | Cuando quieres tasas de error iguales |
| **Paridad predictiva** | La precisión es igual en todos los grupos | Cuando quieres que las predicciones signifiquen lo mismo para todos los grupos |
| **Equidad individual** | Personas similares reciben un trato similar | Cuando quieres coherencia |
**Teorema de imposibilidad**: generalmente no se pueden satisfacer múltiples definiciones de equidad simultáneamente. Elegir qué métrica de equidad utilizar es en sí misma un juicio de valor.
### Mitigación de sesgos
| Etapa | Técnica |
|-------|-----------|
| **Preprocesamiento** | Reequilibrar los datos de entrenamiento; eliminar características sesgadas; sobremuestreo sintético |
| **En procesamiento** | Agregue restricciones de equidad a la función de pérdida; desesgo contradictorio |
| **Postprocesamiento** | Ajustar los umbrales por grupo; calibrar predicciones |
| **Evaluación** | Auditorías periódicas de equidad; métricas de desempeño desagregadas |
---

## Explicabilidad
### Por qué es importante la explicabilidad
| Razón | Descripción |
|--------|-------------|
| **Confianza** | Los usuarios deben comprender por qué se tomó una decisión |
| **Depuración** | Los desarrolladores necesitan encontrar y corregir errores del modelo |
| **Reglamento** | el "derecho a explicación" del RGPD; Requisitos de la Ley de IA de la UE |
| **Equidad** | No se pueden detectar sesgos sin comprender el comportamiento del modelo |
| **Responsabilidad** | Las organizaciones necesitan justificar las decisiones automatizadas |
### Métodos de explicación
| Método | Tipo | Cómo funciona | Limitación |
|--------|------|-------------|------------|
| **FORMA** | Importancia de la característica | Estima la contribución de cada característica utilizando la teoría de juegos | Computacionalmente caro; aproximaciones |
| **LIMA** | Madre sustituta local | Se adapta a un modelo simple en torno a la predicción | Inestable; no refleja la lógica del modelo real |
| **Visualización de atención** | Mecanismo interno | Mostrar a qué entradas atiende el modelo | Atención ≠ importancia; puede ser engañoso |
| **Contrafactuales** | Análisis de qué pasaría si | "Si esta característica fuera diferente, ¿cambiaría la predicción?" | Depende de contrafactuales realistas |
| **Atribución de funciones** | Puntuaciones de importancia | Mapas de prominencia, gradientes integrados | No explica *por qué*; justo *dónde* |
---

## Regulación de la IA
### Ley de IA de la UE (2026)
La primera ley integral de IA del mundo.
| Nivel de riesgo | Ejemplos | Requisitos |
|------------|----------|-------------|
| **Riesgo inaceptable** | Puntuación social; manipulación subliminal; vigilancia biométrica en tiempo real (con excepciones) | Prohibido |
| **Alto riesgo** | IA médica; vehículos autónomos; aplicación de la ley; infraestructura crítica | Evaluación de la conformidad; supervisión humana; transparencia |
| **Riesgo limitado** | chatbots; falsificaciones profundas; sistemas de recomendación | Debe revelar la participación de la IA |
| **Riesgo mínimo** | Filtros de spam; Juegos de vídeo; la mayoría de las aplicaciones de IA | Sin requisitos específicos |
### Otros enfoques regulatorios
| Región | Enfoque | Estado |
|--------|----------|--------|
| **Estados Unidos** | Específico del sector; órdenes ejecutivas; compromisos voluntarios | Fragmentado; no existe una ley federal integral |
| **Reino Unido** | Basado en principios; reguladores del sector | Instituto de Seguridad de IA; enfoque pro-innovación |
| **China** | Normativa específica para IA generativa, deepfakes, recomendaciones | Aplicación activa de la ley; requisitos de contenido |
| **Canadá** | AIDA (Ley de Datos e Inteligencia Artificial) | Propuesto; similar al enfoque de la UE |
| **Brasil** | Marco de regulación de la IA | En curso |
---

## Impacto ambiental
Entrenar y ejecutar modelos de IA consume energía y genera emisiones de carbono.
| Actividad | Emisiones estimadas | Comparación |
|----------|-------------------|------------|
| **Entrenamiento GPT-4** | Estimación de más de 50 toneladas de CO₂ | Equivalente a las emisiones anuales de varios coches |
| **Entrenamiento de un transformador grande** | 280-620 toneladas de CO₂ | 5 veces las emisiones de un automóvil durante su vida útil |
| **Inferencia diaria (1 millón de usuarios)** | En curso; depende del tamaño del modelo y del hardware | Puede superar las emisiones del entrenamiento con el tiempo |
| **Afinando un modelo 7B** | 1-5 toneladas de CO₂ | Importante pero mucho menor que la formación previa |
### Mitigación
| Estrategia | Impacto |
|----------|--------|
| **Hardware eficiente** | Las nuevas GPU son más eficientes energéticamente por cálculo |
| **Optimización del modelo** | Los modelos más pequeños y cuantificados utilizan menos energía |
| **Energía verde** | Alimentar centros de datos con energía renovable |
| **Arquitecturas eficientes** | Mezcla de Expertos; modelos escasos; destilación |
| **Programación consciente del carbono** | Realiza entrenamiento cuando la red esté más limpia |
---

## Propiedad intelectual y derechos de autor
| Problema | Descripción | Estado |
|-------|-------------|--------|
| **Capacitación sobre obras protegidas por derechos de autor** | Modelos entrenados en libros, artículos e imágenes sin permiso | Juicios activos; debate sobre el uso legítimo |
| **Salida generada por IA** | ¿Quién es el propietario del contenido generado por la IA? | Oficina de derechos de autor de EE. UU.: El contenido generado por IA no está protegido por derechos de autor sin suficiente autoría humana |
| **Imitación de estilo** | La IA puede imitar el estilo de un artista | Legalmente gris; preocupaciones éticas |
| **Mecanismos de exclusión voluntaria** | Algunos proveedores permiten a los creadores optar por no participar en la formación | robots.txt; filtrado de contenidos |
---

## Divulgación responsable
| Principio | Descripción |
|-----------|-------------|
| **Pruebas previas a la implementación** | Equipo rojo, auditorías parciales, evaluaciones de seguridad antes del lanzamiento |
| **Implementación gradual** | Comience con acceso limitado; expandirse a medida que se demuestra la seguridad |
| **Reporte de incidentes** | Documentar y compartir información sobre fallas y daños |
| **Recompensas por errores** | Recompensar a los investigadores externos por encontrar vulnerabilidades |
| **Tarjetas modelo** | Capacidades, limitaciones y uso previsto del modelo de documento |
---

## Procedencia de los datos
| Preocupación | Descripción |
|---------|-------------|
| **Transparencia de los datos de formación** | La mayoría de los modelos de frontera no revelan sus datos de entrenamiento |
| **Consentimiento** | ¿Se utilizaron los datos de las personas con su conocimiento y permiso? |
| **Intoxicación de datos** | ¿Pueden los atacantes inyectar datos maliciosos en conjuntos de entrenamiento? |
| **Tarjetas de conjunto de datos** | Documentación de la composición del conjunto de datos, métodos de recopilación y limitaciones |
| **Marca de agua** | Incrustar marcadores invisibles en contenido generado por IA para identificarlo |
---

## Marcos éticos prácticos
### Para desarrolladores de IA
| Pregunta | Por qué es importante |
|----------|---------------|
| **¿Quién podría resultar perjudicado por este sistema?** | Identifica las partes interesadas afectadas |
| **¿Qué pasa si el modelo es incorrecto?** | Evalúa el coste de los errores |
| **¿Se pueden explicar las decisiones del modelo?** | Determina los requisitos de explicabilidad |
| **¿Son representativos los datos de entrenamiento?** | Verificaciones de sesgos de selección y medición |
| **¿Cuáles son los modos de falla?** | Anticipa casos extremos y mal uso |
| **¿Cómo se monitoreará el sistema?** | Planes para una supervisión continua |
### Para organizaciones que implementan IA
| Práctica | Descripción |
|----------|-------------|
| **Junta de gobierno de IA** | Equipo multifuncional que revisa las implementaciones de IA |
| **Evaluaciones de impacto** | Evaluar los daños potenciales antes del despliegue |
| **Procesos de supervisión humana** | Limpiar vías de escalada cuando la IA comete errores |
| **Auditorías periódicas** | Compruebe si hay sesgos, derivas y consecuencias no deseadas |
| **Canales de comentarios de los usuarios** | Permitir a las personas afectadas informar problemas |
| **Documentación** | Mantener registros de las decisiones modelo y su justificación |
---

## Resumen
La ética y la gobernanza de la IA no son ideas tardías: son requisitos de ingeniería. El sesgo, la opacidad, el costo ambiental y las violaciones de la privacidad no son sólo preocupaciones éticas; son errores que causan daño real a personas reales. El panorama de la gobernanza está evolucionando rápidamente y la Ley de IA de la UE establece el estándar mundial. Pero la regulación por sí sola no es suficiente. Todo desarrollador de IA debe pensar en la equidad, la explicabilidad y la rendición de cuentas como parte de su trabajo diario. La pregunta no es si la IA debe ser gobernada, sino cómo construir sistemas que sean dignos de confianza.