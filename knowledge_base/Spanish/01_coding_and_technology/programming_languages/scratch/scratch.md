---
# Metadatos
título: "Rasca"
descripción: "Referencia completa para el lenguaje de programación Scratch que cubre descripción general, compensaciones, fundamentos de sintaxis, ecosistema y cuándo usarlo".
categoría: "Codificación y tecnología"
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
review_by: "Equipo de base de conocimientos de codificación y tecnología"
next_review: "2027-08-05"
# Clasificación
Etiquetas: [scratch, lenguaje-de-programación, sintaxis, ecosistema, codificación-y-tecnología]
nivel_dificultad: "principiante"
requisitos previos: []
estimado_reading_time: "29 minutos"
# Guía de contribución
contribución:
  licencia: "MIT"
  feedback_channel: "Problemas de GitHub"
  how_to_contribute: "Enviar un PR con cambios y actualizar el registro de cambios"
  review_process: "Los mantenedores de categorías revisan los cambios antes de fusionarlos"
---
# Rascar
Scratch es un lenguaje de programación visual basado en bloques desarrollado por el MIT Media Lab y lanzado por primera vez en 2007. En lugar de escribir código basado en texto, los usuarios juntan bloques de colores para crear programas. Scratch está diseñado específicamente para niños de 8 a 16 años (aunque lo usan estudiantes de todas las edades) para enseñar conceptos fundamentales de programación (bucles, condicionales, variables, eventos y funciones) sin la barrera de los errores de sintaxis.
Scratch es el lenguaje de programación introductorio más utilizado en el mundo, con más de 100 millones de usuarios registrados y disponibilidad en más de 70 idiomas. Se ejecuta en un navegador web y es gratuito.
---

## Por qué es importante el scratch
- **Mejor introducción a la programación**: elimina por completo las barreras de sintaxis. Los conceptos se enseñan mediante manipulación visual.
- **Pensamiento computacional**: Enseña descomposición, reconocimiento de patrones, abstracción y diseño de algoritmos.
- **Impulsado por la creatividad**: los niños crean juegos, animaciones, historias y música, y aprenden a programar como subproducto de la fabricación de cosas que les interesan.
- **Alcance global**: utilizado en escuelas de todo el mundo. Disponible en más de 70 idiomas. Gratis y basado en navegador.
- **Comunidad**: La comunidad en línea de Scratch enseña a compartir, mezclar y aprender colaborativamente.
## Las compensaciones
| Limitación | Detalles | Solución típica |
|-----------|-----------------|-------------------|
| **No es un lenguaje de programación "real"** | No se puede crear software, API o sistemas de producción | Transición a Python, JavaScript o lenguajes basados ​​en texto |
| **Capacidad limitada** | Sin E/S de archivos, redes ni estructuras de datos avanzadas | Úselo para aprender; pasar a idiomas de texto para proyectos reales |
| **Rendimiento** | Interpretado, lento para proyectos complejos | No diseñado para trabajos críticos para el rendimiento |
| **Percepción de edad** | A menudo visto como "sólo para niños" | Scratch es una herramienta de aprendizaje, no un lenguaje profesional |
---

## Cómo funciona Scratch
Los programas Scratch (llamados "proyectos") constan de **sprites** (personajes/objetos) que responden a **bloques** unidos en scripts.
### Conceptos básicos (enseñados a través de bloques)
| Concepto | Categoría de bloque de Scratch | Ejemplo |
|---------|----------------------|---------|
| **Secuencias** | Movimiento, Miradas | "Avanzar 10 pasos" y luego "Di hola" |
| **Bucles** | Control (amarillo) | "Repetir 10", "Para siempre", "Repetir hasta" |
| **Condicionales** | Control (amarillo) | "Si... entonces", "Si... entonces... más" |
| **Variables** | Variables (naranja) | "Establecer puntuación en 0", "Cambiar puntuación en 1" |
| **Eventos** | Eventos (amarillo) | "Cuando se hace clic en la bandera verde", "Cuando se presiona la tecla" |
| **Funciones** | Mis bloques (personalizado) | Definir secuencias de bloques reutilizables |
| **Listas (matrices)** | Variables (naranja) | "Agregar a la lista", "Elemento de la lista" |
| **Radiodifusión** | Eventos | Enviar mensajes entre sprites |
### Ejemplo: Lógica de juego simple
```
When green flag clicked:
  Set [score] to 0
  Forever:
    If <touching [enemy]?> then:
      Change [score] by -1
      Play sound [ouch]
    If <touching [coin]?> then:
      Change [score] by 1
      Go to random position
```

