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

# سکریچ
سکریچ ایک بصری، بلاک پر مبنی پروگرامنگ لینگویج ہے جسے MIT میڈیا لیب نے تیار کیا تھا اور اسے پہلی بار 2007 میں ریلیز کیا گیا تھا۔ متن پر مبنی کوڈ لکھنے کے بجائے، صارف پروگرام بنانے کے لیے رنگین بلاکس کو اکٹھا کرتے ہیں۔ سکریچ خاص طور پر 8-16 سال کی عمر کے بچوں کے لیے ڈیزائن کیا گیا ہے (حالانکہ ہر عمر کے سیکھنے والے اسے استعمال کرتے ہیں) بنیادی پروگرامنگ کے تصورات — لوپس، کنڈیشنلز، متغیرات، ایونٹس اور فنکشنز — بغیر نحوی غلطیوں کی رکاوٹ کے۔
سکریچ دنیا میں سب سے زیادہ استعمال ہونے والی تعارفی پروگرامنگ زبان ہے، جس میں 100 ملین سے زیادہ رجسٹرڈ صارفین اور 70+ زبانوں میں دستیابی ہے۔ یہ ایک ویب براؤزر میں چلتا ہے اور مفت ہے۔
---

## سکریچ کیوں اہم ہے۔
- **پروگرامنگ کا بہترین تعارف**: نحوی رکاوٹوں کو مکمل طور پر ہٹاتا ہے۔ تصورات بصری ہیرا پھیری کے ذریعے سکھائے جاتے ہیں۔
- **کمپیوٹیشنل سوچ**: سڑنے، پیٹرن کی شناخت، تجرید، اور الگورتھم ڈیزائن سکھاتی ہے۔
- **تخلیق پر مبنی**: بچے گیمز، اینیمیشنز، کہانیاں، اور موسیقی بناتے ہیں — پروگرامنگ سیکھنا ان چیزوں کو بنانے کے ضمنی پروڈکٹ کے طور پر جن کا وہ خیال رکھتے ہیں۔
- **عالمی رسائی**: دنیا بھر کے اسکولوں میں استعمال کیا جاتا ہے۔ 70+ زبانوں میں دستیاب ہے۔ مفت اور براؤزر پر مبنی۔
- **کمیونٹی**: سکریچ آن لائن کمیونٹی اشتراک کرنا، دوبارہ مکس کرنا، اور باہمی تعاون سے سیکھنا سکھاتی ہے۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **"اصلی" پروگرامنگ زبان نہیں** | پروڈکشن سافٹ ویئر، APIs، یا سسٹمز نہیں بنا سکتے | ازگر، جاوا اسکرپٹ، یا متن پر مبنی زبانوں میں منتقلی |
| **محدود صلاحیتیں** | کوئی فائل I/O، نیٹ ورکنگ، یا جدید ڈیٹا سٹرکچر نہیں | سیکھنے کے لیے استعمال کریں؛ اصلی پروجیکٹس کے لیے ٹیکسٹ لینگوئجز پر جائیں |
| **کارکردگی** | تشریح شدہ، پیچیدہ منصوبوں کے لیے سست | کارکردگی کے اہم کام کے لیے ڈیزائن نہیں کیا گیا |
| **عمر کا ادراک** | اکثر "صرف بچوں کے لیے" کے طور پر دیکھا جاتا ہے۔ سکریچ ایک سیکھنے کا آلہ ہے، پیشہ ورانہ زبان نہیں۔
---

