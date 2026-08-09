---
# Metadatos
título: "Procesamiento de voz y audio"
descripción: "ASR, TTS, funciones de audio, Whisper, canales de voz"
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
Etiquetas: [voz, audio, procesamiento, inteligencia artificial y aprendizaje automático]
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
# Procesamiento de voz y audio
El procesamiento del habla y el audio cubre las tecnologías que permiten a las máquinas escuchar, comprender, generar y manipular el sonido. Esto incluye reconocimiento de voz (convertir palabras habladas en texto), síntesis de voz (convertir texto en palabras habladas), identificación del hablante, generación de música y comprensión del sonido ambiental. El campo se ha visto transformado por el aprendizaje profundo: los sistemas modernos se acercan a la precisión del nivel humano para el reconocimiento de voz y producen voces sintéticas inquietantemente naturales.
---

## Fundamentos del audio digital
El sonido es una onda de presión. Para procesarla digitalmente, tomamos muestras de la ola a intervalos regulares.
| Concepto | Descripción | Valor típico |
|---------|-------------|---------------|
| **Frecuencia de muestreo** | ¿Cuántas veces por segundo se mide el sonido? 8 kHz (teléfono), 16 kHz (voz), 44,1 kHz (CD), 48 kHz (profesional) |
| **Profundidad de bits** | Precisión de cada muestra | 16 bits (CD), 24 bits (profesional), 32 bits flotantes (procesamiento) |
| **Canales** | Mono (1), estéreo (2), envolvente (5.1, 7.1) | Estéreo para música; mono para el habla |
| **Duración** | Duración del audio | Varía |
Una grabación mono de 1 minuto a 16 kHz, 16 bits = 1,92 MB. Una canción estéreo de 3 minutos a 44,1 kHz, 16 bits = 30,3 MB.
---

## Extracción de funciones de audio
Es difícil que los modelos trabajen directamente con las formas de onda de audio sin procesar. Extraemos características que capturan las características importantes del sonido.
| Característica | Lo que captura | Caso de uso |
|---------|-----------------|----------|
| **Espectrograma Mel** | Contenido de frecuencia a lo largo del tiempo, asignado a la percepción auditiva humana | Reconocimiento de voz, clasificación musical |
| **MFCC** (Coeficientes cepstrales de frecuencia de fusión) | Representación compacta de la envolvente espectral | Reconocimiento de voz tradicional |
| **Cromagrama** | Distribución de clases de tono (qué notas se reproducen) | Análisis musical, detección de acordes |
| **Tasa de cruce por cero** | ¿Con qué frecuencia la señal cruza cero? Detección sonora versus sorda |
| **Energía RMS** | Volumen de la señal a lo largo del tiempo | Detección de actividad de voz |
| **Tono (F0)** | Frecuencia fundamental | Identificación de locutores, transcripción de música |
### Espectrograma Mel
La representación de audio más común para el aprendizaje profundo. Convierte el audio a un formato similar a una imagen 2D:
| Eje | Representa |
|------|-----------|
| **Eje X** | Hora |
| **Eje Y** | Frecuencia (en la escala Mel - perceptualmente espaciada) |
| **Color/intensidad** | Energía en esa frecuencia y tiempo |
La escala Mel se aproxima a la audición humana: somos mejores para distinguir las frecuencias bajas de las altas.
---

