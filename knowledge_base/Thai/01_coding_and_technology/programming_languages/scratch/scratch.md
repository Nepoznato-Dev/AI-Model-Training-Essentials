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

# เกา
Scratch เป็นภาษาโปรแกรมแบบบล็อกภาพซึ่งพัฒนาโดย MIT Media Lab และเปิดตัวครั้งแรกในปี 2550 แทนที่จะเขียนโค้ดแบบข้อความ ผู้ใช้จะรวมบล็อกสีเข้าด้วยกันเพื่อสร้างโปรแกรม Scratch ได้รับการออกแบบมาโดยเฉพาะสำหรับเด็กอายุ 8-16 ปี (แม้ว่าผู้เรียนทุกวัยจะใช้ก็ตาม) เพื่อสอนแนวคิดการเขียนโปรแกรมขั้นพื้นฐาน เช่น ลูป เงื่อนไข ตัวแปร เหตุการณ์ และฟังก์ชัน โดยไม่มีอุปสรรคจากข้อผิดพลาดทางไวยากรณ์
Scratch เป็นภาษาการเขียนโปรแกรมเบื้องต้นที่ใช้กันอย่างแพร่หลายที่สุดในโลก โดยมีผู้ใช้ที่ลงทะเบียนมากกว่า 100 ล้านคน และพร้อมให้บริการในกว่า 70 ภาษา มันทำงานบนเว็บเบราว์เซอร์และฟรี
---

## ทำไมรอยขีดข่วนจึงมีความสำคัญ
- **บทแนะนำการเขียนโปรแกรมที่ดีที่สุด**: ขจัดอุปสรรคทางไวยากรณ์ทั้งหมด แนวคิดต่างๆ ได้รับการสอนผ่านการปรุงแต่งด้วยภาพ
- **การคิดเชิงคำนวณ**: สอนการแยกส่วน การจดจำรูปแบบ นามธรรม และการออกแบบอัลกอริทึม
- **ขับเคลื่อนด้วยความคิดสร้างสรรค์**: เด็กๆ สร้างเกม แอนิเมชัน เรื่องราว และเพลง — การเรียนรู้การเขียนโปรแกรมเป็นผลพลอยได้จากการทำสิ่งที่พวกเขาใส่ใจ
- **การเข้าถึงทั่วโลก**: ใช้ในโรงเรียนทั่วโลก มีให้บริการในกว่า 70 ภาษา ฟรีและใช้งานบนเบราว์เซอร์
- **ชุมชน**: ชุมชนออนไลน์ Scratch สอนการแบ่งปัน การรีมิกซ์ และการเรียนรู้ร่วมกัน
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ไม่ใช่ภาษาโปรแกรม "ของจริง"** | ไม่สามารถสร้างซอฟต์แวร์ที่ใช้งานจริง, API หรือระบบได้ | การเปลี่ยนไปใช้ Python, JavaScript หรือภาษาแบบข้อความ |
| **ความสามารถจำกัด** | ไม่มีไฟล์ I/O, ระบบเครือข่าย หรือโครงสร้างข้อมูลขั้นสูง | ใช้สำหรับการเรียนรู้ ย้ายไปใช้ภาษาข้อความสำหรับโครงการจริง |
| **ประสิทธิภาพ** | ตีความช้าสำหรับโครงการที่ซับซ้อน | ไม่ได้ออกแบบมาสำหรับงานที่เน้นประสิทธิภาพ |
| **การรับรู้เรื่องอายุ** | มักถูกมองว่าเป็น "เพียงสำหรับเด็ก" | Scratch เป็นเครื่องมือการเรียนรู้ ไม่ใช่ภาษาระดับมืออาชีพ |
---

