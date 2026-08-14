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

# खरोंचना
स्क्रैच एमआईटी मीडिया लैब द्वारा विकसित एक दृश्य, ब्लॉक-आधारित प्रोग्रामिंग भाषा है और पहली बार 2007 में जारी की गई थी। टेक्स्ट-आधारित कोड लिखने के बजाय, उपयोगकर्ता प्रोग्राम बनाने के लिए रंगीन ब्लॉकों को एक साथ स्नैप करते हैं। स्क्रैच को विशेष रूप से 8-16 वर्ष की आयु के बच्चों के लिए डिज़ाइन किया गया है (हालाँकि सभी उम्र के शिक्षार्थी इसका उपयोग करते हैं) ताकि सिंटैक्स त्रुटियों की बाधा के बिना मौलिक प्रोग्रामिंग अवधारणाओं - लूप, सशर्त, चर, घटनाओं और कार्यों को सिखाया जा सके।
स्क्रैच दुनिया में सबसे व्यापक रूप से उपयोग की जाने वाली परिचयात्मक प्रोग्रामिंग भाषा है, जिसके 100 मिलियन से अधिक पंजीकृत उपयोगकर्ता हैं और 70 से अधिक भाषाओं में उपलब्धता है। यह वेब ब्राउज़र में चलता है और मुफ़्त है।
---

## स्क्रैच क्यों मायने रखता है
- **प्रोग्रामिंग का सर्वोत्तम परिचय**: सिंटैक्स बाधाओं को पूरी तरह से हटा देता है। अवधारणाओं को दृश्य हेरफेर के माध्यम से सिखाया जाता है।
- **कम्प्यूटेशनल सोच**: अपघटन, पैटर्न पहचान, अमूर्तता और एल्गोरिदम डिजाइन सिखाता है।
- **रचनात्मकता से प्रेरित**: बच्चे गेम, एनिमेशन, कहानियां और संगीत बनाते हैं - जिन चीज़ों की वे परवाह करते हैं उन्हें बनाने के उपोत्पाद के रूप में प्रोग्रामिंग सीखते हैं।
- **वैश्विक पहुंच**: दुनिया भर के स्कूलों में उपयोग किया जाता है। 70+ भाषाओं में उपलब्ध है। मुफ़्त और ब्राउज़र-आधारित।
- **समुदाय**: स्क्रैच ऑनलाइन समुदाय साझा करना, रीमिक्सिंग और सहयोगात्मक शिक्षा सिखाता है।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **एक "वास्तविक" प्रोग्रामिंग भाषा नहीं** | उत्पादन सॉफ्टवेयर, एपीआई या सिस्टम नहीं बना सकते | पायथन, जावास्क्रिप्ट, या टेक्स्ट-आधारित भाषाओं में संक्रमण |
| **सीमित क्षमताएं** | कोई फ़ाइल I/O, नेटवर्किंग, या उन्नत डेटा संरचना नहीं | सीखने के लिए उपयोग करें; वास्तविक परियोजनाओं के लिए टेक्स्ट भाषाओं की ओर बढ़ें |
| **प्रदर्शन** | व्याख्या की गई, जटिल परियोजनाओं के लिए धीमी गति | प्रदर्शन-महत्वपूर्ण कार्य के लिए डिज़ाइन नहीं किया गया |
| **आयु बोध** | अक्सर "सिर्फ बच्चों के लिए" के रूप में देखा जाता है | स्क्रैच एक सीखने का उपकरण है, कोई पेशेवर भाषा नहीं |
---

