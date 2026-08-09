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

＃ 刮痕
Scratch 是一種基於區塊的視覺化程式語言，由麻省理工學院媒體實驗室開發，於 2007 年首次發布。使用者無需編寫基於文字的程式碼，而是將彩色區塊組合在一起來創建程式。 Scratch 專為 8-16 歲的兒童設計（儘管所有年齡層的學習者都使用它），用於教授基本程式設計概念（循環、條件、變數、事件和函數），而不會出現語法錯誤。
Scratch 是世界上使用最廣泛的入門程式語言，擁有超過 1 億註冊用戶，並提供 70 多種語言版本。它在網絡瀏覽器中運行並且免費。
---

## 為什麼 Scratch 很重要
- **最佳编程入门**：完全消除语法障碍。概念是透過視覺操縱來教導的。
- **计算思维**：教授分解、模式识别、抽象和算法设计。
- **创造力驱动**：孩子们创造游戏、动画、故事和音乐——学习编程是制作他们关心的东西的副产品。
- **全球覆盖**：在世界各地的学校中使用。有 70 多種語言版本。免費且基於瀏覽器。
- **社区**：Scratch 在线社区教授共享、混音和协作学习。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **不是「真正的」程式語言** |無法建立生產軟體、API 或系統 |過渡到 Python、JavaScript 或基於文字的語言 |
| **能力有限** |沒有文件 I/O、網絡或高級資料結構 |用於學習；轉向實際專案的文本語言|
| **效能** |解釋性強，複雜專案速度慢 |不是為效能關鍵型工作而設計的 |
| **年齡認知** |通常被視為「只適合孩子」 | Scratch是一種學習工具，而不是一種專業語言 |
---

## Scratch 是如何運作的
Scratch 程式（稱為「專案」）由**精靈**（字元/物件）組成，這些**精靈**響應在腳本中對齊在一起的**區塊**。
### 核心概念（透過模組教授）
|概念 |暫存區塊類別 |範例|
|---------|--------------------------------|---------|
| **序列** |運動、外觀 | “移動 10 步”然後“打個招呼” |
| **循環** |控制（黃色）| “重複 10”、“永遠”、“重複直到”|
| **條件** |控制（黃色）| 「如果...那麼」、「如果...那麼...否則」 |
| **變數** |變數（橘色）| “將分數設為 0”、「將分數改為 1」|
| **活動** |活動（黃色）| “當綠旗點擊時”，“當按鍵按下時” |
| **功能** |我的區塊（自訂）|定義可重複使用的區塊序列 |
| **清單（陣列）** |變數（橘色）| “新增至清單”、「清單項目」|
| **廣播** |活動 |在精靈之間傳送訊息 |
### 範例：簡單的遊戲邏輯
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

## 進階語法和模式
### 區塊類別詳細信息
Scratch 3.0 將區塊組織成顏色編碼的類別：
|類別 |顏色 |區塊類型 |
|----------|--------|-------------|
| **運動** |藍色|移動、轉動、轉到、滑行、指向、更改 x/y |
| **看起來** |紫色|說、思考、切換服裝、更改尺寸、顯示/隱藏 |
| **聲音** |粉紅色|播放聲音、停止聲音、改變音量、改變音調 |
| **活動** |黃色|當標記被點擊時，當按鍵被按下時，當精靈被點擊時，廣播 |
| **控制** |黃金|等待、重複、永遠、如果、如果-否則、重複直到、停止 |
| **感測** |淺藍色 |觸控、按鍵、滑鼠、距離、詢問/回答、計時器 |
| **操作員** |綠色|數學操作、文字操作、比較和/或/非、隨機 |
| **變數** |橘色|設定/更改變數、清單操作 |
| **我的區塊** |深紅色|自訂區塊定義（函數）|
### 進階區塊模式
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

### 自訂區塊（函數）
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

### 列表操作（陣列）
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

### 廣播（精靈間通訊）
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

## 架構與系統設計
### 事件驅動設計
Scratch 使用事件驅動的架構。每個腳本都以事件塊（帽子塊）開始，並運行以響應該事件。
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

### 專案結構
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

### 複製系統（物件建立）
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

## 專案配置與建置系統
### 暫存擴展
Scratch 支援官方和社群擴展，可添加以下功能：
|擴充|目的|
|------------|---------|
| **筆** |在舞台上繪製線條和形狀 |
| **視訊感測** |使用網路攝影機進行動作偵測 |
| **文字轉語音** |將文字轉換為語音 |
| **翻譯** |在語言之間翻譯文字 |
| **馬基馬基** |連接物理物件作為輸入 |
| **微：位元** |連接 BBC micro:bit 硬體 |
| **樂高腦力激盪** |控制樂高機器人 |
| **音樂** |演奏音符與樂器|
### 暫存檔案格式
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

### 離線編輯器
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

## 測試和調試
### 內建偵錯工具
Scratch 提供了幾個內建的工具來調試專案：
|工具|如何使用 |
|------|------------|
| **海龜模式** |右鍵單擊精靈並選擇“顯示調試”以查看坐標 |
| **可變監視器** |右鍵單擊變數並選擇“顯示”以即時查看其值 |
| **列出監視器** |以正常、行或列顯示方式檢視清單內容 |
| **渦輪模式** |按住 Shift 鍵的同時點選綠旗可加快執行速度 |
| **單步模式** |右鍵點選綠色標誌「單步」（減慢執行速度）|
### 偵錯模式
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

