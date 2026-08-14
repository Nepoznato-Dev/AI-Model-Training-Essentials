---
# Metadata
title: "Shell & PowerShell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Shell and PowerShell ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [shell, powershell, bash, ecosystem, tooling, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Shell と PowerShell — エコシステムとツールのガイド
このガイドでは、シェル スクリプト (Bash/Zsh) と PowerShell に必要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## シェルの実装
|シェル |プラットフォーム |メモ |
|------|----------|------|
| **バッシュ** | Unix/Linux/macOS |最も広く使用されている |
| **ズシュ** | macOSのデフォルト |強化された Bash |
| **魚** |クロスプラットフォーム |ユーザーフレンドリー |
| **ダッシュ** | Debian/Ubuntu |高速、POSIX 準拠 |
| **ksh** |ユニックス |コーンシェル
| **PowerShell** |クロスプラットフォーム |オブジェクト指向 (pwsh) |
| **ヌシェル** |クロスプラットフォーム |構造化データシェル |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## パッケージ マネージャー (シェル ツール)
|ツール |目的 |
|-----|----------|
| **自作** | macOS/Linux パッケージ マネージャー |
| **apt / yum / dnf** | Linux パッケージ マネージャー |
| **パッケージ** | FreeBSD パッケージマネージャー |
| **スクープ** | Windows CLI インストーラー |
| **チョコレート** | Windows パッケージ マネージャー |
| **ウィンゲット** | Windows パッケージ マネージャー |
```bash
# Homebrew
brew install jq ripgrep fd bat    # install tools
brew upgrade                      # upgrade all

# apt (Debian/Ubuntu)
sudo apt update && sudo apt install -y jq curl

# PowerShell
Install-Module -Name PSReadLine -Force
```

---

## 必須の CLI ツール
|ツール |目的 |
|-----|----------|
| **jq** | JSON処理 |
| **yq** | YAML処理 |
| **ripgrep (rg)** |高速 grep |
| **fd** |素早い検索 |
| **コウモリ** |強化された猫 |
| **エクサ / エザ** |強化されたls |
| **fzf** |ファジーファインダー |
| **hトップ** |プロセスビューア |
| **tmux** |ターミナルマルチプレクサ |
| **カール / wget** | HTTP リクエスト |
| **sed / awk** |テキスト処理 |
| **xargs** |入力からコマンドを構築する |
| **作る** |タスクランナー |
| **エントリー** |ファイル変更時にコマンドを実行する |
| **平行** |並列実行 |
| **シェルチェック** |シェルスクリプトリンター |
---

