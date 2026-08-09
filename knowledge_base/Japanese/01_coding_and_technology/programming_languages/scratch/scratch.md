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

＃ 傷
Scratch は、MIT メディア ラボによって開発され、2007 年に初めてリリースされたビジュアルなブロックベースのプログラミング言語です。ユーザーは、テキストベースのコードを記述する代わりに、色付きのブロックをスナップしてプログラムを作成します。 Scratch は、8 歳から 16 歳までの子供たち (ただし、あらゆる年齢層の学習者が使用します) を対象に、構文エラーの壁なしで基本的なプログラミングの概念 (ループ、条件文、変数、イベント、関数) を学べるように特別に設計されています。
Scratch は世界で最も広く使用されている入門用プログラミング言語で、登録ユーザー数は 1 億人を超え、70 以上の言語で利用できます。 Web ブラウザ上で動作し、無料です。
---

## スクラッチが重要な理由
- **プログラミングへの最良の入門**: 構文の障壁を完全に取り除きます。概念は視覚的な操作を通じて教えられます。
- **計算論的思考**: 分解、パターン認識、抽象化、アルゴリズム設計を教えます。
- **創造性重視**: 子供たちはゲーム、アニメーション、ストーリー、音楽を作成し、興味のあるものを作る副産物としてプログラミングを学びます。
- **世界的な展開**: 世界中の学校で使用されています。 70 以上の言語で利用可能。無料でブラウザベース。
- **コミュニティ**: Scratch オンライン コミュニティでは、共有、リミックス、共同学習を教えています。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **「本物の」プログラミング言語ではありません** |実稼働ソフトウェア、API、またはシステムを構築できない | Python、JavaScript、またはテキストベースの言語への移行 |
| **制限された機能** |ファイル I/O、ネットワーク、または高度なデータ構造はありません。学習のために使用します。実際のプロジェクトではテキスト言語に移行 |
| **パフォーマンス** |解釈済み、複雑なプロジェクトの場合は遅い |パフォーマンスが重要な作業用に設計されていない |
| **年齢認識** | 「子供向け」と見なされることが多い | Scratch は学習ツールであり、専門的な言語ではありません |
---

## スクラッチの仕組み
スクラッチ プログラム (「プロジェクト」と呼ばれる) は、スクリプト内でスナップされた **ブロック** に応答する **スプライト** (キャラクター/オブジェクト) で構成されます。
### 中心となる概念 (ブロックを通じて学習)
|コンセプト |スクラッチブロックカテゴリ |例 |
|----------|-----------|----------|
| **シーケンス** |動き、見た目 | 「10 歩移動」してから「こんにちは」 |
| **ループ** |コントロール (黄色) | 「10回繰り返す」、「永遠に」、「次まで繰り返す」 |
| **条件付き** |コントロール（黄色） | 「もし...なら」、「もし...なら...そうでなければ」 |
| **変数** |変数 (オレンジ) | 「スコアを 0 に設定する」、「スコアを 1 ずつ変更する」 |
| **イベント** |イベント (黄色) | 「緑の旗がクリックされたとき」、「キーが押されたとき」 |
| **機能** |マイブロック (カスタム) |再利用可能なブロック シーケンスを定義する |
| **リスト (配列)** |変数 (オレンジ) | 「リストに追加」、「リストの項目」 |
| **放送** |イベント |スプライト間でメッセージを送信する |
### 例: 単純なゲーム ロジック
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

## 高度な構文とパターン
### ブロック カテゴリの詳細
Scratch 3.0 では、ブロックが色分けされたカテゴリに分類されます。
|カテゴリー |色 |ブロックの種類 |
|----------|----------|---------------|
| **モーション** |ブルー |移動、回転、移動、滑空、ポイント、X/Y の変更 |
| **見た目** |紫 |言う、考える、衣装を切り替える、サイズを変更する、表示/非表示 |
| **サウンド** |ピンク |音の再生、音の停止、音量の変更、ピッチの変更 |
| **イベント** |黄色 |フラグがクリックされたとき、キーが押されたとき、スプライトがクリックされたとき、ブロードキャスト |
| **コントロール** |ゴールド |待つ、繰り返す、永遠、if、if-else、まで繰り返す、停止 |
| **センシング** |ライトブルー |タッチ、キー押下、マウス、距離、質問/回答、タイマー |
| **オペレーター** |緑 |数学演算、テキスト演算、比較、および/または/以外、ランダム |
| **変数** |オレンジ |変数の設定/変更、リスト操作 |
| **私のブロック** |ダークレッド |カスタム ブロック定義 (関数) |
### 高度なブロック パターン
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

