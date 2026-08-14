---
# Metadata
title: "Java — Version History & Evolution"
description: "Comprehensive version history and evolution of Java from 1.0 to modern Java."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [java, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Java — バージョン履歴と進化
## タイムライン
|バージョン |発売日 |主要テーマ |
|----------|---------------|----------|
| JDK 1.0 | 1996 年 1 月 |初期リリース (「オーク」) |
| JDK 1.1 | 1997 年 2 月 |内部クラス、JDBC、RMI |
| J2SE 1.2 | 1998年12月 |コレクション フレームワーク、Swing、`strictfp` |
| J2SE 1.3 | 2000年5月 |ホットスポット JVM、`assert` |
| J2SE 1.4 | 2002 年 2 月 | `assert`、NIO、正規表現、`java.net` |
| J2SE 5.0 | 2004 年 9 月 | **主要**: ジェネリック、列挙型、注釈、オートボクシング、可変引数 |
| Java SE 6 | 2006 年 12 月 |スクリプト、コンパイラ API、インターフェイス上の`@Override`|
| Java SE 7 | 2011 年 7 月 | `try-with-resources`、文字列上の `switch`、NIO.2 |
| Java SE 8 | 2014年3月 | **主要**: Lambdas、Streams、`Optional`、`java.time`、デフォルトのメソッド |
| Java 9 | 2017年9月 |モジュール (JPMS)、`var`、`jshell`、プライベート インターフェイス メソッド |
| Java 10 | 2018年3月 |  ローカル変数の場合は`var`|
| Java 11 | 2018年9月 | **LTS**:`String`メソッド、`HttpClient`、単一ファイルの起動 |
| Java 12 | 2019年3月 |式の切り替え (プレビュー) |
| Java 13 | 2019年9月 |テキスト ブロック (プレビュー) |
| Java 14 | 2020年3月 | `record`(プレビュー)、スイッチ式、`instanceof` パターン |
| Java 15 | 2020年9月 |テキスト ブロック、シールされたクラス (プレビュー) |
| Java 16 | 2021年3月 | `record`、`instanceof`パターン マッチング |
| Java 17 | 2021年9月 | **LTS**: シールされたクラス、`switch` のパターン マッチング |
| Java 18 | 2022 年 3 月 |シンプルな Web サーバー、UTF-8 デフォルト |
| Java 19 | 2022 年 9 月 |仮想スレッド (プレビュー)、パターン マッチング |
| Java 20 | 2023 年 3 月 |スコープ付き値 (インキュベーター)、レコード パターン |
| Java 21 | 2023 年 9 月 | **LTS**: **仮想スレッド**、パターン マッチング、`switch` パターン、シーケンスされたコレクション |
| Java 22 | 2024 年 3 月 |文字列テンプレート (プレビュー)、外部メモリ API |
| Java 23 | 2024 年 9 月 |パターン内のプリミティブ型 (プレビュー) |
| Java 24 | 2025 年 3 月 |構造化された同時実行 (プレビュー) |
| Java 25 | 2025 年 9 月 | **LTS**: (予想) |
## 主要なマイルストーン
### クラシック時代 (1996 ～ 2004 年)
- **1.0 (1996)**: 「一度書けばどこでも実行」 — アプレット、AWT
- **1.2 (1998)**: コレクション フレームワーク (Java コレクションの基礎)
- **1.4 (2002)**: NIO、ロギング、正規表現、アサーション
- **5.0 (2004)**: 最大のアップデート — ジェネリックス、列挙型、注釈、オートボクシング、強化された for ループ、可変長引数、`static import`
### エンタープライズ時代 (2006 ～ 2014 年)
- **6 (2006)**: スクリプトのサポート、コンパイラ API
- **7 (2011)**:`try-with-resources`、ダイヤモンド演算子、文字列上の `switch`、NIO.2
- **8 (2014)**: その他の「ビッグバン」 — ラムダ、ストリーム、`Optional`、`java.time`、デフォルト メソッド、 `CompletableFuture`
### 現代 (2017–現在)
- **9 (2017)**: モジュール システム (JPMS)、`var` 、`jshell` REPL
- **11 (2018)**: 6 か月のリリース頻度での最初の LTS。 `HttpClient`; Oracle JDK ライセンスの変更
- **17 (2021)**: LTS — シールされたクラス、パターン マッチング
- **21 (2023)**: LTS — **仮想スレッド** (Project Loom)、パターン マッチング、レコード パターン
## 6 か月のリリース頻度
```
Before Java 9:  Major releases every 2-4 years
Java 9+:        New release every 6 months (March & September)
LTS releases:   Every ~2 years (8, 11, 17, 21, 25...)
Non-LTS:        Feature previews, 6-month support
```

## ジェネリックの旅
```
2004: Java 5.0 — type erasure generics (backward compatible)
2014: Java 8 — improved inference with lambdas
2016: Java 9 — diamond operator with anonymous classes
2018: Java 11 — `var` with generics
2023: Java 21 — record patterns with generics
```

## 関数型プログラミングの進化
```
2004: Anonymous inner classes (verbose)
2004: Java 5 — enums as pseudo-functional
2014: Java 8 — lambdas, streams, Optional
2017: Java 9 — Stream API additions
2019: Java 12 — switch expressions
2023: Java 21 — pattern matching in switch, record patterns
```

## 同時実行の進化
```
1.0:     Thread class, synchronized
1.5:     java.util.concurrent (Executors, locks, atomics)
1.7:     ForkJoinPool
1.8:     CompletableFuture, parallel streams
1.9:     Flow API (reactive streams)
1.19:    Virtual threads preview
1.21:    **Virtual threads** (Project Loom) — lightweight threads
```

## 言語機能の進化
```
Java 5:   Generics, enums, annotations, autoboxing, varargs
Java 7:   try-with-resources, diamond <>, switch on String
Java 8:   Lambdas, streams, default methods, Optional
Java 9:   var (local), modules, jshell
Java 14:  record (preview), switch expressions
Java 16:  record, instanceof pattern
Java 17:  sealed classes, switch pattern matching
Java 21:  virtual threads, pattern matching, record patterns
```

## JVM の進化
```
1.0:  Interpreter
1.3:  HotSpot (JIT compilation)
1.5:  Generics via type erasure
1.7:  InvokeDynamic (for JVM languages)
1.9:  Module system, AOT compilation (experimental)
16:   ZGC (low-latency GC) production-ready
21:   Virtual threads, generational ZGC
```

## エコシステムの成長
```
1998: J2EE — enterprise Java begins
2001: Spring Framework
2004: Hibernate, Maven
2006: Java on Android (modified Java)
2010: Oracle acquires Sun (Java)
2014: Java 8 — Spring Boot era
2018: Java 11 — modular JDK, GraalVM
2023: Java 21 — virtual threads, Spring Boot 3
2025: Java remains #1 enterprise language
```
