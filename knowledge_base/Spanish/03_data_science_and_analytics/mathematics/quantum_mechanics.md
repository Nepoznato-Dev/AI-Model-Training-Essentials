---
# Metadata
title: "Quantum Mechanics"
description: "Wave-particle duality, Schrodinger equation, operators and observables, uncertainty principle, quantum states and superposition, entanglement, qubits, quantum gates, and relevance to quantum computing"
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
    changes: "Initial deep-dive into quantum mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [quantum-mechanics, schrodinger-equation, uncertainty-principle, superposition, entanglement, qubits, quantum-gates, quantum-computing]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Mecánica Cuántica
La mecánica cuántica es la teoría de la física en las escalas más pequeñas: átomos, electrones, fotones y las partículas fundamentales de la naturaleza. Reemplaza el mundo determinista de la mecánica clásica con probabilidades, superposiciones y entrelazamientos. A pesar de su naturaleza contraintuitiva, la mecánica cuántica es la teoría probada con mayor precisión en toda la ciencia. Hoy en día, sus principios se están volviendo directamente relevantes para la computación a través de computadoras cuánticas, que prometen resolver ciertos problemas exponencialmente más rápido que las máquinas clásicas.
---

## Motivación histórica
### Fallos de la Física Clásica
| Problema | Predicción clásica | Observación | Resolución |
|---------|---------------------|-------------|------------|
| Radiación de cuerpo negro | Catástrofe ultravioleta (energía infinita en λ corta) | Longitud de onda máxima finita | Planck: la energía se cuantifica (E = nhν) |
| Efecto fotoeléctrico | KE depende de la intensidad, no de la frecuencia | KE depende de la frecuencia | Einstein: la luz se cuantifica (fotones, E = hν) |
| Espectros atómicos | Espectro de emisión continua | Líneas espectrales discretas | Bohr: los electrones ocupan órbitas cuantificadas |
| Difracción de electrones | Las partículas no se difractan | Los electrones producen patrones de interferencia | de Broglie: las partículas tienen longitud de onda λ = h/p |
### Constantes clave
| Constante | Símbolo | Valor |
|----------|--------|-------|
| Constante de Planck | h | 6,626 × 10⁻³⁴ J·s |
| Constante de Planck reducida | ℏ = h/2π | 1,055 × 10⁻³⁴ J·s |
| Velocidad de la luz | c | 3,0 × 10⁸ m/s |
| Masa de electrones | yo_yo | 9,109 × 10⁻³¹ kg |
| Carga elemental | mi | 1,602 × 10⁻¹⁹ C |
| Radio de Bohr | un₀ | 5,292 × 10⁻¹¹ metro |
---

## Dualidad onda-partícula
### Longitud de onda de Broglie
Cada partícula con momento p tiene una longitud de onda asociada:
λ = h/p = h/(mv)
| Partícula | Típico λ | ¿Comportamiento observable de las ondas? |
|----------|-----------|---------------------|
| Electrón (100 eV) | 0,12 nm | Sí (difracción de cristales) |
| Protón | 0,003 nm | Sí (dispersión de neutrones) |
| Béisbol (40 m/s) | 10⁻³⁴ metro | No (demasiado pequeño para detectarlo) |
### Experimento de doble rendija
El experimento cuántico por excelencia:
1. Disparar partículas (electrones, fotones) una a la vez en dos rendijas
2. Cada partícula aterriza en un solo punto del detector.
3. Con el tiempo, surge un patrón de interferencia, como si cada partícula pasara por ambas rendijas simultáneamente.
4. Si mides por qué rendija pasa la partícula, el patrón de interferencia desaparece.
**Conclusión:** Los objetos cuánticos no son puramente partículas ni puramente ondas. Exhiben un comportamiento ondulatorio cuando no se observan y un comportamiento similar a una partícula cuando se miden.
---

## La función de onda
### Definición
La **función de onda** ψ(x, t) describe completamente un sistema cuántico. Es una función de valores complejos cuyo módulo cuadrado da la densidad de probabilidad:
P(x) = |ψ(x)|² = ψ*(x)ψ(x)
### Normalización
La probabilidad total debe ser igual a 1:
∫ |ψ(x)|² dx = 1 (en todo el espacio)
### Regla nacida
La probabilidad de encontrar la partícula entre x y x + dx:
P(x a x+dx) = |ψ(x)|² dx
Para un observable general con estados propios φₙ:
P(medición del valor propio aₙ) = |⟨φₙ|ψ⟩|²
---

