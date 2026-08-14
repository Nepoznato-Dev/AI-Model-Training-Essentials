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
# يخدش
سكراتش هي لغة برمجة مرئية تعتمد على الكتل، تم تطويرها بواسطة مختبر الوسائط في معهد ماساتشوستس للتكنولوجيا وتم إصدارها لأول مرة في عام 2007. وبدلاً من كتابة التعليمات البرمجية المستندة إلى النص، يقوم المستخدمون بتجميع الكتل الملونة معًا لإنشاء البرامج. تم تصميم Scratch خصيصًا للأطفال الذين تتراوح أعمارهم بين 8 و16 عامًا (على الرغم من أن المتعلمين من جميع الأعمار يستخدمونه) لتعليم مفاهيم البرمجة الأساسية - الحلقات والشروط والمتغيرات والأحداث والوظائف - دون حاجز الأخطاء النحوية.
Scratch هي لغة البرمجة التمهيدية الأكثر استخدامًا في العالم، مع أكثر من 100 مليون مستخدم مسجل ومتوفرة بأكثر من 70 لغة. يتم تشغيله في متصفح الويب وهو مجاني.
---

## لماذا يعتبر الخدش مهمًا؟
- **أفضل مقدمة للبرمجة**: تزيل الحواجز النحوية تمامًا. يتم تدريس المفاهيم من خلال التلاعب البصري.
- **التفكير الحسابي**: يعلم التحليل والتعرف على الأنماط والتجريد وتصميم الخوارزميات.
- **يعتمد على الإبداع**: ينشئ الأطفال الألعاب والرسوم المتحركة والقصص والموسيقى، ويتعلمون البرمجة كنتيجة ثانوية لصنع الأشياء التي يهتمون بها.
- **الوصول العالمي**: يُستخدم في المدارس في جميع أنحاء العالم. متوفر بأكثر من 70 لغة. مجاني وقائم على المتصفح.
- **المجتمع**: يقوم مجتمع Scratch عبر الإنترنت بتعليم المشاركة وإعادة المزج والتعلم التعاوني.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| ** ليست لغة برمجة "حقيقية"** | لا يمكن إنشاء برامج إنتاج أو واجهات برمجة التطبيقات أو الأنظمة | الانتقال إلى Python أو JavaScript أو اللغات النصية |
| **إمكانيات محدودة** | لا يوجد إدخال/إخراج للملفات، أو شبكات، أو هياكل بيانات متقدمة | استخدام للتعلم. الانتقال إلى اللغات النصية للمشاريع الحقيقية |
| **الأداء** | تفسير بطيء للمشاريع المعقدة | غير مصمم للأعمال ذات الأداء الحرج |
| **إدراك العمر** | غالبًا ما يُنظر إليه على أنه "للأطفال فقط" | سكراتش أداة تعليمية وليست لغة احترافية |
---

## كيف يعمل برنامج سكراتش
تتكون برامج Scratch (وتسمى "المشاريع") من **العفاريت** (الأحرف/الكائنات) التي تستجيب **للكتل** المجمعة معًا في البرامج النصية.
### المفاهيم الأساسية (يتم تدريسها من خلال الكتل)
| المفهوم | فئة كتلة الصفر | مثال |
|---------|----------------------|---------|
| **التسلسلات** | الحركة، النظرات | "تحرك 10 خطوات" ثم "قل مرحبًا" |
| **الحلقات** | التحكم (أصفر) | "كرر 10"، "للأبد"، "كرر حتى" |
| **الشروط** | التحكم (أصفر) | "إذا...فإذا...فإذا...وإلا" |
| **المتغيرات** | المتغيرات (برتقالي) | "اضبط النتيجة على 0"، "قم بتغيير النتيجة بمقدار 1" |
| **الأحداث** | الأحداث (أصفر) | "عند النقر على العلم الأخضر"، "عند الضغط على المفتاح" |
| **الوظائف** | كتلتي (مخصصة) | تحديد تسلسلات الكتلة القابلة لإعادة الاستخدام |
| **القوائم (المصفوفات)** | المتغيرات (برتقالي) | "أضف إلى القائمة"، "عنصر القائمة" |
| **الإذاعة** | أحداث | إرسال رسائل بين النقوش المتحركة |
### مثال: منطق اللعبة البسيط
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

