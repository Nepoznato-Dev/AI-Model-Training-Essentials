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
# scratch
Ang Scratch ay isang visual, block-based na programming language na binuo ng MIT Media Lab at unang inilabas noong 2007. Sa halip na magsulat ng text-based na code, ang mga user ay magkakabit ng mga color block upang lumikha ng mga programa. Ang Scratch ay partikular na idinisenyo para sa mga batang edad 8-16 (bagaman ginagamit ito ng mga nag-aaral sa lahat ng edad) upang magturo ng mga pangunahing konsepto ng programming — mga loop, conditional, variable, kaganapan, at function — nang walang hadlang ng mga error sa syntax.
Ang Scratch ay ang pinakamalawak na ginagamit na panimulang programming language sa mundo, na may mahigit 100 milyong rehistradong user at availability sa 70+ na wika. Gumagana ito sa isang web browser at libre.
---

## Bakit Mahalaga ang scratch
- **Pinakamahusay na panimula sa programming**: Ganap na nag-aalis ng mga hadlang sa syntax. Itinuturo ang mga konsepto sa pamamagitan ng visual manipulation.
- **Computational thinking**: Nagtuturo ng decomposition, pattern recognition, abstraction, at algorithm na disenyo.
- **Creativity-driven**: Gumagawa ang mga bata ng mga laro, animation, kwento, at musika — pag-aaral ng programming bilang isang byproduct ng paggawa ng mga bagay na mahalaga sa kanila.
- **Global reach**: Ginagamit sa mga paaralan sa buong mundo. Available sa 70+ na wika. Libre at nakabatay sa browser.
- **Komunidad**: Ang Scratch online na komunidad ay nagtuturo ng pagbabahagi, remixing, at collaborative na pag-aaral.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Hindi isang "totoong" programming language** | Hindi makabuo ng production software, API, o system | Transition sa Python, JavaScript, o text-based na mga wika |
| **Mga limitadong kakayahan** | Walang file I/O, networking, o advanced na istruktura ng data | Gamitin para sa pag-aaral; lumipat sa mga text na wika para sa mga totoong proyekto |
| **Pagganap** | Binigyang-kahulugan, mabagal para sa mga kumplikadong proyekto | Hindi idinisenyo para sa gawaing kritikal sa pagganap |
| **Pagdama sa edad** | Madalas na nakikita bilang "para lamang sa mga bata" | Ang scratch ay isang tool sa pag-aaral, hindi isang propesyonal na wika |
---

## Paano Gumagana ang Scratch
Ang mga scratch program (tinatawag na "mga proyekto") ay binubuo ng **sprite** (mga character/object) na tumutugon sa **mga bloke** na pinagsama-sama sa mga script.
### Mga Pangunahing Konsepto (Itinuro sa pamamagitan ng mga Block)
| Konsepto | Kategorya ng Scratch Block | Halimbawa |
|---------|----------------------|---------|
| **Mga Pagkakasunod-sunod** | Paggalaw, Mukhang | "Move 10 steps" then "Say Hello" |
| **Mga Loop** | Kontrol (dilaw) | "Ulitin ang 10", "Magpakailanman", "Ulitin hanggang" |
| **Mga Kondisyon** | Kontrol (dilaw) | "Kung... kung gayon", "Kung... kung gayon... iba pa" |
| **Mga Variable** | Mga variable (orange) | "Itakda ang marka sa 0", "Baguhin ang marka ng 1" |
| **Mga Kaganapan** | Mga Kaganapan (dilaw) | "Kapag nag-click ang berdeng bandila", "Kapag pinindot ang key" |
| **Mga Pag-andar** | Aking Mga Block (custom) | Tukuyin ang reusable block sequences |
| **Mga listahan (mga array)** | Mga variable (orange) | "Idagdag sa listahan", "Item ng listahan" |
| **Broadcast** | Mga Kaganapan | Magpadala ng mga mensahe sa pagitan ng mga sprite |
### Halimbawa: Simpleng Logic ng Laro
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

