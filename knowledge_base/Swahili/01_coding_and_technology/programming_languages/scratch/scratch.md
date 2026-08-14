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
# Mkwaruzo
Scratch ni lugha inayoonekana, yenye msingi wa programu iliyotengenezwa na MIT Media Lab na ilitolewa kwa mara ya kwanza mwaka wa 2007. Badala ya kuandika msimbo unaotegemea maandishi, watumiaji hupiga pamoja vitalu vya rangi ili kuunda programu. Scratch imeundwa mahususi kwa watoto wa miaka 8-16 (ingawa wanafunzi wa umri wote huitumia) kufundisha dhana za kimsingi za upangaji - vitanzi, masharti, vigeu, matukio na vitendakazi - bila kizuizi cha makosa ya sintaksia.
Scratch ndiyo lugha ya utangulizi inayotumika zaidi duniani, ikiwa na watumiaji zaidi ya milioni 100 waliosajiliwa na inapatikana katika lugha 70+. Inatumika katika kivinjari cha wavuti na ni bure.
---

## Kwanini Kukuna Mambo
- **Utangulizi bora wa upangaji**: Huondoa vizuizi vya sintaksia kabisa. Dhana hufundishwa kupitia upotoshaji wa kuona.
- **Fikra za kimahesabu**: Hufundisha mtengano, utambuzi wa muundo, uondoaji na muundo wa algoriti.
- **Ubunifu unaoendeshwa**: Watoto huunda michezo, uhuishaji, hadithi na muziki — kujifunza kupanga programu kama matokeo ya kutengeneza mambo wanayojali.
- **Ufikiaji wa kimataifa**: Inatumika shuleni kote ulimwenguni. Inapatikana katika lugha 70+. Bure na msingi wa kivinjari.
- **Jumuiya**: Jumuiya ya mtandaoni ya Scratch inafundisha kushiriki, kuchanganya upya na kujifunza kwa kushirikiana.
## Mapatano
| Kizuizi | Maelezo | Njia ya Kawaida |
|-----------|---------|-------------------|
| **Sio lugha "halisi" ya upangaji** | Haiwezi kuunda programu ya uzalishaji, API, au mifumo | Mpito hadi Python, JavaScript, au lugha zinazotegemea maandishi |
| **Uwezo mdogo** | Hakuna faili I/O, mitandao, au miundo ya data ya hali ya juu | Tumia kwa kujifunza; nenda kwa lugha za maandishi kwa miradi halisi |
| **Utendaji** | Imefasiriwa, polepole kwa miradi changamano | Haijaundwa kwa kazi muhimu ya utendaji |
| **Mtazamo wa umri** | Mara nyingi huonekana kama "kwa watoto tu" | Mkwaruzo ni zana ya kujifunzia, si lugha ya kitaalamu |
---

## Jinsi Mkwaruzo Hufanya Kazi
Programu za kuchana (zinazoitwa "miradi") zinajumuisha **sprites** (herufi/vitu) vinavyojibu **vizuizi** vilivyochongwa pamoja katika hati.
### Dhana za Msingi (Zinazofundishwa Kupitia Vitalu)
| Dhana | Kitengo cha Kuzuia Mkwaruzo | Mfano |
|---------|---------------------|---------|
| **Mfuatano** | Mwendo, Inaonekana | "Sogeza hatua 10" kisha "Sema Hujambo" |
| **Tanzi** | Udhibiti (njano) | "Rudia 10", "Milele", "Rudia hadi" |
| **Masharti** | Udhibiti (njano) | "Kama ... basi", "Kama ... basi ... vinginevyo" |
| **Vigezo** | Vigezo (machungwa) | "Weka alama kuwa 0", "Badilisha alama kwa 1" |
| **Matukio** | Matukio (njano) | "Bendera ya kijani ilipobofya", "Kitufe kilipobonyezwa" |
| **Kazi** | Vitalu Vyangu (desturi) | Bainisha mpangilio wa vizuizi vinavyoweza kutumika tena |
| **Orodha (safu)** | Vigezo (machungwa) | "Ongeza kwenye orodha", "Kipengee cha orodha" |
| **Utangazaji** | Matukio | Tuma ujumbe kati ya sprites |
### Mfano: Mantiki Rahisi ya Mchezo
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

