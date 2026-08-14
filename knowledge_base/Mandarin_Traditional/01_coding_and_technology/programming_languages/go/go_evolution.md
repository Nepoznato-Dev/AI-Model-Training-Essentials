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
# Go — 版本歷史與演變
## 時間軸
|版本 |發佈日期 |關鍵主題 |
|--------|-------------|------------|
| 1.0 | 2012 年 3 月 |第一個穩定版本 |
| 1.1| 2013 年 5 月 |效能，競賽偵測器|
| 1.3 | 1.3 2014 年 6 月 |網路輪詢，加密/TLS |
| 1.4 | 1.4 2014 年 12 月 | Bootstrap with Go（自架）|
| 1.5 | 1.5 2015 年 8 月 | **並發GC**，寫屏障|
| 1.7 | 1.7 2016 年 8 月 |`context`套件、`testing` 子測驗 |
| 1.8 | 1.8 2017 年 2 月 |`http.Server.Shutdown`，插件 |
| 1.9 | 1.9 2017 年 8 月 |型別別名，並行`make`|
| 1.10 | 1.10 2018 年 2 月 |`database/sql`連線池 |
| 1.11 | 1.11 2018 年 8 月 | **Go 模組**，`go mod` |
| 1.12 | 1.12 2019 年 2 月 | TLS 1.3，模組版本控制 |
| 1.13 | 1.13 2019 年 9 月 |`errors.Is/As`、數位文字`0b`、`0o`|
| 1.14 | 1.14 2020 年 2 月 | **Windows 上的重疊 I/O**、goroutine 搶佔 |
| 1.15 | 1.15 2020 年 8 月 |`time.Ticker`/`Timer`重位，模組代理 |
| 1.16 | 1.16 2021 年 2 月 |`embed`包，`io/fs`，預設模組感知 |
| 1.17 | 1.17 2021 年 8 月 |切片到陣列的轉換，`unsafe.Slice` |
| 1.18 | 1.18 2022 年 3 月 | **泛型**、模糊測驗、工作區 |
| 1.19 | 1.19 2022 年 8 月 |文件評論、記憶體模型修訂|
| 1.20 | 1.20 2023 年 2 月 | `errors.Join`，設定檔引導優化 |
| 1.21 | 1.21 2023 年 8 月 | **`slog`**、`min/max` 內建、`maps/slices` |
| 1.22 | 1.22 2024 年 2 月 |範圍超過整數，增強路由|
| 1.23 | 1.23 2024 年 8 月 |迭代器（`iter`）封裝，定時器變更|
| 1.24 | 1.24 2025 年 2 月 |`weak`包，改進的地圖 |
## 主要里程碑
### 開始（2009-2012）
- **2009**：Go 被 Google 宣布（Robert Griesemer、Rob Pike、Ken Thompson）
- **2012**：**Go 1.0** —“Go 1 相容性承諾”
### 性能與工具（2012–2018）
- **1.1**：效能提升 30% 以上；種族偵測器
- **1.5**：併發垃圾收集器（GC 暫停從毫秒降至微秒）
- **1.5**：Go 編譯器引導 - 用 Go 寫（不再是 C）
- **1.7**：`context` 封裝成為標準
### 模組與生態系（2018–2021）
- **1.11**：**Go 模組** — 官方依賴管理
- **1.13**：`errors.Is/As` — 錯誤包裝變成慣用
- **1.16**：`embed` 套件 — 在編譯時嵌入文件
### 現代圍棋（2022 年至今）
- **1.18**：**泛型** — 帶有約束的型別參數
- **1.21**：`slog` — stdlib 中的結構化日誌記錄；`min/max`內建
- **1.22**：整數範圍 (`for i := range 10`)
- **1.23**：迭代器套件 - stdlib 中的惰性求值
## 泛型之旅
```
2010: "Go doesn't need generics" (early stance)
2016: Go generics proposal discussions begin
2018: Type parameters design draft published
2020: Go 2 generics proposal (draft designs)
2022: Go 1.18 — generics land! Type parameters, constraints
2023: Generic code patterns emerge (slices, maps packages)
2024: Community adapts — generic data structures, algorithms
```

## 錯誤處理哲學
```
1.0:     Explicit error returns — "errors are values"
1.13:    Error wrapping with %w — "inspect and unwrap"
1.20:    errors.Join — multiple errors
Future:  go2 proposal for try/handle (not yet adopted)
```

## 並發演進
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

## Go 相容性承諾
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

## 生態系成長
```
2012: Go 1.0 — basic stdlib, no package manager
2014: dep (early dependency management experiments)
2018: Go modules — official solution
2019: Go used by Uber, Twitch, Dropbox, Cloudflare
2022: Generics — opens new library design patterns
2023: Go in Kubernetes, Docker, Terraform, Hugo
2025: Top 10 most used language; cloud-native standard
```

## 效能演變
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