## รอยขีดข่วนทำงานอย่างไร
โปรแกรม Scratch (เรียกว่า "โปรเจ็กต์") ประกอบด้วย **สไปรต์** (อักขระ/วัตถุ) ที่ตอบสนองต่อ **บล็อก** ที่รวมเข้าด้วยกันในสคริปต์
### แนวคิดหลัก (สอนผ่านบล็อก)
| แนวคิด | หมวดหมู่บล็อกรอยขีดข่วน | ตัวอย่าง |
|---------|-----------------|---------|
| **ลำดับ** | การเคลื่อนไหว รูปลักษณ์ | "ขยับ 10 ก้าว" จากนั้น "ทักทาย" |
| **วนซ้ำ** | ควบคุม (สีเหลือง) | "ทำซ้ำ 10", "ตลอดไป", "ทำซ้ำจนกว่า" |
| **เงื่อนไข** | ควบคุม (สีเหลือง) | "ถ้า... แล้ว", "ถ้า... แล้ว... อย่างอื่น" |
| **ตัวแปร** | ตัวแปร (สีส้ม) | "กำหนดคะแนนเป็น 0", "เปลี่ยนคะแนนเป็น 1" |
| **กิจกรรม** | กิจกรรม (สีเหลือง) | "เมื่อคลิกธงเขียว", "เมื่อกดปุ่ม" |
| **ฟังก์ชั่น** | บล็อกของฉัน (กำหนดเอง) | กำหนดลำดับบล็อกที่ใช้ซ้ำได้ |
| **รายการ (อาร์เรย์)** | ตัวแปร (สีส้ม) | "เพิ่มในรายการ", "รายการในรายการ" |
| **การออกอากาศ** | กิจกรรม | ส่งข้อความระหว่างสไปรท์ |
### ตัวอย่าง: ตรรกะของเกมอย่างง่าย
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

## ไวยากรณ์และรูปแบบขั้นสูง
### หมวดหมู่บล็อกโดยละเอียด
Scratch 3.0 จัดระเบียบบล็อกเป็นหมวดหมู่รหัสสี:
| หมวดหมู่ | สี | ประเภทบล็อก |
|----------|--------|-------------|
| **การเคลื่อนไหว** | สีฟ้า | ย้าย เลี้ยว ข้ามไป ร่อน ชี้ เปลี่ยน x/y |
| **รูปลักษณ์** | สีม่วง | พูด คิด สลับชุด เปลี่ยนขนาด แสดง/ซ่อน |
| **เสียง** | สีชมพู | เล่นเสียง, หยุดเสียง, เปลี่ยนระดับเสียง, เปลี่ยนระดับเสียง |
| **กิจกรรม** | เหลือง | เมื่อคลิกธง เมื่อกดปุ่ม เมื่อคลิกสไปรท์ ออกอากาศ |
| **การควบคุม** | ทอง | รอ, ทำซ้ำ, ตลอดไป, ถ้า, if-else, ทำซ้ำจนกระทั่ง, หยุด |
| **การตรวจจับ** | ฟ้าอ่อน | การสัมผัส การกดปุ่ม เมาส์ ระยะทาง ถาม/ตอบ ตัวจับเวลา |
| **ผู้ประกอบการ** | เขียว | ตัวเลือกทางคณิตศาสตร์ ตัวเลือกข้อความ การเปรียบเทียบ และ/หรือ/ไม่ใช่ สุ่ม |
| **ตัวแปร** | ส้ม | ตั้งค่า/เปลี่ยนตัวแปร การดำเนินการรายการ |
| **บล็อกของฉัน** | แดงเข้ม | คำจำกัดความของบล็อกแบบกำหนดเอง (ฟังก์ชัน) |
### รูปแบบบล็อกขั้นสูง
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

### บล็อกแบบกำหนดเอง (ฟังก์ชัน)
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

### การดำเนินการรายการ (อาร์เรย์)
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

### การออกอากาศ (การสื่อสารระหว่างสไปรท์)
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

## สถาปัตยกรรมและการออกแบบระบบ
### การออกแบบที่ขับเคลื่อนด้วยเหตุการณ์
Scratch ใช้สถาปัตยกรรมที่ขับเคลื่อนด้วยเหตุการณ์ ทุกสคริปต์เริ่มต้นด้วยบล็อกเหตุการณ์ (บล็อกหมวก) และทำงานเพื่อตอบสนองต่อเหตุการณ์นั้น
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

### โครงสร้างโครงการ
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

