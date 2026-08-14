---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
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
tags: [performance, optimization, coding-and-technology]
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
# Optimización del rendimiento
La optimización del rendimiento es la práctica de hacer que el software sea más rápido: reducir los tiempos de respuesta, aumentar el rendimiento, reducir el uso de memoria y eliminar cuellos de botella. Es una de las habilidades más impactantes que puede tener un desarrollador, porque el software lento pierde usuarios, desperdicia recursos y frustra a todos. Pero también es uno de los errores más comunes: los desarrolladores optimizan las cosas incorrectas basándose en la intuición en lugar de en la evidencia.
---

## La regla de oro
> **Primero medir, luego optimizar.** Nunca optimice basándose en suposiciones. Perfile el código, encuentre el cuello de botella real y solucionelo.
| Antipatrón | Por qué es malo |
|-------------|-------------|
| **Optimización prematura** | Dedicar tiempo a acelerar código que no sea lento |
| **Optimización sin medición** | Solucionar el cuello de botella equivocado; no hay forma de verificar la mejora |
| **Sacrificar la legibilidad por la velocidad** | El código ilegible cuesta más que la ganancia de rendimiento |
| **Almacenando todo en caché** | Datos obsoletos, exceso de memoria, complejidad |
---

## Perfilado
Antes de poder hacer algo más rápido, necesita saber *dónde* se está invirtiendo el tiempo.
| Tipo de herramienta | Qué mide | Ejemplos |
|-----------|-----------------|----------|
| **Perfilador de CPU** | ¿Qué funciones consumen más tiempo de CPU? cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Perfilador de memoria** | Asignación de memoria y fugas | tracemalloc (Python), Valgrind, heaptrack |
| **Perfilador de E/S** | Cuellos de botella de E/S de disco y red | iotop, strace, Wireshark |
| **APM (Monitoreo del rendimiento de aplicaciones)** | Cronograma de solicitud de un extremo a otro | Nueva reliquia, Datadog, Jaeger |
| **Herramientas de desarrollo del navegador** | Representación frontend, ejecución de JavaScript, red | Chrome DevTools, Perfilador de Firefox |
### Flujo de trabajo de creación de perfiles
| Paso | Descripción |
|------|-------------|
| 1. Identificar la operación lenta | Los usuarios informan que la carga de la página es lenta; monitoreo muestra alta latencia |
| 2. Perfilar la ruta completa | Encuentre qué componente requiere más tiempo |
| 3. Profundizar | Perfile ese componente específico para encontrar la función activa |
| 4. Solucionar el cuello de botella | Aplicar la optimización adecuada |
| 5. Medir nuevamente | Verificar la mejora; comprobar si hay regresiones |
---

## Optimización algorítmica
Las mayores ganancias de rendimiento provienen de la elección de mejores algoritmos, no de microoptimizaciones.
| Cambiar | Mejora |
|--------|------------|
| Búsqueda lineal O (n) → Búsqueda de tabla hash O (1) | 100x+ para grandes conjuntos de datos |
| Bucle anidado O(n²) → Ordenar + búsqueda binaria O(n log n) | Órdenes de magnitud para n grande |
| Cálculo repetido → Memorización / almacenamiento en caché | Elimina el trabajo redundante |
| Concatenación de cadenas en un bucle → Generador/unión | Evita la copia de cadenas cuadráticas |
| Datos sin clasificar → Datos ordenados con búsqueda binaria | O(log n) en lugar de O(n) por búsqueda |
---

