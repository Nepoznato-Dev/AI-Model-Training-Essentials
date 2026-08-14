---
# Metadata
title: "Go — Version History & Evolution"
description: "Comprehensive version history and evolution of Go from 1.0 to modern Go."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [go, golang, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Go — バージョン履歴と進化
## タイムライン
|バージョン |発売日 |主要テーマ |
|----------|---------------|----------|
| 1.0 | 2012年3月 |最初の安定版リリース |
| 1.1 | 2013年5月 |パフォーマンス、競合検出器 |
| 1.3 | 2014年6月 |ネットワークポーリング、crypto/tls |
| 1.4 | 2014年12月 | Go によるブートストラップ (セルフホスティング) |
| 1.5 | 2015年8月 | **同時 GC**、書き込みバリア |
| 1.7 | 2016 年 8 月 | `context`パッケージ、`testing` サブテスト |
| 1.8 | 2017年2月 | `http.Server.Shutdown`、プラグイン |
| 1.9 | 2017年8月 |型別名、並列`make`|
| 1.10 | 2018年2月 | `database/sql`接続プール |
| 1.11 | 2018年8月 | **Go モジュール**、`go mod` |
| 1.12 | 2019年2月 | TLS 1.3、モジュールのバージョン管理 |
| 1.13 | 2019年9月 | `errors.Is/As`、数値リテラル`0b`、`0o`|
| 1.14 | 2020年2月 | **Windows での重複 I/O**、ゴルーチンのプリエンプション |
| 1.15 | 2020年8月 | `time.Ticker`/`Timer`リセット、モジュール プロキシ |
| 1.16 | 2021年2月 | `embed`パッケージ、`io/fs`、デフォルトでモジュール認識 |
| 1.17 | 2021年8月 |スライスからアレイへの変換、`unsafe.Slice` |
| 1.18 | 2022 年 3 月 | **ジェネリック**、ファジング、ワークスペース |
| 1.19 | 2022 年 8 月 |ドキュメントのコメント、メモリ モデルのリビジョン |
| 1.20 | 2023 年 2 月 | `errors.Join`、プロファイルに基づく最適化 |
| 1.21 | 2023 年 8 月 | **`slog`**、`min/max` ビルトイン、`maps/slices` |
| 1.22 | 2024 年 2 月 |整数を超える範囲、ルーティングの強化 |
| 1.23 | 2024 年 8 月 | Iterator (`iter`) パッケージ、タイマーの変更 |
| 1.24 | 2025 年 2 月 | `weak`パッケージ、改良されたマップ |
## 主要なマイルストーン
### 始まり (2009–2012)
- **2009**: Google が Go を発表 (Robert Griesemer、Rob Pike、Ken Thompson)
- **2012**: **Go 1.0** — 「Go 1 互換性の約束」
### パフォーマンスとツール (2012 ～ 2018)
- **1.1**: 30% 以上のパフォーマンスの向上。レースディテクター
- **1.5**: 同時ガベージ コレクター (GC 一時停止がミリ秒からマイクロ秒に低下)
- **1.5**: Go コンパイラはブートストラップされています — Go で書かれています (C は不要です)
- **1.7**:`context`パッケージが標準になります
### モジュールとエコシステム (2018–2021)
- **1.11**: **Go モジュール** — 公式の依存関係管理
- **1.13**:`errors.Is/As`— エラーラップが慣用的になる
- **1.16**:`embed`パッケージ — コンパイル時にファイルを埋め込む
### モダン囲碁 (2022–現在)
- **1.18**: **ジェネリック** — 制約のある型パラメータ
- **1.21**:`slog`— stdlib の構造化ログ。 `min/max`ビルトイン
- **1.22**: 整数の範囲 (`for i := range 10`)
- **1.23**: Iterator パッケージ — stdlib での遅延評価
## ジェネリックの旅
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## エラー処理の哲学
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## 同時実行の進化
```
1.0:  Goroutines + channels — CSP-inspired
1.1:  Race detector
1.4:  Non-blocking syscalls (net poller)
1.5:  Concurrent GC
1.7:  context package for cancellation
1.14: Cooperative goroutine preemption (signals)
1.21: Synchronization improvements
1.23: iter package — iterator pattern
```

## Go 互換性の約束
```
Go 1.0 (2012): "Go 1 will be available for a long time.
  Compatibility is important. Programs that work at Go 1
  will continue to work at every subsequent Go 1 release."

This means:
- No breaking changes to the language spec
- No breaking changes to the standard library
- Only additive changes
- Forward compatibility guaranteed
```

## エコシステムの成長
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## パフォーマンスの進化
```
Go 1.0:  Baseline
Go 1.1:  ~30% faster (register-based calling prep)
Go 1.5:  Concurrent GC (pause time: ms → μs)
Go 1.7:  SSA backend (15-30% faster)
Go 1.11: PGO experiments
Go 1.13: Faster map operations
Go 1.18: Generics (initial overhead, optimized in 1.19+)
Go 1.20: Profile-guided optimization
Go 1.22: Faster crypto, improved compiler
```