---

## Sintaxis y patrones avanzados
### Bloquear categorías en detalle
Scratch 3.0 organiza bloques en categorías codificadas por colores:
| Categoría | Color | Tipos de bloques |
|----------|--------|-------------|
| **Movimiento** | Azul | mover, girar, ir, deslizarse, apuntar, cambiar x/y |
| **Aspectos** | Púrpura | decir, pensar, cambiar de disfraz, cambiar de talla, mostrar/ocultar |
| **Sonido** | Rosa | reproducir sonido, detener sonidos, cambiar volumen, cambiar tono |
| **Eventos** | Amarillo | cuando se hace clic en la bandera, cuando se presiona una tecla, cuando se hace clic en el sprite, transmisión |
| **Controlar** | Oro | espera, repite, para siempre, si, si no, repite hasta, para |
| **Detección** | Azul claro | tocar, tecla presionada, mouse, distancia, preguntar/responder, cronómetro |
| **Operadores** | Verde | operaciones matemáticas, operaciones de texto, comparación y/o/no, aleatorias |
| **Variables** | Naranja | establecer/cambiar variable, enumerar operaciones |
| **Mis bloques** | Rojo oscuro | definiciones de bloques personalizados (funciones) |
### Patrones de bloques avanzados
```
// Pattern: Timer-based movement (smooth animation)
When green flag clicked:
  Set [speed] to 5
  Forever:
    Change x by (speed)
    If <(x position) > 200> then
      Set [speed] to ((speed) * -1)
    If <(x position) < -200> then
      Set [speed] to ((speed) * -1)

// Pattern: State machine using variables
When green flag clicked:
  Set [game_state] to [menu]
  Forever:
    If <(game_state) = [menu]> then
      Show
      Go to x: 0 y: 0
    If <(game_state) = [playing]> then
      Hide
    If <(game_state) = [game_over]> then
      Say [Game Over!] for 2 secs

// Pattern: Object-oriented sprite (each sprite manages its own state)
When green flag clicked:
  Set [hp] to 100
  Set [max_hp] to 100
  Set [is_alive] to true
  Forever:
    If <(is_alive) = true> then
      If <touching [enemy]?> then
        Change [hp] by -10
        If <(hp) < 1> then
          Set [is_alive] to false
          Broadcast [player_dead]
```

### Bloques personalizados (funciones)
```
// Define a custom block with parameters
Define: Jump (height) times (count)
  Repeat (count):
    Change y by (height)
    Wait 0.2 seconds
    Change y by ((height) * -1)
    Wait 0.2 seconds

// Usage:
When space key pressed:
  Jump height: 50 times: 3

// Custom block with "run without screen refresh" (optimization)
Define: Draw fractal (depth) (size)
  Run without screen refresh: true
  If <(depth) = 0> then
    Move (size) steps
  Else:
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn left 120 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
```

### Operaciones de lista (matrices)
```
// Creating and using lists
When green flag clicked:
  Delete all of [scores]
  Add [100] to [scores]
  Add [85] to [scores]
  Add [92] to [scores]
  Add [78] to [scores]
  
  // Access items (1-indexed)
  Set [total] to 0
  Set [i] to 1
  Repeat (length of [scores]):
    Change [total] by (item (i) of [scores])
    Change [i] by 1
  
  Set [average] to ((total) / (length of [scores]))
  Say (join [Average: ] (average)) for 2 secs

// Sorting a list (bubble sort)
Define: Sort List
  Set [n] to (length of [scores])
  Repeat (n)
    Set [i] to 1
    Repeat ((n) - 1)
      If <(item (i) of [scores]) > (item ((i) + 1) of [scores])> then
        // Swap
        Set [temp] to (item (i) of [scores])
        Replace item (i) of [scores] with (item ((i) + 1) of [scores])
        Replace item ((i) + 1) of [scores] with (temp)
      Change [i] by 1
```