## シェルのフレームワークと機能強化
|ツール |目的 |
|-----|----------|
| **オーマイザッシュ** | Zsh フレームワーク (テーマ、プラグイン) |
| **プレズト** | Zsh フレームワーク (高速) |
| **スターシップ** |クロスシェルプロンプト |
| **zsh-autosuggestions** |自動提案 |
| **zsh-syntax-highlighting** |構文の強調表示 |
| **バッシュイット** | Bash フレームワーク |
| **アトゥイン** |シェル履歴 (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## PowerShell モジュール
|モジュール |目的 |
|--------|--------|
| **PSReadLine** |強化されたコマンドライン編集 |
| **ペスター** |テストフレームワーク |
| **PSScriptAnalyzer** |リンティング |
| **ポッシュギット** | Git の統合 |
| **ターミナルアイコン** |ファイルアイコン |
| **PSWindowsUpdate** | Windows アップデート |
| **アズ** | Azure管理 |
| **AWSPowerShell** | AWS管理 |
| **SQLサーバー** | SQL Server 管理 |
| **ポデ** |ウェブフレームワーク |
| **ユニバーサル ダッシュボード** |ウェブダッシュボード |
```powershell
# Install modules
Install-Module -Name PSReadLine -Force
Install-Module -Name Pester -Force
Install-Module -Name PSScriptAnalyzer -Force
Install-Module -Name Az -Force

# Import module
Import-Module Az
```

---

## テスト
|フレームワーク |シェル |目的 |
|----------|----------|----------|
| **コウモリ** |バッシュ | Bash 自動テスト |
| **シュユニット2** |シェル | xUnit スタイルのテスト |
| **ペスター** |パワーシェル |テストとモック |
| **assert.sh** |バッシュ |アサーション ライブラリ |
```bash
# Bats example
#!/usr/bin/env bats

@test "addition" {
  result=$((2 + 3))
  [ "$result" -eq 5 ]
}

@test "file exists" {
  [ -f "/etc/passwd" ]
}

@test "command succeeds" {
  run echo "hello"
  [ "$status" -eq 0 ]
  [ "$output" = "hello" ]
}
```

```powershell
# Pester example
Describe "UserService" {
    It "finds user by id" {
        $user = Get-User -Id 1
        $user.Name | Should -Be "Alice"
    }
    
    It "throws when user not found" {
        { Get-User -Id 999 } | Should -Throw
    }
}
```

---

## コードの品質
|ツール |シェル |目的 |
|------|-------|-----------|
| **シェルチェック** |バッシュ/Zsh |リンティングと静的分析 |
| **シュフムト** |バッシュ/Zsh |コードのフォーマット |
| **PSScriptAnalyzer** |パワーシェル |リンティング |
| **PSScript 設定** |パワーシェル |フォーマット |
```bash
# ShellCheck
shellcheck script.sh        # lint
shellcheck -s bash script.sh  # specify shell

# shfmt
shfmt -w script.sh          # format
shfmt -d script.sh          # diff (check only)
```

```powershell
# PSScriptAnalyzer
Invoke-ScriptAnalyzer -Path .\script.ps1
Invoke-ScriptAnalyzer -Path .\script.ps1 -Fix  # auto-fix
```

---

## 主要なライブラリとパターン
### バッシュ
|パターン |目的 |
|----------|----------|
| **set -euo パイプ失敗** |厳密モード |
| **トラップ** |信号処理 |
| **出典 / .** |インクルードファイル |
| **ゲトップ** |引数の解析 |
| **ヒアドキュメント** |複数行の文字列 |
| **プロセスの置換** | `<()`および`>()`|
| **配列** |インデックス付きと連想 |
```bash
#!/usr/bin/env bash
set -euo pipefail

# Functions
log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"; }

# Argument parsing
while getopts "hn:v" opt; do
  case $opt in
    h) echo "Usage: $0 [-h] [-n name] [-v]"; exit 0 ;;
    n) NAME="$OPTARG" ;;
    v) VERBOSE=true ;;
  esac
done

# Cleanup trap
cleanup() { rm -rf "$TMPDIR"; }
trap cleanup EXIT
```

### パワーシェル
|パターン |目的 |
|----------|----------|
| **コマンドレットバインド** |先進機能 |
| **パラメータ** |パラメータの属性 |
| **パイプライン** |オブジェクトパイプライン |
| **トライ/キャッチ** |エラー処理 |
| **クラス** | OOP |
```powershell
function Get-User {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$Id,
        
        [ValidateSet("json", "xml")]
        [string]$Format = "json"
    )
    
    try {
        $user = Invoke-RestMethod -Uri "https://api.example.com/users/$Id"
        return $user
    }
    catch {
        Write-Error "Failed to get user: $_"
    }
}
```

---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード** |シェル/PowerShell のサポート |
| **ネオビム** |ターミナルベース |
| **Windows ターミナル** |最新のターミナル (PowerShell) |
| **iTerm2** | macOSターミナル |
| **ワープ** | AI搭載端末 |
| **アラクリティ** | GPU アクセラレーション端末 |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **クロン** |スケジュールされたタスク (Unix) |
| **システム** |サービス管理 (Linux) |
| **タスク スケジューラ** | Windows のスケジュールされたタスク |
| **Docker エントリポイント** |コンテナスクリプト |
| **CI/CD パイプライン** | GitHub アクション、GitLab CI |
| **アンシブル** |構成管理 |
| **テラフォーム** |コードとしてのインフラストラクチャ |
---

＃＃ まとめ
シェル スクリプトのエコシステムは多様です。**Bash** は依然として普遍的な標準であり、**Zsh** は対話型使用の最新のデフォルトであり、**PowerShell** は Windows 管理の主流となっています。標準スタックは次のとおりです。スクリプト作成には **Bash/Zsh**、リンティングには **ShellCheck**、フォーマットには **shfmt**、テストには **Bats**、JSON には **jq**、検索には **ripgrep**、ターミナル多重化には **tmux** です。 PowerShell の場合: テストには **Pester**、lint には **PSScriptAnalyzer**、拡張編集には **PSReadLine**。シェル スクリプトは、自動化、CI/CD、システム管理、DevOps ワークフローに不可欠です。