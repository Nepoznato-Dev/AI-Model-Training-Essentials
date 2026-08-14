<!--
---
# Metadata
title: "Electromagnetism"
description: "Electric and magnetic fields, Coulomb's law, Gauss's law, Faraday's law, Ampere's law, Maxwell's equations, electromagnetic waves, and RLC circuits"
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
    changes: "Initial deep-dive into electromagnetism"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [electromagnetism, maxwell-equations, electric-fields, magnetic-fields, electromagnetic-waves, circuits, gauss-law, faraday]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "classical_mechanics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Electromagnetismo
El electromagnetismo es el estudio de los campos eléctricos y magnéticos y sus interacciones. Unificado por Maxwell en la década de 1860, el electromagnetismo explica la luz, la electricidad, el magnetismo, las ondas de radio y la estructura de los átomos. Fue la primera fuerza fundamental que se entendió completamente matemáticamente, y sus ecuaciones inspiraron la relatividad especial de Einstein y la teoría de campos moderna.
---

## Campos eléctricos
### Ley de Coulomb
La fuerza entre dos cargas puntuales q₁ y q₂ separadas por una distancia r:
**F** = (1/4πε₀) · (q₁q₂/r²) · r̂
| Constante | Valor |
|----------|-------|
| ε₀ (permisividad del espacio libre) | 8,854 × 10⁻¹² F/m |
| 1/4πε₀ (Constante de Coulomb k) | 8,988 × 10⁹ N·m²/C² |
### Definición del campo eléctrico
**E** = **F**/q (fuerza por unidad de carga)
Para una carga puntual Q: **E** = (1/4πε₀) · (Q/r²) · r̂
### Líneas de campo eléctrico
| Propiedad | Regla |
|----------|------|
| Dirección | Apuntar lejos de las cargas positivas, hacia las negativas |
| Densidad | Líneas más cercanas = campo más fuerte |
| Cruce | Las líneas de campo nunca se cruzan |
| Conductores | Las líneas se encuentran con la superficie perpendicularmente |
### Potencial eléctrico (voltaje)
V = −∫ **E** · d**l** (la diferencia de potencial es la integral de línea negativa de E)
**E** = −∇V (el campo es el gradiente negativo de potencial)
Para una carga puntual: V = (1/4πε₀) · Q/r
| Concepto | Fórmula | Unidad |
|---------|---------|------|
| Energía potencial | U = qV | Julios |
| Electrovoltio | 1 eV = 1,602 × 10⁻¹⁹ J | Unidad de energía |
| Superficie equipotencial | Superficie donde V es constante | E es perpendicular a él |
---

## Ley de Gauss
### Declaración
El flujo eléctrico total a través de cualquier superficie cerrada es igual a la carga encerrada dividida por ε₀:
∮ **E** · d**A** = Q_enc / ε₀
En forma diferencial: ∇ · **E** = ρ/ε₀
### Usando la ley de Gauss
La ley de Gauss es más útil cuando la simetría permite sacar E de la integral.
| Simetría | Superficie gaussiana | Resultado |
|----------|-----------------|--------|
| Esférico | Esfera | E = Q/(4πε₀r²) exterior |
| Cilíndrico (carga lineal) | Cilindro | mi = λ/(2πε₀r) |
| Planar (hoja infinita) | Pastillero | mi = σ/(2ε₀) |
| Entre placas paralelas | Pastillero | mi = σ/ε₀ |
---

## Conductores y Condensadores
### Conductores en equilibrio electrostático
| Propiedad | Explicación |
|----------|-------------|
| mi = 0 dentro | Cargos se reorganizan para cancelar campo interno |
| Toda la carga en superficie | Sin cargo neto en interior |
| E perpendicular a la superficie | Sin componente tangencial (de lo contrario las cargas se mueven) |
| Equipotencial en todo | Misma V en todas partes dentro y en la superficie |
### Condensadores
Un **condensador** almacena energía en un campo eléctrico entre dos conductores.
| Configuración | Capacitancia |
|--------------|-------------|
| Placas paralelas | C = ε₀A/d |
| Cilíndrico | C = 2πε₀L / ln(b/a) |
| Esférico | C = 4πε₀ab / (b−a) |
| Fórmula | Expresión |
|---------|------------|
| Tensión de carga | Q = CV |
| Energía almacenada | U = ½CV² = ½Q²/C |
| Densidad de energía | tu = ½ε₀E² |
| Combinación de series | 1/C_total = 1/C₁ + 1/C₂ + ... |
| Combinación paralela | C_total = C₁ + C₂ + ... |
### Dieléctricos
Insertar un dieléctrico (material aislante) con κ constante aumenta la capacitancia: C = κC₀.
---