### Radiodifusión (Comunicación entre Sprites)
```
// Sprite 1 (Player):
When space key pressed:
  Broadcast [fire_bullet]

// Sprite 2 (Bullet):
When I receive [fire_bullet]:
  Go to [Player]
  Show
  Repeat 50:
    Change y by 10
  Hide

// Sprite 3 (Enemy):
When I receive [fire_bullet]:
  If <touching [Bullet]?> then
    Change [hp] by -25
    If <(hp) < 1> then
      Broadcast [enemy_destroyed]
      Hide
```

---

## Arquitectura y diseño de sistemas
### Diseño basado en eventos
Scratch utiliza una arquitectura basada en eventos. Cada script comienza con un bloque de eventos (bloque de sombrero) y se ejecuta en respuesta a ese evento.
```
Event Types:
+-------------------------------------------+
| when [green flag] clicked    (startup)     |
| when [space] key pressed     (keyboard)    |
| when this sprite clicked     (mouse)       |
| when [backdrop] switches to  (stage event) |
| when [loudness] > [10]       (sound)       |
| when I receive [message]     (broadcast)   |
| when video motion > [10]     (camera)      |
+-------------------------------------------+
```

### Estructura del proyecto
```
scratch-project/
├── project.sb3              * Saved project file (ZIP format)
├── sprites/
│   ├── Player/              * Player sprite
│   │   ├── costumes/        * Costume images
│   │   └── sounds/          * Sound files
│   ├── Enemy/
│   │   ├── costumes/
│   │   └── sounds/
│   └── Bullet/
├── stage/
│   ├── backdrops/           * Background images
│   └── sounds/              * Stage sounds
└── README.md
```

### Sistema de clonación (creación de objetos)
```
// Creating clones (like creating object instances)
When green flag clicked:
  Forever:
    Wait 1 seconds
    Create clone of [Enemy]

When I start as a clone:
  Go to random position
  Show
  Set [hp] to 3
  Forever:
    Change y by -3
    If <(y position) < -170> then
      Delete this clone
    If <touching [Bullet]?> then
      Change [hp] by -1
      If <(hp) < 1> then
        Change [score] by 10
        Delete this clone
```

---

## Configuración del proyecto y sistema de construcción
### Extensiones Scratch
Scratch admite extensiones oficiales y comunitarias que agregan capacidades:
| Ampliación | Propósito |
|-----------|------------------|
| **Bolígrafo** | Dibuja líneas y formas en el escenario |
| **Detección de vídeo** | Utilice la cámara web para detectar movimiento |
| **Texto a voz** | Convertir texto a audio hablado |
| **Traducir** | Traducir texto entre idiomas |
| **Makey Makey** | Conecte objetos físicos como entrada |
| **micro:bit** | Conecte el hardware BBC micro:bit |
| **Tormentas mentales LEGO** | Controla robots LEGO |
| **Música** | Tocar notas e instrumentos musicales |
### Formato de archivo borrador
```
Scratch 3.0 projects (.sb3) are ZIP archives containing:
├── project.json             * All scripts, sprites, and metadata
├── [md5hash].svg           * Costume images (SVG or PNG)
├── [md5hash].png           * Additional costumes
└── [md5hash].wav           * Sound files

The project.json contains:
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "costumes": [...],
      "sounds": [...],
      "blocks": {...}
    },
    {
      "isStage": false,
      "name": "Sprite1",
      "position": {"x": 0, "y": 0},
      "blocks": {...}
    }
  ],
  "monitors": [...],
  "meta": {"semver": "3.0.0"}
}
```

### Editor sin conexión
```
Scratch Desktop (offline editor) available for:
- Windows 10+ (Microsoft Store or direct download)
- macOS 10.13+
- ChromeOS

Installation:
1. Download from https://scratch.mit.edu/download
2. Install and run — no internet required
3. Projects save as .sb3 files locally
```

---

