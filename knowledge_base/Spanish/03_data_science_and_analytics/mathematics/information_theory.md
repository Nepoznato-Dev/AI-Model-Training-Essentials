<!--
---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
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
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teoría de la información
La teoría de la información, fundada por Claude Shannon en 1948, cuantifica la información en sí. ¿Cuánto te dice un mensaje? ¿Cuánto puedes comprimir datos? ¿Qué tan rápido puede comunicarse a través de un canal ruidoso? Estas preguntas tienen respuestas matemáticas precisas. Más allá de la comunicación, la teoría de la información se ha vuelto fundamental para el aprendizaje automático: la entropía cruzada es la función de pérdida predeterminada para la clasificación, la divergencia de KL mide la similitud de distribución y la información mutua impulsa la selección de características.
---

## Entropía
La **entropía** mide la incertidumbre o "sorpresa" promedio de una variable aleatoria.
### Entropía de Shannon (discreta)
Para una variable aleatoria discreta X con función de masa de probabilidad p(x):
H(X) = −Σₓ p(x) log₂ p(x)
Unidades: **bits** (cuando se usa log₂) o **nats** (cuando se usa ln).
| Distribución | Entropía | Intuición |
|-------------|---------|-----------|
| Moneda justa (p = 0,5, 0,5) | 1 bit | Incertidumbre máxima para el resultado binario |
| Moneda sesgada (p = 0,9, 0,1) | 0,469 bits | Menos sorprendente: en su mayoría caras |
| Determinista (p = 1, 0) | 0 bits | Ninguna incertidumbre en absoluto |
| Dado justo (6 caras) | 2,585 bits | Más resultados = más incertidumbre |
| Uniforme sobre n resultados | log₂(n) bits | Entropía máxima para n resultados |
### Propiedades de la entropía
| Propiedad | Declaración |
|----------|-----------|
| No negatividad | H(X) ≥ 0 |
| Máximo | H(X) ≤ log₂(\|X\|) con igualdad para distribución uniforme |
| Regla de la cadena | H(X, Y) = H(X) + H(Y \| X) |
| El acondicionamiento reduce | H(X \| Y) ≤ H(X) |
| Concavidad | H es una función cóncava de la distribución de probabilidad |
### Entropía diferencial (continua)
Para una variable aleatoria continua X con densidad p(x):
h(X) = −∫ p(x) log p(x) dx
A diferencia de la entropía discreta, la entropía diferencial puede ser **negativa**.
| Distribución | Entropía diferencial |
|-------------|---------------------|
| Uniforme en [a,b] | Iniciar sesión(b − a) |
| Normal norte(μ, σ²) | (1/2) log(2πeσ²) |
| Exponencial(λ) | 1 − ln(λ) |
---

