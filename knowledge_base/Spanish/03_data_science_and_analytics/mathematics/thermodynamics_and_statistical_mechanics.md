---
# Metadata
title: "Thermodynamics and Statistical Mechanics"
description: "Laws of thermodynamics, entropy (thermodynamic and statistical), enthalpy, free energy, Carnot cycle, Boltzmann distribution, partition functions, and connections to information-theoretic entropy"
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
    changes: "Initial deep-dive into thermodynamics and statistical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [thermodynamics, statistical-mechanics, entropy, enthalpy, free-energy, carnot-cycle, boltzmann, partition-function]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
  - "classical_mechanics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Termodinámica y Mecánica Estadística
La termodinámica describe el comportamiento macroscópico de los sistemas en términos de temperatura, presión y entropía, sin saber cómo son los átomos. La mecánica estadística explica la termodinámica de abajo hacia arriba: deriva propiedades macroscópicas del comportamiento microscópico de un gran número de partículas. Juntos, proporcionan la comprensión más profunda de la energía, la entropía y el equilibrio, conceptos que han migrado a la teoría de la información, el aprendizaje automático y más allá.
---

## Variables termodinámicas y estado
### Variables de estado
| Variables | Tipo | Unidad | Descripción |
|----------|------|------|-------------|
| Temperatura (T) | Intensivo | grados Kelvin (K) | Energía cinética media por partícula |
| Presión (P) | Intensivo | Pascal (Pa) | Fuerza por unidad de área |
| Volumen (V) | Amplia | m³ | Espacio ocupado |
| Energía interna (U) | Amplia | Julios (J) | Energía microscópica total |
| Entropía (S) | Amplia | J/K | Medida de desorden/microestados |
| Número de partículas (N) | Amplia | moles o contar | Cantidad de sustancia |
Las variables **intensivas** no dependen del tamaño del sistema; Las variables **extensas** sí lo hacen.
### Ecuación de estado
Para un gas ideal: PV = nRT = Nk_BT
| Constante | Valor |
|----------|-------|
| R (constante de los gases) | 8,314 J/(mol·K) |
| k_B (constante de Boltzmann) | 1,381 × 10⁻²³ J/K |
| N_A (número de Avogadro) | 6,022 × 10²³ /mol |
---

## Las leyes de la termodinámica
### Ley Cero
Si A está en equilibrio térmico con B y B con C, entonces A está en equilibrio térmico con C.
**Significado:** La temperatura está bien definida y se puede medir.
### Primera Ley (Conservación de Energía)
ΔU = Q − W
| Símbolo | Significado |
|--------|---------|
| ΔU | Cambio de energía interna |
| Q | Calor agregado al sistema |
| W | Trabajo realizado por sistema |
**Forma diferencial:** dU = δQ − δW = δQ − PdV
| Proceso | Restricción | Consecuencia |
|---------|-----------|-------------|
| Isocórico | dV = 0 | W = 0, ΔU = Q |
| isobárico | dP = 0 | W = PVΔV |
| Isotérmico | dT = 0 | ΔU = 0 (gas ideal), Q = W |
| Adiabático | δQ = 0 | ΔU = −W |
### Segunda Ley (Entropía)
**Afirmación de Clausius:** El calor no puede fluir espontáneamente del frío al calor.
**Declaración de Kelvin-Planck:** Ningún motor puede convertir todo el calor en trabajo.
**Declaración de entropía:** Para cualquier proceso: ΔS_universe ≥ 0
| Tipo de proceso | ΔS_universo |
|-------------|-------------|
| reversibles | = 0 |
| Irreversibles (reales) | > 0 |
**Cambio de entropía:** dS = δQ_rev / T
### Tercera ley
Cuando T → 0 K, la entropía de un cristal perfecto se acerca a cero: lim_{T→0} S = 0
**Significado:** El cero absoluto es inalcanzable en pasos finitos.
---

## Entropía en profundidad
### Entropía termodinámica
S es una función de estado. Para un proceso reversible entre los estados A y B:
ΔS = ∫_A^B δQ_rev / T
**Ejemplo resuelto:** Cambio de entropía al calentar agua de T₁ a T₂ a presión constante.
ΔS = ∫_{T₁}^{T₂} (mc_p/T) dT = mc_p ln(T₂/T₁)
### Entropía estadística (Boltzmann)
S = k_B ln Ω
donde Ω es el número de microestados consistentes con el macroestado.
| Macroestado | Microestados (Ω) | Entropía |
|-----------|-----------------|---------|
| Todo el gas en la mitad de la caja | Pequeño | Bajo |
| Gas distribuido uniformemente | Muy grande | Alto |
| Cristal perfecto a 0 K | 1 | 0 |
**Conexión:** La segunda ley se vuelve estadística: los sistemas evolucionan hacia macroestados con más microestados simplemente porque son abrumadoramente más probables.
---

