<!--
---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [scratch, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Graffio
Scratch è un linguaggio di programmazione visivo basato su blocchi sviluppato dal MIT Media Lab e rilasciato per la prima volta nel 2007. Invece di scrivere codice basato su testo, gli utenti uniscono blocchi colorati per creare programmi. Scratch è progettato specificamente per i bambini dagli 8 ai 16 anni (anche se gli studenti di tutte le età lo utilizzano) per insegnare i concetti fondamentali della programmazione (loop, condizionali, variabili, eventi e funzioni) senza la barriera degli errori di sintassi.
Scratch è il linguaggio di programmazione introduttivo più utilizzato al mondo, con oltre 100 milioni di utenti registrati e disponibilità in oltre 70 lingue. Funziona in un browser web ed è gratuito.
---

## Perché Scratch è importante
- **La migliore introduzione alla programmazione**: rimuove completamente le barriere sintattiche. I concetti vengono insegnati attraverso la manipolazione visiva.
- **Pensiero computazionale**: insegna la scomposizione, il riconoscimento di modelli, l'astrazione e la progettazione di algoritmi.
- **Orientati alla creatività**: i bambini creano giochi, animazioni, storie e musica, imparando la programmazione come sottoprodotto della creazione di cose a cui tengono.
- **Portata globale**: utilizzato nelle scuole di tutto il mondo. Disponibile in oltre 70 lingue. Gratuito e basato su browser.
- **Comunità**: la comunità online di Scratch insegna condivisione, remix e apprendimento collaborativo.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Non è un linguaggio di programmazione "reale"** | Impossibile creare software, API o sistemi di produzione | Transizione a Python, JavaScript o linguaggi basati su testo |
| **Funzionalità limitate** | Nessun I/O di file, rete o strutture dati avanzate | Utilizzare per l'apprendimento; passare ai linguaggi di testo per progetti reali |
| **Prestazioni** | Interpretato, lento per progetti complessi | Non progettato per lavori critici in termini di prestazioni |
| **Percezione dell'età** | Spesso visto come "solo per bambini" | Scratch è uno strumento di apprendimento, non un linguaggio professionale |
---

## Come funziona Scratch
I programmi Scratch (chiamati "progetti") sono costituiti da **sprite** (caratteri/oggetti) che rispondono a **blocchi** uniti insieme negli script.
### Concetti fondamentali (insegnati attraverso i blocchi)
| Concetto | Categoria Blocco da grattare | Esempio |
|---------|----------------------|---------|
| **Sequenze** | Movimento, sguardi | "Muovi 10 passi" poi "Saluta" |
| **Loop** | Controllo (giallo) | "Ripeti 10", "Per sempre", "Ripeti fino a" |
| **Condizionali** | Controllo (giallo) | "Se... allora", "Se... allora... altro" |
| **Variabili** | Variabili (arancione) | "Imposta punteggio a 0", "Cambia punteggio di 1" |
| **Eventi** | Eventi (giallo) | "Quando si fa clic sulla bandiera verde", "Quando si preme il tasto" |
| **Funzioni** | I miei blocchi (personalizzati) | Definire sequenze di blocchi riutilizzabili |
| **Liste (array)** | Variabili (arancione) | "Aggiungi alla lista", "Voce della lista" |
| **Trasmissione** | Eventi | Invia messaggi tra sprite |
### Esempio: logica di gioco semplice
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

## Sintassi e modelli avanzati
### Categorie di blocco in dettaglio
Scratch 3.0 organizza i blocchi in categorie codificate a colori:
| Categoria | Colore | Tipi di blocco |
|----------|--------|-----|
| **Movimento** | Blu | muoviti, gira, vai a, plana, punta, cambia x/y |
| **Sembra** | Viola | dì, pensa, cambia costume, cambia taglia, mostra/nascondi |
| **Suono** | Rosa | riproduci suono, interrompi suoni, cambia volume, cambia tono |
| **Eventi** | Giallo | quando si fa clic sulla bandiera, quando si preme un tasto, quando si fa clic sullo sprite, si trasmette |
| **Controllo** | Oro | aspetta, ripeti, per sempre, se, if-else, ripeti finché, ferma |
| **Rilevamento** | Azzurro | tocco, tasto premuto, mouse, distanza, domanda/risposta, timer |
| **Operatori** | Verde | operazioni di matematica, operazioni di testo, confronto e/o/non casuale |
| **Variabili** | Arancione | imposta/modifica variabile, operazioni di lista |
| **I miei blocchi** | Rosso scuro | definizioni di blocco personalizzate (funzioni) |
### Schemi di blocco avanzati
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

### Blocchi personalizzati (funzioni)
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

### Operazioni sugli elenchi (array)
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

### Trasmissione (comunicazione tra Sprite)
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

## Architettura e progettazione di sistemi
### Progettazione guidata dagli eventi
Scratch utilizza un'architettura guidata dagli eventi. Ogni script inizia con un blocco evento (blocco hat) e viene eseguito in risposta a quell'evento.
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

### Struttura del progetto
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

### Sistema clone (creazione di oggetti)
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

## Configurazione del progetto e sistema di creazione
### Estensioni Scratch
Scratch supporta estensioni ufficiali e della community che aggiungono funzionalità:
| Estensione | Scopo |
|-----------|---------|
| **Penna** | Disegna linee e forme sul palco |
| **Rilevamento video** | Utilizza la webcam per il rilevamento del movimento |
| **Sintesi vocale** | Converti testo in audio parlato |
| **Traduci** | Tradurre il testo tra le lingue |
| **Makey Makey** | Connetti oggetti fisici come input |
| **micro:bit** | Collega l'hardware BBC micro:bit |
| **LEGO Mindstorms** | Controlla i robot LEGO |
| **Musica** | Suonare note e strumenti musicali |
### Formato file zero
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

### Editor offline
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

## Test e debug
### Strumenti di debug integrati
Scratch fornisce diversi strumenti integrati per il debug dei progetti:
| Strumento | Come usare |
|------|-----------|
| **Modalità Tartaruga** | Fare clic con il tasto destro su uno sprite e selezionare "mostra debug" per vedere le coordinate |
| **Monitor variabili** | Fare clic con il tasto destro su una variabile e selezionare "mostra" per vederne il valore in tempo reale |
| **Elenco monitor** | Visualizza il contenuto dell'elenco nella visualizzazione normale, di riga o di colonna |
| **Modalità Turbo** | Tieni premuto Maiusc mentre fai clic sulla bandiera verde per un'esecuzione più rapida |
| **Modalità passo singolo** | Fare clic con il pulsante destro del mouse sulla bandierina verde per "passaggio singolo" (rallenta l'esecuzione) |
### Modelli di debug
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

### Problemi comuni
| Problema | Causa | Soluzione |
|---------|-------|----------|
| Lo sprite non risponde | Nessun blocco cappello evento | Aggiungi "Quando si fa clic sulla bandiera verde" o altro evento |
| La clonazione non funziona | Clone creato ma non mostrato | Aggiungi il blocco "Mostra" dopo "Quando avvio come clone" |
| Variabile condivisa tra sprite | Confusione tra variabili globali e locali | Usa l'opzione "Solo per questo sprite" |
| Trasmissione non ricevuta | Nome messaggio errato | Verificare che i nomi di trasmissione e ricezione corrispondano esattamente |
| Blocco del ciclo infinito | "Per sempre" senza aspettare | Aggiungi piccoli blocchi "Aspetta" in cicli stretti |
---

## Interoperabilità
### Estensioni hardware
Scratch può connettersi all'hardware fisico tramite estensioni:
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

### API delle estensioni Scratch (estensioni personalizzate)
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

## Modelli di progettazione
### Modello 1: movimento platform
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

### Motivo 2: sfondo scorrevole
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

### Schema 3: Inseguimento dello Sprite (Inseguimento dell'IA)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Modello 4: Sistema di inventario con elenchi
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

### Modello 5: Sistema di particelle con cloni
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

## Prestazioni e ottimizzazione
### Ottimizzazione degli sprite
| Tecnica | Impatto | Descrizione |
|-----------|--------|-----|
| **Riduci al minimo i cloni** | Alto | Ogni clone consuma memoria; elimina al termine |
| **Riduci i costumi** | Medio | Meno cambi di costume significano meno spese di rendering |
| **Utilizza "esegui senza aggiornamento dello schermo"** | Alto | I blocchi personalizzati senza aggiornamento dello schermo vengono eseguiti più velocemente |
| **Limita i blocchi "dire"** | Medio | I fumetti causano un sovraccarico del rendering |
| **Evita "per sempre" in ogni sprite** | Medio | Utilizza trasmissioni ed eventi invece del polling costante |
### Gestione dei cloni
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

### Elenco di controllo per l'ottimizzazione
| Tecnica | Impatto | Descrizione |
|-----------|--------|-----|
| **Esegui senza aggiornamento dello schermo** | Molto alto | I blocchi personalizzati saltano il rendering per velocità |
| **Riduci al minimo i cloni attivi** | Alto | Elimina i cloni non appena non sono più necessari |
| **Utilizzare le trasmissioni con parsimonia** | Medio | Troppe trasmissioni per frame causano ritardi |
| **Semplifica i costumi** | Medio | Le immagini più piccole vengono visualizzate più velocemente |
| **Riduci le operazioni sull'elenco** | Medio | Evitare la scansione di elenchi di grandi dimensioni a ogni fotogramma |
| **Usa i blocchi "wait"** | Basso | Impedisci il blocco della CPU in cicli eterni |
---

## Distribuzione e utilizzo nel mondo reale
### Condivisione di progetti
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

### Utilizzo educativo nel mondo reale
| Contesto | Come viene utilizzato Scratch | Scala |
|---------|-----|-------|
| **Scuole K-12** | Introduzione alla programmazione nelle classi CS | Utilizzato in oltre 190 paesi |
| **Club di codifica** | Workshop Scratch Club / CoderDojo | Oltre 3000 club in tutto il mondo |
| **Biblioteche** | Programmi di programmazione doposcuola | Sistemi bibliotecari pubblici |
| **Istruzione domiciliare** | Educazione alla programmazione autodidattica | Milioni di studenti a casa |
| **Università CS0** | Corsi introduttivi di informatica non importanti | Programmi ponte universitari |
| **Accessibilità** | Insegnare la programmazione ai non vedenti | Supporto per la lettura dello schermo |
| **Terapia** | Sviluppo delle abilità cognitive e motorie | Terapia occupazionale |
### Scratch nella ricerca educativa
La ricerca ha dimostrato che Scratch insegna efficacemente:
- **Pensiero sequenziale**: suddividere i problemi in passaggi ordinati
- **Capacità di debug**: ricerca e correzione di errori nella logica
- **Espressione creativa**: combinazione di arte, musica e programmazione
- **Collaborazione**: remixare e sviluppare progetti di altri
- **Persistenza**: iterazione sui progetti per migliorarli
---

## Transizione da zero
Dopo aver appreso Scratch, i passaggi successivi tipici includono:
| Lingua successiva | Perché |
|--------------|-----|
| **Pitone** | Transizione più naturale: sintassi leggibile, concetti logici simili |
| **JavaScript** | Se interessato al web/ai giochi: feedback visivo immediato |
| **Lua (tramite Roblox/Love2D)** | Se interessato allo sviluppo di giochi |
| **Inventore di app** | Blocchi visivi per app Android (stesso lignaggio MIT) |
| **Bloccato** | Libreria di programmazione visiva di Google (concetti simili) |
### Mappatura concettuale: da Scratch a Python
| Concetto di graffio | Equivalente in Python |
|-----------------|-----|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Chiamata di funzione o sistema di eventi |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(indicizzato a 0!) |
| `length of [list]`| `len(list)`|
---

## Quando utilizzare Scratch
| Scenario | Perché graffiare | Alternativa migliore |
|----------|-----------|-------------|
| Insegnare ai bambini (8-16 anni) a programmare | Progettato appositamente per questo | — |
| Introduzione al pensiero computazionale | Visivo, nessun errore di sintassi | — |
| Laboratori scolastici/club di codifica | Gratuito, basato su browser, nessuna configurazione | — |
| Prototipazione visiva di idee di gioco | Iterazione veloce | — |
| Sviluppo professionale | Non progettato per questo | Python, JavaScript, qualsiasi linguaggio testuale |
| Formazione informatica a livello universitario | Troppo semplice | Python, Java, C |
---

## Domande e risposte sintetiche
**Q1: Scratch è davvero un linguaggio di programmazione?**
A1: Sì, Scratch è un vero linguaggio di programmazione, ma è visivo anziché testuale. Supporta tutti i concetti fondamentali della programmazione: variabili, cicli, condizionali, funzioni (blocchi personalizzati), elenchi e programmazione guidata dagli eventi. La differenza è che trascini e rilascia i blocchi invece di digitare il codice. Ciò elimina gli errori di sintassi e rende la programmazione accessibile ai giovani studenti.
**Q2: Come posso creare funzioni personalizzate (blocchi personalizzati) in Scratch?**
R2: Vai alla categoria "I miei blocchi" e fai clic su "Crea un blocco". Dagli un nome, aggiungi parametri se necessario, quindi definisci il suo comportamento aggiungendo blocchi sottostanti. I blocchi personalizzati possono accettare input (numeri, stringhe, booleani) e possono chiamare altri blocchi personalizzati. Ciò consente la programmazione modulare e il riutilizzo del codice.
**Q3: Qual è il modo migliore per gestire la logica di gioco complessa in Scratch?**
R3: Utilizza blocchi personalizzati per organizzare la logica, trasmetti messaggi per il coordinamento degli eventi tra sprite e utilizza elenchi per memorizzare lo stato del gioco (punteggi, livelli, inventario). Per l'intelligenza artificiale complessa, utilizzare macchine a stati finiti con variabili che tracciano lo stato corrente. Clona gli sprite per più nemici e usa "quando inizio come clone" per dare a ciascuno un comportamento indipendente.
**Q4: Come posso condividere i dati tra gli sprite in Scratch?**
R4: Utilizza variabili globali (create senza "solo per questo sprite") per dati condivisi come punteggio o stato del gioco. Utilizza i messaggi trasmessi per attivare eventi tra gli sprite. Per comunicazioni più complesse, utilizzare gli elenchi come strutture dati condivise. Ogni sprite può leggere e modificare variabili ed elenchi globali, consentendo il coordinamento.
**Q5: Quali sono alcune tecniche avanzate in Scratch?**
A5: utilizzare i blocchi penna per disegnare e creare effetti visivi. Implementa il raycasting per una grafica simile al 3D. Utilizza variabili cloud per giochi multiplayer (richiede lo stato Scratcher). Crea una generazione procedurale con numeri ed elenchi casuali. Utilizza blocchi personalizzati con parametri per algoritmi riutilizzabili. Sperimenta il rilevamento video e la manipolazione del suono per progetti interattivi.
---

## Catena di pensieri
### Problema 1: creare un gioco platform
**Passaggio 1: comprendere il problema**
Dobbiamo creare un platform in cui un personaggio possa muoversi a sinistra/destra, saltare, evitare ostacoli e raccogliere oggetti.
**Passaggio 2: identificare l'approccio**
- Utilizzare la simulazione della gravità con una variabile "in caduta".
- Rileva terreno/collisione utilizzando il colore o il tocco dello sprite
- Memorizza i dati di livello negli elenchi
- Utilizza blocchi personalizzati per la logica del salto e del movimento
**Passaggio 3: implementa la soluzione**```scratch
// Gravity and movement
when green flag clicked
forever
  change y by (y velocity)
  if touching color [brown] then
    set [y velocity v] to [0]
    set [is jumping v] to [0]
  else
    change [y velocity v] by (-1)
  end
  
  if key [right arrow v] pressed then
    change x by (5)
  end
  if key [left arrow v] pressed then
    change x by (-5)
  end
  if key [space v] pressed and not <is jumping = [1]> then
    set [y velocity v] to [10]
    set [is jumping v] to [1]
  end
end
```

**Passaggio 4: verifica e ottimizza**
Prova a saltare su diverse piattaforme. Regola la gravità e l'altezza del salto per una buona sensazione di gioco. Aggiungi animazioni per correre e saltare. Implementare checkpoint utilizzando messaggi broadcast.
---

### Problema 2: creazione di un gioco a quiz con monitoraggio del punteggio
**Passaggio 1: comprendere il problema**
Costruisci un gioco a quiz che pone domande, controlla le risposte e tiene traccia del punteggio del giocatore.
**Passaggio 2: identificare l'approccio**
- Memorizza domande e risposte in elenchi paralleli
- Utilizza un contatore di domande per monitorare i progressi
- Utilizzare i blocchi "chiedi e attendi" per l'input
- Confronta le risposte e aggiorna il punteggio
**Passaggio 3: implementa la soluzione**```scratch
when green flag clicked
set [score v] to [0]
set [question number v] to [1]

repeat (length of [questions v])
  ask (item (question number) of [questions v]) and wait
  if <(answer) = (item (question number) of [answers v])> then
    change [score v] by (1)
    say [Correct!] for (2) secs
  else
    say [Wrong!] for (2) secs
  end
  change [question number v] by (1)
end

say (join [Final score: ] join (score) [/5]) for (4) secs
```

**Passaggio 4: verifica e ottimizza**
Test con varie risposte inclusi casi limite. Aggiungi feedback per le risposte sbagliate. Implementare un'opzione di riprova. Aggiungi effetti sonori e feedback visivo per le risposte corrette/sbagliate.
---

### Problema 3: disegnare alberi frattali con la penna
**Passaggio 1: comprendere il problema**
Crea un albero frattale ricorsivo utilizzando l'estensione penna.
**Passaggio 2: identificare l'approccio**
- Usa la ricorsione per disegnare rami
- Ogni ramo si divide in due rami più piccoli
- Usa angoli casuali per variazioni naturali
- Tieni traccia della lunghezza del ramo e diminuisci con ogni livello di ricorsione
**Passaggio 3: implementa la soluzione**```scratch
define draw branch (length)
pen down
glide (1) secs to (x:(x position) + (length * cos of direction)) (y:(y position) + (length * sin of direction))
pen up

if <(length) > [5]> then
  turn right (pick random (10) to (45))
  draw branch (length * 0.7)
  turn left (pick random (20) to (90))
  draw branch (length * 0.7)
end

when green flag clicked
erase all
goto x:(0) y:(-150)
point in direction (90)
draw branch (100)
```

**Passaggio 4: verifica e ottimizza**
Regola la soglia della lunghezza del ramo e gli intervalli di angolazione per alberi estetici. Aggiungi foglie alle punte dei rami usando i cambi di colore. Implementa diversi stili di albero. Salva i disegni come immagini.
---

## Riepilogo
Scratch non è un linguaggio di programmazione nel senso tradizionale: è un ambiente di apprendimento. La sua genialità sta nell'abbattere ogni barriera tra un bambino e la gioia di creare qualcosa di interattivo. Concentrandosi sui concetti piuttosto che sulla sintassi, Scratch insegna i fondamenti della programmazione che possono essere trasferiti a qualsiasi linguaggio. Per introdurre la programmazione ai giovani studenti, Scratch è lo standard di riferimento.