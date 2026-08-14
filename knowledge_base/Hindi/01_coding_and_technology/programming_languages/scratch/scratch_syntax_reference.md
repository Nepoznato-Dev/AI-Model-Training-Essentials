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

# स्क्रैच - सिंटैक्स संदर्भ
यह दस्तावेज़ स्क्रैच 3.0 के लिए एक व्यापक, संरचित सिंटैक्स संदर्भ प्रदान करता है। यह संपूर्ण ब्लॉक श्रेणियों, इवेंट-संचालित पैटर्न, स्प्राइट प्रबंधन, क्लोनिंग और रचनात्मक कोडिंग तकनीकों पर ध्यान केंद्रित करके मुख्य स्क्रैच संदर्भ को पूरक करता है।
---

## ब्लॉक श्रेणियों का अवलोकन
| श्रेणी | रंग | ब्लॉक प्रकार | उद्देश्य |
|---|--------|---|---|
| **मोशन** | नीला | ढेर | स्प्राइट्स को स्थानांतरित करें, स्थिति, दिशा बदलें |
| **दिखता है** | बैंगनी | ढेर | रूप बदलें, कहें/सोचें, दिखाएँ/छिपाएँ |
| **ध्वनि** | गुलाबी | ढेर | ध्वनियाँ बजाएं, वॉल्यूम/पिच बदलें |
| **घटनाएँ** | पीला | टोपी | स्क्रिप्ट प्रारंभ करें, संदेश प्रसारित/प्राप्त करें |
| **नियंत्रण** | सोना | ढेर | लूप्स, सशर्त, रुकें, रुकें |
| **संवेदन** | हल्का नीला | रिपोर्टर | टकराव, इनपुट, टाइमर, उत्तर का पता लगाएं |
| **संचालक** | हरा | रिपोर्टर | गणित, पाठ, तुलना, तर्क |
| **चर** | नारंगी | स्टैक/रिपोर्टर | डेटा संग्रहित करें, सूची संचालन |
| **मेरे ब्लॉक** | गहरा लाल | ढेर | कस्टम ब्लॉक परिभाषाएँ (फ़ंक्शन) |
---

## मोशन ब्लॉक
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

## ब्लॉक दिखता है
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

## इवेंट ब्लॉक (हैट ब्लॉक)
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

## नियंत्रण ब्लॉक
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

## सेंसिंग ब्लॉक
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

## संचालक
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

## चर और सूचियाँ
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

## कस्टम ब्लॉक (कार्य)
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

## पेन एक्सटेंशन
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

## ध्वनि ब्लॉक
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

## सारांश
स्क्रैच का ब्लॉक-आधारित सिंटैक्स टाइपिंग त्रुटियों को समाप्त करता है और प्रोग्रामिंग अवधारणाओं को मूर्त बनाता है। प्रत्येक स्क्रिप्ट एक हैट ब्लॉक (ईवेंट) से शुरू होती है, फिर कमांड ब्लॉक (गति, रूप, ध्वनि, नियंत्रण, सेंसिंग, ऑपरेटर, वेरिएबल) को स्टैक करती है और मूल्यों के लिए रिपोर्टर ब्लॉक (गोल/अंडाकार आकार) का उपयोग करती है। कस्टम ब्लॉक मॉड्यूलर प्रोग्रामिंग को सक्षम करते हैं। क्लोन वस्तु जैसा व्यवहार प्रदान करते हैं। स्टोर संग्रह सूचीबद्ध करता है। पेन एक्सटेंशन रचनात्मक ड्राइंग को सक्षम बनाता है। युवा शिक्षार्थियों के लिए, स्क्रैच प्रोग्रामिंग लॉजिक, इवेंट-संचालित डिज़ाइन और कोड के माध्यम से रचनात्मक अभिव्यक्ति का संपूर्ण परिचय प्रदान करता है।