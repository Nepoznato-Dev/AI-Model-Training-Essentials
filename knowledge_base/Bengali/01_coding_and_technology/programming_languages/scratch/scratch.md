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
# আঁচড়
স্ক্র্যাচ হল একটি ভিজ্যুয়াল, ব্লক-ভিত্তিক প্রোগ্রামিং ভাষা যা MIT মিডিয়া ল্যাব দ্বারা তৈরি করা হয়েছে এবং 2007 সালে প্রথম প্রকাশিত হয়েছিল। পাঠ্য-ভিত্তিক কোড লেখার পরিবর্তে, ব্যবহারকারীরা প্রোগ্রাম তৈরি করতে রঙিন ব্লকগুলি একত্রিত করে। স্ক্র্যাচ বিশেষভাবে 8-16 বছর বয়সী শিশুদের জন্য ডিজাইন করা হয়েছে (যদিও সব বয়সের শিক্ষার্থীরা এটি ব্যবহার করে) মৌলিক প্রোগ্রামিং ধারণাগুলি শেখানোর জন্য — লুপ, কন্ডিশনাল, ভেরিয়েবল, ইভেন্ট এবং ফাংশন — সিনট্যাক্স ত্রুটির বাধা ছাড়াই।
স্ক্র্যাচ হল বিশ্বের সর্বাধিক ব্যবহৃত পরিচিতিমূলক প্রোগ্রামিং ভাষা, যেখানে 100 মিলিয়নেরও বেশি নিবন্ধিত ব্যবহারকারী এবং 70+ ভাষায় উপলব্ধতা রয়েছে। এটি একটি ওয়েব ব্রাউজারে চলে এবং বিনামূল্যে।
---

## কেন স্ক্র্যাচ গুরুত্বপূর্ণ
- **প্রোগ্রামিং এর সর্বোত্তম ভূমিকা**: সিনট্যাক্সের বাধা সম্পূর্ণরূপে দূর করে। ধারণাগুলি ভিজ্যুয়াল ম্যানিপুলেশনের মাধ্যমে শেখানো হয়।
- **কম্পিউটেশনাল চিন্তা**: পচন, প্যাটার্ন স্বীকৃতি, বিমূর্ততা, এবং অ্যালগরিদম ডিজাইন শেখায়।
- **সৃজনশীলতা-চালিত**: বাচ্চারা গেমস, অ্যানিমেশন, গল্প এবং সঙ্গীত তৈরি করে — প্রোগ্রামিং শেখার উপজাত হিসেবে তারা যে জিনিসগুলি যত্ন করে তা তৈরি করে।
- **বিশ্বব্যাপী পৌঁছান**: বিশ্বব্যাপী স্কুলে ব্যবহৃত হয়। 70+ ভাষায় উপলব্ধ। বিনামূল্যে এবং ব্রাউজার ভিত্তিক.
- **সম্প্রদায়**: স্ক্র্যাচ অনলাইন সম্প্রদায় ভাগাভাগি, রিমিক্সিং এবং সহযোগিতামূলক শিক্ষা শেখায়।
## বাণিজ্য বন্ধ
| সীমাবদ্ধতা | বিস্তারিত | সাধারণ সমাধান |
|------------|---------|---------|
| **একটি "বাস্তব" প্রোগ্রামিং ভাষা নয়** | উত্পাদন সফ্টওয়্যার, API, বা সিস্টেম তৈরি করতে পারে না | পাইথন, জাভাস্ক্রিপ্ট, বা পাঠ্য-ভিত্তিক ভাষাতে রূপান্তর |
| **সীমিত ক্ষমতা** | কোন ফাইল I/O, নেটওয়ার্কিং, বা উন্নত ডেটা স্ট্রাকচার নেই | শেখার জন্য ব্যবহার করুন; বাস্তব প্রকল্পের জন্য পাঠ্য ভাষায় সরান |
| **পারফরম্যান্স** | ব্যাখ্যা করা, জটিল প্রকল্পের জন্য ধীর | কর্মক্ষমতা-সমালোচনামূলক কাজের জন্য ডিজাইন করা হয়নি |
| **বয়স উপলব্ধি** | প্রায়শই "শুধু বাচ্চাদের জন্য" হিসাবে দেখা হয় | স্ক্র্যাচ একটি শেখার সরঞ্জাম, একটি পেশাদার ভাষা নয় |
---

