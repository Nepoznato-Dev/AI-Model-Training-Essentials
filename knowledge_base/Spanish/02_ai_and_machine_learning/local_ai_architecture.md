---
# Metadatos
título: "Arquitectura local de IA"
descripción: "Arquitecturas de implementación de IA local"
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
Etiquetas: [local, ai, arquitectura, ai y aprendizaje automático]
nivel_dificultad: "intermedio"
requisitos previos: []
estimado_reading_time: "10 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Arquitectura de IA local
Una guía práctica para ejecutar modelos de lenguaje grandes completamente en el dispositivo: consideraciones de hardware, motores de inferencia, optimización de la memoria y diseño de sistemas para la implementación periférica.
---

## ¿Por qué ejecutar la IA localmente?
- **Privacidad**: No salen datos del dispositivo.
- **Costo**: Sin tarifas API por token.
- **Latencia**: inferencia predecible y sin red.
- **Disponibilidad sin conexión**: Funciona sin internet.
- **Control**: control total sobre la versión, personalización y ajuste del modelo.
---

## Requisitos de hardware
### Memoria GPU (VRAM)
El recurso más crítico. Tamaño del modelo en memoria ≈ **parámetros × bytes por parámetro**.
| Precisión | Bytes por parámetro | Modelo 3.8B | modelo 7B | modelo 13B | modelo 70B |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32 | 4 | ~15 GB | ~28GB | ~52GB | ~280GB |
| FP16 | 2 | ~7,6 GB | ~14 GB | ~26GB | ~140GB |
| INT8 (8 bits) | 1 | ~3,8GB | ~7GB | ~13 GB | ~70GB |
| INT4 (4 bits) | 0,5 | ~1,9GB | ~3,5GB | ~6,5 GB | ~35GB |
**Pautas prácticas:**
- 8GB VRAM → hasta modelos 7B a 4 bits.
- 12GB VRAM → hasta 13B modelos a 4 bits.
- 24 GB de VRAM → hasta 70 B en modelos de 4 bits (o 13 B en 8 bits).
- Apple Silicon (memoria unificada) puede ejecutar modelos de 70B en sistemas de más de 64GB.
### RAM (memoria del sistema)
- Para la inferencia de CPU, necesita suficiente RAM del sistema para cargar el modelo (similar a los números de VRAM).
- Para la inferencia de GPU, la RAM del sistema es importante para cargar el modelo en la memoria antes de descargarlo a la VRAM.
### Almacenamiento
- Los pesos de los modelos cuantificados ocupan unos pocos GB (por ejemplo, 4 bits 7B ≈ 4 GB en disco). Asegúrese de tener al menos entre 20 y 50 GB libres para varios modelos.
### CPU
- Para el procesamiento rápido (relleno previo) y la descarga de la CPU, resulta útil una CPU multinúcleo moderna.
- Los chips Apple de la serie M tienen un rendimiento excelente para LLM gracias a la memoria unificada y Neural Engine.
---

## Cuantización
La cuantificación reduce la precisión numérica de los pesos, reduciendo drásticamente la memoria y aumentando la velocidad con un pequeño coste de precisión.
### Formatos populares
| Formato | Puntas | Descripción | Uso típico |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | formato llama.cpp, optimizado para híbrido CPU/GPU | Lo mejor para la inferencia local |
| **GPTQ** | 4–8 | Solo GPU, eficiente en CUDA | Lo mejor para GPU NVIDIA |
| **AWQ** | 4 | Con reconocimiento de activación, solo GPU | Bueno para la inferencia por lotes en GPU |
| **ONNX** | variables | Estandarizado, multiplataforma | Servicio de producción |
### Elección de un nivel de cuantificación
- **Q8_0** (8 bits): pérdida mínima de calidad, tamaño más grande.
- **Q6_K** (6 bits): buena calidad, compresión decente.
- **Q5_K_M** (5 bits): punto óptimo común.
- **Q4_K_M** (4 bits): calidad más pequeña y aceptable para la mayoría de las tareas.
- **IQ4_XS** / **IQ3_XS**: Cuantización mejorada con mejor perplejidad a 4/3 bits.
**Regla general:** Utilice Q4_K_M para lograr un buen equilibrio entre calidad y tamaño. Si tiene VRAM adicional, use Q5 o Q6.
---

## Motores de inferencia (locales)
### llama.cpp
- Escrito en C++.
- Admite el formato GGUF.
- Optimizado para CPU y GPU (a través de CUDA, Metal, OpenCL).
- Muy rápido, especialmente en CPU.
- Línea de comandos, modo servidor y enlaces de Python.
**Comando de ejemplo:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Envuelve llama.cpp con una CLI simple y una API REST.
- Descarga automáticamente modelos, los gestiona.
- Ideal para creación de prototipos y aplicaciones de escritorio.
- Admite archivos de modelo personalizados para indicaciones del sistema.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### Estudio LM
- Aplicación gráfica de escritorio para Windows, macOS, Linux.
- Interfaz de chat y descarga con un solo clic.
- Servidor local integrado con API compatible con OpenAI.
- Bueno para usuarios no técnicos y pruebas rápidas.
### Transformadores de cara abrazada + bitsandbytes
- La biblioteca estándar de Python para modelos HF.
- Utilice`bitsandbytes`para cuantificación de 4 bits (`load_in_4bit=True`).
- Más flexible para ajustes finos pero más lento que llama.cpp para inferencias.
### ExLlamaV2
- Inferencia de GPU muy rápida para GPTQ y AWQ.
- Mejor rendimiento en GPU NVIDIA.
- Admite generación por lotes.
### mlx (manzana)
- Marco de Apple para chips de la serie M.
- Altamente optimizado para Apple Silicon.
- API de Python.
---