## Advanced na Syntax at Mga Pattern
### I-block ang Mga Kategorya sa Detalye
Inaayos ng Scratch 3.0 ang mga bloke sa mga kategoryang may kulay na code:
| Kategorya | Kulay | Mga Uri ng Block |
|----------|--------|-------------|
| **Paggalaw** | Asul | ilipat, liko, goto, glide, point, palitan x/y |
| **Mukhang** | Lila | sabihin, isipin, lumipat ng costume, baguhin ang laki, ipakita/itago |
| **Tunog** | Pink | play sound, stop sounds, change volume, change pitch |
| **Mga Kaganapan** | Dilaw | kapag na-click ang flag, kapag pinindot ang key, kapag nag-click ang sprite, i-broadcast |
| **Kontrol** | Ginto | maghintay, ulitin, magpakailanman, kung, kung-iba, ulitin hanggang, huminto |
| **Sensing** | Banayad na Asul | pagpindot, pinindot ang key, mouse, distansya, tanong/sagot, timer |
| **Mga Operator** | Berde | math ops, text ops, paghahambing, at/o/hindi, random |
| **Mga Variable** | Orange | itakda/palitan ang variable, listahan ng mga pagpapatakbo |
| **My Blocks** | Madilim na Pula | pasadyang mga kahulugan ng block (mga function) |
### Mga Advanced na Pattern ng Block
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

### Mga Custom na Block (Mga Function)
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

### Mga Operasyon ng Listahan (Mga Array)
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

### Broadcasting (Inter-Sprite Communication)
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

## Arkitektura at Disenyo ng System
### Disenyo na Batay sa Kaganapan
Gumagamit si Scratch ng arkitektura na hinimok ng kaganapan. Ang bawat script ay nagsisimula sa isang event block (hat block) at tumatakbo bilang tugon sa event na iyon.
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

### Istraktura ng Proyekto
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

### Clone System (Paglikha ng Bagay)
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

## Project Configuration at Build System
### Mga Extension ng Scratch
Sinusuportahan ng Scratch ang opisyal at mga extension ng komunidad na nagdaragdag ng mga kakayahan:
| Extension | Layunin |
|-----------|---------|
| **Pulat** | Gumuhit ng mga linya at hugis sa entablado |
| **Video Sensing** | Gumamit ng webcam para sa motion detection |
| **Text to Speech** | I-convert ang teksto sa pasalitang audio |
| **Isalin** | Isalin ang teksto sa pagitan ng mga wika |
| **Makey Makey** | Ikonekta ang mga pisikal na bagay bilang input |
| **micro:bit** | Ikonekta ang BBC micro:bit hardware |
| **LEGO Mindstorms** | Kontrolin ang mga LEGO robot |
| **Musika** | Magpatugtog ng mga musical notes at instruments |
### Scratch File Format
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

### Offline na Editor
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

## Pagsubok at Pag-debug
### Mga Built-in na Debugging Tool
Nagbibigay ang Scratch ng ilang built-in na tool para sa pag-debug ng mga proyekto:
| Tool | Paano Gamitin |
|------|-----------|
| **Turtle mode** | I-right-click ang isang sprite at piliin ang "ipakita ang debug" upang makita ang mga coordinate |
| **Mga variable na monitor** | I-right-click ang isang variable at piliin ang "ipakita" upang makita ang halaga nito sa real-time |
| **Ilista ang mga monitor** | Tingnan ang mga nilalaman ng listahan sa normal, row, o column display |
| **Turbo mode** | Pindutin ang Shift habang nagki-click sa berdeng bandila para sa mas mabilis na pagpapatupad |
| **Single-step mode** | I-right-click ang berdeng bandila para sa "isang hakbang" (pinabagal ang pagpapatupad) |
### Mga Pattern ng Pag-debug
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

### Mga Karaniwang Isyu
| Problema | Dahilan | Solusyon |
|---------|-------|----------|
| Hindi tumutugon ang Sprite | Walang block ng sumbrero ng kaganapan | Idagdag ang "Kapag nag-click ang berdeng bandila" o iba pang kaganapan |
| Hindi gumagana ang clone | Ginawa ang clone ngunit hindi ipinakita | Idagdag ang "Show" block pagkatapos ng "When I start as a clone" |
| Variable na ibinahagi sa pagitan ng mga sprite | Global vs lokal na variable na kalituhan | Gamitin ang opsyong "Para sa sprite na ito" |
| Hindi natanggap ang broadcast | Maling pangalan ng mensahe | I-verify ang broadcast at tumanggap ng mga pangalan na eksaktong tugma |
| Infinite loop freeze | "Magpakailanman" na walang paghihintay | Magdagdag ng maliliit na "Maghintay" na mga bloke sa mahigpit na mga loop |
---

