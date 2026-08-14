---
# Metadata
title: "Shell & PowerShell — Version History & Evolution"
description: "Comprehensive version history and evolution of Unix Shell and PowerShell from sh to modern shells."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [shell, powershell, bash, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Shell と PowerShell — バージョン履歴と進化
## Unix シェルのタイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
|トンプソン・シュ | 1971年 |最初の Unix シェル (Ken Thompson) |
|ボーン・シュ | 1977年 | **`sh`** — スクリプト、変数、制御フロー |
| csh | 1978年 | C のような構文、ジョブ制御、エイリアス |
| ksh | 1983年 | Korn シェル —`sh`+`csh`の機能 |
|バッシュ | 1989年 | **Bourne Again シェル** — GNU`sh`の置き換え |
|バッシュ2.0 | 1996年 |  `[[ ]]`、`(( ))`、`+=` |
|バッシュ3.0 | 2004年 | `=~`正規表現、`|&` |
|バッシュ4.0 | 2009年 | **連想配列**、`mapfile`、`declare -g`|
|バッシュ4.3 | 2014年 | Shellshock の脆弱性が発見 |
|バッシュ5.0 | 2019年 | `declare -n`名前参照、`printf %q` |
|バッシュ5.1 | 2020年 | `wait -n`、`shopt`の改善 |
|バッシュ5.2 | 2022年 | `${var@U}`(大文字)、`shopt -s compat` |
| zsh | 1990年 |拡張 bash — 補完、テーマ |
|魚 | 2005年 | **ユーザーフレンドリー** — 自動提案、構文ハイライト |
|ヌシェル | 2019年 |構造化データ、テーブルのパイプライン |
|オイル/オーシュ | 2020年 |より優れたセマンティクスを備えた Bash 互換 |
## PowerShell タイムライン
|バージョン |年 |主要テーマ |
|----------|------|----------|
| 1.0 | 2006年 |初期リリース (Microsoft、Jeffrey Snover) |
| 2.0 | 2009年 | **モジュール**、リモート処理、バックグラウンド ジョブ、トランザクション |
| 3.0 | 2012年 |ワークフロー、`Invoke-RestMethod`、スケジュールされたジョブ |
| 4.0 | 2013年 | **望ましい状態構成 (DSC)**、`if` /`switch`の改善 |
| 5.0 | 2016年 | **クラス**、`enum`、`using`、`using module` |
| 5.1 | 2017年 |最新の Windows 専用バージョン |
| 6.0 | 2018年 | **PowerShell コア** — クロスプラットフォーム (Windows、Linux、macOS) |
| 6.1 | 2018年 | `ForEach-Object -Parallel`(実験的) |
| 6.2 | 2019年 | `&&`/`||`パイプライン チェーン オペレーター |
| 7.0 | 2020年 | **主要**:`?.`null 条件、`??` null 合体、`using assembly` |
| 7.1 | 2020年 |三項演算子`? :`、`using module`の改善 |
| 7.2 | 2021年 | **LTS リリース**、`using namespace` の改善 |
| 7.3 | 2022年 | `switch`の改善、`ErrorView` のオプション |
| 7.4 | 2023年 | `using module`の改善、`Get-Error` |
| 7.5 | 2024年 |パフォーマンスの向上、`PSResourceGet` |
| 7.6 | 2025年 |進行中の開発 |
## 主要なマイルストーン
### Unix シェルの遺産 (1971 ～ 1989 年)
- **1971**: Thompson シェル — 最初の Unix シェル、単純なコマンド実行
- **1977**: Bourne シェル (`sh`) — 変数、制御フロー (`if`、`while`)、ヒアドキュメント
- **1978**: C シェル (`csh`) — C に似た構文、ジョブ制御、エイリアス、履歴
- **1983**: Korn シェル (`ksh`) —`sh`+`csh`のベスト版
### bash — スタンダード (1989 年から現在)
- **1989**: Brian Fox が GNU プロジェクト用に bash を作成 — Bourne Again Shell
- **2.0 (1996)**:`[[ ]]`テスト、`(( ))` 算術演算、`+=` 
- **4.0 (2009)**: 連想配列 (`declare -A`)、`mapfile` 
- **5.0 (2019)**: 名前参照、`printf %q` 
- **5.2 (2022)**: 文字列の大文字と小文字の操作
### zsh — パワーユーザーのシェル (1990–現在)
- **1990**: Paul Falstad が zsh を作成 — bash、ksh、tcsh の機能を組み合わせたもの
- **2000年代**: oh-my-zshフレームワーク — テーマ、プラグイン、補完
- **2019**: macOS のデフォルト シェル (bash を置き換えます)
### 魚 — フレンドリー シェル (2005–現在)
- **2005**: アクセル・リルジャンクランツが魚を作成 — 「ついにインタラクティブな貝殻が完成」
- 自動提案、構文ハイライト、Web ベースの設定
- bash と互換性がない - 別のスクリプト言語
### PowerShell — Microsoft のシェル (2006 ～現在)
- **2006**: PowerShell 1.0 — .NET ベース、オブジェクト パイプライン、コマンドレット
- **2.0 (2009)**: モジュール、リモート処理、バックグラウンド ジョブ
- **5.0 (2016)**: クラス、列挙型
- **6.0 (2018)**: **クロスプラットフォーム** — PowerShell Core (.NET Core 上に構築)
- **7.0 (2020)**: null 条件付き`?.`、null 合体`??`、三項 `?:`
## 構文の進化
```bash
# Bourne shell (1977): Basic scripting
#!/bin/sh
name="World"
echo "Hello, $name"
for file in *.txt; do
  echo "Processing $file"
done

# bash 4.0: Associative arrays
declare -A colors
colors[red]="#FF0000"
colors[green]="#00FF00"
echo "${colors[red]}"

# bash 5.0+: Modern bash
mapfile -t lines < input.txt
for line in "${lines[@]}"; do
  echo "${line^^}"  # uppercase
done

# zsh + oh-my-zsh: Enhanced interactive
# Autosuggestions, syntax highlighting, git aliases

# fish: Modern interactive
# Autosuggestions, web config, not bash-compatible
function greet
    echo "Hello, $argv"
end
```

```powershell
# PowerShell 1.0: Basic cmdlets
Get-Process | Where-Object { $_.CPU -gt 100 }

# PowerShell 5.0: Classes
class Person {
    [string]$Name
    [int]$Age
    Person([string]$n, [int]$a) { $this.Name = $n; $this.Age = $a }
}

# PowerShell 7.0+: Modern syntax
$person = [Person]::new("Alice", 30)
$name = $person?.Name ?? "Unknown"  # null-conditional, null-coalescing
$result = $x -gt 0 ? "positive" : "non-positive"  # ternary

# PowerShell: Object pipeline (unique feature)
Get-ChildItem |
  Where-Object { $_.Extension -eq ".md" } |
  ForEach-Object { $_.FullName }
```

## 主要な設計原則
```
Shell (bash/zsh):
1. "Text is the universal interface" — pipes connect everything
2. "Do one thing well" — small tools, compose via pipes
3. "Everything is a file" — Unix philosophy
4. "Backward compatible" — 40-year-old scripts still work

PowerShell:
1. "Objects, not text" — pipeline passes .NET objects
2. "Consistent" — Verb-Noun naming (Get-Process, Set-Location)
3. "Extensible" — modules, providers, remoting
4. "Cross-platform" — PowerShell 7+ runs everywhere
```

## エコシステムの成長
```
1971: Thompson shell — first Unix shell
1977: Bourne shell (sh) — scripting begins
1989: bash — GNU shell, becomes Linux default
1990: zsh — power user shell
2005: fish — user-friendly shell
2006: PowerShell 1.0 — Microsoft's object shell
2010: oh-my-zsh — zsh framework (themes, plugins)
2018: PowerShell 6.0 — cross-platform
2019: nushell — structured data shell
2020: PowerShell 7.0 — modern syntax
2025: bash remains the default on Linux/macOS
       PowerShell dominates Windows administration
       zsh is macOS default; fish gaining popularity
```
