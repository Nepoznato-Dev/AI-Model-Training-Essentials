<!--
---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Sesgos cognitivos y falacias lógicas
Este documento consolida los sesgos cognitivos, las falacias lógicas y los errores de razonamiento que afectan tanto la toma de decisiones humana como los resultados del sistema de IA.
---

## Sesgos cognitivos
Los sesgos cognitivos son patrones sistemáticos de desviación de la racionalidad en el juicio y la toma de decisiones. En el desarrollo de software y los sistemas de inteligencia artificial, esto puede conducir a decisiones de diseño deficientes, requisitos defectuosos y comportamiento sesgado del modelo.
### Sesgo de confirmación
**Qué es:** La tendencia a buscar, interpretar y recordar información de una manera que confirme creencias preexistentes.
**Mal ejemplo en desarrollo:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**En revisiones de código:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Mitigación:**
- Buscar activamente pruebas que lo refuten.
- Utilice revisiones de código ciego
- Fomentar opiniones disidentes.
- Documentar los supuestos explícitamente
### Sesgo de anclaje
**Qué es:** Depender demasiado de la primera información encontrada.
**Mal ejemplo:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Mitigación:**
- Obtenga múltiples estimaciones independientes
- Utilice el póquer de planificación para realizar estimaciones.
- Considere rangos en lugar de estimaciones puntuales
- Datos históricos de referencia.
### Falacia del costo hundido
**Qué es:** Continuar un esfuerzo debido a los recursos previamente invertidos (tiempo, dinero, esfuerzo), incluso cuando abandonarlo sería mejor.
**Mal ejemplo:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Mitigación:**
- Evaluar decisiones basadas en el valor futuro, no en inversiones pasadas.
- Reevaluar periódicamente la viabilidad del proyecto.
- Crear seguridad psicológica para pivotar.
- Utilizar criterios objetivos para tomar decisiones de continuar/detener.
### Heurística de disponibilidad
**Qué es:** Sobreestimar la importancia de la información que está disponible o que es reciente.
**Mal ejemplo:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Mitigación:**
- Utilice la toma de decisiones basada en datos.
- Consultar modelos integrales de amenazas.
- Mirar tarifas base y estadísticas.
- Evitar el sesgo de actualidad en la priorización
### Efecto Dunning-Kruger
**Qué es:** Las personas con baja capacidad para realizar una tarea sobreestiman su capacidad; los expertos pueden subestimar los suyos.
**Mal ejemplo:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Mitigación:**
- Fomentar el aprendizaje continuo.
- Implementar procesos de revisión por pares.
- Crear programas de tutoría.
- Fomentar la humildad y la curiosidad.
---

## Falacias lógicas
Las falacias lógicas son errores de razonamiento que socavan la validez de un argumento. Los modelos de IA pueden producir resultados que contengan estas falacias.
### Ad Hominem (Ataque contra la persona)
**Qué es:** Atacar a la persona que presenta un argumento en lugar del argumento en sí.
**Mal ejemplo:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Por qué es malo:** La validez de los comentarios depende de su contenido, no de la antigüedad del revisor.
### Apelación a la autoridad
**Qué es:** Afirmar que algo es cierto porque una figura de autoridad lo dice, sin evidencia.
**Mal ejemplo:**```markdown
"This architecture must be correct because Google uses it."
```

**Por qué es malo:** Lo que funciona para Google a su escala puede no funcionar para su caso de uso.
### Falsa dicotomía (pensamiento en blanco y negro)
**Qué es:** Presentamos solo dos opciones cuando existen más.
**Mal ejemplo:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Realidad:** Existen muchas opciones entre estos extremos (optimizar rutas activas, usar Rust para componentes específicos, mejorar el código Python, etc.)
### Pendiente resbaladiza
**Qué es:** Argumentar que un evento conducirá inevitablemente a una cadena de consecuencias negativas.
**Mal ejemplo:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Por qué es malo:** Asume una progresión inevitable sin evidencia; ignora los factores atenuantes.
### Razonamiento circular
**Qué es:** Usar la conclusión como premisa.
**Mal ejemplo:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (Causa falsa)
**Qué es:** Suponiendo que debido a que B siguió a A, A causó B.
**Mal ejemplo:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Realidad:** La correlación no implica causalidad. Otros factores podrían ser responsables.
### Hombre de paja
**Qué es:** Tergiversar el argumento de alguien para facilitar el ataque.
**Mal ejemplo:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Falacia del carro
**Qué es:** Argumentar que algo es correcto porque mucha gente lo cree.
**Mal ejemplo:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Por qué es malo:** La popularidad no garantiza la idoneidad para sus necesidades específicas.
---

