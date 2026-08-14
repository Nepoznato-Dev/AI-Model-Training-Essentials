---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [time, series, forecasting, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Series temporales y pronósticos
Los datos de series temporales son cualquier dato recopilado a lo largo del tiempo: precios de acciones, lecturas de temperatura, tráfico del sitio web, cifras de ventas, monitores de frecuencia cardíaca, consumo de energía. Pronosticar significa predecir valores futuros basándose en patrones pasados. Es una de las aplicaciones de la ciencia de datos con mayor valor práctico, y una de las más difíciles, porque el futuro es genuinamente incierto y las series temporales del mundo real están llenas de ruido, estacionalidad y rupturas estructurales.
---

## Características de las series temporales
| Componente | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Tendencia** | Aumento o disminución a largo plazo | Las temperaturas globales aumentan durante décadas |
| **Estacionalidad** | Patrones regulares y predecibles a intervalos fijos | Las ventas minoristas aumentan cada diciembre |
| **Ciclicidad** | Fluctuaciones a intervalos no fijos (a menudo económicas) | Recesiones cada 5-10 años |
| **Ruido (residual)** | Variación aleatoria que no se puede explicar | Movimientos diarios del precio de las acciones |
| **Autocorrelación** | Los valores actuales dependen de los valores pasados ​​| La temperatura de hoy es similar a la de ayer |
### Estacionariedad
Una serie temporal es **estacionaria** si sus propiedades estadísticas (media, varianza) no cambian con el tiempo. La mayoría de los métodos de pronóstico asumen estacionariedad.
| Prueba | Propósito |
|------|---------|
| **Dickey-Fuller aumentado (ADF)** | Comprueba si existe una raíz unitaria (no estacionaria) |
| **Prueba KPSS** | Prueba si la serie es estacionaria en términos de tendencia |
| Transformación | Cuándo utilizar |
|---------------|-------------|
| **Diferenciación** | Eliminar tendencia: y'(t) = y(t) - y(t-1) |
| **Transformación de registro** | Estabilizar la varianza (para un crecimiento exponencial) |
| **Diferenciación estacional** | Eliminar la estacionalidad: y'(t) = y(t) - y(t-s) donde s es la duración de la temporada |
---

## Métodos de pronóstico clásicos
### Medias móviles
| Método | Descripción | Mejor para |
|--------|-------------|----------|
| **Promedio móvil simple (SMA)** | Promedio de las últimas N observaciones | Suavizado de datos ruidosos |
| **Promedio móvil ponderado** | Las observaciones más recientes obtienen mayor peso | Cuando los datos recientes importan más |
| **Promedio Móvil Exponencial (EMA)** | Pesos exponencialmente decrecientes | Seguimiento de tendencias con menos retraso |
### Suavizado exponencial
| Método | Componentes | Caso de uso |
|--------|-----------|----------|
| **Sencillo (SES)** | Solo nivel | Sin tendencia, sin estacionalidad |
| **Holt's (Doble)** | Nivel + tendencia | Datos con tendencia pero sin estacionalidad |
| **Holt-Winters (Triple)** | Nivel + tendencia + estacionalidad | Datos con tendencia y estacionalidad |
### ARIMA y variantes
ARIMA (Promedio Móvil Integrado AutoRegresivo) es el caballo de batalla del pronóstico de series de tiempo clásico.
| Componente | Significado | Parámetro |
|-----------|---------|-----------|
| **RA (p)** | Regreso a los valores p anteriores | ¿Cuántos valores pasados ​​usar?
| **Yo (d)** | Número de pasos diferenciadores para hacer estacionario | Cuantas veces diferenciar |
| **MA (q)** | Modele el error como una combinación de errores pasados ​​| Cuántos errores pasados ​​usar |
| Variante | Ampliación | Caso de uso |
|---------|-----------|----------|
| **SARIMA** | Añade componentes estacionales (P, D, Q, s) | Datos con fuerte estacionalidad |
| **ARIMAX** | Agrega variables externas | Cuando sepas sobre los próximos eventos |
| **VAR** | ARIMA multivariada; múltiples series interdependientes | Cuando las variables se afectan entre sí |
---

## Enfoques modernos de aprendizaje automático
### Modelos basados ​​en LSTM y RNN
| Modelo | Arquitectura | Ventaja |
|-------|-------------|-----------|
| **LSTM** | Red de Memoria a Corto Plazo | Capta dependencias temporales de largo alcance |
| **GRU** | Unidad recurrente cerrada (LSTM más simple) | Entrenamiento más rápido; rendimiento similar |
| **Seq2Seq** | Codificador-decodificador de series temporales | Longitudes de entrada/salida flexibles |
| **Red convolucional temporal (TCN)** | Circunvoluciones causales dilatadas | Formación paralela; campo receptivo largo |
### Profeta (Meta)
Una práctica herramienta de previsión diseñada para series temporales empresariales.
| Característica | Descripción |
|---------|-------------|
| **Descomposición** | Tendencia + estacionalidad + vacaciones |
| **Flexibles** | Maneja datos faltantes, valores atípicos y rupturas estructurales |
| **Interpretable** | Los componentes son legibles por humanos |
| **Automático** | incumplimientos razonables; ajuste mínimo requerido |
| Fuerza | Limitación |
|----------|------------|
| Excelente para métricas comerciales (ventas, usuarios) | No es ideal para datos de muy alta frecuencia |
| Maneja días festivos y eventos especiales | Asume estacionalidad aditiva o multiplicativa |
| Robusto ante valores atípicos | Menos preciso que el aprendizaje profundo para patrones complejos |
### Modelos basados ​​en transformadores
| Modelo | Característica clave |
|-------|-------------|
| **Informador** | ProbAtención escasa para secuencias largas |
| **Autoformador** | Mecanismo de autocorrelación para la descomposición en series |
| **ParcheTST** | Parchea la serie temporal; independiente del canal |
| **TimesFM** (Google) | Modelo básico para series temporales; pre-entrenado en datos diversos |
| **Cronos** (Amazonía) | Tokeniza series temporales; utiliza arquitectura estilo LLM |
---

## Detección de anomalías en series temporales
Detectar patrones inusuales que se desvían del comportamiento esperado.
| Método | Enfoque | Caso de uso |
|--------|----------|----------|
| **Estadístico** | Puntuación Z, IQR, gráficos de control | Sencillo, bien entendido |
| **Bosque de aislamiento** | Basado en árboles; aísla anomalías mediante partición aleatoria | Detección de anomalías multivariadas |
| **LOF** (factor de valor atípico local) | Basado en densidad; compara la densidad local con la de los vecinos | Cuando las anomalías se encuentran en regiones de baja densidad |
| **Codificadores automáticos** | Error de reconstrucción; error alto = anomalía | Patrones complejos y no lineales |
| **Basado en LSTM** | Predecir el siguiente paso; gran error de predicción = anomalía | Anomalías secuenciales |
### Aplicaciones
| Dominio | Qué significan las anomalías |
|--------|-------------------|
| **Finanzas** | Fraude, caídas del mercado, caídas repentinas |
| **Cuidado de la salud** | Frecuencia cardíaca anormal, aparición de convulsiones |
| **Fabricación** | Fallos de equipos, defectos de calidad |
| **Ciberseguridad** | Intentos de intrusión, ataques DDoS |
| **Infraestructura** | Sobrecarga del servidor, fallas de red |
---

## Métricas de evaluación
| Métrica | Fórmula (conceptual) | Cuándo utilizar |
|--------|---------------------|-------------|
| **MAE** (Error medio absoluto) | Media de errores absolutos | Interpretables; mismas unidades que los datos |
| **RMSE** (Error cuadrático medio) | Raíz cuadrada de errores cuadráticos medios | Penaliza más los grandes errores |
| **MAPE** (Error porcentual absoluto medio) | Media de errores porcentuales absolutos | Cuando el error relativo importa |
| **SMAPE** (MAPE simétrico) | Versión simétrica de MAPE | Maneja mejor los valores cercanos a cero |
| **MASE** (Error escalado absoluto medio) | MAE frente a una previsión ingenua | Comparando entre diferentes series |
---

## Flujo de trabajo práctico
| Paso | Descripción |
|------|-------------|
| **1. Explorar** | Trama la serie; identificar tendencia, estacionalidad y valores atípicos |
| **2. Descomponer** | Separar en componentes tendenciales, estacionales y residuales |
| **3. Estacionar** | Aplicar diferenciación o transformaciones si es necesario |
| **4. Dividir** | División basada en el tiempo (nunca división aleatoria para series temporales) |
| **5. Línea de base** | Comience con un pronóstico ingenuo (último valor, ingenuo estacional) |
| **6. Modelo** | Pruebe los métodos clásicos (ARIMA, Prophet), luego los métodos ML |
| **7. Evaluar** | Utilice métricas apropiadas; comparar con la línea de base |
| **8. Iterar** | Agregue funciones, pruebe diferentes modelos, ajuste hiperparámetros |
---

## Herramientas y bibliotecas
| Herramienta | Propósito |
|------|---------|
| **modelos de estadísticas** | Series temporales clásicas (ARIMA, ETS, descomposición) |
| **Profeta** (Meta) | Previsión de series temporales de negocios |
| **tiempo de espera** | Interfaz ML unificada para series temporales |
| **Dardos** | Biblioteca completa de pronósticos (clásico + aprendizaje profundo) |
| **GluonTS** (Amazonía) | Modelado probabilístico de series temporales |
| **Profeta Neural** | Profeta con componentes de red neuronal |
| **tsfresco** | Extracción automática de características de series temporales |
| **pandas** | Manipulación y remuestreo de series temporales |
---

## Resumen
El pronóstico de series temporales combina las estadísticas clásicas con el aprendizaje automático moderno. Los métodos clásicos (ARIMA, suavizado exponencial, Prophet) son interpretables, rápidos y a menudo precisos. Los métodos de aprendizaje profundo (LSTM, Transformers) capturan patrones complejos pero requieren más datos y ajustes. Los principios clave siguen siendo los mismos independientemente del método: comprenda la estructura de sus datos (tendencia, estacionalidad, ruido), compare con una línea de base simple, evalúe con métricas apropiadas y tenga en cuenta que el futuro no replicará exactamente el pasado.