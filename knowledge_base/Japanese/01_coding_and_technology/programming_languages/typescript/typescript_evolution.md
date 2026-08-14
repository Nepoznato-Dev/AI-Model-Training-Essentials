<!--
---
# Metadata
title: "TypeScript — Version History & Evolution"
description: "Comprehensive version history and evolution of TypeScript from 0.8 to modern TypeScript."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [typescript, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# TypeScript — バージョン履歴と進化
## タイムライン
|バージョン |発売日 |主要テーマ |
|----------|---------------|----------|
| 0.8 | 2012 年 10 月 |初期公開リリース (Anders Hejlsberg) |
| 0.9 | 2013年4月 |ジェネリック |
| 1.0 | 2014年4月 |最初の安定版リリース |
| 1.1 | 2014 年 11 月 |コンパイラのパフォーマンス |
| 1.4 | 2015年1月 |テンプレート リテラル タイプ (基本)、`let` |
| 1.5 | 2015 年 7 月 |  `namespace`、`destructuring`、`for...of` |
| 1.6 | 2015年9月 | `abstract`クラス、JSX サポート |
| 1.7 | 2015 年 11 月 | `async/await`(ES2017 ターゲット) |
| 1.8 | 2016年2月 |タグ付きテンプレート文字列、`--strictNullChecks` |
| 2.0 | 2016年9月 | **主要**: 和集合/交差タイプ、`never`、`keyof`、`protected`|
| 2.1 | 2016年12月 | `keyof`、マップされた型、`async` ジェネレーター |
| 2.2 | 2017年2月 |  `object`タイプ、改良型`this` |
| 2.3 | 2017年4月 |一般的なデフォルト、`--strict` モード |
| 2.4 | 2017年6月 |弱い型、文字列列挙型 |
| 2.5 | 2017年9月 |オプションのキャッチ バインディング |
| 2.6 | 2017年10月 |厳密な関数型、`--strictFunctionTypes` |
| 2.7 | 2018年1月 |確定割り当て (`!`)、`const` 列挙型 |
| 2.8 | 2018年3月 | **条件型**、`Exclude`、`Extract`|
| 2.9 | 2018年6月 |  数値/記号の場合は `keyof`、`import()` タイプ |
| 3.0 | 2018年7月 | **主要**: 残りのタプル、`unknown`、プロジェクト参照 |
| 3.1 | 2018年9月 |タプル、`readonly` 配列のマップされた型 |
| 3.2 | 2018年11月 | `bigint`、`object`スプレッド |
| 3.4 | 2019年3月 | `const`アサーション、高次型推論 |
| 3.5 | 2019年5月 | `Omit`ヘルパー タイプ |
| 3.7 | 2019年11月 | **オプションのチェーン**、ヌル合体、再帰型 |
| 3.8 | 2020年2月 | `type-only`インポート/エクスポート、`#private` フィールド |
| 3.9 | 2020年5月 | `// @ts-expect-error`、推論の改善 |
| 4.0 | 2020年8月 | **主要**: 可変個引数タプル、ラベル付きタプル、テンプレート リテラル型 |
| 4.1 | 2020年11月 | **テンプレート リテラル タイプ**、キーの再マッピング、再帰的条件 |
| 4.2 | 2021年2月 |抽象プロパティ、マップされた型の`~`|
| 4.3 | 2021年6月 |個別の書き込みタイプ、`override` キーワード |
| 4.4 | 2021年8月 |シンボル/インデックス署名、制御フローの絞り込み |
| 4.5 | 2021年11月 | `.js`からの `.d.ts`、`.d.ts` の`await`|
| 4.6 | 2022 年 2 月 |ブロック スコープの関数チェック、オブジェクトの残余厳密型 |
| 4.7 | 2022 年 5 月 | `infer`の`extends`制約、`.ts`の ESM |
| 4.8 | 2022 年 8 月 |交差点の削減の改善、`--strictNullChecks` の修正 |
| 4.9 | 2022 年 11 月 | **`satisfies`演算子**、`in` 狭め |
| 5.0 | 2023 年 3 月 | **主要**:`const`タイプのパラメータ、デコレータ、`enum` のオーバーホール |
| 5.1 | 2023 年 6 月 |無関係な型セッター、`--exactOptionalPropertyTypes` |
| 5.2 | 2023 年 8 月 | `using`宣言 (明示的なリソース管理) |
| 5.3 | 2023 年 11 月 |インポート属性、`switch true` 絞り込み |
| 5.4 | 2024 年 3 月 | `NoInfer`ユーティリティ、縮小されたクロージャ パラメータ |
| 5.5 | 2024 年 6 月 |推論型述語、正規表現の`@`|
| 5.6 | 2024 年 9 月 | `--erasableSyntaxOnly`、反復子ヘルパー |
| 5.7 | 2024 年 11 月 | `--noCheck`、パス補完 |
| 5.8 | 2025 年 2 月 |`isolatedDeclarations`の改善 |
## 主要なマイルストーン
### 初期の頃 (2012 ～ 2015 年)
- **0.8 (2012)**: Anders Hejlsberg (C# 作成者) Microsoft で TypeScript をリード
- **1.0 (2014)**: 安定版リリース。クラス、インターフェース、基本型
- **1.5 (2015)**: ES6 機能 — 構造化、名前空間、`for...of`
### 文字革命 (2016–2018)
- **2.0 (2016)**: 共用体型、交差型、`never`、`keyof`— TypeScript の型システムが独自になります
- **2.8 (2018)**: 条件付き型 — 高度な型レベル プログラミングの基礎
- **3.0 (2018)**: 残りパラメータのタプル、`unknown` タイプ、プロジェクト参照
### 最新の TypeScript (2019–現在)
- **3.7 (2019)**: オプションのチェーン`?.`とヌル合体`??`(JS 標準以前!)
- **4.0 (2020)**: 可変個引数タプル、テンプレート リテラル型
- **4.1 (2020)**: テンプレート リテラル型 — 型レベルの文字列操作
- **4.9 (2022)**:`satisfies`演算子 — 拡張を行わない型チェック
- **5.0 (2023)**:`const`型パラメータ、デコレータ (ステージ 3)
- **5.2 (2023)**:`using`宣言 — 明示的なリソース管理
## 型システムの進化
```
2012: Basic types, classes, interfaces
2014: Generics, enums
2016: Union types, intersection types, discriminated unions
2018: Conditional types, mapped types, keyof, infer
2020: Template literal types, variadic tuples
2022: satisfies operator
2023: const type parameters
2023: using declarations
```

## デコレータの進化
```
2014: TypeScript experimental decorators (legacy)
2022: TC39 stage 3 decorators proposal
2023: TypeScript 5.0 — standard decorators (stage 3)
2024: Both legacy and standard decorators supported
```

## 構成の進化
```
2014: Basic tsconfig.json
2016: --strict flag introduced
2017: --strictFunctionTypes, --strictNullChecks
2018: --strict mode becomes recommended
2020: --strictPropertyInitialization
2023: --exactOptionalPropertyTypes
2024: --erasableSyntaxOnly, --noCheck
```

## エコシステムの成長
```
2012: TypeScript launches — few adopters
2014: Angular 2 built with TypeScript
2016: VS Code (built with TS) drives adoption
2018: TypeScript overtakes Flow (React community)
2020: TypeScript used by most npm packages
2023: TypeScript 5.0 — decorators, const generics
2025: TypeScript — de facto standard for large JS projects
```

## 主要な設計上の決定事項
```
1. Structural typing (not nominal) — duck typing for types
2. Gradual adoption — any type, type widening
3. Erased types — no runtime overhead
4. JS compatibility — all valid JS is valid TS
5. Declaration files (.d.ts) — types for JS libraries
6. Playground — interactive type exploration
```