## स्क्रैच कैसे काम करता है
स्क्रैच प्रोग्राम (जिन्हें "प्रोजेक्ट" कहा जाता है) में **स्प्राइट** (अक्षर/ऑब्जेक्ट) शामिल होते हैं जो स्क्रिप्ट में एक साथ स्नैप किए गए **ब्लॉक** पर प्रतिक्रिया करते हैं।
### मूल अवधारणाएँ (ब्लॉकों के माध्यम से सिखाई गईं)
| संकल्पना | स्क्रैच ब्लॉक श्रेणी | उदाहरण |
|------|----------------------|------|
| **अनुक्रम** | चाल, रूप | "10 कदम चलें" फिर "हैलो कहें" |
| **लूप्स** | नियंत्रण (पीला) | "10 दोहराएँ", "हमेशा", "जब तक दोहराएँ" |
| **सशर्त** | नियंत्रण (पीला) | "अगर...तो", "अगर...तो...नहीं तो" |
| **चर** | चर (नारंगी) | "स्कोर को 0 पर सेट करें", "स्कोर को 1 से बदलें" |
| **घटनाएँ** | घटनाएँ (पीला) | "जब हरी झंडी दिखाई गई", "जब कुंजी दबाई गई" |
| **कार्य** | मेरे ब्लॉक (कस्टम) | पुन: प्रयोज्य ब्लॉक अनुक्रमों को परिभाषित करें |
| **सूचियाँ (सरणियाँ)** | चर (नारंगी) | "सूची में जोड़ें", "सूची का आइटम" |
| **प्रसारण** | घटनाएँ | स्प्राइट्स के बीच संदेश भेजें |
### उदाहरण: सरल खेल तर्क
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

## उन्नत सिंटैक्स और पैटर्न
### श्रेणियों को विस्तार से ब्लॉक करें
स्क्रैच 3.0 ब्लॉकों को रंग-कोडित श्रेणियों में व्यवस्थित करता है:
| श्रेणी | रंग | ब्लॉक प्रकार |
|---|--------|--------|
| **मोशन** | नीला | हिलना, मुड़ना, गोटो, सरकना, बिंदु, परिवर्तन x/y |
| **दिखता है** | बैंगनी | कहना, सोचना, पोशाक बदलना, आकार बदलना, दिखाना/छिपाना |
| **ध्वनि** | गुलाबी | ध्वनि बजाओ, ध्वनियाँ रोको, आवाज़ बदलो, पिच बदलो |
| **घटनाएँ** | पीला | जब फ़्लैग क्लिक किया गया, जब कुंजी दबाई गई, जब स्प्राइट क्लिक किया गया, प्रसारण |
| **नियंत्रण** | सोना | रुकना, दोहराना, हमेशा के लिए, अगर, अगर-और, तब तक दोहराना, रुकना |
| **संवेदन** | हल्का नीला | स्पर्श करना, कुंजी दबाना, माउस, दूरी, पूछना/उत्तर देना, टाइमर |
| **संचालक** | हरा | गणित संचालन, पाठ संचालन, तुलना, और/या/नहीं, यादृच्छिक |
| **चर** | नारंगी | सेट/परिवर्तन चर, सूची संचालन |
| **मेरे ब्लॉक** | गहरा लाल | कस्टम ब्लॉक परिभाषाएँ (फ़ंक्शन) |
### उन्नत ब्लॉक पैटर्न
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

### कस्टम ब्लॉक (फ़ंक्शन)
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

### सूची संचालन (सरणी)
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

### प्रसारण (इंटर-स्प्राइट कम्युनिकेशन)
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

## वास्तुकला एवं सिस्टम डिज़ाइन
### इवेंट-संचालित डिज़ाइन
स्क्रैच एक इवेंट-संचालित आर्किटेक्चर का उपयोग करता है। प्रत्येक स्क्रिप्ट एक इवेंट ब्लॉक (हैट ब्लॉक) से शुरू होती है और उस इवेंट के जवाब में चलती है।
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

### परियोजना संरचना
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

