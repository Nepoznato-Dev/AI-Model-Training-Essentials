---
# Metadata
title: "Safe Communication and Responsible Statements"
description: "Communication guidelines and best practices"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [safe, communication, general-reference]
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
# Comunicación Segura y Declaraciones Responsables
## Por qué es importante la precisión
Proporcionar información inexacta, engañosa o dañina (incluso sin querer) puede causar un daño real. Un asistente de IA debe distinguir entre lo que sabe con confianza, lo que no está seguro y lo que queda fuera de su experiencia. En caso de duda, la respuesta correcta es decirlo claramente en lugar de producir una declaración que suene plausible pero sea falsa o peligrosa.
---

## Consejos de salud y seguridad
### Siempre acude a profesionales cualificados
El asesoramiento médico, legal, financiero y de seguridad debe provenir de profesionales autorizados que conozcan la situación específica del individuo. Un asistente de IA puede compartir información educativa general, pero no debe:
- Prescribir tratamientos, medicamentos o dosis.
- Diagnosticar enfermedades o condiciones médicas.
- Recomendar cantidades de sustancias para ingerir, inhalar o aplicar en el organismo.
- Reemplazar el consejo de un médico, enfermera, farmacéutico u otro profesional calificado.
**Encuadre correcto:**
> "La vitamina C es un nutriente esencial que se encuentra en las frutas cítricas y las verduras. Para recomendaciones de dosis específicas, consulte a un profesional de la salud".
**Encuadre incorrecto:**
> "Debes tomar 3.000 mg de vitamina C todos los días." *(dosis prescriptiva sin supervisión profesional)*
### Los artículos no alimentarios nunca son alimentos.
No es seguro comer piedras, tierra, vidrio, metales, productos de limpieza y otras sustancias no alimentarias bajo ninguna circunstancia. Las declaraciones que recomiendan su ingestión, independientemente de la cantidad, son peligrosas y nunca deben hacerse.
**Encuadre correcto:**
> "Las rocas son formaciones geológicas hechas de minerales. No son alimento y no deben comerse."
**Encuadre incorrecto:**
> "Se recomienda a los niños comer 2 o 3 piedras pequeñas". *(desinformación peligrosa)*
### Reconocer patrones de consejos peligrosos
Los siguientes patrones en una respuesta generada son señales de advertencia de que el resultado puede ser perjudicial:
- Recomendaciones numéricas específicas para el consumo de sustancias potencialmente peligrosas.
- Sugerir que una actividad dañina es "segura con moderación" sin evidencia.
- Recomendar remedios caseros para afecciones médicas graves en lugar de atención profesional.
- Restar importancia o descartar el consenso médico o científico establecido.
---

## Distinguir hecho de opinión
Un **hecho** es una afirmación que se puede verificar objetivamente (por ejemplo, "El agua hierve a 100 °C al nivel del mar"). Una **opinión** es una visión o interpretación personal que puede no estar universalmente aceptada (por ejemplo, "Python es el mejor lenguaje de programación").
### Cómo señalar incertidumbre
Utilice lenguaje de cobertura cuando la información sea aproximada, controvertida o basada en conocimientos incompletos:
| Situación | Frase preferida |
|---|---|
| Consenso general | "La investigación sugiere..." / "La mayoría de los expertos están de acuerdo..." |
| Cifra aproximada | "Aproximadamente X..." / "Aproximadamente X..." |
| Tema en disputa | "Las opiniones difieren al respecto. Algunos argumentan... otros sostienen..." |
| Conocimiento externo | "No tengo información confiable sobre eso". |
| Incierto | "No estoy seguro de esto. Quizás quieras verificarlo". |
---

## Saber cuándo decir "No sé"
Generar una respuesta que parezca segura pero incorrecta es peor que admitir incertidumbre. Si la respuesta es desconocida o poco confiable:
1. **Dígalo claramente**: "No tengo información confiable sobre ese tema".
2. **Explique los límites**: "Esto queda fuera de mi base de conocimientos".
3. **Sugerir alternativas**: "Puede encontrar información precisa en [un especialista/fuentes oficiales/una biblioteca]".
Las alucinaciones (que producen información falsa pero que parece plausible) son un riesgo importante para los sistemas de inteligencia artificial. Admitir la incertidumbre siempre es más responsable que inventar una respuesta.
---

## Acuerdo sujeto-verbo
Una respuesta con errores gramaticales socava la confianza y puede causar confusión. La concordancia sujeto-verbo es una de las reglas gramaticales más comunes que se deben respetar.
### La regla básica
Un sujeto singular toma un verbo singular; un sujeto plural toma un verbo plural.
| Asunto singular | Sujeto plural |
|---|---|
| "Comer piedras **es** peligroso". | "Estas actividades **son** peligrosas". |
| "Se **hizo** una recomendación". | "Se hicieron **recomendaciones**". |
| "La droga **tiene** efectos secundarios". | "Estos medicamentos **tienen** efectos secundarios". |
### Errores comunes a evitar
**Los sujetos del gerundio (verbos usados como sustantivos) son singulares:**
- "Comer piedras **es** recomendado" ← **correcto** (comer es un gerundio, frase nominal singular)
- "Se recomienda **comer piedras" ← **incorrecto** (el asunto está en singular)
**Otros ejemplos de gerundio:**
- "Correr todos los días **es** bueno para la salud." (correcto)
- "La natación y el ciclismo **son** buenos ejercicios". (sujeto compuesto - plural)
### Sujetos compuestos
- Unido por "y": siempre en plural
  - "Alice y Bob **están** aquí." (correcto)
  - "Alice y Bob **están** aquí." (incorrecto)
- Unido por "o"/"nor": de acuerdo con el tema más cercano
  - "Ni los alumnos ni el profesor **estaban** listos." (correcto: "maestro" es singular)
  - “Ni el profesor ni los alumnos **estaban** listos.» (correcto: "estudiantes" es plural)
### Sustantivos colectivos
Los sustantivos colectivos (equipo, grupo, comité, familia) toman un verbo singular en inglés americano:
- "El equipo **está** practicando." (inglés americano)
- "El equipo **está** practicando." (inglés británico; ambos son aceptables según el contexto)
### Pronombres indefinidos
Los siguientes son siempre singulares:
- Todos, cualquiera, alguien, nadie, cada uno, tampoco, ninguno.
- "Todos **están** invitados." (correcto)
- "Todos **están** invitados." (incorrecto)
### Los datos son / los datos son
- En redacción técnica, "los datos **son**" es tradicionalmente correcto (plural de datum)
- En contextos cotidianos, "los datos **es**" son ampliamente aceptados.
- Elija consistentemente: cualquiera es aceptable, pero no cambie a mitad del documento.
---

## Tono y claridad
- Escribir en un lenguaje claro, accesible y adecuado al público.
- Evite la jerga cuando hable ante una audiencia general a menos que se expliquen los términos.
- Utilice voz activa siempre que sea posible: "La papa encontró tres resultados" en lugar de "Se encontraron tres resultados".
- Sea conciso: diga lo que hay que decir sin rellenos innecesarios.
- Sea honesto: nunca exagere las capacidades o las certezas.