### カスタム ブロック (関数)
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

### リスト操作 (配列)
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

### ブロードキャスト（スプライト間通信）
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

## アーキテクチャとシステム設計
### イベント駆動型の設計
Scratch はイベント駆動型のアーキテクチャを使用します。すべてのスクリプトはイベント ブロック (ハット ブロック) で始まり、そのイベントに応答して実行されます。
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

### プロジェクトの構造
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

### クローンシステム (オブジェクト作成)
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

## プロジェクトの構成とシステムの構築
### スクラッチ拡張機能
Scratch は、機能を追加する公式拡張機能とコミュニティ拡張機能をサポートしています。
|拡張子 |目的 |
|----------|----------|
| **ペン** |ステージ上に線や形を描く |
| **ビデオセンシング** |動き検出にウェブカメラを使用する |
| **テキスト読み上げ** |テキストを音声に変換 |
| **翻訳** |言語間でテキストを翻訳する |
| **メイキー メイキー** |物理オブジェクトを入力として接続する |
| **マイクロ:ビット** | BBC micro:bit ハードウェアを接続する |
| **レゴ マインドストーム** |レゴロボットを制御 |
| **音楽** |音符や楽器を演奏する | 写真
### スクラッチ ファイル形式
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

### オフラインエディター
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

## テストとデバッグ
### 組み込みデバッグツール
Scratch には、プロジェクトをデバッグするためのいくつかの組み込みツールが用意されています。
|ツール |使い方 |
|------|-----------|
| **タートルモード** |スプライトを右クリックして「デバッグを表示」を選択すると、座標が表示されます。
| **可変モニター** |変数を右クリックして「表示」を選択すると、その値がリアルタイムで表示されます。
| **モニターのリストを表示** |リストの内容を通常、行、または列表示で表示する |
| **ターボモード** |実行を高速化するには、Shift キーを押しながら緑色のフラグをクリックします。
| **シングルステップモード** | 「単一ステップ」の緑色のフラグを右クリックします (実行が遅くなります)。
### デバッグパターン
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

### 一般的な問題
|問題 |原因 |ソリューション |
|----------|----------|----------|
|スプライトが応答しない |イベントなしのハットブロック | 「緑の旗がクリックされたとき」またはその他のイベントを追加 |
|クローンが機能しない |クローンが作成されましたが表示されません | 「クローンとして開始するとき」の後に「表示」ブロックを追加します。
|スプライト間で共有される変数 |グローバル変数とローカル変数の混同 | 「このスプライトのみ」オプションを使用します。
|ブロードキャストが受信されませんでした |メッセージ名が間違っています |ブロードキャスト名と受信名が正確に一致することを確認します。
|無限ループのフリーズ |待ち時間なしで「永遠に」 |小さな「待機」ブロックをタイトなループに追加します。
---

## 相互運用性
### ハードウェア拡張機能
Scratch は拡張機能を通じて物理ハードウェアに接続できます。
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

### スクラッチ拡張 API (カスタム拡張)
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

## デザインパターン
### パターン 1: プラットフォーマーの動き
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

### パターン 2: スクロール背景
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

### パターン 3: スプライト追従 (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### パターン 4: リストを使用した在庫システム
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

### パターン 5: クローンを含むパーティクル システム
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

## パフォーマンスと最適化
### スプライトの最適化
|テクニック |影響 |説明 |
|----------|----------|---------------|
| **クローンを最小限に抑える** |高 |各クローンはメモリを消費します。終わったら削除 |
| **衣装を減らす** |中 |コスチュームの切り替えが少ないほど、レンダリングのオーバーヘッドが少なくなります。
| **「画面を更新せずに実行」を使用します** |高 |画面を更新しないカスタム ブロックはより高速に実行されます。
| **「発言」ブロックを制限する** |中 |吹き出しによりレンダリングのオーバーヘッドが発生する |
| **すべてのスプライトで「永遠」を避ける** |中 |定期的なポーリングの代わりにブロードキャストとイベントを使用する |
### クローン管理
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

