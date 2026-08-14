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
# Scratch

Scratch is a visual, block-based programming language developed by the MIT Media Lab and first released in 2007. Instead of writing text-based code, users snap together coloured blocks to create programs. Scratch is designed specifically for children ages 8-16 (though learners of all ages use it) to teach fundamental programming concepts — loops, conditionals, variables, events, and functions — without the barrier of syntax errors.

Scratch is the most widely-used introductory programming language in the world, with over 100 million registered users and availability in 70+ languages. It runs in a web browser and is free.

---

## Why Scratch Matters

- **Best introduction to programming**: Removes syntax barriers entirely. Concepts are taught through visual manipulation.
- **Computational thinking**: Teaches decomposition, pattern recognition, abstraction, and algorithm design.
- **Creativity-driven**: Kids create games, animations, stories, and music — learning programming as a byproduct of making things they care about.
- **Global reach**: Used in schools worldwide. Available in 70+ languages. Free and browser-based.
- **Community**: The Scratch online community teaches sharing, remixing, and collaborative learning.

## The Trade-offs

| Limitation | Details | Typical Workaround |
|-----------|---------|-------------------|
| **Not a "real" programming language** | Cannot build production software, APIs, or systems | Transition to Python, JavaScript, or text-based languages |
| **Limited capabilities** | No file I/O, networking, or advanced data structures | Use for learning; move to text languages for real projects |
| **Performance** | Interpreted, slow for complex projects | Not designed for performance-critical work |
| **Age perception** | Often seen as "just for kids" | Scratch is a learning tool, not a professional language |

---

## How Scratch Works

Scratch programs (called "projects") consist of **sprites** (characters/objects) that respond to **blocks** snapped together in scripts.

### Core Concepts (Taught Through Blocks)

| Concept | Scratch Block Category | Example |
|---------|----------------------|---------|
| **Sequences** | Motion, Looks | "Move 10 steps" then "Say Hello" |
| **Loops** | Control (yellow) | "Repeat 10", "Forever", "Repeat until" |
| **Conditionals** | Control (yellow) | "If... then", "If... then... else" |
| **Variables** | Variables (orange) | "Set score to 0", "Change score by 1" |
| **Events** | Events (yellow) | "When green flag clicked", "When key pressed" |
| **Functions** | My Blocks (custom) | Define reusable block sequences |
| **Lists (arrays)** | Variables (orange) | "Add to list", "Item of list" |
| **Broadcasting** | Events | Send messages between sprites |

### Example: Simple Game Logic

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

## Advanced Syntax & Patterns

### Block Categories in Detail

Scratch 3.0 organises blocks into colour-coded categories:

| Category | Colour | Block Types |
|----------|--------|-------------|
| **Motion** | Blue | move, turn, goto, glide, point, change x/y |
| **Looks** | Purple | say, think, switch costume, change size, show/hide |
| **Sound** | Pink | play sound, stop sounds, change volume, change pitch |
| **Events** | Yellow | when flag clicked, when key pressed, when sprite clicked, broadcast |
| **Control** | Gold | wait, repeat, forever, if, if-else, repeat until, stop |
| **Sensing** | Light Blue | touching, key pressed, mouse, distance, ask/answer, timer |
| **Operators** | Green | math ops, text ops, comparison, and/or/not, random |
| **Variables** | Orange | set/change variable, list operations |
| **My Blocks** | Dark Red | custom block definitions (functions) |

### Advanced Block Patterns

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

### Custom Blocks (Functions)

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

### List Operations (Arrays)

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

### Broadcasting (Inter-Sprite Communication)

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

## Architecture & System Design

### Event-Driven Design

Scratch uses an event-driven architecture. Every script starts with an event block (hat block) and runs in response to that event.

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

### Project Structure

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

### Clone System (Object Creation)

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

## Project Configuration & Build System

### Scratch Extensions

Scratch supports official and community extensions that add capabilities:

| Extension | Purpose |
|-----------|---------|
| **Pen** | Draw lines and shapes on the stage |
| **Video Sensing** | Use webcam for motion detection |
| **Text to Speech** | Convert text to spoken audio |
| **Translate** | Translate text between languages |
| **Makey Makey** | Connect physical objects as input |
| **micro:bit** | Connect BBC micro:bit hardware |
| **LEGO Mindstorms** | Control LEGO robots |
| **Music** | Play musical notes and instruments |

### Scratch File Format

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

### Offline Editor

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

## Testing & Debugging

### Built-in Debugging Tools

