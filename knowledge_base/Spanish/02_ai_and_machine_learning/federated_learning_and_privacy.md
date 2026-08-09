---
# Metadatos
título: "Aprendizaje federado y privacidad"
descripción: "Formación descentralizada, privacidad diferencial, agregación segura"
categoría: "IA y aprendizaje automático"
versión: "1.0.0"
estado: "activo"
# Contribución
autores:
  - nombre: "Equipo de formación del modelo de IA"
    correo electrónico: ""
    rol: "autor_original"
colaboradores: []
registro de cambios:
  - versión: "1.0.0"
    fecha: "2026-08-05"
    autor: "Equipo de formación del modelo de IA"
    cambios: "Se agregaron metadatos de temas frontales de YAML para el seguimiento de los contribuyentes"
# Revisión
creado: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
review_by: "Equipo de base de conocimientos de inteligencia artificial y aprendizaje automático"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [federado, aprendizaje, privacidad, inteligencia artificial y aprendizaje automático]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "9 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Aprendizaje federado y privacidad
El aprendizaje federado es una técnica para entrenar modelos de aprendizaje automático en múltiples dispositivos u organizaciones sin compartir los datos sin procesar. En lugar de enviar datos a un servidor central, cada dispositivo entrena un modelo local y solo comparte las actualizaciones del modelo (gradientes o pesos). El servidor central agrega estas actualizaciones para producir un modelo global. Fue diseñado por Google para entrenar modelos de lenguaje de teclado en teléfonos Android y desde entonces se ha convertido en una técnica clave para la IA que preserva la privacidad.
---

## ¿Por qué el aprendizaje federado?
| Motivación | Descripción | Ejemplo |
|------------|-------------|---------|
| **Privacidad de datos** | Los datos sin procesar nunca salen del dispositivo | Los registros médicos permanecen en el hospital; fotos se quedan en el teléfono |
| **Cumplimiento normativo** | GDPR, HIPAA y otras regulaciones restringen el intercambio de datos | Los bancos pueden colaborar sin compartir los datos de los clientes |
| **Volumen de datos** | Mover datos es caro y lento | La capacitación en miles de millones de teléfonos no es práctica si es necesario cargar datos |
| **Confidencialidad de los datos** | Algunos datos son demasiado confidenciales para compartirlos, incluso con consentimiento | Inteligencia gubernamental; datos personales de salud |
---

## Cómo funciona el aprendizaje federado
### El protocolo básico (FedAvg)
| Paso | Qué pasa |
|------|-------------|
| **1. Inicializar** | Servidor central crea un modelo global con pesos aleatorios |
| **2. Distribuir** | El servidor envía el modelo global actual a los dispositivos seleccionados |
| **3. Formación local** | Cada dispositivo entrena el modelo con sus datos locales durante varias épocas |
| **4. Subir** | Los dispositivos envían los pesos de sus modelos actualizados (no datos) al servidor |
| **5. Agregado** | Servidor promedia los pesos (Promedio Federado) para crear un nuevo modelo global |
| **6. Repetir** | Vuelva al paso 2 hasta que el modelo converja |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Propiedades clave
| Propiedad | Descripción |
|----------|-------------|
| **Datos no IID** | Cada dispositivo tiene distribuciones de datos diferentes (no independientes e idénticamente distribuidas) |
| **Datos no balanceados** | Algunos dispositivos tienen muchos datos, otros tienen muy pocos |
| **Participación parcial** | No todos los dispositivos están disponibles en todas las rondas |
| **Eficiencia de la comunicación** | El cuello de botella es la comunicación, no la computación |
---

## Variantes de aprendizaje federado
| Variante | Descripción | Ventaja |
|---------|-------------|-----------|
| **Promedio Fed** | Pesos promedio de los modelos en todos los dispositivos | Simple; funciona bien para datos IID |
| **FedProx** | Añade un término próximo a la formación local | Mejor para datos que no son IID |
| **ANDAMIO** | Utiliza variables de control para corregir la heterogeneidad de los datos | Convergencia más rápida en datos no IID |
| **FedSGD** | Como FedAvg pero con un paso de gradiente por ronda | Menor costo de comunicación por ronda |
| **FL personalizado** | Cada dispositivo mantiene un modelo personalizado junto al global | Mejor rendimiento por dispositivo |
| **FL verticales** | Diferentes características (no diferentes muestras) entre partidos | Cuando las partes poseen aspectos diferentes de los mismos datos |
---