## Información conjunta, condicional y mutua
### Entropía conjunta
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Mide la incertidumbre total del par (X, Y).
### Entropía condicional
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Mide la incertidumbre restante sobre Y después de observar X.
### Información mutua
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Mide cuánto te dice saber X sobre Y (y viceversa).
| Propiedad | Declaración |
|----------|-----------|
| No negatividad | Yo(X; Y) ≥ 0 |
| Simetría | Yo(X; Y) = Yo(Y; X) |
| Relación con la entropía | I(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Relación con la articulación | I(X; Y) = H(X) + H(Y) − H(X, Y) |
| Independencia | I(X; Y) = 0 si X e Y son independientes |
| Autoinformación | Yo(X; X) = H(X) |
### Visual: El diagrama de entropía
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## Divergencia KL
La **divergencia de Kullback-Leibler (KL)** mide qué tan diferente es una distribución de otra.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Propiedad | Declaración |
|----------|-----------|
| No negatividad | D_KL(P \|\| Q) ≥ 0 (desigualdad de Gibbs) |
| Identidad | D_KL(P \|\| Q) = 0 si y solo P = Q |
| Asimetría | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) en general |
| No es una métrica | Falla la simetría y la desigualdad del triángulo |
**Interpretación:** D_KL(P || Q) es el número adicional de bits necesarios para codificar datos de P utilizando un código optimizado para Q.
### Relación con otras cantidades
| Relación | Fórmula |
|-------------|---------|
| Entropía cruzada | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Información mutua | I(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| KL condicional | D_KL(P(Y\|X) \|\| Q(Y\|X)) promediado sobre X |
---

## Entropía cruzada
**Entropía cruzada** entre las distribuciones P y Q:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Entropía cruzada como función de pérdida
En clasificación, P es la distribución verdadera (etiqueta codificada en caliente) y Q es la distribución predicha del modelo.
**Entropía cruzada binaria (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Entropía cruzada categórica:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Escenario | y (verdadero) | ŷ (predicho) | Pérdida |
|----------|----------|---------------|------|
| Correcto, confiado | 1 | 0,95 | 0,051 |
| Correcto, incierto | 1 | 0,55 | 0,598 |
| Equivocado, confiado | 1 | 0,05 | 2.996 |
| Equivocado, incierto | 1 | 0,45 | 0,799 |
Minimizar la entropía cruzada equivale a minimizar la divergencia de KL con respecto a la distribución verdadera, razón por la cual funciona tan bien como función de pérdida.
---

## Capacidad del canal
### Modelo de canal de comunicación
```
X → [Channel] → Y
```

- X: variable aleatoria de entrada
- Y: variable aleatoria de salida
- Canal: definido por probabilidades condicionales p(y|x)
### Teorema de codificación de canales ruidosos de Shannon
Para un canal con capacidad C, si la velocidad de transmisión R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C, la comunicación confiable es imposible.
**Capacidad de canales:**
C = máx_{p(x)} I(X; Y)
### Ejemplos de canales importantes
| Canal | Descripción | Capacidad |
|---------|-------------|----------|
| **Binario simétrico (BSC)** | Invierte cada bit con probabilidad p | 1 − H(p) bits |
| **Borrado binario (BEC)** | Borra cada bit con probabilidad ε | 1 − ε bits |
| **Gaussiano (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2)log(1 + SNR) bits |
| **Binario silencioso** | Transmisión perfecta | 1 bit |
---

## Codificación fuente y compresión
### Teorema de codificación fuente
El número promedio de bits necesarios para codificar una fuente está limitado por su entropía:
L ≥ H(X)
Un código óptimo logra L ≈ H(X).
### Codificación Huffman
Un código **sin prefijo** que asigna códigos más cortos a símbolos más probables.
| Símbolo | Probabilidad | Código Huffman | Longitud |
|--------|-------------|-------------|--------|
| Un | 0,5 | 0 | 1 |
| B | 0,25 | 10 | 2 |
| C | 0,125 | 110 | 3 |
| D | 0,125 | 111 | 3 |
Longitud media: 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 bits/símbolo
Entropía: H = 1,75 bits/símbolo (¡óptimo en este caso!)
### Compresión sin pérdidas frente a compresión con pérdidas
| Tipo | Principio | Ejemplos | Límite |
|------|-----------|----------|-------|
| **Sin pérdidas** | Eliminar la redundancia estadística | ZIP, PNG, FLAC | Tasa de entropía H(X) |
| **Con pérdida** | Eliminar información perceptualmente irrelevante | JPEG, MP3, H.264 | Función de distorsión de velocidad R(D) |
**Teoría de la tasa de distorsión:** Para compresión con pérdidas con distorsión máxima D, la tasa mínima es R(D) = min I(X; X̂) sujeta a E[d(X, X̂)] ≤ D.
---

## Conexiones a otros campos
### Teoría de la información y termodinámica
| Concepto | Teoría de la información | Termodinámica |
|---------|-------------------|----------------|
| Entropía | Entropía de Shannon H(X) | Entropía de Boltzmann S = k_B ln W |
| Entropía máxima | Distribución uniforme | Equilibrio térmico |
| Divergencia KL | Diferencia de distribución | Diferencia de energía libre |
| Información mutua | Información compartida | Correlaciones en sistemas físicos |
Las formas matemáticas son idénticas: Shannon deliberadamente tomó prestado el término "entropía" de la mecánica estadística.
### Teoría de la información y estadística
| Concepto | Solicitud |
|---------|-------------|
| Máxima probabilidad | Equivalente a minimizar la divergencia de KL desde la distribución empírica a la del modelo |
| Información de pescadores | Curvatura de divergencia KL; límite inferior de la varianza del estimador (Cramér-Rao) |
| Longitud mínima de descripción (MDL) | Selección de modelo minimizando la longitud total de codificación |
| AIC/BIC | Criterios aproximados de selección de modelos basados ​​en KL |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto de TI | Aplicación de aprendizaje automático |
|-----------|----------------|
| Pérdida de entropía cruzada | Pérdida de clasificación predeterminada (binaria y multiclase) |
| Divergencia KL | Pérdida de VAE (término de regularización), equiparación de distribución, destilación |
| Información mutua | Selección de características (MIFS), aprendizaje de representación (InfoMax), desenredo |
| Entropía | Criterio de división del árbol de decisión (ganancia de información), exploración en RL (entropía máxima RL) |
| Capacidad del canal | Complejidad de la comunicación, comprensión de los límites de la generalización |
| Codificación fuente | Compresión de datos para almacenamiento y transmisión, codificación eficiente |
| Entropía máxima | Clasificadores MaxEnt, selección previa en inferencia bayesiana |
| Distorsión de tasa | Comprender las ventajas y desventajas de la compresión con pérdidas y la cuantificación en redes neuronales |
| Información de pescadores | Descenso de gradiente natural, comprensión de la sensibilidad de los parámetros |
| MDL/AIC/BIC | Selección de modelo, evitando el sobreajuste |
---

## Resumen
| Cantidad | Fórmula (discreta) | Significado |
|----------|-------------------|---------|
| Entropía H(X) | −Σ p(x) log p(x) | Incertidumbre media |
| Entropía conjunta H(X,Y) | −Σ p(x,y) log p(x,y) | Incertidumbre total del par |
| Entropía condicional H(Y\|X) | H(X,Y) − H(X) | Incertidumbre restante sobre Y dado X |
| Información mutua I(X;Y) | H(X) − H(X\|Y) | Información compartida entre X e Y |
| Divergencia KL D_KL(P\|\|Q) | Σ P(x) log(P(x)/Q(x)) | "Distancia" entre distribuciones |
| Entropía cruzada H(P,Q) | −Σ P(x) log Q(x) | Costo de codificación usando distribución incorrecta |
| Capacidad del canal C | máx I(X;Y) | Máxima tasa de comunicación confiable |
La teoría de la información proporciona los límites fundamentales de lo que se puede aprender, comprimir y comunicar. Para los profesionales del aprendizaje automático, explica por qué la entropía cruzada funciona como una función de pérdida, cómo medir la calidad de las representaciones aprendidas y cómo pensar en el equilibrio entre la complejidad del modelo y el ajuste de los datos. Las ideas de Shannon de 1948 siguen siendo tan relevantes para la IA moderna como lo son para las telecomunicaciones.