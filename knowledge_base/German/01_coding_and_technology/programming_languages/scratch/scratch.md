---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
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
# Kratzen
Scratch ist eine visuelle, blockbasierte Programmiersprache, die vom MIT Media Lab entwickelt und erstmals 2007 veröffentlicht wurde. Anstatt textbasierten Code zu schreiben, fügen Benutzer farbige Blöcke zusammen, um Programme zu erstellen. Scratch wurde speziell für Kinder im Alter von 8 bis 16 Jahren entwickelt (obwohl es von Lernenden jeden Alters verwendet wird), um grundlegende Programmierkonzepte – Schleifen, Bedingungen, Variablen, Ereignisse und Funktionen – ohne die Hürde von Syntaxfehlern zu vermitteln.
Scratch ist mit über 100 Millionen registrierten Benutzern und einer Verfügbarkeit in über 70 Sprachen die am weitesten verbreitete Einführungsprogrammiersprache der Welt. Es läuft in einem Webbrowser und ist kostenlos.
---

## Warum Kratzer wichtig sind
- **Beste Einführung in die Programmierung**: Entfernt Syntaxbarrieren vollständig. Konzepte werden durch visuelle Manipulation vermittelt.
- **Computergestütztes Denken**: Lehrt Zerlegung, Mustererkennung, Abstraktion und Algorithmusdesign.
- **Kreativitätsorientiert**: Kinder erstellen Spiele, Animationen, Geschichten und Musik – das Erlernen des Programmierens ist ein Nebenprodukt bei der Herstellung von Dingen, die ihnen wichtig sind.
- **Globale Reichweite**: Wird in Schulen weltweit verwendet. Verfügbar in über 70 Sprachen. Kostenlos und browserbasiert.
- **Community**: Die Scratch-Online-Community lehrt Teilen, Remixen und kollaboratives Lernen.
## Die Kompromisse
| Einschränkung | Einzelheiten | Typische Problemumgehung |
|-----------|---------|-----|
| **Keine „echte“ Programmiersprache** | Produktionssoftware, APIs oder Systeme können nicht erstellt werden | Übergang zu Python, JavaScript oder textbasierten Sprachen |
| **Eingeschränkte Möglichkeiten** | Keine Datei-E/A, kein Netzwerk oder keine erweiterten Datenstrukturen | Zum Lernen verwenden; Umstellung auf Textsprachen für reale Projekte |
| **Leistung** | Interpretiert, langsam für komplexe Projekte | Nicht für leistungskritische Arbeiten konzipiert |
| **Alterswahrnehmung** | Wird oft als „nur für Kinder“ angesehen | Scratch ist ein Lernwerkzeug, keine professionelle Sprache |
---

## So funktioniert Scratch
Scratch-Programme (genannt „Projekte“) bestehen aus **Sprites** (Zeichen/Objekten), die auf in Skripten zusammengefügte **Blöcke** reagieren.
### Kernkonzepte (durch Blöcke vermittelt)
| Konzept | Scratch-Block-Kategorie | Beispiel |
|---------|-------|---------|
| **Sequenzen** | Bewegung, Aussehen | „10 Schritte bewegen“ und dann „Hallo sagen“ |
| **Schleifen** | Kontrolle (gelb) | „10 wiederholen“, „Für immer“, „Wiederholen bis“ |
| **Bedingungen** | Kontrolle (gelb) | „Wenn… dann“, „Wenn… dann… sonst“ |
| **Variablen** | Variablen (orange) | „Punktzahl auf 0 setzen“, „Punktzahl um 1 ändern“ |
| **Veranstaltungen** | Ereignisse (gelb) | „Beim Klicken auf die grüne Flagge“, „Beim Drücken der Taste“ |
| **Funktionen** | Meine Blöcke (benutzerdefiniert) | Definieren Sie wiederverwendbare Blocksequenzen |
| **Listen (Arrays)** | Variablen (orange) | „Zur Liste hinzufügen“, „Element der Liste“ |
| **Rundfunk** | Veranstaltungen | Nachrichten zwischen Sprites senden |
### Beispiel: Einfache Spiellogik
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

## Erweiterte Syntax und Muster
### Blockkategorien im Detail
Scratch 3.0 organisiert Blöcke in farbcodierte Kategorien:
| Kategorie | Farbe | Blocktypen |
|----------|--------|-------------|
| **Antrag** | Blau | bewegen, drehen, gehen, gleiten, zeigen, x/y ändern |
| **Sieht aus** | Lila | sagen, denken, Kostüm wechseln, Größe ändern, ein-/ausblenden |
| **Ton** | Rosa | Ton abspielen, Töne stoppen, Lautstärke ändern, Tonhöhe ändern |
| **Veranstaltungen** | Gelb | Wenn die Flagge angeklickt wird, wenn die Taste gedrückt wird, wenn das Sprite angeklickt wird, wird gesendet |
| **Kontrolle** | Gold | warten, wiederholen, für immer, wenn, wenn-sonst, wiederholen bis, stoppen |
| **Erkennung** | Hellblau | Berühren, Tastendruck, Maus, Entfernung, Fragen/Antworten, Timer |
| **Operatoren** | Grün | Mathe-Operationen, Text-Operationen, Vergleich und/oder/nicht, zufällig |
| **Variablen** | Orange | Variable setzen/ändern, Operationen auflisten |
| **Meine Blöcke** | Dunkelrot | benutzerdefinierte Blockdefinitionen (Funktionen) |
### Erweiterte Blockmuster
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