## Pruebas y depuración
### Herramientas de depuración integradas
Scratch proporciona varias herramientas integradas para depurar proyectos:
| Herramienta | Cómo utilizar |
|------|-----------|
| **Modo tortuga** | Haga clic derecho en un objeto y seleccione "mostrar depuración" para ver las coordenadas |
| **Monitores variables** | Haga clic derecho en una variable y seleccione "mostrar" para ver su valor en tiempo real |
| **Listar monitores** | Ver el contenido de la lista en visualización normal, de fila o de columna |
| **Modo turbo** | Mantenga presionada la tecla Mayús mientras hace clic en la bandera verde para una ejecución más rápida |
| **Modo de un solo paso** | Haga clic derecho en la bandera verde para "un solo paso" (ralentiza la ejecución) |
### Patrones de depuración
```
// Debug: Display variable values on sprite
When green flag clicked:
  Forever:
    Say (join [Score: ] (score))

// Debug: Visual boundary checking
When green flag clicked:
  Forever:
    If <(x position) > 240> then
      Say [TOO FAR RIGHT!] for 0.5 secs
      Set x to 240
    If <(x position) < -240> then
      Say [TOO FAR LEFT!] for 0.5 secs
      Set x to -240

// Debug: Frame counter
When green flag clicked:
  Set [frames] to 0
  Forever:
    Change [frames] by 1
    If <(frames) mod 30 = 0> then
      Say (join [FPS: ] ((frames) / (timer))) for 0.1 secs
```

### Problemas comunes
| Problema | Causa | Solución |
|---------|-------|----------|
| Sprite no responde | Sin bloque de sombreros para eventos | Agregar "Cuando se hace clic en la bandera verde" u otro evento |
| Clon no funciona | Clon creado pero no mostrado | Agregue el bloque "Mostrar" después de "Cuando comienzo como clon" |
| Variable compartida entre sprites | Confusión de variables globales versus locales | Utilice la opción "Solo para este objeto" |
| Transmisión no recibida | Nombre de mensaje incorrecto | Verifique que los nombres de transmisión y recepción coincidan exactamente |
| Congelación de bucle infinito | "Para siempre" sin espera | Agregue pequeños bloques de "espera" en bucles cerrados |
---

## Interoperabilidad
### Extensiones de hardware
Scratch puede conectarse al hardware físico a través de extensiones:
```
Supported Hardware:
├── micro:bit
│   ├── Accelerometer/gyroscope input
│   ├── LED matrix display output
│   ├── Button input
│   └── Radio communication
├── LEGO Education
│   ├── SPIKE Prime / Essential
│   ├── EV3 (older)
│   └── Motors and sensors
├── Makey Makey
│   ├── Capacitive touch input
│   ├── Any conductive object as button
│   └── USB connection (no drivers needed)
├── Arduino (via extensions)
│   ├── GPIO pin control
│   ├── Sensor readings
│   └── Motor control
└── Camera / Webcam
    ├── Video sensing (motion detection)
    └── Face detection (via extensions)
```

### API de extensiones Scratch (extensiones personalizadas)
```javascript
// Custom Scratch extension (JavaScript)
class MyExtension {
  getInfo() {
    return {
      id: 'myExtension',
      name: 'My Extension',
      blocks: [
        {
          opcode: 'greet',
          blockType: Scratch.BlockType.REPORTER,
          text: 'greet [NAME]',
          arguments: {
            NAME: { type: Scratch.ArgumentType.STRING, defaultValue: 'World' }
          }
        },
        {
          opcode: 'addNumbers',
          blockType: Scratch.BlockType.REPORTER,
          text: '[A] + [B]',
          arguments: {
            A: { type: Scratch.ArgumentType.NUMBER, defaultValue: 1 },
            B: { type: Scratch.ArgumentType.NUMBER, defaultValue: 2 }
          }
        }
      ]
    };
  }
  greet(args) { return 'Hello, ' + args.NAME + '!'; }
  addNumbers(args) { return Number(args.A) + Number(args.B); }
}
Scratch.extensions.register(new MyExtension());
```
---