## Campos magnéticos
### Fuerza magnética
**F** = q(**v** × **B**) (fuerza de Lorentz, componente magnético)
| Propiedad | Declaración |
|----------|-----------|
| Dirección | Perpendicular a v y a B (regla de la mano derecha) |
| Trabajo realizado | Cero (la fuerza es perpendicular a la velocidad) |
| Movimiento circular | Radio r = mv/(qB) en campo B uniforme |
### Ley Biot-Savart
El campo magnético debido a un pequeño elemento actual:
d**B** = (μ₀/4π) · I(d**l** × r̂) / r²
| Constante | Valor |
|----------|-------|
| μ₀ (permeabilidad del espacio libre) | 4π × 10⁻⁷ T·m/A |
### Ley de Ampere
∮ **B** · d**l** = μ₀I_enc
En forma diferencial: ∇ × **B** = μ₀**J**
**Aplicaciones:**
| Configuración | Campo B |
|--------------|---------|
| Alambre largo y recto | B = μ₀I/(2πr) |
| Solenoide (interior) | B = μ₀nI |
| Toroide (interior) | B = μ₀NI/(2πr) |
---

## Inducción electromagnética
### Ley de Faraday
Un flujo magnético cambiante induce una fuerza electromotriz (EMF):
FEM = −dΦ_B/dt
donde Φ_B = ∫ **B** · d**A** es el flujo magnético.
En forma diferencial: ∇ × **E** = −∂**B**/∂t
**Ley de Lenz:** La FEM inducida se opone al cambio de flujo (el signo menos).
### Aplicaciones de la Inducción
| Solicitud | Principio |
|-------------|-----------|
| Generador | Bobina giratoria en campo B → EMF alternante |
| Transformador | Cambio de corriente en primario → EMF en secundario |
| Inductores | Se opone a los cambios de corriente: EMF = −L(dI/dt) |
| Corrientes parásitas | Corrientes inducidas en conductores masivos (frenado, calentamiento) |
### Inductores
| Fórmula | Expresión |
|---------|------------|
| Enlace de flujo | Φ = LI |
| Energía almacenada | U = ½LI² |
| Combinación de series | L_total = L₁ + L₂ + ... |
| Combinación paralela | 1/L_total = 1/L₁ + 1/L₂ + ... |
---

## Ecuaciones de Maxwell
Las ecuaciones de Maxwell unifican la electricidad y el magnetismo en una sola teoría.
### En forma integral
| Ecuación | Nombre | Declaración |
|----------|------|-----------|
| ∮ **E** · d**A** = Q/ε₀ | Ley de Gauss (eléctrica) | Flujo eléctrico = carga cerrada |
| ∮ **B** · d**A** = 0 | Ley de Gauss (magnética) | Sin monopolos magnéticos |
| ∮ **E** · d**l** = −dΦ_B/dt | Ley de Faraday | Cambiar B induce E |
| ∮ **B** · d**l** = μ₀I + μ₀ε₀ dΦ_E/dt | Ley de Ampère-Maxwell | La E actual y cambiante produce B |
### En forma diferencial
| Ecuación | Nombre | Expresión |
|----------|------|------------|
| Gauss (eléctrico) | ∇ · **E** = ρ/ε₀ |
| Gauss (magnético) | ∇ · **B** = 0 |
| Faraday | ∇ × **E** = −∂**B**/∂t |
| Amperio-Maxwell | ∇ × **B** = μ₀**J** + μ₀ε₀ ∂**E**/∂t |
### La corriente de desplazamiento
La adición clave de Maxwell: el término μ₀ε₀ ∂**E**/∂t (corriente de desplazamiento). Esto asegura la conservación de la carga y predice las ondas electromagnéticas.
---