Scratch provides several built-in tools for debugging projects:

| Tool | How to Use |
|------|-----------|
| **Turtle mode** | Right-click a sprite and select "show debug" to see coordinates |
| **Variable monitors** | Right-click a variable and select "show" to see its value in real-time |
| **List monitors** | View list contents in normal, row, or column display |
| **Turbo mode** | Hold Shift while clicking the green flag for faster execution |
| **Single-step mode** | Right-click the green flag for "single step" (slows execution) |

### Debugging Patterns

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

### Common Issues

| Problem | Cause | Solution |
|---------|-------|----------|
| Sprite not responding | No event hat block | Add "When green flag clicked" or other event |
| Clone not working | Clone created but not shown | Add "Show" block after "When I start as a clone" |
| Variable shared between sprites | Global vs local variable confusion | Use "For this sprite only" option |
| Broadcast not received | Wrong message name | Verify broadcast and receive names match exactly |
| Infinite loop freeze | "Forever" with no wait | Add small "Wait" blocks in tight loops |

---

## Interoperability

### Hardware Extensions

Scratch can connect to physical hardware through extensions:

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

### Scratch Extensions API (Custom Extensions)

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

## Design Patterns

### Pattern 1: Platformer Movement

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

### Pattern 2: Scrolling Background

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

### Pattern 3: Sprite Following (Chase AI)

```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Pattern 4: Inventory System with Lists

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

### Pattern 5: Particle System with Clones

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

## Performance & Optimization

### Sprite Optimization

| Technique | Impact | Description |
|-----------|--------|-------------|
| **Minimize clones** | High | Each clone consumes memory; delete when done |
| **Reduce costumes** | Medium | Fewer costume switches means less rendering overhead |
| **Use "run without screen refresh"** | High | Custom blocks without screen refresh run faster |
| **Limit "say" blocks** | Medium | Speech bubbles cause rendering overhead |
| **Avoid "forever" in every sprite** | Medium | Use broadcasts and events instead of constant polling |

### Clone Management

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

### Optimization Checklist

| Technique | Impact | Description |
|-----------|--------|-------------|
| **Run without screen refresh** | Very High | Custom blocks skip rendering for speed |
| **Minimize active clones** | High | Delete clones as soon as they are no longer needed |
| **Use broadcasts sparingly** | Medium | Too many broadcasts per frame cause lag |
| **Simplify costumes** | Medium | Smaller images render faster |
| **Reduce list operations** | Medium | Avoid scanning large lists every frame |
| **Use "wait" blocks** | Low | Prevent CPU hogging in forever loops |

---

## Deployment & Real-World Usage

### Sharing Projects

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

### Real-World Educational Usage

| Context | How Scratch Is Used | Scale |
|---------|-------------------|-------|
| **K-12 schools** | Introduction to programming in CS classes | Used in 190+ countries |
| **Coding clubs** | Scratch Club / CoderDojo workshops | 3000+ clubs worldwide |
| **Libraries** | After-school programming programs | Public library systems |
| **Homeschooling** | Self-paced programming education | Millions of home learners |
| **University CS0** | Non-major introductory CS courses | University bridge programs |
| **Accessibility** | Teaching programming to visually impaired | Screen reader support |
| **Therapy** | Cognitive and motor skill development | Occupational therapy |

### Scratch in Education Research

Research has shown that Scratch effectively teaches:
- **Sequential thinking**: Breaking problems into ordered steps
- **Debugging skills**: Finding and fixing errors in logic
- **Creative expression**: Combining art, music, and programming
- **Collaboration**: Remixing and building on others' projects
- **Persistence**: Iterating on projects to improve them

---

## Transitioning From Scratch

After learning Scratch, typical next steps include:

| Next Language | Why |
|--------------|-----|
| **Python** | Most natural transition — readable syntax, similar logic concepts |
| **JavaScript** | If interested in web/games — immediate visual feedback |
| **Lua (via Roblox/Love2D)** | If interested in game development |
| **App Inventor** | Visual blocks for Android apps (same MIT lineage) |
| **Blockly** | Google's visual programming library (similar concepts) |

### Concept Mapping: Scratch to Python

| Scratch Concept | Python Equivalent |
|----------------|-------------------|
| `set [x] to 0` | `x = 0` |
| `change [x] by 1` | `x += 1` |
| `repeat 10` | `for i in range(10):` |
| `forever` | `while True:` |
| `if ... then` | `if ...:` |
| `broadcast [msg]` | Function call or event system |
| `My Blocks` | `def function():` |
| `list` | `list = []` |
| `item 1 of [list]` | `list[0]` (0-indexed!) |
| `length of [list]` | `len(list)` |

---

## When to Use Scratch

| Scenario | Why Scratch | Better Alternative |
|----------|-----------|-------------------|
| Teaching children (8-16) to code | Designed specifically for this | — |
| Introducing computational thinking | Visual, no syntax errors | — |
| School workshops / coding clubs | Free, browser-based, no setup | — |
| Prototyping game ideas visually | Fast iteration | — |
| Professional development | Not designed for this | Python, JavaScript, any text language |
| University-level CS education | Too simple | Python, Java, C |

---

## Synthetic Q&A

**Q1: Is Scratch really a programming language?**
A1: Yes, Scratch is a real programming language, but it's visual rather than text-based. It supports all fundamental programming concepts: variables, loops, conditionals, functions (custom blocks), lists, and event-driven programming. The difference is that you drag and drop blocks instead of typing code. This eliminates syntax errors and makes programming accessible to young learners.

**Q2: How do I create custom functions (custom blocks) in Scratch?**
A2: Go to the "My Blocks" category and click "Make a Block". Give it a name, add parameters if needed, then define its behavior by adding blocks below it. Custom blocks can take inputs (numbers, strings, booleans) and can call other custom blocks. This enables modular programming and code reuse.

**Q3: What's the best way to handle complex game logic in Scratch?**
A3: Use custom blocks to organize logic, broadcast messages for event coordination between sprites, and use lists to store game state (scores, levels, inventory). For complex AI, use finite state machines with variables tracking the current state. Clone sprites for multiple enemies and use "when I start as a clone" to give each independent behavior.

**Q4: How can I share data between sprites in Scratch?**
A4: Use global variables (created without "for this sprite only") for shared data like score or game state. Use broadcast messages to trigger events across sprites. For more complex communication, use lists as shared data structures. Each sprite can read and modify global variables and lists, enabling coordination.

**Q5: What are some advanced techniques in Scratch?**
A5: Use pen blocks for drawing and creating visual effects. Implement raycasting for 3D-like graphics. Use cloud variables for multiplayer games (requires Scratcher status). Create procedural generation with random numbers and lists. Use custom blocks with parameters for reusable algorithms. Experiment with video sensing and sound manipulation for interactive projects.

---

## Chain-of-Thought

### Problem 1: Creating a Platformer Game

**Step 1: Understand the Problem**
We need to create a platformer where a character can move left/right, jump, avoid obstacles, and collect items.

**Step 2: Identify the Approach**
- Use gravity simulation with a "falling" variable
- Detect ground/collision using color or sprite touching
- Store level data in lists
- Use custom blocks for jump and movement logic

**Step 3: Implement the Solution**
```scratch
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

