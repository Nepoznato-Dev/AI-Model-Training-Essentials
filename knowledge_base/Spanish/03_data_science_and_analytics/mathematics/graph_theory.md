---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teoría de grafos
Un **gráfico** es una estructura matemática que consta de vértices (nodos) conectados por aristas (enlaces). Los gráficos modelan relaciones: redes sociales, mapas de carreteras, redes neuronales, dependencias, canales de comunicación. La teoría de grafos (el estudio de estas estructuras) proporciona algoritmos y teoremas que son fundamentales para la informática, la investigación de operaciones y la ciencia de datos.
---

## Conceptos fundamentales
### Definiciones
| Término | Definición | Notación |
|------|------------|----------|
| **Gráfico** | Un par G = (V, E) de vértices y aristas | GRAMO |
| **Vértice (nodo)** | Un elemento de V | v, u, w |
| **Borde** | Una conexión entre dos vértices | mi = (u, v) o {u, v} |
| **Pedido** | Número de vértices | \|V\| = norte |
| **Tamaño** | Número de aristas | \|E\| = metro |
| **Título** | Número de aristas incidentes en un vértice | grados(v) |
| **Ruta** | Secuencia de distintos vértices conectados por aristas | v₁, v₂, ..., vₖ |
| **Ciclo** | Un camino que comienza y termina en el mismo vértice | v₁ → v₂ → ... → vₖ → v₁ |
| **Conectado** | Existe un camino entre cada par de vértices | — |
| **Componente** | Un subgrafo máximo conectado | — |
| **Subgrafo** | Un gráfico formado a partir de un subconjunto de V y E | H ⊆ GRAMO |
### Tipos de gráficos
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **No dirigido** | Los bordes no tienen dirección | Red de amistad |
| **Dirigido (dígrafo)** | Las aristas tienen dirección (arcos) | Enlaces a páginas web |
| **Ponderado** | Los bordes llevan valores numéricos | Distancias por carretera |
| **Sin ponderar** | Todas las aristas son equivalentes | Conexiones sociales |
| **Sencillo** | Sin bucles, sin múltiples bordes | La mayoría de los gráficos de libros de texto |
| **Múltigrafo** | Se permiten múltiples aristas entre los mismos vértices | Rutas de vuelo (múltiples vuelos entre ciudades) |
| **Completo** | Cada par de vértices está conectado | Kₙ tiene n(n−1)/2 aristas |
| **Bipartito** | Los vértices se dividen en dos grupos; bordes sólo cruzan grupos | Matrices de recomendación de elementos de usuario |
| **Plano** | Se puede dibujar sin cruces de bordes | Diseños de placas de circuito |
| **Árbol** | Gráfico conectado y acíclico | Árboles de decisión, sistemas de archivos |
| **DAG** | Ciclos dirigidos, no dirigidos | Programación de tareas, gráficos de dependencia |
### El lema del apretón de manos
La suma de todos los grados de los vértices es igual al doble del número de aristas:
Σᵥ grados(v) = 2|E|
**Corolario:** Cada gráfico tiene un número par de vértices de grado impar.
**Ejemplo:** En un grupo de 10 personas donde todos dan la mano a exactamente 3 personas más: Σ deg = 30, entonces |E| = 15 apretones de manos en total.
---

## Representaciones gráficas
La forma en que se almacena un gráfico en la memoria determina la eficiencia de cada algoritmo que se ejecuta en él.
| Representación | Espacio | Búsqueda de bordes | Iterar vecinos | Mejor para |
|----------------|-------|-------------|--------------------|----------|
| **Matriz de adyacencia** | O(n²) | O(1) | O(n) | Gráficos densos, pruebas de borde rápidas |
| **Lista de adyacencia** | O(norte + metro) | O(grados(v)) | O(grados(v)) | Gráficos dispersos, la mayoría de las redes del mundo real |
| **Lista de bordes** | O(metro) | O(metro) | O(metro) | Algoritmos simples, MST de Kruskal |
| **Matriz de incidencia** | O(n·m) | O(metro) | O(metro) | Algoritmos especializados |
### Matriz de adyacencia
Una matriz A de n × n donde A[i][j] = 1 si existe el borde (i,j), 0 en caso contrario. Para gráficos ponderados, A[i][j] = peso.
**Propiedades:**
- Simétrico para gráficos no dirigidos.
- Aᵏ[i][j] = número de recorridos de longitud k desde i hasta j
- Los valores propios de A revelan propiedades estructurales (ver Teoría de grafos espectrales)
### Lista de adyacencia
Una matriz (o mapa hash) donde cada vértice v almacena una lista de sus vecinos.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Esta es la representación más común de gráficos del mundo real, que suelen ser escasos (m ≪ n²).
---