### क्लोन सिस्टम (वस्तु निर्माण)
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### स्क्रैच एक्सटेंशन
स्क्रैच आधिकारिक और सामुदायिक एक्सटेंशन का समर्थन करता है जो क्षमताएं जोड़ता है:
| विस्तार | उद्देश्य |
|----|----|
| **कलम** | मंच पर रेखाएं और आकृतियां बनाएं |
| **वीडियो सेंसिंग** | गति का पता लगाने के लिए वेबकैम का उपयोग करें |
| **पाठ से भाषण** | टेक्स्ट को बोले गए ऑडियो में बदलें |
| **अनुवाद** | भाषाओं के बीच पाठ का अनुवाद करें |
| **मेकी मेकी** | भौतिक वस्तुओं को इनपुट के रूप में कनेक्ट करें |
| **माइक्रो:बिट** | बीबीसी माइक्रो:बिट हार्डवेयर कनेक्ट करें |
| **लेगो माइंडस्टॉर्म** | लेगो रोबोट को नियंत्रित करें |
| **संगीत** | संगीत नोट्स और वाद्ययंत्र बजाएं |
### स्क्रैच फ़ाइल स्वरूप
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

### ऑफ़लाइन संपादक
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

## परीक्षण एवं डिबगिंग
### अंतर्निहित डिबगिंग उपकरण
स्क्रैच डिबगिंग परियोजनाओं के लिए कई अंतर्निहित उपकरण प्रदान करता है:
| उपकरण | कैसे उपयोग करें |
|------|--------|
| **कछुआ मोड** | स्प्राइट पर राइट-क्लिक करें और निर्देशांक देखने के लिए "डिबग दिखाएं" चुनें |
| **वेरिएबल मॉनिटर** | किसी वेरिएबल पर राइट-क्लिक करें और वास्तविक समय में उसका मान देखने के लिए "शो" चुनें |
| **सूची मॉनिटर** | सूची सामग्री को सामान्य, पंक्ति या स्तंभ प्रदर्शन में देखें |
| **टर्बो मोड** | तेजी से निष्पादन के लिए हरी झंडी पर क्लिक करते समय Shift दबाए रखें |
| **सिंगल-स्टेप मोड** | "एकल चरण" के लिए हरे झंडे पर राइट-क्लिक करें (निष्पादन धीमा) |
### डिबगिंग पैटर्न
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

### सामान्य मुद्दे
| समस्या | कारण | समाधान |
|------|-------|-------|
| स्प्राइट प्रतिक्रिया नहीं दे रहा है | कोई इवेंट हैट ब्लॉक नहीं | "जब हरी झंडी दिखाई गई" या अन्य घटना जोड़ें |
| क्लोन काम नहीं कर रहा | क्लोन बनाया गया लेकिन दिखाया नहीं गया | "जब मैं क्लोन के रूप में प्रारंभ करूं" के बाद "शो" ब्लॉक जोड़ें |
| स्प्राइट्स के बीच साझा किया गया वेरिएबल | वैश्विक बनाम स्थानीय परिवर्तनीय भ्रम | "केवल इस स्प्राइट के लिए" विकल्प का उपयोग करें |
| प्रसारण प्राप्त नहीं हुआ | गलत संदेश का नाम | प्रसारण सत्यापित करें और प्राप्त नाम बिल्कुल मेल खाते हैं |
| अनंत लूप फ्रीज | बिना किसी प्रतीक्षा के "हमेशा के लिए" | टाइट लूप्स में छोटे "प्रतीक्षा करें" ब्लॉक जोड़ें |
---

## अंतरसंचालनीयता
### हार्डवेयर एक्सटेंशन
स्क्रैच एक्सटेंशन के माध्यम से भौतिक हार्डवेयर से जुड़ सकता है:
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

### स्क्रैच एक्सटेंशन एपीआई (कस्टम एक्सटेंशन)
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

## डिज़ाइन पैटर्न
### पैटर्न 1: प्लेटफ़ॉर्मर मूवमेंट
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

### पैटर्न 2: स्क्रॉलिंग पृष्ठभूमि
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