## Sintaksia na Miundo ya Kina
### Zuia Aina kwa Maelezo
Scratch 3.0 hupanga vizuizi katika kategoria zenye msimbo wa rangi:
| Kitengo | Rangi | Aina za Kuzuia |
|----------|--------|-------------|
| **Mwendo** | Bluu | sogeza, geuza, nenda, telezesha, elekeza, badilisha x/y |
| **Inaonekana** | Zambarau | sema, fikiria, badilisha vazi, badilisha saizi, onyesha/ficha |
| **Sauti** | Pinki | cheza sauti, acha sauti, badilisha sauti, badilisha sauti |
| **Matukio** | Njano | wakati bendera ilibofya, wakati ufunguo umebonyezwa, sprite ilipobofya, tangaza |
| **Dhibiti** | Dhahabu | subiri, rudia, milele, ikiwa, kama-vinginevyo, rudia hadi, acha |
| **Kuhisi** | Bluu Isiyokolea | kugusa, kubonyeza kitufe, kipanya, umbali, uliza/jibu, kipima saa |
| **Waendeshaji** | Kijani | utendakazi wa hesabu, utendakazi wa maandishi, ulinganisho, na/au/sivyo, nasibu |
| **Vigezo** | Chungwa | weka/badilisha utofauti, orodhesha shughuli |
| **Vizuizi Vyangu** | Nyekundu Iliyokolea | ufafanuzi maalum wa kuzuia (kazi) |
### Miundo ya Juu ya Kuzuia
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

### Vitalu Maalum (Kazi)
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

### Orodhesha Operesheni (Safu)
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

### Utangazaji (Inter-Sprite Communication)
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

## Usanifu na Usanifu wa Mfumo
### Muundo Unaoendeshwa na Tukio
Scratch hutumia usanifu unaoendeshwa na tukio. Kila hati huanza na kizuizi cha tukio (kizuizi cha kofia) na huendesha kwa kujibu tukio hilo.
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

### Muundo wa Mradi
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

### Mfumo wa Kuiga (Uundaji wa Kitu)
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

## Usanidi wa Mradi & Mfumo wa Kuunda
### Viendelezi vya Kukwaruza
Scratch inasaidia viendelezi rasmi na vya jumuiya vinavyoongeza uwezo:
| Kiendelezi | Kusudi |
|-----------|---------|
| **Kalamu** | Chora mistari na maumbo kwenye jukwaa |
| **Kuhisi Video** | Tumia kamera ya wavuti kugundua mwendo |
| **Nakala kwa Hotuba** | Badilisha maandishi kuwa sauti inayozungumzwa |
| **Tafsiri** | Tafsiri maandishi kati ya lugha |
| **Makey Makey** | Unganisha vitu halisi kama ingizo |
| **micro:bit** | Unganisha BBC micro:bit hardware |
| **Dhoruba za Akili za LEGO** | Dhibiti roboti za LEGO |
| **Muziki** | Cheza maelezo ya muziki na ala |
### Chambua Umbizo la Faili
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

### Kihariri Nje ya Mtandao
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

## Majaribio na Utatuzi
### Zana za Utatuzi Zilizojengwa ndani
Scratch hutoa zana kadhaa zilizojengwa ndani za miradi ya kurekebisha hitilafu:
| Zana | Jinsi ya kutumia |
|------|------------|
| **Njia ya kasa** | Bofya kulia sprite na uchague "onyesha utatuzi" ili kuona viwianishi |
| **Vichunguzi vinavyobadilika** | Bofya kulia kigezo na uchague "onyesha" ili kuona thamani yake katika muda halisi |
| **Orodhesha wachunguzi** | Tazama yaliyomo kwenye orodha katika onyesho la kawaida, safu mlalo au safuwima |
| **Modi ya Turbo** | Shikilia Shift huku ukibofya bendera ya kijani kwa utekelezaji wa haraka |
| **Njia ya hatua moja** | Bofya kulia bendera ya kijani kwa "hatua moja" (inapunguza utekelezaji) |
### Miundo ya utatuzi
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