### ระบบโคลน (การสร้างวัตถุ)
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### ส่วนขยายรอยขีดข่วน
Scratch รองรับส่วนขยายอย่างเป็นทางการและชุมชนที่เพิ่มความสามารถ:
| ส่วนขยาย | วัตถุประสงค์ |
|----------|---------|
| **ปากกา** | วาดเส้นและรูปร่างบนเวที |
| **การตรวจจับวิดีโอ** | ใช้เว็บแคมเพื่อตรวจจับการเคลื่อนไหว |
| **ข้อความเป็นคำพูด** | แปลงข้อความเป็นเสียงพูด |
| **แปล** | แปลข้อความระหว่างภาษา |
| **เมกี เมกี** | เชื่อมต่อวัตถุทางกายภาพเป็นอินพุต |
| **ไมโคร:บิต** | เชื่อมต่อฮาร์ดแวร์ BBC micro:bit |
| **เลโก้ มายสตอร์ม** | ควบคุมหุ่นยนต์ LEGO |
| **ดนตรี** | เล่นโน้ตดนตรีและเครื่องดนตรี |
### รูปแบบไฟล์รอยขีดข่วน
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

### ตัวแก้ไขออฟไลน์
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

## การทดสอบและการดีบัก
### เครื่องมือแก้ไขข้อบกพร่องในตัว
Scratch มีเครื่องมือในตัวมากมายสำหรับการดีบักโปรเจ็กต์:
| เครื่องมือ | วิธีใช้ |
|------|-----------|
| **โหมดเต่า** | คลิกขวาที่สไปรท์แล้วเลือก "แสดงการแก้ไขข้อบกพร่อง" เพื่อดูพิกัด |
| **จอภาพแปรผัน** | คลิกขวาที่ตัวแปรและเลือก "แสดง" เพื่อดูค่าแบบเรียลไทม์ |
| **รายการจอภาพ** | ดูเนื้อหารายการในรูปแบบปกติ แถว หรือคอลัมน์ |
| **โหมดเทอร์โบ** | กด Shift ค้างไว้ขณะคลิกธงสีเขียวเพื่อการดำเนินการที่รวดเร็วขึ้น |
| **โหมดขั้นตอนเดียว** | คลิกขวาที่ธงสีเขียวสำหรับ "ขั้นตอนเดียว" (ดำเนินการช้าลง) |
### รูปแบบการแก้ไขข้อบกพร่อง
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

### ปัญหาทั่วไป
| ปัญหา | สาเหตุ | โซลูชั่น |
|---------|-------|----------|
| สไปรท์ไม่ตอบสนอง | ไม่มีกิจกรรมหมวกบล็อก | เพิ่ม "เมื่อคลิกธงเขียว" หรือกิจกรรมอื่น |
| โคลนไม่ทำงาน | สร้างโคลนแล้วแต่ไม่แสดง | เพิ่มบล็อก "แสดง" หลัง "เมื่อฉันเริ่มเป็นโคลน" |
| ตัวแปรที่ใช้ร่วมกันระหว่างสไปรท์ | ความสับสนของตัวแปร Global และ Local | ใช้ตัวเลือก "สำหรับสไปรท์นี้เท่านั้น" |
| ไม่ได้รับการออกอากาศ | ชื่อข้อความผิด | ตรวจสอบการออกอากาศและรับชื่อให้ตรงกันทุกประการ |
| การหยุดวนซ้ำไม่สิ้นสุด | “ตลอดไป” โดยไม่ต้องรอ | เพิ่มบล็อก "รอ" ขนาดเล็กในลูปแน่น |
---

## การทำงานร่วมกัน
### ส่วนขยายฮาร์ดแวร์
Scratch สามารถเชื่อมต่อกับฮาร์ดแวร์กายภาพผ่านส่วนขยาย:
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

### Scratch Extensions API (ส่วนขยายที่กำหนดเอง)
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

## รูปแบบการออกแบบ
### รูปแบบ 1: การเคลื่อนไหวของ Platformer
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

### รูปแบบ 2: พื้นหลังการเลื่อน
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