## سکریچ کیسے کام کرتا ہے۔
سکریچ پروگرامز (جسے "پروجیکٹ" کہا جاتا ہے) **اسپرائٹس** (کردار/آبجیکٹ) پر مشتمل ہوتا ہے جو اسکرپٹ میں ایک ساتھ **بلاکس** کا جواب دیتے ہیں۔
### بنیادی تصورات (بلاک کے ذریعے سکھائے گئے)
| تصور | سکریچ بلاک کیٹیگری | مثال |
|---------|-------------------------|---------|
| **سلسلہ** | حرکت، لگ رہا ہے | "10 قدم بڑھائیں" پھر "ہیلو کہو" |
| **لوپس** | کنٹرول (پیلا) | "10 کو دہرائیں"، "ہمیشہ"، "جب تک دہرائیں" |
| **مشروط** | کنٹرول (پیلا) | "اگر... پھر"، "اگر... تو... اور" |
| **متغیرات** | متغیرات (سنتری) | "اسکور کو 0 پر سیٹ کریں"، "اسکور کو 1 سے تبدیل کریں" |
| **واقعات** | واقعات (پیلا) | "جب سبز پرچم پر کلک کیا گیا"، "جب کلید دبائی گئی" |
| **فنکشنز** | میرے بلاکس (اپنی مرضی کے مطابق) | دوبارہ قابل استعمال بلاک کی ترتیب کی وضاحت کریں |
| **فہرستیں (ارے)** | متغیرات (سنتری) | "فہرست میں شامل کریں"، "فہرست کی شے" |
| **براڈکاسٹنگ** | واقعات | sprites کے درمیان پیغامات بھیجیں |
### مثال: سادہ گیم منطق
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

## اعلی درجے کی نحو اور نمونے۔
### تفصیل سے زمرہ جات کو بلاک کریں۔
سکریچ 3.0 بلاکس کو رنگین کوڈ شدہ زمروں میں ترتیب دیتا ہے:
| زمرہ | رنگ | بلاک کی اقسام |
|------------|---------|---------------|
| **حرکت** | بلیو | حرکت، موڑ، گوٹو، گلائیڈ، پوائنٹ، تبدیلی x/y |
| **دیکھتا ہے** | جامنی | کہو، سوچو، لباس بدلو، سائز تبدیل کرو، دکھائیں/چھپائیں |
| **آواز** | گلابی | آواز چلائیں، آوازیں بند کریں، والیوم تبدیل کریں، پچ تبدیل کریں |
| **واقعات** | پیلا | جب پرچم پر کلک کیا گیا، جب کلید دبائی گئی، جب اسپرائٹ پر کلک کیا گیا، براڈکاسٹ |
| **کنٹرول** | گولڈ | انتظار کریں، دہرائیں، ہمیشہ کے لیے، اگر، اگر-اور، دہرائیں جب تک، رکیں |
| **حساس** | ہلکا نیلا | چھونا، کلید دبانا، ماؤس، فاصلہ، پوچھنا/جواب، ٹائمر |
| **آپریٹرز** | سبز | ریاضی کے آپریشنز، ٹیکسٹ آپس، موازنہ، اور/یا/نہیں، بے ترتیب |
| **متغیرات** | اورنج | متغیر سیٹ/تبدیل کریں، فہرست آپریشنز |
| **میرے بلاکس** | گہرا سرخ | اپنی مرضی کے مطابق بلاک کی تعریفیں (فنکشنز) |
### ایڈوانسڈ بلاک پیٹرنز
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

### حسب ضرورت بلاکس (فنکشنز)
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

### لسٹ آپریشنز (ایرے)
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

### براڈکاسٹنگ (انٹر سپرائٹ کمیونیکیشن)
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

## آرکیٹیکچر اور سسٹم ڈیزائن
### ایونٹ سے چلنے والا ڈیزائن
سکریچ ایونٹ پر مبنی فن تعمیر کا استعمال کرتا ہے۔ ہر اسکرپٹ ایونٹ بلاک (ہیٹ بلاک) سے شروع ہوتا ہے اور اس ایونٹ کے جواب میں چلتا ہے۔
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

### پروجیکٹ کا ڈھانچہ
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

