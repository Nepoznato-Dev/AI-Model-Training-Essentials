---
# Metadata
title: "R — Version History & Evolution"
description: "Comprehensive version history and evolution of R from S-Plus origins to modern R."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [r, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# R — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| S | 1976年 | S 言語はベル研究所 (ベッカー、チェンバース、ウィルクス) で作成されました。
|エスプラス | 1988年 |商用 S 実装 (StatSci) |
| R0.10 | 1995年 |最初の R リリース (Ihaka & Gentleman、オークランド) |
| R1.0 | 2000年 | **最初の安定版リリース** |
| R1.4 | 2002年 | S4 のクラスとメソッド |
| R2.0 | 2004年 |正規表現、`R.home()` |
| R2.1 | 2005年 | UTF-8 のサポート |
| R2.5 | 2007年 |メモリ管理の改善 |
| R2.8 | 2008年 |参照クラス (初期の OOP) |
| R2.14 | 2011年 |  `loadNamespace`、パラレルパッケージ |
| R2.15 | 2012年 | `stringsAsFactors = FALSE`オプション |
| R3.0 | 2013年 | **64 ビット サポート**、参照クラスは安定しています |
| R3.1 | 2014年 | `vapply`の改善 |
| R3.2 | 2015年 | `readRDS`/`saveRDS`、サンプリングの改善 |
| R3.3 | 2016年 | `xz`圧縮、`person()` の改善 |
| R3.4 | 2017年 |シリアル化の並列化、`switch` の改善 |
| R3.5 | 2018年 |デフォルトの`stringsAsFactors`警告 |
| R3.6 | 2019年 |乱数ジェネレーターの改善 |
| R4.0 | 2020年 | **メジャー**:`stringsAsFactors = FALSE`デフォルト |
| R4.1 | 2021年 | **パイプ`|>`**、無名関数`\(x) ...`|
| R4.2 | 2022年 | `|>`は、`on.exit` のプレースホルダー`_`、`after`引数を取得します。
| R4.3 | 2023年 | `R_cmd`の改善、エラー メッセージの改善 |
| R4.4 | 2024年 | `find()`の改善、`deparse1()` のデフォルト |
| R4.5 | 2025年 |継続的な改善 |
## 主要なマイルストーン
### S および S-PLUS (1976 ～ 1994)
- **1976**: ジョン・チェンバースがベル研究所で S を作成 — 言語としての統計プログラミング
- **1988**: S-PLUS — StatSci (後の TIBCO) による商用実装
- S の導入: データ フレーム、式 (`y ~ x`)、遅延評価
### R の誕生 (1995 ～ 2000)
- **1995**: ロス・イハカとロバート・ジェントルマンがオークランド大学で R を作成
- 「R」 = ロスとロバートの頭文字
- 無料のオープンソース S 実装として設計
- **2000**: R 1.0 — 最初の安定版リリース。 CRAN（総合Rアーカイブネットワーク）設立
### R マチュア (2000–2012)
- **1.4 (2002)**: S4 クラス — 正式な OOP システム
- **2.0 (2004)**: 正規表現、内部構造の改善
- **2.8 (2008)**: 参照クラス — 初期の近代的な OOP
- **2.14 (2011)**:`parallel`パッケージ (マルチコア サポート)
### R 3.x — データ サイエンスの時代 (2013 ～ 2019 年)
- **3.0 (2013)**: 64 ビットのサポート — 大規模なデータセットを処理します
- **3.1–3.6**: 段階的な改善
- **2013–2015**: 「R 革命」 — ggplot2、dplyr、tidyverse 変換データ サイエンス
### R 4.x — モダン R (2020–現在)
- **4.0 (2020)**: デフォルトで`stringsAsFactors = FALSE`— 数十年来の問題点を修正
- **4.1 (2021)**: **ネイティブ パイプ`|>`**、匿名関数短縮表現`\(x) x + 1`
- **4.2 (2022)**: パイプ プレースホルダー`_`、`\(x, y)`の短縮表記が安定しました
- **4.3 (2023)**: エラー メッセージの改善 (修正の提案)
- **4.4–4.5**: 継続的な改良
## 構文の進化
```r
# S / early R: Basic statistics
x <- c(1, 2, 3, 4, 5)
mean(x)
lm(y ~ x, data = df)

# R 3.x: tidyverse revolution (2013+)
library(dplyr)
library(ggplot2)
df %>%
  filter(age > 18) %>%
  group_by(category) %>%
  summarise(mean_age = mean(age))

# R 4.0: stringsAsFactors default changes
df <- read.csv("data.csv")  # strings no longer auto-converted to factors

# R 4.1: Native pipe and lambda shorthand
df |>
  filter(age > 18) |>
  mutate(label = \(x) paste(x$name, x$age))

# R 4.2: Pipe placeholder
result |> (\(x) x[is.na(x)] <- 0)()
# With placeholder:
x |> f(y = _)

# R 4.3+: Better error messages
mean("hello")
# Warning: In mean.default("hello") : argument is not numeric or logical: returning NA
```

## パッケージ エコシステムの進化
```
1995: R launches with basic stats packages
2000: CRAN established — centralized package repository
2001: Bioconductor — bioinformatics packages
2007: ggplot2 released (Hadley Wickham) — grammar of graphics
2008: reshape2 — data reshaping
2012: dplyr released — fast data manipulation
2014: tidyr, readr — complete data science toolkit
2015: tidyverse meta-package — unified ecosystem
2016: RMarkdown — literate programming
2019: Quarto — next-gen documents
2020: RStudio → Posit — company rebrands, broader tooling
2025: 20,000+ packages on CRAN; R is the #1 statistical language
```

## OOP の進化
```
S3 (1992):   Informal classes, generic functions — method dispatch by class attribute
S4 (2002):   Formal classes, multiple inheritance, formal generics
Reference Classes (2010):  Mutable objects, reference semantics
R6 (2014):   Simple reference classes (popular alternative)
S7 (2023):   New OOP system — unifies S3/S4, modern design
```

## 主要な設計原則
```
1. "Statistics first" — designed for data analysis
2. "Functional programming" — functions are first-class
3. "Vectorized operations" — operate on whole vectors at once
4. "Lazy evaluation" — arguments evaluated only when needed
5. "Extensibility" — S3/S4 generic functions, packages
6. "Open source" — GPL license, community-driven
```

## エコシステムの成長
```
1995: R created at University of Auckland
2000: CRAN established — package repository
2003: Bioconductor — bioinformatics ecosystem
2007: ggplot2 — revolutionizes data visualization
2012: dplyr — modern data manipulation
2014: tidyverse — unified data science toolkit
2015: RMarkdown — reproducible research
2020: R 4.0 — modern defaults
2021: R 4.1 — native pipe |>
2025: R remains dominant in statistics, bioinformatics, and academia
       20,000+ CRAN packages; used by pharma, finance, research
```