## بناء الجملة والأنماط المتقدمة
### حظر الفئات بالتفصيل
يقوم Scratch 3.0 بتنظيم الكتل في فئات مرمزة بالألوان:
| الفئة | اللون | أنواع الكتل |
|----------|-------|-------------|
| **الحركة** | أزرق | تحرك، استدر، انتقل، انزلق، أشر، غيّر x/y |
| **المظهر** | أرجواني | قل، فكر، غيّر المظهر، غيّر الحجم، أظهر/أخفي |
| **الصوت** | وردي | تشغيل الصوت، إيقاف الأصوات، تغيير مستوى الصوت، تغيير درجة الصوت |
| **الأحداث** | أصفر | عند النقر على العلم، عند الضغط على المفتاح، عند النقر على الكائن، يتم بث |
| **التحكم** | الذهب | انتظر، كرر، إلى الأبد، إذا، إذا كان الأمر كذلك، كرر حتى، توقف |
| **الاستشعار** | أزرق فاتح | اللمس، الضغط على المفتاح، الماوس، المسافة، السؤال/الإجابة، المؤقت |
| **المشغلين** | أخضر | العمليات الحسابية، العمليات النصية، المقارنة، و/أو/لا، عشوائي |
| **المتغيرات** | برتقالي | ضبط/تغيير متغير، قائمة العمليات |
| ** كتلتي ** | احمر غامق | تعريفات الكتلة المخصصة (الوظائف) |
### أنماط الكتلة المتقدمة
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

### الكتل المخصصة (الوظائف)
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

### عمليات القائمة (المصفوفات)
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

### البث (الاتصال بين الكائنات الحية)
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

## الهندسة المعمارية وتصميم النظام
### تصميم يحركه الحدث
يستخدم Scratch بنية تعتمد على الأحداث. يبدأ كل برنامج نصي بكتلة حدث (كتلة القبعة) ويتم تشغيله استجابة لهذا الحدث.
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

### هيكل المشروع
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

### نظام الاستنساخ (إنشاء الكائن)
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

## تكوين المشروع ونظام البناء
### ملحقات الصفر
يدعم Scratch الامتدادات الرسمية والمجتمعية التي تضيف إمكانيات:
| ملحق | الغرض |
|-----------|--------|
| **القلم** | رسم الخطوط والأشكال على المسرح |
| **استشعار الفيديو** | استخدم كاميرا الويب لاكتشاف الحركة |
| ** تحويل النص إلى كلام ** | تحويل النص إلى صوت منطوق |
| **ترجمة** | ترجمة النص بين اللغات |
| **ماكي ماكي** | قم بتوصيل الأشياء المادية كمدخل |
| **مايكرو:بت** | توصيل بي بي سي مايكرو: أجهزة بت |
| ** ليغو مايندستورمز ** | التحكم في روبوتات ليغو |
| **موسيقى** | عزف النوتات والآلات الموسيقية |
### تنسيق ملف سكراتش
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

### محرر غير متصل
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

## الاختبار والتصحيح
### أدوات التصحيح المضمنة
يوفر Scratch العديد من الأدوات المضمنة لتصحيح الأخطاء في المشاريع:
| أداة | كيفية الاستخدام |
|------|-----------|
| **وضع السلحفاة** | انقر بزر الماوس الأيمن فوق كائن وحدد "إظهار التصحيح" لرؤية الإحداثيات |
| **شاشات متغيرة** | انقر بزر الماوس الأيمن فوق متغير وحدد "إظهار" لرؤية قيمته في الوقت الفعلي |
| ** قائمة المراقبين ** | عرض محتويات القائمة بطريقة العرض العادية أو الصف أو العمود |
| **وضع التربو** | اضغط مع الاستمرار على Shift أثناء النقر على العلم الأخضر لتنفيذ أسرع |
| **وضع الخطوة الواحدة** | انقر بزر الماوس الأيمن فوق العلم الأخضر لـ "خطوة واحدة" (يبطئ التنفيذ) |
### أنماط التصحيح
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

