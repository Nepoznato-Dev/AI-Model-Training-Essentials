<!--
---
# Metadata
title: "Tool Usage"
description: "Development tools and utilities"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [tool, usage, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# ツールの使用法
## Git — バージョン管理
Git は分散バージョン管理システムです。すべての開発者は、ローカル マシン上にリポジトリ履歴の完全なコピーを持っています。
### コアワークフロー
```bash
# Start a new repository
git init

# Clone an existing repository
git clone https://github.com/owner/repo.git

# Check status and recent history
git status
git log --oneline -10

# Stage changes
git add file.py            # stage a specific file
git add .                  # stage all changes in the working directory

# Commit
git commit -m "Short, imperative description of change"

# Push to a remote
git push origin main
```

### 分岐
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### マージとリベース
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### プル リクエスト (PR) ワークフロー
1.`main`から機能ブランチを作成します。
2. 機能ブランチにコミットを作成します。
3. ブランチ`git push origin feature/new-thing`をプッシュします。
4. GitHub / GitLab でプル リクエストを開きます。
5. 追加のコミットでコードレビューのフィードバックに対処します。
6. 承認されたら PR をマージします。
### 変更を元に戻す
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## パッケージマネージャー
### pip (Python)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

プロジェクトの依存関係を分離するために、常に仮想環境内で作業してください。
### npm (Node.js / JavaScript)
```bash
npm init -y                     # create package.json
npm install express             # install as a runtime dependency
npm install --save-dev jest     # install as a dev dependency
npm uninstall express
npm update
npm run test                    # run the "test" script from package.json
npm run build
npx create-react-app my-app     # run a package without installing globally
```

`package-lock.json` は正確なバージョンを記録します。それをソース管理にコミットします。
### 貨物 (錆び)
```bash
cargo new my_project            # new binary project
cargo new --lib my_lib          # new library project
cargo add serde --features derive
cargo build
cargo run
cargo test
cargo clippy                    # lint
cargo fmt                       # format
cargo update                    # update dependencies within constraints
```

### Go モジュール (Go)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apt (Debian / Ubuntu Linux)
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## コマンドラインの基本
### ナビゲーション
```bash
pwd                             # print working directory
ls                              # list directory contents
ls -la                          # detailed listing including hidden files
cd /path/to/dir                 # change directory
cd ..                           # go up one level
cd ~                            # go to home directory
mkdir new_folder
rm file.txt                     # remove a file
rm -r folder/                   # remove a directory recursively
cp src.txt dst.txt
mv old_name.txt new_name.txt
```

### テキスト処理
```bash
cat file.txt                    # print file contents
less file.txt                   # scroll through a file
head -n 20 file.txt             # first 20 lines
tail -n 20 file.txt             # last 20 lines
tail -f log.txt                 # follow a growing log file
grep "pattern" file.txt         # search for a pattern
grep -r "pattern" ./src/        # recursive search
grep -i "pattern" file.txt      # case-insensitive
```

### パイプとリダイレクト
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### ネットワークとファイル転送
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### 権限
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### プロセス管理
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## エディターと IDE
### VS コード
VS Code は、豊富な拡張機能エコシステムを備えた軽量のクロスプラットフォーム コード エディターです。
- ターミナルでフォルダー`File > Open Folder`または`code .`を開きます。
- コマンドパレット:`Ctrl+Shift+P`(macOS: `Cmd+Shift+P`)。
- 統合ターミナル:`Ctrl+`` (backtick)` 。
- マルチカーソル:`Alt+Click`追加のカーソルを配置します。
- 定義に移動します:`F12`。
- シンボルの名前を`F2`に変更します。
- ドキュメントの形式:`Shift+Alt+F`。
- 拡張機能: 拡張機能パネル (`Ctrl+Shift+X`) から言語サポート (Python、Rust、Go など)、リンター、およびフォーマッタをインストールします。
-`settings.json`(ユーザーまたはワークスペース) はエディターの動作を制御します。
-`launch.json`はデバッガを設定します。
### JetBrains IDE (IntelliJ IDEA、PyCharm、WebStorm、CLion、GoLand)
- スマートなコード補完とリファクタリングはコア機能です。
- 実行/デバッグ構成を使用すると、ワンクリックでプログラムを起動してデバッグできます。
- VCS メニューに Git サポートが組み込まれています。
-`Shift+Shift`は、どこでも検索ダイアログを開きます。
-`Ctrl+Alt+L`(macOS: `Cmd+Option+L`) コードを再フォーマットします。
- プラグインは言語サポートを拡張し、ツールを追加します。
### ターミナルのヒント
- タブ補完を使用して、ファイル名とコマンドをすばやく終了します。
-`Ctrl+R`を押してコマンド履歴を対話的に検索します。
-`alias ll='ls -la'`はショートカットを作成します。それを`~/.bashrc`または`~/.zshrc`に追加します。
- リモート サーバーから切断されたときにセッションを維持するには、`tmux` または`screen`を使用します。
-`man <command>`は、組み込みコマンドのマニュアル ページを表示します。
---

## ドッカー
Docker は、アプリケーションとその依存関係をポータブル コンテナーにパッケージ化します。
### 中心となる概念
- **画像**:`Dockerfile`から構築された読み取り専用テンプレート。
- **コンテナ**: イメージの実行中のインスタンス。
- **レジストリ**: イメージのストレージおよび配布サービス (Docker Hub、GHCR)。
- **ボリューム**: コンテナーよりも長く存続する永続ストレージ。
### 一般的なコマンド
```bash
# Images
docker pull ubuntu:22.04
docker images
docker rmi ubuntu:22.04

# Containers
docker run -it ubuntu:22.04 bash        # interactive shell
docker run -d -p 8080:80 nginx          # detached, port mapping
docker ps                               # running containers
docker ps -a                            # all containers
docker stop <container_id>
docker rm <container_id>
docker logs <container_id>
docker exec -it <container_id> bash     # open shell in running container

# Building
docker build -t myapp:1.0 .
docker push myrepo/myapp:1.0
```

### Dockerfile の例
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose
Docker Compose は、`docker-compose.yml` ファイルを使用してマルチコンテナー アプリケーションを管理します。
```yaml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://db:5432/mydb
    depends_on:
      - db
  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

```bash
docker compose up -d       # start all services in the background
docker compose down        # stop and remove containers
docker compose logs -f     # stream logs
docker compose build       # rebuild images
```