## Árboles
Un **árbol** es un gráfico no dirigido, acíclico y conectado. Un **bosque** es una unión inconexa de árboles.
### Propiedades de los árboles
Para un árbol con n vértices:
- Tiene exactamente n − 1 aristas
- Hay exactamente un camino entre dos vértices cualesquiera.
- Quitar cualquier borde lo desconecta
- Agregar cualquier borde crea exactamente un ciclo
### Tipos de árboles
| Tipo | Descripción | Solicitud |
|------|-------------|-------------|
| **Árbol enraizado** | Un vértice designado como raíz | Sistemas de archivos, organigramas |
| **Árbol binario** | Cada nodo tiene como máximo 2 hijos | BST, análisis de expresiones, árboles de decisión |
| **Árbol equilibrado** | La altura es O (log n) | Árboles AVL, árboles rojo-negros (bases de datos) |
| **Árbol de expansión** | Subgrafo que incluye todos los vértices y es un árbol | Diseño de redes, algoritmos de aproximación |
| **Árbol de expansión mínimo** | Árbol de expansión con peso total mínimo en los bordes | Diseño de redes, clustering |
| **Gráfico de estrellas** | Un nodo central conectado a todos los demás | Redes radiales |
### Propiedades del árbol binario
| Propiedad | Fórmula |
|----------|---------|
| Nodos máximos en profundidad d | 2ᵈ |
| Máx. de nodos en árbol de altura h | 2ʰ⁺¹ − 1 |
| Altura mínima para n nodos | ⌊log₂(n)⌋ |
| Nodos hoja en árbol binario completo | Nodos internos + 1 |
### Recorridos de árboles
| transversal | Orden | Caso de uso |
|-----------|-------|----------|
| **Reserva** | Raíz → Izquierda → Derecha | Copiar un árbol, expresión de prefijo |
| **En orden** | Izquierda → Raíz → Derecha | Salida ordenada de BST |
| **Post-pedido** | Izquierda → Derecha → Raíz | Eliminar un árbol, expresión postfix |
| **Orden de niveles (BFS)** | Nivel por nivel, de izquierda a derecha | Camino más corto en árbol no ponderado |
---

## Recorridos de gráficos
Los algoritmos transversales visitan sistemáticamente todos los vértices alcanzables.
### Búsqueda en amplitud (BFS)
Explora los vértices capa por capa, usando una **cola**.
| Propiedad | Valor |
|----------|-------|
| Estructura de datos | Cola (FIFO) |
| Complejidad del tiempo | O(V + mi) |
| Complejidad espacial | O(V) |
| ¿Encuentra el camino más corto? | Sí (gráficos no ponderados) |
| ¿Completo? | Sí (explora todos los vértices alcanzables) |
**Algoritmo:**
1. Comience en los vértices de origen. Mark ha visitado. Poner en cola s.
2. Mientras la cola no esté vacía: retire el vértice u de la cola. Para cada vecino no visitado v de u: marcar v visitado, poner en cola v.
**Aplicaciones:** ruta más corta en gráficos no ponderados, componentes conectados, pruebas de bipartición, rastreo web.
### Búsqueda en profundidad (DFS)
Explora lo más profundo posible antes de retroceder, usando una **pila** (o recursividad).
| Propiedad | Valor |
|----------|-------|
| Estructura de datos | Pila (LIFO) / recursividad |
| Complejidad del tiempo | O(V + mi) |
| Complejidad espacial | O(V) |
| ¿Encuentra el camino más corto? | No |
| ¿Completo? | Sí (para gráficos finitos) |
**Algoritmo:**
1. Comience en el vértice s. Mark ha visitado.
2. Para cada vecino no visitado v de s: recursivamente DFS desde v.
**DFS clasifica los bordes en:**
- **Bordes del árbol:** parte del árbol DFS
- **Bordes posteriores:** conecta un vértice con su ancestro (indica ciclos)
- **Aristas anteriores:** conecta un vértice con su descendiente
- **Aristas cruzadas:** conecta vértices en diferentes ramas
**Aplicaciones:** clasificación topológica, detección de ciclos, componentes fuertemente conectados, resolución de laberintos.
### Comparación entre BFS y DFS
| Criterio | BFS | DFS |
|-----------|-----|-----|
| Estrategia | Amplio y luego profundo | Profundo y luego ancho |
| Memoria | Superior (frontera de tiendas) | Inferior (ruta de tiendas) |
| Ruta más corta (no ponderada) | Garantizado | No garantizado |
| Úselo cuando la solución esté cerca de comenzar | Mejor | Peor |
| Usar cuando el gráfico es muy profundo | Peor | Mejor |
| Clasificación topológica | Variante del algoritmo de Kahn | Enfoque estándar |
---

