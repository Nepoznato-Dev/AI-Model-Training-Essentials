---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
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
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Pruebas estadísticas y experimentación
La estadística es la gramática de la ciencia. Le brinda las herramientas para distinguir patrones reales del ruido aleatorio, medir si un cambio realmente mejoró las cosas y tomar decisiones en condiciones de incertidumbre. Este archivo cubre los conceptos centrales de la prueba de hipótesis, el diseño experimental y los errores comunes que hacen tropezar a las personas.
---

## El marco de prueba de hipótesis
Cada prueba estadística sigue la misma lógica:
1. **Establezca la hipótesis nula (H₀)**: No hay efecto/no hay diferencia.
2. **Establezca la hipótesis alternativa (H₁)**: Hay un efecto/una diferencia.
3. **Elija un nivel de significancia (α)**: normalmente 0,05 (5 % de probabilidad de falso positivo).
4. **Recopilar datos y calcular una estadística de prueba**.
5. **Calcule el valor p**: Probabilidad de observar este resultado (o más extremo) si H₀ es verdadero.
6. **Tome una decisión**: Si p < α, rechace H₀ (estadísticamente significativo). De lo contrario, no rechace el H₀.
### Conceptos clave
| Concepto | Significado | Concepto erróneo común |
|---------|---------|---------------------|
| **valor p** | P(datos \| H₀ es verdadero) | NO "la probabilidad de que H₀ sea verdadera" |
| **α (nivel de significancia)** | Umbral de rechazo de H₀ | No es una medida de la importancia del efecto |
| **Significancia estadística** | Resultado improbable debido únicamente al azar | NO significa prácticamente significativo |
| **Tamaño del efecto** | Magnitud del efecto observado | Separado del valor p; un efecto pequeño puede ser significativo con N |
| **Poder** | Probabilidad de rechazar correctamente un H₀ falso | Normalmente apunta a 80%+ |
| **Intervalo de confianza** | Rango de valores plausibles para el parámetro | Un IC del 95% no significa "95% de probabilidad de que el valor real esté en este rango" |
---

## Tipos de errores
| | H₀ es verdadero | H₀ es falso |
|---|-----------|------------|
| **Rechazar H₀** | Error tipo I (falso positivo) | ✅ Correcto (verdadero positivo) |
| **No se pudo rechazar H₀** | ✅ Correcto (verdadero negativo) | Error tipo II (falso negativo) |
| Error | Símbolo | Significado |
|-------|--------|---------|
| **Tipo I** | α | Concluyendo que hay un efecto cuando no lo hay |
| **Tipo II** | β | Falta un efecto real |
---

## Elegir la prueba adecuada
| Escenario | Prueba | Supuestos |
|----------|------|-------------|
| Comparar medias de 2 grupos | **prueba t** (independiente) | Distribución normal, igual varianza |
| Comparar medias de observaciones pareadas | **Prueba t pareada** | Las diferencias se distribuyen normalmente |
| Comparar medias de más de 3 grupos | **ANOVA** | Distribución normal, igual varianza |
| Comparar distribuciones categóricas | **Prueba de chi-cuadrado** | Tamaño de muestra suficiente por celda |
| Comparar distribuciones (no paramétricas) | **Mann-Whitney U** | Sin supuesto de normalidad |
| Comparar más de 3 grupos (no paramétricos) | **Kruskal-Wallis** | Sin supuesto de normalidad |
| Correlación de prueba | **Pearson** (lineal) o **Spearman** (monótono) | Pearson: normalidad; Spearman: basado en rangos |
| Pruebe si los datos siguen una distribución | **Kolmogorov-Smirnov** | Datos continuos |
### Paramétrico versus no paramétrico
| | Paramétrico | No paramétrico |
|---|-----------|---------------|
| **Supuestos** | Los datos siguen una distribución específica (normalmente normal) | Sin supuesto de distribución |
| **Poder** | Mayor cuando se cumplieron los supuestos | Más bajo, pero más robusto |
| **Cuándo utilizar** | Muestras grandes, datos aproximadamente normales | Muestras pequeñas, datos asimétricos, datos ordinales |
---

