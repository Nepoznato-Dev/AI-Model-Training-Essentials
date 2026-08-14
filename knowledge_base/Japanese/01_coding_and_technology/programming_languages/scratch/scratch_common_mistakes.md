---
# Metadata
title: "Scratch — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Scratch with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [scratch, common-mistakes, anti-patterns, pitfalls, visual-programming, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# スクラッチ — よくある間違いとアンチパターン
このドキュメントでは、Scratch で最もよくある間違いと罠を修正とともにカタログ化します。
---

## 1. スクリプトの終了に「停止」を使用しない
```
❌ WRONG — script keeps running after game over
when green flag clicked
forever
    if <touching [edge v]?> then
        say [Game Over]
        // script continues!
    end
end

✅ CORRECT — use stop block
when green flag clicked
forever
    if <touching [edge v]?> then
        say [Game Over]
        stop [all v]
    end
end
```

---

## 2. クローンの混乱
```
❌ WRONG — modifying original sprite thinking it's a clone
when I start as a clone
change [score v] by (1)  // modifies global variable
// but "when green flag clicked" also runs on clones!

✅ CORRECT — separate clone logic from original
when green flag clicked
// setup code only

when I start as a clone
// clone-specific behavior only
```

---

## 3. ブロードキャストのタイミング
```
❌ WRONG — expecting immediate response
broadcast [jump v]
// code continues immediately, doesn't wait!

✅ CORRECT — use broadcast and wait
broadcast [jump v] and wait
// now waits for all recipients to finish
```

---

## 4. 変数のスコープ
```
❌ WRONG — using global variable when local needed
// All sprites share the variable "my variable"
// Sprite A changes it, Sprite B sees the change

✅ CORRECT — use "For this sprite only"
// Create variable as "For this sprite only"
// Each sprite has its own copy
```

---

## 5. 収量のない無限ループ
```
❌ WRONG — freezes the program
when green flag clicked
forever
    // no wait or visual change
    // locks up the interface
end

✅ CORRECT — add a small wait
when green flag clicked
forever
    // do work
    wait (0.1) seconds
end
```

---

＃＃ まとめ
スクラッチ トラップ: ゲームを終了するには常に「停止」を使用し、クローン ロジックを元のスプライト ロジックから分離し、同期通信に「ブロードキャストと待機」を使用し、必要に応じてスプライト固有の変数を使用し、フリーズを防ぐために永久ループに待機を追加します。 Scratch は基本的な概念、つまりイベント駆動型モデルを尊重することを教えます。