## Estrategias de almacenamiento en caché
El almacenamiento en caché almacena los resultados calculados para que no sea necesario volver a calcularlos.
| Tipo de caché | Ubicación | Velocidad | Toda la vida |
|-----------|----------|-------|----------|
| **Caché de CPU** | L1/L2/L3 | ~1 ns | Automático |
| **En memoria** | RAM de aplicación (dict, HashMap) | ~100 ns | Hasta que sean absueltos o desalojados |
| **Caché distribuida** | Redis, Memcached | ~1ms | TTL configurable |
| **CDN** | Servidores perimetrales en todo el mundo | ~10-50 ms | TTL configurable |
| **Caché del navegador** | Navegador del usuario | ~1ms | Encabezados de caché HTTP |
| **Caché de consultas de base de datos** | Nivel de base de datos u ORM | ~1-10 ms | Hasta que cambien los datos |
### Patrones de almacenamiento en caché
| Patrón | Descripción | Cuándo utilizar |
|---------|-------------|-------------|
| **Aparte del caché** | La aplicación comprueba el caché; cargas desde DB en caso de error; almacena en caché | Más común; sencillo |
| **Escritura simultánea** | Escribir en caché y base de datos simultáneamente | Cuando lee >> escribe; consistencia importante |
| **Escritura retrasada** | Escribir en caché; escribir asincrónicamente en DB | Alto rendimiento de escritura; cierto riesgo de pérdida de datos |
| **TTL (Tiempo de vida)** | Las entradas de caché caducan después de un tiempo determinado | Cuando los datos cambian periódicamente |
| **Invalidación** | Eliminar explícitamente las entradas de caché obsoletas | Cuándo sabes exactamente cuándo cambian los datos |
### Invalidación de caché
Los dos problemas más difíciles en informática: invalidación de caché, nombres de cosas y errores uno por uno.
| Estrategia | Descripción |
|----------|-------------|
| **Basado en TTL** | Las entradas caducan después de N segundos; simple pero puede servir para datos obsoletos |
| **Basado en eventos** | Invalidar cuando cambien los datos; más complejo pero preciso |
| **Basado en versiones** | Incluya un número de versión; incremento en cambios |
| **Basado en etiquetas** | Entradas de caché relacionadas con etiquetas; invalidar todas las entradas con una etiqueta |
---

## Optimización de la base de datos
Las bases de datos suelen ser el mayor cuello de botella en las aplicaciones web.
| Técnica | Descripción | Impacto |
|-----------|-------------|--------|
| **Indexación** | Agregue índices en las columnas utilizadas en DÓNDE, UNIRSE, ORDENAR POR | Consultas entre 10 y 1000 veces más rápidas |
| **Optimización de consultas** | Evite SELECCIONAR *; utilice EXPLAIN para analizar consultas | Reducir E/S |
| **Agrupación de conexiones** | Reutilizar conexiones de bases de datos en lugar de crear nuevas | Eliminar gastos generales de conexión |
| **Leer réplicas** | Enrutar consultas de lectura a bases de datos de réplica | Distribuir carga de lectura |
| **Partición** | Divida mesas grandes en particiones más pequeñas | Consultas más rápidas en grandes conjuntos de datos |
| **Desnormalización** | Agregue datos redundantes para evitar uniones | Lecturas más rápidas; escrituras más lentas |
| **Visitas materializadas** | Resultados de consultas precalculados | Consultas complejas instantáneas |
| **Prevención N+1** | Utilice JOIN, carga ansiosa o consultas por lotes | Elimina miles de consultas |
---

## Concurrencia y Paralelismo
| Concepto | Descripción | Cuándo utilizar |
|---------|-------------|-------------|
| **Enhebrado** | Múltiples hilos dentro de un solo proceso | Tareas vinculadas a E/S (red, disco) |
| **Multiprocesamiento** | Múltiples procesos (omite GIL en Python) | Tareas vinculadas a la CPU |
| **Asíncrono/espera** | Multitarea cooperativa; hilo único | E/S de alta concurrencia (servidores web) |
| ** Computación GPU ** | Miles de núcleos paralelos | Operaciones matriciales; procesamiento de imágenes; aprendizaje automático |
### Asíncrono frente a subprocesos
| Aspecto | Asíncrono/Espera | Enhebrado |
|--------|------------|-----------|
| **Modelo** | Cooperativa (tareas de control de rendimiento) | Preventivo (el sistema operativo cambia subprocesos) |
| **Arriba** | Muy bajo (sin cambio de contexto) | Superior (creación de hilos, cambio de contexto) |
| **Complejidad** | Razonamiento más simple (hilo único) | Condiciones de carrera, puntos muertos, bloqueos |
| **Mejor para** | Muchas operaciones de E/S simultáneas | Bloqueo de operaciones que no se pueden convertir en asíncronas |
| **Limitación** | No se puede usar código vinculado a la CPU sin bloquear | GIL en Python limita el verdadero paralelismo |
---

