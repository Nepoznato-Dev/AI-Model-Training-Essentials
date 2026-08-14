---
# Metadata
title: "Control Theory"
description: "Transfer functions, block diagrams, feedback loops, PID controllers, stability analysis, state-space representation, and optimal control"
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
    changes: "Initial deep-dive into control theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [control-theory, transfer-functions, pid-controllers, feedback, stability, state-space, optimal-control]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "signal_processing.md"
  - "dynamical_systems.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Teoría del control
La teoría del control es la matemática necesaria para hacer que los sistemas se comporten como usted desea. Desde termostatos hasta pilotos automáticos, desde brazos robóticos hasta reactores químicos, los sistemas de control detectan, deciden y actúan para mantener el comportamiento deseado. Este campo proporciona herramientas rigurosas para analizar la estabilidad, el rendimiento y la solidez, conceptos que han migrado al aprendizaje por refuerzo, el ajuste de hiperparámetros y los sistemas adaptativos.
---

## Conceptos fundamentales
### Circuito abierto frente a circuito cerrado
| Tipo | Descripción | Ejemplo | Ventaja |
|------|-------------|---------|-----------|
| **Bucle abierto** | Acción de control independiente de la producción | Temporizador de lavadora | Sencillo, no necesita sensor |
| **Circuito cerrado (retroalimentación)** | La acción de control depende de la producción | Termostato, control de crucero | Rechaza perturbaciones, robusto |
### Elementos del diagrama de bloques
| Elemento | Símbolo | Función |
|---------|--------|----------|
| **Planta** | G(es) | El sistema que se controla |
| **Controlador** | C(es) | Calcula la acción de control |
| **Sensor** | H(es) | Mide la salida |
| **Unión sumadora** | ⊕ | Error de cálculo: r − y |
| **Referencia** | r(t)| Salida deseada |
| **Error** | mi(t) = r(t) − y(t) | Diferencia entre deseado y real |
| **Perturbación** | d(t) | Insumos no deseados que afectan a la planta |
### Función de transferencia de circuito cerrado
Para un sistema de retroalimentación negativa estándar:
T(s) = C(s)G(s) / (1 + C(s)G(s)H(s))
| Cantidad | Fórmula |
|----------|---------|
| Función de transferencia de bucle abierto | L(s) = C(s)G(s)H(s) |
| Función de transferencia en circuito cerrado | T(s) = L(s)/H(s) / (1 + L(s)) |
| Función de transferencia de errores | E(s)/R(s) = 1 / (1 + L(s)) |
| Sensibilidad | S(s) = 1 / (1 + L(s)) |
---

## Funciones de transferencia
Una **función de transferencia** H(s) = Y(s)/X(s) describe la relación entrada-salida de un sistema lineal invariante en el tiempo (LTI) en el dominio de Laplace.
### Formularios estándar
| Sistema | Función de transferencia | Parámetros |
|--------|-------------------|------------|
| **Primer orden** | K/(τs + 1) | K = ganancia, τ = constante de tiempo |
| **Segundo orden** | Kωₙ²/(s² + 2ζωₙs + ωₙ²) | ωₙ = frecuencia natural, ζ = relación de amortiguación |
| **Integrado** | K/s | — |
| **Diferenciador** | ks | — |
| **Retraso** | mi^{−sT_d} | T_d = retardo de tiempo |
### Comportamiento del sistema de segundo orden
| Relación de amortiguación ζ | Comportamiento | Ubicaciones de postes |
|-----------|-----------|---------------|
| ζ = 0 | Oscilación no amortiguada | Puro imaginario |
| 0< ζ < 1 | Underdamped (oscillates, decays) | Complex with negative real part |
| ζ = 1 | Critically damped (fastest no-oscillation) | Real, repeated |
| ζ >1 | Sobreamortiguado (lento, sin oscilación) | Real, distinto |
### Métricas de rendimiento (respuesta al paso)
| Métrica | Fórmula (segundo orden, subamortiguada) | Descripción |
|--------|----------------------------------|-------------|
| Tiempo de subida (t_r) | ≈ 1,8/ωₙ | Es hora de pasar del 10% al 90% |
| Hora punta (t_p) | π/(ωₙ√(1−ζ²)) | Tiempo hasta el primer máximo |
| Sobreimpulso (M_p) | mi^{−πζ/√(1−ζ²)} × 100% | Pico máximo por encima del valor final |
| Tiempo de asentamiento (t_s) | ≈ 4/(ζωₙ) | Es hora de mantenerse dentro del 2% del final |
| Error de estado estacionario | Depende del tipo de sistema | Diferencia entre deseado y real como t → ∞ |
---

