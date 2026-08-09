---
# Metadatos
título: "Fundamentos de la PNL"
descripción: "Procesamiento de texto, incrustaciones, Transformers, BERT, GPT"
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
Etiquetas: [pnl, inteligencia artificial y aprendizaje automático]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "8 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Fundamentos de PNL
El procesamiento del lenguaje natural (PNL) es el campo de enseñar a las máquinas a comprender, generar y trabajar con el lenguaje humano. Impulsa motores de búsqueda, chatbots, sistemas de traducción, análisis de sentimientos y los grandes modelos de lenguaje (LLM) que han transformado la IA desde 2020. Este archivo cubre la evolución desde las técnicas clásicas hasta las arquitecturas modernas basadas en Transformer.
---

## Preprocesamiento de texto
El texto sin formato está desordenado. Antes de que un modelo pueda usarlo, es necesario limpiarlo y estructurarlo.
| Paso | Qué hace | Ejemplo |
|------|-------------|---------|
| **Tokenización** | Dividir texto en tokens (palabras, subpalabras o caracteres) | "Me encanta la PNL" →`["I", "love", "NLP"]`|
| **Minúsculas** | Convertir a minúsculas | "Hola" → "hola" |
| **Detener eliminación de palabras** | Eliminar palabras comunes (the, is, at) | "el gato se sentó" → "el gato se sentó" |
| **Derivado** | Cortar terminaciones de palabras (crudas) | "corriendo" → "correr" |
| **Lematización** | Reducir a forma de diccionario (considerando el contexto) | "mejor" → "bueno" |
| **Normalización** | Corregir codificación, eliminar caracteres especiales, expandir contracciones | "no" → "no" |
Los modelos Transformer modernos a menudo omiten la eliminación y la derivación de palabras vacías: aprenden estos patrones a partir de los datos.
---

## Representación de texto
Las máquinas necesitan números, no palabras. La forma en que representamos el texto como vectores es fundamental.
### Enfoques clásicos
| Método | Descripción | Limitación |
|--------|-------------|-----------|
| **Codificación en caliente** | Cada palabra es una posición única en un vector enorme | Escaso; sin significado semántico |
| **Bolsa de palabras (Arco)** | Cuente la frecuencia de las palabras; ignorar orden | Pierde el orden de las palabras por completo |
| **TF-IDF** | Ponderar palabras por frecuencia en el documento × rareza en el corpus | Todavía ignora el orden y el contexto |
### Incrustaciones de palabras
Las incrustaciones asignan palabras a vectores densos donde palabras similares están muy juntas.
| Modelo | Idea clave |
|-------|----------|
| **Palabra2Vec** (2013) | Predecir palabra a partir del contexto (CBOW) o contexto a partir de la palabra (Skip-gram) |
| **Guante** (2014) | Estadísticas globales de coocurrencia → vectores densos |
| **Texto rápido** (2016) | Word2Vec + información de subpalabras (maneja mejor las palabras raras) |
El famoso ejemplo:`king - man + woman ≈ queen`. Las incrustaciones capturan relaciones semánticas.
**Limitación**: las incrustaciones clásicas asignan un vector por palabra, por lo que no pueden manejar la polisemia (palabras con múltiples significados). "Banco" en "orilla del río" y "cuenta bancaria" obtienen el mismo vector.
---

## Modelos de secuencia
Antes de Transformers, el enfoque estándar de PNL era procesar texto de forma secuencial.
| Arquitectura | Cómo funciona | Fuerza | Debilidad |
|-------------|-------------|----------|----------|
| **RNN** | Procese los tokens uno a la vez; mantener estado oculto | Maneja entradas de longitud variable | Degradados que desaparecen; no puede capturar dependencias largas |
| **LSTM** | RNN con puertas (olvido, entrada, salida) para controlar el flujo de información | Mejor en dependencias de largo alcance | Todavía secuencial; lento para entrenar |
| **GRU** | LSTM simplificado (menos puertas) | Más rápido que LSTM; rendimiento similar | Mismas limitaciones fundamentales |
Estos modelos procesan texto de izquierda a derecha, lo que significa que su entrenamiento es lento (no pueden paralelizarse) y tienen problemas con dependencias de largo alcance.
---

## El mecanismo de atención
La atención permite que un modelo observe todas las posiciones en una secuencia simultáneamente y decida cuáles son las más relevantes para la predicción actual.
### Información clave
En lugar de comprimir una oración completa en un único estado oculto (como lo hacen los RNN), la atención calcula una suma ponderada de todos los estados ocultos, donde se aprenden los pesos.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Componente | Rol |
|-----------|--------------|
| **Consulta (Q)** | ¿Qué estoy buscando? |
| **Clave (K)** | ¿Qué contengo? |
| **Valor (V)** | ¿Qué información proporciono? |
| **√d_k** | Factor de escala para evitar productos punto grandes |
---