## Gestión de memoria
### Ventana de contexto y caché KV
La caché KV almacena pares clave-valor para cada capa y cada token en el contexto. Crece linealmente con la longitud del contexto.
Costo de memoria ≈ 2 × capas × (cabezas KV × cabeza tenue) × tokens × bytes por valor
Para un modelo de 32 capas con cabezales de 8 KV y 128 cabezales tenues, cada token cuesta ~32 × 8 × 128 × 2 bytes = 65 KB por token. Para tokens de 128k, son ~8 GB solo para el caché.
### Estrategias de descarga
- **Descarga de capas**: coloque algunas capas en la GPU y otras en la CPU. Más rápido que la CPU pura, menor requisito de VRAM.
- **Transmisión de tokens**: procese los tokens de forma incremental en lugar de hacerlo todos a la vez.
### Almacenamiento en caché rápido
Reutilice las cachés de KV en mensajes similares para evitar volver a calcular la fase de precarga. Algunos marcos admiten esto (por ejemplo, vLLM, llama.cpp con `--prompt-cache`).
### Archivos asignados en memoria
Cargue los pesos de los modelos directamente desde el disco sin cargarlos por completo en la RAM (útil para modelos grandes en sistemas con memoria limitada). llama.cpp utiliza mapeo de memoria de forma predeterminada.
---

## Arquitecturas de implementación
### Modo de dispositivo único
Un modelo se ejecuta en una máquina (computadora portátil, teléfono inteligente, dispositivo perimetral). Se utiliza para asistentes personales, aplicaciones para tomar notas y completar código.
### Nube de borde híbrida
El modelo local maneja consultas comunes; recurrir a un modelo de nube para preguntas complejas. Esto ofrece lo mejor de ambos mundos: velocidad/privado para la mayoría, capacidad para casos extremos.
### Inferencia distribuida (Multi-GPU)
Para modelos más grandes, divida las capas en varias GPU (paralelismo tensorial) o divida el contexto entre dispositivos (paralelismo de canalización). Utilice llama.cpp con`-ngl`o ExLlamaV2 con `--num-gpu-layers`.
### Implementación móvil
- **Android**: use llama.cpp a través de enlaces JNI o ML Kit.
- **iOS**: use llama.cpp a través de enlaces Swift o mlx.
- **Web**: use WebLLM (se ejecuta en WebGPU a través del tiempo de ejecución de ONNX) o transformadores.js.
---

## Optimización del rendimiento
### Atención relámpago
Acelera el cálculo de la atención y reduce el uso de memoria. Disponible en llama.cpp, ExLlamaV2 y bibliotecas de transformadores modernos.
### Inferencia por lotes
Procese múltiples indicaciones en un solo paso hacia adelante. Aumenta drásticamente el rendimiento. Utilice`llama-batch`o vLLM.
### Parada anticipada/Presupuesto de tokens
Establezca un presupuesto máximo de tokens para evitar una generación ilimitada.
### Decodificación especulativa
Utilice un modelo rápido pequeño (borrador) para predecir tokens y luego verifique con el modelo grande en paralelo. Puede producir una aceleración de 2 a 3 veces.
---

## Guía práctica de configuración
### 1. Instalar Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Tirar de un modelo
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Ejecutar con API
```bash
ollama serve
```

Luego envíe solicitudes a `http://localhost:11434/api/generate`.
### 4. Integración de Python
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternativa) Utilice llama.cpp directamente
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Monitoreo y observabilidad
- Seguimiento de la utilización de GPU (`nvidia-smi` en Linux, Monitor de actividad en macOS).
- Seguimiento del uso de memoria (RAM y VRAM).
- Seguimiento de tokens por segundo (rendimiento).
- Seguimiento del tiempo hasta el primer token (latencia).
- Utilice el registro integrado de llama.cpp u Ollama.
---

## Limitaciones y compensaciones
- **Brecha de calidad**: los modelos locales pequeños (3.8B–7B) generalmente tienen un rendimiento inferior a los modelos de nube grandes (GPT-4, Claude 3.5) en razonamiento complejo.
- **Límite de conocimiento**: el conocimiento del modelo se congela en el momento del entrenamiento; Utilice RAG para inyectar información actual.
- **Multilingüe**: los modelos más pequeños pueden tener menos capacidad multilingüe.
- **Uso de herramientas**: los flujos de trabajo agentes (llamadas a funciones) pueden ser menos confiables en modelos pequeños.
Para muchas tareas cotidianas (resumen, preguntas y respuestas, finalización de código, clasificación), los modelos locales ya son suficientes y mejoran rápidamente.