## Pruebas específicas en detalle
### prueba t
Compara las medias de dos grupos.
| Variante | Caso de uso |
|---------|----------|
| **Prueba t independiente** | Dos grupos separados (tratamiento versus control) |
| **Prueba t pareada** | Mismo grupo medido dos veces (antes vs después) |
| **Prueba t de una muestra** | Comparar una media muestral con un valor conocido |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Análisis de Varianza)
Compara medias en 3 o más grupos. Prueba si al menos la media de un grupo difiere del resto.
| Tipo | Diseño |
|------|--------|
| **ANOVA unidireccional** | Una variable independiente con más de 3 niveles |
| **ANOVA bidireccional** | Dos variables independientes; prueba efectos de interacción |
| **ANOVA de medidas repetidas** | Los mismos sujetos medidos en diferentes condiciones |
Si el ANOVA es significativo, realice un seguimiento con **pruebas post hoc** (HSD de Tukey) para encontrar qué grupos específicos difieren.
### Prueba de chi-cuadrado
Prueba si dos variables categóricas son independientes.
| Caso de uso | Ejemplo |
|----------|---------|
| **Prueba de independencia** | ¿Está el género asociado con la preferencia de producto? |
| **Bondad de ajuste** | ¿La tirada de un dado sigue una distribución uniforme? |
**Regla general**: cada celda debe tener un recuento esperado de al menos 5.
---

## Pruebas A/B
Las pruebas A/B son la aplicación de pruebas de hipótesis a decisiones comerciales, generalmente comparando un control (A) con una variante (B).
### Proceso de diseño
| Paso | Descripción |
|------|-------------|
| **1. Definir hipótesis** | "Cambiar el color del botón de azul a verde aumentará la tasa de clics" |
| **2. Elija métrica** | Principal: tasa de clics. Secundario: tasa de conversión, ingresos. |
| **3. Calcular el tamaño de la muestra** | Basado en el efecto mínimo detectable, el poder (80%) y la significancia (5%) |
| **4. Aleatorizar** | Asignar usuarios aleatoriamente para control y tratamiento |
| **5. Ejecutar experimento** | Recopilar datos hasta alcanzar el tamaño de muestra objetivo |
| **6. Analizar** | Comparar métricas utilizando pruebas estadísticas apropiadas |
| **7. Decidir** | Implementar si es estadística y prácticamente significativo |
### Cálculo del tamaño de la muestra
El tamaño de muestra que necesita depende de:
| factor | Efecto sobre el tamaño de la muestra |
|--------|----------------------|
| **Efecto más pequeño para detectar** | Necesita más muestras |
| **Mayor potencia** | Necesita más muestras |
| **Nivel de significancia inferior** | Necesita más muestras |
| **Mayor variación** | Necesita más muestras |
### Errores comunes en las pruebas A/B
| Error | Por qué está mal |
|---------|---------------|
| **Echando un vistazo temprano** | La verificación diaria de los resultados aumenta la tasa de falsos positivos |
| **Múltiples métricas sin corrección** | Probando 20 métricas en α=0.05 → espere 1 falso positivo por casualidad |
| **Parando antes del objetivo N** | Una prueba con poca potencia no puede detectar efectos reales |
| **Ignorando la estacionalidad** | Realizar una prueba durante un período de vacaciones versus una semana normal |
| **Asignación no aleatoria** | Sesgo de selección (por ejemplo, asignar nuevos usuarios al tratamiento) |
| **Confundir significado con importancia** | Un aumento del 0,1% puede ser estadísticamente significativo, pero no vale la pena enviarlo |
---

## Comparaciones múltiples
Cuando se ejecutan muchas pruebas simultáneamente, la posibilidad de que se produzca al menos un falso positivo aumenta drásticamente.
| Número de pruebas | Probabilidad de ≥1 falso positivo (con α=0,05) |
|----------------|----------------------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |
### Correcciones
| Método | Cómo funciona | Cuándo utilizar |
|--------|-------------|-------------|
| **Bonferroni** | Divida α por el número de pruebas (α/n) | Conservador; pocas comparaciones |
| **Holm-Bonferroni** | Procedimiento de reducción; menos conservador | Uso general |
| **Benjamini-Hochberg (FDR)** | Controla la tasa de descubrimiento falso | Muchas pruebas; análisis exploratorio |
---