## কিভাবে স্ক্র্যাচ কাজ করে
স্ক্র্যাচ প্রোগ্রাম (যাকে "প্রকল্প" বলা হয়) **স্প্রাইট** (অক্ষর/অবজেক্ট) নিয়ে গঠিত যা স্ক্রিপ্টে একসাথে **ব্লক**কে সাড়া দেয়।
### মূল ধারণা (ব্লকের মাধ্যমে শেখানো)
| ধারণা | স্ক্র্যাচ ব্লক বিভাগ | উদাহরণ |
|---------|-------------------------|---------|
| **ক্রম** | গতি, চেহারা | "10টি ধাপ সরান" তারপর "হ্যালো বলুন" |
| **লুপ** | নিয়ন্ত্রণ (হলুদ) | "পুনরাবৃত্তি 10", "চিরকাল", "পর্যন্ত পুনরাবৃত্তি" |
| **শর্তাবলী** | নিয়ন্ত্রণ (হলুদ) | "যদি... তারপর", "যদি... তাহলে... অন্যথায়" |
| **ভেরিয়েবল** | ভেরিয়েবল (কমলা) | "স্কোর 0 এ সেট করুন", "স্কোর 1 দ্বারা পরিবর্তন করুন" |
| **ইভেন্ট** | ঘটনা (হলুদ) | "যখন সবুজ পতাকা ক্লিক করা হয়", "যখন কী চাপা হয়" |
| **ফাংশন** | আমার ব্লক (কাস্টম) | পুনর্ব্যবহারযোগ্য ব্লক ক্রম সংজ্ঞায়িত করুন |
| **তালিকা (অ্যারে)** | ভেরিয়েবল (কমলা) | "তালিকাতে যোগ করুন", "তালিকার আইটেম" |
| **সম্প্রচার** | ঘটনা | sprites মধ্যে বার্তা পাঠান |
### উদাহরণ: সরল গেম লজিক
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

## উন্নত সিনট্যাক্স এবং প্যাটার্নস
### বিস্তারিতভাবে ব্লক বিভাগ
স্ক্র্যাচ 3.0 ব্লকগুলিকে রঙ-কোডেড বিভাগে সংগঠিত করে:
| বিভাগ | রঙ | ব্লকের ধরন |
|------------|---------|---------------|
| **গতি** | নীল | সরান, ঘুরুন, গোটো, গ্লাইড করুন, পয়েন্ট করুন, x/y পরিবর্তন করুন |
| **দেখতে** | বেগুনি | বলুন, ভাবুন, পোশাক পরিবর্তন করুন, আকার পরিবর্তন করুন, দেখান/লুকান |
| **শব্দ** | গোলাপী | শব্দ চালান, শব্দ বন্ধ করুন, ভলিউম পরিবর্তন করুন, পিচ পরিবর্তন করুন |
| **ইভেন্ট** | হলুদ | যখন পতাকা ক্লিক করা হয়, যখন কী চাপা হয়, যখন স্প্রাইট ক্লিক করা হয়, সম্প্রচার |
| **নিয়ন্ত্রণ** | সোনা | অপেক্ষা করুন, পুনরাবৃত্তি করুন, চিরতরে, যদি, যদি-অন্যথায়, পুনরাবৃত্তি না হওয়া পর্যন্ত, থামুন |
| **অনুভূতি** | হালকা নীল | স্পর্শ, কী চাপা, মাউস, দূরত্ব, জিজ্ঞাসা/উত্তর, টাইমার |
| **অপারেটর** | সবুজ | গণিত অপ্স, টেক্সট অপ্স, তুলনা, এবং/বা/না, এলোমেলো |
| **ভেরিয়েবল** | কমলা | পরিবর্তনশীল সেট/পরিবর্তন, তালিকা অপারেশন |
| **আমার ব্লক** | গাঢ় লাল | কাস্টম ব্লক সংজ্ঞা (ফাংশন) |
### অ্যাডভান্সড ব্লক প্যাটার্ন
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

