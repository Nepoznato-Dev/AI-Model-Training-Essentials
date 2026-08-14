<!--
---
# Metadata
title: "Relativity"
description: "Special relativity, Lorentz transformations, time dilation, length contraction, mass-energy equivalence, four-vectors, and introduction to general relativity"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into relativity"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [relativity, special-relativity, general-relativity, lorentz-transformations, time-dilation, length-contraction, mass-energy, spacetime]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Relatividad
Las teorías de la relatividad de Einstein revolucionaron nuestra comprensión del espacio, el tiempo y la gravedad. **La relatividad especial** (1905) demostró que el espacio y el tiempo no están separados sino entrelazados en un solo tejido llamado espaciotiempo, y que la velocidad de la luz es la misma para todos los observadores. **La relatividad general** (1915) reinventó la gravedad no como una fuerza sino como la curvatura del espacio-tiempo causada por la masa y la energía. Estas teorías sustentan la navegación GPS, los aceleradores de partículas y nuestra comprensión de los agujeros negros y la evolución del universo.
---

## Postulados de la Relatividad Especial
Einstein construyó la relatividad especial sobre dos postulados engañosamente simples:
| Postulado | Declaración |
|-----------|-----------|
| **Principio de Relatividad** | Las leyes de la física son las mismas en todos los sistemas de referencia inerciales (no acelerados) |
| **Constancia de c** | La velocidad de la luz en el vacío (c ≈ 3 × 10⁸ m/s) es la misma para todos los observadores, independientemente de su movimiento o del movimiento de la fuente.
Estos dos postulados, combinados, anulan siglos de intuición newtoniana sobre el espacio y el tiempo absolutos.
---

## Transformaciones de Lorentz
Las **transformaciones de Lorentz** relacionan coordenadas entre dos sistemas inerciales que se mueven a una velocidad relativa v.
### Ecuaciones de transformación
Para el cuadro S' que se mueve a una velocidad v a lo largo del eje x en relación con el cuadro S:
| Cantidad | Transformación |
|----------|---------------|
| x' | γ(x − vt) |
| t' | γ(t − vx/c²) |
| y' | y |
| z' | z |
donde γ (factor de Lorentz) = 1/√(1 − v²/c²)
### El factor Lorentz γ
| v/c | γ | Efecto |
|-----|---|--------|
| 0 | 1.0 | Sin efectos relativistas (límite newtoniano) |
| 0,1 | 1.005 | Corrección del 0,5% |
| 0,5 | 1.155 | Corrección del 15,5% |
| 0,9 | 2.294 | Dilatación del tiempo significativa |
| 0,99 | 7.089 | Efectos extremos |
| 0,999 | 22.37 | Régimen del acelerador de partículas |
| → 1 | → ∞ | Imposible para objetos masivos |
### Transformaciones inversas
Para volver de S' a S: reemplace v con −v.
---

## Dilatación del tiempo
Los relojes en movimiento corren lento.
Δt = γΔt₀
donde Δt₀ es el **tiempo propio** (tiempo medido en el marco de reposo del reloj).
**Ejemplo resuelto:** Un muón creado a 10 km de altitud viaja a 0,998c. Su vida útil en reposo es de 2,2 μs.
- γ = 1/√(1 − 0,998²) ≈ 15,8
- Vida útil dilatada: Δt = 15,8 × 2,2 μs = 34,8 μs
- Distancia recorrida: d = 0,998c × 34,8 μs ≈ 10,4 km
- Sin dilatación del tiempo: d = 0,998c × 2,2 μs ≈ 0,66 km (nunca llegaría al suelo)
- **Realidad:** Los muones llegan a la superficie de la Tierra, lo que confirma experimentalmente la dilatación del tiempo.
### Paradoja de los gemelos
Un gemelo viaja a gran velocidad y regresa. Son más jóvenes que el gemelo que se queda en casa. No es una verdadera paradoja: el gemelo que viaja acelera (cambia el marco inercial), rompiendo la simetría.
---

## Contracción de longitud
Los objetos en movimiento se acortan según la dirección del movimiento.
L = L₀/γ
donde L₀ es la **longitud adecuada** (longitud medida en el marco de reposo del objeto).
| v/c | γ | Factor de contracción L/L₀ |
|-----|---|------------------------|
| 0,5 | 1.15 | 87% |
| 0,9 | 2.29 | 44% |
| 0,99 | 7.09 | 14% |
| 0,999 | 22.4 | 4,5% |
**Punto clave:** La contracción de longitud no es una ilusión óptica: es un efecto físico real medido por observadores en movimiento relativo.
---