## La ecuación de Schrödinger
### Ecuación de Schrodinger dependiente del tiempo
iℏ ∂ψ/∂t = Ĥψ
donde Ĥ es el **operador hamiltoniano** (operador de energía total).
### Ecuación de Schrodinger independiente del tiempo
Para estados estacionarios (estados propios de energía):
Ĥψ = Eψ
Esta es una ecuación de valores propios: las energías permitidas E son los valores propios de Ĥ.
### Partícula en una caja (pozo cuadrado infinito)
El sistema cuántico más simple: partícula confinada a 0 < x < L.
| Cantidad | Resultado |
|----------|--------|
| Funciones de onda | ψₙ(x) = √(2/L) sen(nπx/L) |
| Niveles de energía | Eₙ = n²π²ℏ²/(2mL²) = n²h²/(8mL²) |
| Estado fundamental | n = 1, E₁ = h²/(8mL²) |
| Energía de punto cero | E₁ > 0 (la partícula no puede estar perfectamente quieta) |
| Número cuántico | n = 1, 2, 3, ... (solo enteros positivos) |
### Oscilador armónico cuántico
V(x) = ½mω²x²
| Cantidad | Resultado |
|----------|--------|
| Niveles de energía | miₙ = (norte + ½)ℏω |
| Energía de punto cero | mi₀ = ½ℏω |
| Espaciado | ΔE = ℏω (uniforme) |
| Funciones de onda | Polinomios de Hermite × Gaussiano |
---

## Operadores y observables
En mecánica cuántica, cada observable físico corresponde a un **operador hermitiano**.
### Operadores clave
| Observables | Operador (espacio de posición) | Valores propios |
|-----------|--------------------|-------------|
| Posición | x̂ = x | Todo real x |
| Impulso | p̂ = −iℏ ∂/∂x | Todo real p |
| Energía (Hamiltoniano) | Ĥ = −(ℏ²/2m)∂²/∂x² + V(x) | Eₙ (discreto para estados vinculados) |
| Momento angular | L̂ = r × p̂ | ℏ√(l(l+1)) |
| Girar | Ŝ = (ℏ/2)σ (matrices de Pauli) | ±ℏ/2 (para centrifugado-½) |
### Valores esperados
El resultado promedio de medir el observable A en el estado ψ:
⟨A⟩ = ⟨ψ|Â|ψ⟩ = ∫ ψ*(x) Â ψ(x) dx
### Relaciones de conmutación
[Â, B̂] = ÂB̂ − B̂Â
| Conmutador | Resultado | Importancia |
|-----------|--------|-------------|
| [x̂, p̂] | yoℏ | Posición e impulso son incompatibles |
| [L̂ₓ, L̂ᵧ] | iℏL̂_z | Los componentes del momento angular son incompatibles |
| [σ̂ₓ, σ̂ᵧ] | 2iσ̂_z | Matrices de Pauli (componentes de espín) |
Si [Â, B̂] = 0, los observables se pueden medir simultáneamente (compartir estados propios).
---

## Principio de incertidumbre
### Principio de incertidumbre de Heisenberg
Δx · Δp ≥ ℏ/2
De manera más general, para dos observables A y B cualesquiera:
ΔA · ΔB ≥ (1/2)|⟨[Â, B̂]⟩|
### Relaciones de incertidumbre
| Par | Relación | Interpretación |
|------|----------|----------------|
| Posición-impulso | ΔxΔp ≥ ℏ/2 | No se pueden saber ambos con precisión |
| Tiempo de energía | ΔEΔt ≥ ℏ/2 | Los estados de corta duración tienen una energía incierta |
| Momento angular | ΔLₓΔLᵧ ≥ (ℏ/2)\|⟨L_z⟩\| | No se pueden conocer todos los componentes simultáneamente |
**Importante:** La incertidumbre no tiene que ver con la perturbación de la medición: es una propiedad fundamental de los estados cuánticos. Una partícula no tiene una posición y un momento definidos simultáneamente.
---