**Step 4: Verify and Optimize**
Test jumping on different platforms. Adjust gravity and jump height for good game feel. Add animations for running and jumping. Implement checkpoints using broadcast messages.

---

### Problem 2: Creating a Quiz Game with Score Tracking

**Step 1: Understand the Problem**
Build a quiz game that asks questions, checks answers, and tracks the player's score.

**Step 2: Identify the Approach**
- Store questions and answers in parallel lists
- Use a question counter to track progress
- Use "ask and wait" blocks for input
- Compare answers and update score

**Step 3: Implement the Solution**
```scratch
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

**Step 4: Verify and Optimize**
Test with various answers including edge cases. Add feedback for wrong answers. Implement a retry option. Add sound effects and visual feedback for correct/wrong answers.

---

### Problem 3: Drawing Fractal Trees with the Pen

**Step 1: Understand the Problem**
Create a recursive fractal tree using the pen extension.

**Step 2: Identify the Approach**
- Use recursion to draw branches
- Each branch splits into two smaller branches
- Use random angles for natural variation
- Track branch length and decrease with each recursion level

**Step 3: Implement the Solution**
```scratch
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

**Step 4: Verify and Optimize**
Adjust branch length threshold and angle ranges for aesthetic trees. Add leaves at branch tips using color changes. Implement different tree styles. Save drawings as images.

---

## Summary

Scratch is not a programming language in the traditional sense — it is a learning environment. Its genius is removing every barrier between a child and the joy of creating something interactive. By focusing on concepts rather than syntax, Scratch teaches the fundamentals of programming that transfer to any language. For introducing programming to young learners, Scratch is the gold standard.