## Algoritmos de ruta más corta
Encontrar el camino más corto entre los vértices es uno de los problemas gráficos más importantes en la práctica.
### Algoritmo de Dijkstra
Encuentra las rutas más cortas desde una única fuente hasta todos los demás vértices en un gráfico con pesos de borde **no negativos**.
| Propiedad | Valor |
|----------|-------|
| Pesos de borde | Debe ser ≥ 0 |
| Tiempo (montón binario) | O((V + E) Iniciar sesión V) |
| Tiempo (montón de Fibonacci) | O(E + V Iniciar sesión V) |
| ¿Avaro? | Sí |
| ¿Maneja pesos negativos? | No |
**Algoritmo:**
1. Inicialice dist[s] = 0, dist[v] = ∞ para todos v ≠ s. Cola de prioridad Q con todos los vértices.
2. Mientras Q no esté vacío: extraiga el vértice u con una distancia mínima. Para cada vecino v de u con peso de borde w: si dist[u] + w < dist[v], actualice dist[v] = dist[u] + w.
**Ejemplo resuelto:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Algoritmo Bellman-Ford
Maneja pesos de borde **negativos** y detecta ciclos negativos.
| Propiedad | Valor |
|----------|-------|
| Pesos de borde | Cualquiera (detecta ciclos negativos) |
| Complejidad del tiempo | O(V·E) |
| Complejidad espacial | O(V) |
| ¿Maneja los ciclos negativos? | Sí (detecta e informa) |
**Algoritmo:**
1. Inicialice dist[s] = 0, dist[v] = ∞ para todos v ≠ s.
2. Repita V − 1 veces: para cada borde (u, v) con peso w: si dist[u] + w < dist[v], actualice dist[v].
3. Compruebe si hay ciclos negativos: si aún se puede relajar algún borde, existe un ciclo negativo.
### Algoritmo Floyd-Warshall
Encuentra caminos más cortos entre **todos los pares** de vértices.
| Propiedad | Valor |
|----------|-------|
| Complejidad del tiempo | O(V³) |
| Complejidad espacial | O(V²) |
| ¿Maneja pesos negativos? | Sí (pero no ciclos negativos) |
| Enfoque | Programación dinámica |
**Recurrencia:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) para cada vértice intermedio k.
### Guía de selección de algoritmos
| Escenario | Algoritmo |
|----------|-----------|
| Pesos no negativos de fuente única | Dijkstra |
| Fuente única, posibles ponderaciones negativas | Bellman-Ford |
| Todos los pares, gráfico denso | Floyd-Warshall |
| Todos los pares, gráfico disperso | Ejecute Dijkstra desde cada vértice |
| Gráfico no ponderado | BFS |
| DAG (sin ciclos) | Clasificación topológica + relajación |
| A* (guiado por heurística) | Búsqueda A* (para encontrar caminos con buena heurística) |
---

## Árboles de expansión mínima
Un **árbol de expansión mínima (MST)** conecta todos los vértices con un peso total mínimo de borde.
### Propiedades
- Un MST tiene exactamente n − 1 aristas (para n vértices)
- Existe un MST si el gráfico está conectado
- Un gráfico con pesos de borde distintos tiene un MST único
- MST satisface la **propiedad de corte**: el borde de peso mínimo que cruza cualquier corte pertenece al MST
- MST satisface la **propiedad del ciclo**: el borde de peso máximo en cualquier ciclo no pertenece al MST
### Algoritmo de Kruskal
| Propiedad | Valor |
|----------|-------|
| Estrategia | Codicioso: agregue bordes en orden de peso |
| Estructura de datos | Conjunto disjunto (unión-hallazgo) |
| Complejidad del tiempo | O(E Iniciar sesión E) |
| Lo mejor para | Gráficos dispersos |
**Algoritmo:**
1. Clasifique todos los bordes por peso.
2. Para cada borde (en orden): si agregarlo no crea un ciclo (verifique con union-find), agréguelo al MST.
3. Deténgase cuando se seleccionen n − 1 aristas.
### Algoritmo de Prim
| Propiedad | Valor |
|----------|-------|
| Estrategia | Codicioso: hacer crecer un árbol desde un vértice inicial |
| Estructura de datos | Cola de prioridad (montón mínimo) |
| Complejidad del tiempo | O(E log V) con montón binario |
| Lo mejor para | Gráficos densos |
**Algoritmo:**
1. Empiece desde cualquier vértice. Márquelo como parte del MST.
2. Agregue repetidamente el borde de peso mínimo que conecta un vértice en el MST con un vértice fuera de él.
3. Deténgase cuando todos los vértices estén incluidos.
### Aplicaciones MST
| Solicitud | Cómo ayuda MST |
|-------------|---------------|
| Diseño de redes | Coloque un mínimo de cable/tubería para conectar todas las ubicaciones |
| Agrupación | Elimine los k − 1 bordes MST más largos para obtener k grupos |
| Algoritmos de aproximación | 2-aproximación para TSP métrico |
| Segmentación de imágenes | Agrupar píxeles por MST de similitud de color |
| Eliminación de funciones | Eliminar funciones redundantes utilizando MST del gráfico de correlación |
---

