---
# Metadatos
título: "Ingeniería rápida"
descripción: "Técnicas y estrategias rápidas"
categoría: "IA y aprendizaje automático"
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
review_by: "Equipo de base de conocimientos de inteligencia artificial y aprendizaje automático"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [rápido, ingeniería, inteligencia artificial y aprendizaje automático]
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
# Ingeniería rápida
La ingeniería de indicaciones es la práctica de diseñar, refinar y optimizar las indicaciones de entrada para obtener el mejor resultado posible de un modelo de lenguaje. Es a la vez un arte y una ciencia, y es la interfaz principal para controlar el comportamiento del LLM sin realizar ajustes.
---

## Principios básicos
### Claridad y especificidad
Una indicación clara no deja lugar a ambigüedades. Especifique exactamente lo que desea, incluido el formato, la longitud y la perspectiva.
**Vago:**
> "Háblame de Python."
**Específico:**
> "Explique el bloqueo de intérprete global (GIL) de Python. Describa su impacto en los subprocesos múltiples, proporcione una solución alternativa y mantenga su respuesta en menos de 200 palabras".
### Proporcionar contexto
Los modelos se desempeñan mejor cuando conocen el rol, la audiencia y el objetivo.
**Sin contexto:**
> "Escribir una función para ordenar una lista."
**Con contexto:**
> "Usted es un desarrollador senior de Python. Escriba una función para ordenar una lista de diccionarios según una clave determinada. Utilice sugerencias de escritura y maneje casos extremos. La audiencia son desarrolladores junior".
### Utilice instrucciones positivas
Dígale al modelo qué hacer, no qué evitar. "No incluyas jerga" es más débil que "Utiliza un lenguaje sencillo y accesible para un niño de 10 años".
---

## Estructuras rápidas
### Roles de sistema/usuario/asistente
La mayoría de las API de LLM admiten una estructura de múltiples turnos:
- **Mensaje del sistema**: establece el comportamiento, la personalidad y las restricciones del modelo (persiste durante toda la sesión).
- **Mensaje de usuario**: La consulta o instrucción actual.
- **Mensaje del asistente**: Las respuestas anteriores del modelo (usadas para continuidad).
**Ejemplo (estilo API OpenAI):**
Sistema: eres un útil asistente de codificación. Responde con ejemplos de código concisos y breves explicaciones. Nunca proporciones código inseguro.
Usuario: escriba una función de Python para descargar un archivo desde una URL.
### Indicaciones breves
Proporcione 2 o 3 ejemplos del formato de entrada y salida deseado antes de pedirle al modelo que realice la tarea. Esto enseña el patrón.
**Ejemplo:**
Usuario: Convierta estas oraciones a voz pasiva:
Entrada: El gato persiguió al ratón.
Producción: El ratón fue perseguido por el gato.
Entrada: El chef preparó la comida.
Resultado: La comida fue preparada por el chef.
Entrada: La tormenta destruyó la casa.
Salida: (el modelo se completa)
### Cadena de pensamiento (CoT)
Anime al modelo a mostrar su razonamiento paso a paso. Esto mejora la precisión en tareas aritméticas, lógicas y de varios pasos.
**Sin cuna:**
> "¿Qué es 24 × 37?"
**Con cuna:**
> "Calcula 24×37. Muestra tu razonamiento paso a paso."
El modelo producirá pasos intermedios, reduciendo los errores aritméticos.
### Resultados estructurados
Solicite un formato específico como JSON, YAML o tablas de rebajas para que el análisis sea confiable.
Usuario: enumere tres ventajas y tres desventajas de los microservicios. Devuelve solo un objeto JSON válido con las claves "pros" y "contras", cada una de las cuales es una matriz de cadenas.
---