### کلون سسٹم (آبجیکٹ تخلیق)
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### سکریچ ایکسٹینشنز
سکریچ آفیشل اور کمیونٹی ایکسٹینشنز کو سپورٹ کرتا ہے جو صلاحیتوں کو شامل کرتی ہے:
| توسیع | مقصد |
|------------|---------|
| **قلم** | اسٹیج پر لکیریں اور شکلیں بنائیں |
| **ویڈیو سینسنگ** | حرکت کا پتہ لگانے کے لیے ویب کیم استعمال کریں۔
| **متن سے تقریر** | متن کو بولی ہوئی آڈیو میں تبدیل کریں۔
| **ترجمہ** | زبانوں کے درمیان متن کا ترجمہ کریں |
| **مکی مکی** | جسمانی اشیاء کو بطور ان پٹ جوڑیں |
| **مائیکرو: بٹ** | بی بی سی مائیکرو: بٹ ہارڈ ویئر سے جڑیں |
| **LEGO Mindstorms** | کنٹرول لیگو روبوٹ |
| **موسیقی** | موسیقی کے نوٹ اور آلات بجائیں |
### سکریچ فائل فارمیٹ
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

### آف لائن ایڈیٹر
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

## ٹیسٹنگ اور ڈیبگنگ
### بلٹ ان ڈیبگنگ ٹولز
سکریچ ڈیبگنگ پروجیکٹس کے لیے کئی بلٹ ان ٹولز فراہم کرتا ہے:
| ٹول | استعمال کرنے کا طریقہ |
|------|------------|
| **ٹرٹل موڈ** | اسپرائٹ پر دائیں کلک کریں اور کوآرڈینیٹ دیکھنے کے لیے "شو ڈیبگ" کو منتخب کریں۔
| **متغیر مانیٹر** | کسی متغیر پر دائیں کلک کریں اور اس کی قدر کو حقیقی وقت میں دیکھنے کے لیے "شو" کو منتخب کریں۔
| **فہرست مانیٹر** | فہرست کے مواد کو عام، قطار، یا کالم ڈسپلے میں دیکھیں |
| **ٹربو موڈ** | تیزی سے عمل درآمد کے لیے سبز پرچم پر کلک کرتے ہوئے شفٹ کو دبائے رکھیں |
| **ایک قدمی موڈ** | "سنگل سٹیپ" کے لیے سبز جھنڈے پر دائیں کلک کریں (عمل کو سست کر دیتا ہے) |
### ڈیبگنگ پیٹرنز
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

### مشترکہ مسائل
| مسئلہ | وجہ | حل |
|---------|------|---------|
| سپرائٹ جواب نہیں دے رہا ہے | کوئی ایونٹ ہیٹ بلاک نہیں | "جب سبز پرچم پر کلک کیا گیا" یا دیگر ایونٹ شامل کریں۔
| کلون کام نہیں کر رہا | کلون بنایا لیکن نہیں دکھایا گیا | "جب میں کلون کے طور پر شروع کرتا ہوں" کے بعد "شو" بلاک شامل کریں۔
| متغیر sprites کے درمیان مشترکہ | عالمی بمقابلہ مقامی متغیر کنفیوژن | "صرف اس سپرائٹ کے لیے" اختیار استعمال کریں۔
| براڈکاسٹ موصول نہیں ہوا | غلط پیغام نام | براڈکاسٹ کی توثیق کریں اور وصول کریں نام بالکل مماثل ہیں۔
| لامحدود لوپ منجمد | "ہمیشہ" بغیر انتظار کے | تنگ لوپس میں چھوٹے "انتظار" بلاکس شامل کریں |
---

## انٹرآپریبلٹی
### ہارڈ ویئر ایکسٹینشنز
سکریچ ایکسٹینشن کے ذریعے فزیکل ہارڈویئر سے منسلک ہو سکتا ہے:
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

### سکریچ ایکسٹینشن API (کسٹم ایکسٹینشنز)
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

## ڈیزائن پیٹرن
### پیٹرن 1: پلیٹ فارمر موومنٹ
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

### پیٹرن 2: اسکرولنگ بیک گراؤنڈ
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