### কাস্টম ব্লক (ফাংশন)
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

### তালিকা অপারেশন (অ্যারে)
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

### সম্প্রচার (আন্তঃস্প্রাইট কমিউনিকেশন)
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

## আর্কিটেকচার এবং সিস্টেম ডিজাইন
### ইভেন্ট-চালিত ডিজাইন
স্ক্র্যাচ একটি ইভেন্ট-চালিত আর্কিটেকচার ব্যবহার করে। প্রতিটি স্ক্রিপ্ট একটি ইভেন্ট ব্লক (হ্যাট ব্লক) দিয়ে শুরু হয় এবং সেই ইভেন্টের প্রতিক্রিয়ায় চলে।
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

### প্রকল্পের কাঠামো
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

### ক্লোন সিস্টেম (বস্তু তৈরি)
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

## প্রজেক্ট কনফিগারেশন এবং বিল্ড সিস্টেম
### স্ক্র্যাচ এক্সটেনশন
স্ক্র্যাচ অফিসিয়াল এবং কমিউনিটি এক্সটেনশানগুলিকে সমর্থন করে যা ক্ষমতা যুক্ত করে:
| এক্সটেনশন | উদ্দেশ্য |
|------------|---------|
| **কলম** | মঞ্চে লাইন এবং আকার আঁকুন |
| **ভিডিও সেন্সিং** | গতি সনাক্তকরণের জন্য ওয়েবক্যাম ব্যবহার করুন |
| **টেক্সট টু স্পিচ** | পাঠ্যকে কথ্য অডিওতে রূপান্তর করুন |
| **অনুবাদ** | ভাষার মধ্যে পাঠ্য অনুবাদ করুন |
| **মেকি মেকি** | ইনপুট হিসাবে ভৌত বস্তু সংযুক্ত করুন |
| **মাইক্রো:বিট** | বিবিসি মাইক্রো:বিট হার্ডওয়্যার সংযুক্ত করুন |
| **লেগো মাইন্ডস্টর্ম** | লেগো রোবট নিয়ন্ত্রণ করুন |
| **সঙ্গীত** | বাদ্যযন্ত্রের নোট এবং যন্ত্র বাজান |
### স্ক্র্যাচ ফাইল ফরম্যাট
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

### অফলাইন সম্পাদক
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

## পরীক্ষা এবং ডিবাগিং
### অন্তর্নির্মিত ডিবাগিং টুল
স্ক্র্যাচ ডিবাগিং প্রকল্পের জন্য বেশ কয়েকটি অন্তর্নির্মিত সরঞ্জাম সরবরাহ করে:
| টুল | কিভাবে ব্যবহার করবেন |
|------|------------|
| **কচ্ছপ মোড** | একটি স্প্রাইট রাইট-ক্লিক করুন এবং স্থানাঙ্ক দেখতে "ডিবাগ দেখান" নির্বাচন করুন |
| **ভেরিয়েবল মনিটর** | একটি ভেরিয়েবলে ডান-ক্লিক করুন এবং রিয়েল-টাইমে এর মান দেখতে "শো" নির্বাচন করুন |
| **তালিকা মনিটর** | সাধারণ, সারি, বা কলাম প্রদর্শনে তালিকা বিষয়বস্তু দেখুন |
| **টার্বো মোড** | দ্রুত সম্পাদনের জন্য সবুজ পতাকা ক্লিক করার সময় Shift ধরে রাখুন |
| **একক-পদক্ষেপ মোড** | "একক পদক্ষেপ" এর জন্য সবুজ পতাকায় ডান-ক্লিক করুন (মন্থর সম্পাদন) |
### ডিবাগিং প্যাটার্ন
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

