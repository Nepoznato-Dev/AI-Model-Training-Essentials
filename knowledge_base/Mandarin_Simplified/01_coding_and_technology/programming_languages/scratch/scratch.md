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
＃ 划痕
Scratch 是一种基于块的可视化编程语言，由麻省理工学院媒体实验室开发，于 2007 年首次发布。用户无需编写基于文本的代码，而是将彩色块组合在一起来创建程序。 Scratch 专为 8-16 岁的儿童设计（尽管所有年龄段的学习者都使用它），用于教授基本编程概念（循环、条件、变量、事件和函数），而不会出现语法错误。
Scratch 是世界上使用最广泛的入门编程语言，拥有超过 1 亿注册用户，并提供 70 多种语言版本。它在网络浏览器中运行并且免费。
---

## 为什么 Scratch 很重要
- **最佳编程入门**：完全消除语法障碍。概念是通过视觉操纵来教授的。
- **计算思维**：教授分解、模式识别、抽象和算法设计。
- **创造力驱动**：孩子们创造游戏、动画、故事和音乐——学习编程是制作他们关心的东西的副产品。
- **全球覆盖**：在世界各地的学校中使用。有 70 多种语言版本。免费且基于浏览器。
- **社区**：Scratch 在线社区教授共享、混音和协作学习。
## 权衡
|限制|详情 |典型解决方法|
|------------|---------|--------------------|
| **不是“真正的”编程语言** |无法构建生产软件、API 或系统 |过渡到 Python、JavaScript 或基于文本的语言 |
| **能力有限** |没有文件 I/O、网络或高级数据结构 |用于学习；转向实际项目的文本语言|
| **性能** |解释性强，复杂项目速度慢 |不是为性能关键型工作而设计的 |
| **年龄认知** |通常被视为“只适合孩子” | Scratch是一种学习工具，而不是一种专业语言 |
---

## Scratch 是如何工作的
Scratch 程序（称为“项目”）由**精灵**（字符/对象）组成，这些**精灵**响应在脚本中对齐在一起的**块**。
### 核心概念（通过模块教授）
|概念 |暂存块类别 |示例|
|---------|----------------------|---------|
| **序列** |运动、外观 | “移动 10 步”然后“打个招呼” |
| **循环** |控制（黄色）| “重复 10”、“永远”、“重复直到”|
| **条件** |控制（黄色）| “如果...那么”、“如果...那么...否则” |
| **变量** |变量（橙色）| “将分数设置为 0”、“将分数更改为 1”|
| **活动** |活动（黄色）| “当绿旗点击时”，“当按键按下时” |
| **功能** |我的块（自定义）|定义可重用的块序列 |
| **列表（数组）** |变量（橙色）| “添加到列表”、“列表项目”|
| **广播** |活动 |在精灵之间发送消息 |
### 示例：简单的游戏逻辑
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

## 高级语法和模式
### 块类别详细信息
Scratch 3.0 将块组织成颜色编码的类别：
|类别 |颜色 |块类型 |
|----------|--------|-------------|
| **运动** |蓝色|移动、转动、转到、滑行、指向、更改 x/y |
| **看起来** |紫色|说、思考、切换服装、更改尺寸、显示/隐藏 |
| **声音** |粉色|播放声音、停止声音、改变音量、改变音调 |
| **活动** |黄色|当标记被点击时，当按键被按下时，当精灵被点击时，广播 |
| **控制** |黄金|等待、重复、永远、如果、如果-否则、重复直到、停止 |
| **传感** |浅蓝色|触摸、按键、鼠标、距离、询问/回答、计时器 |
| **运营商** |绿色|数学操作、文本操作、比较和/或/非、随机 |
| **变量** |橙色|设置/更改变量、列表操作 |
| **我的区块** |深红色|自定义块定义（函数）|
### 高级块模式
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

### 自定义块（函数）
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

### 列表操作（数组）
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

### 广播（精灵间通信）
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

## 架构与系统设计
### 事件驱动设计
Scratch 使用事件驱动的架构。每个脚本都以事件块（帽子块）开始，并运行以响应该事件。
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

### 项目结构
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

### 克隆系统（对象创建）
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

## 项目配置和构建系统
### 暂存扩展
Scratch 支持官方和社区扩展，可添加以下功能：
|扩展|目的|
|------------|---------|
| **笔** |在舞台上绘制线条和形状 |
| **视频传感** |使用网络摄像头进行运动检测 |
| **文字转语音** |将文本转换为语音 |
| **翻译** |在语言之间翻译文本 |
| **马基马基** |连接物理对象作为输入 |
| **微：位** |连接 BBC micro:bit 硬件 |
| **乐高头脑风暴** |控制乐高机器人 |
| **音乐** |演奏音符和乐器|
### 暂存文件格式
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