## La arquitectura transformadora
The Transformer (Vaswani et al., 2017 - "La atención es todo lo que necesitas") reemplazó la recurrencia por completo con atención. Es la base de prácticamente toda la PNL moderna.
### Arquitectura
| Componente | Descripción |
|-----------|-------------|
| **Codificador** | Lee el texto de entrada; produce representaciones contextuales |
| **Decodificador** | Genera texto de salida; atiende a la salida del codificador |
| **Autoatención** | Cada token atiende a todos los demás tokens en la misma secuencia |
| **Atención multicabezal** | Ejecute varios cabezales de atención en paralelo; capturar diferentes relaciones |
| **Codificación posicional** | Inyectar información de posición (ya que no hay recurrencia) |
| **Red de retroalimentación** | Aplicado a cada puesto de forma independiente |
| **Normalización de capas** | Estabilizar el entrenamiento |
| **Conexiones residuales** | Saltar conexiones para flujo en gradiente |
### Sólo codificador, Sólo decodificador, Codificador-Decodificador
| Variante | Arquitectura | Mejor para | Ejemplos |
|---------|-------------|----------|---------|
| **Solo codificador** | Entiende texto | Clasificación, NER, análisis de sentimiento | BERT, RoBERTa, DeBERTa |
| **Solo decodificador** | Genera texto | Modelos de lenguaje, chatbots, generación de código | GPT-3/4, LLaMA, Claude |
| **Codificador-Decodificador** | Transforma texto | Traducción, resumen | T5, BART, mBART |
---

## Familias modelo principales
### Familia BERT (solo codificador)
| Modelo | Característica clave |
|-------|-------------|
| **BERTO** (2018) | Modelo de lenguaje enmascarado + Predicción de la siguiente oración |
| **RoBERTa** | Se eliminó el NSP; entrenado por más tiempo con más datos |
| **ALBERTO** | Compartir parámetros; huella más pequeña |
| **DeBERTa** | Atención desenredada; NLU mejorada |
| **DistilBERT** | 40 % más pequeño, 60 % más rápido, conserva el 97 % del rendimiento de BERT |
### Familia GPT (solo decodificador)
| Modelo | Parámetros | Notas |
|-------|-----------|-------|
| **GPT-2** | 1.500 millones | Los modelos mostrados sólo con decodificador pueden generar texto coherente |
| **GPT-3** | 175B | Aprendizaje en pocas oportunidades; impulsado en lugar de ajustado |
| **GPT-3.5/GPT-4** | No revelado | Instrucción ajustada + RLHF; conversacional |
| **LLaMA** (Meta) | 7B–70B | Peso abierto; generó el ecosistema LLM de código abierto |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Modelos abiertos eficientes con gran rendimiento |
---

## Tareas principales de PNL
| Tarea | Descripción | Modelo típico |
|------|-------------|--------------|
| **Clasificación de texto** | Asignar una etiqueta al texto (spam/no spam, positivo/negativo) | BERT, clasificadores afinados |
| **Reconocimiento de entidad nombrada (NER)** | Identificar personas, organizaciones y ubicaciones en el texto | Capa BERT + CRF |
| **Análisis de sentimiento** | Determinar el tono emocional | BERT ajustado o LLM de tiro cero |
| **Traducción automática** | Traducir entre idiomas | T5, mBART, MarianMT |
| **Respuesta de preguntas** | Responder preguntas dado el contexto | BERT (extractivo), GPT (generativo) |
| **Resumen** | Texto largo condensado | T5, BART, GPT |
| **Generación de texto** | Producir texto coherente | GPT-4, LLaMA, Claude |
---

## Ajuste fino frente a indicaciones
| Enfoque | Cómo funciona | Cuándo utilizar |
|----------|-------------|-------------|
| **Ajustes** | Actualice los pesos del modelo en los datos específicos de su tarea | Tienes datos etiquetados; necesita el máximo rendimiento |
| **Instigación** | Dar instrucciones al modelo en lenguaje natural | Creación rápida de prototipos; datos limitados; utilizando LLM |
| **Pocos disparos** | Incluya ejemplos en el mensaje | Cuando tiene algunos ejemplos pero no los suficientes para realizar ajustes |
| **LoRA/QLoRA** | Ajuste eficiente; actualizar pequeñas matrices de bajo rango | Afina modelos grandes con memoria GPU limitada |
---

## Herramientas y marcos
| Herramienta | Propósito |
|------|---------|
| **Abrazando transformadores de cara** | Modelos previamente entrenados, tokenizadores, canalizaciones de ajuste |
| **espacioso** | Canalización de PNL de grado de producción (tokenización, NER, POS, dependencia) |
| **NLTK** | Educativo; algoritmos clásicos de PNL |
| **Gensim** | Modelado de temas (LDA), incrustaciones de palabras (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Marcos para crear aplicaciones impulsadas por LLM |
| **vLLM** | Servicio LLM de alto rendimiento |
| **Tokenizadores (HF)** | Tokenización rápida (BPE, WordPieza, SentencePieza) |
---

## El panorama del LLM
El panorama moderno de la PNL está dominado por grandes modelos de lenguaje:
| Categoría | Ejemplos | Notas |
|----------|---------|-------|
| **Propietario** | GPT-4, Claude, Géminis | Mejor desempeño; Acceso API únicamente |
| **Peso abierto** | LLaMA 3, Mistral, Qwen | Pesos disponibles; ejecutar localmente |
| **Código abierto** | Pitia, OPT | Totalmente abierto (datos, pesos, código) |
| **Multimodal** | GPT-4V, Géminis, LLaVA | Procesar texto + imágenes |
| **Código especializado** | CodeLlama, StarCoder, DeepSeek Coder | Capacitado en código |
| **Pequeño / Eficiente** | Phi-3, Gemma, TinyLlama | Fuerte desempeño a pequeña escala |
El campo avanza rápido. Lo que hoy es vanguardista puede ser reemplazado en meses. Los fundamentos (atención, tokenización, ajuste, evaluación) se mantienen estables.