### पैटर्न 3: स्प्राइट फॉलोइंग (चेस एआई)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### पैटर्न 4: सूचियों के साथ इन्वेंटरी प्रणाली
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

### पैटर्न 5: क्लोन के साथ कण प्रणाली
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

## प्रदर्शन एवं अनुकूलन
### स्प्राइट अनुकूलन
| तकनीक | प्रभाव | विवरण |
|----|-------|----|
| **क्लोन न्यूनतम करें** | उच्च | प्रत्येक क्लोन मेमोरी की खपत करता है; हो जाने पर हटा दें |
| **वेशभूषा कम करें** | मध्यम | कम पोशाक स्विच का मतलब है कम ओवरहेड प्रतिपादन |
| **"स्क्रीन रिफ्रेश के बिना चलाएं" का उपयोग करें** | उच्च | स्क्रीन रिफ्रेश के बिना कस्टम ब्लॉक तेजी से चलते हैं |
| **"कहें" ब्लॉक को सीमित करें** | मध्यम | भाषण के बुलबुले ओवरहेड प्रतिपादन का कारण बनते हैं |
| **प्रत्येक स्प्राइट में "हमेशा के लिए" से बचें** | मध्यम | निरंतर मतदान के बजाय प्रसारण और घटनाओं का उपयोग करें |
### क्लोन प्रबंधन
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

### अनुकूलन चेकलिस्ट
| तकनीक | प्रभाव | विवरण |
|----|-------|----|
| **स्क्रीन रिफ्रेश किए बिना चलाएँ** | बहुत ऊँचा | कस्टम ब्लॉक गति के लिए रेंडरिंग को छोड़ देते हैं |
| **सक्रिय क्लोन को न्यूनतम करें** | उच्च | जैसे ही क्लोन की आवश्यकता न रह जाए, उन्हें हटा दें |
| **प्रसारण का संयम से उपयोग करें** | मध्यम | प्रति फ़्रेम बहुत अधिक प्रसारण अंतराल का कारण बनते हैं |
| **वेशभूषा को सरल बनाएं** | मध्यम | छोटी छवियां तेजी से प्रस्तुत होती हैं |
| **सूची संचालन कम करें** | मध्यम | प्रत्येक फ्रेम में बड़ी सूचियों को स्कैन करने से बचें |
| **"प्रतीक्षा" ब्लॉक का उपयोग करें** | निम्न | सीपीयू को हमेशा के लिए लूप में फंसाने से रोकें |
---

## परिनियोजन और वास्तविक दुनिया में उपयोग
### प्रोजेक्ट साझा करना
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

### वास्तविक-विश्व शैक्षिक उपयोग
| प्रसंग | स्क्रैच का उपयोग कैसे किया जाता है | स्केल |
|------|-------------------|-------|
| **के-12 स्कूल** | सीएस कक्षाओं में प्रोग्रामिंग का परिचय | 190+ देशों में उपयोग किया जाता है |
| **कोडिंग क्लब** | स्क्रैच क्लब / कोडरडोजो कार्यशालाएँ | दुनिया भर में 3000+ क्लब |
| **पुस्तकालय** | स्कूल के बाद के प्रोग्रामिंग कार्यक्रम | सार्वजनिक पुस्तकालय प्रणालियाँ |
| **होमस्कूलिंग** | स्व-गति वाली प्रोग्रामिंग शिक्षा | लाखों घरेलू विद्यार्थी |
| **विश्वविद्यालय CS0** | गैर-प्रमुख परिचयात्मक सीएस पाठ्यक्रम | विश्वविद्यालय ब्रिज कार्यक्रम |
| **पहुंचयोग्यता** | दृष्टिबाधितों को प्रोग्रामिंग सिखाना | स्क्रीन रीडर समर्थन |
| **थेरेपी** | संज्ञानात्मक और मोटर कौशल विकास | व्यावसायिक चिकित्सा |
### शिक्षा अनुसंधान में खरोंच
शोध से पता चला है कि स्क्रैच प्रभावी ढंग से सिखाता है:
- **अनुक्रमिक सोच**: समस्याओं को क्रमबद्ध चरणों में तोड़ना
- **डिबगिंग कौशल**: तर्क में त्रुटियों को ढूंढना और ठीक करना
- **रचनात्मक अभिव्यक्ति**: कला, संगीत और प्रोग्रामिंग का संयोजन
- **सहयोग**: दूसरों की परियोजनाओं पर रीमिक्सिंग और निर्माण
- **दृढ़ता**: परियोजनाओं को बेहतर बनाने के लिए उन पर बार-बार विचार करना
---