## Controladores PID
El **controlador PID** es el controlador más utilizado en la industria (más del 90% de los controladores industriales).
### Fórmula PID
u(t) = K_p e(t) + K_i ∫₀ᵗ e(τ)dτ + K_d de(t)/dt
En el dominio de Laplace: C(s) = K_p + K_i/s + K_d s
| Término | Efecto | Demasiado | Muy poco |
|------|--------|----------|------------|
| **Proporcional (K_p)** | Reacciona al error actual | Oscilación, inestabilidad | Respuesta lenta, gran error |
| **Integral (K_i)** | Elimina el error de estado estacionario | Sobreimpulso, oscilación | Compensación persistente |
| **Derivada (K_d)** | Predice errores futuros (amortiguación) | Amplificación de ruido | Pobre rechazo de perturbaciones |
### Métodos de ajuste PID
| Método | Enfoque |
|--------|----------|
| **Ziegler-Nichols** | Incrementar K_u hasta oscilación; utilice K_u y el período P_u para establecer ganancias |
| **Cohen-Coon** | Basado en parámetros de respuesta al escalón (ganancia, constante de tiempo, tiempo muerto) |
| **IMC (Control de modelo interno)** | Basado en el modelo de proceso; proporciona buena robustez |
| **Sintonización automática** | Identificación online + sintonización (muchos controladores modernos) |
| **Manual** | Comience solo con K_p, agregue K_i para eliminar el desplazamiento, agregue K_d para amortiguar |
### Reglas de Ziegler-Nichols
1. Establecer K_i = K_d = 0
2. Incrementar K_p hasta oscilación sostenida: ganancia final K_u, período P_u
3. Establecer ganancias:
| Controlador | K_p | k_i | K_d |
|-----------|-----|-----|-----|
| P | 0.5K_u | — | — |
| IP | 0.45K_u | 1.2K_u/P_u | — |
| PID | 0.6K_u | 2K_u/P_u | K_u P_u/8 |
---

## Análisis de estabilidad
Un sistema es **estable** si su salida permanece limitada para las entradas limitadas (estabilidad BIBO).
### Estabilidad basada en postes
| Condición | Estabilidad |
|-----------|-----------|
| Todos los polos en el semiplano izquierdo (Re(s)< 0) | Stable |
| Any pole in right half-plane (Re(s) >0) | Inestable |
| Polos sobre eje imaginario (Re(s) = 0) | Marginalmente estable (o inestable si se repite) |
### Criterio de Routh-Hurwitz
Determina la estabilidad sin calcular los polos explícitamente. Construye la matriz de Routh a partir de los coeficientes polinomiales característicos.
**Regla:** El número de cambios de signo en la primera columna es igual al número de polos del semiplano derecho.
### Criterio de estabilidad de Nyquist
Traza la respuesta de frecuencia de bucle abierto L(jω) en el plano complejo.
**Regla:** El sistema de circuito cerrado es estable si el diagrama de Nyquist rodea el punto (−1, 0) en sentido antihorario un número de veces igual al número de polos inestables de circuito abierto.
**Margen de ganancia:** Cuánto puede aumentar la ganancia antes de la inestabilidad (distancia del gráfico a −1 en el eje real).
**Margen de fase:** Cuánto puede aumentar el desfase antes de la inestabilidad (ángulo desde el gráfico hasta el círculo unitario en el cruce de ganancia).
### Análisis de la trama de Bode
Traza la ganancia (dB) y la fase (grados) frente a la frecuencia (escala logarítmica).
| Métrica | Definición | Valor deseado |
|--------|-----------|---------------|
| **Margen de ganancia (GM)** | Aumento de ganancia para alcanzar 0 dB en fase = −180° | > 6dB |
| **Margen de fase (PM)** | Fase en el cruce de ganancia (0 dB) + 180° | > 45° |
| **Cruce de ganancia** | Frecuencia donde ganancia = 0 dB | — |
| **Cruce de fase** | Frecuencia donde fase = −180° | — |
---

## Representación del espacio de estados
Para los sistemas de múltiples entradas y múltiples salidas (MIMO), la forma del espacio de estados es más natural que las funciones de transferencia.
### Formulario estándar
ẋ(t) = Ax(t) + Bu(t) (ecuación de estado)
y(t) = Cx(t) + Du(t) (ecuación de salida)
| Matriz | Nombre | Dimensiones |
|--------|------|-----------|
| Un | Matriz sistema/estado | norte × norte |
| B | Matriz de entrada | norte × metro |
| C | Matriz de salida | p × norte |
| D | Matriz de paso | p×m |
### Función de transferencia desde el espacio de estados
G(s) = C(sI − A)⁻¹B + D
### Controlabilidad y observabilidad
| Propiedad | Prueba | Significado |
|----------|------|---------|
| **Controlable** | Rango[C_B] = n (donde C_B = [B, AB, A²B, ...]) | Puede dirigirse a cualquier estado |
| **Observables** | Rango[O_B] = n (donde O_B = [C; CA; CA²; ...]) | Puede determinar el estado a partir de la salida |
Un sistema debe ser controlable para ser estabilizable mediante retroalimentación y observable para la estimación del estado.
### Comentarios del estado
u = −Kx + r (retroalimentación de estado completo)
Bucle cerrado: ẋ = (A − BK)x + Br
**Colocación de polos:** Elija K de modo que A − BK tenga los valores propios deseados (polos).
---