### Benutzerdefinierte Blöcke (Funktionen)
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

### Listenoperationen (Arrays)
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

### Rundfunk (Inter-Sprite-Kommunikation)
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

## Architektur und Systemdesign
### Ereignisgesteuertes Design
Scratch verwendet eine ereignisgesteuerte Architektur. Jedes Skript beginnt mit einem Ereignisblock (Hat-Block) und wird als Reaktion auf dieses Ereignis ausgeführt.
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

### Projektstruktur
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

### System klonen (Objekterstellung)
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

## Projektkonfiguration und Build-System
### Scratch-Erweiterungen
Scratch unterstützt offizielle und Community-Erweiterungen, die zusätzliche Funktionen bieten:
| Erweiterung | Zweck |
|-----------|---------|
| **Stift** | Zeichnen Sie Linien und Formen auf der Bühne |
| **Videoerkennung** | Webcam zur Bewegungserkennung nutzen |
| **Text-to-Speech** | Text in gesprochenes Audio umwandeln |
| **Übersetzen** | Text zwischen Sprachen übersetzen |
| **Makey Makey** | Physische Objekte als Eingabe verbinden |
| **micro:bit** | BBC micro:bit-Hardware anschließen |
| **LEGO Mindstorms** | Steuern Sie LEGO-Roboter |
| **Musik** | Noten und Instrumente spielen |
### Scratch-Dateiformat
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

### Offline-Editor
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

## Testen und Debuggen
### Integrierte Debugging-Tools
Scratch bietet mehrere integrierte Tools zum Debuggen von Projekten:
| Werkzeug | Verwendung |
|------|-----------|
| **Schildkrötenmodus** | Klicken Sie mit der rechten Maustaste auf ein Sprite und wählen Sie „Debug anzeigen“, um die Koordinaten anzuzeigen |
| **Variable Monitore** | Klicken Sie mit der rechten Maustaste auf eine Variable und wählen Sie „Anzeigen“, um ihren Wert in Echtzeit anzuzeigen |
| **Monitore auflisten** | Listeninhalte in normaler, Zeilen- oder Spaltenanzeige anzeigen |
| **Turbomodus** | Halten Sie die Umschalttaste gedrückt, während Sie auf die grüne Flagge klicken, um die Ausführung zu beschleunigen |
| **Einzelschrittmodus** | Klicken Sie mit der rechten Maustaste auf die grüne Flagge für „Einzelschritt“ (verlangsamt die Ausführung) |
### Debugging-Muster
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

### Häufige Probleme
| Problem | Ursache | Lösung |
|---------|-------|----------|
| Sprite antwortet nicht | Kein Event-Hat-Block | „Wenn die grüne Flagge angeklickt wurde“ oder ein anderes Ereignis hinzufügen |
| Klon funktioniert nicht | Klon erstellt, aber nicht angezeigt | Fügen Sie den Block „Anzeigen“ nach „Wenn ich als Klon starte“ hinzu |
| Von Sprites gemeinsam genutzte Variable | Verwirrung zwischen globalen und lokalen Variablen | Verwenden Sie die Option „Nur für dieses Sprite“ |
| Sendung nicht empfangen | Falscher Nachrichtenname | Überprüfen Sie, ob Broadcast- und Empfangsnamen genau übereinstimmen |
| Endlosschleife einfrieren | „Für immer“ ohne Wartezeit | Fügen Sie kleine „Wait“-Blöcke in engen Schleifen hinzu |
---

## Interoperabilität
### Hardware-Erweiterungen
Scratch kann über Erweiterungen eine Verbindung zu physischer Hardware herstellen:
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

### Scratch Extensions API (benutzerdefinierte Erweiterungen)
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

## Designmuster
### Muster 1: Platformer-Bewegung
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

### Muster 2: Scrollender Hintergrund
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

### Muster 3: Sprite-Verfolgung (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Muster 4: Inventarsystem mit Listen
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

### Muster 5: Partikelsystem mit Klonen
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

## Leistung und Optimierung
### Sprite-Optimierung
| Technik | Auswirkungen | Beschreibung |
|-----------|--------|-------------|
| **Klone minimieren** | Hoch | Jeder Klon verbraucht Speicher; löschen, wenn fertig |
| **Kostüme reduzieren** | Mittel | Weniger Kostümwechsel bedeuten weniger Rendering-Overhead |
| **Verwenden Sie „Ohne Bildschirmaktualisierung ausführen“** | Hoch | Benutzerdefinierte Blöcke ohne Bildschirmaktualisierung werden schneller ausgeführt |
| **„Sagen“-Blöcke begrenzen** | Mittel | Sprechblasen verursachen Rendering-Aufwand |
| **Vermeiden Sie „für immer“ in jedem Sprite** | Mittel | Nutzen Sie Broadcasts und Events statt ständigem Polling |
### Klonverwaltung
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

