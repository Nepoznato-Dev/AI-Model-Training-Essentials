<!--
---
# Metadata
title: "Supply Chain and Operations Management"
description: "Inventory management, lean manufacturing, logistics, bullwhip effect"
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
tags: [supply, chain, operations, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Gestión de operaciones y cadena de suministro
La gestión de la cadena de suministro es la coordinación de todas las actividades involucradas en el abastecimiento, la adquisición, la conversión y la logística, desde las materias primas hasta el producto terminado en manos del cliente. La gestión de operaciones es el funcionamiento diario de los sistemas de producción. Juntos, determinan si una empresa puede entregar el producto correcto, en el momento correcto, al costo correcto y con la calidad adecuada. La pandemia, la escasez de chips y los bloqueos de canales han demostrado cuán frágiles y globalmente interconectadas son las cadenas de suministro.
---

## Fundamentos de la cadena de suministro
### El flujo de la cadena de suministro
| Etapa | Actividad | Preocupación clave |
|-------|----------|-------------|
| **Planificar** | Previsión de la demanda; planificación de suministros; Compra y venta | Exactitud; capacidad de respuesta |
| **Fuente** | Selección de proveedores; obtención; contratación | Costo; calidad; fiabilidad; ética |
| **Hacer** | Producción; asamblea; control de calidad | Eficiencia; flexibilidad; capacidad |
| **Entregar** | Almacenamiento; cumplimiento de pedidos; transporte | Velocidad; costo; exactitud |
| **Volver** | Logística inversa; devoluciones; reciclaje | Satisfacción del cliente; recuperación de costes |
### Tipos de cadenas de suministro
| Tipo | Características | Mejor para |
|------|----------------|----------|
| **Eficiente** | Alta utilización; bajo costo; predecible | Productos funcionales con demanda estable (alimentos) |
| **Responsivo** | Capacidad de amortiguación; flexible; rápido | Productos innovadores con demanda incierta (moda) |
| **Resiliente** | Redundancia; visibilidad; adaptabilidad | Entornos de alto riesgo; bienes críticos |
| **Ágil** | Aplazamiento; personalización masiva | Productos con gran variedad y ciclos de vida cortos |
| **Magro** | Eliminar el desperdicio; basado en extracción; justo a tiempo | Alto volumen; baja variedad; demanda estable |
---

## Gestión de inventario
### Tipos de inventario
| Tipo | Descripción | Propósito |
|------|-------------|---------|
| **Materias primas** | Insumos no procesados ​​| Amortiguador contra la variabilidad de la oferta |
| **Trabajo en progreso (WIP)** | Productos parcialmente terminados | Zona intermedia entre etapas de producción |
| **Productos terminados** | Listo para vender | Amortiguador contra la variabilidad de la demanda |
| **MRO** (Mantenimiento, Reparación, Operaciones) | Suministros necesarios para las operaciones | Mantenga la producción en marcha |
| **Existencias de seguridad** | Inventario adicional por encima de la demanda esperada | Protegerse contra la incertidumbre |
| **Inventario de tuberías** | En tránsito entre ubicaciones | Inevitable durante el transporte |
### Modelos de gestión de inventario
| Modelo | Descripción | Cuándo utilizar |
|-------|-------------|-------------|
| **EOQ** (Cantidad de pedido económica) | Tamaño de pedido óptimo que minimiza los costos totales de tenencia + pedidos | Demanda estable; plazo de entrega constante |
| **Punto de reorden (ROP)** | Orden cuando el inventario cae a un umbral | Revisión continua; demanda predecible |
| **Análisis ABC** | Clasificar artículos por valor: A (alto), B (medio), C (bajo) | Priorizar la atención de la gestión |
| **Justo a tiempo (JIT)** | Recibir bienes solo según sea necesario en producción | Cadena de suministro estable; baja variabilidad |
| **Inventario administrado por el proveedor (VMI)** | Proveedor gestiona los niveles de inventario | Fuertes relaciones con proveedores |
| **Envío** | El proveedor posee el inventario hasta su uso | Reducir los costos de transporte del comprador |
---

## Sistemas de producción
### Enfoques de fabricación
| Enfoque | Descripción | Volumen | Variedad | Ejemplo |
|----------|-------------|--------|---------|---------|
| **Tienda de trabajo** | Productos personalizados; equipos de uso general | Bajo | Alto | Taller de máquinas; muebles a medida |
| **Lote** | Producir en lotes; cambio entre lotes | Medio | Medio | Panaderías; productos farmacéuticos |
| **Producción en masa** | Alto volumen; equipo dedicado; líneas de montaje | Alto | Bajo | Automóviles; electrónica |
| **Flujo continuo** | Producción ininterrumpida; totalmente automatizado | Muy alto | Muy bajo | Refinación de petróleo; productos químicos; acero |
| **Personalización masiva** | Alto volumen + gran variedad; automatización flexible | Alto | Alto | Computadoras Dell; Nike por ti |
### Fabricación ajustada
| Principio | Descripción |
|-----------|-------------|
| **Valor** | Definir lo que el cliente considera valioso |
| **Flujo de valor** | Mapear todos los pasos; identificar aquellos que añaden valor |
| **Flujo** | Haga que los pasos de creación de valor fluyan sin interrupciones |
| **Tirar** | Producir sólo cuando el cliente lo solicite |
| **Perfección** | Eliminar continuamente los residuos (muda) |
### Los Siete Desechos (Muda)
| Residuos | Descripción | Ejemplo |
|-------|-------------|---------|
| **Sobreproducción** | Haciendo más de lo necesario | Producir para pronosticar cuando la demanda es incierta |
| **Esperando** | Tiempo de inactividad entre pasos | Piezas a la espera de la próxima máquina |
| **Transporte** | Movimiento innecesario de materiales | Traslado de productos entre almacenes distantes |
| **Sobreprocesamiento** | Haciendo más trabajo del necesario | Inspecciones adicionales; características innecesarias |
| **Inventario** | Exceso de stock más allá de lo necesario | Stock de seguridad "por si acaso" |
| **Movimiento** | Movimiento innecesario de personas | Caminar para buscar herramientas; buscando piezas |
| **Defectos** | Productos que no cumplen con las especificaciones | Rehacer; chatarra; reclamaciones de garantía |
---

## Logística y Transporte
### Modos de transporte
| Modo | Costo | Velocidad | Capacidad | Mejor para |
|------|------|-------|----------|----------|
| **Carretera** (camión) | Medio | Medio | Medio | Última milla; regional; enrutamiento flexible |
| **Ferrocarril** | Bajo | Medio | Alto | Productos a granel; larga distancia por tierra |
| **Marítimo** (barco) | Muy bajo | Muy lento | Muy alto | Internacional; a granel; contenedores |
| **Aire** | Muy alto | Muy rápido | Bajo | Alto valor; urgente; perecedero |
| **Tubería** | Bajo (después de la construcción) | Continuo | Alto | Aceite; gas; agua |
| **Intermodal** | Varía | Varía | Alto | Combinando modos; transporte en contenedores |
### Diseño de almacén
| Decisión | Opciones | Compensación |
|----------|---------|-----------|
| **Número de almacenes** | Pocos (centralizados) versus muchos (regionales) | Rentabilidad frente a velocidad de entrega |
| **Nivel de automatización** | Manual versus semiautomático versus totalmente automatizado | Costo de capital versus costo laboral y precisión |
| **Diseño** | Flujo en U frente a flujo pasante | Utilización del espacio vs distancia de viaje |
| **Sistema de almacenamiento** | Estantería; atroz; COMO/RS; carrusel | Densidad vs accesibilidad vs costo |
---

## Gestión de riesgos de la cadena de suministro
### Riesgos comunes
| Categoría de riesgo | Ejemplos | Mitigación |
|--------------|----------|------------|
| **Riesgo de demanda** | Errores de pronóstico; efecto látigo | Mejores pronósticos; detección de demanda; stock de seguridad |
| **Riesgo de suministro** | Quiebra de proveedores; fallos de calidad | Doble abastecimiento; auditorías de proveedores; stock de seguridad |
| **Riesgo logístico** | Congestión portuaria; fallos del transportista | Multimodal; rutas alternativas |
| **Riesgo geopolítico** | Aranceles; guerras comerciales; sanciones | Nearshoring; diversificando los países de abastecimiento |
| **Desastre natural** | Terremoto; inundación; pandemia | Diversificación geográfica; planes de continuidad del negocio |
| **Riesgo cibernético** | ransomware; violación de datos | seguridad informática; sistemas de respaldo |
### El efecto látigo
| Causa | Descripción | Solución |
|-------|-------------|----------|
| **Actualización de la previsión de demanda** | Cada etapa suma su propio stock de seguridad | Compartir datos de puntos de venta en toda la cadena |
| **Pedido por lotes** | Los pedidos periódicos crean picos de demanda | Reducir los tiempos del ciclo de pedidos; EDI |
| **Fluctuaciones de precios** | Compra a plazo durante promociones | Precios bajos todos los días; precios estables |
| **Juegos de racionamiento y escasez** | Pedidos excesivos durante la escasez | Asignar en función de las ventas pasadas; compartir información de capacidad |
---

## Tendencias modernas de la cadena de suministro
| Tendencia | Descripción | Impacto |
|-------|-------------|--------|
| **Gemelos digitales** | Réplica virtual de la cadena de suministro para simulación | Mejor planificación; análisis de escenarios |
| **Torres de control de la cadena de suministro** | Visibilidad centralizada en toda la cadena | Respuesta más rápida a las perturbaciones |
| **Nearshoring/amigoshoring** | Acercar la producción a casa o a países aliados | Riesgo reducido; mayor costo |
| **Cadenas de suministro circulares** | Diseño para reutilización, remanufactura, reciclaje | Sostenibilidad; eficiencia de recursos |
| **Detección de demanda impulsada por IA** | Aprendizaje automático sobre datos en tiempo real para pronósticos a corto plazo | Más preciso; respuesta más rápida |
| **Vehículos autónomos y drones** | Camiones autónomos; entrega con drones | Menor costo; última milla más rápida |
---

## Resumen
La gestión de la cadena de suministro y las operaciones consiste en hacer que el flujo físico de bienes sea eficiente, receptivo y resiliente. La gestión de inventario equilibra el costo de mantener existencias con el riesgo de desabastecimiento. Los sistemas de producción varían desde talleres (personalizados, bajo volumen) hasta flujo continuo (productos básicos, alto volumen). La fabricación ajustada elimina el desperdicio para mejorar la eficiencia. Las decisiones logísticas (modo de transporte, ubicación del almacén, nivel de automatización) determinan el costo y la calidad del servicio. La gestión de riesgos aborda el efecto látigo, las fallas de los proveedores, las perturbaciones geopolíticas y los desastres naturales. Las tendencias modernas, como los gemelos digitales, la detección de la demanda impulsada por la IA y la deslocalización cercana, reflejan la respuesta de la industria a un mundo cada vez más volátil. Las mejores cadenas de suministro no sólo son eficientes: son visibles, flexibles y están preparadas para las interrupciones.