## Interoperability
### Mga Extension ng Hardware
Maaaring kumonekta ang scratch sa pisikal na hardware sa pamamagitan ng mga extension:
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

### Scratch Extensions API (Custom Extensions)
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

## Mga Pattern ng Disenyo
### Pattern 1: Platformer Movement
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

### Pattern 2: Pag-scroll sa Background
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

### Pattern 3: Pagsunod sa Sprite (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Pattern 4: Sistema ng Imbentaryo na may Mga Listahan
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

### Pattern 5: Particle System na may mga Clone
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

## Pagganap at Pag-optimize
### Pag-optimize ng Sprite
| Teknik | Epekto | Paglalarawan |
|-----------|--------|-------------|
| **I-minimize ang mga clone** | Mataas | Ang bawat clone ay kumonsumo ng memorya; tanggalin kapag tapos na |
| **Bawasan ang mga costume** | Katamtaman | Ang mas kaunting mga switch ng costume ay nangangahulugan ng mas kaunting rendering overhead |
| **Gamitin ang "run without screen refresh"** | Mataas | Ang mga custom na bloke nang walang pag-refresh ng screen ay tumatakbo nang mas mabilis |
| **Limitahan ang "sabihin" na mga bloke** | Katamtaman | Ang mga speech bubble ay nagdudulot ng pag-render sa itaas |
| **Iwasan ang "magpakailanman" sa bawat sprite** | Katamtaman | Gumamit ng mga broadcast at kaganapan sa halip na patuloy na pagboto |
### Pamamahala ng Clone
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

### Checklist ng Pag-optimize
| Teknik | Epekto | Paglalarawan |
|-----------|--------|-------------|
| **Tumakbo nang walang pag-refresh ng screen** | Napakataas | Nilaktawan ng mga custom na bloke ang pag-render para sa bilis |
| **I-minimize ang mga aktibong clone** | Mataas | Tanggalin ang mga clone sa sandaling hindi na sila kailangan |
| **Gamitin ang mga broadcast nang matipid** | Katamtaman | Masyadong maraming mga broadcast sa bawat frame sanhi ng lag |
| **Pasimplehin ang mga costume** | Katamtaman | Mas mabilis na nagre-render ang mas maliliit na larawan |
| **Bawasan ang mga pagpapatakbo ng listahan** | Katamtaman | Iwasang mag-scan ng malalaking listahan sa bawat frame |
| **Gumamit ng "wait" blocks** | Mababa | Pigilan ang CPU hogging sa forever loops |
---

## Deployment at Real-World na Paggamit
### Pagbabahagi ng mga Proyekto
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

### Real-World Educational na Paggamit
| Konteksto | Paano Ginagamit ang Scratch | Iskala |
|---------|--------------------|-------|
| **K-12 na paaralan** | Panimula sa programming sa mga klase ng CS | Ginamit sa 190+ na bansa |
| **Mga coding club** | Mga workshop sa Scratch Club / CoderDojo | 3000+ club sa buong mundo |
| **Mga Aklatan** | Mga programang programming pagkatapos ng paaralan | Mga sistema ng pampublikong aklatan |
| **Homeschooling** | Self-paced programming education | Milyun-milyong mga nag-aaral sa bahay |
| **University CS0** | Mga hindi pangunahing panimulang kurso sa CS | Mga programa sa tulay ng unibersidad |
| **Accessibility** | Pagtuturo ng programming sa may kapansanan sa paningin | Suporta sa screen reader |
| **Therapy** | Pag-unlad ng cognitive at motor skill | Occupational therapy |
### Gasgas sa Pananaliksik sa Edukasyon
Ipinakita ng pananaliksik na epektibong nagtuturo si Scratch ng:
- **Sunod-sunod na pag-iisip**: Paghiwa-hiwalay ng mga problema sa mga nakaayos na hakbang
- **Mga kasanayan sa pag-debug**: Paghahanap at pag-aayos ng mga error sa logic
- **Creative expression**: Pinagsasama-sama ang sining, musika, at programming
- **Collaboration**: Pag-remix at pagbuo sa mga proyekto ng iba
- **Pagtitiyaga**: Pag-ulit sa mga proyekto upang mapabuti ang mga ito
---

