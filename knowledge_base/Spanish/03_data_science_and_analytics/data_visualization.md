<!--
---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, visualization, data-science-and-analytics]
difficulty_level: "intermediate"
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
# Visualización de datos
Un gráfico bien diseñado puede revelar patrones que ocultan las tablas de números. Uno mal diseñado puede inducir a error, confundir o aburrir. La visualización de datos es el arte de convertir datos en historias visuales que informen las decisiones. Este archivo cubre la selección de gráficos, los principios de diseño, los errores comunes y las herramientas que lo hacen posible.
---

## Elegir el gráfico correcto
La decisión más importante en cualquier visualización es elegir el tipo de gráfico adecuado para sus datos y mensaje.
### Guía de selección de gráficos
| Tu objetivo | Mejores tipos de gráficos |
|-----------|-----------------|
| **Comparar categorías** | Gráfico de barras, gráfico de barras agrupadas |
| **Mostrar cambios a lo largo del tiempo** | Gráfico de líneas, gráfico de áreas |
| **Mostrar distribución** | Histograma, diagrama de caja, diagrama de violín |
| **Mostrar relación** | Diagrama de dispersión, gráfico de burbujas |
| **Mostrar composición** | Barras apiladas, gráfico circular (porciones limitadas), mapa de árbol |
| **Mostrar correlación** | Diagrama de dispersión, mapa de calor, diagrama de pares |
| **Mostrar ranking** | Gráfico de barras horizontales |
| **Mostrar patrones geográficos** | Mapa de coropletas, mapa de puntos |
| **Mostrar parte y todo a lo largo del tiempo** | Gráfico de áreas apiladas |
### Cuándo utilizar cada gráfico
| Gráfico | Fortalezas | Evitar cuando |
|-------|-----------|-----------|
| **Barra** | Comparaciones claras entre categorías | Demasiadas categorías (>15) |
| **Línea** | Tendencias a lo largo del tiempo; datos continuos | Los datos no son secuenciales |
| **Dispersión** | Relaciones entre dos variables | Demasiados puntos superpuestos |
| **Histograma** | Forma de distribución de una variable | Tamaños de muestra pequeños (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |
---

## Principios de diseño
### Ideas centrales de Tufte
Los principios de Edward Tufte siguen siendo el estándar de oro para la visualización de datos:
| Principio | Descripción |
|-----------|-------------|
| **Maximizar la relación datos-tinta** | Cada gota de tinta debe transmitir datos. Elimina todo lo demás. |
| **Eliminar chartjunk** | Sin efectos 3D, degradados gratuitos ni elementos decorativos. |
| **Mostrar los datos** | No distorsiones, escondas ni selecciones. Dejemos que los datos hablen. |
| **Múltiplos pequeños** | Utilice gráficos pequeños repetidos para comparar entre categorías. |
| **Minigráficos** | Pequeños gráficos del tamaño de una palabra para datos de tendencias en línea. |
### Reglas prácticas de diseño
| Regla | Por qué |
|------|-----|
| **Iniciar el eje y en cero** (para gráficos de barras) | De lo contrario exageras las diferencias |
| **Etiquetar directamente** | Coloque etiquetas en líneas/barras en lugar de usar una leyenda cuando sea posible |
| **Usa el color a propósito** | Resalte lo que importa; use gris para contexto |
| **Hazlo simple** | Un mensaje por gráfico; no sobrecargues |
| **Utilice escalas consistentes** | Al comparar gráficos, mantenga los mismos ejes |
| **Ordene de manera significativa** | Ordena las barras por valor (no alfabéticamente) a menos que haya un orden natural |
| **Proporcionar contexto** | Agregar puntos de referencia, objetivos o promedios históricos |
### Pautas de color
| Caso de uso | Enfoque |
|----------|----------|
| **Categórico** | Tonos distintos (azul, naranja, verde, rojo): máximo 7 a 8 categorías |
| **Secuencial** | De claro a oscuro de un tono (azul claro → azul oscuro) |
| **Divergente** | Degradado de dos tonos para datos con un punto medio significativo (rojo ← blanco → azul) |
| **Accesibilidad** | Prueba con simuladores daltónicos; no confíe sólo en el color (agregue etiquetas o patrones) |
---

## Narrar historias con datos
Un gráfico sin narrativa es sólo una imagen. La narración convierte los datos en conocimiento.
### El marco de la narración
1. **Contexto**: ¿Cuál es la situación? ¿Qué sabe ya el público?
2. **Conflicto**: ¿Cuál es el problema, la sorpresa o la tensión en los datos?
3. **Resolución**: ¿Qué debería hacer la audiencia con esta información?
### Consejos prácticos
| Consejo | Descripción |
|-----|-------------|
| **Liderar con conocimiento** | Titula el gráfico con la conclusión, no con los datos ("Los ingresos crecieron un 30%", no "Ingresos por trimestre") |
| **Anotar puntos clave** | Agregue notas de texto para eventos importantes o puntos de inflexión |
| **Usar divulgación progresiva** | Muestre un gráfico a la vez; construir la historia paso a paso |
| **Destaca lo que importa** | Utilice color o tamaño para llamar la atención sobre el punto de datos clave |
| **Proporcione un "¿y qué?"** | Cada gráfico debe responder una pregunta o provocar una acción |
---

## Errores comunes
| Error | Por qué es malo | Arreglar |
|---------|-------------|-----|
| **Eje y truncado** | Exagera las pequeñas diferencias | Comience desde cero para gráficos de barras |
| **Rango de tiempo de selección** | Engaños sobre las tendencias | Mostrar gama completa disponible |
| **Demasiados colores** | Abruma al espectador | Límite de 5 a 7; use gris para contexto |
| **Dos ejes y** | Implica correlación que puede no existir | Utilice dos gráficos separados |
| **Gráficos 3D** | Distorsiona las proporciones | Utilice siempre 2D |
| **Gráficos circulares con más de 10 sectores** | Imposible comparar | Utilice un gráfico de barras en su lugar |
| **Faltan etiquetas** | El espectador no puede entender el gráfico | Etiquete siempre los ejes, el título y las unidades |
| **Gráficos de áreas engañosos** | Las áreas apiladas distorsionan la percepción de series individuales | Utilice gráficos de líneas o múltiplos pequeños |
---

## Herramientas
### Pitón
| Biblioteca | Fuerza |
|---------|----------|
| **matplotlib** | Fundación del trazado de Python; totalmente personalizable |
| **nacido en el mar** | Visualización estadística; hermosos valores predeterminados; construido en matplotlib |
| **trama** | Gráficos interactivos basados ​​en web; tableros de instrumentos |
| **altair** | Gramática declarativa de gráficos (Vega-Lite) |
| **bokeh** | Visualización interactiva para navegadores |
### JavaScript/Web
| Biblioteca | Fuerza |
|---------|----------|
| **D3.js** | Máxima flexibilidad; curva de aprendizaje pronunciada |
| **Gráfico.js** | Gráficos simples y responsivos |
| **Recargas** | Gráficos compatibles con React |
| **Trama observable** | Gramática ligera y expresiva de gráficos |
### Sin código/herramientas de BI
| Herramienta | Tipo |
|------|------|
| **Cuadro** | Análisis visual estándar de la industria |
| **PowerBI** | ecosistema de Microsoft; BI empresarial |
| **Mirador** | Nube de Google; exploración de datos |
| **Metabase** | Código abierto; configuración sencilla |
| **Superconjunto de Apache** | Código abierto; SQL nativo |
---

## Diseño de tablero
Un panel es una colección de visualizaciones que juntas cuentan una historia completa sobre un proceso, sistema o negocio.
### Tipos de paneles
| Tipo | Audiencia | Propósito |
|------|----------|---------|
| **Estratégico** | Ejecutivos | KPI de alto nivel; tendencias a largo plazo |
| **Operativo** | Gerentes | Monitoreo en tiempo real; operaciones diarias |
| **Analítico** | Analistas | Exploración profunda; filtrado, desglose |
### Lista de verificación de diseño
- **Conozca a su audiencia**: ¿Qué decisiones tomarán desde este panel?
- **Regla de los 5 segundos**: ¿Se puede comprender la conclusión principal en 5 segundos?
- **Diseño**: métricas más importantes en la parte superior izquierda (donde van primero los ojos).
- **Limitar tipos de gráficos**: 3 o 4 tipos como máximo por panel para mantener la coherencia.
- **Interactivo por defecto**: filtros, selectores de rango de fechas, desgloses.
- **Rendimiento**: Los paneles que tardan >5 segundos en cargarse no se utilizan.
- **Móvil**: considere el diseño responsivo si los usuarios lo necesitan mientras viajan.
---

## Resumen
Una buena visualización de datos tiene que ver con claridad, honestidad e impacto. Elija el gráfico adecuado para sus datos. Elimina todo lo que no sirva al mensaje. Utilice colores y anotaciones para guiar al espectador. Y siempre, siempre deje que los datos cuenten la historia, no al revés.