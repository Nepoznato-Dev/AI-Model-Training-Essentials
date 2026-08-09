---
# فراداده
عنوان: "خراش"
توضیحات: "مرجع جامع برای زبان برنامه نویسی Scratch شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب‌ها: [اسکراچ، زبان برنامه‌نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "مبتدی"
پیش نیاز: []
تخمینی_زمان_خواندن: "29 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
#خراش
Scratch یک زبان برنامه نویسی بصری و مبتنی بر بلوک است که توسط آزمایشگاه MIT Media Lab توسعه یافته و برای اولین بار در سال 2007 منتشر شد. کاربران به جای نوشتن کد مبتنی بر متن، بلوک های رنگی را برای ایجاد برنامه به هم می چسبانند. Scratch به طور خاص برای کودکان 8 تا 16 ساله طراحی شده است (اگرچه زبان آموزان در تمام سنین از آن استفاده می کنند) تا مفاهیم اساسی برنامه نویسی - حلقه ها، شرطی ها، متغیرها، رویدادها و توابع - را بدون مانع از خطاهای نحوی آموزش دهد.
اسکرچ پرکاربردترین زبان برنامه نویسی مقدماتی در جهان است، با بیش از 100 میلیون کاربر ثبت نام شده و در دسترس بودن به بیش از 70 زبان. این برنامه در یک مرورگر وب اجرا می شود و رایگان است.
---

## چرا خراش مهم است
- **بهترین مقدمه برای برنامه نویسی**: موانع نحوی را به طور کامل حذف می کند. مفاهیم از طریق دستکاری بصری آموزش داده می شوند.
- **تفکر محاسباتی**: تجزیه، تشخیص الگو، انتزاع و طراحی الگوریتم را آموزش می دهد.
- **خلاقیت محور**: بچه ها بازی، انیمیشن، داستان و موسیقی می سازند — یادگیری برنامه نویسی به عنوان محصول جانبی ساختن چیزهایی که برایشان مهم است.
- **دسترسی جهانی **: در مدارس سراسر جهان استفاده می شود. در بیش از 70 زبان موجود است. رایگان و مبتنی بر مرورگر.
- **Community**: انجمن آنلاین Scratch به اشتراک گذاری، ترکیب مجدد و یادگیری مشارکتی را آموزش می دهد.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **یک زبان برنامه نویسی "واقعی" نیست** | نمی توان نرم افزار تولید، API یا سیستم ساخت | انتقال به پایتون، جاوا اسکریپت یا زبان های مبتنی بر متن |
| **قابلیت های محدود** | بدون I/O فایل، شبکه، یا ساختارهای داده پیشرفته | استفاده برای یادگیری؛ انتقال به زبان های متنی برای پروژه های واقعی |
| **عملکرد** | تفسیر شده، کند برای پروژه های پیچیده | برای کارهای مهم عملکرد طراحی نشده است |
| **تصور سن ** | اغلب به عنوان "فقط برای بچه ها" دیده می شود | Scratch یک ابزار یادگیری است نه یک زبان حرفه ای |
---

## چگونه خراش کار می کند
برنامه‌های اسکرچ (که «پروژه‌ها» نامیده می‌شوند) از **اسپرایت** (شخصیت‌ها/اشیاء) تشکیل شده‌اند که به **بلاک**هایی که در اسکریپت‌ها به هم چسبیده‌اند پاسخ می‌دهند.
### مفاهیم اصلی (آموزش از طریق بلوک ها)
| مفهوم | دسته بندی بلوک خراش | مثال |
|---------|---------------------|---------|
| **سکانس** | حرکت، نگاه | "10 مرحله حرکت دهید" سپس "سلام بگویید" |
| **حلقه** | کنترل (زرد) | "تکرار 10"، "برای همیشه"، "تکرار تا" |
| **شرط** | کنترل (زرد) | "اگر... پس"، "اگر... پس... دیگر" |
| **متغیرها** | متغیرها (نارنجی) | "نمره را روی 0 تنظیم کنید"، "تغییر امتیاز با 1" |
| **رویدادها** | رویدادها (زرد) | "هنگامی که پرچم سبز کلیک شد"، "وقتی کلید فشار داده شد" |
| **توابع** | بلوک های من (سفارشی) | تعریف توالی بلوک قابل استفاده مجدد |
| **لیست ها (آرایه ها)** | متغیرها (نارنجی) | "افزودن به لیست"، "مورد لیست" |
| **پخش** | رویدادها | ارسال پیام بین sprites |
### مثال: منطق بازی ساده
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