### সাধারণ সমস্যা
| সমস্যা | কারণ | সমাধান |
|---------|-------|----------|
| স্প্রাইট সাড়া দিচ্ছে না | কোন ইভেন্ট টুপি ব্লক | যোগ করুন "যখন সবুজ পতাকা ক্লিক করা হয়" বা অন্য ইভেন্ট |
| ক্লোন কাজ করছে না | ক্লোন তৈরি কিন্তু দেখানো হয়নি | "যখন আমি একটি ক্লোন হিসাবে শুরু করি" এর পরে "শো" ব্লক যোগ করুন |
| স্প্রাইটের মধ্যে ভাগ করা পরিবর্তনশীল | গ্লোবাল বনাম স্থানীয় পরিবর্তনশীল বিভ্রান্তি | "শুধুমাত্র এই স্প্রাইটের জন্য" বিকল্পটি ব্যবহার করুন |
| সম্প্রচার গৃহীত হয়নি | ভুল বার্তা নাম | সম্প্রচার যাচাই করুন এবং নামগুলি হুবহু মেলে |
| অসীম লুপ ফ্রিজ | "চিরকাল" কোন অপেক্ষা ছাড়া | টাইট লুপে ছোট "অপেক্ষা" ব্লক যোগ করুন |
---

## ইন্টারঅপারেবিলিটি
### হার্ডওয়্যার এক্সটেনশন
স্ক্র্যাচ এক্সটেনশনের মাধ্যমে শারীরিক হার্ডওয়্যারের সাথে সংযোগ করতে পারে:
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

### স্ক্র্যাচ এক্সটেনশন API (কাস্টম এক্সটেনশন)
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

## ডিজাইন প্যাটার্ন
### প্যাটার্ন 1: প্ল্যাটফর্মার আন্দোলন
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

### প্যাটার্ন 2: স্ক্রলিং ব্যাকগ্রাউন্ড
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

### প্যাটার্ন ৩: স্প্রাইট অনুসরণ (চেজ এআই)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### প্যাটার্ন 4: তালিকা সহ ইনভেন্টরি সিস্টেম
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

### প্যাটার্ন 5: ক্লোন সহ কণা সিস্টেম
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

## কর্মক্ষমতা এবং অপ্টিমাইজেশান
### স্প্রাইট অপ্টিমাইজেশান
| টেকনিক | প্রভাব | বর্ণনা |
|------------|---------|---------------|
| **ক্লোনগুলি ছোট করুন** | উচ্চ | প্রতিটি ক্লোন মেমরি গ্রাস করে; ডিলিট হয়ে গেলে |
| **পরিচ্ছদ কমান** | মাঝারি | কম কস্টিউম সুইচ মানে কম রেন্ডারিং ওভারহেড |
| **"স্ক্রিন রিফ্রেশ ছাড়া রান" ব্যবহার করুন ** | উচ্চ | স্ক্রিন রিফ্রেশ ছাড়াই কাস্টম ব্লক দ্রুত চলে |
| ** সীমিত "বলুন" ব্লক** | মাঝারি | বক্তৃতা বুদবুদ ওভারহেড রেন্ডারিং কারণ |
| **প্রতিটি পরকীয়াতে "চিরকাল" এড়িয়ে চলুন** | মাঝারি | স্থির ভোটের পরিবর্তে সম্প্রচার এবং ইভেন্ট ব্যবহার করুন |
### ক্লোন ব্যবস্থাপনা
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