## Flujo de red
Los problemas de flujo de red modelan el movimiento de recursos a través de un sistema.
### Definición de red de flujo
Una **red de flujo** es un gráfico dirigido con:
- Un vértice **fuente** (produce flujo)
- Un vértice **sumidero** (consume flujo)
- **Capacidades** c(u,v) ≥ 0 en cada borde
- **Flujo** f(u,v) satisfactorio:
  - **Restricción de capacidad:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Conservación del flujo:** flujo de entrada = flujo de salida en cada vértice excepto s y t
### Problema de flujo máximo
Encuentre el flujo total máximo de s a t.
**Método Ford-Fulkerson:**
1. Si bien existe una ruta creciente de s a t en el gráfico residual:
2. Encuentre la capacidad del cuello de botella a lo largo del camino.
3. Aumentar el flujo a lo largo del camino en la cantidad del cuello de botella.
4. Actualizar las capacidades residuales
| Algoritmo | Complejidad del tiempo | Notas |
|-----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) donde f* es el flujo máximo | No puede terminar con capacidades irracionales |
| Edmonds-Karp (BFS) | O(V·E²) | Siempre termina, elige el camino de aumento más corto |
| Algoritmo de Dinic | O(V²·E) | Utiliza flujos de bloqueo; O(V^(1/2) · E) para capacidades unitarias |
### Teorema de corte mínimo de flujo máximo
El **flujo máximo** de s a t es igual a la capacidad de **corte mínimo** que separa s de t.
Un **corte** (S, T) divide los vértices en S (que contiene s) y T (que contiene t). La capacidad de corte es la suma de las capacidades de los bordes de S a T.
**Aplicaciones de flujo máximo:**
- Coincidencia bipartita (asignar trabajadores a puestos de trabajo)
- Segmentación de imágenes (separar el primer plano del fondo)
- Eliminación de béisbol (¿aún puede ganar el equipo X?)
- Fiabilidad de la red (rendimiento máximo de datos)
### Coincidencia bipartita a través de Max Flow
Dado un gráfico bipartito G = (L ∪ R, E):
1. Agregue fuentes con aristas a todos los vértices en L (capacidad 1)
2. Agregue el fregadero t con aristas de todos los vértices en R (capacidad 1)
3. Establezca todas las capacidades de los bordes originales en 1.
4. Caudal máximo = coincidencia máxima
---

