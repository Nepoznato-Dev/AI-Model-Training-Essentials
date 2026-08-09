---
# Metadatos
título: "Graficar redes neuronales"
descripción: "GCN, GAT, paso de mensajes, gráficos de conocimiento, tareas de gráficos"
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
Etiquetas: [gráfico, neuronal, redes, inteligencia artificial y aprendizaje automático]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "8 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Graficar redes neuronales
Las redes neuronales gráficas (GNN) son redes neuronales diseñadas para operar con datos estructurados en gráficos: redes de nodos conectados por bordes. Mientras que las redes neuronales tradicionales funcionan en cuadrículas (imágenes) o secuencias (texto), las GNN manejan estructuras relacionales arbitrarias: redes sociales, gráficos moleculares, gráficos de conocimiento, redes de carreteras, gráficos de recomendación y más. Se han vuelto esenciales para el descubrimiento de fármacos, la detección de fraudes, los sistemas de recomendación y cualquier ámbito donde las relaciones entre entidades sean importantes.
---

## ¿Qué es un gráfico?
| Componente | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Nodo (vértice)** | Una entidad | Una persona, el átomo de una molécula, una ciudad |
| **Borde** | Una relación entre dos nodos | Amistad, vínculo químico, camino |
| **Peso del borde** | Fuerza o tipo de relación | Distancia, similitud, capacidad |
| **Características del nodo** | Atributos de cada nodo | Edad, número atómico, población |
| **Características de borde** | Atributos de cada borde | Tipo de relación, distancia |
| **Matriz de adyacencia** | Matriz A donde A[i][j] = 1 si los nodos i y j están conectados | Codifica la estructura del gráfico |
### Tipos de gráficos
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **No dirigido** | Los bordes no tienen dirección | Red de amistad |
| **Dirigida** | Las aristas tienen dirección (A→B ≠ B→A) | Seguidores de Twitter |
| **Ponderado** | Las aristas tienen valores numéricos | Red de carreteras con distancias |
| **Heterogéneo** | Múltiples tipos de nodos y bordes | Gráfico académico (artículos, autores, lugares) |
| **Dinámico** | La estructura del gráfico cambia con el tiempo | Red social evolucionando con el tiempo |
| **Bipartito** | Dos tipos de nodos; bordes sólo entre tipos | Gráfico de recomendación de elementos de usuario |
---

## ¿Por qué no redes neuronales regulares?
| Enfoque | Por qué falla |
|----------|-------------|
| **Red de retroalimentación** | Requiere entrada de tamaño fijo; los gráficos varían en tamaño y estructura |
| **CNN** | Asume estructura de cuadrícula; los gráficos no tienen una cuadrícula regular |
| **RNN/Transformador** | Asume orden secuencial; los gráficos no tienen orden natural |
Los GNN resuelven esto operando directamente sobre la estructura del gráfico, procesando cada nodo en el contexto de sus vecinos.
---

## Arquitecturas principales de GNN
### Marco de paso de mensajes
La mayoría de las GNN siguen el mismo patrón: cada nodo recopila información de sus vecinos, la combina y actualiza su propia representación.
| Paso | Descripción |
|------|-------------|
| **1. Mensaje** | Cada nodo envía un mensaje a sus vecinos (según sus características actuales) |
| **2. Agregado** | Cada nodo recopila y combina mensajes de todos los vecinos |
| **3. Actualización** | Cada nodo actualiza su propia representación utilizando el mensaje agregado |
| **4. Repetir** | Haga esto para K capas → cada nodo captura información de K saltos de distancia |
### Modelos clave de GNN
| Modelo | Método de agregación | Innovación clave |
|-------|-------------------|----------------|
| **GCN** (Red convolucional de gráficos) | Media de las características vecinas | Simple; eficaz; motivación espectral |
| **GráficoSAGE** | Muestra y agregado; puede usar media, LSTM o agrupación | Inductivo (maneja nodos invisibles); escalable |
| **GAT** (Red de atención de gráficos) | Agregación de vecinos ponderada por atención | Aprende qué vecinos son más importantes |
| **GIN** (Red de isomorfismo de gráficos) | Suma de características vecinas | Máximamente expresivo; puede distinguir cualquier gráfico distinguible mediante la prueba WL |
| **MPNN** (Red neuronal de paso de mensajes) | Marco general de paso de mensajes | Unifica muchas variantes de GNN |
### Cómo funciona GCN (paso a paso)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Después de K capas, la representación de cada nodo codifica información de K saltos en el gráfico.
---

## Tareas a nivel de gráfico
| Tarea | Descripción | Ejemplo |
|------|-------------|---------|
| **Clasificación de nodos** | Predecir la etiqueta de cada nodo | Clasificar usuarios como bots o humanos |
| **Predicción de enlaces** | Predecir si existe (o existirá) una ventaja | Predecir relaciones perdidas; recomendar conexiones |
| **Clasificación de gráficos** | Predecir una etiqueta para todo el gráfico | Clasificar moléculas como tóxicas o no tóxicas |
| **Detección comunitaria** | Encuentra grupos de nodos densamente conectados | Identificar grupos sociales |
| **Generación de gráficos** | Generar nuevos gráficos con las propiedades deseadas | Diseñar nuevas moléculas |
---

