---
# Metadatos
título: "Matemáticas y Lógica"
descripción: "Matemáticas, lógica, pruebas"
categoría: "Ciencia y análisis de datos"
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
review_by: "Equipo de la base de conocimientos de análisis y ciencia de datos"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [matemáticas, lógica, ciencia-de-datos-y-análisis]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "10 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Matemáticas y Lógica
Las matemáticas no son sólo una materia que se estudia en la escuela: es el sistema operativo subyacente en casi todos los campos técnicos. La física lo utiliza para describir el universo. La informática lo utiliza para diseñar algoritmos. El aprendizaje automático lo utiliza para optimizar los pesos. Las finanzas lo utilizan para valorar el riesgo. No es necesario dominar todas las ramas, pero comprender el panorama y saber dónde aparece cada rama hace que todo lo demás funcione más rápido.
---

## Sistemas numéricos
Antes que nada, es útil comprender los tipos de números con los que está trabajando. Cada capa extiende la anterior para resolver un problema que la capa anterior no pudo.
| Tipo de número | Qué incluye | Por qué se inventó | Ejemplo |
|---|---|---|---|
| Números naturales | 1, 2, 3, 4, ... | Contando cosas | 5 manzanas |
| Números enteros | 0, 1, 2, 3, ... | Representando "nada" | 0 grados |
| Enteros | ..., −2, −1, 0, 1, 2, ... | Deuda, temperatura bajo cero | −15°C |
| Números racionales | pag/q donde q ≠ 0 | Dividiendo las cosas de manera desigual | 1/3, 0,75 |
| Números irracionales | No se puede expresar como fracciones | Diagonales, círculos, crecimiento | √2, π, mi |
| Números reales | Todo racional + irracional | La recta numérica completa | 3.14159... |
| Números imaginarios | Múltiplos de i = √(−1) | Resolviendo x² + 1 = 0 | 3i |
| Números complejos | a + bi (real + imaginario) | Ingeniería eléctrica, mecánica cuántica | 2+3i |
---

## Aritmética y teoría de números
Lo básico: suma, resta, multiplicación, división y las reglas que rigen su orden.
**Orden de operaciones** (PEMDAS/BODMAS): Paréntesis → Exponentes → Multiplicación/División (de izquierda a derecha) → Suma/Resta (de izquierda a derecha).
**Los números primos** (números enteros mayores que 1 sin más divisores que 1 y ellos mismos) son los átomos de la teoría de números. Los primeros: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Por qué los números primos son importantes más allá de la clase de matemáticas: el cifrado moderno (RSA) se basa en el hecho de que multiplicar dos números primos grandes es fácil, pero factorizar el resultado es computacionalmente brutal.
**Operaciones útiles:**
- Factorización prima: 84 = 2² × 3 × 7
- Máximo común divisor (MCD) de 24 y 36: 12
- Mínimo Común Múltiplo (MCM) de 4 y 6: 12
---

## Álgebra
Álgebra es donde dejas de trabajar con números específicos y comienzas a trabajar con *relaciones*. Una variable como`x`no tiene un valor fijo; representa lo que hace que la ecuación sea verdadera.
**La fórmula cuadrática** resuelve ax² + bx + c = 0:
x = (−b ± √(b² − 4ac)) / 2a
**Tipos de funciones comunes y dónde aparecen:**
| Función | Fórmula | Forma | Ejemplo del mundo real |
|---|---|---|---|
| Lineal | y = mx + b | Línea recta | Coste unitario a tanto alzado |
| Cuadrático | y = ax² + bx + c | Parábola | Movimiento de proyectil, distancia de frenado |
| Exponencial | y = a × b² | Rápido crecimiento/decadencia | Interés compuesto, crecimiento demográfico, propagación viral |
| Logarítmico | y = log_b(x) | Crecimiento lento, inverso del exponencial | Escala de decibelios, escala de pH, complejidad del algoritmo |
**Vocabulario clave:**
- **Dominio**: todas las entradas válidas (por ejemplo, no se puede dividir por cero, no se puede tomar √ de un negativo en reales)
- **Rango**: todas las salidas posibles
- **Pendiente** (m): tasa de cambio — "por cada unidad de x, y cambia en m"
- **Intersección**: donde la función cruza un eje
---

## Geometría
La geometría estudia formas, tamaños y relaciones espaciales. Aparece en todas partes: los motores de juegos lo usan para renderizar, la robótica lo usa para planificar rutas, la arquitectura lo usa para el diseño estructural.
**Fórmulas esenciales:**
| Forma | Propiedad | Fórmula |
|---|---|---|
| Triángulo | Suma de ángulos | 180° |
| Cuadrilátero | Suma de ángulos | 360° |
| Círculo | Circunferencia | 2πr |
| Círculo | Área | πr² |
| Esfera | Volumen | (4/3)πr³ |
| Triángulo rectángulo | Teorema de Pitágoras | a² + b² = c² |
**π (pi)** ≈ 3,14159 — la relación entre la circunferencia de cualquier círculo y su diámetro. Aparece en lugares que no se esperaría: probabilidad (distribución normal), ingeniería (procesamiento de señales), incluso la ecuación del principio de incertidumbre de Heisenberg.
---

