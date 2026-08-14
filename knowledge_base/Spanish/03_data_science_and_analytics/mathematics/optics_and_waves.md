---
# Metadata
title: "Optics and Waves"
description: "Wave equation, superposition, interference, diffraction, polarization, geometric optics, Fourier optics, and applications to signal processing and imaging"
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
    changes: "Initial deep-dive into optics and waves"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optics, waves, wave-equation, interference, diffraction, polarization, geometric-optics, fourier-optics]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "electromagnetism.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Óptica y Ondas
Las ondas están en todas partes: sonido, luz, agua, señales de radio, amplitudes de probabilidad cuántica, fluctuaciones del mercado de valores y vibraciones de activaciones de redes neuronales. La óptica (el estudio de la luz) es la ciencia ondulatoria mejor desarrollada y sus herramientas matemáticas (análisis de Fourier, interferencia, difracción) se aplican a todos los fenómenos ondulatorios. Comprender las ondas es esencial para el procesamiento de señales, el análisis de imágenes, las comunicaciones y la capa física de toda la tecnología moderna.
---

## La ecuación de onda
### Ecuación general de onda
La ecuación de onda unidimensional:
∂²u/∂t² = c² ∂²u/∂x²
donde u(x,t) es el desplazamiento de la onda y c es la velocidad de la onda.
### Solución general (d'Alembert)
u(x,t) = f(x − ct) + g(x + ct)
donde f es una onda que viaja hacia la derecha y g es una onda que viaja hacia la izquierda.
### Parámetros de onda clave
| Parámetro | Símbolo | Unidad | Descripción |
|-----------|--------|------|-------------|
| Amplitud | Un | varía | Desplazamiento máximo |
| Longitud de onda | λ | metros | Distancia entre crestas consecutivas |
| Frecuencia | f o ν | Hercios (Hz) | Ciclos por segundo |
| Periodo | T = 1/f | segundos | Tiempo para un ciclo completo |
| Número de onda | k = 2π/λ | rad/m | Frecuencia espacial |
| Frecuencia angular | ω = 2πf | rad/s | Frecuencia temporal |
| Velocidad de onda | c = fλ = ω/k | m/s | Velocidad de propagación |
### Onda sinusoidal
u(x,t) = A pecado(kx − ωt + φ)
donde φ es la constante de fase.
### Velocidad de onda en diferentes medios
| Tipo de onda | Medio | Fórmula de velocidad |
|-----------|--------|---------------|
| Cadena | Tensión T, densidad lineal μ | c = √(T/μ) |
| Sonido | Módulo volumétrico B, densidad ρ | c = √(B/ρ) |
| Sonido (gas ideal) | γ, R, T, M | c = √(γRT/M) |
| Onda EM | Permitividad ε, permeabilidad μ | c = 1/√(με) |
| Onda EM (vacío) | ε₀, μ₀ | c = 3 × 10⁸ m/s |
---

## Superposición e interferencia
### Principio de superposición
Cuando dos o más ondas se superponen, el desplazamiento resultante es la suma de los desplazamientos individuales:
u_total = u₁ + u₂ + ... + uₙ
Esto es válido para ecuaciones de ondas lineales.
### Interferencia de dos ondas
Dos ondas con la misma frecuencia y amplitud, diferencia de fase Δφ:
u_total = 2A cos(Δφ/2) sin(kx − ωt + Δφ/2)
| Diferencia de fase | Resultado | Intensidad |
|-----------------|--------|-----------|
| Δφ = 0, 2π, 4π, ... | **Constructivo** (amplitud = 2A) | 4I₀ (máximo) |
| Δφ = π, 3π, 5π, ... | **Destructivo** (amplitud = 0) | 0 (mínimo) |
| Δφ = π/2 | Parcial | 2I₀ |
### Condiciones de interferencia
| Condición | Tipo | Diferencia de ruta |
|-----------|--------------|-----------------|
| Constructivo | Franja brillante | ΔL = mλ (m = 0, 1, 2, ...) |
| Destructivo | franja oscura | ΔL = (m + ½)λ |
---

## Experimento de la doble rendija de Young
La luz pasa a través de dos rendijas estrechas separadas por una distancia d, creando un patrón de interferencia en una pantalla a una distancia L.
### Posiciones marginales
| Franja | Posición en pantalla |
|--------|-------------------|
| Brillante (máxima) | y_m = mλL/d |
| Oscuro (mínimo) | y_m = (m + ½)λL/d |
| Espaciado de franjas | Δy = λL/d |
Este experimento demostró la naturaleza ondulatoria de la luz (Thomas Young, 1801) y más tarde se convirtió en un elemento central de la mecánica cuántica (dualidad onda-partícula).
---