## Estados cuánticos y superposición
### Notación de Dirac (Bra-Ket)
| Símbolo | Nombre | Significado |
|--------|------|---------|
| \|ψ⟩ | ket | Vector de estado (vector de columna) |
| ⟨ψ\| | sujetador | Transposición conjugada (vector de fila) |
| ⟨φ\|ψ⟩ | Producto interior | Amplitud para ψ que se encontrará en el estado φ |
| \|ψ\|² | Norma al cuadrado | Probabilidad |
### Principio de superposición
Si \|ψ₁⟩ y \|ψ₂⟩ son estados cuánticos válidos, entonces cualquier combinación lineal también es válida:
\|ψ⟩ = α\|ψ₁⟩ + β\|ψ₂⟩

donde |α|² + |β|² = 1 (normalización).
**Medición:** Cuando se mide, el sistema "colapsa" a \|ψ₁⟩ con probabilidad |α|² o \|ψ₂⟩ con probabilidad |β|².
### Qubits
Un **qubit** es un bit cuántico: un sistema cuántico de dos niveles.
\|ψ⟩ = α\|0⟩ + β\|1⟩, donde |α|² + |β|² = 1
| Representación | \|0⟩ | \|1⟩ |
|---------------|------|------|
| Girar | Girar ↑ | Girar hacia abajo ↓ |
| Polarización de fotones | Horizontales | Verticales |
| Nivel de energía | Estado fundamental | Estado emocionado |
| Circuito | \|0⟩ = [1, 0]ᵀ | \|1⟩ = [0, 1]ᵀ |
**Esfera de Bloch:** Cualquier estado de qubit se puede escribir como:
\|ψ⟩ = cos(θ/2)\|0⟩ + e^{iφ} sin(θ/2)\|1⟩
donde θ ∈ [0, π] y φ ∈ [0, 2π). El espacio de estados es una esfera.
---

## Enredo
Dos qubits están **entrelazados** cuando su estado conjunto no puede escribirse como un producto de estados individuales.
### Estados de Bell (Máximamente entrelazados)
| Estado | Expresión | Nombre |
|-------|-----------|------|
| \|Φ⁺⟩ | (1/√2)(\|00⟩ + \|11⟩) | Estado de campana |
| \|Φ⁻⟩ | (1/√2)(\|00⟩ − \|11⟩) | Estado de campana |
| \|Ψ⁺⟩ | (1/√2)(\|01⟩ + \|10⟩) | Estado de campana |
| \|Ψ⁻⟩ | (1/√2)(\|01⟩ − \|10⟩) | Estado singlete |
### Propiedades del entrelazamiento
| Propiedad | Descripción |
|----------|-------------|
| Correlación | Medir un qubit determina instantáneamente el otro, independientemente de la distancia |
| Sin comunicación | No se puede utilizar el entrelazamiento por sí solo para enviar información más rápido que la luz |
| Monogamia | Si A está entrelazado al máximo con B, no puede entrelazarse con C |
| Fragilidad | La interacción con el medio ambiente destruye el entrelazamiento (decoherencia) |
### Paradoja EPR y teorema de Bell
Einstein, Podolsky y Rosen sostuvieron que la mecánica cuántica debe ser incompleta (variables ocultas). Bell demostró que cualquier teoría local de variables ocultas satisface ciertas desigualdades. Los experimentos violan las desigualdades de Bell, confirmando la mecánica cuántica y descartando variables locales ocultas.
---