## Privacidad diferencial
La privacidad diferencial (DP) proporciona una garantía matemática de que el resultado de un algoritmo no revela si se incluyeron datos de algún individuo.
### Definición principal
Un mecanismo M satisface la privacidad diferencial (ε, δ) si para dos conjuntos de datos cualesquiera D y D' que difieren en un registro:
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Parámetro | Significado |
|-----------|------------------|
| **ε (épsilon)** | Presupuesto de privacidad. Más pequeño = más privado. Valores típicos: 0,1–10. |
| **δ (delta)** | Probabilidad de que falle la garantía de privacidad. Normalmente se establece en 1/N (inverso del tamaño del conjunto de datos). |
### Mecanismos para agregar privacidad
| Mecanismo | Cómo funciona | Caso de uso |
|-----------|-------------|----------|
| **Mecanismo gaussiano** | Agregue ruido gaussiano calibrado a la sensibilidad de la consulta | Valores continuos (ponderaciones del modelo) |
| **Mecanismo de Laplace** | Añadir ruido de Laplace | Contando consultas |
| **Mecanismo exponencial** | Seleccionar productos con probabilidad proporcional a su utilidad | Opciones discretas |
### DP-SGD (Descenso de gradiente estocástico diferencialmente privado)
| Paso | Descripción |
|------|-------------|
| 1. Calcular gradientes por muestra | En lugar de gradientes por lotes |
| 2. Recortar degradados | Limita la norma máxima de cada gradiente (limita la influencia de cualquier muestra única) |
| 3. Añade ruido | Agregue ruido gaussiano calibrado al gradiente agregado |
| 4. Actualizar parámetros | Paso de descenso de gradiente estándar |
| Compensación | Descripción |
|-----------|-------------|
| **Privacidad versus precisión** | Una mayor privacidad (ε inferior) requiere más ruido, lo que reduce la precisión del modelo |
| **Privacidad vs tiempo de entrenamiento** | Más ruido significa una convergencia más lenta |
| **Seguimiento del presupuesto de privacidad** | Cada paso de la formación consume parte del presupuesto de privacidad; una vez gastado, no se puede recuperar |
---

## Combinando el aprendizaje federado con la privacidad diferencial
| Capa | Protección |
|-------|-----------|
| **Aprendizaje federado** | Los datos sin procesar permanecen en los dispositivos |
| **Privacidad diferencial** | Incluso las actualizaciones de modelos son ruidosas y protegen las contribuciones individuales |
| **Agregación segura** | El servidor sólo ve el conjunto de todas las actualizaciones, no las individuales |
Esta combinación proporciona sólidas garantías de privacidad: incluso si el servidor está comprometido, no puede determinar si los datos de algún individuo específico se utilizaron en la capacitación.
---

## Otras técnicas para preservar la privacidad
### Computación segura multipartita (SMPC)
Varias partes calculan una función sobre sus datos combinados sin revelar sus entradas individuales.
| Característica | Descripción |
|---------|-------------|
| **Cómo funciona** | Los datos se dividen en partes distribuidas entre las partes; el cálculo ocurre en acciones |
| **Garantía** | Ningún partido aprende nada sobre las aportaciones de los demás |
| **Arriba** | Importante coste de comunicación y cálculo |
| **Caso de uso** | Los bancos calculan modelos de riesgo conjunto sin compartir datos de clientes |
### Cifrado homomórfico (HE)
Realice cálculos directamente sobre datos cifrados.
| Tipo | Qué soporta | Arriba |
|------|-----------------|----------|
| **Parcialmente ÉL** | Una operación (suma O multiplicación) | Bajo |
| **Algo ÉL** | Número limitado de ambas operaciones | Medio |
| **Completamente ÉL** | Cálculos arbitrarios | Muy alto (desaceleración de 100-1000x) |
| Solicitud | Descripción |
|-------------|-------------|
| **Inferencia privada** | Ejecute modelos de aprendizaje automático con datos cifrados; devolver predicciones cifradas |
| **Entrenamiento cifrado** | Capacítese con datos cifrados (aún en su mayoría teóricos para el aprendizaje profundo) |
| **Consultas privadas** | Consultar una base de datos sin revelar la consulta ni los datos |
### Entornos de ejecución confiables (TEE)
Aislamiento basado en hardware (Intel SGX, ARM Trustzone) que protege los datos incluso del sistema operativo.
| Ventaja | Limitación |
|-----------|------------|
| Rendimiento casi nativo | Requiere hardware específico |
| Fuertes garantías de seguridad | Memoria limitada (tamaño de enclave) |
| Sin sobrecarga criptográfica | Posibles ataques de canal lateral |
---