## Fallos de razonamiento en IA
### Errores de lógica de varios pasos
**Mal ejemplo:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Por qué es malo:**
- Comete la falacia de afirmar el consecuente
- Alice podía escribir código sin ser programadora.
- Estructura lógica: (P→Q, Q) ⊬ P
**Razonamiento correcto:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Fallos de razonamiento matemático
**Mal ejemplo:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Realidad:** Si la pelota cuesta $0,10 y el bate cuesta $1 más ($1,10), el total sería $1,20. La respuesta correcta es $0.05 por la pelota y $1.05 por el bate.
### Errores de razonamiento causal
**Mal ejemplo:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Realidad:** Ambos son causados ​​por un tercer factor (el clima cálido), no entre sí.
---

## Estrategias de mejora
### Para la toma de decisiones humana
1. **Capacitación de concientización**: aprenda a reconocer sesgos comunes
2. **Uso de listas de verificación**: utilice listas de verificación de decisiones para contrarrestar los sesgos
3. **Equipos diversos**: incluya personas con diferentes perspectivas
4. **Pre-mortems**: Imagine el fracaso y trabaje hacia atrás para identificar las causas.
5. **Documentación**: Registre el razonamiento para su posterior revisión.
### Para sistemas de IA
1. **Instigadores de cadena de pensamiento**: Pídale al modelo que muestre los pasos de razonamiento
2. **Autocorrección**: Haga que el modelo revise y critique sus respuestas.
3. **Verificación formal**: utilice herramientas de razonamiento simbólico para la lógica crítica
4. **Descomposición**: divide problemas complejos en pasos más pequeños
5. **Herramientas externas**: use calculadoras y solucionadores para tareas matemáticas
6. **Múltiples muestras**: genere múltiples respuestas y compare
---

## Temas relacionados
- **Fallos de AI/LLM**: consulte`ai_llm_failures.md`para alucinaciones y problemas de razonamiento.
- **Fuentes contradictorias**: consulte la documentación sobre la evaluación de información contradictoria.
- **Pensamiento crítico**: aplique estos conceptos para evaluar argumentos y evidencia
- **Ingeniería rápida**: consulte`../02_artificial_intelligence/prompt_engineering.md`para conocer técnicas para reducir los errores de razonamiento.
---

## Sesgos cognitivos adicionales en el desarrollo de software
### Sesgo del statu quo
**Qué es:** Preferencia por mantener el estado actual; cualquier cambio se percibe como una pérdida.
**Mal ejemplo:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Mitigación:**
- Cuantificar los costos de no cambiar.
- Establecer cronogramas de actualización regulares
- Crear entornos de experimentación seguros.
- Enmarcar los cambios como oportunidades, no como amenazas.
### Sesgo de optimismo
**Qué es:** Subestimar el tiempo, los costos y los riesgos y sobreestimar los beneficios.
**Mal ejemplo:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Mitigación:**
- Utilice pronósticos de clase de referencia (compárelos con proyectos anteriores similares)
- Añadir reservas de contingencia (20-50%)
- Realizar autopsias
- Seguimiento de la precisión de la estimación a lo largo del tiempo
### Sesgo de supervivencia
**Qué es:** Centrarse en ejemplos exitosos e ignorar los fracasos.
**Mal ejemplo:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Mitigación:**
- Estudiar tanto los éxitos como los fracasos.
- Busque tarifas base y estadísticas.
- Considere los datos invisibles
- Evite seleccionar ejemplos
### Error de atribución fundamental
**Qué es:** Atribuir el comportamiento de los demás al carácter y no a las circunstancias.
**Mal ejemplo:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Mitigación:**
- Considere los factores situacionales.
- Practica la empatía
- Centrarse en los sistemas, no en los individuos.
- Utilice autopsias inocentes.
### Sesgo retrospectivo
**Qué es:** Después de que ocurre un evento, creer que era predecible desde el principio.
**Mal ejemplo:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Mitigación:**
- Documentar las predicciones antes que los resultados.
- Revisar el contexto de la decisión, no solo los resultados.
- Evita la cultura del "te lo dije"
- Centrarse en mejorar los procesos, no en asignar culpas.
---

## Más falacias lógicas
### Apelación a la novedad
**Qué es:** Suponiendo que algo es mejor porque es más nuevo.
**Mal ejemplo:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Apelación a la tradición
**Qué es:** Argumentar que algo es correcto porque siempre se ha hecho así.
**Mal ejemplo:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Apelación a la hipocresía)
**Qué es:** Descartar las críticas señalando su inconsistencia.
**Mal ejemplo:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Pregunta cargada
**Qué es:** Hacer una pregunta que contenga una suposición.
**Mal ejemplo:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Ningún verdadero escocés
**Qué es:** Hacer una excepción a un reclamo universal cuando se cuestiona.
**Mal ejemplo:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Falacia genética
**Qué es:** Juzgar algo en función de su origen en lugar de su mérito actual.
**Mal ejemplo:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Falacia del término medio
**Qué es:** Suponer que la verdad siempre está en medio de dos extremos.
**Mal ejemplo:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Sesgos cognitivos en los sistemas de IA
### Sesgo de datos de entrenamiento
Los modelos de IA heredan sesgos presentes en sus datos de entrenamiento.
**Ejemplo:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Mitigación:**
- Auditar datos de capacitación para detectar sesgos.
- Utilizar técnicas de desescalamiento.
- Prueba de salidas sesgadas
- Recopilación de datos diversos.
### Sesgo de automatización
**Qué es:** Depender demasiado de sistemas automatizados, incluso cuando están equivocados.
**Ejemplo:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Mitigación:**
- Mantener la supervisión humana.
- Fomentar la evaluación crítica de los resultados de la IA.
- No trates a la IA como infalible
- Implementar procesos de revisión.
### Ilusión de comprensión
**Qué es:** Creer que entiendes cómo funciona una IA cuando no es así.
**Ejemplo:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Mitigación:**
- Educar a los usuarios sobre las limitaciones de la IA.
- Ser transparente sobre cómo funcionan los sistemas.
- Evite antropomorfizar la IA
- Establecer expectativas adecuadas
---