## Puertas cuánticas
Las puertas cuánticas son operaciones unitarias en qubits.
### Puertas de un solo qubit
| Puerta | Matriz | Efecto |
|------|--------|--------|
| **Pauli-X** (NO) | [[0,1],[1,0]] | Inversión de bits: \|0⟩ ↔ \|1⟩ |
| **Pauli-Y** | [[0,-i],[i,0]] | Bit + cambio de fase |
| **Pauli-Z** | [[1,0],[0,-1]] | Cambio de fase: \|1⟩ → −\|1⟩ |
| **Hadamard** (H) | (1/√2)[[1,1],[1,−1]] | Crea superposición: \|0⟩ → (\|0⟩+\|1⟩)/√2 |
| **Fase** (S) | [[1,0],[0,i]] | Rotación π/2 alrededor de Z |
| **Puerta T** | [[1,0],[0,e^{iπ/4}]] | Rotación π/4 alrededor de Z |
| **Rotación** Rₓ(θ) | cos(θ/2)I − i sin(θ/2)σₓ | Rotación por θ alrededor del eje X |
### Puertas de dos Qubits
| Puerta | Descripción | Efecto |
|------|-------------|--------|
| **NO** | Controlado-NO | Voltea el objetivo si el control es \|1⟩ |
| **CZ** | Controlado-Z | Aplica Z al objetivo si el control es \|1⟩ |
| **CAMBIAR** | Intercambiar qubits | \|ab⟩ → \|ba⟩ |
### Creando entrelazamiento
Aplique H al qubit 1, luego CNOT con el qubit 1 como control:
\|00⟩ → (H⊗I)\|00⟩ → CNOT → (1/√2)(\|00⟩ + \|11⟩) = \|Φ⁺⟩
---

## Algoritmos cuánticos
| Algoritmo | Aceleración | Solicitud |
|-----------|---------|-------------|
| **Shor** | Exponencial (factoring) | Rompe el cifrado RSA |
| **De Grover** | Cuadrática (búsqueda) | Búsqueda no estructurada en O(√N) |
| **VQE** | Heurística | Encontrar energías del estado fundamental (química, materiales) |
| **QAOA** | Heurística | Optimización combinatoria |
| **HHL** | Exponencial (bajo condiciones) | Resolución de sistemas lineales |
| **Simulación cuántica** | Exponencial | Simulación de sistemas cuánticos (la motivación original de Feynman) |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto cuántico | Solicitud |
|----------|-------------|
| Qubits y superposición | Aprendizaje automático cuántico, muestreo mejorado cuántico |
| Enredo | Comunicación cuántica, distribución de claves cuánticas (QKD) |
| Puertas cuánticas | Diseño de circuitos cuánticos para subrutinas ML |
| Algoritmo de Grover | Aceleración cuadrática para optimización basada en búsquedas |
| Algoritmo de Sho | Amenaza a la criptografía actual; motiva a las criptomonedas post-cuánticas |
| Simulación cuántica | Descubrimiento de fármacos, ciencia de materiales, simulación química |
| Algoritmos variacionales (VQE, QAOA) | ML cuántico a corto plazo en dispositivos NISQ |
| Regla nata | Resultados probabilísticos análogos al muestreo a partir de distribuciones |
| Productos tensoriales | Sistemas multiqubit (espacio de estados exponencial: las mismas matemáticas que el álgebra multilineal en ML) |
| Matrices unitarias | Análogos cuánticos de transformaciones ortogonales |
---

## Resumen
| Concepto | Idea central | Ecuación clave |
|---------|-----------|-------------|
| Dualidad onda-partícula | La materia tiene propiedades ondulatorias | λ = h/p |
| Función de onda | Descripción completa del estado cuántico | P(x) = \|ψ(x)\|² |
| Ecuación de Schrödinger | Cómo evolucionan los estados cuánticos | iℏ ∂ψ/∂t = Ĥψ |
| Operadores | Los observables son operadores hermitianos | ⟨A⟩ = ⟨ψ\|Â\|ψ⟩ |
| Incertidumbre | Límites fundamentales del conocimiento simultáneo | ΔxΔp ≥ ℏ/2 |
| Superposición | Se pueden agregar estados | \|ψ⟩ = α\|0⟩ + β\|1⟩ |
| Enredo | Estados conjuntos no separables | \|Φ⁺⟩ = (\|00⟩ + \|11⟩)/√2 |
| Puertas cuánticas | Operaciones unitarias sobre qubits | H, CNOT y conjuntos de puertas universales |
La mecánica cuántica desafía nuestras intuiciones más profundas sobre la realidad: partículas que son ondas, objetos en dos lugares a la vez, correlaciones que desafían la explicación clásica. Sin embargo, sus matemáticas son precisas y sus predicciones son incomparables en precisión. Para los científicos de datos, la mecánica cuántica se está volviendo directamente relevante a través de la computación cuántica, que promete transformar la optimización, la criptografía, la simulación y, potencialmente, el propio aprendizaje automático.