### অপ্টিমাইজেশান চেকলিস্ট
| টেকনিক | প্রভাব | বর্ণনা |
|------------|---------|---------------|
| **স্ক্রিন রিফ্রেশ ছাড়াই চালান** | খুব উচ্চ | কাস্টম ব্লক গতির জন্য রেন্ডারিং এড়িয়ে যায় |
| **সক্রিয় ক্লোনগুলিকে ছোট করুন** | উচ্চ | ক্লোনগুলি আর প্রয়োজন না হওয়ার সাথে সাথে মুছুন |
| **সম্প্রচার অল্প করে ব্যবহার করুন** | মাঝারি | ফ্রেমের প্রতি অনেক বেশি সম্প্রচারের কারণে ল্যাগ হয় |
| **পরিচ্ছদ সরলীকরণ** | মাঝারি | ছোট ছবি দ্রুত রেন্ডার হয় |
| **তালিকা ক্রিয়াকলাপ হ্রাস করুন** | মাঝারি | প্রতিটি ফ্রেমে বড় তালিকা স্ক্যান করা এড়িয়ে চলুন |
| **"অপেক্ষা" ব্লক ব্যবহার করুন** | কম | চিরকালের লুপগুলিতে সিপিইউ হগিং প্রতিরোধ করুন |
---

## স্থাপনা এবং বাস্তব-বিশ্ব ব্যবহার
### শেয়ারিং প্রজেক্ট
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

### বাস্তব-বিশ্ব শিক্ষামূলক ব্যবহার
| প্রসঙ্গ | কিভাবে স্ক্র্যাচ ব্যবহার করা হয় | স্কেল |
|---------|----------------------|---------|
| **K-12 স্কুল** | CS ক্লাসে প্রোগ্রামিং এর পরিচিতি | 190+ দেশে ব্যবহৃত |
| **কোডিং ক্লাব** | স্ক্র্যাচ ক্লাব / কোডারডোজো ওয়ার্কশপ | বিশ্বব্যাপী 3000+ ক্লাব |
| **লাইব্রেরি** | স্কুল পরবর্তী প্রোগ্রামিং প্রোগ্রাম | পাবলিক লাইব্রেরি সিস্টেম |
| **হোমস্কুলিং** | স্ব-গতি সম্পন্ন প্রোগ্রামিং শিক্ষা | লাখ লাখ গৃহশিক্ষক |
| **বিশ্ববিদ্যালয় CS0** | অ-প্রধান পরিচিতিমূলক সিএস কোর্স | বিশ্ববিদ্যালয় সেতু কর্মসূচী |
| **অভিগম্যতা** | দৃষ্টি প্রতিবন্ধীদের প্রোগ্রামিং শেখানো | স্ক্রিন রিডার সমর্থন |
| **থেরাপি** | জ্ঞানীয় এবং মোটর দক্ষতা উন্নয়ন | পেশাগত থেরাপি |
### শিক্ষা গবেষণায় আঁচড়
গবেষণায় দেখানো হয়েছে যে স্ক্র্যাচ কার্যকরভাবে শেখায়:
- **অনুক্রমিক চিন্তা**: সমস্যাগুলিকে সাজানো ধাপে ভাঙা
- **ডিবাগিং দক্ষতা**: যুক্তিতে ত্রুটি খুঁজে বের করা এবং ঠিক করা
- **সৃজনশীল অভিব্যক্তি**: শিল্প, সঙ্গীত এবং প্রোগ্রামিংয়ের সমন্বয়
- **সহযোগিতা**: রিমিক্সিং এবং অন্যদের প্রকল্প তৈরি করা
- **অধ্যবসায়**: প্রকল্পগুলিকে উন্নত করার জন্য পুনরাবৃত্তি করা
---

## স্ক্র্যাচ থেকে রূপান্তর
স্ক্র্যাচ শেখার পরে, সাধারণ পরবর্তী পদক্ষেপগুলি অন্তর্ভুক্ত করে:
| পরবর্তী ভাষা | কেন |
|---------------|------|
| **পাইথন** | সর্বাধিক প্রাকৃতিক রূপান্তর — পাঠযোগ্য সিনট্যাক্স, অনুরূপ যুক্তি ধারণা |
| **জাভাস্ক্রিপ্ট** | ওয়েব/গেমে আগ্রহী হলে — অবিলম্বে ভিজ্যুয়াল প্রতিক্রিয়া |
| **লুয়া (রব্লক্স/লাভ2ডি এর মাধ্যমে)** | গেম ডেভেলপমেন্টে আগ্রহী হলে |
| **অ্যাপ উদ্ভাবক** | অ্যান্ড্রয়েড অ্যাপ্লিকেশনের জন্য ভিজ্যুয়াল ব্লক (একই এমআইটি বংশ) |
| **অবরুদ্ধ** | গুগলের ভিজ্যুয়াল প্রোগ্রামিং লাইব্রেরি (অনুরূপ ধারণা) |
### কনসেপ্ট ম্যাপিং: স্ক্র্যাচ টু পাইথন
| স্ক্র্যাচ ধারণা | পাইথন সমতুল্য |
|------------------------------------------------
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| ফাংশন কল বা ইভেন্ট সিস্টেম |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-সূচিবদ্ধ!) |
| `length of [list]`| `len(list)`|
---