## Teoría de gráficos espectrales
La teoría de grafos espectrales estudia gráficas a través de los valores propios y vectores propios de matrices asociadas con la gráfica.
### Matrices clave
| Matriz | Definición | Lo que captura |
|--------|------------|------------------|
| **Matriz de adyacencia** A | A[i][j] = 1 si existe el borde (i,j) | Patrón de conectividad |
| **Matriz de grados** D | Diagonal; D[i][i] = grados(i) | Importancia del vértice por grado |
| **Laplaciano** L = D − A | L[i][j] = −1 si borde, grados(i) en diagonal | Suavidad de funciones en el gráfico |
| **Laplaciano normalizado** L_norm = D^(−1/2) L D^(−1/2) | Versión invariante de escala | Estructura comunitaria |
### Valores propios del laplaciano
El Laplaciano L es semidefinido positivo, por lo que todos los valores propios son ≥ 0.
| Valor propio | Significado |
|------------|---------|
| λ₁ = 0 | Siempre cero; vector propio es el vector constante |
| λ₂ (conectividad algebraica) | > 0 si el gráfico está conectado; más grande = mejor conectado |
| Número de valores propios cero | Igual al número de componentes conectados |
| λₙ | Relacionado con el grado máximo y la expansión del gráfico |
### Aplicaciones de los métodos espectrales
| Solicitud | Método |
|-------------|--------|
| **Partición de gráficos** | Utilice vectores propios de L para dividir el gráfico en partes equilibradas |
| **Detección comunitaria** | Agrupación espectral: incruste vértices utilizando vectores propios inferiores, luego agrupe |
| **PageRank** | Vector propio de la matriz de adyacencia (o matriz de transición) del gráfico web |
| **Dibujo gráfico** | Coloque los vértices utilizando vectores propios del laplaciano |
| **Aprendizaje semi-supervisado** | Propagar etiquetas usando el gráfico Laplaciano (propagación de etiquetas) |
| **Graficar redes neuronales** | Convoluciones espectrales: filtrar señales en gráficos utilizando vectores propios de L |
### Desigualdad de Cheeger
Relaciona el segundo valor propio λ₂ con la **expansión** del gráfico (qué tan bien conectado está):
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
donde h(G) es la constante de Cheeger (número isperimétrico). Esto significa que λ₂ mide aproximadamente qué tan difícil es cortar el gráfico en dos partes, una idea clave para la agrupación.
---

## Estructuras gráficas especiales
| Gráfico | Vértices | Bordes | Propiedades |
|-------|----------|-------|------------|
| Completa Kₙ | norte | norte(norte−1)/2 | Cada par conectado; diámetro 1 |
| Ciclo Cₙ | norte | norte | 2-regulares; conectado |
| Ruta Pₙ | norte | norte-1 | Árbol; diámetro norte −1 |
| Hipercubo Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-regular; diámetro k; bipartito |
| Bipartito completo K_{m,n} | m+n | m·n | Cada vértice de una parte se conecta con todos los de la otra |
| Gráfico de Petersen | 10 | 15 | 3-regulares; diámetro 2; no plano; sin ciclo hamiltoniano |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto gráfico | Solicitud |
|---------------|-------------|
| BFS/DFS | Rastreo web, análisis de redes sociales, etiquetado de componentes conectados |
| Dijkstra/A* | Planificación de rutas, búsqueda de rutas con IA de juegos, navegación robótica |
| Árbol de expansión mínimo | Agrupación (enlace único), selección de funciones, diseño de redes |
| Flujo máximo/corte mínimo | Segmentación de imágenes, coincidencia bipartita, asignación de recomendaciones |
| Métodos espectrales | Agrupación espectral, redes neuronales gráficas, reducción de dimensionalidad (mapas propios laplacianos) |
| Rango de página | Ranking en buscadores, análisis de influencia en redes sociales |
| DAG | Redes bayesianas, inferencia causal, programación de tareas, gráficos de cálculo en aprendizaje profundo |
| Gráficos bipartitos | Matrices de elementos de usuario en sistemas de recomendación, mercados bilaterales |
| Estructuras de árboles | Árboles de decisión, bosques aleatorios, agrupamiento jerárquico, navegación por sistemas de archivos |
| Representaciones gráficas | Gráficos de conocimiento (Wikidata, DBpedia), gráficos moleculares (descubrimiento de fármacos), redes de citas |
---

## Resumen
| Tema | Idea central | Algoritmo clave/Resultado |
|-------|-----------|----------------------|
| Fundamentos | Vértices, aristas, grados, caminos | Lema del apretón de manos |
| Representaciones | Cómo almacenar gráficos | Matriz de adyacencia vs lista de adyacencia |
| árboles | Gráficos acíclicos conectados | n vértices → n−1 aristas |
| Recorridos | Exploración sistemática de vértices | BFS (camino más corto), DFS (exploración profunda) |
| Caminos más cortos | Rutas con peso mínimo | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Árbol de expansión mínimo | La forma más barata de conectar todos los vértices | Kruskal's, Prim's |
| Flujo de red | Rendimiento máximo | Ford-Fulkerson, teorema de flujo máximo y corte mínimo |
| Teoría espectral | Los valores propios revelan la estructura | Valores propios laplacianos, agrupamiento espectral |
Podría decirse que la teoría de grafos es la rama de las matemáticas más directamente aplicable a la ciencia de datos moderna. Las redes sociales, los gráficos de conocimiento, las estructuras moleculares, los gráficos de cálculo en marcos de aprendizaje profundo, la resolución de dependencias, los sistemas de recomendación: todos son fundamentalmente problemas de gráficos. Los algoritmos que se tratan aquí no son sólo teóricos; funcionan a escala en los sistemas de producción todos los días.