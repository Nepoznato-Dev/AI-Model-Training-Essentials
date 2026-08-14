---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [computer, vision, ai-and-machine-learning]
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

# Fundamentos de visión por computadora
La visión por computadora brinda a las máquinas la capacidad de interpretar y comprender información visual del mundo: imágenes, videos y datos 3D. Impulsa todo, desde el reconocimiento facial en su teléfono hasta vehículos autónomos, análisis de imágenes médicas y control de calidad industrial. Este archivo cubre los conceptos, arquitecturas y técnicas principales.
---

## Cómo ven las imágenes las computadoras
### Píxeles y canales
Una imagen digital es una cuadrícula de píxeles. Cada píxel tiene valores numéricos que representan la intensidad del color.
| Tipo de imagen | Canales | Valores por píxel | Ejemplo |
|-----------|----------|-----------------|---------|
| **Escala de grises** | 1 | 0 (negro) a 255 (blanco) | Radiografías médicas |
| **RGB** | 3 | Rojo, verde, azul (cada uno de 0 a 255) | Fotografías en color estándar |
| **RGBA** | 4 | RGB + Alfa (transparencia) | Imágenes con fondos transparentes |
| **VHS** | 3 | Tono, saturación, valor | Segmentación basada en colores |
Una imagen RGB de 1920 × 1080 es un tensor de forma `(1080, 1920, 3)`, es decir, 6,2 millones de píxeles, cada uno con 3 valores.
### Operaciones clave
| Operación | Descripción |
|-----------|-------------|
| **Cambiar tamaño** | Escalar la imagen a las dimensiones objetivo (interpolación bilineal del vecino más cercano) |
| **Recorte** | Extraer una región de interés |
| **Normalización** | Escale los valores de píxeles a [0,1] o [-1,1] para redes neuronales |
| **Aumento** | Ampliar artificialmente los datos de entrenamiento (rotación, giro, fluctuación de color, recorte) |
---

## Convolución: la operación central
Una convolución desliza un pequeño filtro (núcleo) a través de la imagen, calculando productos escalares en cada posición. Así es como las CNN detectan bordes, texturas y patrones.
### Parámetros de convolución
| Parámetro | Efecto |
|-----------|----------------|
| **Tamaño del kernel** | 3×3, 5×5, 7×7: los núcleos más grandes capturan patrones más grandes |
| **Paso** | Tamaño del paso; stride=2 reduce a la mitad las dimensiones de salida |
| **Relleno** | Agregue ceros alrededor del borde para preservar las dimensiones espaciales |
| **Número de filtros** | Cada filtro aprende una característica diferente (borde, textura, patrón de color) |
### Qué aprenden las convoluciones
| Profundidad de capa | Funciones detectadas |
|-------------|------------------|
| **Primeras capas** | Bordes, esquinas, texturas simples |
| **Capas intermedias** | Formas, partes de objetos (ruedas, ojos, hojas) |
| **Capas profundas** | Conceptos de alto nivel (rostros, coches, animales) |
---

## Arquitecturas CNN
La evolución de las arquitecturas CNN cuenta la historia del progreso del aprendizaje profundo en la visión por computadora.
| Arquitectura | Año | Innovación clave |
|-------------|------|---------------|
| **LeNet-5** | 1998 | Primera CNN práctica; reconocimiento de dígitos |
| **AlexNet** | 2012 | Deep CNN gana ImageNet; ReLU, abandono, entrenamiento de GPU |
| **VGGNet** | 2014 | Convoluciones apiladas de 3 × 3 (más profundas = mejores) |
| **GoogLeNet (Inicio)** | 2014 | Módulos iniciales (tamaños de filtro paralelos); 22 capas |
| **ResNet** | 2015 | Saltar conexiones (aprendizaje residual); Más de 152 capas |
| **EfficientNet** | 2019 | Escalado compuesto (profundidad + ancho + resolución) |
| **ConvNeXt** | 2022 | ResNet modernizado; competitivo con transformadores |
### Por qué ResNet lo cambió todo
Antes de ResNet, entrenar redes muy profundas era casi imposible debido al problema del gradiente evanescente. ResNet introdujo **saltar conexiones** (también llamadas conexiones residuales): la entrada a una capa se agrega a su salida.
```
output = F(x) + x    # Skip connection
```

Esta idea simple permitió entrenar redes con más de 152 capas de manera efectiva y ahora es estándar en prácticamente todas las arquitecturas profundas.
---