### รูปแบบ 3: สไปรท์ติดตาม (ไล่ AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### รูปแบบ 4: ระบบสินค้าคงคลังพร้อมรายการ
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

### รูปแบบ 5: ระบบอนุภาคพร้อมโคลน
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
### การเพิ่มประสิทธิภาพสไปรท์
| เทคนิค | ผลกระทบ | คำอธิบาย |
|----------|--------|-------------|
| **ย่อขนาดโคลนให้เล็กสุด** | สูง | แต่ละโคลนใช้หน่วยความจำ ลบเมื่อเสร็จแล้ว |
| **ลดเครื่องแต่งกาย** | ปานกลาง | สวิตช์เครื่องแต่งกายที่น้อยลงหมายถึงค่าใช้จ่ายในการเรนเดอร์น้อยลง |
| **ใช้ "ทำงานโดยไม่รีเฟรชหน้าจอ"** | สูง | บล็อกแบบกำหนดเองที่ไม่มีการรีเฟรชหน้าจอจะทำงานเร็วขึ้น |
| **จำกัดการบล็อก "พูด"** | ปานกลาง | ฟองคำพูดทำให้เกิดการเรนเดอร์โอเวอร์เฮด |
| **หลีกเลี่ยง "ตลอดไป" ในทุกสไปรท์** | ปานกลาง | ใช้การออกอากาศและกิจกรรมแทนการสำรวจความคิดเห็นอย่างต่อเนื่อง |
### การจัดการโคลน
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

### รายการตรวจสอบการเพิ่มประสิทธิภาพ
| เทคนิค | ผลกระทบ | คำอธิบาย |
|----------|--------|-------------|
| **ทำงานโดยไม่รีเฟรชหน้าจอ** | สูงมาก | บล็อกที่กำหนดเองข้ามการเรนเดอร์เพื่อความรวดเร็ว |
| **ย่อขนาดโคลนที่ใช้งานอยู่ให้น้อยที่สุด** | สูง | ลบโคลนทันทีที่ไม่ต้องการอีกต่อไป |
| **ใช้การออกอากาศเท่าที่จำเป็น** | ปานกลาง | การออกอากาศต่อเฟรมมากเกินไปทำให้เกิดความล่าช้า |
| **ทำให้เครื่องแต่งกายง่ายขึ้น** | ปานกลาง | รูปภาพที่เล็กลงจะเรนเดอร์เร็วขึ้น |
| **ลดการดำเนินการรายการ** | ปานกลาง | หลีกเลี่ยงการสแกนรายการขนาดใหญ่ทุกๆ เฟรม |
| **ใช้บล็อก "รอ"** | ต่ำ | ป้องกันไม่ให้ CPU hogging ในลูปตลอดไป |
---

## การปรับใช้และการใช้งานในโลกแห่งความเป็นจริง
### โครงการแบ่งปัน
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

### การใช้การศึกษาในโลกแห่งความเป็นจริง
| บริบท | วิธีใช้ Scratch | สเกล |
|---------|-------------------|-------|
| **โรงเรียนอนุบาลถึงมัธยมศึกษาตอนปลาย** | ความรู้เบื้องต้นเกี่ยวกับการเขียนโปรแกรมในคลาส CS | ใช้ในกว่า 190 ประเทศ |
| **ชมรมเขียนโค้ด** | เวิร์กช็อป Scratch Club / CoderDojo | 3,000+ สโมสรทั่วโลก |
| **ห้องสมุด** | โปรแกรมเขียนโปรแกรมหลังเลิกเรียน | ระบบห้องสมุดสาธารณะ |
| **โฮมสคูล** | การศึกษาการเขียนโปรแกรมด้วยตนเอง | ผู้เรียนที่บ้านหลายล้านคน |
| **มหาวิทยาลัย CS0** | หลักสูตร CS เบื้องต้นที่ไม่ใช่วิชาเอก | โปรแกรมสะพานมหาวิทยาลัย |
| **การเข้าถึง** | สอนเขียนโปรแกรมสำหรับผู้พิการทางสายตา | รองรับโปรแกรมอ่านหน้าจอ |
| **การบำบัด** | การพัฒนาทักษะทางปัญญาและการเคลื่อนไหว | กิจกรรมบำบัด |
### รอยขีดข่วนในการวิจัยด้านการศึกษา
การวิจัยแสดงให้เห็นว่า Scratch สอนสิ่งต่อไปนี้ได้อย่างมีประสิทธิภาพ
- **การคิดตามลำดับ**: แบ่งปัญหาเป็นขั้นตอนตามลำดับ
- **ทักษะการแก้ไขจุดบกพร่อง**: การค้นหาและแก้ไขข้อผิดพลาดในตรรกะ
- **การแสดงออกอย่างสร้างสรรค์**: ผสมผสานศิลปะ ดนตรี และรายการ
- **การทำงานร่วมกัน**: การรีมิกซ์และสร้างโปรเจ็กต์ของผู้อื่น
- **ความคงอยู่**: ทำซ้ำโครงการเพื่อปรับปรุง
---