## Tamaño del efecto
Los valores P le indican *si* existe un efecto. El tamaño del efecto te dice *qué tan grande* es.
| Medida | Para | Interpretación |
|---------|-----|-----------------------|
| **La muerte de Cohen** | Diferencia entre dos medias | 0,2 = pequeño, 0,5 = mediano, 0,8 = grande |
| **R de Pearson** | Correlación | 0,1 = pequeño, 0,3 = mediano, 0,5 = grande |
| **η² (eta-cuadrado)** | ANOVA | 0,01 = pequeño, 0,06 = mediano, 0,14 = grande |
| **Razón de probabilidades** | Resultados categóricos | 1,0 = sin efecto; >1 o <1 = efecto |
**Indique siempre el tamaño del efecto junto con los valores p.** Un resultado puede ser estadísticamente significativo pero prácticamente carecer de significado.
---

## Bayesiano vs Frecuentista
| Aspecto | Frecuentista | Bayesiano |
|--------|------------|----------|
| **Probabilidad** | Frecuencia de eventos a largo plazo | Grado de creencia |
| **Parámetros** | Corregido pero desconocido | Variables aleatorias con distribuciones |
| **Usos** | valores p, intervalos de confianza, pruebas de hipótesis | Distribuciones posteriores, intervalos creíbles |
| **Anterior** | No se incorporan creencias previas | Distribución previa explícita |
| **Interpretación** | "Si repitiéramos este experimento muchas veces..." | "Dados los datos, la probabilidad de que..." |
| **Fortalezas** | Objetivo, bien establecido, sencillo | Interpretación intuitiva, incorpora conocimientos previos |
| **Debilidades** | valores p ampliamente mal entendidos | La elección del prior puede ser subjetiva |
---

## Conceptos básicos de la inferencia causal
La correlación no es causalidad. Pero a veces es necesario saber *si X causó Y*, no sólo si están asociados.
| Método | Descripción | Cuándo utilizar |
|--------|-------------|-------------|
| **Experimentos aleatorios** | Patrón oro; la asignación aleatoria elimina los factores de confusión | Cuando puedes aleatorizar |
| **Diferencia en diferencias (DiD)** | Comparar los cambios a lo largo del tiempo entre tratamiento y control | Cambios de política, experimentos naturales |
| **Discontinuidad de regresión (RDD)** | Explotar un umbral de corte | Becas, umbrales de elegibilidad |
| **Variables instrumentales (IV)** | Utilice un instrumento que afecte el tratamiento pero no el resultado directamente | Cuando la aleatorización no es posible |
| **Cotejo de puntuación de propensión** | Emparejar las unidades tratadas y de control según las características observadas | Estudios observacionales |
---

## Errores estadísticos comunes
| Error | Descripción |
|---------|-------------|
| **p-hacking** | Probando muchos análisis hasta encontrar p < 0,05 |
| **ESCUCHANDO** | Formular hipótesis después de conocer los resultados |
| **Sesgo de supervivencia** | Sólo mirando los éxitos (por ejemplo, empresas exitosas) |
| **La paradoja de Simpson** | La tendencia se invierte cuando los datos se agregan en lugar de dividirse por grupo |
| **Descuido de la tasa base** | Ignorar la probabilidad previa al interpretar los resultados |
| **Falacia ecológica** | Inferir el comportamiento individual a partir de datos a nivel de grupo |
| **Confuso** | Una tercera variable explica la relación observada |
| **Sobreajuste** | El modelo captura ruido, no señal |
---

## Resumen
Las pruebas estadísticas consisten en tomar decisiones en condiciones de incertidumbre con honestidad intelectual. Exponga siempre sus hipótesis antes de recopilar datos. Elija la prueba adecuada para su tipo de datos. Informe los tamaños del efecto, no solo los valores p. Correcto para comparaciones múltiples. Y recuerde: significación estadística no es lo mismo que significación práctica.