### القضايا الشائعة
| مشكلة | السبب | الحل |
|---------|-------|---------|
| العفريت لا يستجيب | لا توجد كتلة قبعة الحدث | أضف "عند النقر على العلم الأخضر" أو أي حدث آخر |
| استنساخ لا يعمل | تم إنشاء الاستنساخ ولكن لم يتم عرضه | أضف كتلة "إظهار" بعد "عندما أبدأ كنسخة" |
| متغير مشترك بين العفاريت | ارتباك المتغير العالمي مقابل المحلي | استخدم خيار "لهذا الكائن فقط" |
| لم يتم استقبال البث | اسم الرسالة خاطئ | التحقق من تطابق أسماء البث والاستقبال تمامًا |
| تجميد حلقة لا نهائية | "للأبد" بلا انتظار | أضف كتل "انتظار" صغيرة في حلقات ضيقة |
---

## إمكانية التشغيل البيني
### ملحقات الأجهزة
يستطيع برنامج Scratch الاتصال بالأجهزة المادية من خلال الامتدادات:
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

### واجهة برمجة تطبيقات Scratch Extensions (ملحقات مخصصة)
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

## أنماط التصميم
### النمط 1: حركة المنصات
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

### النمط 2: خلفية التمرير
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

### النموذج 3: متابعة الكائنات (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### النموذج 4: نظام الجرد بالقوائم
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

### النموذج 5: نظام الجسيمات مع النسخ
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

## الأداء والتحسين
### تحسين العفريت
| تقنية | التأثير | الوصف |
|-----------|-------|-------------|
| **تقليل النسخ** | عالية | كل استنساخ يستهلك الذاكرة؛ احذف عند الانتهاء |
| **تقليل الأزياء** | متوسطة | يعني عدد أقل من تبديلات الأزياء تقليل حمل العرض |
| **استخدم "تشغيل بدون تحديث الشاشة"** | عالية | تعمل الكتل المخصصة بدون تحديث الشاشة بشكل أسرع |
| **الحد من كتل "قل"** | متوسطة | فقاعات الكلام تتسبب في عرض النفقات العامة |
| **تجنب كلمة "للأبد" في كل كائن** | متوسطة | استخدم عمليات البث والأحداث بدلاً من الاقتراع المستمر |
### إدارة الاستنساخ
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

### قائمة التحقق من التحسين
| تقنية | التأثير | الوصف |
|-----------|-------|-------------|
| ** تشغيل بدون تحديث الشاشة ** | عالية جدًا | الكتل المخصصة تتخطى العرض من أجل السرعة |
| **تقليل النسخ النشطة** | عالية | احذف النسخ بمجرد عدم الحاجة إليها |
| ** استخدم عمليات البث باعتدال ** | متوسطة | يؤدي عدد كبير جدًا من عمليات البث لكل إطار إلى حدوث تأخير |
| **تبسيط الأزياء** | متوسطة | يتم عرض الصور الأصغر بشكل أسرع |
| **تقليل عمليات القائمة** | متوسطة | تجنب مسح القوائم الكبيرة في كل إطار |
| ** استخدم كتل "الانتظار" ** | منخفض | منع استنزاف وحدة المعالجة المركزية في الحلقات إلى الأبد |
---

## النشر والاستخدام في العالم الحقيقي
### مشاريع المشاركة
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

### الاستخدام التعليمي في العالم الحقيقي
| السياق | كيف يتم استخدام سكراتش | مقياس |
|---------|-------------------|-------|
| ** مدارس الروضة حتى الصف الثاني عشر ** | مقدمة للبرمجة في دروس CS | يستخدم في أكثر من 190 دولة |
| **نوادي البرمجة** | نادي سكراتش / ورش عمل CoderDojo | أكثر من 3000 نادي حول العالم |
| **المكتبات** | برامج برمجة ما بعد المدرسة | أنظمة المكتبات العامة |
| **التعليم المنزلي** | تعليم البرمجة الذاتية | الملايين من المتعلمين في المنزل |
| **جامعة CS0** | دورات علوم الكمبيوتر التمهيدية غير الرئيسية | برامج الجسر الجامعي |
| **إمكانية الوصول** | تعليم البرمجة للمعاقين بصريا | دعم قارئ الشاشة |
| **العلاج** | تنمية المهارات المعرفية والحركية | العلاج الوظيفي |
### الصفر في بحوث التعليم
أظهرت الأبحاث أن برنامج سكراتش يعلم بشكل فعال:
- **التفكير المتسلسل**: تقسيم المشكلات إلى خطوات مرتبة
- **مهارات تصحيح الأخطاء**: العثور على الأخطاء وإصلاحها في المنطق
- **التعبير الإبداعي**: يجمع بين الفن والموسيقى والبرمجة
- **التعاون**: إعادة الدمج والبناء على مشاريع الآخرين
- **المثابرة**: تكرار المشاريع لتحسينها
---

