---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Estadística y probabilidad
La probabilidad y la estadística son los fundamentos matemáticos de la ciencia de datos, el aprendizaje automático y la investigación científica. La probabilidad le dice qué tan probables son los eventos; Las estadísticas le dicen cómo sacar conclusiones de los datos. Juntos, convierten la incertidumbre en conocimiento cuantificable y manejable.
---

## Teoría de la probabilidad
### Conceptos básicos
| Concepto | Descripción | Ejemplo |
|---------|-------------|---------|
| **Espacio de muestra** | Conjunto de todos los resultados posibles | Lanzar un dado: {1, 2, 3, 4, 5, 6} |
| **Evento** | Un subconjunto del espacio muestral | Sacar un número par: {2, 4, 6} |
| **Probabilidad** | Número entre 0 y 1 que mide la probabilidad | P(rodando 6) = 1/6 |
| **Probabilidad condicional** | P(A|B): probabilidad de que A dado B haya ocurrido | P(lluvia | nublado) |
| **Independencia** | Eventos donde uno no afecta al otro | Los lanzamientos de monedas son independientes |
### Reglas de probabilidad
| Regla | Fórmula | Caso de uso |
|------|---------|----------|
| **Regla de adición** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Probabilidad de A o B |
| **Regla de multiplicación** | P(A ∩ B) = P(A) × P(B|A) | Probabilidad de A y B |
| **Regla de complemento** | P(no A) = 1 − P(A) | Probabilidad de que el evento no ocurra |
| **Ley de Probabilidad Total** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Partición por eventos mutuamente excluyentes |
| **Teorema de Bayes** | P(A|B) = P(B|A) × P(A) / P(B) | Actualizando creencias con evidencia |
### Distribuciones de probabilidad
| Distribución | Tipo | Parámetros clave | Caso de uso |
|-------------|------|----------|----------|
| **Normal (gaussiano)** | Continuo | Media (μ), Desviación estándar (σ) | Fenómenos naturales, errores de medición |
| **Binomio** | Discreto | n (ensayos), p (probabilidad) | El éxito/el fracaso cuenta |
| **Poisson** | Discreto | λ (tasa) | Eventos raros en el tiempo/espacio |
| **Exponencial** | Continuo | λ (tasa) | Tiempo entre eventos |
| **Uniforme** | Ambos | a, b (límites) | Resultados igualmente probables |
| **Chi-Cuadrado** | Continuo | k (grados de libertad) | Pruebas de bondad de ajuste |
| **Distribución t** | Continuo | ν (grados de libertad) | Inferencia de muestra pequeña |
### Propiedades clave de las distribuciones
| Propiedad | Descripción |
|----------|-------------|
| **Media (valor esperado)** | Centro de masa de la distribución: E[X] = Σ xᵢ × P(xᵢ) |
| **Varianza** | Distribuido alrededor de la media: Var(X) = E[(X − μ)²] |
| **Desviación estándar** | Raíz cuadrada de la varianza; mismas unidades que los datos |
| **Asimetría** | Asimetría de la distribución |
| **Curtosis** | "Tailedness": qué tan pesadas son las colas |
---

## Inferencia estadística
### Estadística descriptiva versus inferencial
| | Descriptivo | Inferencial |
|---|-------------|-------------|
| **Propósito** | Resumir y describir datos | Sacar conclusiones sobre una población a partir de una muestra |
| **Herramientas** | Media, mediana, moda, desviación estándar, gráficos | Pruebas de hipótesis, intervalos de confianza, regresión |
| **Alcance** | Sólo los datos que tienes | Generalizando más allá de su muestra |
### Marco de prueba de hipótesis
| Paso | Descripción |
|------|-------------|
| 1. **Hipótesis estatales** | Hipótesis nula (H₀): sin efecto; Alternativa (H₁): existe efecto |
| 2. **Elija el nivel de significancia** | α = 0,05 (convencional) |
| 3. **Seleccione prueba** | Basado en el tipo de datos, el tamaño de la muestra y los supuestos |
| 4. **Calcular estadística de prueba** | Depende de la prueba elegida |
| 5. **Encuentra el valor p** | Probabilidad de observar los datos si H₀ es verdadero |
| 6. **Tomar decisión** | Si p < α, rechace H₀; de lo contrario, no rechace H₀ |
### Pruebas estadísticas comunes
| Prueba | Cuándo utilizar | Qué compara |
|------|-------------|-----------------|
| **prueba t** | Compare las medias de 1 o 2 grupos | Medias de grupo con respecto a un valor o entre sí |
| **Prueba de chi-cuadrado** | Datos categóricos | Frecuencias observadas versus esperadas |
| **ANOVA** | Comparar medias de más de 3 grupos | Variación entre grupos versus dentro del grupo |
| **Mann-Whitney U** | Alternativa no paramétrica a la prueba t | Distribuciones de rango de dos grupos |
| **Correlación de Pearson** | Relación lineal entre dos variables continuas | valor de r de −1 a +1 |
| **Correlación de lancero** | Relación monótona (basada en rangos) | Valor ρ para datos ordinales o no normales |
### Intervalos de confianza
Un intervalo de confianza proporciona un rango de valores plausibles para un parámetro de población:
- **IC del 95% para la media** (σ conocida): x̄ ± 1,96 × (σ / √n)
- **Interpretación**: "Tenemos un 95% de confianza en que la verdadera media poblacional se encuentra dentro de este intervalo"
- **IC más amplio** = más incertidumbre (muestra más pequeña, mayor variabilidad o mayor nivel de confianza)
---