### پیٹرن 3: اسپرائٹ فالونگ (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### پیٹرن 4: فہرستوں کے ساتھ انوینٹری سسٹم
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

### پیٹرن 5: کلون کے ساتھ پارٹیکل سسٹم
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

## کارکردگی اور اصلاح
### سپرائٹ آپٹیمائزیشن
| تکنیک | اثر | تفصیل |
|------------|---------|------------|
| **کلون کو کم سے کم کریں** | ہائی | ہر کلون میموری استعمال کرتا ہے۔ مکمل ہونے پر حذف کریں |
| **ملبوسات کو کم کریں** | میڈیم | کم ملبوسات کے سوئچ کا مطلب ہے کم رینڈرنگ اوور ہیڈ |
| ** استعمال کریں "اسکرین ریفریش کے بغیر چلائیں"** | ہائی | اسکرین ریفریش کے بغیر اپنی مرضی کے بلاکس تیزی سے چلتے ہیں |
| ** "کہنے" بلاکس کو محدود کریں** | میڈیم | تقریر کے بلبلوں کی وجہ سے اوور ہیڈ |
| **ہر اسپرائٹ میں "ہمیشہ" سے بچیں** | میڈیم | مسلسل پولنگ کے بجائے نشریات اور واقعات کا استعمال کریں |
### کلون مینجمنٹ
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

### آپٹیمائزیشن چیک لسٹ
| تکنیک | اثر | تفصیل |
|------------|---------|------------|
| **اسکرین ریفریش کے بغیر چلائیں** | بہت اعلیٰ | اپنی مرضی کے بلاکس رفتار کے لیے رینڈرنگ کو چھوڑ دیتے ہیں |
| **ایکٹو کلون کو کم سے کم کریں** | ہائی | کلون جیسے ہی ان کی مزید ضرورت نہیں ہے حذف کریں |
| **براڈکاسٹ کا استعمال کفایت سے کریں** | میڈیم | بہت زیادہ نشریات فی فریم وقفہ کا سبب بنتی ہیں۔
| **ملبوسات کو آسان بنائیں** | میڈیم | چھوٹی تصاویر تیزی سے پیش کرتی ہیں |
| ** فہرست کی کارروائیوں کو کم کریں** | میڈیم | ہر فریم میں بڑی فہرستوں کو اسکین کرنے سے گریز کریں۔
| **"انتظار" بلاکس کا استعمال کریں** | کم | ہمیشہ کے لیے لوپس میں سی پی یو ہاگنگ کو روکیں |
---

## تعیناتی اور حقیقی دنیا کا استعمال
### شیئرنگ پروجیکٹس
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

### حقیقی دنیا کا تعلیمی استعمال
| سیاق و سباق | سکریچ کا استعمال کیسے کیا جاتا ہے | پیمانہ |
|---------|----------------------|------|
| **K-12 اسکول** | CS کلاسز میں پروگرامنگ کا تعارف | 190+ ممالک میں استعمال کیا جاتا ہے |
| **کوڈنگ کلب** | سکریچ کلب / کوڈر ڈوجو ورکشاپس | دنیا بھر میں 3000+ کلب |
| **لائبریریاں** | اسکول کے بعد پروگرامنگ پروگرامز | پبلک لائبریری سسٹمز |
| **ہوم اسکولنگ** | خود رفتار پروگرامنگ کی تعلیم | لاکھوں گھریلو سیکھنے والے |
| **یونیورسٹی CS0** | غیر اہم تعارفی CS کورسز | یونیورسٹی پل پروگرامز |
| **رسائی** | نابینا افراد کو پروگرامنگ سکھانا | سکرین ریڈر سپورٹ |
| **تھراپی** | علمی اور موٹر مہارت کی ترقی | پیشہ ورانہ تھراپی |
### تعلیمی تحقیق میں خراش
تحقیق سے پتہ چلتا ہے کہ سکریچ مؤثر طریقے سے سکھاتا ہے:
- **تسلسلاتی سوچ**: مسائل کو ترتیب شدہ مراحل میں توڑنا
- **ڈیبگنگ کی مہارتیں**: منطق میں غلطیوں کو تلاش کرنا اور ٹھیک کرنا
- **تخلیقی اظہار**: آرٹ، موسیقی اور پروگرامنگ کا امتزاج
- **تعاون**: دوسروں کے پروجیکٹس کو دوبارہ مکس کرنا اور ان پر تعمیر کرنا
- **استقامت**: منصوبوں کو بہتر بنانے کے لیے اعادہ کرنا
---

