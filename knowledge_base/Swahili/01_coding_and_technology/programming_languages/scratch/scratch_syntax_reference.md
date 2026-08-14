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

# Mkwaruzo - Rejeleo la Sintaksia
Hati hii inatoa marejeleo ya kina, yenye muundo wa sintaksia ya Scratch 3.0. Inakamilisha rejeleo kuu la Mwanzo kwa kuzingatia kategoria kamili za kuzuia, mifumo inayoendeshwa na hafla, usimamizi wa sprite, uundaji wa cloning, na mbinu bunifu za usimbaji.
---

## Zuia Muhtasari wa Aina
| Kitengo | Rangi | Aina za Kuzuia | Kusudi |
|----------|----------------------|---------|
| **Mwendo** | Bluu | Rafu | Sogeza sprites, badilisha msimamo, mwelekeo |
| **Inaonekana** | Zambarau | Rafu | Badilisha mwonekano, sema/fikiria, onyesha/ficha |
| **Sauti** | Pinki | Rafu | Cheza sauti, badilisha sauti/ sauti |
| **Matukio** | Njano | Kofia | Anzisha hati, tangaza/pokea ujumbe |
| **Dhibiti** | Dhahabu | Rafu | Vitanzi, masharti, subiri, acha |
| **Kuhisi** | Bluu Isiyokolea | Mwandishi | Tambua migongano, ingizo, kipima muda, majibu |
| **Waendeshaji** | Kijani | Mwandishi | Hisabati, maandishi, kulinganisha, mantiki |
| **Vigezo** | Chungwa | Rafu/Mwandishi | Hifadhi data, orodhesha shughuli |
| **Vizuizi Vyangu** | Nyekundu Iliyokolea | Rafu | Ufafanuzi maalum wa kuzuia (kazi) |
---

## Vizuizi vya Mwendo
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

## Inaonekana Vitalu
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

## Matukio Blocks (Hat Blocks)
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

## Vizuizi vya Kudhibiti
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

## Vitalu vya Kuhisi
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

## Waendeshaji
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

## Vigezo & Orodha
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

## Vitalu Maalum (Kazi)
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

## Upanuzi wa kalamu
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

## Vizuizi vya sauti
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

## Muhtasari
Sintaksia ya msingi wa block ya Scratch huondoa makosa ya kuandika na kufanya dhana za upangaji kushikika. Kila hati huanza na kizuizi cha kofia (tukio), kisha hupanga vizuizi vya amri (mwendo, mwonekano, sauti, udhibiti, hisi, waendeshaji, vigeu) na hutumia vizuizi vya ripota (maumbo ya duara/mviringo) kwa thamani. Vitalu maalum huwezesha upangaji wa kawaida. Clones hutoa tabia kama kitu. Inaorodhesha makusanyo ya duka. Ugani wa kalamu huwezesha kuchora kwa ubunifu. Kwa wanafunzi wachanga, Scratch hutoa utangulizi kamili wa mantiki ya programu, muundo unaoendeshwa na matukio, na usemi wa ubunifu kupitia msimbo.