### 离线编辑器
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

## 测试和调试
### 内置调试​​工具
Scratch 提供了几个用于调试项目的内置工具：
|工具|如何使用 |
|------|------------|
| **海龟模式** |右键单击精灵并选择“显示调试”以查看坐标|
| **可变监视器** |右键单击变量并选择“显示”以实时查看其值 |
| **列出监视器** |以正常、行或列显示方式查看列表内容 |
| **涡轮模式** |按住 Shift 键的同时单击绿旗可加快执行速度 |
| **单步模式** |右键单击绿色标志“单步”（减慢执行速度）|
### 调试模式
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

### 常见问题
|问题 |原因 |解决方案 |
|--------|--------|----------|
|精灵没有响应 |没有事件帽子块|添加“当绿旗被点击时”或其他事件 |
|克隆不工作 |克隆已创建但未显示 |在“当我作为克隆开始时”之后添加“显示”块 |
|精灵之间共享的变量 |全局变量与局部变量的混淆 |使用“仅针对此精灵”选项 |
|未收到广播 |留言名称错误 |验证广播和接收名称完全匹配 |
|无限循环冻结| “永远”，无需等待|在紧密循环中添加小“等待”块 |
---

## 互操作性
### 硬件扩展
Scratch可以通过扩展连接到物理硬件：
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

### Scratch 扩展 API（自定义扩展）
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

## 设计模式
### 模式 1：平台游戏运动
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

### 模式 2：滚动背景
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

### 模式 3：精​​灵跟随（Chase AI）
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### 模式 4：带有列表的库存系统
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

### 模式 5：带有克隆的粒子系统
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

## 性能与优化
### 精灵优化
|技术|影响 |描述 |
|------------|--------|-------------|
| **最大限度地减少克隆** |高|每个克隆都会消耗内存；完成后删除|
| **减少服装** |中等|更少的服装切换意味着更少的渲染开销 |
| **使用“不刷新屏幕运行”** |高|无需屏幕刷新的自定义块运行速度更快 |
| **限制“说”块** |中等|语音气泡导致渲染开销 |
| **避免在每个精灵中“永远”** |中等|使用广播和事件而不是不断的轮询 |
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

### 优化清单
|技术|影响 |描述 |
|------------|--------|-------------|
| **运行时无需刷新屏幕** |非常高 |自定义块跳过渲染以提高速度 |
| **最大限度地减少活动克隆** |高|不再需要克隆时立即将其删除 |
| **谨慎使用广播** |中等|每帧广播太多导致延迟 |
| **简化服装** |中等|较小的图像渲染速度更快 |
| **减少列表操作** |中等|避免每帧扫描大型列表 |
| **使用“等待”块** |低|防止 CPU 陷入无限循环 |
---

## 部署和实际使用
### 共享项目
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

### 现实世界的教育用途
|背景 |如何使用Scratch |规模|
|--------|--------------------|--------|
| **K-12 学校** | CS课程编程简介|在 190 多个国家/地区使用 |
| **编码俱乐部** | Scratch Club / CoderDojo 研讨会 |全球 3000+ 俱乐部 |
| **图书馆** |课后编程课程|公共图书馆系统|
| **在家上学** |自定进度的编程教育 |数以百万计的家庭学习者|
| **大学CS0** |非专业CS入门课程 |大学桥梁课程|
| **辅助功能** |向视障人士教授编程|屏幕阅读器支持 |
| **治疗** |认知和运动技能发展 |职业治疗|
### 教育研究中的 Scratch
研究表明，Scratch 可以有效地教授：
- **顺序思维**：将问题分解为有序的步骤
- **调试技巧**：查找并修复逻辑错误
- **创意表达**：结合艺术、音乐和编程
- **协作**：重新混合和构建其他人的项目
- **坚持**：迭代项目以改进它们
---

## 从头开始​​过渡
学习 Scratch 后，典型的后续步骤包括：
|下一个语言 |为什么 |
|--------------|-----|
| **Python** |最自然的过渡——可读的语法，相似的逻辑概念|
| **JavaScript** |如果对网络/游戏感兴趣 - 即时视觉反馈 |
| **Lua（来自 Roblox/Love2D）** |如果对游戏开发感兴趣 |
| **应用程序发明者** | Android 应用程序的视觉块（与 MIT 血统相同）|
| **块状** | Google的可视化编程库（类似概念） |
### 概念图：从 Scratch 到 Python
|刮刮概念| Python 等效项 |
|----------------|--------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`|函数调用或事件系统|
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`|  `list[0]`（0索引！）|
| `length of [list]`| `len(list)`|
---