## การเปลี่ยนจากศูนย์
หลังจากเรียนรู้ Scratch แล้ว ขั้นตอนถัดไปโดยทั่วไปได้แก่:
| ภาษาถัดไป | ทำไม |
|--------------|-----|
| **หลาม** | การเปลี่ยนแปลงที่เป็นธรรมชาติที่สุด — ไวยากรณ์ที่อ่านได้, แนวคิดตรรกะที่คล้ายกัน |
| **จาวาสคริปต์** | หากสนใจเว็บ/เกม — ตอบรับด้วยภาพทันที |
| **หลัว (ผ่าน Roblox/Love2D)** | หากสนใจในการพัฒนาเกม |
| **นักประดิษฐ์แอป** | บล็อกภาพสำหรับแอป Android (เชื้อสาย MIT เดียวกัน) |
| **บล็อก** | ไลบรารีการเขียนโปรแกรมภาพของ Google (แนวคิดที่คล้ายกัน) |
### การทำแผนที่แนวคิด: เกาเป็น Python
| แนวคิดรอยขีดข่วน | เทียบเท่าหลาม |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| การเรียกใช้ฟังก์ชันหรือระบบเหตุการณ์ |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(ดัชนี 0!) |
| `length of [list]`| `len(list)`|
---

## เมื่อใดจึงควรใช้ Scratch
| สถานการณ์ | ทำไมต้องเกา | ทางเลือกที่ดีกว่า |
|----------|-----------|-------------------|
| การสอนเด็ก (8-16) ให้เขียนโค้ด | ออกแบบมาโดยเฉพาะสำหรับสิ่งนี้ | — |
| แนะนำการคิดคำนวณ | ภาพ ไม่มีข้อผิดพลาดทางไวยากรณ์ | — |
| เวิร์คช็อปของโรงเรียน / ชมรมเขียนโค้ด | ฟรี ใช้เบราว์เซอร์ ไม่ต้องตั้งค่า | — |
| การสร้างต้นแบบไอเดียเกมด้วยสายตา | ทำซ้ำอย่างรวดเร็ว | — |
| การพัฒนาวิชาชีพ | ไม่ได้ออกแบบมาสำหรับสิ่งนี้ | Python, JavaScript, ภาษาข้อความใด ๆ |
| การศึกษา CS ระดับมหาวิทยาลัย | ง่ายเกินไป | หลาม, จาวา, ซี |
---