## الانتقال من الصفر
بعد تعلم لغة Scratch، تتضمن الخطوات التالية النموذجية ما يلي:
| اللغة التالية | لماذا |
|-------------|-----|
| **بايثون** | معظم التحولات الطبيعية - بناء جملة قابل للقراءة، ومفاهيم منطقية مماثلة |
| **جافا سكريبت** | إذا كنت مهتمًا بالويب/الألعاب - تعليقات مرئية فورية |
| ** لوا (عبر Roblox / Love2D) ** | إذا كنت مهتمًا بتطوير اللعبة |
| **مخترع التطبيق** | الكتل المرئية لتطبيقات Android (نفس نسب معهد ماساتشوستس للتكنولوجيا) |
| **بلوكلي** | مكتبة جوجل للبرمجة المرئية (مفاهيم مشابهة) |
### رسم خرائط المفاهيم: من الصفر إلى لغة بايثون
| مفهوم الصفر | بايثون يعادل |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| استدعاء الوظيفة أو نظام الحدث |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-مفهرس!) |
| `length of [list]`| `len(list)`|
---

## متى تستخدم سكراتش
| السيناريو | لماذا سكراتش | البديل الأفضل |
|----------|---------|------------------|
| تعليم الأطفال (8-16) البرمجة | مصممة خصيصا لهذا | — |
| التعريف بالتفكير الحسابي | مرئي، لا توجد أخطاء نحوية | — |
| ورش عمل مدرسية / أندية البرمجة | مجاني، قائم على المتصفح، بدون إعداد | — |
| أفكار لعبة النماذج بصريا | التكرار السريع | — |
| التطوير المهني | ليست مصممة لهذا | بايثون، جافا سكريبت، أي لغة نصية |
| تعليم علوم الكمبيوتر على المستوى الجامعي | بسيط جدا | بايثون، جافا، سي |
---

## أسئلة وأجوبة اصطناعية
**س1: هل لغة سكراتش هي لغة برمجة حقًا؟**
ج1: نعم، لغة Scratch هي لغة برمجة حقيقية، ولكنها لغة مرئية وليست مستندة إلى النصوص. وهو يدعم جميع مفاهيم البرمجة الأساسية: المتغيرات، والحلقات، والشروط، والوظائف (الكتل المخصصة)، والقوائم، والبرمجة المستندة إلى الأحداث. والفرق هو أنك تقوم بسحب وإفلات الكتل بدلاً من كتابة التعليمات البرمجية. وهذا يزيل الأخطاء النحوية ويجعل البرمجة في متناول المتعلمين الصغار.
**س2: كيف يمكنني إنشاء وظائف مخصصة (كتل مخصصة) في سكراتش؟**
A2: انتقل إلى فئة "الكتل الخاصة بي" وانقر على "إنشاء كتلة". أعطه اسمًا، وأضف المعلمات إذا لزم الأمر، ثم حدد سلوكه عن طريق إضافة كتل أسفله. يمكن للكتل المخصصة أن تأخذ مدخلات (أرقام، سلاسل، منطقيات) ويمكنها استدعاء كتل مخصصة أخرى. وهذا يتيح البرمجة المعيارية وإعادة استخدام التعليمات البرمجية.
**س3: ما هي أفضل طريقة للتعامل مع منطق اللعبة المعقد في سكراتش؟**
ج3: استخدم الكتل المخصصة لتنظيم المنطق، وبث الرسائل لتنسيق الأحداث بين الكائنات، واستخدام القوائم لتخزين حالة اللعبة (النتائج، والمستويات، والمخزون). بالنسبة للذكاء الاصطناعي المعقد، استخدم أجهزة الحالة المحدودة مع متغيرات تتبع الحالة الحالية. قم باستنساخ الكائنات الحية لأعداء متعددين واستخدم "عندما أبدأ كمستنسخ" لإعطاء كل منهم سلوكًا مستقلاً.
**س4: كيف يمكنني مشاركة البيانات بين الكائنات في برنامج سكراتش؟**
ج4: استخدم المتغيرات العامة (التي تم إنشاؤها بدون "لهذا الكائن فقط") للبيانات المشتركة مثل النتيجة أو حالة اللعبة. استخدم رسائل البث لتشغيل الأحداث عبر الكائنات. لمزيد من التواصل المعقد، استخدم القوائم كهياكل بيانات مشتركة. يمكن لكل كائن قراءة وتعديل المتغيرات والقوائم العامة، مما يتيح التنسيق.
**س5: ما هي بعض التقنيات المتقدمة في لغة سكراتش؟**
ج5: استخدم كتل القلم للرسم وإنشاء تأثيرات مرئية. تنفيذ raycasting للرسومات ثلاثية الأبعاد. استخدم المتغيرات السحابية للألعاب متعددة اللاعبين (يتطلب حالة Scratcher). إنشاء توليد إجرائي بأرقام وقوائم عشوائية. استخدم الكتل المخصصة مع المعلمات للخوارزميات القابلة لإعادة الاستخدام. قم بتجربة استشعار الفيديو ومعالجة الصوت للمشاريع التفاعلية.
---

