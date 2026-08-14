<!--
---
# Metadata
title: "Signal Processing"
description: "Fourier transforms, FFT, Laplace transforms, Z-transforms, filtering, sampling theorem, windowing, spectral analysis, and wavelets"
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
    changes: "Initial deep-dive into signal processing"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [signal-processing, fourier-transform, fft, laplace-transform, z-transform, filtering, sampling-theorem, wavelets]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "optics_and_waves.md"
  - "numerical_methods.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Procesamiento de señales
El procesamiento de señales es la ciencia de analizar, modificar y sintetizar señales: representaciones de cantidades físicas que varían en el tiempo, el espacio o la frecuencia. Audio, imágenes, vídeo, datos de sensores, ondas cerebrales, precios de acciones: todos son señales. Las herramientas matemáticas del procesamiento de señales (transformadas de Fourier, filtros, teoría de muestreo) son fundamentales para el aprendizaje automático, las comunicaciones, las imágenes médicas y prácticamente todos los campos que trabajan con datos.
---

## Señales y Sistemas
### Clasificación de señal
| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Tiempo continuo** | Definido para todo t ∈ ℝ | Voltaje de audio, temperatura |
| **Tiempo discreto** | Definido en índices enteros n | Audio muestreado, valores de píxeles |
| **Analógico** | Continuo en tiempo y amplitud | Ranura de disco de vinilo |
| **Digital** | Discreto en el tiempo y amplitud cuantificada | Archivo MP3, imagen JPEG |
| **Periódico** | x(t + T) = x(t) para todo t | Onda sinusoidal, onda cuadrada |
| **Aperiódico** | Sin patrón repetitivo | Discurso, música |
| **Determinista** | Completamente predecible | Onda sinusoidal |
| **Estocástico** | Contiene aleatoriedad | Ruido, precios de las acciones |
### Propiedades del sistema
| Propiedad | Definición | Ejemplo |
|----------|-----------|---------|
| **Lineal** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Filtro de paso bajo |
| **Invariante en el tiempo** | Cambio en la entrada → mismo cambio en la salida | Cualquier filtro fijo |
| **Causal** | La producción depende sólo de los insumos presentes y pasados ​​| Sistema en tiempo real |
| **Estable (BIBO)** | Entrada limitada → salida limitada | Filtro bien diseñado |
| **Sin memoria** | La salida depende sólo de la entrada actual | Amplificador |
---

## Transformada de Fourier
La **transformada de Fourier** descompone una señal en sus frecuencias constituyentes.
### Transformada continua de Fourier
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Inversa: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Pares de transformada de Fourier
| Dominio del tiempo x(t) | Dominio de frecuencia X(f) |
|-------------------|----------------------|
| Pulso rectangular | función sinc |
| función sinc | Pulso rectangular |
| Gaussiano e^{−at²} | Gaussiano (√(π/a))e^{−π²f²/a} |
| Delta de Dirac δ(t) | 1 (todas las frecuencias) |
| Exponencial compleja e^{j2πf₀t} | δ(f − f₀) |
| Coseno cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Propiedades clave
| Propiedad | Dominio del tiempo | Dominio de frecuencia |
|----------|-------------|-----------------|
| Linealidad | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Cambio de tiempo | x(t − t₀) | X(f)e^{−j2πft₀} |
| Cambio de frecuencia | x(t)e^{j2πf₀t} | X(f − f₀) |
| Convolución | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Multiplicación | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Diferenciación | dx/dt | j2πfX(f) |
| Teorema de Parseval | ∫\|x(t)\|² dt | ∫\|X(f)\|² gl |
**Teorema de convolución:** Convolución en el tiempo = multiplicación en frecuencia. Esta es la propiedad más importante: convierte costosas operaciones de convolución en multiplicaciones baratas.
### Transformada discreta de Fourier (DFT)
Para una secuencia x[0], x[1], ..., x[N−1]:
X[k] = Σ_{n=0}^{N-1} x[n] e^{-j2πkn/N}, k = 0, 1, ..., N-1
| Propiedad | Valor |
|----------|-------|
| Entrada | N muestras reales o complejas |
| Salida | N contenedores de frecuencia complejos |
| Resolución de frecuencia | f_s/N (donde f_s es la frecuencia de muestreo) |
| Frecuencia de Nyquist | f_s/2 (frecuencia máxima representable) |
| Complejidad | Cálculo directo O(N²) |
### Transformada rápida de Fourier (FFT)
La **FFT** calcula la DFT en O(N log N) en lugar de O(N²).
| norte | Operaciones O(N²) | O(N log N) Operaciones | Aceleración |
|---|------------------|----------------------|---------|
| 1.024 | 1.048.576 | 10.240 | 102 × |
| 1.048.576 | 1,1 × 10¹² | 20.971.520 | 52,428 × |
La FFT es uno de los algoritmos más importantes jamás inventados. Permite procesamiento de audio en tiempo real, compresión de imágenes (JPEG), comunicación inalámbrica (OFDM) y análisis espectral.
---