## شروع سے منتقلی
سکریچ سیکھنے کے بعد، عام اگلے مراحل میں شامل ہیں:
| اگلی زبان | کیوں |
|---------------|------|
| **ازگر** | زیادہ تر قدرتی منتقلی — پڑھنے کے قابل نحو، اسی طرح کے منطقی تصورات |
| **جاوا اسکرپٹ** | اگر ویب/گیمز میں دلچسپی ہے — فوری بصری تاثرات |
| **لوا (روبلوکس/لوو 2 ڈی کے ذریعے)** | اگر گیم ڈویلپمنٹ میں دلچسپی ہے |
| **ایپ موجد** | اینڈرائیڈ ایپس کے لیے بصری بلاکس (ایک ہی MIT نسب) |
| **بلاک طور پر** | گوگل کی بصری پروگرامنگ لائبریری (اسی طرح کے تصورات) |
### تصور کی نقشہ سازی: ازگر کو سکریچ کریں۔
| سکریچ تصور | ازگر کے برابر |
|----------------------------------------------------------------
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| فنکشن کال یا ایونٹ سسٹم |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-انڈیکسڈ!) |
| `length of [list]`| `len(list)`|
---

## سکریچ کب استعمال کریں۔
| منظر نامہ | کیوں سکریچ | بہتر متبادل |
|------------|------------|-------------------|
| بچوں (8-16) کو کوڈ سکھانا | اس کے لیے خاص طور پر ڈیزائن کیا گیا ہے | - |
| کمپیوٹیشنل سوچ کا تعارف | بصری، کوئی نحوی غلطیاں نہیں | - |
| اسکول ورکشاپس / کوڈنگ کلب | مفت، براؤزر پر مبنی، کوئی سیٹ اپ نہیں | - |
| پروٹو ٹائپنگ گیم آئیڈیاز ضعف | تیز تکرار | - |
| پیشہ ورانہ ترقی | اس کے لیے ڈیزائن نہیں کیا گیا | ازگر، جاوا اسکرپٹ، کوئی بھی ٹیکسٹ لینگوئج |
| یونیورسٹی کی سطح کی CS تعلیم | بہت سادہ | ازگر، جاوا، سی |
---