## نحو و الگوهای پیشرفته
### دسته بندی ها را با جزئیات مسدود کنید
Scratch 3.0 بلوک ها را در دسته بندی های رنگی سازماندهی می کند:
| دسته بندی | رنگ | انواع بلوک |
|----------|--------|-------------|
| **حرکت** | آبی | حرکت، چرخش، رفتن، سر خوردن، نقطه، تغییر x/y |
| **به نظر می رسد** | بنفش | بگویید، فکر کنید، لباس را تغییر دهید، اندازه را تغییر دهید، نشان دهید/پنهان کنید |
| **صدا** | صورتی | پخش صدا، توقف صداها، تغییر صدا، تغییر گام |
| **رویدادها** | زرد | وقتی روی پرچم کلیک شد، وقتی کلید فشار داده شد، وقتی اسپرایت کلیک شد، پخش |
| **کنترل** | طلا | صبر کنید، تکرار کنید، برای همیشه، اگر، در غیر این صورت، تکرار کنید تا، توقف |
| **احساس** | آبی روشن | لمس کردن، کلید فشرده، ماوس، فاصله، پرسش/پاسخ، تایمر |
| **اپراتور** | سبز | عملیات ریاضی، عملیات متنی، مقایسه، و/یا/نه، تصادفی |
| **متغیرها** | نارنجی | تنظیم/تغییر متغیر، لیست عملیات |
| **بلاک های من** | قرمز تیره | تعاریف بلوک سفارشی (توابع) |
### الگوهای بلوک پیشرفته
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

### بلوک های سفارشی (توابع)
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

### لیست عملیات (آرایه ها)
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

### پخش (ارتباطات بین اسپریت)
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

## معماری و طراحی سیستم
### طراحی رویداد محور
Scratch از معماری رویداد محور استفاده می کند. هر اسکریپت با یک بلوک رویداد (بلاک کلاه) شروع می شود و در پاسخ به آن رویداد اجرا می شود.
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

### ساختار پروژه
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

### سیستم کلون (ایجاد شی)
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

## پیکربندی پروژه و سیستم ساخت
### Scratch Extensions
Scratch از برنامه‌های افزودنی رسمی و انجمن پشتیبانی می‌کند که قابلیت‌هایی را اضافه می‌کنند:
| پسوند | هدف |
|-----------|---------|
| **قلم** | کشیدن خطوط و اشکال بر روی صحنه |
| **حسگر ویدئو** | استفاده از وب کم برای تشخیص حرکت |
| **متن به گفتار** | تبدیل متن به صوتی گفتاری |
| **ترجمه** | ترجمه متن بین زبان ها |
| **Makey Makey** | اتصال اشیاء فیزیکی به عنوان ورودی |
| **micro:bit** | اتصال سخت افزار micro:bit BBC |
| **LEGO Mindstorms** | کنترل ربات های لگو |
| **موسیقی** | نواختن نت و آلات موسیقی |
### فرمت فایل اسکرچ
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

### ویرایشگر آفلاین
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

## تست و اشکال زدایی
### ابزارهای رفع اشکال داخلی
Scratch چندین ابزار داخلی برای اشکال زدایی پروژه ها ارائه می دهد:
| ابزار | نحوه استفاده |
|------|-----------|
| **حالت لاک پشت** | روی یک sprite راست کلیک کرده و "show debug" را انتخاب کنید تا مختصات |
| **مانیتورهای متغیر** | روی یک متغیر کلیک راست کرده و "show" را انتخاب کنید تا مقدار آن را در زمان واقعی | ببینید
| **لیست مانیتور** | مشاهده محتویات لیست در نمایش عادی، ردیف یا ستون |
| **حالت توربو** | برای اجرای سریعتر، Shift را نگه دارید و روی پرچم سبز کلیک کنید
| **حالت تک مرحله ای** | روی پرچم سبز رنگ برای "تک مرحله" (اجرای آهسته) کلیک راست کنید |
### اشکال زدایی الگوها
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