## खरोंच से संक्रमण
स्क्रैच सीखने के बाद, सामान्य अगले चरणों में शामिल हैं:
| अगली भाषा | क्यों |
|----|-----|
| **पायथन** | सबसे प्राकृतिक संक्रमण - पठनीय वाक्यविन्यास, समान तर्क अवधारणाएँ |
| **जावास्क्रिप्ट** | यदि वेब/गेम्स में रुचि है - तत्काल दृश्य प्रतिक्रिया |
| **लुआ (रोबोक्स/लव2डी के माध्यम से)** | यदि खेल विकास में रुचि है |
| **ऐप आविष्कारक** | एंड्रॉइड ऐप्स के लिए विज़ुअल ब्लॉक (समान एमआईटी वंशावली) |
| **ब्लॉकली** | Google की विज़ुअल प्रोग्रामिंग लाइब्रेरी (समान अवधारणाएँ) |
### कॉन्सेप्ट मैपिंग: स्क्रैच टू पायथन
| स्क्रैच संकल्पना | पायथन समतुल्य |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| फ़ंक्शन कॉल या इवेंट सिस्टम |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-अनुक्रमित!) |
| `length of [list]`| `len(list)`|
---

## स्क्रैच का उपयोग कब करें
| परिदृश्य | स्क्रैच क्यों | बेहतर विकल्प |
|---|----|-----|
| बच्चों (8-16) को कोड सिखाना | इसके लिए विशेष रूप से डिज़ाइन किया गया | — |
| कम्प्यूटेशनल सोच का परिचय | दृश्य, कोई वाक्यविन्यास त्रुटियाँ नहीं | — |
| स्कूल वर्कशॉप/कोडिंग क्लब | मुफ़्त, ब्राउज़र-आधारित, कोई सेटअप नहीं | — |
| खेल के विचारों का दृश्य रूप से प्रोटोटाइप करना | तेजी से पुनरावृत्ति | — |
| व्यावसायिक विकास | इसके लिए डिज़ाइन नहीं किया गया है | पायथन, जावास्क्रिप्ट, कोई भी टेक्स्ट भाषा |
| विश्वविद्यालय स्तरीय सीएस शिक्षा | बहुत सरल | पायथन, जावा, सी |
---