## Tareas principales de la visión
### Clasificación de imágenes
Asigne una etiqueta a una imagen completa.
| Modelo | Enfoque |
|-------|----------|
| CNN (ResNet, EfficientNet) | Enfoque tradicional; excelente precisión |
| Transformadores de visión (ViT) | Trate la imagen como una secuencia de parches; Codificador de transformador |
| Transferir aprendizaje | Ajuste un modelo previamente entrenado en su conjunto de datos |
### Detección de objetos
Busque y clasifique varios objetos dentro de una imagen, con cuadros delimitadores.
| Modelo | Tipo | Velocidad |
|-------|------|-------|
| **R-CNN** | Dos etapas (propuesta + clasificación) | Lento |
| **R-CNN rápido** | Mejorado de dos etapas | Medio |
| **R-CNN más rápido** | Región Propuesta Red + detector | Medio |
| **YOLO** (v1–v10) | De una sola etapa; predecir cajas + clases en una sola pasada | Muy rápido |
| **DETR** | Basado en transformador; sin cajas de anclaje | Medio |
**YOLO** (Sólo miras una vez) es la opción ideal para la detección en tiempo real. Se prefiere **R-CNN** más rápido cuando la precisión importa más que la velocidad.
### Segmentación de imágenes
Clasifica cada píxel de una imagen.
| Tipo | Descripción | Caso de uso |
|------|-------------|----------|
| **Segmentación semántica** | Cada píxel recibe una etiqueta de clase | Conducción autónoma (carretera, coche, peatón) |
| **Segmentación de instancias** | Cada píxel + ID de instancia de objeto | Contar objetos, imágenes médicas |
| **Segmentación panóptica** | Semántica + instancia combinada | Comprensión integral de la escena |
Modelos clave: U-Net (imágenes médicas), Mask R-CNN (instancia), DeepLab (semántico), Segment Anything Model (SAM - segmentación universal).
### Generación de imágenes
| Enfoque | Descripción | Ejemplos |
|----------|-------------|----------|
| **GAN** | Entrenamiento adversario generador versus discriminador | EstiloGAN, CicloGAN |
| **VAEs** | Aprenda la distribución latente; muestra para generar | Autocodificadores variacionales |
| **Modelos de difusión** | Eliminar iterativamente el ruido aleatorio | Difusión estable, DALL-E, mitad del viaje |
Los modelos de difusión han superado en gran medida a las GAN en cuanto a calidad de generación de imágenes.
---

## Transferir aprendizaje para la visión
Entrenar una CNN desde cero requiere computación y datos masivos. El aprendizaje por transferencia le permite comenzar con un modelo ya entrenado en millones de imágenes (ImageNet) y ajustarlo para su tarea específica.
### Pasos
1. **Elija un modelo previamente entrenado** (ResNet50, EfficientNet-B0, ViT).
2. **Reemplace el encabezado de clasificación** por el suyo propio (que coincida con su número de clases).
3. **Congelar las primeras capas** (capturan características genéricas como bordes).
4. **Ajuste** su conjunto de datos con una tasa de aprendizaje baja.
5. **Descongelar gradualmente** si necesitas más adaptación.
Este enfoque logra habitualmente una alta precisión con tan solo entre 1.000 y 10.000 imágenes etiquetadas.
---

## Aumento de datos
El aumento expande artificialmente su conjunto de datos de entrenamiento mediante la aplicación de transformaciones.
| Aumento | Efecto | Cuándo utilizar |
|-------------|--------|-------------|
| **Recorte aleatorio** | Recortar a región aleatoria | Casi siempre |
| **Giro horizontal** | Imagen reflejada | Cuando la orientación no importa |
| **Rotación** | Girar en ángulo aleatorio | Cuando los objetos aparecen en cualquier ángulo |
| **Vibración del color** | Ajusta aleatoriamente el brillo, el contraste y la saturación | Cuando la iluminación varía |
| **Borrado aleatorio** | Enmascarar regiones aleatorias | Mejora la robustez |
| **Mezcla/CortarMezcla** | Combina dos imágenes y etiquetas | Regularización |
Bibliotecas: `torchvision.transforms`, `albumentations`, `imgaug`, `tf.keras.preprocessing`.
---

## Herramientas y marcos
| Herramienta | Propósito |
|------|---------|
| **OpenCV** | Operaciones CV clásicas (filtrado, detección de bordes, transformaciones geométricas) |
| **visión de antorcha** | Modelos de visión de PyTorch, transformaciones y conjuntos de datos |
| **tf.keras.aplicaciones** | Modelos previamente entrenados en TensorFlow/Keras |
| **Ultralíticos (YOLOv8/v11)** | Detección, segmentación, clasificación de objetos |
| **Cara abrazada (transformers)** | Transformadores de visión, SegFormer, DETR |
| **Segmentar cualquier cosa (SAM)** | Segmentación de imágenes universal de Meta |
| **Abumentaciones** | Biblioteca de aumento de imágenes rápida y flexible |
---

## Consejos prácticos
- **Comience con el aprendizaje por transferencia.** En casi todos los casos, ajustar un modelo previamente entrenado es mejor que entrenar desde cero.
- **Normalice sus entradas.** Haga coincidir la normalización que espera el modelo previamente entrenado (generalmente media/estándar de ImageNet).
- **Utilice métricas apropiadas.** Precisión para conjuntos de datos equilibrados; F1, mAP o IoU para tareas de detección o desequilibrio.
- **Visualice sus datos.** Mire imágenes de muestra, verifique las distribuciones de clases, inspeccione las predicciones del modelo.
- **Aumente sabiamente.** Aplique únicamente las transformaciones que tengan sentido para su dominio (no invierta las imágenes médicas verticalmente).
- **Monitorear el sobreajuste.** Si la precisión del entrenamiento es alta pero la validación es baja, aumente el aumento o agregue abandono.