## Control óptimo
### Regulador cuadrático lineal (LQR)
Minimizar: J = ∫₀^∞ (xᵀQx + uᵀRu) dt
donde Q ≥ 0 (costo estatal) y R > 0 (costo de control).
**Solución:** u = −Kx donde K = R⁻¹BᵀP, y P resuelve la **ecuación algebraica de Riccati:**
AᵀP + PA − PBR⁻¹BᵀP + Q = 0
| Sintonización | Efecto |
|--------|--------|
| Aumentar Q | Respuesta más rápida, mayor esfuerzo de control |
| Aumentar R | Respuesta más lenta, menos esfuerzo de control |
| Q≫R | Control agresivo (como K_p alto) |
### Filtro Kalman
El estimador de estado óptimo para sistemas lineales con ruido gaussiano.
**Modelo del sistema:**
ẋ = Ax + Bu + w (ruido de proceso w ~ N(0, Q))
y = Cx + v (ruido de medición v ~ N(0, R))
**Ecuaciones del filtro de Kalman:**
- Predecir: x̂⁻ = Ax̂ + Bu, P⁻ = APAᵀ + Q
- Actualización: K = P⁻Cᵀ(CP⁻Cᵀ + R)⁻¹, x̂ = x̂⁻ + K(y − Cx̂⁻), P = (I − KC)P⁻
El filtro de Kalman es el LQR dual: minimiza la variación del error de estimación.
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto de teoría del control | Solicitud |
|----------------------|-------------|
| Control de retroalimentación | Tasas de aprendizaje adaptativo, estabilización del entrenamiento |
| Controladores PID | Ajuste de hiperparámetros, control de temperatura en centros de datos |
| Modelos de espacio de estados | Modelado de series temporales, redes neuronales recurrentes |
| Filtro de Kalman | Seguimiento, fusión de sensores, estimación de estado, previsión de series temporales |
| LQR / control óptimo | Aprendizaje por refuerzo (control LQG), robótica |
| Análisis de estabilidad | Dinámica de entrenamiento de GAN, convergencia de algoritmos RL |
| Controlabilidad/observabilidad | Comprensión de la expresividad RNN, identificación del sistema |
| Funciones de transferencia | Entendiendo las CNN como filtros lineales, análisis en el dominio de la frecuencia |
| Nyquist/Bode | Análisis de robustez para sistemas adaptativos |
| Colocación de postes | Diseño de dinámicas de sistemas aprendidos (OED neuronales) |
---

## Resumen
| Concepto | Idea central | Herramienta clave |
|---------|-----------|----------|
| Comentarios | Utilice la salida para corregir la entrada | Función de transferencia en circuito cerrado |
| Función de transferencia | Relación entrada-salida en el dominio s | G(s) = Y(s)/X(s) |
| Control PID | Proporcional + Integral + Derivada | Controlador industrial más utilizado |
| Estabilidad | Salida acotada para entrada acotada | Routh-Hurwitz, Nyquist, Bode |
| Espacio de estados | Representación estatal interna | ẋ = Ax + Bu, y = Cx + Du |
| Controlabilidad | ¿Podemos llegar a cualquier estado? | Prueba de rango en matriz de controlabilidad |
| Observabilidad | ¿Podemos inferir el estado? | Prueba de rango en la matriz de observabilidad |
| LQR | Retroalimentación de estado óptimo | Ecuación de Riccati |
| Filtro de Kalman | Estimación del estado óptimo | Predecir el ciclo de actualización |
La teoría del control es la matemática para hacer que los sistemas hagan lo que usted quiere: confiable, robusto y eficiente. Sus principios de retroalimentación, estabilidad y optimización han demostrado ser universales y aparecen en campos que van desde la robótica hasta el aprendizaje por refuerzo, desde la economía hasta la biología. Para los científicos de datos, la teoría del control proporciona el lenguaje para comprender los sistemas adaptativos, diseñar procedimientos de entrenamiento estables y construir agentes inteligentes que interactúen con entornos dinámicos.