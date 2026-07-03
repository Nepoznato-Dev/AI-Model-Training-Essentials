<!-- 
This file was automatically translated from English to Japanese.
Source: git_commands.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Gitコマンド クイックリファレンス

バージョン管理のための基本的な Git コマンド。

---

## セットアップと設定

```bash
# ユーザー情報を設定
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 設定を表示
git config --list
git config user.name

# デフォルトブランチ名を設定
git config --global init.defaultBranch main
```

---

## リポジトリの初期化

```bash
# 新しいリポジトリを初期化
git init

# 既存のリポジトリをクローン
git clone <url>
git clone <url> folder-name

# 特定のブランチをクローン
git clone -b branch-name <url>
```

---

## 基本的なワークフロー

```bash
# 状態を確認
git status

# 変更を表示
git diff
git diff --staged

# ファイルをステージに追加
git add file.txt          # 特定のファイル
git add .                 # すべてのファイル
git add *.py              # パターンに一致

# 変更をコミット
git commit -m "Commit message"
git commit -am "Message"  # 追跡済みファイルをステージしてコミット

# コミット履歴を表示
git log
git log --oneline
git log --graph --oneline --all
```

---

## ブランチ操作

```bash
# ブランチ一覧を表示
git branch                # ローカルブランチ
git branch -a             # すべてのブランチ
git branch -r             # リモートブランチ

# ブランチを作成
git branch branch-name
git checkout -b branch-name   # 作成して切り替え

# ブランチを切り替え
git checkout branch-name
git switch branch-name        # 新しい構文

# 現在のブランチ名を変更
git branch -m new-name

# ブランチを削除
git branch -d branch-name     # 安全な削除（マージ済み）
git branch -D branch-name     # 強制削除

# ブランチをマージ
git merge branch-name

# ブランチをリベース
git rebase main
```

---

## リモート操作

```bash
# リモートを表示
git remote -v

# リモートを追加
git remote add origin <url>

# リモートから取得
git fetch origin
git fetch --all

# 変更をプル（fetch + merge）
git pull origin main
git pull --rebase origin main

# 変更をプッシュ
git push origin main
git push -u origin main     # 上流ブランチを設定
git push --force            # 強制プッシュ（注意して使用）
git push --force-with-lease # より安全な強制プッシュ

# タグをプッシュ
git push --tags
```

---

## 変更の取り消し

```bash
# ファイルのステージを外す（変更は保持）
git reset HEAD file.txt
git restore --staged file.txt

# 作業中の変更を破棄
git checkout -- file.txt
git restore file.txt

# 直前のコミットを修正
git commit --amend -m "New message"
git commit --amend --no-edit

# コミットを取り消す（共有リポジトリ向けに安全）
git revert commit-hash

# 以前のコミットにリセット
git reset --soft HEAD~1     # 変更をステージ済みのまま保持
git reset --mixed HEAD~1    # 変更を未ステージのまま保持（既定）
git reset --hard HEAD~1     # すべての変更を破棄（危険）
```

---

## スタッシュ

```bash
# 作業中の内容を保存
git stash
git stash save "message"

# スタッシュ一覧を表示
git stash list

# スタッシュを適用
git stash apply             # 最新のもの
git stash apply stash@{1}   # 特定のスタッシュ

# 適用して削除
git stash pop

# スタッシュを削除
git stash drop stash@{1}

# すべてのスタッシュを消去
git stash clear
```

---

## タグ

```bash
# タグ一覧を表示
git tag
git tag -l "v1.*"

# タグを作成
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # 注釈付きタグ

# タグをチェックアウト
git checkout v1.0.0

# タグを削除
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## 表示と検索

```bash
# コミットの詳細を表示
git show commit-hash
git show --stat commit-hash

# blame（誰が何を変更したか）
git blame file.txt

# コミットを検索
git log --grep="keyword"
git log --author="name"

# 履歴内のコードを検索
git log -S"function_name"

# 特定のコミット時点のファイルを表示
git show commit-hash:file.txt
```

---

## 高度な操作

```bash
# コミットをチェリーピック
git cherry-pick commit-hash

# 対話的リベース
git rebase -i HEAD~5

# コミットを squash（リベース中）
# エディタで 'pick' を 'squash' または 's' に変更

# パッチを作成
git format-patch -1 commit-hash

# パッチを適用
git apply patch-file.patch
git am patch-file.patch

# サブモジュール
git submodule add <url> path
git submodule update --init --recursive
```

---

## クリーンアップ

```bash
# 未追跡ファイルを削除（試行実行）
git clean -n
git clean -f                # 実際に削除

# 未追跡ディレクトリを削除
git clean -fd

# 削除済みリモートブランチを整理
git fetch --prune
git remote prune origin
```

---

## よくあるワークフロー

### 新機能の開始
```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... 作業 ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# プラットフォームで PR/MR を作成
```

### メインとの同期
```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# 競合があれば解決
git push --force-with-lease
```

### ホットフィックスのワークフロー
```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... 修正 ...
git commit -am "Fix critical bug"
git checkout main
git merge hotfix/urgent-fix
git push
git tag v1.0.1
git push --tags
```

---

## .gitignore パターン

```gitignore
# 特定のファイルを無視
filename.txt

# すべての .log ファイルを無視
*.log

# ディレクトリを無視
node_modules/
__pycache__/

# 例外として含める
!important.log

# コメント
# これはコメントです
```

---

## キーボードショートカット（Git Bash）

| Shortcut | Action |
|----------|--------|
| `Ctrl+R` | 履歴の逆検索 |
| `Tab` | 自動補完 |
| `Ctrl+C` | コマンドを中止 |
| `Ctrl+Z` | プロセスを一時停止 |
| `fg` | 一時停止したプロセスを再開 |

---

## ベストプラクティス

✅ **Do:**
- わかりやすく具体的なコミットメッセージを書く
- 小まめに、論理的な単位でコミットする
- 機能や修正ごとにブランチを使う
- 作業前に pull する
- `git status` を頻繁に確認する

❌ **Don't:**
- 機密データ（API キー、パスワード）をコミットしない
- 共有ブランチに force push しない
- 大きなバイナリファイルをコミットしない
- マージ競合を無視しない
- main/master で直接作業しない

---

## コミットメッセージ規約

```
type(scope): subject

body (optional)

footer (optional)
```

**種類:**
- `feat`: 新機能
- `fix`: バグ修正
- `docs`: ドキュメント
- `style`: 書式のみの変更
- `refactor`: コードの再構成
- `test`: テスト
- `chore`: 保守作業

**例:**
```
feat(auth): add password reset functionality

メールによるパスワードリセットをトークンベースの
検証で実装する。トークンは 24 時間で期限切れになる。

Closes #123
```

---

*最終更新: 2025年6月 | Git 2.x*
