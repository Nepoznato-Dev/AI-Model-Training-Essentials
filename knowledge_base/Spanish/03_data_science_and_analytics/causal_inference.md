---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Inferencia causal
La inferencia causal es la ciencia que determina si una cosa realmente causa otra, no sólo si están correlacionadas. La correlación te dice que dos variables se mueven juntas. La causalidad te dice que cambiar uno cambiará el otro. Esta distinción es de enorme importancia en medicina (¿este medicamento funciona?), políticas (¿esta intervención reduce la pobreza?), negocios (¿esta campaña publicitaria aumenta las ventas?) y ciencia (¿este mecanismo explica el fenómeno?).
---

## Correlación vs causalidad
| Concepto | Descripción | Ejemplo |
|---------|-------------|---------|
| **Correlación** | Dos variables se mueven juntas | Las ventas de helados y las muertes por ahogamiento aumentan en verano |
| **Causalidad** | Una variable afecta directamente a otra | Fumar causa cáncer de pulmón |
| **Confuso** | Una tercera variable causa ambos | El calor provoca tanto la venta de helados como la natación (y ahogamiento) |
| **Causalidad inversa** | El efecto en realidad causa la supuesta causa | La gente compra suplementos para la salud porque está enferma, no al revés |
| **Correlación espuria** | Relación coincidente | El consumo de queso per cápita se correlaciona con las muertes por enredo en sábanas |
---

## El marco de resultados potenciales
### Modelo causal de Rubin
| Concepto | Descripción |
|---------|-------------|
| **Resultados potenciales** | Para cada unidad, hay un resultado si se trata Y(1) y un resultado si no se trata Y(0) |
| **Efecto del tratamiento** | La diferencia: Y(1) - Y(0) para una unidad determinada |
| **Problema fundamental** | Nunca podremos observar Y(1) e Y(0) para la misma unidad; solo podemos ver uno |
| **Efecto promedio del tratamiento (ATE)** | El promedio de los efectos del tratamiento individual en toda la población |
| **Contrafactual** | El resultado no observado: qué habría sucedido bajo la otra condición |
### Supuestos clave
| Asunción | Significado | Cómo satisfacer |
|-----------|----------------|----------------|
| **Ignorabilidad (sin fundamento)** | La asignación del tratamiento es independiente de los posibles resultados, dadas las covariables observadas | Aleatorización; medir todos los factores de confusión |
| **Positividad (superposición)** | Cada unidad tiene una probabilidad distinta de cero de recibir cualquiera de los tratamientos | Verifique la superposición de covariables entre grupos |
| **SUTVA** (Supuesto de valor de tratamiento unitario estable) | El tratamiento de una unidad no afecta el resultado de otra; el tratamiento es consistente | Sin interferencias; no hay versiones ocultas de tratamiento |
| **Consistencia** | El resultado observado es igual al resultado potencial bajo el tratamiento recibido | Tratamiento bien definido |
---