## سلسلة الفكر
### المشكلة الأولى: إنشاء لعبة منصات
**الخطوة الأولى: فهم المشكلة**
نحن بحاجة إلى إنشاء منصة حيث يمكن للشخصية التحرك يسارًا/يمينًا، والقفز، وتجنب العوائق، وجمع العناصر.
**الخطوة 2: تحديد النهج**
- استخدم محاكاة الجاذبية مع متغير "السقوط".
- كشف الأرض / الاصطدام باستخدام اللون أو لمس الكائنات
- تخزين بيانات المستوى في القوائم
- استخدم الكتل المخصصة لمنطق القفز والحركة
**الخطوة 3: تنفيذ الحل**```scratch
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

**الخطوة 4: التحقق والتحسين**
اختبار القفز على منصات مختلفة. اضبط الجاذبية وارتفاع القفزة لتشعر باللعبة بشكل جيد. إضافة رسوم متحركة للجري والقفز. تنفيذ نقاط التفتيش باستخدام رسائل البث.
---

### المشكلة الثانية: إنشاء لعبة اختبار مع تتبع النتائج
**الخطوة الأولى: فهم المشكلة**
أنشئ لعبة اختبار تطرح الأسئلة وتتحقق من الإجابات وتتتبع نتيجة اللاعب.
**الخطوة 2: تحديد النهج**
- تخزين الأسئلة والأجوبة في قوائم متوازية
- استخدم عداد الأسئلة لتتبع التقدم
- استخدم كتل "اسأل وانتظر" للإدخال
- قارن الإجابات وتحديث النتيجة
**الخطوة 3: تنفيذ الحل**```scratch
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

**الخطوة 4: التحقق والتحسين**
اختبر بإجابات مختلفة بما في ذلك حالات الحافة. إضافة تعليقات للإجابات الخاطئة. تنفيذ خيار إعادة المحاولة. أضف مؤثرات صوتية وملاحظات مرئية للإجابات الصحيحة/الخاطئة.
---

### المشكلة الثالثة: رسم الأشجار الكسورية بالقلم
**الخطوة الأولى: فهم المشكلة**
قم بإنشاء شجرة فركتالية متكررة باستخدام امتداد القلم.
**الخطوة 2: تحديد النهج**
- استخدم العودية لرسم الفروع
- ينقسم كل فرع إلى فرعين أصغر
- استخدم زوايا عشوائية للتنوع الطبيعي
- تتبع طول الفرع وتقليله مع كل مستوى من مستويات التكرار
**الخطوة 3: تنفيذ الحل**```scratch
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

**الخطوة 4: التحقق والتحسين**
ضبط عتبة طول الفرع ونطاقات الزوايا للأشجار الجمالية. أضف أوراقًا عند أطراف الفروع باستخدام تغييرات اللون. تنفيذ أنماط شجرة مختلفة. حفظ الرسومات كصور.
---

## ملخص
سكراتش ليست لغة برمجة بالمعنى التقليدي، بل هي بيئة تعليمية. عبقريته تزيل كل حاجز بين الطفل ومتعة خلق شيء تفاعلي. من خلال التركيز على المفاهيم بدلاً من بناء الجملة، يقوم برنامج Scratch بتعليم أساسيات البرمجة التي يمكن نقلها إلى أي لغة. لتقديم البرمجة للمتعلمين الصغار، يعتبر Scratch هو المعيار الذهبي.