## কখন স্ক্র্যাচ ব্যবহার করবেন
| দৃশ্যকল্প | কেন আঁচড় | ভাল বিকল্প |
|------------|------------|---------|
| শিশুদের (8-16) কোড শেখানো | এই জন্য বিশেষভাবে ডিজাইন করা | — |
| কম্পিউটেশনাল চিন্তাধারার পরিচয় | ভিজ্যুয়াল, কোন সিনট্যাক্স ত্রুটি নেই | — |
| স্কুল কর্মশালা / কোডিং ক্লাব | বিনামূল্যে, ব্রাউজার-ভিত্তিক, কোনো সেটআপ নেই | — |
| প্রোটোটাইপিং গেম ধারণা দৃশ্যত | দ্রুত পুনরাবৃত্তি | — |
| পেশাগত উন্নয়ন | এর জন্য ডিজাইন করা হয়নি | পাইথন, জাভাস্ক্রিপ্ট, যেকোনো পাঠ্য ভাষা |
| বিশ্ববিদ্যালয় পর্যায়ের সিএস শিক্ষা | খুব সহজ | পাইথন, জাভা, সি |
---

## সিন্থেটিক প্রশ্নোত্তর
**প্রশ্ন 1: স্ক্র্যাচ কি সত্যিই একটি প্রোগ্রামিং ভাষা?**
A1: হ্যাঁ, স্ক্র্যাচ একটি বাস্তব প্রোগ্রামিং ভাষা, কিন্তু এটি পাঠ্য-ভিত্তিক নয় বরং ভিজ্যুয়াল। এটি সমস্ত মৌলিক প্রোগ্রামিং ধারণা সমর্থন করে: ভেরিয়েবল, লুপ, কন্ডিশনাল, ফাংশন (কাস্টম ব্লক), তালিকা এবং ইভেন্ট-চালিত প্রোগ্রামিং। পার্থক্য হল যে আপনি কোড টাইপ করার পরিবর্তে ব্লকগুলি টেনে আনেন এবং ড্রপ করেন। এটি সিনট্যাক্স ত্রুটি দূর করে এবং তরুণ শিক্ষার্থীদের জন্য প্রোগ্রামিং অ্যাক্সেসযোগ্য করে তোলে।
**প্রশ্ন 2: আমি কীভাবে স্ক্র্যাচে কাস্টম ফাংশন (কাস্টম ব্লক) তৈরি করব?**
A2: "আমার ব্লক" বিভাগে যান এবং "একটি ব্লক তৈরি করুন" এ ক্লিক করুন। এটির একটি নাম দিন, প্রয়োজনে পরামিতি যোগ করুন, তারপর এর নিচে ব্লক যোগ করে এর আচরণ সংজ্ঞায়িত করুন। কাস্টম ব্লক ইনপুট নিতে পারে (সংখ্যা, স্ট্রিং, বুলিয়ান) এবং অন্যান্য কাস্টম ব্লক কল করতে পারে। এটি মডুলার প্রোগ্রামিং এবং কোড পুনঃব্যবহার সক্ষম করে।
**প্রশ্ন 3: স্ক্র্যাচে জটিল গেম লজিক পরিচালনা করার সর্বোত্তম উপায় কী?**
A3: যুক্তি সংগঠিত করতে কাস্টম ব্লক ব্যবহার করুন, স্প্রাইটের মধ্যে ইভেন্ট সমন্বয়ের জন্য বার্তা সম্প্রচার করুন এবং গেম স্টেট (স্কোর, লেভেল, ইনভেন্টরি) সঞ্চয় করতে তালিকা ব্যবহার করুন। জটিল AI এর জন্য, বর্তমান অবস্থা ট্র্যাকিং ভেরিয়েবল সহ সীমিত স্টেট মেশিন ব্যবহার করুন। একাধিক শত্রুর জন্য ক্লোন স্প্রাইট এবং প্রতিটি স্বাধীন আচরণ দিতে "যখন আমি একটি ক্লোন হিসাবে শুরু করি" ব্যবহার করুন।
**প্রশ্ন 4: স্ক্র্যাচে স্প্রাইটের মধ্যে আমি কীভাবে ডেটা ভাগ করতে পারি?**
A4: স্কোর বা গেম স্টেটের মতো শেয়ার করা ডেটার জন্য গ্লোবাল ভেরিয়েবল ("শুধুমাত্র এই স্প্রাইটের জন্য" ছাড়া তৈরি) ব্যবহার করুন। স্প্রাইট জুড়ে ইভেন্ট ট্রিগার করতে সম্প্রচার বার্তা ব্যবহার করুন। আরও জটিল যোগাযোগের জন্য, শেয়ার করা ডেটা স্ট্রাকচার হিসেবে তালিকা ব্যবহার করুন। প্রতিটি স্প্রাইট বিশ্বব্যাপী ভেরিয়েবল এবং তালিকাগুলি পড়তে এবং সংশোধন করতে পারে, সমন্বয় সক্ষম করে।
**প্রশ্ন 5: স্ক্র্যাচে কিছু উন্নত কৌশল কি কি?**
A5: অঙ্কন এবং ভিজ্যুয়াল এফেক্ট তৈরি করার জন্য পেন ব্লক ব্যবহার করুন। 3D-এর মতো গ্রাফিক্সের জন্য রেকাস্টিং প্রয়োগ করুন। মাল্টিপ্লেয়ার গেমের জন্য ক্লাউড ভেরিয়েবল ব্যবহার করুন (স্ক্র্যাচার স্ট্যাটাস প্রয়োজন)। এলোমেলো সংখ্যা এবং তালিকা সহ পদ্ধতিগত প্রজন্ম তৈরি করুন। পুনরায় ব্যবহারযোগ্য অ্যালগরিদমের জন্য পরামিতি সহ কাস্টম ব্লক ব্যবহার করুন। ইন্টারেক্টিভ প্রজেক্টের জন্য ভিডিও সেন্সিং এবং সাউন্ড ম্যানিপুলেশন নিয়ে পরীক্ষা করুন।
---