## Transformada de Laplace
La **transformada de Laplace** amplía la transformada de Fourier para manejar sistemas inestables y análisis transitorios.
F(s) = ∫₀^∞ f(t) e^{−st} dt, donde s = σ + jω
### Transformadas de Laplace comunes
| f(t) | F(es) | Región de Convergencia |
|------|------|----------------------|
| δ(t) (impulso) | 1 | Todos los s |
| u(t) (paso) | 1/s | Re(s) > 0 |
| mi^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| tⁿtu(t) | norte!/s^{n+1} | Re(s) > 0 |
| pecado(ωt)u(t) | ω/(s²+ω²) | Re(s) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Re(s) > 0 |
### Conexión a la transformada de Fourier
Cuando σ = 0 (s = jω), la transformada de Laplace se reduce a la transformada de Fourier. La transformada de Laplace proporciona una imagen más completa al incluir información sobre crecimiento/decaimiento (σ).
---

## Transformada Z
La **transformada Z** es el equivalente en tiempo discreto de la transformada de Laplace.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Transformadas Z comunes
| x[norte] | X(z) | República de China |
|------|------|-----|
| δ[norte] | 1 | Todos z |
| u[n] (paso) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z−a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| pecado(ω₀n)u[n] | z pecado(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Relación con otras transformaciones
| Transformar | Dominio | Variables |
|-----------|--------|----------|
| Fourier | Frecuencia continua | f o ω |
| Laplace | Frecuencia compleja | s = σ + jω |
| Transformada Z | Frecuencia compleja (discreta) | z = mi^{sT} |
El círculo unitario en el plano z (|z| = 1) corresponde a la transformada de Fourier.
---

## Filtros
Los filtros pasan o bloquean selectivamente ciertos componentes de frecuencia.
### Tipos de filtro
| Tipo | Pases | Bloques | Solicitud |
|------|--------|--------|-------------|
| **Paso bajo** | Bajas frecuencias | Altas frecuencias | Suavizado, antialiasing |
| **Paso alto** | Altas frecuencias | Bajas frecuencias | Detección de bordes, eliminación de ruido |
| **Paso de banda** | Una gama de frecuencias | Fuera del rango | Selección de canal (radio) |
| **Parada de banda (muesca)** | Todo excepto una gama | Una gama específica | Eliminación de zumbidos en líneas eléctricas |
### Filtros FIR frente a IIR
| Propiedad | FIR (Respuesta de Impulso Finito) | IIR (Respuesta de Impulso Infinito) |
|----------|-------------------------------|--------------------------------|
| Respuesta al impulso | Duración finita | Duración infinita |
| Estabilidad | Siempre estable | Puede ser inestable |
| Fase | Puede ser exactamente lineal | Fase generalmente no lineal |
| Comentarios | No | Sí |
| Computación | Se necesitan más coeficientes | Menos coeficientes para la misma reducción |
| Diseño | Ventanas, Parques-McClellan | Butterworth, Chebyshev, elíptica |
| Función de transferencia | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Especificaciones de diseño del filtro
| Parámetro | Descripción |
|-----------|-------------|
| **Pasa de banda** | Rango de frecuencia que debería pasar con una pérdida mínima |
| **Banda de parada** | Rango de frecuencia que debe atenuarse |
| **Frecuencia de corte** | Límite entre banda de paso y banda de exclusión |
| **Ondulación** | Variación de la ganancia de la banda de paso (o banda de parada) |
| **Descenso** | Tasa de atenuación (dB por octava o década) |
| **Banda de transición** | Región entre banda de paso y banda de parada |
### Diseños de filtros comunes
| Diseño | Características | Caso de uso |
|--------|----------------|----------|
| **Butterworth** | Banda de paso máximamente plana, caída moderada | Propósito general |
| **Chebyshev Tipo I** | Ondulación en la banda de paso, caída más pronunciada | Cuando la reducción importa |
| **Chebyshev Tipo II** | Ondulación en banda de parada, banda de paso plana | Cuando la planitud de la banda de paso importa |
| **Elíptica (Cauer)** | Ondulación en ambos, caída más pronunciada | Pedido mínimo necesario |
| **Bessel** | Fase lineal (retardo de grupo máximo plano) | Preservar la forma de onda |
---

## Teoría del muestreo
### Teorema de muestreo de Nyquist-Shannon
Una señal continua se puede reconstruir perfectamente a partir de sus muestras si la frecuencia de muestreo supera el doble de la frecuencia máxima:
f_s > 2f_max
| Término | Definición |
|------|------------|
| **Tasa de muestreo** (f_s) | Número de muestras por segundo |
| **Tasa Nyquist** | 2f_max (frecuencia de muestreo mínima) |
| **Frecuencia de Nyquist** | f_s/2 (frecuencia máxima representable) |
| **Alias** | Altas frecuencias disfrazadas de bajas frecuencias cuando f_s < 2f_max |
### Tasas de muestreo comunes
| Solicitud | Tarifa | Frecuencia de Nyquist |
|-------------|------|-------------------|
| Discurso telefónico | 8kHz | 4kHz |
| CD de audio | 44,1 kHz | 22,05 kHz |
| Audio profesional | 48 kHz | 24 kHz |
| Audio de alta resolución | 96 kHz | 48 kHz |
| Vídeo (30 fps) | 30 Hz (temporales) | 15Hz |
### Antialiasing
Antes del muestreo, un **filtro antialiasing** (paso bajo) elimina las frecuencias superiores a f_s/2 para evitar el aliasing.
---

## Ventanas
Al analizar un segmento finito de una señal, implícitamente lo multiplicamos por una ventana rectangular, lo que provoca una fuga espectral. **Las funciones de ventana** reducen esta fuga.
### Ventanas comunes
| Ventana | Ancho del lóbulo principal | Nivel del lóbulo lateral | Caso de uso |
|--------|----------------|-----------------|----------|
| Rectángulos | Más estrecho | −13dB | Cuando la resolución es más importante |
| Hann | 2×rectangulares | −31dB | Propósito general |
| Hamming | 2×rectangulares | −41dB | Lóbulo lateral más cercano reducido |
| hombre negro | 3×rectangulares | −58dB | Alto rango dinámico |
| Káiser | Ajustable | Ajustable (vía β) | Cuando la compensación es ajustable |
### Fuga espectral
Al multiplicar una señal por una ventana, su espectro convoluciona con el espectro de la ventana. Los lóbulos principales más anchos reducen la resolución de frecuencia; Los lóbulos laterales inferiores reducen las fugas.
---

## Ondas
**Wavelets** son funciones pequeñas y localizadas similares a ondas que se utilizan para el análisis de señales de resolución múltiple.
### Transformada Wavelet
A diferencia de la transformada de Fourier (que proporciona información de frecuencia global), la transformada wavelet proporciona una localización **tiempo-frecuencia**.
| Transformar | Resolución de tiempo | Resolución de frecuencia |
|-----------|----------------|---------------------|
| Fourier | Ninguno (global) | Excelente |
| FT a corto plazo | Fijo (tamaño de ventana) | Fijo |
| Ondícula | Variable (buena a alta frecuencia) | Variable (buena a baja frecuencia) |
### Familias Wavelet comunes
| Familia | Propiedades | Solicitud |
|--------|-----------|-------------|
| **Pelo** | Más simple, discontinuo | Detección de bordes, análisis rápido |
| **Daubechies** (dbN) | Soporte compacto, N momentos de fuga | Compresión, eliminación de ruido |
| **Símbolos** | Daubechies casi simétricos | Distorsión de fase reducida |
| **Cofias** | Diseñado para condiciones de momento | Procesamiento de señales |
| **Morlet** | Sinusoide de ventana gaussiana | Análisis tiempo-frecuencia |
| **Sombrero mexicano** | Segunda derivada de Gaussiano | Detección de características |
### Aplicaciones de las Wavelets
| Solicitud | Cómo ayudan las wavelets |
|-------------|-------------------|
| Compresión de imágenes (JPEG 2000) | Representación multiresolución, mejor que DCT para bordes |
| Eliminación de ruido | Umbral de coeficientes wavelet pequeños (la señal está en coeficientes grandes) |
| Detección de características | Detección de bordes, detección de transitorios en series temporales |
| Análisis de ECG | Detección de complejos QRS, clasificación de arritmias |
| Análisis sísmico | Identificación de capas geológicas, procesamiento de señales de terremotos |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto de procesamiento de señales | Solicitud |
|--------------------|-------------|
| Transformada de Fourier | Características espectrales para audio ML, análisis en el dominio de la frecuencia de series temporales |
| FFT | Convolución rápida en CNN (convolución espectral), correlación eficiente |
| Teorema de convolución | Entendiendo cómo funcionan las CNN (son filtros aprendidos) |
| Filtros | Preprocesamiento (suavizado, eliminación de ruido), extracción de características |
| Teorema de muestreo | Comprender la discretización, elegir velocidades de sensores y evitar el aliasing |
| Ventanas | STFT para audio ML (espectrogramas), análisis tiempo-frecuencia |
| Ondas | Extracción de características para series temporales, compresión, eliminación de ruido |
| Transformada de Laplace/Z | Teoría de control para robótica, comprensión de la estabilidad del sistema |
| Análisis espectral | Análisis EEG/fMRI, monitorización de vibraciones, mantenimiento predictivo |
| Tasa de Nyquist | Elección de tasas de recopilación de datos adecuadas para canales de ML |
---

## Resumen
| Herramienta | Dominio | Información clave |
|------|--------|-------------|
| Transformada de Fourier | Hora → Frecuencia | Las señales son sumas de sinusoides |
| Transformada de Laplace | Tiempo → Frecuencia compleja | Maneja transitorios y estabilidad |
| Transformada Z | Tiempo discreto → Complejo | Análisis y diseño de filtros digitales |
| FFT | Cálculo DFT eficiente | O(N log N) en lugar de O(N²) |
| Filtros | Selección de frecuencia | Pasa lo que necesitas, bloquea lo que no |
| Teorema de muestreo | Continuo ↔ discreto | Pruebe lo suficientemente rápido, no pierda nada |
| Ventanas | Compensación tiempo-frecuencia | Resolución de saldos y fugas |
| Ondas | Análisis de resolución múltiple | Local tanto en horario como en frecuencia |
El procesamiento de señales proporciona la base matemática para comprender, analizar y manipular datos. Cada canal de aprendizaje automático que trabaja con series temporales, audio, imágenes o datos de sensores utiliza implícitamente conceptos de procesamiento de señales. La transformada de Fourier, en particular, es posiblemente la herramienta matemática más importante después del cálculo para cualquier científico de datos.