## Métodos de inferencia causal
### Métodos experimentales
| Método | Descripción | Fuerza | Limitación |
|--------|-------------|----------|------------|
| **Ensayo controlado aleatorio (ECA)** | Asignar unidades aleatoriamente a tratamiento o control | Patrón oro; elimina la confusión | Caro; a veces poco ético; no puede generalizar |
| **Pruebas A/B** | RCT en un contexto empresarial/tecnológico | Simple; riguroso | Métricas de corto plazo; efectos novedosos; interferencia |
| **Experimentos de retroceso** | Tratamiento alternativo a lo largo de períodos de tiempo | Maneja la interferencia en los mercados | Requiere un entorno estable |
### Métodos cuasiexperimentales
| Método | Descripción | Supuesto clave |
|--------|-------------|----------------|
| **Diferencia en diferencias (DiD)** | Compare el cambio en los resultados entre los grupos tratados y de control a lo largo del tiempo | Tendencias paralelas: grupos habrían seguido la misma trayectoria sin tratamiento |
| **Discontinuidad de regresión (RD)** | Compare las unidades justo por encima y por debajo de un límite de tratamiento | Las unidades cercanas al límite son comparables (como si fueran aleatorias) |
| **Variables instrumentales (IV)** | Utilice una variable que afecte el tratamiento pero no el resultado excepto a través del tratamiento | El instrumento se correlaciona con el tratamiento; afecta el resultado sólo a través del tratamiento |
| **Control sintético** | Construya una combinación ponderada de unidades de control para que coincida con la unidad tratada | El control sintético representa con precisión el contrafactual de la unidad tratada |
| **Emparejamiento de puntuación de propensión** | Emparejar unidades tratadas y de control con probabilidades de tratamiento similares | Todos los factores de confusión se miden e incluyen en el modelo de propensión.
### Diferencia en diferencias (visualizada)
| Periodo | Grupo tratado | Grupo de control | Diferencia |
|--------|--------------|---------------|------------|
| **Pretratamiento** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Postratamiento** | Y_t_post | Y_c_post | Y_t_post-Y_c_post |
| **Estimación de DiD** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Gráficos acíclicos dirigidos (DAG)
Los DAG son herramientas visuales para codificar suposiciones causales e identificar factores de confusión.
### Estructuras básicas
| Estructura | Patrón | Implicación |
|-----------|---------|-------------|
| **Cadena** | A → B → C | A y C están asociados a través de B; controlar por B bloquea el camino |
| **Tenedor** | A ← B → C | A y C se confunden con B; controlar por B bloquea el camino |
| **Colisionador** | A → B ← C | A y C son independientes; controlar B abre el camino (crea asociación espuria) |
### Reglas para DAG
| Regla | Descripción |
|------|-------------|
| **Criterio de puerta trasera** | Para estimar el efecto causal de X sobre Y, bloquee todas las rutas de puerta trasera (rutas con una flecha hacia X) condicionando las variables apropiadas |
| **Criterio de entrada** | Si no se pueden bloquear las rutas de puerta trasera, utilice mediadores: estime X → M → Y en dos etapas |
| **No condicionar a los colisionadores** | Controlar por un efecto común abre un camino espurio |
| **No condicionar a los descendientes de colisionadores** | El mismo problema que el acondicionamiento del propio colisionador |
---

## Errores comunes
| Escollo | Descripción | Ejemplo |
|---------|-------------|---------|
| **Sesgo de variable omitida** | No controlar un factor de confusión | Estimación de la educación → ingresos sin controlar la capacidad |
| **Control excesivo** | Condicionamiento sobre un mediador o colisionador | Controlar por el puesto de trabajo al estimar la educación → ingresos |
| **Sesgo de selección** | Condicionamiento sobre una variable afectada por el tratamiento | Sólo analizando a los ocupados cuando estudian formación → salarios |
| **Sesgo del tiempo inmortal** | Clasificación errónea del tiempo-persona en estudios de cohortes | Los pacientes deben sobrevivir el tiempo suficiente para recibir tratamiento |
| **Regresión a la media** | Los valores extremos tienden a moverse hacia el promedio | Los pacientes enfermos mejoran después del tratamiento independientemente |
| **Sesgo post-tratamiento** | Condicionamiento sobre variables que ocurren después del tratamiento | Control de eventos adversos al estimar la eficacia del fármaco |
---

## Herramientas y bibliotecas
| Herramienta | Idioma | Descripción |
|------|----------|-------------|
| **Hacer por qué** | Pitón | biblioteca de Microsoft; Inferencia causal basada en DAG |
| **CausalML** | Pitón | Biblioteca de Uber para modelado de elevación y aprendizaje automático causal |
| **EconML** | Pitón | Doble ML, bosques causales, variables instrumentales |
| **modelos lineales** | Pitón | IV, modelos de datos de panel, DiD |
| **Combina** | R | Emparejamiento de puntuación de propensión |
| **dagitoso** | R/web | análisis DAG; identificar conjuntos de ajustes |
| **Impacto Causal** | R/Python | Series temporales estructurales bayesianas para inferencia causal |
---

## Resumen
La inferencia causal consiste en ir más allá de "lo que sucedió" y llegar a "lo que habría sucedido si las cosas fueran diferentes". El desafío fundamental es que nunca podemos observar los resultados tratados y no tratados para la misma unidad: siempre falta el contrafactual. Los experimentos aleatorios resuelven esto haciendo que los grupos de tratamiento y control sean comparables. Cuando la aleatorización no es posible, los métodos cuasiexperimentales (DiD, discontinuidad de regresión, variables instrumentales, control sintético) intentan reconstruir el contrafactual a partir de datos observacionales. Los DAG ayudan a hacer suposiciones explícitas e identificar las variables correctas que se deben controlar. La habilidad clave es pensar detenidamente sobre el proceso de generación de datos: qué causa qué, qué es un factor de confusión, qué es un colisionador y qué habría sucedido con la alternativa.