## مصنوعی سوال و جواب
**Q1: کیا سکریچ واقعی ایک پروگرامنگ زبان ہے؟**
A1: جی ہاں، سکریچ ایک حقیقی پروگرامنگ لینگویج ہے، لیکن یہ ٹیکسٹ بیسڈ کے بجائے بصری ہے۔ یہ پروگرامنگ کے تمام بنیادی تصورات کی حمایت کرتا ہے: متغیرات، لوپس، کنڈیشنلز، فنکشنز (کسٹم بلاکس)، فہرستیں، اور ایونٹ پر مبنی پروگرامنگ۔ فرق یہ ہے کہ آپ کوڈ ٹائپ کرنے کے بجائے بلاکس کو گھسیٹتے اور چھوڑتے ہیں۔ یہ نحو کی غلطیوں کو ختم کرتا ہے اور پروگرامنگ کو نوجوان سیکھنے والوں کے لیے قابل رسائی بناتا ہے۔
**Q2: میں سکریچ میں کسٹم فنکشنز (کسٹم بلاکس) کیسے بناؤں؟**
A2: "میرے بلاکس" کے زمرے میں جائیں اور "ایک بلاک بنائیں" پر کلک کریں۔ اسے ایک نام دیں، اگر ضرورت ہو تو پیرامیٹرز شامل کریں، پھر اس کے نیچے بلاکس شامل کرکے اس کے رویے کی وضاحت کریں۔ کسٹم بلاکس ان پٹ لے سکتے ہیں (نمبر، تار، بولین) اور دوسرے کسٹم بلاکس کو کال کرسکتے ہیں۔ یہ ماڈیولر پروگرامنگ اور کوڈ کو دوبارہ استعمال کرنے کے قابل بناتا ہے۔
**Q3: سکریچ میں پیچیدہ گیم منطق کو سنبھالنے کا بہترین طریقہ کیا ہے؟**
A3: منطق کو ترتیب دینے کے لیے حسب ضرورت بلاکس کا استعمال کریں، اسپرائٹس کے درمیان ایونٹ کوآرڈینیشن کے لیے پیغامات نشر کریں، اور گیم اسٹیٹ (اسکور، لیول، انوینٹری) کو ذخیرہ کرنے کے لیے فہرستیں استعمال کریں۔ پیچیدہ AI کے لیے، موجودہ حالت کو ٹریک کرنے والے متغیر کے ساتھ محدود ریاستی مشینیں استعمال کریں۔ ایک سے زیادہ دشمنوں کے لیے کلون اسپرائٹس اور ہر ایک کو آزاد رویہ دینے کے لیے "جب میں بطور کلون شروع کرتا ہوں" کا استعمال کریں۔
**Q4: میں سکریچ میں اسپرائٹس کے درمیان ڈیٹا کا اشتراک کیسے کرسکتا ہوں؟**
A4: اسکور یا گیم اسٹیٹ جیسے مشترکہ ڈیٹا کے لیے عالمی متغیرات ("صرف اس سپرائٹ کے لیے" کے بغیر تخلیق کردہ) استعمال کریں۔ اسپرائٹس میں واقعات کو متحرک کرنے کے لیے براڈکاسٹ پیغامات کا استعمال کریں۔ مزید پیچیدہ مواصلات کے لیے، فہرستوں کو مشترکہ ڈیٹا ڈھانچے کے طور پر استعمال کریں۔ ہر اسپرائٹ عالمی متغیرات اور فہرستوں کو پڑھ اور ان میں ترمیم کر سکتا ہے، جس سے ہم آہنگی کو فعال کیا جا سکتا ہے۔
**Q5: سکریچ میں کچھ جدید تکنیکیں کیا ہیں؟**
A5: ڈرائنگ اور بصری اثرات بنانے کے لیے پین بلاکس کا استعمال کریں۔ 3D جیسے گرافکس کے لیے raycasting لاگو کریں۔ ملٹی پلیئر گیمز کے لیے کلاؤڈ متغیرات کا استعمال کریں (اسکریچر کی حیثیت کی ضرورت ہے)۔ بے ترتیب نمبروں اور فہرستوں کے ساتھ طریقہ کار کی نسل بنائیں۔ دوبارہ قابل استعمال الگورتھم کے لیے پیرامیٹرز کے ساتھ حسب ضرورت بلاکس کا استعمال کریں۔ انٹرایکٹو پروجیکٹس کے لیے ویڈیو سینسنگ اور صوتی ہیرا پھیری کے ساتھ تجربہ کریں۔
---