## Relatividad de la simultaneidad
Los eventos que son simultáneos en un cuadro NO lo son en otro cuadro que se mueve con respecto al primero.
**Experimento mental del tren de Einstein:** Un rayo cae en ambos extremos de un tren en movimiento. Un observador en la plataforma los ve simultáneos. Un observador en el tren (que avanza hacia una huelga) ve primero la huelga frontal.
**Conclusión:** "Simultáneo" no es absoluto; depende del marco de referencia del observador.
---

## Suma de velocidad
Las velocidades no se suman simplemente a la relatividad especial.
### Suma de velocidad relativista
Si un objeto se mueve a una velocidad u' en el marco S', y S' se mueve a una velocidad v relativa a S:
u = (u' + v) / (1 + u'v/c²)
| Escenario | Resultado |
|----------|--------|
| u' = c (luz) | u = c (la velocidad de la luz es invariante) |
| u', v ≪ c | u ≈ u' + v (se reduce a la suma galileana) |
| u' = 0,9c, v = 0,9c | u = 0,9945c (nunca supera c) |
---

## Equivalencia masa-energía
E = mc²
| Concepto | Fórmula | Significado |
|---------|---------|---------|
| Descanso energía | E₀ = mc² | Energía de una masa en reposo |
| Energía total | mi = γmc² | Incluye energía cinética |
| Energía cinética | KE = (γ − 1)mc² | Se reduce a ½mv² para v ≪ c |
| Momento-energía | E² = (pc)² + (mc²)² | Relación relativista energía-momento |
| Partículas sin masa | mi = ordenador personal | Los fotones tienen energía e impulso pero no masa en reposo |
### Ejemplos de energía nuclear
| Reacción | Defecto masivo | Energía liberada |
|----------|-------------|-----------------|
| Fisión del U-235 | 0,1% de la masa | ~200 MeV por fisión |
| Fusión D-T | 0,7% de la masa | 17,6 MeV por reacción |
| Materia-antimateria | 100% de la masa | 2mc² (conversión completa) |
---

## Cuatro vectores y espacio-tiempo
### Espacio-tiempo de Minkowski
La relatividad especial unifica el espacio y el tiempo en 4D **espaciotiempo de Minkowski** con coordenadas (ct, x, y, z).
### El intervalo espacio-temporal
ds² = −c²dt² + dx² + dy² + dz²
| Tipo de intervalo | Condición | Significado |
|--------------|-----------|---------|
| **Tiempo** | ds²< 0 | Events can be causally connected |
| **Lightlike (null)** | ds² = 0 | Connected by a light signal |
| **Spacelike** | ds² >0 | Los acontecimientos no pueden influirse entre sí |
El intervalo espacio-temporal es **invariante**: todos los observadores están de acuerdo en su valor.
### Cuatro vectores
| Cuatro vectores | Componentes | Cantidad invariante |
|-------------|-----------|-------------------|
| Posición | (ct, x, y, z) | Intervalo espacio-temporal |
| Velocidad | γ(c, vₓ, vᵧ, v_z) | Momento adecuado |
| Impulso | (E/c, pₓ, pᵧ, p_z) | Masa en reposo: m²c² = E²/c² − p² |
| Fuerza | dP/dτ | Aceleración adecuada |
---