## 何时使用 Scratch
|场景|为什么要从头开始？更好的选择|
|----------|----------|--------------------|
|教孩子（8-16 岁）编码 |专为此而设计 | — |
|介绍计算思维 |可视化，无语法错误 | — |
|学校研讨会/编码俱乐部|免费、基于浏览器、无需设置 | — |
|直观地制作游戏创意原型 |快速迭代 | — |
|专业发展|不是为此设计的 | Python、JavaScript、任何文本语言 |
|大学级计算机科学教育 |太简单了| Python、Java、C |
---

## 综合问答
**问题1：Scratch真的是一种编程语言吗？**
A1：是的，Scratch 是一种真正的编程语言，但它是可视化的而不是基于文本的。它支持所有基本编程概念：变量、循环、条件、函数（自定义块）、列表和事件驱动编程。不同之处在于您拖放块而不是键入代码。这消除了语法错误，并使年轻学习者可以轻松编程。
**问题2：如何在Scratch中创建自定义函数（自定义块）？**
A2：进入“我的区块”类别，点击“创建区块”。为其命名，根据需要添加参数，然后通过在其下方添加块来定义其行为。自定义块可以接受输入（数字、字符串、布尔值）并可以调用其他自定义块。这使得模块化编程和代码重用成为可能。
**问题3：在Scratch中处理复杂游戏逻辑的最佳方式是什么？**
A3：使用自定义块来组织逻辑，广播消息以在精灵之间进行事件协调，并使用列表来存储游戏状态（分数、级别、库存）。对于复杂的人工智能，请使用带有跟踪当前状态的变量的有限状态机。为多个敌人克隆精灵，并使用“当我作为克隆开始时”来赋予每个敌人独立的行为。
**问题4：如何在Scratch中的精灵之间共享数据？**
A4：使用全局变量（在没有“仅用于此精灵”的情况下创建）来共享数据，例如得分或游戏状态。使用广播消息来触发跨精灵的事件。对于更复杂的通信，请使用列表作为共享数据结构。每个精灵都可以读取和修改全局变量和列表，从而实现协调。
**Q5：Scratch中有哪些高级技巧？**
A5：使用笔块进行绘画和创建视觉效果。为类似 3D 的图形实现光线投射。将云变量用于多人游戏（需要 Scratcher 状态）。使用随机数和列表创建程序生成。使用带有参数的自定义块以实现可重用算法。尝试交互式项目的视频传感和声音处理。
---

## 思路
### 问题 1：创建平台游戏
**第 1 步：了解问题**
我们需要创建一个平台游戏，角色可以向左/向右移动、跳跃、避开障碍物和收集物品。
**第 2 步：确定方法**
- 使用带有“下落”变量的重力模拟
- 使用颜色或精灵触摸检测地面/碰撞
- 将关卡数据存储在列表中
- 使用自定义块进行跳跃和移动逻辑
**第 3 步：实施解决方案**```scratch
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

**第4步：验证和优化**
在不同平台上测试跳跃。调整重力和跳跃高度以获得良好的游戏感觉。添加跑步和跳跃的动画。使用广播消息实施检查点。
---

### 问题 2：创建带有分数跟踪功能的问答游戏
**第 1 步：了解问题**
构建一个提问、检查答案并跟踪玩家得分的问答游戏。
**第 2 步：确定方法**
- 将问题和答案存储在并行列表中
- 使用问题计数器来跟踪进度
- 使用“询问并等待”块进行输入
- 比较答案并更新分数
**第 3 步：实施解决方案**```scratch
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

**第4步：验证和优化**
使用包括边缘情况在内的各种答案进行测试。添加错误答案的反馈。实施重试选项。添加正确/错误答案的声音效果和视觉反馈。
---

### 问题 3：用钢笔绘制分形树
**第 1 步：了解问题**
使用笔扩展创建递归分形树。
**第 2 步：确定方法**
- 使用递归来绘制分支
- 每个分支分裂成两个较小的分支
- 使用随机角度实现自然变化
- 跟踪分支长度并随着每个递归级别而减少
**第 3 步：实施解决方案**```scratch
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

**第4步：验证和优化**
调整美观树木的树枝长度阈值和角度范围。使用颜色变化在树枝尖端添加叶子。实施不同的树样式。将绘图另存为图像。
---

＃＃ 概括
Scratch 不是传统意义上的编程语言——它是一个学习环境。它的天才在于消除了孩子与创造互动事物的乐趣之间的所有障碍。通过关注概念而不是语法，Scratch 教授可迁移到任何语言的编程基础知识。对于向年轻学习者介绍编程，Scratch 是黄金标准。