## Aplicaciones
### Descubrimiento de fármacos y predicción de propiedades moleculares
| Tarea | Cómo ayudan las GNN |
|------|--------------|
| **Predicción de propiedades moleculares** | Representar moléculas como gráficos (átomos=nodos, enlaces=bordes); predecir toxicidad, solubilidad y afinidad de unión |
| **Interacción fármaco-fármaco** | Modelar fármacos y objetivos en forma de gráfico; predecir interacciones adversas |
| **Diseño de fármacos de novo** | Genere nuevos gráficos moleculares con las propiedades deseadas |
### Sistemas de recomendación
| Enfoque | Descripción |
|----------|-------------|
| **Gráfico de elementos de usuario** | Los usuarios y los elementos son nodos; compras/vistas son bordes |
| **Filtrado colaborativo basado en gráficos** | Los GNN propagan preferencias a través del gráfico |
| **Recomendaciones de gráficos de conocimiento** | Combine las preferencias del usuario con el conocimiento del elemento (géneros, actores, directores) |
### Detección de fraude
| Solicitud | Estructura del gráfico |
|-------------|----------------|
| **Fraude financiero** | Las transacciones forman un gráfico; patrones fraudulentos surgen como estructuras de subgrafos |
| **Fraude de seguros** | Los reclamantes, proveedores y pólizas forman un gráfico; se detectan redes de estafadores |
| **Adquisición de cuentas** | Los patrones de inicio de sesión forman un gráfico; conexiones anómalas indican compromiso |
### Gráficos de conocimiento
| Tarea | Descripción |
|------|-------------|
| **Predicción de enlaces** | Predecir hechos faltantes (por ejemplo, "¿París es la capital de?") |
| **Resolución de entidad** | Determinar si dos menciones se refieren a la misma entidad |
| **Respuesta de preguntas** | Navega por el gráfico para encontrar respuestas |
---

## Conceptos avanzados de GNN
### Suavizado excesivo
| Problema | Descripción | Solución |
|---------|-------------|----------|
| **Suavizado excesivo** | Después de muchas capas, todas las representaciones de los nodos se vuelven similares | Limitar la profundidad (2-4 capas); utilizar conexiones residuales; utilizar el conocimiento de salto |
### Aplastamiento excesivo
| Problema | Descripción | Solución |
|---------|-------------|----------|
| **Aplastamiento excesivo** | La información de nodos distantes se comprime en vectores de tamaño fijo | Utilice transformadores de gráficos; agrupación jerárquica |
### Transformadores gráficos
| Modelo | Característica clave |
|-------|-------------|
| **Transformador gráfico** | Aplique la atención estándar del transformador a todos los pares de nodos |
| **GPS** (Sistema de indicación de gráficos) | Combine capas GNN locales con capas Transformer globales |
| **Grafórmico** | Agregue codificación posicional basada en la estructura del gráfico |
### Redes de gráficos heterogéneos
| Modelo | Descripción |
|-------|-------------|
| **R-GCN** | GCN relacional; diferentes matrices de peso para diferentes tipos de bordes |
| **HAN** | Red de Atención Heterogénea; atención sobre diferentes tipos de nodos y bordes |
| **HetGNN** | Red neuronal de gráficos heterogéneos; maneja múltiples tipos de nodos |
---

## Escalabilidad
| Desafío | Solución |
|-----------|----------|
| **Gráficos grandes** (millones de nodos) | Entrenamiento en mini lotes; muestreo vecino |
| **Memoria** | Partición de gráficos entre GPU |
| **Velocidad** | Operaciones matriciales dispersas; bibliotecas especializadas |
### Estrategias de muestreo
| Estrategia | Descripción |
|----------|-------------|
| **Muestreo de nodos** | Muestra un subconjunto de nodos y sus barrios K-hop |
| **Muestreo de bordes** | Aristas de muestra y los nodos que conectan |
| **Muestreo por conglomerados** | Divida el gráfico en grupos; tren sobre clusters |
| **Muestreo de caminata aleatoria** | Muestra de nodos mediante recorridos aleatorios desde los nodos objetivo |
---

## Herramientas y marcos
| Herramienta | Propósito |
|------|---------|
| **PyTorch Geométrico (PyG)** | Biblioteca GNN más popular; rico conjunto de modelos y conjuntos de datos |
| **DGL** (Biblioteca de gráficos profundos) | Agnóstico del marco; admite PyTorch, TensorFlow, MXNet |
| **RedX** | Algoritmos de gráficos clásicos; manipulación de datos |
| **OGB** (Parámetro de referencia de gráfico abierto) | Puntos de referencia estándar y conjuntos de datos para la investigación de GNN |
| **CogDL** | Aprendizaje profundo para gráficos; orientado a la investigación |
| **Espectral** | Biblioteca GNN para TensorFlow/Keras |
---

## Resumen
Graph Neural Networks extiende el aprendizaje profundo a datos relacionales: redes, moléculas, gráficos de conocimiento y cualquier sistema donde las entidades estén conectadas. Funcionan pasando mensajes entre vecinos, lo que permite que cada nodo aprenda de su contexto local. Las GNN han encontrado sus aplicaciones más sólidas en el descubrimiento de fármacos, sistemas de recomendación, detección de fraude y gráficos de conocimiento. El campo está evolucionando hacia transformadores de gráficos, gráficos heterogéneos y entrenamiento escalable para redes masivas del mundo real. Si sus datos tienen relaciones, probablemente valga la pena considerar los GNN.