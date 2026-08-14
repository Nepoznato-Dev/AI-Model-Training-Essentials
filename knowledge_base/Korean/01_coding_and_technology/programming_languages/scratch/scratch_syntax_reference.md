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

# 스크래치 — 구문 참조
이 문서는 스크래치 3.0에 대한 포괄적이고 구조화된 구문 참조를 제공합니다. 이는 철저한 블록 카테고리, 이벤트 중심 패턴, 스프라이트 관리, 복제 및 창의적인 코딩 기술에 중점을 두어 기본 스크래치 참조를 보완합니다.
---

## 블록 카테고리 개요
| 카테고리 | 색상 | 블록 유형 | 목적 |
|------------|---------|-------------|---------|
| **모션** | 블루 | 스택 | 스프라이트 이동, 위치, 방향 변경 |
| **룩** | 보라색 | 스택 | 외모 바꾸기, 말하기/생각하기, 보이기/숨기기 |
| **소리** | 핑크 | 스택 | 소리 재생, 볼륨/피치 변경 |
| **이벤트** | 노란색 | 모자 | 스크립트 시작, 메시지 브로드캐스트/수신 |
| **제어** | 골드 | 스택 | 루프, 조건문, 대기, 중지 |
| **센싱** | 라이트 블루 | 기자 | 충돌 감지, 입력, 타이머, 답변 |
| **운영자** | 그린 | 기자 | 수학, 텍스트, 비교, 논리 |
| **변수** | 오렌지 | 스택/리포터 | 데이터 저장, 목록 작업 |
| **내 블록** | 다크 레드 | 스택 | 사용자 정의 블록 정의(함수) |
---

## 모션 블록
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

## 보이는 블록
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

## 이벤트 블록(해트 블록)
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

## 제어 블록
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

## 감지 블록
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

## 연산자
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

## 변수 및 목록
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

## 사용자 정의 블록(기능)
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

## 펜 확장
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

## 사운드 블록
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

## 요약
스크래치의 블록 기반 구문은 입력 오류를 제거하고 프로그래밍 개념을 실체화합니다. 모든 스크립트는 모자 블록(이벤트)으로 시작한 다음 명령 블록(모션, 모양, 소리, 제어, 감지, 연산자, 변수)을 쌓고 값에 대해 리포터 블록(원형/타원형 모양)을 사용합니다. 맞춤형 블록을 사용하면 모듈식 프로그래밍이 가능합니다. 클론은 객체와 유사한 동작을 제공합니다. 상점 컬렉션을 나열합니다. 펜 확장 기능을 사용하면 창의적인 그림을 그릴 수 있습니다. 어린 학습자를 위해 스크래치는 프로그래밍 논리, 이벤트 중심 디자인, 코드를 통한 창의적인 표현에 대한 완전한 소개를 제공합니다.