### Optimierungs-Checkliste
| Technik | Auswirkungen | Beschreibung |
|-----------|--------|-------------|
| **Ohne Bildschirmaktualisierung ausführen** | Sehr hoch | Benutzerdefinierte Blöcke überspringen das Rendern aus Geschwindigkeitsgründen |
| **Aktive Klone minimieren** | Hoch | Klone löschen, sobald sie nicht mehr benötigt werden |
| **Gehen Sie mit Sendungen sparsam um** | Mittel | Zu viele Übertragungen pro Frame führen zu Verzögerungen |
| **Kostüme vereinfachen** | Mittel | Kleinere Bilder werden schneller gerendert |
| **Listenoperationen reduzieren** | Mittel | Vermeiden Sie es, bei jedem Frame große Listen zu scannen |
| **Verwenden Sie „Warte“-Blöcke** | Niedrig | Verhindern Sie, dass die CPU in Endlosschleifen überlastet wird |
---

## Bereitstellung und reale Nutzung
### Projekte teilen
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

### Praktische Nutzung im Bildungsbereich
| Kontext | Wie Scratch verwendet wird | Maßstab |
|---------|-----|-------|
| **K-12-Schulen** | Einführung in die Programmierung im CS-Unterricht | Wird in über 190 Ländern verwendet |
| **Codierungsclubs** | Scratch Club / CoderDojo-Workshops | Über 3000 Clubs weltweit |
| **Bibliotheken** | Außerschulische Programmierprogramme | Öffentliche Bibliothekssysteme |
| **Homeschooling** | Selbstgesteuerte Programmierausbildung | Millionen von Heimlernern |
| **Universität CS0** | Nicht-Hauptfach-Einführungskurse in Informatik | Hochschulbrückenprogramme |
| **Barrierefreiheit** | Programmierunterricht für Sehbehinderte | Unterstützung für Bildschirmleseprogramme |
| **Therapie** | Entwicklung kognitiver und motorischer Fähigkeiten | Ergotherapie |
### Kratzer in der Bildungsforschung
Untersuchungen haben gezeigt, dass Scratch Folgendes effektiv lehrt:
- **Sequentielles Denken**: Probleme in geordnete Schritte aufteilen
- **Debugging-Fähigkeiten**: Fehler in der Logik finden und beheben
- **Kreativer Ausdruck**: Kombination von Kunst, Musik und Programmierung
- **Zusammenarbeit**: Projekte anderer remixen und darauf aufbauen
- **Beharrlichkeit**: Projekte iterieren, um sie zu verbessern
---

## Übergang von Grund auf
Zu den typischen nächsten Schritten nach dem Erlernen von Scratch gehören:
| Nächste Sprache | Warum |
|--------------|-----|
| **Python** | Natürlichster Übergang – lesbare Syntax, ähnliche Logikkonzepte |
| **JavaScript** | Bei Interesse an Web/Spielen – sofortiges visuelles Feedback |
| **Lua (über Roblox/Love2D)** | Bei Interesse an Spieleentwicklung |
| **App-Erfinder** | Visuelle Blöcke für Android-Apps (gleiche MIT-Abstammung) |
| **Blockly** | Googles visuelle Programmierbibliothek (ähnliche Konzepte) |
### Konzeptzuordnung: Scratch zu Python
| Scratch-Konzept | Python-Äquivalent |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Funktionsaufruf oder Ereignissystem |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-indiziert!) |
| `length of [list]`| `len(list)`|
---

## Wann man Scratch verwenden sollte
| Szenario | Warum Scratch | Bessere Alternative |
|----------|-----------|-------------------|
| Kindern (8-16) das Programmieren beibringen | Speziell für diesen Zweck entwickelt | — |
| Einführung in rechnergestütztes Denken | Visuell, keine Syntaxfehler | — |
| Schulworkshops / Programmierclubs | Kostenlos, browserbasiert, kein Setup | — |
| Spielideen visuell prototypisieren | Schnelle Iteration | — |
| Berufliche Entwicklung | Nicht dafür ausgelegt | Python, JavaScript, jede Textsprache |
| CS-Ausbildung auf Universitätsniveau | Zu einfach | Python, Java, C |
---

## Zusammenfassung
Scratch ist keine Programmiersprache im herkömmlichen Sinne – es ist eine Lernumgebung. Seine Genialität besteht darin, jede Barriere zwischen einem Kind und der Freude, etwas Interaktives zu schaffen, zu beseitigen. Durch die Konzentration auf Konzepte statt auf Syntax vermittelt Scratch die Grundlagen der Programmierung, die auf jede Sprache übertragen werden können. Für den Einstieg in das Programmieren für junge Lernende ist Scratch der Goldstandard.