### 最適化チェックリスト
|テクニック |影響 |説明 |
|----------|----------|---------------|
| **画面を更新せずに実行** |非常に高い |カスタム ブロックは速度を上げるためにレンダリングをスキップします |
| **アクティブなクローンを最小限に抑える** |高 |クローンが不要になったらすぐに削除します。
| **ブロードキャストは控えめに使用してください** |中 |フレームごとのブロードキャストが多すぎると遅延が発生します。
| **衣装を簡素化** |中 |画像が小さいほどレンダリングが速くなります |
| **リスト操作を削減** |中 |大きなリストをフレームごとにスキャンすることは避けてください。
| **「待機」ブロックを使用する** |低い |永久ループでの CPU の占有を防ぐ |
---

## 導入と実際の使用法
### プロジェクトの共有
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

### 実際の教育用途
|コンテキスト |スクラッチの使い方 |スケール |
|-------|-------|------|
| **幼稚園から高等学校まで** | CSクラスでのプログラミング入門 | 190 か国以上で使用 |
| **コーディング クラブ** | Scratch Club / CoderDojo ワークショップ |世界中の 3000 以上のクラブ |
| **図書館** |放課後プログラミング プログラム |公共図書館システム |
| **ホームスクーリング** |マイペースなプログラミング教育 |何百万人もの家庭学習者 |
| **大学 CS0** |非主要な CS 入門コース |大学ブリッジプログラム |
| **アクセシビリティ** |視覚障害者にプログラミングを教える |スクリーン リーダーのサポート |
| **セラピー** |認知能力と運動能力の発達 |作業療法 |
### 教育研究におけるスクラッチ
研究によると、Scratch は次のことを効果的に教えることができます。
- **逐次的思考**: 問題を順序立てたステップに分割する
- **デバッグ スキル**: ロジック内のエラーを見つけて修正する
- **クリエイティブ表現**: アート、音楽、プログラミングの組み合わせ
- **コラボレーション**: 他人のプロジェクトをリミックスして構築する
- **永続性**: プロジェクトを反復して改善します。
---

## ゼロからの移行
Scratch を学習した後の一般的な次のステップは次のとおりです。
|次の言語 |なぜ |
|--------------|-----|
| **Python** |最も自然な遷移 - 読みやすい構文、同様のロジック概念 |
| **JavaScript** | Web/ゲームに興味がある場合 - 即座に視覚的なフィードバック |
| **Lua (Roblox/Love2D 経由)** |ゲーム開発に興味がある方 |
| **アプリ発明者** | Android アプリ用のビジュアル ブロック (同じ MIT 系統) |
| **ブロックリー** | Google のビジュアル プログラミング ライブラリ (同様の概念) |
### コンセプトのマッピング: スクラッチから Python へ
|スクラッチコンセプト | Python の同等物 |
|-|-----------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`|関数呼び出しまたはイベント システム |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0 からインデックス付き!) |
| `length of [list]`| `len(list)`|
---

## スクラッチを使用する場合
|シナリオ |スクラッチをする理由 |より良い代替案 |
|----------|-----------|--------|
|子供たち (8 ～ 16 歳) にコードを教える |このために特別に設計されました | — |
|計算論的思考の紹介 |視覚的、構文エラーなし | — |
|学校のワークショップ / コーディング クラブ |無料、ブラウザベース、セットアップ不要 | — |
|ゲームのアイデアを視覚的にプロトタイプ化する |高速な反復 | — |
|専門能力開発 |この目的のために設計されていません | Python、JavaScript、任意のテキスト言語 |
|大学レベルのCS教育 |シンプルすぎる | Python、Java、C |
---

＃＃ まとめ
Scratch は従来の意味でのプログラミング言語ではなく、学習環境です。その天才的な点は、子供とインタラクティブなものを作る喜びとの間にあるあらゆる障壁を取り除くことです。 Scratch は構文ではなく概念に重点を置くことで、あらゆる言語に応用できるプログラミングの基礎を教えます。若い学習者にプログラミングを紹介するには、Scratch がゴールドスタンダードです。