## Estadística y probabilidad
La estadística es la forma de darle sentido a los datos. Es la diferencia entre "Creo que esto funciona" y "Tengo pruebas de que esto funciona".
**Medidas de tendencia central: lo que es "típico":**
| Medida | Cómo se calcula | Cuándo usarlo |
|---|---|---|
| Media (promedio) | Suma ÷ contar | Elección predeterminada; sensible a valores atípicos |
| Mediana | Valor medio al ordenar | Datos sesgados (por ejemplo, precios de la vivienda, salarios) |
| Modo | Valor más frecuente | Datos categóricos (por ejemplo, color más popular) |
**Medidas de propagación: qué tan "variados" son los datos:**
| Medida | Idea de fórmula | Lo que te dice |
|---|---|---|
| Gama | máximo − mínimo | Spread total, pero sensible a valores atípicos |
| Variación | Desviación cuadrática promedio de la media | En unidades al cuadrado (difícil de interpretar directamente) |
| Desviación estándar | √varianza | Mismas unidades que los datos: la medida de dispersión ideal |
**Conceptos básicos de probabilidad:**
- Varía de 0 (imposible) a 1 (cierto)
- Eventos independientes: P(A y B) = P(A) × P(B)
- Ejemplo: sacar dos 6 seguidos = (1/6) × (1/6) = 1/36
**Distribuciones de probabilidad que encontrarás en ML:**
| Distribución | Qué modela | Ejemplo |
|---|---|---|
| bernoulli | Ensayo único, dos resultados | Un lanzamiento de moneda |
| Binomio | Éxitos en n ensayos | Respuestas correctas en un MCQ de 10 preguntas |
| Normal (gaussiano) | Curva de campana, fenómenos naturales | Alturas, puntuaciones de exámenes, medición de ruido |
| veneno | Eventos en un intervalo fijo | Correos electrónicos por hora, defectos por lote |
**Teorema de Bayes**: actualización de creencias con evidencia:
P(A|B) = P(B|A) × P(A) / P(B)
Esta es la columna vertebral de los filtros de spam, los diagnósticos médicos y los modelos bayesianos de aprendizaje automático. Dice: su creencia actualizada = (qué tan bien se ajusta la evidencia a su hipótesis × su creencia anterior) / qué tan probable es la evidencia en general.
---

## Cálculo
El cálculo estudia *cambio* y *acumulación*. Si el álgebra se ocupa de instantáneas, el cálculo se ocupa de imágenes en movimiento.
**Cálculo diferencial**: tasas de cambio. La derivada f'(x) indica qué tan rápido cambia f en cualquier punto.
| Función f(x) | Derivada f'(x) | Intuición |
|---|---|---|
| xⁿ | n·xⁿâ»¹ | Regla de poder |
| e² | e² | La única función igual a su propia derivada |
| ln(x) | 1/x | La tasa de crecimiento se desacelera a medida que x aumenta |
| pecado(x) | porque(x) | Tasa de cambio de oscilación |
Por qué las derivadas son importantes en ML: el descenso de gradiente, el algoritmo que entrena la mayoría de las redes neuronales, funciona calculando las derivadas de la función de pérdida y avanzando en la dirección que reduce el error.
**Cálculo integral** — acumulación. La integral representa el área bajo una curva. Si las derivadas responden "¿a qué velocidad está cambiando?", las integrales responden "¿cuánto se ha acumulado?"
El **teorema fundamental del cálculo** conecta ambos: la diferenciación y la integración son operaciones inversas.
---

## Lógica y razonamiento
La lógica es el estudio del razonamiento *válido*: no si una conclusión *parece* correcta, sino si *se sigue* de las premisas.
**Razonamiento deductivo** (conclusión garantizada si las premisas son verdaderas):
- Todos los humanos son mortales. Sócrates es humano. → Sócrates es mortal.
**Razonamiento inductivo** (conclusión probable, no garantizada):
- Todos los cisnes que he visto son blancos. → Todos los cisnes probablemente sean blancos. (Pero los cisnes negros existen).
**Falacias lógicas comunes: errores que parecen razonamiento pero no lo son:**
| Falacia | Qué es | Ejemplo |
|---|---|---|
| Ad hominem | Atacar a la persona, no al argumento | "No se puede confiar en su idea política: es joven". |
| Hombre de paja | Tergiversar un argumento para derribarlo | "¿Quiere recortar el gasto militar? ¡Quiere dejarnos indefensos!" |
| Falsa dicotomía | Presentando dos opciones cuando existen más | "O estás con nosotros o contra nosotros". |
| Razonamiento circular | Utilizando la conclusión como premisa propia | "Esta ley es injusta porque es injusta". |
| Apelación a la autoridad | "Es cierto porque lo dijo un experto" | "Esta acción subirá, lo dijo un famoso inversor". |
| Post hoc | Suponiendo que A causó B porque A fue primero | "Tomé este suplemento y luego mi resfriado desapareció. El suplemento me curó". |
---

