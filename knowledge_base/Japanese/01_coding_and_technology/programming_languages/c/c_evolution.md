<!--
---
# Metadata
title: "C — Version History & Evolution"
description: "Comprehensive version history and evolution of C from K&R to C23."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [c, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# C — バージョン履歴と進化
## タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| K&R C | 1972–78 |オリジナル C (カーニハン & リッチー) |
| C89/C90 | 1989/90 |最初の ANSI/ISO 規格 |
| C95 | 1995年 |修正 1:`wchar.h`、ダイグラフ |
| C99 | 1999年 | `//`コメント、`inline`、`bool`、 VLA、指定された初期化子 |
| C11 | 2011年 |アトミック、スレッド、`_Static_assert`、匿名構造体/共用体 |
| C17 | 2018年 |欠陥修正 (新機能なし) |
| C23 | 2024年 | `nullptr`、`typeof`、`constexpr`、`#embed`、属性 |
## 主要なマイルストーン
### K&R C (1972–1989)
- **1972**: デニス・リッチーがベル研究所で Unix 用の C を作成
- **1978**: カーニハンとリッチーが「The C Programming Language」を出版
- 主な機能:`struct`、`int`、`char`、ポインター、関数、`#include`
-`void`、`enum`、`unsigned`、`const`はありません
### C89/C90 — スタンダード (1989)
- 最初の ANSI 規格 (ANSI X3.159-1989)
- 追加:`void`、`enum`、`const`、`volatile`、関数プロトタイプ、`signed`
- 「黄金時代」 — ポータブルで広く採用されている
- 依然として多くの組み込みシステムのベースライン
### C99 — モダン C (1999)
-`//`単一行コメント
- `inline`関数
-`<stdbool.h>`経由の`bool`
- 可変長配列 (VLA)
- 指定されたイニシャライザ:`struct Point p = {.x = 1, .y = 2};`
-`for (int i = 0; ...)`— ループ内の宣言
-`<stdint.h>`:`int32_t`、`uint64_t`など
-`restrict`キーワード
- 可変個引数マクロ
- 複合リテラル
### C11 — 安全性と同時実行性 (2011)
-`<stdatomic.h>`— アトミック操作
-`<threads.h>`— スレッドのサポート
-`_Static_assert`— コンパイル時のアサーション
- ネストされた構造体の匿名構造体/共用体
-`_Alignof`、`_Alignas`— アライメント制御
- 一般的な選択:`_Generic(x, int: ..., default: ...)`
- Unicode サポート:`<uchar.h>`
- オプションの VLA サポート (組み込みの問題によりオプションになりました)
### C23 — ルネサンス (2024)
-`nullptr`— NULL ポインタ定数 (`NULL` マクロを置き換えます)
-`typeof`— 型推論
-`constexpr`— 定数式
-`#embed`— コンパイル時にバイナリ データを埋め込む
-`[[attribute]]`構文 (C23 スタイルの属性)
- キーワードとして`true`/`false`(`<stdbool.h>`は必要なくなりました)
- `auto`型推論
-`static_assert`(アンダースコアなし)
-`alignof`(アンダースコアなし)
- デフォルトの`int`リターンが削除されました
## 標準プロセス
```
1983: ANSI X3J11 committee formed
1989: C89 ratified (ANSI)
1990: C90 ratified (ISO/IEC 9899:1990)
1999: C99 (ISO/IEC 9899:1999)
2011: C11 (ISO/IEC 9899:2011)
2018: C17 (ISO/IEC 9899:2018) — defect fixes only
2024: C23 (ISO/IEC 9899:2024)
```

## 互換性の哲学
```
C has always valued backward compatibility:
- C99 compilers accept most C89 code
- C11 compilers accept most C99 code
- C23 makes some breaking changes (removes K&R function definitions)
- Key principle: "Trust the programmer"
- Key principle: "No hidden costs"
- Key principle: "Portability through standardization"
```

## プリプロセッサの進化
```
K&R:    #include, #define, #ifdef, #if
C89:    #elif, function-like macros, stringification
C99:    Variadic macros (__VA_ARGS__), _Pragma
C11:    _Static_assert
C23:    #embed, [[attribute]], #if has_include
```

## 型システムの進化
```
K&R:    int, char, float, double, struct, pointer, function
C89:    void, enum, const, volatile, signed, unsigned
C99:    bool (via macro), complex, long long, intN_t types
C11:    _Atomic, _Alignas, _Generic, char16_t, char32_t
C23:    typeof, nullptr, auto, bool (keyword), constexpr
```

## 生態系への影響
```
1970s: C replaces assembly for OS development (Unix)
1980s: C becomes dominant systems language
1990s: C99 influences Java, C#, JavaScript
2000s: C89 still widely used in embedded
2010s: C11 adds modern concurrency
2020s: C23 modernizes while preserving simplicity
2025: C remains the foundation of all computing (Linux, Windows, macOS kernels)
```
