<!--
---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
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
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
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
# Estructuras de datos y algoritmos
Las estructuras de datos son las formas en que organizamos los datos en la memoria para que las operaciones sobre ellos sean eficientes. Los algoritmos son procedimientos paso a paso para resolver problemas. Juntos, forman la base de la informática: todos los programas que haya utilizado se basan en ellos. Elegir la estructura de datos correcta puede convertir un programa increíblemente lento en uno rápido, y conocer el algoritmo correcto puede convertir un problema sin solución en uno trivial.
---

## Estructuras de datos fundamentales
### Estructuras lineales
| Estructura | Acceso | Buscar | Insertar | Eliminar | Caso de uso |
|-----------|--------|--------|--------|--------|----------|
| **Matriz** | O(1) por índice | O(n) | O(n) | O(n) | Colecciones de tamaño fijo; acceso aleatorio |
| **Lista enlazada** | O(n) | O(n) | O(1) en la cabecera | O(1) en la cabecera | Tamaño dinámico; inserciones/eliminaciones |
| **Pila** | O(n) | O(n) | O(1) empujar/pop | O(1) pop | Llamadas a funciones; deshacer; análisis |
| **Cola** | O(n) | O(n) | O(1) poner en cola | O(1) sacar de la cola | Programación de tareas; BFS; colas de mensajes |
| **Deque** | O(1) en ambos extremos | O(n) | O(1) en ambos extremos | O(1) en ambos extremos | ventana corredera; robo de trabajo |
### Estructuras basadas en hash
| Estructura | Buscar | Insertar | Eliminar | Caso de uso |
|-----------|--------|--------|--------|----------|
| **Tabla hash** | O(1) promedio | O(1) promedio | O(1) promedio | Búsquedas de valores clave; cachés; conjuntos |
| **Conjunto de hash** | O(1) | O(1) | O(1) | Pruebas de membresía; deduplicación |
**Colisiones de hash**: cuando dos claves se conectan a la misma ranura, se almacenan en una lista vinculada (encadenamiento) o en la siguiente ranura disponible (direccionamiento abierto). Las buenas funciones hash minimizan las colisiones.
### Estructuras de árboles
| Estructura | Buscar | Insertar | Eliminar | Caso de uso |
|-----------|--------|--------|--------|----------|
| **Árbol de búsqueda binaria** | O(log n) promedio | O(log n) | O(log n) | Datos ordenados; consultas de rango |
| **AVL / Árbol Rojo-Negro** | O(log n) garantizado | O(log n) | O(log n) | Autoequilibrio; utilizado en mapas/conjuntos |
| **Árbol B / Árbol B+** | O(log n) | O(log n) | O(log n) | Índices de bases de datos; sistemas de archivos |
| **Intenta** | O(k) donde k = longitud de la clave | O(k) | O(k) | Autocompletar; coincidencia de prefijos |
| **Montón (binario)** | O(n) | O(log n) | O(log n) | Colas prioritarias; programación |
### Representaciones gráficas
| Representación | Espacio | Búsqueda de bordes | Agregar borde | Iterar vecinos |
|---------------|-------|-------------|----------|-------------|
| **Matriz de adyacencia** | O(V²) | O(1) | O(1) | O(V) |
| **Lista de adyacencia** | O(V + mi) | O(grado) | O(1) | O(grado) |
| **Lista de bordes** | O(E) | O(E) | O(1) | O(E) |
---

## Complejidad del algoritmo (Big-O)
La notación Big-O describe cómo crecen los requisitos de tiempo o espacio de un algoritmo a medida que aumenta el tamaño de entrada.
| Complejidad | Nombre | Ejemplo |
|-----------|------|---------|
| **O(1)** | Constante | Búsqueda de tabla hash; acceso a la matriz por índice |
| **O(log n)** | Logarítmico | Búsqueda binaria; operaciones de árboles equilibrados |
| **O(n)** | Lineal | Búsqueda lineal; iterando una matriz |
| **O(n iniciar sesión n)** | Linearítmica | Combinar clasificación; clasificación de montón; tipos de uso general más eficientes |
| **O(n²)** | Cuadrático | Clasificación de burbujas; bucles anidados sobre los mismos datos |
| **O(2^n)** | Exponencial | Generación de subconjuntos de fuerza bruta; ingenuo recursivo Fibonacci |
| **O(n!)** | Factoriales | Vendedor ambulante (fuerza bruta); permutaciones |
### Conceptos erróneos comunes
| Concepto erróneo | Realidad |
|--------------|---------|
| "O(n) siempre es más rápido que O(n²)" | Para n pequeño, el factor constante importa más |
| "Lower Big-O siempre es mejor" | Existen compensaciones espacio-temporales; La búsqueda O(1) utiliza memoria O(n) |
| "Big-O te dice la velocidad exacta" | Describe la tasa de crecimiento, no el tiempo absoluto |
---