## Regulaciones de privacidad y ML
| Reglamento | Región | Impacto en el aprendizaje automático |
|------------|--------|-------------|
| **RGPD** | UE | Derecho a explicación; minimización de datos; consentimiento para el procesamiento; derecho de supresión |
| **CCPA** | California | Derecho a conocer, eliminar y excluirse de la venta de datos |
| **HIPAA** | EE.UU. (atención sanitaria) | Controles estrictos sobre los datos de salud; requisitos de desidentificación |
| **PIPL** | China | Localización de datos; requisitos de consentimiento; normas de transferencia transfronteriza |
| **Ley de IA** | UE | Requisitos de transparencia; clasificación de riesgos; prácticas prohibidas |
### Impacto en los flujos de trabajo de ML
| Principio RGPD | Implicación del aprendizaje automático |
|----------------|---------------|
| **Minimización de datos** | Reúna sólo lo que se necesita; el aprendizaje federado ayuda |
| **Limitación de finalidad** | No se pueden reutilizar los datos sin un nuevo consentimiento |
| **Derecho de supresión** | Debe poder eliminar los datos de una persona de un modelo entrenado (desaprendizaje automático) |
| **Derecho a explicación** | Los modelos deben ser lo suficientemente interpretables para explicar las predicciones individuales |
| **Privacidad por diseño** | La privacidad debe integrarse en los sistemas desde el principio |
---

## Desafíos
| Desafío | Descripción |
|-----------|-------------|
| **Coste de comunicación** | Enviar actualizaciones de modelos a millones de dispositivos es caro |
| **Datos no IID** | Los dispositivos tienen distribuciones de datos muy diferentes, lo que perjudica la convergencia |
| **Rezagados** | Dispositivos lentos retrasan toda la ronda |
| **Compensación entre privacidad y servicios públicos** | Una mayor privacidad significa un peor rendimiento del modelo |
| **Ataques de envenenamiento** | Los participantes malintencionados pueden corromper el modelo global |
| **Extracción de modelo** | Incluso las actualizaciones de modelos compartidas pueden filtrar información sobre datos de entrenamiento |
| **Heterogeneidad del hardware** | Diferentes dispositivos tienen diferentes capacidades informáticas |
---

## Herramientas y marcos
| Herramienta | Propósito |
|------|---------|
| **Flor** | Marco de aprendizaje federado de código abierto; independiente del marco |
| **TensorFlow federado** | Marco FL de Google para modelos TensorFlow |
| **PySyft** (OpenMined) | ML que preserva la privacidad en PyTorch |
| **DESTINO** (Webank) | Plataforma de aprendizaje federado de nivel industrial |
| **HOJA** | Conjunto de referencias para la investigación del aprendizaje federado |
| **Opacus** (Meta) | Privacidad diferencial para PyTorch |
| **Privacidad TF de Google** | Privacidad diferencial para TensorFlow |
---

## Resumen
El aprendizaje federado y las técnicas de preservación de la privacidad abordan una tensión fundamental: ¿cómo se construyen modelos de IA potentes cuando los datos están distribuidos, son confidenciales o están regulados? El aprendizaje federado mantiene datos en los dispositivos y comparte solo actualizaciones de modelos. La privacidad diferencial añade garantías matemáticas de que no se pueden detectar las contribuciones individuales. La computación segura y el cifrado homomórfico van más allá y permiten el cálculo de datos cifrados. Cada técnica tiene costos (gastos generales de comunicación, precisión reducida, gastos computacionales), pero juntas forman un conjunto de herramientas para construir una IA que respete la privacidad y al mismo tiempo aprenda de los datos del mundo.