## सिंथेटिक प्रश्नोत्तर
**Q1: क्या स्क्रैच वास्तव में एक प्रोग्रामिंग भाषा है?**
A1: हां, स्क्रैच एक वास्तविक प्रोग्रामिंग भाषा है, लेकिन यह टेक्स्ट-आधारित के बजाय दृश्य है। यह सभी मूलभूत प्रोग्रामिंग अवधारणाओं का समर्थन करता है: चर, लूप, सशर्त, फ़ंक्शन (कस्टम ब्लॉक), सूचियां और इवेंट-संचालित प्रोग्रामिंग। अंतर यह है कि आप कोड टाइप करने के बजाय ब्लॉक को खींचते और छोड़ते हैं। यह सिंटैक्स त्रुटियों को दूर करता है और प्रोग्रामिंग को युवा शिक्षार्थियों के लिए सुलभ बनाता है।
**प्र2: मैं स्क्रैच में कस्टम फ़ंक्शन (कस्टम ब्लॉक) कैसे बनाऊं?**
A2: "मेरे ब्लॉक" श्रेणी पर जाएं और "एक ब्लॉक बनाएं" पर क्लिक करें। इसे एक नाम दें, यदि आवश्यक हो तो पैरामीटर जोड़ें, फिर इसके नीचे ब्लॉक जोड़कर इसके व्यवहार को परिभाषित करें। कस्टम ब्लॉक इनपुट (संख्या, स्ट्रिंग, बूलियन) ले सकते हैं और अन्य कस्टम ब्लॉक को कॉल कर सकते हैं। यह मॉड्यूलर प्रोग्रामिंग और कोड पुन: उपयोग को सक्षम बनाता है।
**Q3: स्क्रैच में जटिल गेम लॉजिक को संभालने का सबसे अच्छा तरीका क्या है?**
A3: तर्क को व्यवस्थित करने के लिए कस्टम ब्लॉक का उपयोग करें, स्प्राइट्स के बीच ईवेंट समन्वय के लिए संदेश प्रसारित करें, और गेम स्थिति (स्कोर, स्तर, इन्वेंट्री) को संग्रहीत करने के लिए सूचियों का उपयोग करें। जटिल एआई के लिए, वर्तमान स्थिति पर नज़र रखने वाले चर के साथ परिमित राज्य मशीनों का उपयोग करें। कई दुश्मनों के लिए क्लोन स्प्राइट और प्रत्येक स्वतंत्र व्यवहार देने के लिए "जब मैं क्लोन के रूप में शुरू करता हूँ" का उपयोग करें।
**प्रश्न4: मैं स्क्रैच में स्प्राइट के बीच डेटा कैसे साझा कर सकता हूं?**
A4: स्कोर या गेम स्थिति जैसे साझा डेटा के लिए वैश्विक चर ("केवल इस स्प्राइट के लिए" के बिना बनाया गया) का उपयोग करें। स्प्राइट्स में घटनाओं को ट्रिगर करने के लिए प्रसारण संदेशों का उपयोग करें। अधिक जटिल संचार के लिए, सूचियों को साझा डेटा संरचनाओं के रूप में उपयोग करें। प्रत्येक स्प्राइट समन्वय को सक्षम करते हुए वैश्विक चर और सूचियों को पढ़ और संशोधित कर सकता है।
**प्रश्न5: स्क्रैच में कुछ उन्नत तकनीकें क्या हैं?**
A5: चित्र बनाने और दृश्य प्रभाव बनाने के लिए पेन ब्लॉक का उपयोग करें। 3डी-जैसे ग्राफ़िक्स के लिए रेकास्टिंग लागू करें। मल्टीप्लेयर गेम के लिए क्लाउड वेरिएबल का उपयोग करें (स्क्रैचर स्थिति की आवश्यकता है)। यादृच्छिक संख्याओं और सूचियों के साथ प्रक्रियात्मक पीढ़ी बनाएं। पुन: प्रयोज्य एल्गोरिदम के लिए पैरामीटर के साथ कस्टम ब्लॉक का उपयोग करें। इंटरैक्टिव परियोजनाओं के लिए वीडियो सेंसिंग और ध्वनि हेरफेर के साथ प्रयोग।
---