## Algoritmos de clasificación
| Algoritmo | Mejor | Promedio | Peor | Espacio | Estable | En el lugar |
|-----------|------|---------|-------|-------|--------|----------|
| **Clasificación de burbujas** | O(n) | O(n²) | O(n²) | O(1) | Sí | Sí |
| **Clasificación por inserción** | O(n) | O(n²) | O(n²) | O(1) | Sí | Sí |
| **Clasificación por selección** | O(n²) | O(n²) | O(n²) | O(1) | No | Sí |
| **Combinar orden** | O(norte Iniciar sesiónnorte) | O(norte Iniciar sesiónnorte) | O(norte Iniciar sesiónnorte) | O(n) | Sí | No |
| **Clasificación rápida** | O(norte Iniciar sesiónnorte) | O(norte Iniciar sesiónnorte) | O(n²) | O(log n) | No | Sí |
| **Clasificación de montón** | O(norte Iniciar sesiónnorte) | O(norte Iniciar sesiónnorte) | O(norte Iniciar sesiónnorte) | O(1) | No | Sí |
| **Tiempo ordenar** | O(n) | O(norte Iniciar sesiónnorte) | O(norte Iniciar sesiónnorte) | O(n) | Sí | No |
**Consejos prácticos**: utilice la clasificación integrada de su idioma (`sorted()` de Python,`Array.sort()`de JavaScript). Utilizan algoritmos altamente optimizados (Tim Sort, Introsort) que manejan todos los casos extremos.
---

## Algoritmos de búsqueda
| Algoritmo | Estructura de datos | Complejidad | Requisito |
|-----------|---------------|-----------|-------------|
| **Búsqueda lineal** | Cualquiera | O(n) | Ninguno |
| **Búsqueda binaria** | Matriz ordenada | O(log n) | Los datos deben estar ordenados |
| **Búsqueda de tabla hash** | Tabla hash | O(1) promedio | Buena función hash |
| **BFS** (Búsqueda primero en amplitud) | Gráfico/árbol | O(V + mi) | Camino más corto no ponderado |
| **DFS** (Búsqueda en profundidad) | Gráfico/árbol | O(V + mi) | Búsqueda de caminos; detección de ciclos |
| **Dijkstra** | Gráfico ponderado | O((V + E) Iniciar sesión V) | Pesos no negativos; camino más corto |
| **A* Búsqueda** | Gráfico ponderado | O((V + E) Iniciar sesión V) | Guiado heurístico; óptimo con heurística admisible |
---

## Patrones de algoritmos clave
| Patrón | Descripción | Problemas de ejemplo |
|---------|-------------|-----------------|
| **Divide y vencerás** | Dividir el problema en subproblemas; resolver recursivamente; combinar | Combinar clasificación; clasificación rápida; búsqueda binaria |
| **Programación dinámica** | Dividase en subproblemas superpuestos; resultados de caché | Fibonacci; mochila; subsecuencia común más larga |
| **Codicioso** | Haga la elección localmente óptima en cada paso | el de Dijkstra; codificación de Huffman; selección de actividades |
| **Retroceder** | Pruebe posibilidades; deshacer malas decisiones; prueba alternativas | solucionador de sudokus; N-reinas; permutaciones |
| **Ventana corredera** | Mantener una ventana de elementos; deslízalo por los datos | Subarreglo de suma máxima de tamaño K; subcadena más larga sin repeticiones |
| **Dos consejos** | Utilice dos punteros que se muevan uno hacia el otro o en la misma dirección | Suma de pares en una matriz ordenada; eliminar duplicados |
| **Búsqueda binaria por respuesta** | Búsqueda binaria en el espacio de respuesta | Asignar páginas mínimas; vacas agresivas |
---

## Cuándo usar qué
| Problema | Estructura de datos | Algoritmo |
|---------|---------------|-----------|
| Búsqueda rápida de valores-clave | Tabla hash/diccionario | Hash |
| Mantener orden ordenado | BST equilibrado (TreeMap, std::set) | Operaciones de árboles |
| Procesamiento basado en prioridades | Montón/cola de prioridad | Operaciones de montón |
| Ruta más corta (no ponderada) | Gráfico (lista de adyacencia) | BFS |
| Ruta más corta (ponderada) | Gráfico (lista de adyacencia) | Dijkstra / A* |
| Pruebas de membresía | Conjunto de hash/filtro Bloom | Hash |
| Coincidencia de prefijos | Intenta | Trie recorrido |
| Consultas de rango | Árbol de segmentos/árbol de Fenwick | Operaciones de árboles |
| Caché LRU | Mapa hash + lista doblemente enlazada | Operaciones combinadas |
| Componentes conectados | Unión de conjuntos disjuntos (Unión-Buscar) | Unión y Encontrar |
---

## Resumen
Las estructuras de datos y los algoritmos no son sólo temas de entrevista: son los componentes básicos de un software eficiente. Las matrices y las tablas hash satisfacen la mayoría de las necesidades cotidianas. Los árboles y gráficos manejan datos jerárquicos y relacionales. La clasificación y la búsqueda son problemas resueltos en las bibliotecas estándar. Los patrones algorítmicos (divide y vencerás, programación dinámica, avaricia, retroceso) son estrategias reutilizables para abordar nuevos problemas. La habilidad clave no es memorizar algoritmos; se trata de reconocer qué patrón se ajusta a un problema determinado y elegir la estructura de datos adecuada para el trabajo.