## Transitioning Mula sa scratch
Pagkatapos matutunan ang Scratch, ang mga karaniwang susunod na hakbang ay kinabibilangan ng:
| Susunod na Wika | Bakit |
|--------------|-----|
| **Python** | Karamihan sa natural na paglipat — nababasang syntax, mga katulad na konsepto ng lohika |
| **JavaScript** | Kung interesado sa web/laro — agarang visual na feedback |
| **Lua (sa pamamagitan ng Roblox/Love2D)** | Kung interesado sa pagbuo ng laro |
| **App Inventor** | Mga visual block para sa Android app (parehong MIT lineage) |
| **Blockly** | Visual programming library ng Google (katulad na mga konsepto) |
### Concept Mapping: Scratch to Python
| Konsepto ng scratch | Katumbas ng Python |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Function call o event system |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-na-index!) |
| `length of [list]`| `len(list)`|
---

## Kailan Gamitin ang Scratch
| Sitwasyon | Bakit scratch | Mas mahusay na Alternatibo |
|----------|-----------|-------------------|
| Pagtuturo sa mga bata (8-16) sa code | Partikular na idinisenyo para dito | — |
| Ipinapakilala ang computational thinking | Visual, walang syntax error | — |
| Mga workshop sa paaralan / coding club | Libre, batay sa browser, walang setup | — |
| Pag-prototyping ng mga ideya sa laro nang biswal | Mabilis na pag-ulit | — |
| Propesyonal na pag-unlad | Hindi idinisenyo para dito | Python, JavaScript, anumang text language |
| Edukasyon sa CS sa antas ng unibersidad | Masyadong simple | Python, Java, C |
---

## Synthetic na Q&A
**Q1: Ang Scratch ba ay talagang isang programming language?**
A1: Oo, ang Scratch ay isang tunay na programming language, ngunit ito ay visual kaysa sa text-based. Sinusuportahan nito ang lahat ng pangunahing konsepto ng programming: mga variable, loop, conditional, function (custom blocks), listahan, at event-driven na programming. Ang kaibahan ay nag-drag at drop ka ng mga bloke sa halip na mag-type ng code. Inaalis nito ang mga error sa syntax at ginagawang naa-access ang programming sa mga batang nag-aaral.
**Q2: Paano ako gagawa ng mga custom na function (custom blocks) sa Scratch?**
A2: Pumunta sa kategoryang "My Blocks" at i-click ang "Make a Block". Bigyan ito ng pangalan, magdagdag ng mga parameter kung kinakailangan, pagkatapos ay tukuyin ang pag-uugali nito sa pamamagitan ng pagdaragdag ng mga bloke sa ibaba nito. Ang mga custom na bloke ay maaaring kumuha ng mga input (mga numero, string, boolean) at maaaring tumawag sa iba pang mga custom na bloke. Nagbibigay-daan ito sa modular programming at muling paggamit ng code.
**Q3: Ano ang pinakamahusay na paraan upang pangasiwaan ang kumplikadong lohika ng laro sa Scratch?**
A3: Gumamit ng mga custom na bloke upang ayusin ang lohika, mag-broadcast ng mga mensahe para sa koordinasyon ng kaganapan sa pagitan ng mga sprite, at gumamit ng mga listahan upang mag-imbak ng estado ng laro (mga marka, antas, imbentaryo). Para sa kumplikadong AI, gumamit ng mga finite state machine na may mga variable na sumusubaybay sa kasalukuyang estado. I-clone ang mga sprite para sa maraming kaaway at gamitin ang "kapag nagsimula ako bilang isang clone" upang bigyan ang bawat independiyenteng pag-uugali.
**Q4: Paano ko maibabahagi ang data sa pagitan ng mga sprite sa Scratch?**
A4: Gumamit ng mga pandaigdigang variable (ginawa nang walang "para sa sprite na ito lang") para sa nakabahaging data tulad ng marka o estado ng laro. Gumamit ng mga broadcast na mensahe upang ma-trigger ang mga kaganapan sa mga sprite. Para sa mas kumplikadong komunikasyon, gumamit ng mga listahan bilang mga nakabahaging istruktura ng data. Ang bawat sprite ay maaaring magbasa at magbago ng mga pandaigdigang variable at listahan, na nagpapagana ng koordinasyon.
**Q5: Ano ang ilang advanced na diskarte sa Scratch?**
A5: Gumamit ng mga pen block para sa pagguhit at paglikha ng mga visual effect. Ipatupad ang raycasting para sa 3D-like graphics. Gumamit ng mga cloud variable para sa mga multiplayer na laro (nangangailangan ng status ng Scratcher). Gumawa ng procedural generation na may mga random na numero at listahan. Gumamit ng mga custom na bloke na may mga parameter para sa mga magagamit muli na algorithm. Mag-eksperimento sa video sensing at sound manipulation para sa mga interactive na proyekto.
---

