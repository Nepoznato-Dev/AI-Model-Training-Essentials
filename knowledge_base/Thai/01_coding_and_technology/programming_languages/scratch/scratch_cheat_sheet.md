---
# Metadata
title: "Scratch — Cheat Sheet"
description: "Quick-reference cheat sheet for Scratch blocks, events, and common patterns."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial cheat sheet"
tags: [scratch, visual-programming, cheat-sheet, quick-reference, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "8 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Scratch - แผ่นโกง
## กิจกรรม
```
when green flag clicked          → Start program
when [space v] key pressed       → Key press
when this sprite clicked         → Click sprite
when I receive [message v]       → Broadcast received
when backdrop switches to [v]    → Backdrop change
when [loudness v] > [10 v]       → Sound trigger
when I start as a clone          → Clone starts
```

## การเคลื่อนไหว
```
move [10] steps
go to x:[0] y:[0]
glide [1] secs to x:[0] y:[0]
point in direction [90]
point towards [mouse-pointer v]
change x by [10]
set x to [0]
change y by [10]
set y to [0]
if on edge, bounce
set rotation style [left-right v]
(x position)
(y position)
(direction)
```

## หน้าตา.
```
say [Hello!] for [2] seconds
say [Hello!]
think [Hmm...] for [2] seconds
think [Hmm...]
switch costume to [costume1 v]
next costume
switch backdrop to [backdrop1 v]
change [color v] effect by [25]
clear [color v] effect
show
hide
go to [front v] layer
change size by [10]
set size to [100] %
(size)
```

## เสียง
```
play sound [Meow v] until done
start sound [Meow v]
stop all sounds
change volume by [-10]
set volume to [100] %
(volume)
change [pitch v] effect by [10]
clear [pitch v] effect
```

## ควบคุม
```
wait [1] seconds
repeat [10]
  ...
end
forever
  ...
end
if < > then
  ...
end
if < > then
  ...
else
  ...
end
wait until < >
stop [all v]
repeat until < >
  ...
end
```

## การตรวจจับ
```
<touching [edge v] ?>
<touching color [#ff0000] ?>
<color [#ff0000] is touching [#0000ff] ?>
(distance to [mouse-pointer v])
ask [What's your name?] and wait
(answer)
<key [space v] pressed?>
<mouse down?>
(mouse x)
(mouse y)
set drag mode [draggable v]
(loudness)
(timer)
reset timer
([x v] of [Stage v])
(current [year v])
(days since 2000)
```

## ผู้ประกอบการ
```
<() + ()>
<() - ()>
<() * ()>
<() / ()>
(pick random [1] to [10])
(join [hello] [world])
(letter [1] of [hello])
(length of [hello])
<[hello] contains [ell] ?>
<() mod ()>
<round ()>
([sqrt v] of [9])

// Comparisons
<() > ()>
<() < ()>
<() = ()>

// Logic
<<> and <>>
<<> or <>>
<not <>>
```

## ตัวแปรและรายการ
```
// Variables
set [my variable v] to [0]
change [my variable v] by [1]
show variable [my variable v]
hide variable [my variable v]

// Lists (arrays)
add [thing] to [my list v]
delete [1] of [my list v]
delete all of [my list v]
insert [thing] at [1] of [my list v]
replace item [1] of [my list v] with [thing]
(item [1] of [my list v])
(item # of [thing] in [my list v])
(length of [my list v])
<[my list v] contains [thing] ?>
```

## บล็อกที่กำหนดเอง (บล็อกของฉัน)
```
// Define custom block
define jump
  change y by [50]
  wait [0.3] seconds
  change y by [-50]

// With parameters
define move steps (steps) direction (dir)
  point in direction (dir)
  move (steps) steps

// Run without screen refresh (fast)
define calculate (n)
  // runs instantly, no visual updates
```

## การโคลนนิ่ง
```
// Create clone
create clone of [myself v]

// When clone starts
when I start as a clone
  // initialization

// Delete clone
delete this clone
```

## ปากกา (วาดรูป)
```
erase all
stamp
pen down
pen up
set pen color to [#ff0000]
change pen [color v] by [10]
set pen [color v] to [#ff0000]
change pen size by [1]
set pen size to [1]
```