## Patrones de diseño
### Patrón 1: movimiento de plataformas
```
When green flag clicked:
  Set [gravity] to -1
  Set [velocity_y] to 0
  Set [speed] to 5
  Set [is_jumping] to false
  Forever:
    // Horizontal movement
    If <key [right arrow] pressed?> then
      Change x by (speed)
    If <key [left arrow] pressed?> then
      Change x by ((speed) * -1)
    // Jumping
    If <key [space] pressed?> then
      If <(is_jumping) = false> then
        Set [velocity_y] to 12
        Set [is_jumping] to true
    // Gravity
    Change [velocity_y] by (gravity)
    Change y by (velocity_y)
    // Ground collision
    If <(y position) < -100> then
      Set y to -100
      Set [velocity_y] to 0
      Set [is_jumping] to false
```

### Patrón 2: Fondo en desplazamiento
```
// Background sprite scrolls left to create side-scrolling effect
When green flag clicked:
  Forever:
    Change x by -5
    If <(x position) < -240> then
      Set x to 240

// Or use two copies for seamless scrolling
When I start as a clone:
  Forever:
    Change x by -5
    If <(x position) < -480> then
      Change x by 960
```

### Patrón 3: Seguimiento de Sprite (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Patrón 4: Sistema de inventario con listas
```
When green flag clicked:
  Delete all of [inventory]
  Add [Sword] to [inventory]
  Add [Shield] to [inventory]
  Add [Potion] to [inventory]

When key [i] pressed:
  // Display inventory
  Set [display] to []
  Set [idx] to 1
  Repeat (length of [inventory]):
    Set [display] to (join (display) (join (item (idx) of [inventory]) [
]))
    Change [idx] by 1
  Say (display) for 3 secs

When key [1] pressed:
  // Use first item
  If <(length of [inventory]) > 0> then
    Set [used_item] to (item 1 of [inventory])
    Delete 1 of [inventory]
    Say (join [Used: ] (used_item)) for 1 secs
```

### Patrón 5: Sistema de partículas con clones
```
// Create particles on click
When this sprite clicked:
  Repeat 10:
    Create clone of [Particle]

// Each particle moves randomly and fades
When I start as a clone:
  Go to [mouse-pointer]
  Point in direction (pick random 0 to 360)
  Set [size] to (pick random 20 to 50)
  Set [ghost] to 0
  Show
  Repeat 20:
    Move 5 steps
    Change [ghost] by 5
  Hide
  Delete this clone
```

---

## Rendimiento y optimización
### Optimización de sprites
| Técnica | Impacto | Descripción |
|-----------|--------|-------------|
| **Minimizar clones** | Alto | Cada clon consume memoria; eliminar cuando haya terminado |
| **Reducir disfraces** | Medio | Menos cambios de vestuario significan menos gastos generales de renderizado |
| **Utilice "ejecutar sin actualizar la pantalla"** | Alto | Los bloques personalizados sin actualización de pantalla se ejecutan más rápido |
| **Limitar bloques de "decir"** | Medio | Las burbujas del discurso causan sobrecarga de renderizado |
| **Evita "para siempre" en cada sprite** | Medio | Utilice retransmisiones y eventos en lugar de encuestas constantes |
### Gestión de clones
```
// BAD: Creating clones without cleanup
When green flag clicked:
  Forever:
    Create clone of [Enemy]
    Wait 0.1 secs
    // Clones pile up and slow everything down

// GOOD: Limit active clones
When green flag clicked:
  Set [max_enemies] to 10
  Forever:
    If <(enemy_count) < (max_enemies)> then
      Create clone of [Enemy]
      Change [enemy_count] by 1
    Wait 1 secs

When I start as a clone:
  // ... enemy behaviour ...
  // When done:
  Change [enemy_count] by -1
  Delete this clone
```

### Lista de verificación de optimización
| Técnica | Impacto | Descripción |
|-----------|--------|-------------|
| **Ejecutar sin actualizar la pantalla** | Muy Alto | Los bloques personalizados omiten el renderizado para aumentar la velocidad |
| **Minimizar clones activos** | Alto | Eliminar clones tan pronto como ya no sean necesarios |
| **Utilice las retransmisiones con moderación** | Medio | Demasiadas transmisiones por cuadro causan retraso |
| **Simplifica disfraces** | Medio | Las imágenes más pequeñas se procesan más rápido |
| **Reducir operaciones de lista** | Medio | Evite escanear listas grandes en cada cuadro |
| **Utilice bloques de "espera"** | Bajo | Evite el acaparamiento de la CPU en bucles eternos |
---