### Masuala ya Kawaida
| Tatizo | Sababu | Suluhisho |
|---------|-------------------|
| Sprite haijibu | Hakuna kizuizi cha kofia ya tukio | Ongeza "Wakati bendera ya kijani ilipobofya" au tukio lingine |
| Clone haifanyi kazi | Clone imeundwa lakini haijaonyeshwa | Ongeza kizuizi cha "Onyesha" baada ya "Ninapoanza kama mshirika" |
| Tofauti iliyoshirikiwa kati ya sprites | Mkanganyiko wa kutofautisha wa kimataifa dhidi ya wa ndani | Tumia chaguo la "Kwa sprite hii pekee" |
| Tangazo halijapokelewa | Jina la ujumbe si sahihi | Thibitisha matangazo na upokee majina yanayolingana haswa |
| Kitanzi kisicho na kikomo | "Milele" bila kusubiri | Ongeza vizuizi vidogo vya "Subiri" kwenye vitanzi vikali |
---

## Kuingiliana
### Viendelezi vya maunzi
Mkwaruzo unaweza kuunganisha kwa maunzi halisi kupitia viendelezi:
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

### API ya Viendelezi vya Scratch (Viendelezi Maalum)
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

## Miundo ya Kubuni
### Mchoro wa 1: Mwendo wa jukwaa
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

### Mchoro wa 2: Mandharinyuma ya Kusogeza
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

### Mchoro wa 3: Ufuatao wa Sprite (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Muundo wa 4: Mfumo wa Mali na Orodha
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

### Muundo wa 5: Mfumo wa Chembe chembe zenye Clones
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

## Utendaji na Uboreshaji
### Uboreshaji wa Sprite
| Mbinu | Athari | Maelezo |
|-----------|--------|-------------|
| **Punguza clones** | Juu | Kila clone hutumia kumbukumbu; futa ukimaliza |
| **Punguza mavazi** | Kati | Swichi chache za mavazi humaanisha uwasilishaji mdogo zaidi |
| **Tumia "endesha bila kuonyesha upya skrini"** | Juu | Vizuizi maalum bila kuonyesha upya skrini hufanya kazi haraka |
| **Punguza vizuizi vya "sema"** | Kati | Viputo vya usemi husababisha utoaji juu |
| **Epuka "milele" katika kila sprite** | Kati | Tumia matangazo na matukio badala ya kupiga kura mara kwa mara |
### Usimamizi wa Clone
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

### Orodha ya Hakiki ya Uboreshaji
| Mbinu | Athari | Maelezo |
|-----------|--------|-------------|
| **Endesha bila kuonyesha upya skrini** | Juu Sana | Vizuizi maalum ruka uwasilishaji kwa kasi |
| **Punguza clones amilifu** | Juu | Futa clones mara tu hazihitajiki tena |
| **Tumia matangazo kwa uangalifu** | Kati | Matangazo mengi sana kwa kila fremu husababisha kuchelewa |
| **Rahisisha mavazi** | Kati | Picha ndogo hutoa haraka |
| **Punguza utendakazi wa orodha** | Kati | Epuka kuchanganua orodha kubwa kila fremu |
| **Tumia vizuizi vya "ngoja"** | Chini | Zuia CPU kuingia kwenye vitanzi vya milele |
---

## Usambazaji na Matumizi Halisi ya Ulimwenguni
### Kushiriki Miradi
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

### Matumizi Halisi ya Kielimu Ulimwenguni
| Muktadha | Jinsi Mkwaruzo Hutumika | Kiwango |
|---------|---------------------------|
| **Shule za K-12** | Utangulizi wa upangaji programu katika madarasa ya CS | Inatumika katika nchi zaidi ya 190 |
| **Vilabu vya kuweka rekodi** | Scratch Club / Warsha za CoderDojo | Zaidi ya vilabu 3000 duniani kote |
| **Maktaba** | Programu za programu za baada ya shule | Mifumo ya maktaba ya umma |
| **Shule ya nyumbani** | Elimu ya programu ya kujitegemea | Mamilioni ya wanafunzi wa nyumbani |
| **Chuo Kikuu CS0** | Kozi zisizo kuu za utangulizi za CS | Mipango ya daraja la chuo kikuu |
| **Ufikivu** | Kufundisha programu kwa wasioona | Usaidizi wa kisomaji skrini |
| **Tiba** | Ukuzaji wa ujuzi wa utambuzi na gari | Tiba ya kazini |
### Mkwaruzo katika Utafiti wa Elimu
Utafiti umeonyesha kuwa Scratch inafundisha kwa ufanisi:
- **Kufikiria kwa kufuatana**: Kuvunja matatizo katika hatua zilizopangwa
- **Ujuzi wa kurekebisha**: Kupata na kurekebisha makosa katika mantiki
- **Usemi wa ubunifu**: Kuchanganya sanaa, muziki, na programu
- **Ushirikiano**: Kuchanganya na kujenga kwenye miradi ya wengine
- **Uvumilivu**: Kurudia miradi ya kuiboresha
---