## Reconocimiento automático de voz (ASR)
ASR convierte el lenguaje hablado en texto. Es una de las aplicaciones de IA de audio más importantes comercialmente.
### Evolución de la ASR
| Época | Enfoque | Limitación |
|-----|----------|------------|
| **Antes de 2010** | Modelos ocultos de Markov + Modelos de mezcla gaussiana | Requirió una extensa ingeniería manual; pobres en condiciones ruidosas |
| **2010-2015** | Híbrido DNN-HMM | Las redes neuronales reemplazaron a los GMM; mejora significativa |
| **2015-2020** | Modelos de extremo a extremo (Deep Speech, LAS) | Red neuronal única de audio a texto |
| **2020+** | Basado en transformador (Whisper, Conformer) | Precisión de última generación; plurilingüe; robusto |
### Modelos clave de ASR
| Modelo | Arquitectura | Datos de entrenamiento | Característica notable |
|-------|-------------|---------------|-----------------|
| **Susurro** (OpenAI) | Transformador codificador-decodificador | 680.000 horas, 99 idiomas | Plurilingüe; resistente a los acentos y al ruido; código abierto |
| **Conformador** | Convolución + autoatención | Varios | Combina funciones locales (conv) y globales (atención) |
| **wav2vec 2.0** | Transformador Autosupervisado | Discurso sin etiqueta | Aprende del audio sin editar y sin transcripciones |
| **USM** (Google) | Modelo de habla universal | 2 millones de horas, más de 300 idiomas | La mayoría de los idiomas cubiertos |
| **MMS** (Meta) | Discurso Masivamente Multilingüe | Más de 1.400 idiomas | Amplía cobertura a lenguas de bajos recursos |
### Métricas ASR
| Métrica | Descripción |
|--------|-------------|
| **WER** (tasa de errores de palabras) | Porcentaje de palabras transcritas incorrectamente. Más bajo es mejor. El desempeño humano es ~4-5% para un inglés limpio. |
| **CER** (tasa de error de caracteres) | Igual que WER pero a nivel de personaje. Se utiliza para idiomas sin límites de palabras (chino, japonés). |
### Desafíos comunes de ASR
| Desafío | Descripción |
|-----------|-------------|
| **Acentos y dialectos** | El rendimiento disminuye significativamente con acentos no estándar |
| **Ruido de fondo** | La música, el tráfico y otros altavoces degradan la precisión |
| **Cambio de código** | Hablantes que cambian de idioma a mitad de una frase |
| **Homófonos** | "Allí" versus "ellos" versus "ellos" - requiere contexto |
| **Puntuación y formato** | La salida ASR normalmente no está puntuada; necesita posprocesamiento |
| **Idiomas de bajos recursos** | La mayoría de los modelos funcionan mal en idiomas con pocos datos de entrenamiento |
---

## Texto a voz (TTS)
TTS convierte texto escrito en audio hablado. Los sistemas modernos producen voz que a menudo es indistinguible de las grabaciones humanas.
### Evolución de TTS
| Época | Enfoque | Calidad |
|-----|----------|---------|
| **Antes de 2010** | Concatenativo (uniendo fragmentos grabados) | Robótico; expresividad limitada |
| **2010-2017** | Estadística paramétrica (HMM, neural temprana) | Mejor pero aún reconocible como sintético |
| **2017-2020** | Neural (Tacotron, WaveNet) | Calidad casi humana; expresivo |
| **2020+** | Códec neuronal (VALL-E, Bark) | Clonación de voz; pocos disparos; muy natural |
### Modelos clave de TTS
| Modelo | Arquitectura | Característica notable |
|-------|-------------|-----------------|
| **WaveNet** (mente profunda) | Modelo generativo autorregresivo | Primer TTS con sonido verdaderamente natural |
| **Tacotrón 2** (Google) | Seq2seq + vocodificador | De extremo a extremo; alta calidad |
| **VITS** | Inferencia variacional + entrenamiento adversario | Rápido; buena calidad; ampliamente utilizado |
| **VALL-E** (Microsoft) | Modelo de lenguaje de códec neuronal | Clonación de voz a partir de una muestra de 3 segundos |
| **Ladrar** (Suno) | Basado en transformador | Plurilingüe; sonidos distintos del habla (risas, música) |
| **ElevenLabs** | Comercial | Clonación de voz líder en la industria |
| **ChatTTS** | Código abierto | Optimizado para discurso conversacional |
| **Discurso de pez** | Código abierto | Rápido; multilingüe |
### Clonación de voz
La clonación de voz crea una voz sintética que suena como una persona específica a partir de una breve muestra de audio.
| Método | Datos necesarios | Calidad |
|--------|------------|---------|
| **Ajustes** | 10-60 minutos de discurso | Alta calidad; específico del hablante |
| **Pocos disparos** | 3-30 segundos de discurso | Buena calidad; configuración rápida |
| **Tiro cero** | No hay datos del hablante objetivo | Utiliza audio de referencia en el momento de la inferencia |
**Preocupación ética**: la clonación de voz se puede utilizar para suplantación de identidad, fraude y deepfakes. La mayoría de los proveedores comerciales requieren consentimiento por voz.
---

## Reconocimiento del orador
| Tarea | Descripción | Solicitud |
|------|-------------|-------------|
| **Verificación del hablante** | "¿Es esta persona quien dice ser?" | Banca telefónica, desbloqueo de dispositivos |
| **Identificación del hablante** | "¿Quién está hablando?" | Transcripción de reuniones, análisis forense |
| **Diario del orador** | "¿Quién habló y cuándo?" (en audio de varios altavoces) | Resúmenes de reuniones, generación de subtítulos |
| Modelo | Enfoque |
|-------|----------|
| **ECAPA-TDNN** | Basado en incrustación; estado del arte para verificación |
| **d-vector** | Incorporaciones simples de altavoces de DNN |
| **vector-x** | Incorporaciones de altavoces mejoradas; ampliamente utilizado |
---