### مسائل رایج
| مشکل | علت | راه حل |
|---------|-------|----------|
| اسپریت پاسخ نمی دهد | بدون بلوک کلاه رویداد | «وقتی روی پرچم سبز کلیک شد» یا رویداد دیگر | را اضافه کنید
| کلون کار نمی کند | کلون ایجاد شد اما نشان داده نشد | بلوک "نمایش" را بعد از "When I start as a clone" اضافه کنید |
| متغیر مشترک بین sprites | سردرگمی متغیر جهانی در مقابل محلی | از گزینه "فقط برای این اسپرایت" استفاده کنید |
| پخش دریافت نشد | نام پیام اشتباه است | بررسی کنید که نام های پخش و دریافت دقیقا مطابقت دارند |
| فریز حلقه بی نهایت | "برای همیشه" بدون انتظار | بلوک های کوچک "صبر کن" را در حلقه های محکم اضافه کنید |
---

## قابلیت همکاری
### برنامه های افزودنی سخت افزاری
Scratch می تواند از طریق برنامه های افزودنی به سخت افزار فیزیکی متصل شود:
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

### Scratch Extensions API (برنامه‌های افزودنی سفارشی)
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

## الگوهای طراحی
### الگوی 1: جنبش پلتفرمر
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

### الگوی 2: پس‌زمینه پیمایش
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

### الگوی 3: دنبال کردن Sprite (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### الگوی 4: سیستم موجودی با لیست
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

### الگوی 5: سیستم ذرات با کلون
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

## عملکرد و بهینه سازی
### بهینه سازی Sprite
| تکنیک | تاثیر | توضیحات |
|-----------|--------|-------------|
| **به حداقل رساندن کلون ها** | بالا | هر کلون حافظه را مصرف می کند. حذف پس از اتمام |
| **کاهش لباس** | متوسط ​​| سوئیچ های لباس کمتر به معنای رندر کمتر سربار |
| **از "اجرا بدون نوسازی صفحه" استفاده کنید** | بالا | بلوک‌های سفارشی بدون به‌روزرسانی صفحه، سریع‌تر اجرا می‌شوند |
| **بلوک‌های «گفتن» را محدود کنید** | متوسط ​​| حباب های گفتار باعث رندر بالای سر می شوند |
| **از "برای همیشه" در هر جن پرهیز کنید** | متوسط ​​| به جای نظرسنجی مداوم از پخش و رویدادها استفاده کنید |
### مدیریت کلون
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

### چک لیست بهینه سازی
| تکنیک | تاثیر | توضیحات |
|-----------|--------|-------------|
| **اجرا بدون رفرش صفحه** | خیلی بالا | بلوک های سفارشی از رندر پرش برای سرعت |
| **کلون های فعال را به حداقل برسانید** | بالا | حذف کلون ها به محض اینکه دیگر مورد نیاز نیستند |
| **از پخش ها کم استفاده کنید** | متوسط ​​| تعداد زیاد پخش در هر فریم باعث تاخیر |
| **ساده سازی لباس** | متوسط ​​| تصاویر کوچکتر سریعتر ارائه می شوند |
| **کاهش عملیات لیست** | متوسط ​​| از اسکن لیست های بزرگ در هر فریم خودداری کنید |
| **از بلوک‌های «انتظار» استفاده کنید** | کم | جلوگیری از هنگ کردن CPU در حلقه های forever |
---

## استقرار و استفاده در دنیای واقعی
### به اشتراک گذاری پروژه ها
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