##विचार-शृंखला
### समस्या 1: एक प्लेटफ़ॉर्मर गेम बनाना
**चरण 1: समस्या को समझें**
हमें एक प्लेटफ़ॉर्मर बनाने की ज़रूरत है जहां एक पात्र बाएं/दाएं घूम सकता है, कूद सकता है, बाधाओं से बच सकता है और आइटम एकत्र कर सकता है।
**चरण 2: दृष्टिकोण को पहचानें**
- "गिरते" चर के साथ गुरुत्वाकर्षण सिमुलेशन का उपयोग करें
- रंग या स्प्राइट स्पर्श का उपयोग करके जमीन/टक्कर का पता लगाएं
- सूचियों में स्तर का डेटा संग्रहीत करें
- जंप और मूवमेंट लॉजिक के लिए कस्टम ब्लॉक का उपयोग करें
**चरण 3: समाधान लागू करें**```scratch
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

**चरण 4: सत्यापित करें और अनुकूलित करें**
विभिन्न प्लेटफार्मों पर कूदने का परीक्षण करें। अच्छे खेल अनुभव के लिए गुरुत्वाकर्षण और छलांग की ऊँचाई को समायोजित करें। दौड़ने और कूदने के लिए एनिमेशन जोड़ें। प्रसारण संदेशों का उपयोग करके चौकियों को लागू करें।
---

### समस्या 2: स्कोर ट्रैकिंग के साथ एक क्विज़ गेम बनाना
**चरण 1: समस्या को समझें**
एक क्विज़ गेम बनाएं जो प्रश्न पूछता है, उत्तरों की जाँच करता है और खिलाड़ी के स्कोर को ट्रैक करता है।
**चरण 2: दृष्टिकोण को पहचानें**
- प्रश्नों और उत्तरों को समानांतर सूचियों में संग्रहित करें
- प्रगति पर नज़र रखने के लिए प्रश्न काउंटर का उपयोग करें
- इनपुट के लिए "पूछें और प्रतीक्षा करें" ब्लॉक का उपयोग करें
- उत्तरों की तुलना करें और स्कोर अपडेट करें
**चरण 3: समाधान लागू करें**```scratch
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

**चरण 4: सत्यापित करें और अनुकूलित करें**
किनारे के मामलों सहित विभिन्न उत्तरों के साथ परीक्षण करें। ग़लत उत्तरों के लिए फ़ीडबैक जोड़ें. पुनः प्रयास विकल्प लागू करें. सही/गलत उत्तरों के लिए ध्वनि प्रभाव और दृश्य प्रतिक्रिया जोड़ें।
---

### समस्या 3: पेन से फ्रैक्टल ट्री बनाना
**चरण 1: समस्या को समझें**
पेन एक्सटेंशन का उपयोग करके एक पुनरावर्ती फ्रैक्टल ट्री बनाएं।
**चरण 2: दृष्टिकोण को पहचानें**
- शाखाएँ खींचने के लिए प्रत्यावर्तन का उपयोग करें
- प्रत्येक शाखा दो छोटी शाखाओं में विभाजित हो जाती है
- प्राकृतिक भिन्नता के लिए यादृच्छिक कोणों का उपयोग करें
- प्रत्येक रिकर्सन स्तर के साथ शाखा की लंबाई और कमी को ट्रैक करें
**चरण 3: समाधान लागू करें**```scratch
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

**चरण 4: सत्यापित करें और अनुकूलित करें**
सौंदर्यपूर्ण पेड़ों के लिए शाखा की लंबाई सीमा और कोण सीमा को समायोजित करें। रंग परिवर्तन का उपयोग करके शाखा के सिरों पर पत्तियाँ जोड़ें। विभिन्न वृक्ष शैलियाँ लागू करें. चित्रों को छवियों के रूप में सहेजें।
---

## सारांश
स्क्रैच पारंपरिक अर्थों में एक प्रोग्रामिंग भाषा नहीं है - यह एक सीखने का माहौल है। इसकी प्रतिभा एक बच्चे और कुछ इंटरैक्टिव बनाने की खुशी के बीच की हर बाधा को दूर कर रही है। वाक्यविन्यास के बजाय अवधारणाओं पर ध्यान केंद्रित करके, स्क्रैच प्रोग्रामिंग के बुनियादी सिद्धांतों को सिखाता है जो किसी भी भाषा में स्थानांतरित हो जाते हैं। युवा शिक्षार्थियों को प्रोग्रामिंग शुरू करने के लिए, स्क्रैच स्वर्ण मानक है।