## Conjuntos
Un **conjunto** es una colección de objetos distintos: la base de las matemáticas modernas.
| Operación | Símbolo | Significado | Ejemplo (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Unión | A∪B | Elementos en cualquier conjunto | {1, 2, 3, 4} |
| Intersección | A∩B | Elementos en ambos conjuntos | {2} |
| Diferencia | A\B | Elementos en A pero no en B | {1, 3} |
| Conjunto vacío | ∅ | No contiene nada | {} |
| Subconjunto | A⊂B | Todos los elementos de A están en B | {1,2} ⊂ {1,2,3} |
La teoría de conjuntos aparece en las bases de datos (las JOIN SQL son esencialmente operaciones de conjuntos), la probabilidad (los eventos son conjuntos de resultados) y la programación (conjuntos, mapas hash).
---

## Bases binarias y numéricas
Las computadoras piensan en binario (base 2): solo 0 y 1. Los humanos piensan en decimal (base 10). Los programadores suelen utilizar hexadecimal (base 16) como una forma compacta de representar binario.
| Base | Dígitos utilizados | Ejemplo | Equivalente decimal |
|---|---|---|---|
| Binario (base 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| decimales (base 10) | 0–9 | 11 | 11 |
| Hexadecimal (base 16) | 0–9, A–F | B | 11 |
| Hexadecimal | 0–9, A–F | A3 | 160 + 3 = 163 |
**Por qué es importante:** cada dato en una computadora (texto, imágenes, audio, video) es, en última instancia, simplemente binario. Un byte (8 bits) puede representar 256 valores distintos. Los colores en CSS (#FF5733), las direcciones de memoria (0x7FFF) y las direcciones IP usan hexadecimal porque comprimen cadenas binarias largas en algo legible.
---

## Álgebra lineal para ML y gráficos
El álgebra lineal (vectores, matrices y transformaciones) es el motor matemático detrás del aprendizaje automático, los gráficos por computadora, las simulaciones físicas y los motores de búsqueda.
**Vectores** son listas ordenadas de números. En ML, cada punto de datos es un vector de características:
- [23, 1.8, 75] podría representar la edad de una persona, su altura en metros y su peso en kg.
**Matrices** son matrices de números 2D. Los pesos de una red neuronal se almacenan como matrices. Un lote de 100 imágenes podría ser una matriz de forma (100, 784): 100 filas, cada una con valores de 784 píxeles.
**Operaciones clave:**
| Operación | Qué hace | Dónde aparece |
|---|---|---|
| Producto escalar | Mide la similitud entre dos vectores | Sistemas de recomendación, similitud coseno |
| Multiplicación de matrices | Combina transformaciones lineales | Cada capa de una red neuronal |
| Valores propios/vectores propios | Direcciones que una matriz escala (no gira) | Reducción de dimensionalidad PCA, PageRank |
| Rango de matriz | Cantidad de información independiente | Compresión, aproximación de rango bajo |
**Similitud del coseno** = (a·b) / (||a|| × ||b||) — varía de −1 (opuesto) a 1 (misma dirección). Así es como los motores de búsqueda miden si dos documentos son "más o menos lo mismo" y cómo los modelos de incrustación comparan la similitud semántica.
---

## Resumen
| Sucursal | Pregunta central | Aplicación clave |
|---|---|---|
| Aritmética y teoría de números | ¿Cómo se comportan los números? | Criptografía, hash |
| Álgebra | ¿Cómo se relacionan las incógnitas? | Modelado, ecuaciones |
| Geometría | ¿Cómo funcionan las formas y los espacios? | Gráfica, robótica, arquitectura |
| Estadística y probabilidad | ¿Qué dicen los datos? | ML, pruebas A/B, análisis de riesgos |
| Cálculo | ¿Cómo cambian las cosas? | Entrenamiento de redes neuronales, física |
| Lógica | ¿Es válido este razonamiento? | Programación, pruebas, análisis de argumentos |
| Teoría de conjuntos | ¿Cómo se relacionan las colecciones? | Bases de datos, probabilidad |
| Álgebra lineal | ¿Cómo funcionan las transformaciones? | ML, gráficos, motores de búsqueda |
No necesitas todo esto el primer día. Pero a medida que profundices en cualquier campo técnico, seguirás volviendo a estos fundamentos. La buena noticia: cada rama tiene mucho más sentido una vez que ves *por qué* se inventó: qué problema intentaba resolver.