## Recuperación de información musical
| Tarea | Descripción | Herramientas/Modelos |
|------|-------------|-------------|
| **Transcripción de música** | Convertir audio a partituras / MIDI | Tono básico de Spotify, Spleeter |
| **Separación de fuentes** | Aislar instrumentos o voces individuales | Demucs, Spleeter, Separación de fuentes musicales |
| **Clasificación de género** | Clasificar música por género | CNN en espectrogramas |
| **Seguimiento de ritmo** | Detectar tempo y posiciones de tiempo | Librosa, Madmom |
| **Reconocimiento de acordes** | Identificar acordes en la música | Acorde-CNN, modelos CRF |
| **Generación musical** | Crear nueva música | MusicGen, MuseNet, AIVA |
---

## Detección de sonido ambiental
| Tarea | Descripción | Solicitud |
|------|-------------|-------------|
| **Detección de eventos sonoros** | Identificar sonidos en un entorno | Hogar inteligente (rotura de cristales, llanto de bebé) |
| **Clasificación de escenas acústicas** | Clasificar el entorno (oficina, parque, tráfico) | Dispositivos sensibles al contexto |
| **Detección de anomalías** | Detectar sonidos inusuales | Vigilancia industrial (machineæ•…éšœ) |
| Conjunto de datos | Sonidos | Tamaño |
|---------|--------|------|
| **Conjunto de audio** | 632 clases de sonido | Más de 2 millones de clips de YouTube |
| **ESC-50** | 50 clases de sonido ambiental | 2.000 clips |
| **UrbanSound8K** | Sonidos urbanos | 8.732 vídeos |
---

## Herramientas y marcos
| Herramienta | Propósito |
|------|---------|
| **Libros** | Biblioteca Python para análisis de audio (características, efectos, visualización) |
| **Pydub** | Manipulación de audio simple (cortar, concatenar, exportar) |
| **FFmpeg** | Procesamiento de audio/vídeo por línea de comandos (la navaja suiza) |
| **Antorchaudio** | Procesamiento de audio PyTorch (transformaciones, conjuntos de datos, modelos) |
| **Cara abrazada (transformers)** | Modelos ASR y TTS previamente entrenados |
| **Susurro (OpenAI)** | Reconocimiento de voz (código abierto) |
| **Coquí TTS** | Kit de herramientas TTS de código abierto |
| **Demucs** | Separación de fuentes musicales |
| **Cerebro del habla** | Kit de herramientas de voz todo en uno (ASR, TTS, reconocimiento de locutor) |
---

## Consejos prácticos
- **Escuche siempre sus datos.** Antes de entrenar algo, escuche el audio de muestra. Tenga en cuenta la frecuencia de muestreo, el nivel de ruido y las características de los altavoces.
- **Iguala frecuencias de muestreo.** Whisper espera 16 kHz. Si su audio es de 44,1 kHz, vuelva a muestrearlo, pero tenga en cuenta que al reducir la resolución se pierde información.
- **Aumente los datos de audio.** Agregue ruido de fondo, varíe la velocidad y el tono, simule diferentes micrófonos. Esto mejora drásticamente la robustez.
- **Utilice modelos previamente entrenados.** Whisper para ASR y VITS/Bark para TTS son excelentes puntos de partida. Hacer ajustes casi siempre es mejor que entrenar desde cero.
- **Manejar el silencio.** La detección de actividad de voz (VAD) elimina el silencio antes del procesamiento, lo que ahorra cálculo y mejora la precisión. Silero VAD y WebRTC VAD son opciones populares.
- **Normalizar volumen.** Diferentes grabaciones tienen niveles de volumen muy diferentes. Normalice a un nivel consistente antes de procesar.
---

## Resumen
El procesamiento del habla y el audio se ha visto revolucionado por el aprendizaje profundo. Los sistemas ASR modernos como Whisper abordan la precisión a nivel humano en docenas de idiomas. Los sistemas TTS producen voz que es cada vez más indistinguible de las grabaciones humanas. La clonación de voz funciona a partir de segundos de audio. La generación de música, la separación de fuentes y la detección de sonido ambiental están avanzando rápidamente. El campo enfrenta desafíos continuos (lenguajes de bajos recursos, entornos ruidosos, preocupaciones éticas en torno a la clonación de voces), pero la trayectoria es clara: las máquinas se están volviendo tan buenas como los humanos para oír, comprender y producir sonido.