## Chain-of-Thought
### Problema 1: Paglikha ng Larong Platformer
**Hakbang 1: Unawain ang Problema**
Kailangan nating lumikha ng isang platformer kung saan ang isang karakter ay maaaring gumalaw pakaliwa/kanan, tumalon, maiwasan ang mga hadlang, at mangolekta ng mga item.
**Hakbang 2: Tukuyin ang Diskarte**
- Gumamit ng gravity simulation na may "falling" variable
- I-detect ang lupa/bangga gamit ang kulay o sprite touching
- Store antas ng data sa mga listahan
- Gumamit ng mga custom na bloke para sa jump at movement logic
**Hakbang 3: Ipatupad ang Solusyon**```scratch
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

**Hakbang 4: I-verify at I-optimize**
Subukan ang paglukso sa iba't ibang platform. Ayusin ang gravity at tumalon taas para sa magandang pakiramdam ng laro. Magdagdag ng mga animation para sa pagtakbo at paglukso. Magpatupad ng mga checkpoint gamit ang mga broadcast message.
---

### Problema 2: Paglikha ng Larong Pagsusulit na may Pagsubaybay sa Iskor
**Hakbang 1: Unawain ang Problema**
Bumuo ng larong pagsusulit na nagtatanong, nagsusuri ng mga sagot, at sumusubaybay sa marka ng manlalaro.
**Hakbang 2: Tukuyin ang Diskarte**
- Mag-imbak ng mga tanong at sagot sa mga parallel na listahan
- Gumamit ng question counter upang subaybayan ang pag-unlad
- Gumamit ng "magtanong at maghintay" na mga bloke para sa input
- Ihambing ang mga sagot at i-update ang marka
**Hakbang 3: Ipatupad ang Solusyon**```scratch
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

**Hakbang 4: I-verify at I-optimize**
Subukan gamit ang iba't ibang mga sagot kabilang ang mga edge case. Magdagdag ng feedback para sa mga maling sagot. Magpatupad ng opsyon na muling subukan. Magdagdag ng mga sound effect at visual na feedback para sa mga tama/maling sagot.
---

### Problema 3: Pagguhit ng Fractal Tree gamit ang Panulat
**Hakbang 1: Unawain ang Problema**
Gumawa ng recursive fractal tree gamit ang extension ng panulat.
**Hakbang 2: Tukuyin ang Diskarte**
- Gumamit ng recursion upang gumuhit ng mga sanga
- Ang bawat sangay ay nahahati sa dalawang mas maliliit na sangay
- Gumamit ng mga random na anggulo para sa natural na pagkakaiba-iba
- Subaybayan ang haba ng sangay at bawasan sa bawat antas ng recursion
**Hakbang 3: Ipatupad ang Solusyon**```scratch
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

**Hakbang 4: I-verify at I-optimize**
Isaayos ang threshold ng haba ng sangay at mga saklaw ng anggulo para sa mga aesthetic na puno. Magdagdag ng mga dahon sa mga tip ng sangay gamit ang mga pagbabago sa kulay. Magpatupad ng iba't ibang estilo ng puno. I-save ang mga guhit bilang mga imahe.
---

## Buod
Ang scratch ay hindi isang programming language sa tradisyonal na kahulugan — ito ay isang kapaligiran sa pag-aaral. Ang henyo nito ay inaalis ang bawat hadlang sa pagitan ng isang bata at ang kagalakan ng paglikha ng isang bagay na interactive. Sa pamamagitan ng pagtuon sa mga konsepto sa halip na syntax, itinuturo ni Scratch ang mga batayan ng programming na lumilipat sa anumang wika. Para sa pagpapakilala ng programming sa mga batang nag-aaral, ang Scratch ang pamantayang ginto.