## Mpito Kutoka Mwanzo
Baada ya kujifunza Scratch, hatua zifuatazo za kawaida ni pamoja na:
| Lugha Inayofuata | Kwa nini |
|--------------|-----|
| **Chatu** | Mpito mwingi wa asili — sintaksia inayoweza kusomeka, dhana sawa za mantiki |
| **JavaScript** | Ikiwa unavutiwa na wavuti/michezo — maoni ya kuona ya papo hapo |
| **Lua (kupitia Roblox/Love2D)** | Ikiwa una nia ya ukuzaji wa mchezo |
| **Mvumbuzi wa Programu** | Vizuizi vinavyoonekana kwa programu za Android (nasaba sawa ya MIT) |
| **Kizuizi** | Maktaba ya programu ya kuona ya Google (dhana zinazofanana) |
### Ramani ya Dhana: Chora hadi chatu
| Dhana ya Mkwaruzo | Chatu Sawa |
|------------------------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Kazi ya simu au mfumo wa tukio |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-faharisi!) |
| `length of [list]`| `len(list)`|
---

## Wakati wa Kutumia Scratch
| Hali | Kwa nini Kukuna | Mbadala Bora |
|----------|-----------|-------------------|
| Kufundisha watoto (8-16) kwa msimbo | Iliyoundwa mahsusi kwa hii | - |
| Kuanzisha fikra za kimahesabu | Visual, hakuna makosa ya sintaksia | - |
| Warsha za shule / vilabu vya kuweka rekodi | Bila malipo, kulingana na kivinjari, hakuna usanidi | - |
| Mawazo ya mchezo wa kuigiza kwa kuibua | Marudio ya haraka | - |
| Maendeleo ya kitaaluma | Haijaundwa kwa ajili hii | Python, JavaScript, lugha yoyote ya maandishi |
| Elimu ya CS ngazi ya chuo kikuu | Rahisi sana | Chatu, Java, C |
---

## Maswali na Majibu Yaliyoundwa
**Swali la 1: Je, Scratch ni lugha ya programu kweli?**
A1: Ndiyo, Scratch ni lugha halisi ya programu, lakini inaonekana badala ya kutegemea maandishi. Inaauni dhana zote za kimsingi za upangaji: vigeu, vitanzi, masharti, vitendakazi (vizuizi maalum), orodha, na upangaji programu unaoendeshwa na hafla. Tofauti ni kwamba unaburuta na kuangusha vizuizi badala ya kuandika msimbo. Hii huondoa makosa ya sintaksia na kufanya upangaji kupatikana kwa wanafunzi wachanga.
**Swali la 2: Je, ninawezaje kuunda vitendaji maalum (vizuizi maalum) katika Mwanzo?**
A2: Nenda kwenye kitengo cha "Vizuizi Vyangu" na ubofye "Fanya Kizuizi". Ipe jina, ongeza vigezo ikiwa inahitajika, kisha ueleze tabia yake kwa kuongeza vizuizi chini yake. Vitalu maalum vinaweza kuchukua pembejeo (nambari, mifuatano, booleans) na vinaweza kupiga vitalu vingine maalum. Hii huwezesha upangaji wa programu na utumiaji wa msimbo tena.
**Swali la 3: Ni ipi njia bora ya kushughulikia mantiki changamano ya mchezo katika Mwanzo?**
A3: Tumia vizuizi maalum ili kupanga mantiki, kutangaza ujumbe kwa uratibu wa matukio kati ya sprites, na kutumia orodha kuhifadhi hali ya mchezo (alama, viwango, orodha). Kwa AI changamano, tumia mashine za hali ya mwisho zenye vigeu vinavyofuatilia hali ya sasa. Clone sprites kwa maadui wengi na tumia "ninapoanza kama clone" kutoa kila tabia huru.
**Swali la 4: Ninawezaje kushiriki data kati ya sprites kwenye Scratch?**
A4: Tumia vigeu vya kimataifa (vilivyoundwa bila "kwa sprite hii pekee") kwa data iliyoshirikiwa kama vile alama au hali ya mchezo. Tumia jumbe za utangazaji kuanzisha matukio kwenye sprites. Kwa mawasiliano changamano zaidi, tumia orodha kama miundo ya data iliyoshirikiwa. Kila sprite inaweza kusoma na kurekebisha vigezo na orodha za kimataifa, kuwezesha uratibu.
**Swali la 5: Je! ni baadhi ya mbinu za hali ya juu katika Scratch?**
A5: Tumia vizuizi vya kalamu kwa kuchora na kuunda athari za kuona. Tekeleza uangazaji kwa michoro inayofanana na 3D. Tumia vigezo vya wingu kwa michezo ya wachezaji wengi (inahitaji hali ya Scratcher). Unda kizazi cha kitaratibu na nambari na orodha nasibu. Tumia vizuizi maalum vilivyo na vigezo kwa algoriti zinazoweza kutumika tena. Jaribio la kutambua video na uchezaji wa sauti kwa miradi shirikishi.
---