## Implementación y uso en el mundo real
### Compartir proyectos
```
Deployment Options:
├── Scratch Community (online)
│   ├── Upload to scratch.mit.edu
│   ├── Share with community
│   └── Allow remixing by others
├── Local sharing
│   ├── Save as .sb3 file
│   ├── Share via email/USB/cloud
│   └── Open in Scratch Desktop or web editor
├── Embedding
│   ├── Embed on websites via iframe
│   └── <iframe src="https://scratch.mit.edu/projects/embed/PROJECT_ID">
└── Standalone apps (via third-party tools)
    ├── TurboWarp (desktop packaging)
    ├── Electron-based wrappers
    └── HTML5 export tools
```

### Uso educativo en el mundo real
| Contexto | Cómo se utiliza Scratch | Escala |
|---------|-------------------|-------|
| **Escuelas K-12** | Introducción a la programación en clases de CS | Utilizado en más de 190 países |
| **Clubes de codificación** | Talleres Scratch Club / CoderDojo | Más de 3000 clubes en todo el mundo |
| **Bibliotecas** | Programas de programación extraescolar | Sistemas de bibliotecas públicas |
| **Educación en casa** | Educación en programación a su propio ritmo | Millones de estudiantes desde casa |
| **Universidad CS0** | Cursos de introducción a la informática no especializados | Programas puente universitarios |
| **Accesibilidad** | Enseñanza de programación a personas con discapacidad visual | Soporte de lector de pantalla |
| **Terapia** | Desarrollo de habilidades cognitivas y motoras | Terapia ocupacional |
### Scratch en la investigación educativa
Las investigaciones han demostrado que Scratch enseña eficazmente:
- **Pensamiento secuencial**: dividir los problemas en pasos ordenados
- **Habilidades de depuración**: encontrar y corregir errores en la lógica
- **Expresión creativa**: Combinando arte, música y programación
- **Colaboración**: remezclar y desarrollar proyectos de otros.
- **Persistencia**: Iterar en proyectos para mejorarlos
---

## Transición desde cero
Después de aprender Scratch, los siguientes pasos típicos incluyen:
| Siguiente Idioma | Por qué |
|--------------|-----|
| **Python** | Transición más natural: sintaxis legible, conceptos lógicos similares |
| **JavaScript** | Si está interesado en la web o los juegos: retroalimentación visual inmediata |
| **Lua (vía Roblox/Love2D)** | Si está interesado en el desarrollo de juegos |
| **Inventor de la aplicación** | Bloques visuales para aplicaciones de Android (mismo linaje MIT) |
| **En bloques** | Biblioteca de programación visual de Google (conceptos similares) |
### Mapeo conceptual: de Scratch a Python
| Concepto de cero | Equivalente de Python |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Llamada a función o sistema de eventos |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(¡indexado en 0!) |
| `length of [list]`| `len(list)`|
---

## Cuándo utilizar Scratch
| Escenario | ¿Por qué rascarse? Mejor alternativa |
|----------|-----------|-------------------|
| Enseñar a codificar a niños (8-16) | Diseñado específicamente para esto | — |
| Introduciendo el pensamiento computacional | Visual, sin errores de sintaxis | — |
| Talleres escolares / clubes de codificación | Gratis, basado en navegador, sin configuración | — |
| Creación visual de prototipos de ideas de juegos | Iteración rápida | — |
| Desarrollo profesional | No diseñado para esto | Python, JavaScript, cualquier lenguaje de texto |
| Educación en informática a nivel universitario | Demasiado simple | Python, Java, C |
---

## Resumen
Scratch no es un lenguaje de programación en el sentido tradicional: es un entorno de aprendizaje. Su genialidad es eliminar todas las barreras entre un niño y el placer de crear algo interactivo. Al centrarse en conceptos en lugar de sintaxis, Scratch enseña los fundamentos de la programación que se transfieren a cualquier lenguaje. Para presentar la programación a estudiantes jóvenes, Scratch es el estándar de oro.