### استفاده آموزشی در دنیای واقعی
| زمینه | نحوه استفاده از Scratch | مقیاس |
|---------|------------------|-------|
| **مدارس K-12** | مقدمه ای بر برنامه نویسی در کلاس های CS | مورد استفاده در 190+ کشور |
| **باشگاه های کدنویسی** | کارگاه های Scratch Club / CoderDojo | بیش از 3000 باشگاه در سراسر جهان |
| **کتابخانه ها** | برنامه های برنامه نویسی بعد از مدرسه | سیستم های کتابخانه های عمومی |
| **آموزش در منزل** | آموزش برنامه نویسی خودگام | میلیون ها زبان آموز خانگی |
| **دانشگاه CS0** | دوره های غیر اصلی مقدماتی CS | برنامه های پل دانشگاه |
| **دسترسی** | آموزش برنامه نویسی به افراد کم بینا | پشتیبانی از صفحه خوان |
| **درمان** | رشد مهارت های شناختی و حرکتی | کاردرمانی |
### خراش در تحقیقات آموزش و پرورش
تحقیقات نشان داده است که Scratch به طور موثر آموزش می دهد:
- **تفکر متوالی**: شکستن مسائل به مراحل منظم
- **مهارت اشکال زدایی**: یافتن و رفع خطاها در منطق
- ** بیان خلاق **: ترکیب هنر، موسیقی و برنامه نویسی
- **همکاری**: بازسازی و ساخت پروژه های دیگران
- ** تداوم **: تکرار پروژه ها برای بهبود آنها
---

## انتقال از ابتدا
پس از یادگیری اسکرچ، مراحل معمولی بعدی عبارتند از:
| زبان بعدی | چرا |
|--------------|-----|
| **پایتون** | طبیعی ترین انتقال - نحو قابل خواندن، مفاهیم منطقی مشابه |
| **جاوا اسکریپت** | در صورت علاقه به وب/بازی - بازخورد بصری فوری |
| **Lua (از طریق Roblox/Love2D)** | در صورت علاقه به بازی سازی |
| **App Inventor** | بلوک های بصری برای برنامه های اندروید (همان نسل MIT) |
| **بلاک** | کتابخانه برنامه نویسی بصری گوگل (مفاهیم مشابه) |
### Concept Mapping: Scratch to Python
| مفهوم خراش | معادل پایتون |
|----------------|-------------------|
| `set [x] to 0`|  __محافظت شده_1__ |
| `change [x] by 1`|  __محافظت شده_3__ |
| `repeat 10`| `for i in range(10):`|
|  __محافظت شده_6__ | `while True:`|
| `if ... then`|  __محافظت شده_9__ |
| `broadcast [msg]`| فراخوانی تابع یا سیستم رویداد |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-شاخص شده!) |
| `length of [list]`| `len(list)`|
---

## چه زمانی از Scratch استفاده کنیم
| سناریو | چرا خراش | جایگزین بهتر |
|----------|----------|------------------|
| آموزش کدنویسی به کودکان (8 تا 16 سال) | طراحی شده به طور خاص برای این | — |
| معرفی تفکر محاسباتی | بصری، بدون خطای نحوی | — |
| کارگاه های آموزشی / باشگاه های کدنویسی | رایگان، مبتنی بر مرورگر، بدون راه اندازی | — |
| نمونه سازی ایده های بازی به صورت بصری | تکرار سریع | — |
| توسعه حرفه ای | برای این طراحی نشده است | پایتون، جاوا اسکریپت، هر زبان متنی |
| آموزش CS در سطح دانشگاه | خیلی ساده | پایتون، جاوا، سی |
---

## خلاصه
Scratch یک زبان برنامه نویسی به معنای سنتی نیست - یک محیط یادگیری است. نبوغ آن از بین بردن هر مانعی بین کودک و لذت ایجاد چیزی تعاملی است. Scratch با تمرکز بر مفاهیم به جای نحو، اصول برنامه نویسی را که به هر زبانی منتقل می شود را آموزش می دهد. برای معرفی برنامه نویسی به زبان آموزان جوان، Scratch استاندارد طلایی است.