## চেইন-অফ-থট
### সমস্যা 1: একটি প্ল্যাটফর্মার গেম তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
আমাদের একটি প্ল্যাটফর্ম তৈরি করতে হবে যেখানে একটি চরিত্র বাম/ডানে যেতে পারে, লাফ দিতে পারে, বাধা এড়াতে পারে এবং আইটেম সংগ্রহ করতে পারে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
- একটি "পতন" ভেরিয়েবল সহ মাধ্যাকর্ষণ সিমুলেশন ব্যবহার করুন
- রঙ বা স্প্রাইট স্পর্শ ব্যবহার করে স্থল / সংঘর্ষ সনাক্ত করুন
- তালিকায় স্তরের ডেটা সংরক্ষণ করুন
- জাম্প এবং আন্দোলনের যুক্তির জন্য কাস্টম ব্লক ব্যবহার করুন
**ধাপ 3: সমাধানটি বাস্তবায়ন করুন**```scratch
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

**পদক্ষেপ 4: যাচাই করুন এবং অপ্টিমাইজ করুন**
বিভিন্ন প্ল্যাটফর্মে পরীক্ষা জাম্পিং। ভাল খেলা অনুভূতির জন্য মাধ্যাকর্ষণ এবং লাফের উচ্চতা সামঞ্জস্য করুন। দৌড় এবং লাফানোর জন্য অ্যানিমেশন যোগ করুন। সম্প্রচারিত বার্তা ব্যবহার করে চেকপয়েন্ট প্রয়োগ করুন।
---

### সমস্যা 2: স্কোর ট্র্যাকিং সহ একটি কুইজ গেম তৈরি করা
**ধাপ 1: সমস্যাটি বুঝুন**
একটি কুইজ গেম তৈরি করুন যা প্রশ্ন জিজ্ঞাসা করে, উত্তর চেক করে এবং খেলোয়াড়ের স্কোর ট্র্যাক করে।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
- সমান্তরাল তালিকায় প্রশ্ন এবং উত্তর সংরক্ষণ করুন
- অগ্রগতি ট্র্যাক করতে একটি প্রশ্ন কাউন্টার ব্যবহার করুন
- ইনপুট জন্য "জিজ্ঞাসা এবং অপেক্ষা করুন" ব্লক ব্যবহার করুন
- উত্তর তুলনা করুন এবং স্কোর আপডেট করুন
**ধাপ 3: সমাধানটি বাস্তবায়ন করুন**```scratch
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