## Estudios de caso
### Estudio de caso 1: Sesgo de confirmación en la selección de arquitectura
**Incidente:** Un equipo eligió una arquitectura de microservicios para una aplicación pequeña.
**Causa raíz:** El líder del equipo había leído varios artículos que elogiaban los microservicios y 
Sólo buscó información que confirmara esta elección, ignorando las advertencias sobre la complejidad.
**Impacto:**
- Gastos generales masivos para un equipo de 3 desarrolladores.
- La complejidad de la implementación aumentó 10 veces.
- Rendimiento degradado debido a llamadas de red
- Proyecto retrasado 6 meses
**Lección:** Evalúe arquitecturas según su contexto específico, no solo 
testimonios positivos. Considere las compensaciones explícitamente.
### Estudio de caso 2: Costo hundido en el sistema heredado
**Incidente:** La empresa continuó manteniendo un CRM personalizado durante 5 años. 
a pesar de mejores alternativas.
**Causa raíz:** "Ya hemos invertido 2 millones de dólares, no podemos abandonarlo ahora".
**Impacto:**
- Costo de mantenimiento anual: $500K
- Costo de oportunidad: no se pudieron utilizar las funciones modernas
- Problemas de retención de talento (los desarrolladores querían trabajar con tecnología moderna)
- Costo total a 5 años: 4,5 millones de dólares frente a 1,5 millones de dólares para la alternativa SaaS
**Lección:** La inversión pasada está perdida. Tomar decisiones basadas en el valor futuro.
### Estudio de caso 3: Heurística de disponibilidad en seguridad
**Incidente:** El equipo dio prioridad a la defensa contra un ataque publicitado recientemente 
vector mientras se ignoran las amenazas más probables.
**Causa principal:** La cobertura de noticias reciente hizo que un tipo de amenaza estuviera altamente disponible 
en la memoria, distorsionando la evaluación de riesgos.
**Impacto:**
- Gastó 100.000 dólares en mitigar amenazas de baja probabilidad
- La infracción real se produjo a través de un vector desatendido
- Costo de recuperación: $500K+
**Lección:** Utilice modelos de amenazas basados ​​en datos, no priorización basada en lo reciente.
---

## Ejercicios prácticos
### Ejercicio de detección de sesgos
Revise las decisiones recientes y pregunte:
1. ¿Qué suposiciones hicimos?
2. ¿Qué evidencia contradiría nuestra conclusión?
3. ¿Consideramos múltiples opciones o nos basamos en la primera idea?
4. ¿Continuamos debido al valor futuro o a la inversión pasada?
5. ¿Qué recomendaríamos si alguien más nos preguntara?
### Detección de falacias lógicas
Practique la identificación de falacias en las discusiones cotidianas:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Técnica premortem
Antes de iniciar un proyecto:
1. Imagina que son 6 meses en el futuro.
2. El proyecto ha fracasado espectacularmente
3. Escribe la historia de por qué falló.
4. Trabajar hacia atrás para evitar esos modos de falla
Esto contrarresta el sesgo de optimismo y la heurística de disponibilidad.
---

## Herramientas y marcos
### Plantilla de diario de decisiones
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Lista de verificación de sesgos
Antes de tomar decisiones importantes:
- [ ] ¿Hemos buscado pruebas que lo refuten?
- [ ] ¿Estamos anclados en la información inicial?
- [ ] ¿Nos está influyendo el coste hundido?
- [ ] ¿Estamos demasiado confiados en nuestras estimaciones?
- [ ] ¿Hemos considerado tarifas base?
- [] ¿Estamos cayendo en el sesgo de disponibilidad/reciente actualidad?
- [ ] ¿Haríamos la misma elección si empezáramos de nuevo?
### Ejercicio del equipo rojo
Asigne a alguien para que argumente en contra de la decisión propuesta:
- Su función es encontrar defectos.
- Deben presentar puntos de vista alternativos.
- Prácticas en equipo respondiendo a las críticas de manera constructiva.
- Documentar las inquietudes planteadas y abordadas
Esto contrarresta el sesgo de confirmación y el pensamiento de grupo.