## Entalpía y energía libre
### Entalpía
H = U + PV
Útil para procesos a presión constante (la mayoría de química y biología).
ΔH = Q_p (calor a presión constante)
### Energía libre de Helmholtz
F = U − TS
| Propiedad | Declaración |
|----------|-----------|
| Significado | Trabajo máximo extraíble a T, V constante |
| Equilibrio | El sistema minimiza F a T, V constante |
| Relación con la función de partición | F = −k_BT en Z |
### Energía libre de Gibbs
GRAMO = H − TS = U + PV − TS
| Propiedad | Declaración |
|----------|-----------|
| Significado | Trabajo máximo sin expansión a T, P constante |
| Equilibrio | El sistema minimiza G a T constante, P |
| Espontaneidad | ΔG < 0 → espontáneo; ΔG = 0 → equilibrio |
| Reacciones químicas | ΔG = ΔH − TΔS determina la dirección |
### Resumen de potenciales termodinámicos
| Potencial | Variables naturales | Diferencial | Minimizado cuando |
|-----------|-------------------|-------------|----------------|
| U (energía interna) | S, V | dU = TdS − PdV | Sistema aislado |
| H (entalpía) | S, P | dH = TdS + VdP | P constante, adiabática |
| F (Helmholtz) | T, V | dF = −SdT − PdV | T constante, V |
| G (Gibbs) | T, P | dG = −SdT + VdP | T constante, P |
---

## El ciclo de Carnot
El **ciclo de Carnot** es el motor térmico más eficiente posible y funciona entre temperaturas T_H (caliente) y T_C (frío).
### Cuatro etapas
| Etapa | Proceso | Qué pasa |
|-------|---------|-------------|
| 1 → 2 | Expansión isotérmica | Absorber calor Q_H del depósito caliente en T_H |
| 2 → 3 | Expansión adiabática | El gas se enfría de T_H a T_C |
| 3 → 4 | Compresión isotérmica | Rechazar calor Q_C al depósito frío en T_C |
| 4 → 1 | Compresión adiabática | El gas se calienta de T_C a T_H |
### Eficiencia de Carnot
η_Carnot = 1 − T_C/T_H
| T_H | T_C | η_Carnot |
|-----|-----|----------|
| 500K | 300K | 40% |
| 1000K | 300K | 70% |
| 300K | 299K | 0,33% |
**Ningún motor real puede superar la eficiencia de Carnot.** Los motores reales son siempre irreversibles (fricción, turbulencia, diferencias finitas de temperatura).
---

## Mecánica estadística
### La distribución de Boltzmann
Para un sistema en equilibrio térmico a temperatura T, la probabilidad de estar en un microestado con energía E_i:
P(E_i) = (1/Z) e^{−E_i / k_BT}
donde Z es la **función de partición**:
Z = Σᵢ e^{−E_i / k_BT}
### La función de partición
Z codifica toda la información termodinámica sobre el sistema.
| Cantidad | Fórmula |
|----------|---------|
| Energía libre de Helmholtz | F = −k_BT en Z |
| Energía media | ⟨E⟩ = −∂(ln Z)/∂β donde β = 1/(k_BT) |
| Entropía | S = k_B(ln Z + β⟨E⟩) |
| Capacidad calorífica | C_V = ∂⟨E⟩/∂T = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Presión | P = (1/β) ∂(ln Z)/∂V |
### Ejemplo resuelto: sistema de dos Estados
Una partícula puede estar en el estado 0 (energía 0) o en el estado 1 (energía ε).
Z = 1 + mi^{−βε}
| Cantidad | Resultado |
|----------|--------|
| P(estado 0) | 1/(1 + mi^{−βε}) |
| P(estado 1) | mi^{−βε}/(1 + mi^{−βε}) |
| ⟨E⟩ | ε/(1 + mi^{βε}) |
| Límite alto de T (β→0) | ⟨E⟩ → ε/2 (igual probabilidad) |
| Límite T inferior (β→∞) | ⟨E⟩ → 0 (estado fundamental) |
### Teorema de equiparpartición
Cada grado de libertad cuadrático aporta ½k_BT a la energía promedio.
| Sistema | Grados de libertad | ⟨E⟩ |
|--------|-------------------|------|
| Gas monoatómico (He) | 3 traducción | (3/2)k_BT |
| Gas diatómico (N₂) en la habitación T | 3 trans + 2 podridos | (5/2)k_BT |
| Gas diatómico a alta T | 3 trans + 2 podridos + 1 vib | (7/2)k_BT |
| Sólido (modelo Einstein) | 3 vibracionales (por átomo) | 3k_BT |
---