## Mlolongo-wa-Fikra
### Tatizo la 1: Kuunda Mchezo wa Mfumo
**Hatua ya 1: Elewa Tatizo**
Tunahitaji kuunda jukwaa ambapo mhusika anaweza kusogea kushoto/kulia, kuruka, kuepuka vikwazo na kukusanya vitu.
**Hatua ya 2: Tambua Mbinu**
- Tumia uigaji wa mvuto na kigezo cha "kuanguka".
- Tambua ardhi/mgongano kwa kutumia rangi au mguso wa sprite
- Hifadhi data ya kiwango katika orodha
- Tumia vizuizi maalum kwa kuruka na mantiki ya harakati
**Hatua ya 3: Tekeleza Suluhisho**```scratch
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

**Hatua ya 4: Thibitisha na Uboreshe**
Mtihani wa kuruka kwenye majukwaa tofauti. Rekebisha mvuto na urefu wa kuruka kwa hisia nzuri ya mchezo. Ongeza uhuishaji wa kukimbia na kuruka. Tekeleza vituo vya ukaguzi kwa kutumia ujumbe wa matangazo.
---

### Tatizo la 2: Kuunda Mchezo wa Maswali kwa Ufuatiliaji wa Alama
**Hatua ya 1: Elewa Tatizo**
Unda mchezo wa maswali unaouliza maswali, kuangalia majibu na kufuatilia alama za mchezaji.
**Hatua ya 2: Tambua Mbinu**
- Hifadhi maswali na majibu katika orodha sambamba
- Tumia kihesabu cha maswali kufuatilia maendeleo
- Tumia vizuizi vya "uliza na subiri" kwa ingizo
- Linganisha majibu na sasisha alama
**Hatua ya 3: Tekeleza Suluhisho**```scratch
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

**Hatua ya 4: Thibitisha na Uboreshe**
Jaribu na majibu mbalimbali ikiwa ni pamoja na kesi za makali. Ongeza maoni kwa majibu yasiyo sahihi. Tekeleza chaguo la kujaribu tena. Ongeza athari za sauti na maoni ya kuona kwa majibu sahihi/mabaya.
---

### Tatizo la 3: Kuchora Miti Iliyovunjika kwa Peni
**Hatua ya 1: Elewa Tatizo**
Unda mti wa fractal unaojirudia kwa kutumia kiendelezi cha kalamu.
**Hatua ya 2: Tambua Mbinu**
- Tumia marudio kuchora matawi
- Kila tawi hugawanyika katika matawi mawili madogo
- Tumia pembe za nasibu kwa utofauti wa asili
- Fuatilia urefu wa tawi na upunguze kwa kila kiwango cha kujirudia
**Hatua ya 3: Tekeleza Suluhisho**```scratch
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

**Hatua ya 4: Thibitisha na Uboreshe**
Rekebisha kizingiti cha urefu wa tawi na safu za pembe kwa miti ya urembo. Ongeza majani kwenye vidokezo vya tawi kwa kutumia mabadiliko ya rangi. Tekeleza mitindo tofauti ya miti. Hifadhi michoro kama picha.
---

## Muhtasari
Mkwaruzo si lugha ya programu kwa maana ya jadi - ni mazingira ya kujifunzia. Ustadi wake ni kuondoa kila kizuizi kati ya mtoto na furaha ya kuunda kitu kinachoingiliana. Kwa kuzingatia dhana badala ya sintaksia, Scratch hufundisha misingi ya upangaji inayohamisha hadi lugha yoyote. Kwa kuanzisha programu kwa wanafunzi wachanga, Scratch ndio kiwango cha dhahabu.