## คำถามและคำตอบสังเคราะห์
**คำถามที่ 1: Scratch เป็นภาษาการเขียนโปรแกรมจริงหรือ**
ตอบ 1: ใช่ Scratch เป็นภาษาโปรแกรมจริงๆ แต่เป็นภาพมากกว่าข้อความ รองรับแนวคิดการเขียนโปรแกรมพื้นฐานทั้งหมด: ตัวแปร ลูป เงื่อนไข ฟังก์ชัน (บล็อกแบบกำหนดเอง) รายการ และการเขียนโปรแกรมที่ขับเคลื่อนด้วยเหตุการณ์ ความแตกต่างก็คือคุณลากและวางบล็อกแทนการพิมพ์โค้ด ซึ่งช่วยลดข้อผิดพลาดทางไวยากรณ์และทำให้ผู้เรียนรุ่นเยาว์เข้าถึงการเขียนโปรแกรมได้
**คำถามที่ 2: ฉันจะสร้างฟังก์ชันแบบกำหนดเอง (บล็อกแบบกำหนดเอง) ใน Scratch ได้อย่างไร**
A2: ไปที่หมวดหมู่ "บล็อกของฉัน" และคลิก "สร้างบล็อก" ตั้งชื่อ เพิ่มพารามิเตอร์หากจำเป็น จากนั้นกำหนดลักษณะการทำงานโดยเพิ่มบล็อกด้านล่าง บล็อกแบบกำหนดเองสามารถรับอินพุต (ตัวเลข สตริง บูลีน) และสามารถเรียกบล็อกแบบกำหนดเองอื่นๆ ได้ ช่วยให้การเขียนโปรแกรมแบบโมดูลาร์และการนำโค้ดกลับมาใช้ใหม่ได้
**คำถามที่ 3: วิธีใดคือวิธีที่ดีที่สุดในการจัดการตรรกะของเกมที่ซับซ้อนใน Scratch**
A3: ใช้บล็อกแบบกำหนดเองเพื่อจัดระเบียบตรรกะ ออกอากาศข้อความสำหรับการประสานงานกิจกรรมระหว่างสไปรท์ และใช้รายการเพื่อจัดเก็บสถานะของเกม (คะแนน ระดับ สินค้าคงคลัง) สำหรับ AI ที่ซับซ้อน ให้ใช้เครื่องสถานะจำกัดพร้อมตัวแปรที่ติดตามสถานะปัจจุบัน โคลนสไปรต์สำหรับศัตรูหลายตัว และใช้ "เมื่อฉันเริ่มเป็นโคลน" เพื่อให้แต่ละพฤติกรรมเป็นอิสระ
**คำถามที่ 4: ฉันจะแชร์ข้อมูลระหว่างสไปรท์ใน Scratch ได้อย่างไร**
A4: ใช้ตัวแปรส่วนกลาง (สร้างโดยไม่มี "สำหรับสไปรท์นี้เท่านั้น") สำหรับข้อมูลที่แชร์ เช่น คะแนนหรือสถานะของเกม ใช้ข้อความออกอากาศเพื่อกระตุ้นเหตุการณ์ข้ามสไปรท์ สำหรับการสื่อสารที่ซับซ้อนมากขึ้น ให้ใช้รายการเป็นโครงสร้างข้อมูลที่ใช้ร่วมกัน สไปรท์แต่ละตัวสามารถอ่านและแก้ไขตัวแปรและรายการส่วนกลางได้ ทำให้เกิดการประสานงานกัน
**คำถามที่ 5: เทคนิคขั้นสูงใน Scratch มีอะไรบ้าง**
A5: ใช้บล็อคปากกาในการวาดภาพและสร้างเอฟเฟ็กต์ภาพ ใช้ raycasting สำหรับกราฟิกที่มีลักษณะคล้าย 3D ใช้ตัวแปรคลาวด์สำหรับเกมที่มีผู้เล่นหลายคน (ต้องมีสถานะ Scratcher) สร้างขั้นตอนการสร้างด้วยตัวเลขและรายการสุ่ม ใช้บล็อกที่กำหนดเองพร้อมพารามิเตอร์สำหรับอัลกอริทึมที่นำมาใช้ซ้ำได้ ทดลองใช้การตรวจจับวิดีโอและการปรับแต่งเสียงสำหรับโปรเจ็กต์แบบโต้ตอบ
---