## Conexión con la teoría de la información
### Entropía de Shannon versus entropía termodinámica
| Aspecto | Entropía de Shannon H(X) | Entropía termodinámica S |
|--------|---------------------|-----------------------|
| Definición | −Σ pᵢ log pᵢ | k_B ln Ω (o −k_B Σ pᵢ ln pᵢ) |
| Máximo cuando | Distribución uniforme | Equilibrio térmico |
| Medidas | Incertidumbre/contenido de la información | Número de microestados accesibles |
| Unidades | Bits o nats | J/K |
**Fórmula de entropía de Gibbs:** S = −k_B Σᵢ pᵢ ln pᵢ (idéntica en forma a la entropía de Shannon)
### Principio de máxima entropía
Ambos campos utilizan el mismo principio: la distribución que mejor representa nuestro estado de conocimiento es la que maximiza la entropía sujeta a restricciones conocidas.
| Restricción | Distribución resultante |
|-----------|----------------------|
| Media conocida | Distribución exponencial |
| Media y varianza conocidas | Distribución gaussiana |
| Energía conocida ⟨E⟩ | Distribución Boltzmann |
| Sin restricciones | Distribución uniforme |
### Principio de Landauer
Al borrar un bit de información se disipa al menos k_BT ln 2 de energía en forma de calor. Esto conecta el procesamiento de información directamente con la termodinámica: la computación tiene un costo energético fundamental.
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto Termo/StatMech | Solicitud |
|-----------------------|-------------|
| Distribución Boltzmann | Función Softmax, modelos basados ​​en energía, recocido simulado |
| Función de partición | Constante de normalización en modelos probabilísticos, intratables en general |
| Energía libre | Inferencia variacional (minimizar la energía libre variacional = minimizar la divergencia KL) |
| Entropía | Regularización, exploración en RL (RL de máxima entropía), árboles de decisión |
| Principio de máxima entropía | Clasificadores MaxEnt, selección previa, estimación de distribución |
| Recocido simulado | Optimización global reduciendo gradualmente la "temperatura" |
| Mecánica estadística | Comprender las transiciones de fases en el aprendizaje (asimilar, doble descenso) |
| Equipartición | Comprensión de la distribución de energía en simulaciones físicas |
| Principio de Landauer | Límites fundamentales de la computación, computación reversible |
| Muestreo de Gibbs | Método MCMC inspirado directamente en la mecánica estadística |
| Temperatura (en softmax) | Controla la aleatoriedad de las predicciones: P(i) ∝ exp(z_i/T) |
---

## Resumen
| Ley/Concepto | Idea central | Fórmula |
|------------|-----------|---------|
| Ley cero | La temperatura está bien definida | Transitividad del equilibrio térmico |
| Primera ley | Se conserva la energía | ΔU = Q − W |
| Segunda ley | Aumenta la entropía del universo | ΔS ≥ 0 |
| Tercera ley | El cero absoluto es inalcanzable | S → 0 como T → 0 |
| Entropía de Boltzmann | La entropía cuenta los microestados | S = k_B ln Ω |
| Distribución Boltzmann | Probabilidad de estados energéticos | P ∝ e^{−E/k_BT} |
| Función de partición | Codifica toda la información termodinámica | Z = Σe^{−E_i/k_BT} |
| Energía libre | Trabajo útil disponible | F = U − TS, GRAMO = H − TS |
| Eficiencia de Carnot | Máxima eficiencia del motor térmico | η = 1 − T_C/T_H |
La termodinámica y la mecánica estadística son el punto de encuentro de la física con la teoría de la información. La misma entropía que gobierna los motores térmicos gobierna la compresión de datos. La misma distribución de Boltzmann que describe las moléculas de gas impulsa la capa softmax en cada clasificador. Comprender estas conexiones le brinda una visión unificada de la física, la probabilidad y el aprendizaje automático.