## سوچ کا سلسلہ
### مسئلہ 1: پلیٹ فارمر گیم بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
ہمیں ایک پلیٹ فارمر بنانے کی ضرورت ہے جہاں ایک کردار بائیں/دائیں حرکت کر سکے، چھلانگ لگا سکے، رکاوٹوں سے بچ سکے اور اشیاء جمع کر سکے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
- ایک "گرنے والے" متغیر کے ساتھ کشش ثقل کا تخروپن استعمال کریں۔
- رنگ یا اسپرائٹ کو چھونے کا استعمال کرتے ہوئے زمین / تصادم کا پتہ لگائیں۔
- فہرستوں میں سطح کا ڈیٹا اسٹور کریں۔
- چھلانگ اور حرکت کی منطق کے لئے کسٹم بلاکس کا استعمال کریں۔
**مرحلہ 3: حل کو نافذ کریں**```scratch
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

**مرحلہ 4: تصدیق کریں اور بہتر بنائیں**
مختلف پلیٹ فارمز پر ٹیسٹ جمپنگ۔ اچھے کھیل کے احساس کے لیے کشش ثقل کو ایڈجسٹ کریں اور اونچائی کودیں۔ دوڑنے اور چھلانگ لگانے کے لیے متحرک تصاویر شامل کریں۔ نشریاتی پیغامات کا استعمال کرتے ہوئے چوکیوں کو نافذ کریں۔
---

### مسئلہ 2: اسکور ٹریکنگ کے ساتھ کوئز گیم بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
ایک کوئز گیم بنائیں جو سوالات پوچھے، جوابات کی جانچ کرے اور کھلاڑی کے اسکور کو ٹریک کرے۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
- متوازی فہرستوں میں سوالات اور جوابات کو اسٹور کریں۔
- پیشرفت کو ٹریک کرنے کے لیے سوال کا کاؤنٹر استعمال کریں۔
- ان پٹ کے لیے "پوچھیں اور انتظار کریں" بلاکس کا استعمال کریں۔
- جوابات کا موازنہ کریں اور اسکور کو اپ ڈیٹ کریں۔
**مرحلہ 3: حل کو نافذ کریں**```scratch
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

**مرحلہ 4: تصدیق کریں اور بہتر بنائیں**
ایج کیسز سمیت مختلف جوابات کے ساتھ ٹیسٹ کریں۔ غلط جوابات کے لیے تاثرات شامل کریں۔ دوبارہ کوشش کرنے کا اختیار نافذ کریں۔ صحیح/غلط جوابات کے لیے صوتی اثرات اور بصری تاثرات شامل کریں۔
---

### مسئلہ 3: قلم کے ساتھ فریکٹل ٹری کھینچنا
**مرحلہ 1: مسئلہ کو سمجھیں**
قلم کی توسیع کا استعمال کرتے ہوئے ایک تکراری فریکٹل ٹری بنائیں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
- شاخیں کھینچنے کے لیے تکرار کا استعمال کریں۔
- ہر شاخ دو چھوٹی شاخوں میں تقسیم ہوتی ہے۔
- قدرتی تغیرات کے لیے بے ترتیب زاویوں کا استعمال کریں۔
- ہر تکرار کی سطح کے ساتھ شاخ کی لمبائی اور کمی کو ٹریک کریں۔
**مرحلہ 3: حل کو نافذ کریں**```scratch
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

**مرحلہ 4: تصدیق کریں اور بہتر بنائیں**
جمالیاتی درختوں کے لیے شاخ کی لمبائی کی حد اور زاویہ کی حدود کو ایڈجسٹ کریں۔ رنگ کی تبدیلیوں کا استعمال کرتے ہوئے شاخ کے سروں پر پتے شامل کریں۔ درختوں کے مختلف انداز کو لاگو کریں۔ ڈرائنگ کو بطور تصویر محفوظ کریں۔
---

## خلاصہ
روایتی معنوں میں سکریچ ایک پروگرامنگ زبان نہیں ہے - یہ ایک سیکھنے کا ماحول ہے۔ اس کی ذہانت ایک بچے اور انٹرایکٹو کچھ تخلیق کرنے کی خوشی کے درمیان ہر رکاوٹ کو دور کر رہی ہے۔ نحو کی بجائے تصورات پر توجہ مرکوز کرکے، سکریچ پروگرامنگ کے بنیادی اصول سکھاتا ہے جو کسی بھی زبان میں منتقل ہوتے ہیں۔ نوجوان سیکھنے والوں کے لیے پروگرامنگ متعارف کرانے کے لیے، سکریچ سونے کا معیار ہے۔