## Técnicas Avanzadas
### Autoconsistencia
Genere múltiples respuestas para el mismo mensaje (con una temperatura > 0) y vote por mayoría sobre la respuesta final. Esto es especialmente eficaz para tareas de razonamiento.
### Árbol de pensamientos
Explora múltiples caminos de razonamiento en paralelo, evalúa cada uno y elige el mejor. Esta es una técnica a nivel de investigación, pero se puede aproximar pidiendo al modelo que "explore soluciones alternativas".
### ReAct (Razonamiento + Actuación)
Deje que el modelo intercale razonamiento con llamadas a herramientas. Puede pensar, luego actuar (por ejemplo, buscar en la web, ejecutar código) y luego pensar de nuevo según el resultado.
**Estructura de aviso:**
Tienes acceso a una calculadora y un motor de búsqueda. Para cada paso, genere:
Pensamiento: (tu razonamiento)
Acción: (nombre de la herramienta, entrada)
Observación: (salida de la herramienta)
... continúa hasta tener la respuesta final.
### Asignación de persona
Asigne una persona específica para enmarcar la respuesta.
**Ejemplos:**
- "Usted es un desarrollador del kernel de Linux y le explica la gestión de la memoria a un recién graduado".
- "Eres un nutricionista amigable que da consejos generales a un cliente".
- "Eres un crítico tecnológico cínico que revisa un nuevo dispositivo".
---

## Ajuste de parámetros
- **Temperatura** (0.0 – 1.0+): Controla la aleatoriedad. Más bajo = más determinista, más alto = más creativo. Utilice 0,0–0,3 para respuestas objetivas; 0,7–1,0 para escritura creativa.
- **Top-p** (muestreo de núcleos): corta la masa de probabilidad en un cierto umbral acumulativo. 0,9 significa que el modelo toma muestras del 90% superior de tokens probables. Por lo general, ajuste la temperatura o la temperatura máxima, no ambas.
- **Tokens máximos**: establece la longitud máxima de salida. Recuerde reservar espacio para la respuesta dentro de la ventana de contexto.
- **Penalización de frecuencia**: Reduce la repetición de los mismos tokens.
- **Penalización de presencia**: Alienta al modelo a introducir nuevos temas.
---

## Errores y soluciones comunes
| Problema | Causa probable | Arreglar |
|---------|--------------|-----|
| El modelo ignora partes del mensaje | Aviso demasiado largo o sobrecargado | Acortar; poner la instrucción más importante al final |
| La salida es demasiado detallada | Sin restricción de longitud | Agregue "Limitar a 3 oraciones" o configure max_tokens |
| La salida es demasiado concisa | Demasiado restrictivo | Añadir "Explicar en detalle" o bajar la temperatura |
| Alucinaciones reales | Contexto insuficiente o pregunta ambigua | Agregue "Si no está seguro, diga 'No lo sé'" y proporcione un contexto RAG |
| Formato inconsistente | Sin instrucciones de formato explícitas | Solicite JSON, tabla de rebajas o lista con viñetas |
| Respuestas modelo en lenguaje equivocado | Sin instrucción de idiomas | Indique explícitamente "Responder en inglés" (o en su idioma de destino) |
---

## Plantillas de mensajes para tareas comunes
### Resumen
Resume el siguiente texto en 3 viñetas. Céntrese en los argumentos principales y evite los detalles.
Texto: [insertar texto]

### Generación de código
Escribe una función [lenguaje] que [haga X].
Requisitos:
Utilice sugerencias de tipografía.
Incluya una cadena de documentación.
Manejar casos extremos: [lista].
No utilice bibliotecas externas a menos que se especifique.

### Explicación
Explicar [concepto] a un [no experto/estudiante universitario/niño]. Utilice una analogía cuando corresponda.
### Lluvia de ideas
Genera 10 ideas para [tema]. Para cada idea, proporcione una descripción de una oración y un desafío potencial.
texto
### Clasificación
Clasifique los siguientes comentarios de los clientes como [positivos, neutrales, negativos].
Proporcione una puntuación de confianza (0-100) y una breve razón.
Comentarios: [insertar texto]
### Traducción con estilo
Traduce el siguiente texto del inglés al español. Utilice un tono informal adecuado para una publicación en las redes sociales.
Texto: [insertar texto]
---

## Evaluación de indicaciones
Trate las indicaciones como código: versione, pruébelas e itere.
- **Prueba A/B** diferentes variantes de mensajes en un conjunto de consultas pendientes.
- **Mida el éxito** mediante evaluación humana o métricas automatizadas (por ejemplo, coincidencia exacta, BLEU, puntuación personalizada).
- **Mantenga un registro de avisos** (un archivo de texto simple u hoja de cálculo) con el aviso, la versión y el rendimiento observado.
---