## Introducción a la Relatividad General
### El principio de equivalencia
| Versión | Declaración |
|---------|-----------|
| **Débil** | Masa gravitacional = masa inercial (todos los objetos caen al mismo ritmo) |
| **Einstein** | Un marco que se acelera uniformemente es localmente indistinguible de un campo gravitacional |
| **Fuerte** | Todas las leyes físicas (no sólo las mecánicas) son localmente iguales en un marco en caída libre |
### La gravedad como espacio-tiempo curvo
La idea central de la relatividad general: la masa y la energía curvan el espacio-tiempo, y los objetos siguen los caminos más rectos posibles (geodésicas) a través del espacio-tiempo curvo.
**Ecuaciones de campo de Einstein:**
G_μν + Λg_μν = (8πG/c⁴) T_μν
| Símbolo | Significado |
|--------|---------|
| G_μν | Tensor de Einstein (codifica la curvatura del espacio-tiempo) |
| Λ | Constante cosmológica (energía oscura) |
| g_μν | Tensor métrico (describe la geometría del espacio-tiempo) |
| GRAMO | Constante gravitacional de Newton |
| T_μν | Tensor tensión-energía (contenido de materia y energía) |
**Resumen de John Wheeler:** "El espacio-tiempo le dice a la materia cómo moverse; la materia le dice al espacio-tiempo cómo curvarse".
### Predicciones de la Relatividad General
| Predicción | Descripción | ¿Confirmado? |
|-----------|-------------|------------|
| Dilatación del tiempo gravitacional | Los relojes funcionan más lento en campos gravitacionales más fuertes | Sí (el GPS requiere corrección) |
| Lentes gravitacionales | La luz se curva alrededor de objetos masivos | Sí (Eddington 1919, imágenes del Hubble) |
| Desplazamiento al rojo gravitacional | La luz pierde energía al salir de los pozos de gravedad | Sí (Pound-Rebka 1959) |
| Agujeros negros | Regiones donde la curvatura del espacio-tiempo impide que la luz se escape | Sí (LIGO, EHT 2019) |
| Ondas gravitacionales | Ondas en el espacio-tiempo debido a masas en aceleración | Sí (LIGO 2015) |
| La precesión del perihelio de Mercurio | 43 segundos de arco adicionales por siglo | Sí (anomalía explicada desde 1859) |
| Arrastre de cuadros | Masas en rotación arrastran el espacio-tiempo a su alrededor | Sí (Sonda de gravedad B 2011) |
### Métrica de Schwarzschild
La solución más simple para un agujero negro (no giratorio, sin carga):
ds² = −(1 − 2GM/rc²)c²dt² + (1 − 2GM/rc²)⁻¹dr² + r²dΩ²
**Radio de Schwarzschild:** r_s = 2GM/c²
| Objeto | Misa | r_s |
|--------|------|-----|
| Tierra | 6 × 10²⁴ kg | 9 milímetros |
| Sol | 2 × 10³⁰ kg | 3 kilómetros |
| Sgr A* (centro de la Vía Láctea) | 4 × 10⁶ M☉ | 12 millones de kilómetros |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto de relatividad | Solicitud |
|-------------------|-------------|
| Transformaciones de Lorentz | Redes neuronales equivalentes de Lorentz, modelos con reconocimiento de simetría |
| Geometría del espacio-tiempo | Aprendizaje profundo geométrico, aprendizaje múltiple |
| Cuatro vectores | Notación tensorial utilizada en simulaciones de física relativista |
| Dilatación del tiempo gravitacional | Correcciones GPS (servicios basados ​​en ubicación, ML geoespacial) |
| Lentes gravitacionales | Análisis de datos astronómicos, mapeo de materia oscura |
| Relatividad general | Redes neuronales basadas en la física para la detección de ondas gravitacionales |
| Geometría riemanniana | Descenso de gradiente natural (geometría de la información), optimización múltiple |
| Tensor métrico | Define distancias en espacios curvos: fundamental para el aprendizaje múltiple |
| Geodésicas | Caminos más cortos en colectores: utilizados en robótica, incrustación de gráficos |
| Cálculo tensorial | Fundación para comprender variedades de datos de alta dimensión |
---

## Resumen
| Concepto | Idea central | Ecuación clave |
|---------|-----------|-------------|
| Relatividad especial | El espacio y el tiempo están unificados; c es absoluto | Transformaciones de Lorentz |
| Dilatación del tiempo | Los relojes en movimiento funcionan lento | Δt = γΔt₀ |
| Contracción de longitud | Los objetos en movimiento se acortan | L = L₀/γ |
| Masa-energía | Masa y energía son equivalentes | mi = mc² |
| Cuatro vectores | Descripciones del espacio-tiempo unificado | Intervalo invariante ds² |
| Principio de equivalencia | Gravedad = aceleración local | Fundación de GR |
| Relatividad general | La gravedad es espacio-tiempo curvo | G_μν = (8πG/c⁴)T_μν |
| Geodésicas | Los objetos siguen caminos más rectos en el espacio-tiempo curvo | Camino más corto en el colector |
La relatividad reformuló nuestra comprensión de los aspectos más fundamentales de la realidad: el espacio, el tiempo, la masa, la energía y la gravedad. Sus herramientas matemáticas (tensores, variedades, geodésicas, espacios métricos) han migrado mucho más allá de la física hacia el aprendizaje automático, donde impulsan el aprendizaje profundo geométrico, los métodos de gradiente natural y los algoritmos de aprendizaje múltiple.