## Difracción
**Difracción** es la curvatura y propagación de ondas alrededor de obstáculos y a través de aberturas.
### Difracción de rendija única
La luz a través de una rendija de ancho a produce un patrón de franjas brillantes y oscuras.
| Característica | Condición |
|---------|-----------|
| Máximo central | Más amplio y brillante; ancho = 2λL/a |
| Mínimas (franjas oscuras) | a sen θ = mλ (m = ±1, ±2, ...) |
| Máximos secundarios | Aproximadamente entre mínimos; mucho más tenue |
### Rejilla de difracción
N rendijas equiespaciadas (espaciado d) producen máximos muy agudos:
d sen θ = mλ (m = 0, 1, 2, ...)
| Propiedad | Efecto |
|----------|--------|
| Más rendijas (N más grande) | Máximos más nítidos y brillantes |
| Poder de resolución | R = mN (puede distinguir longitudes de onda cercanas) |
| Aplicaciones | Espectroscopia, medición de longitudes de onda |
### Criterio de Rayleigh (límite de resolución)
Dos fuentes puntuales se pueden resolver simplemente cuando el máximo central de una cae sobre el primer mínimo de la otra:
θ_mín = 1,22 λ/D
donde D es el diámetro de apertura.
| Sistema | λ | D | θ_mín |
|--------|---|---|-------|
| Ojo humano | 550 nm | 5 milímetros | 1,3 × 10⁻⁴ rad (~0,01°) |
| Telescopio espacial Hubble | 550 nm | 2,4 metros | 2,8 × 10⁻⁷rad |
| Radiotelescopio (Arecibo) | 21cm | 305 metros | 8,4 × 10⁻⁴ rad |
---

## Polarización
**Polarización** describe la orientación de la oscilación del campo eléctrico en una onda transversal.
### Tipos de polarización
| Tipo | Descripción |
|------|-------------|
| **Lineal** | E oscila en un plano fijo |
| **Círculos** | E gira en círculo (para diestros o zurdos) |
| **Elíptica** | E traza una elipse (más general) |
| **Sin polarizar** | Mezcla aleatoria de todas las polarizaciones (la mayoría de la luz natural) |
### Ley de Malus
Cuando la luz polarizada pasa a través de un polarizador formando un ángulo θ con la dirección de polarización:
I = I₀ cos²θ
| Ángulo θ | Intensidad transmitida |
|---------|----------------------|
| 0° | 100% (I₀) |
| 30° | 75% |
| 45° | 50% |
| 60° | 25% |
| 90° | 0% (completamente bloqueado) |
### Polarización por reflexión (ángulo de Brewster)
La luz reflejada en el ángulo de Brewster está completamente polarizada:
tan θ_B = n₂/n₁
| Interfaz | norte₁ | norte₂ | θ_B |
|-----------|----|----|-----|
| Aire → vidrio | 1.0 | 1.5 | 56,3° |
| Aire → agua | 1.0 | 1,33 | 53,1° |
| Vidrio → diamante | 1.5 | 2,42 | 58,1° |
---

## Óptica Geométrica
La óptica geométrica (de rayos) trata la luz como rayos que viajan en línea recta y se doblan en las interfaces.
### Ley de Snell (Refracción)
n₁ sen θ₁ = n₂ sen θ₂
| Materiales | Índice de refracción n |
|----------|-------------------|
| Vacío | 1.000 |
| Aire | 1.0003 |
| Agua | 1,33 |
| Vidrio (corona) | 1,52 |
| Vidrio (pedernal) | 1,62 |
| Diamante | 2,42 |
### Reflexión interna total
Cuando la luz viaja de un medio más denso a un medio menos denso, más allá del **ángulo crítico**:
θ_c = arcosen(n₂/n₁)
Toda la luz se refleja: así funcionan las fibras ópticas.
### Ecuación de lente delgada
1/f = 1/d_o + 1/d_i
| Cantidad | Significado |
|----------|---------|
| f | Distancia focal |
| d_o | Distancia del objeto |
| d_i | Distancia de la imagen |
| M = −d_i/d_o | Ampliación |
| Tipo de lente | f | Imagen |
|-----------|---|-------|
| Convergente (convexo) | Positivo | Real (si d_o > f) o virtual |
| Divergente (cóncavo) | Negativo | Siempre virtual, erguido, reducido |
### Ecuación especular
Misma forma que la ecuación de la lente: 1/f = 1/d_o + 1/d_i, donde f = R/2 para espejos esféricos.
---

## Óptica Fourier
La óptica de Fourier trata la imagen y la difracción como operaciones de transformada de Fourier.
### Principio clave
El patrón de difracción de campo lejano de una apertura es la **transformada de Fourier** de la función de apertura.
| Apertura | Patrón de difracción (transformada de Fourier) |
|----------|----------------------------------------|
| Rendija única | función sinc |
| Apertura circular | Disco aireado (J₁(r)/r) |
| Apertura rectangular | sincronización 2D |
| Rejilla | Funciones delta discretas |
### Transformada óptica de Fourier
Una lente realiza una transformada de Fourier 2D: colocar un objeto en el plano focal frontal produce su transformada de Fourier en el plano focal posterior.
### Aplicaciones
| Solicitud | Cómo ayuda la óptica de Fourier |
|-------------|-------------------------|
| Filtrado de imágenes | Coloque máscaras en el plano de Fourier para bloquear/pasar frecuencias espaciales |
| Detección de bordes | Filtrado de paso alto en el plano de Fourier |
| Reconocimiento de patrones | Correlación mediante transformadas de Fourier |
| Holografía | Grabación y reconstrucción de frentes de onda |
| Computación óptica | Realizando transformadas de Fourier a la velocidad de la luz |
---