### 常見問題
|問題 |原因 |解決方案 |
|--------|--------|----------|
|精靈沒有回應 |沒有事件帽子塊|新增「當綠旗被點擊時」或其他事件 |
|克隆不工作 |克隆已創建但未顯示|在“當我作為克隆開始時”之後添加“顯示”塊 |
|精靈之間共享的變數 |全域變數與局部變數的混淆 |使用「僅針對此精靈」選項 |
|未收到廣播 |留言名稱錯誤 |驗證廣播和接收名稱完全符合 |
|無限循環凍結| “永遠”，無需等待 |在緊密循環中添加小“等待”塊 |
---

## 互通性
### 硬體擴展
Scratch可以透過擴充連接到實體硬體：
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

### Scratch 擴充 API（自訂擴充功能）
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

## 設計模式
### 模式 1：平台遊戲運動
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

### 模式 2：滾動背景
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

### 模式 3：精​​神跟隨（Chase AI）
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### 模式 4：有清單的庫存系統
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

### 模式 5：有克隆的粒子系統
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

## 效能與最佳化
### 精靈最佳化
|技術|影響 |描述 |
|------------|--------|-------------|
| **最大限度地減少克隆** |高|每個克隆都會消耗內存；完成後刪除 |
| **減少服裝** |中|更少的服裝切換意味著更少的渲染開銷 |
| **使用「不刷新螢幕運行」** |高|無需螢幕刷新的自訂區塊運行速度更快 |
| **限制「說」區塊** |中|語音氣泡導致渲染開銷 |
| **避免在每個精靈中「永遠」** |中|使用廣播和事件而不是不斷的輪詢 |
### 克隆管理
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

### 優化清單
|技術|影響 |描述 |
|------------|--------|-------------|
| **運行時無需刷新螢幕** |非常高 |自訂區塊跳過渲染以提高速度 |
| **最大限度地減少活動克隆** |高|不再需要克隆時立即將其刪除 |
| **謹慎使用廣播** |中|每幀廣播太多導致延遲 |
| **簡化服裝** |中|較小的圖像渲染速度更快 |
| **減少清單操作** |中|避免每幀掃描大型清單 |
| **使用「等待」區塊** |低|防止 CPU 陷入無限循環 |
---

## 部署和實際使用
### 共享項目
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

### 現實世界的教育用途
|背景 |如何使用Scratch |規模|
|--------|--------------------|--------|
| **K-12 學校** | CS課程程式設計簡介|在 190 多個國家/地區使用 |
| **編碼俱樂部** | Scratch Club / CoderDojo 研討會 |全球 3000+ 俱樂部 |
| **圖書館** |課後程式設計課程|公共圖書館系統|
| **在家上學** |自定進度的程式教育 |數以百萬計的家庭學習者|
| **大學CS0** |非專業CS入門課程 |大學橋樑課程|
| **輔助功能** |教導視障人士程式設計|螢幕閱讀器支援 |
| **治療** |認知與運動技能發展 |職能治療|
### 教育研究中的 Scratch
研究表明，Scratch 可以有效地教授：
- **順序思考**：將問題分解為有序的步驟
- **偵錯技巧**：尋找並修復邏輯錯誤
- **創意表達**：結合藝術、音樂和編程
- **協作**：重新混合並建構其他人的項目
- **堅持**：迭代項目以改進它們
---

## 從頭開始過渡
學習 Scratch 後，典型的後續步驟包括：
|下一個語言 |為什麼 |
|--------------|-----|
| **Python** |最自然的過渡－可讀的語法，相似的邏輯概念|
| **JavaScript** |如果對網頁/遊戲有興趣 - 即時視覺回饋 |
| **Lua（取自 Roblox/Love2D）** |如果對遊戲開發有興趣 |
| **應用程式發明者** | Android 應用程式的視覺區塊（與 MIT 血統相同）|
| **塊狀** | Google的視覺化程式庫（類似概念） |
### 概念圖：從 Scratch 到 Python
|刮刮概念| Python 等效項 |
|----------------|--------------------|
|`set [x] to 0`|`x = 0`|
|`change [x] by 1`|`x += 1`|
|`repeat 10`|`for i in range(10):`|
|`forever`|`while True:`|
|`if ... then`|`if ...:`|
|`broadcast [msg]`|函數呼叫或事件系統|
|`My Blocks`|`def function():`|
|`list`|`list = []`|
|`item 1 of [list]`| `list[0]`（0索引！）|
|`length of [list]`|`len(list)`|
---

## 何時使用 Scratch
|場景 |為什麼要從頭開始？更好的選擇|
|----------|----------|--------------------|
|教導孩子（8-16 歲）編碼 |專為此設計 | — |
|介紹運算思維 |視覺化，無文法錯誤 | — |
|學校研討會/編碼俱樂部|免費、基於瀏覽器、無需設定 | — |
|直觀地製作遊戲創意原型 |快速迭代 | — |
|專業發展|不是為此設計的 | Python、JavaScript、任何文字語言 |
|大學級電腦科學教育 |太簡單了| Python、Java、C |
---

＃＃ 概括
Scratch 不是傳統意義上的程式語言－它是一個學習環境。它的天才在於消除了孩子與創造互動事物的樂趣之間的所有障礙。透過專注於概念而不是文法，Scratch 教授可遷移到任何語言的程式設計基礎知識。對於向年輕學習者介紹編程，Scratch 是黃金標準。