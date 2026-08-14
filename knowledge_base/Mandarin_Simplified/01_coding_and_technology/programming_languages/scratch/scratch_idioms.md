<!--
---
# Metadata
title: "Scratch — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean, well-organized Scratch projects."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [scratch, visual-programming, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "8 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Scratch — 惯用模式和最佳实践
本指南涵盖了编写干净、组织良好的 Scratch 项目的惯用模式。
---

## 精灵组织
```
✅ Name your sprites clearly
  - "Player", "Enemy", "ScoreKeeper" — descriptive names
  - Avoid "Sprite1", "Sprite2" — rename immediately

✅ One responsibility per sprite
  - Player sprite: handles movement and animation
  - Score sprite: handles score display and updates
  - Stage: handles background and global state

✅ Use "When I receive message" for communication
  - broadcast [start game] → all sprites respond
  - broadcast [game over] → sprites stop or show results
```

---

## 变量和列表模式
```
✅ Use descriptive variable names
  - "player speed" not "var1"
  - "score" not "a"
  - "is game running" not "flag"

✅ Initialize variables at green flag
  when green flag clicked
  set [score v] to [0]
  set [lives v] to [3]
  set [game over v] to [no]

✅ Use lists for collections
  - "high scores" list for top 10 scores
  - "inventory" list for player items
  - Always check list length before accessing by index
```

---

## 自定义块（我的块）
```
✅ Create custom blocks for repeated logic
  define jump
    change y by [50]
    wait [0.3] seconds
    change y by [-50]

  define reset position
    go to x:[0] y:[0]
    point in direction [90]

✅ Use parameters for flexible blocks
  define move steps (steps) in direction (dir)
    point in direction (dir)
    move (steps) steps

✅ Custom blocks with "Run without screen refresh"
  - Use for math calculations and loops
  - Makes complex operations instant
```

---

## 克隆模式
```
✅ Clone for multiple instances
  // In the original sprite:
  when green flag clicked
  forever
    wait [2] seconds
    create clone of [myself v]

  // In "When I start as a clone":
  when I start as a clone
  go to x:(pick random [-200] to [200]) y:[180]
  glide [2] secs to x:(x position) y:[-180]
  delete this clone

✅ Clone cleanup — always delete when done
  if <touching [edge v] ?> then
    delete this clone

✅ Use clone variables for per-instance state
  when I start as a clone
  set [clone speed v] to (pick random [1] to [5])
```

---

## 游戏循环模式
```
✅ Structure game loops clearly
  when green flag clicked
  forever
    if <(game over) = [no]> then
      handle input
      update positions
      check collisions
      update score display
    end
    wait [0.016] seconds  // ~60 FPS
  end

✅ Separate input handling from game logic
  when [right arrow v] key pressed
  change x by [10]

  // vs. polling in game loop:
  if <key [right arrow v] pressed?> then
    change x by [speed]
```

---

## 性能提示
```
✅ "Run without screen refresh" for calculations
  define calculate path (steps)
    // heavy math here — no visual updates
    ...

✅ Minimize "say" and "think" in loops
  // ❌ Bad: saying every frame
  forever
    say (join "Score: " (score))

  // ✅ Good: update only when changed
  if <(score) > (last score)> then
    say (join "Score: " (score))
    set [last score v] to (score)

✅ Use "stop [other scripts in sprite v]"
  // Clean stop when switching states
  stop [other scripts in sprite v]
```

---

＃＃ 概括
Scratch 习语强调：清晰的精灵命名、每个精灵一个责任、用于通信的广播消息、用于重用的自定义块、多个实例的克隆、结构化游戏循环以及“无需屏幕刷新即可运行”的性能。 Scratch 奖励组织——“一个名字好听的精灵就是计划的一半。”