## Sonido y Acústica
### Propiedades de las ondas sonoras
| Propiedad | Rango típico | Unidad |
|----------|--------------|------|
| Frecuencia | 20 − 20.000 (audición humana) | Hz |
| Velocidad (aire, 20°C) | 343 | m/s |
| Velocidad (agua) | 1.480 | m/s |
| Velocidad (acero) | 5.960 | m/s |
| Umbral de intensidad | 10⁻¹² | W/m² |
### Escala de decibelios
β = 10 log₁₀(I/I₀) dB, donde I₀ = 10⁻¹² W/m²
| Sonido | Intensidad (W/m²) | Nivel (dB) |
|-------|-------------------|------------|
| Umbral de audición | 10⁻¹² | 0 |
| Hojas susurrantes | 10⁻¹¹ | 10 |
| Conversación normal | 10⁻⁶ | 60 |
| Concierto de rock | 1 | 120 |
| Umbral del dolor | 10 | 130 |
| Motor a reacción | 100 | 140 |
### Efecto Doppler
Frecuencia observada cuando la fuente y el observador se mueven entre sí:
f' = f(v ± v_o)/(v ∓ v_s)
| Escenario | Efecto |
|----------|--------|
| Fuente acercándose | Frecuencia más alta (desplazamiento hacia el azul para la luz) |
| Fuente retrocediendo | Frecuencia más baja (corrimiento al rojo para la luz) |
| Aplicaciones | Radar, ultrasonido médico, astronomía (desplazamiento al rojo de las galaxias) |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto de onda/óptica | Solicitud |
|---------------------|-------------|
| Ecuación de onda | Redes neuronales basadas en la física, análisis de datos sísmicos, procesamiento de audio |
| Análisis de Fourier | Fundamentos del procesamiento de señales, análisis espectral, extracción de características |
| Transformada de Fourier | Las CNN realizan implícitamente análisis de Fourier local; FFT utilizada en el preprocesamiento de datos |
| Interferencia | Computación analógica, redes neuronales ópticas |
| Difracción | Modelos de formación de imágenes, algoritmos de desenfoque, fotografía computacional |
| Polarización | Teledetección, clasificación de materiales, análisis de imágenes de satélite |
| Óptica geométrica | Modelos de cámaras en visión por computadora, trazado de rayos para generación de datos sintéticos |
| Ecuación de lentes | Calibración de cámara, estimación de profundidad, reconstrucción 3D |
| Óptica de Fourier | Computación óptica, redes neuronales profundas difractivas (D²NN) |
| Efecto Doppler | Procesamiento de señales radar, imágenes médicas (ultrasonido Doppler), estimación de velocidad |
| Escala de decibeles | Ingeniería de funciones de audio, preprocesamiento de reconocimiento de voz |
| Teoría del muestreo | El teorema de Nyquist-Shannon conecta la teoría de ondas con el procesamiento de señales digitales |
---

## Resumen
| Tema | Idea central | Ecuación clave |
|-------|-----------|-------------|
| Ecuación de onda | Las ondas se propagan a velocidad c | ∂²u/∂t² = c²∂²u/∂x² |
| Superposición | Las ondas se suman linealmente | tu = tu₁ + u₂ |
| Interferencia | Fase determina el refuerzo | Δφ = 2πΔL/λ |
| Difracción | Las olas rodean los obstáculos | a sin θ = mλ (rendija única) |
| Polarización | Orientación de la oscilación | Ley de Malus: I = I₀cos²θ |
| Óptica geométrica | Luz como rayos | Ley de Snell: n₁sinθ₁ = n₂sinθ₂ |
| Óptica de Fourier | Imágenes como transformada de Fourier | Campo lejano = pies de apertura |
| Efecto Doppler | Cambio de frecuencia debido al movimiento | f' = f(v ± v_o)/(v ∓ v_s) |
Las ondas son el lenguaje universal de los sistemas oscilantes. Ya sea que esté procesando señales de audio, analizando series temporales, diseñando sistemas de reconocimiento de imágenes o construyendo simulaciones físicas, las matemáticas de las ondas (superposición, análisis de Fourier, interferencia, difracción) proporcionan el conjunto de herramientas esencial. La óptica, como la ciencia ondulatoria más madura, ofrece tanto la base teórica como las técnicas prácticas que impregnan la ciencia de datos moderna.