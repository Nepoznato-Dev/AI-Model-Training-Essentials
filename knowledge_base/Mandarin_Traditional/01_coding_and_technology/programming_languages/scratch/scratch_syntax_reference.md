---
# Metadata
title: "Scratch — Syntax Reference"
description: "Detailed syntax reference for Scratch covering block categories, event-driven programming, sprite management, cloning, variables, lists, custom blocks, and creative coding patterns."
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
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Initial syntax reference document"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [scratch, syntax-reference, visual-programming, block-based, event-driven, education, coding-and-technology]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Scratch — 語法參考
本文檔為 Scratch 3.0 提供全面、結構化的語法參考。它透過專注於詳盡的區塊類別、事件驅動模式、精靈管理、複製和創意編碼技術來補充主要的 Scratch 參考。
---

## 區塊類別概述
|類別 |顏色 |區塊類型 |目的|
|----------|--------|-------------|---------|
| **運動** |藍色|堆疊|移動精靈、改變位置、方向 |
| **看起來** |紫色|堆疊|改變外觀、說出/思考、顯示/隱藏 |
| **聲音** |粉紅色|堆疊|播放聲音、改變音量/音調 |
| **活動** |黃色|帽子|啟動腳本，廣播/接收訊息|
| **控制** |黃金|堆疊|循環、條件、等待、停止 |
| **感測** |淺藍色 |記者|偵測碰撞、輸入、計時器、答案 |
| **運營商** |綠色|記者|數學、文本、比較、邏輯 |
| **變數** |橘色|堆疊/記者 |儲存資料、清單操作 |
| **我的區塊** |深紅色|堆疊|自訂區塊定義（函數）|
---

## 運動塊
```
// Position
move (10) steps
go to x: (0) y: (0)
go to [mouse-pointer v]
glide (1) secs to x: (100) y: (50)
point in direction (90)
point towards [Sprite1 v]

// Change coordinates
change x by (10)
set x to (0)
change y by (10)
set y to (0)

// Direction
turn cw (15) degrees
turn ccw (15) degrees
set heading to (90)

// Queries
(x position)
(y position)
(direction)
```

---

## 看起來塊
```
// Speech bubbles
say [Hello!] for (2) seconds
say [Hello!]
think [Hmm...] for (2) seconds
think [Hmm...]

// Appearance
switch costume to [costume1 v]
next costume
switch backdrop to [backdrop1 v]
next backdrop
change [color v] effect by (25)
set [color v] effect to (0)
clear graphic effects

// Visibility
show
hide

// Size
change size by (10)
set size to (100) %

// Queries
(costume #)
(backdrop name)
(size)
```

---

## 事件區塊（帽子區塊）
```
// Every script MUST start with a hat block
when green flag clicked          // Program start
when [space v] key pressed       // Keyboard input
when this sprite clicked         // Mouse click on sprite
when I start as a clone          // Clone initialization
when backdrop switches to [scene1 v]
when [loudness v] > (10)
when video motion > (10)
when I receive [message1 v]      // Broadcast receiver

// Broadcasting (inter-sprite communication)
broadcast [message1 v]
broadcast [message1 v] and wait  // Wait for all receivers to finish
```

---

## 控制區塊
```
// Sequencing
wait (1) seconds
wait until <condition>

// Loops
repeat (10)
  ...
end

forever
  ...
end

repeat until <condition>
  ...
end

// Conditionals
if <condition> then
  ...
end

if <condition> then
  ...
else
  ...
end

// Cloning
create clone of [myself v]
create clone of [Sprite1 v]
delete this clone

// Stopping
stop [all v]
stop [this script v]
stop [other scripts in sprite v]
```

---

## 感應塊
```
// Collision detection
<touching [Sprite1 v]?>
<touching color [#FF0000]?>
<color [#FF0000] is touching [#00FF00]?>

// Distance
(distance to [Sprite1 v])

// Input
(key [space v] pressed?)
(mouse down?)
(mouse x)
(mouse y)

// User input
ask [What is your name?] and wait
(answer)

// Timer
reset timer
(timer)

// Sprite properties
<touching [edge v]?>

// Drag mode
set drag mode [draggable v]
set drag mode [not draggable v]
```

---

## 運算符
```
// Arithmetic
(() + ())
(() - ())
(() * ())
(() / ())
(pick random (1) to (10))

// Comparison
<() > ()>
<() < ()>
<() = ()>

// Logic
<<> and <>>
<<> or <>>
<not <>>

// Text
(join [hello ] [world])
(letter (1) of [hello])
(length of [hello])
<([hello] contains [ell])>

// Math functions
(round (3.7))
([abs v] of (-5))
([floor v] of (3.7))
([ceiling v] of (3.2))
([sqrt v] of (16))
([sin v] of (90))
([cos v] of (0))
([tan v] of (45))
([ln v] of (2.718))
```

---

## 變數和列表
```
// Variables
set [score v] to (0)
change [score v] by (1)
(score)

// Show/hide variable monitors
show variable [score v]
hide variable [score v]

// Lists (arrays — 1-indexed!)
add [item] to [my list v]
delete (1) of [my list v]
delete all of [my list v]
insert [item] at (1) of [my list v]
replace item (1) of [my list v] with [new value]

// List queries
(item (1) of [my list v])
(item # of [item] in [my list v])
(length of [my list v])
<[my list v] contains [item]?>

// Show list monitors
show list [my list v]
hide list [my list v]
```

---

## 自訂區塊（函數）
```
// Define a custom block
define jump (height) times (count)
  repeat (count)
    change y by (height)
    wait (0.2) seconds
    change y by ((height) * -1)
    wait (0.2) seconds

// Usage:
jump height: (50) times: (3)

// Optimization: run without screen refresh
define draw spiral (size) (angle)
  run without screen refresh
  repeat (100)
    move (size) steps
    turn cw (angle) degrees
    change (size) by (1)

// Custom blocks with boolean inputs
define move if (should move) steps (amount)
  if <(should move)> then
    move (amount) steps
```

---

## 筆擴充
```
// Pen blocks (requires Pen extension)
erase all
stamp
pen down
pen up
set pen color to [#FF0000]
set pen color to (100)          // Color 0-200
change pen (color v) by (25)
set pen (size v) to (5)
change pen (size v) by (1)

// Drawing a square
pen down
repeat (4)
  move (100) steps
  turn right (90) degrees
pen up

// Drawing a circle (approximation)
pen down
repeat (360)
  move (1) steps
  turn right (1) degrees
pen up
```

---

## 聲音區塊
```
// Playing sounds
play sound [Meow v] until done
play sound [Meow v]
stop all sounds

// Volume
change volume by (-10)
set volume to (100) %
(volume)

// Tempo (Music extension)
set tempo to (120)
change tempo by (20)
(tempo)
play drum (1) for (0.2) beats
rest for (0.5) beats
play note (60) for (0.5) beats
set instrument to (1)
```

---

＃＃ 概括
Scratch 基於區塊的語法消除了打字錯誤，並使程式設計概念變得具體。每個腳本都以帽子區塊（事件）開始，然後堆疊命令區塊（運動、外觀、聲音、控制、感測、運算符、變數）並使用報告區塊（圓形/橢圓形）作為值。自訂區塊可實現模組化程式設計。克隆提供類似物件的行為。列出商店收藏。筆擴充可實現創意繪畫。對於年輕學習者來說，Scratch 提供了程式設計邏輯、事件驅動設計和透過程式碼進行創意表達的完整介紹。