**পদক্ষেপ 4: যাচাই করুন এবং অপ্টিমাইজ করুন**
এজ কেস সহ বিভিন্ন উত্তর দিয়ে পরীক্ষা করুন। ভুল উত্তর জন্য প্রতিক্রিয়া যোগ করুন. একটি পুনরায় চেষ্টা বিকল্প বাস্তবায়ন করুন. সঠিক/ভুল উত্তরের জন্য সাউন্ড ইফেক্ট এবং ভিজ্যুয়াল ফিডব্যাক যোগ করুন।
---

### সমস্যা 3: কলম দিয়ে ফ্র্যাক্টাল ট্রি আঁকা
**ধাপ 1: সমস্যাটি বুঝুন**
পেন এক্সটেনশন ব্যবহার করে একটি পুনরাবৃত্ত ফ্র্যাক্টাল ট্রি তৈরি করুন।
**ধাপ 2: পদ্ধতি সনাক্ত করুন**
- শাখা আঁকতে পুনরাবৃত্তি ব্যবহার করুন
- প্রতিটি শাখা দুটি ছোট শাখায় বিভক্ত হয়
- প্রাকৃতিক পরিবর্তনের জন্য এলোমেলো কোণ ব্যবহার করুন
- শাখার দৈর্ঘ্য ট্র্যাক করুন এবং প্রতিটি পুনরাবৃত্তি স্তরের সাথে হ্রাস করুন
**ধাপ 3: সমাধানটি বাস্তবায়ন করুন**```scratch
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

**পদক্ষেপ 4: যাচাই করুন এবং অপ্টিমাইজ করুন**
নান্দনিক গাছের জন্য শাখার দৈর্ঘ্য থ্রেশহোল্ড এবং কোণের রেঞ্জ সামঞ্জস্য করুন। রঙ পরিবর্তন ব্যবহার করে শাখা টিপস এ পাতা যোগ করুন. বিভিন্ন গাছের শৈলী প্রয়োগ করুন। ছবি হিসাবে অঙ্কন সংরক্ষণ করুন.
---

## সারাংশ
স্ক্র্যাচ ঐতিহ্যগত অর্থে একটি প্রোগ্রামিং ভাষা নয় - এটি একটি শেখার পরিবেশ। এর প্রতিভা একটি শিশু এবং ইন্টারেক্টিভ কিছু তৈরি করার আনন্দের মধ্যে প্রতিটি বাধা দূর করছে। সিনট্যাক্সের পরিবর্তে ধারণাগুলির উপর ফোকাস করে, স্ক্র্যাচ প্রোগ্রামিংয়ের মৌলিক বিষয়গুলি শেখায় যা যেকোনো ভাষায় স্থানান্তরিত হয়। তরুণ শিক্ষার্থীদের কাছে প্রোগ্রামিং চালু করার জন্য, স্ক্র্যাচ হল সোনার মান।