## Ondas electromagnéticas
En el vacío (sin cargas, sin corrientes), las ecuaciones de Maxwell producen ecuaciones de onda:
∇²**E** = μ₀ε₀ ∂²**E**/∂t²
∇²**B** = μ₀ε₀ ∂²**B**/∂t²
**Velocidad de la luz:** c = 1/√(μ₀ε₀) ≈ 3 × 10⁸ m/s
### Propiedades de las ondas EM
| Propiedad | Descripción |
|----------|-------------|
| Transversal | E y B son perpendiculares entre sí y a la dirección de propagación |
| En fase | E y B alcanzan máximos simultáneamente |
| Relación de magnitud | mi = cB |
| Flujo de energía | S = (1/μ₀)**E** × **B** (vector de Poynting) |
| Intensidad | I = ⟨S⟩ = E₀²/(2μ₀c) |
### El espectro electromagnético
| Tipo | Longitud de onda | Frecuencia | Fuente |
|------|-----------|-----------|--------|
| Radio | > 1 metro | < 300 MHz | Antennas |
| Microwave | 1 mm − 1 m | 300 MHz − 300 GHz | Magnetrons, klystrons |
| Infrared | 700 nm − 1 mm | 300 GHz − 430 THz | Thermal radiation |
| Visible | 400 − 700 nm | 430 − 750 THz | Atomic transitions |
| Ultraviolet | 10 − 400 nm | 750 THz − 30 PHz | Hot objects, stars |
| X-ray | 0.01 − 10 nm | 30 PHz − 30 EHz | Electron deceleration |
| Gamma ray | < 0.01 nm | >30EHz | Procesos nucleares |
---

## Circuitos de CA
### Componentes del circuito RLC
| Componente | Relación voltaje-corriente | Impedancia |
|-----------|------------------------|-----------|
| Resistencia (R) | V = IR | Z_R = R |
| Inductor (L) | V = L(dI/dt) | Z_L = jωL |
| Condensador (C) | Yo = C(dV/dt) | Z_C = 1/(jωC) |
### Impedancia y resonancia
Impedancia total (serie RLC): Z = R + j(ωL − 1/ωC)
|ω| = √(R² + (ωL − 1/ωC)²)
**Resonancia:** Cuando ωL = 1/ωC → ω₀ = 1/√(LC)
- En resonancia: la impedancia es mínima (= R), la corriente es máxima
- **Factor de calidad:** Q = ω₀L/R (nitidez de resonancia)
### Energía en circuitos de CA
| Cantidad | Fórmula |
|----------|---------|
| Potencia media | P_promedio = V_rms · I_rms · cos φ |
| Factor de potencia | porque φ = R/\|Z\| |
| Tensión RMS | V_rms = V₀/√2 |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto EM | Solicitud |
|-----------|-------------|
| Ecuaciones de Maxwell | Redes neuronales basadas en la física, electromagnetismo computacional |
| Ecuación de onda | Fundamentos del procesamiento de señales, motivación del análisis de Fourier |
| Espectro electromagnético | Datos de sensores (cámaras infrarrojas, radares, imágenes de satélite) |
| Circuitos CA / impedancia | Comprensión del hardware que ejecuta ML (fuentes de alimentación, integridad de la señal) |
| Vector de puntería | Flujo de energía en la comunicación inalámbrica (relevante para IoT/edge ML) |
| Ley de Gauss | Análogo a la divergencia en el cálculo vectorial, utilizado en simulaciones de dinámica de fluidos |
| Condensadores/inductores | Computación analógica para redes neuronales, hardware neuromórfico |
| Resonancia | Diseño de filtros, análisis en el dominio de la frecuencia, métodos espectrales |
| Problemas de valores en la frontera | Métodos de elementos finitos, simulaciones basadas en mallas |
| Cálculo vectorial (∇·, ∇×) | Herramientas matemáticas esenciales utilizadas en toda la teoría del ML |
---

## Resumen
| Ley | Lo que dice | Forma diferencial |
|-----|-------------|-------------------|
| Gauss (eléctrico) | Las cargas crean divergencia del campo eléctrico | ∇ · E = ρ/ε₀ |
| Gauss (magnético) | Sin monopolos magnéticos | ∇ · B = 0 |
| Faraday | Cambiar B crea curvatura E | ∇ × mi = −∂B/∂t |
| Amperio-Maxwell | La E actual y cambiante crea el rizado B | ∇ × B = μ₀J + μ₀ε₀∂E/∂t |
El electromagnetismo es la teoría física más completa y mejor probada jamás construida. Sus ecuaciones (solo cuatro) describen todo, desde la electricidad estática hasta la luz y el comportamiento de cada dispositivo electrónico jamás construido. Para los científicos de datos, comprender el electromagnetismo proporciona una intuición profunda sobre los fenómenos ondulatorios, el cálculo vectorial y la física que subyace a todo el hardware informático moderno.