## ห่วงโซ่แห่งความคิด
### ปัญหาที่ 1: การสร้างเกม Platformer
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
เราจำเป็นต้องสร้างเกมแพลตฟอร์มที่ตัวละครสามารถเคลื่อนที่ไปทางซ้าย/ขวา กระโดด หลีกเลี่ยงอุปสรรค และรวบรวมไอเท็มได้
**ขั้นตอนที่ 2: ระบุแนวทาง**
- ใช้การจำลองแรงโน้มถ่วงด้วยตัวแปร "ตก"
- ตรวจจับพื้น/การชนโดยใช้สีหรือการสัมผัสสไปรท์
- ข้อมูลระดับร้านค้าในรายการ
- ใช้บล็อกแบบกำหนดเองสำหรับการกระโดดและตรรกะการเคลื่อนไหว
**ขั้นตอนที่ 3: นำโซลูชันไปใช้**```scratch
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

**ขั้นตอนที่ 4: ตรวจสอบและเพิ่มประสิทธิภาพ**
ทดสอบการกระโดดบนแพลตฟอร์มต่างๆ ปรับแรงโน้มถ่วงและความสูงของการกระโดดเพื่อความรู้สึกที่ดีในเกม เพิ่มภาพเคลื่อนไหวสำหรับการวิ่งและการกระโดด ใช้จุดตรวจโดยใช้ข้อความออกอากาศ
---

### ปัญหาที่ 2: การสร้างเกมตอบคำถามพร้อมการติดตามคะแนน
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
สร้างเกมตอบคำถามที่ถามคำถาม ตรวจคำตอบ และติดตามคะแนนของผู้เล่น
**ขั้นตอนที่ 2: ระบุแนวทาง**
- เก็บคำถามและคำตอบไว้ในรายการคู่ขนาน
- ใช้ตัวนับคำถามเพื่อติดตามความคืบหน้า
- ใช้บล็อก "ถามและรอ" เพื่อป้อนข้อมูล
- เปรียบเทียบคำตอบและอัปเดตคะแนน
**ขั้นตอนที่ 3: นำโซลูชันไปใช้**```scratch
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

**ขั้นตอนที่ 4: ตรวจสอบและเพิ่มประสิทธิภาพ**
ทดสอบด้วยคำตอบที่หลากหลาย รวมถึง Edge Case เพิ่มข้อเสนอแนะสำหรับคำตอบที่ผิด ใช้ตัวเลือกการลองใหม่ เพิ่มเอฟเฟกต์เสียงและการตอบรับด้วยภาพสำหรับคำตอบที่ถูก/ผิด
---

### ปัญหาที่ 3: การวาดต้นไม้แฟร็กทัลด้วยปากกา
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
สร้างแผนภูมิเศษส่วนแบบเรียกซ้ำโดยใช้ส่วนขยายปากกา
**ขั้นตอนที่ 2: ระบุแนวทาง**
- ใช้การเรียกซ้ำเพื่อวาดกิ่งก้าน
- แต่ละสาขาจะแยกออกเป็นสองสาขาย่อย
- ใช้มุมสุ่มสำหรับการแปรผันตามธรรมชาติ
- ติดตามความยาวของสาขาและลดระดับการเรียกซ้ำแต่ละระดับ
**ขั้นตอนที่ 3: นำโซลูชันไปใช้**```scratch
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

**ขั้นตอนที่ 4: ตรวจสอบและเพิ่มประสิทธิภาพ**
ปรับเกณฑ์ความยาวกิ่งและช่วงมุมสำหรับต้นไม้ที่สวยงาม เพิ่มใบไม้ที่ปลายกิ่งโดยใช้การเปลี่ยนสี ใช้สไตล์ต้นไม้ที่แตกต่างกัน บันทึกภาพวาดเป็นรูปภาพ
---

## สรุป
Scratch ไม่ใช่ภาษาการเขียนโปรแกรมในความหมายดั้งเดิม แต่เป็นสภาพแวดล้อมการเรียนรู้ ความอัจฉริยะของมันคือการขจัดอุปสรรคทุกอย่างระหว่างเด็กและความสุขของการสร้างสรรค์สิ่งที่โต้ตอบได้ ด้วยการมุ่งเน้นไปที่แนวคิดมากกว่าไวยากรณ์ Scratch จะสอนพื้นฐานของการเขียนโปรแกรมที่สามารถถ่ายโอนไปยังภาษาใดก็ได้ สำหรับการแนะนำการเขียนโปรแกรมให้กับผู้เรียนรุ่นเยาว์ Scratch คือมาตรฐานทองคำ