## Rendimiento de la interfaz
| Técnica | Descripción | Impacto |
|-----------|-------------|--------|
| **Minificación** | Eliminar espacios en blanco y acortar nombres de variables | Archivos entre un 20 y un 40 % más pequeños |
| **Agrupación** | Combine varios archivos en menos solicitudes | Menos solicitudes HTTP |
| **División de código** | Cargue sólo el código necesario para la página actual | Carga inicial más rápida |
| **Carga diferida** | Cargue imágenes y componentes cuando sean necesarios | Renderizado inicial más rápido |
| **Árbol sacudido** | Eliminar el código no utilizado de los paquetes | Paquetes más pequeños |
| **Optimización de imagen** | Utilice WebP/AVIF; imágenes receptivas; carga diferida | Imágenes entre un 50 y un 80 % más pequeñas |
| **CDN** | Servir activos estáticos desde servidores perimetrales | Menor latencia a nivel global |
| **HTTP/2 y HTTP/3** | Multiplexación; compresión de encabezados; 0-RTT | Gastos generales de protocolo más rápidos |
| **Trabajadores de servicios** | Activos de caché para uso sin conexión; notificaciones push | Visitas repetidas más rápidas |
---

## Optimización de la memoria
| Técnica | Descripción |
|-----------|-------------|
| **Agrupación de objetos** | Reutilizar objetos en lugar de crear otros nuevos |
| **Transmisión** | Procesar datos en fragmentos en lugar de cargar todo en la memoria |
| **Generadores/iteradores** | Valores de rendimiento uno a la vez en lugar de crear listas |
| **Archivos asignados en memoria** | Acceda a archivos grandes sin cargarlos por completo |
| **Ajuste de recolección de basura** | Ajuste los parámetros de GC para su carga de trabajo |
| **Elección de estructura de datos** | Utilice matrices en lugar de listas vinculadas para la localidad de caché; utilizar conjuntos para pruebas de membresía |
---

## Optimización de la red
| Técnica | Descripción |
|-----------|-------------|
| **Compresión** | gzip, brotli para respuestas HTTP |
| **Reutilización de conexiones** | Conexiones que se mantienen vivas; Multiplexación HTTP/2 |
| **Solicitar lotes** | Combine varias llamadas API en una |
| **Paginación** | Cargue datos en páginas en lugar de todos a la vez |
| **Compresión en reposo** | Comprimir datos en bases de datos y cachés |
| **Elección de protocolo** | gRPC (binario, eficiente) vs REST (legible por humanos) |
---

## Monitoreo y alertas
| Métrica | Lo que te dice |
|--------|------------------|
| **Latencia P50 / P95 / P99** | Tiempo de respuesta en varios percentiles |
| **Rendimiento** | Solicitudes por segundo |
| **Tasa de error** | Porcentaje de solicitudes fallidas |
| **Utilización de CPU** | ¿Cuánta capacidad de procesamiento se utiliza?
| **Uso de memoria** | Consumo de RAM; ¿Acercándose a los límites? |
| **Tiempo de consulta de la base de datos** | Consultas lentas que necesitan optimización |
---

## Resumen
La optimización del rendimiento es un proceso sistemático: medir, identificar el cuello de botella, solucionarlo, volver a medir. Las mayores ganancias provienen de las mejoras algorítmicas y de la eliminación del trabajo innecesario, no de las microoptimizaciones. El almacenamiento en caché, la indexación de bases de datos y la concurrencia son las herramientas más poderosas. El rendimiento del frontend depende de minimizar el tamaño de la carga útil y los viajes de ida y vuelta. Y la regla más importante es siempre la misma: no adivines: perfil.