## Análisis de regresión
### Tipos de regresión
| Tipo | Variable dependiente | Caso de uso |
|------|-------------------|----------|
| **Regresión lineal** | Continuo | Predicción de precios y ventas de viviendas |
| **Regresión logística** | Binario (0/1) | Clasificación: detección de spam, diagnóstico de enfermedades |
| **Regresión polinomial** | Continuo (curvo) | Curvas de crecimiento, tendencias no lineales |
| **Regresión múltiple** | Continuo (2+ predictores) | Control de factores de confusión |
| **Cristal / Lazo** | Continuo (regularizado) | Prevención del sobreajuste, selección de funciones |
### Conceptos básicos de regresión lineal
El modelo: **y = β₀ + β₁x + ε**
| Componente | Significado |
|-----------|------------------|
| β₀ (intersección) | Valor de y cuando x = 0 |
| β₁ (pendiente) | Cambio en y para un cambio de una unidad en x |
| ε (término de error) | Variación inexplicable |
**Métricas clave:**
- **R² (coeficiente de determinación)**: Proporción de varianza explicada por el modelo (0 a 1)
- **R² ajustado**: R² penalizado por el número de predictores
- **RMSE**: error cuadrático medio: error de predicción promedio en las mismas unidades que y
### Supuestos de regresión lineal
| Asunción | Lo que significa | Cómo comprobar |
|-----------|--------------|--------------|
| **Linealidad** | La relación entre X e Y es lineal | Diagramas de dispersión |
| **Independencia** | Las observaciones son independientes | Diseño de estudio |
| **Homoscedasticidad** | Varianza constante de residuos | Parcelas residuales |
| **Normalidad** | Los residuos se distribuyen normalmente | Gráfico Q-Q, prueba de Shapiro-Wilk |
| **Sin multicolinealidad** | Los predictores no están altamente correlacionados | VIF (Factor de inflación de varianza) |
---

## Estadísticas bayesianas
### Frecuentista versus bayesiano
| | Frecuentista | Bayesiano |
|---|-------------|----------|
| **Probabilidad significa** | Frecuencia a largo plazo | Grado de creencia |
| **Los parámetros son** | Corregido pero desconocido | Variables aleatorias con distribuciones |
| **Usos** | valores p, intervalos de confianza | Distribuciones posteriores, intervalos creíbles |
| **Fortalezas** | Objetivo, bien establecido | Incorpora conocimientos previos, interpretación intuitiva |
### Teorema de Bayes en la práctica
**Posterior = (Probabilidad × Previo) / Evidencia**
Ejemplo: pruebas médicas:
- Prevalencia de la enfermedad: 1% (anterior)
- Sensibilidad de la prueba: 95% (tasa de verdaderos positivos)
- Especificidad de la prueba: 90% (tasa de verdaderos negativos)
- Si da positivo: P(enfermedad | positivo) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ 8,8%
Este resultado contrario a la intuición (la mayoría de los resultados positivos son falsos positivos cuando la enfermedad es rara) es la **falacia de la tasa base** y muestra por qué el pensamiento bayesiano es importante.
---

## Consejos prácticos
- **Visualice siempre sus datos** antes de ejecutar cualquier prueba estadística
- **Verifique los supuestos**: las infracciones pueden invalidar los resultados
- **El tamaño del efecto importa**: un resultado estadísticamente significativo puede carecer prácticamente de significado
- **La correlación no es causalidad**: incluso las correlaciones fuertes pueden tener factores de confusión
- **Múltiples comparaciones** inflan las tasas de falsos positivos: aplican correcciones (Bonferroni, FDR)
- **Informar intervalos de confianza**, no solo valores p
---

## Por qué esto es importante
La estadística es la columna vertebral de la investigación científica, el análisis empresarial y el aprendizaje automático. Sin él, no se puede distinguir la señal del ruido, identificar efectos reales de fluctuaciones aleatorias ni hacer predicciones con incertidumbre cuantificada. Ya sea que esté analizando pruebas A/B, entrenando modelos de ML o leyendo artículos de investigación, los conocimientos estadísticos son esenciales.