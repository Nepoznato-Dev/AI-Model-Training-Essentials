<!-- 
This file was automatically translated from English to Japanese.
Source: tool_usage.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tool Usage

## Git — Version Control

Git は分散型バージョン管理システムです。各開発者はリポジトリの完全なコピーと履歴をローカルマシンに持っています。

### Core workflow

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

### Branching

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### マージとリベース

```bash
# メインブランチにフィーチャーブランチをマージ
git checkout main
git merge feature/new-thing

# リベースは履歴を直線的に保つ
git checkout feature/new-thing
git rebase main
```

### プルリクエスト (PR) ワークフロー

1. `main` からフィーチャーブランチを作成する。
2. フィーチャーブランチでコミットを行う。
3. ブランチをプッシュする：`git push origin feature/new-thing`。
4. GitHub / GitLab でプルリクエストを開く。
5. コードレビューのフィードバックに対応し、追加コミットを行う。
6. 承認されたら PR をマージする。

### 変更の取り消し

```bash
git restore file.py            # ステージされていない変更を破棄
git restore --staged file.py   # ファイルをステージから外す
git revert <commit-sha>        # 以前のコミットを取り消す新しいコミットを作成
git reset --soft HEAD~1        # 最後のコミットを取り消し、変更はステージされたままにする
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

`package-lock.json` は正確なバージョンを記録します。ソースコントロールにコミットしてください。

### Cargo (Rust)

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

### Go modules (Go)

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

## コマンドライン基本

### ナビゲーション

```bash
pwd                             # 作業ディレクトリを表示
ls                              # ディレクトリ内容を一覧表示
ls -la                          # 隠しファイルを含む詳細一覧
cd /path/to/dir                 # ディレクトリを変更
cd ..                           # 1 つ上の階層へ移動
cd ~                            # ホームディレクトリへ移動
mkdir new_folder
rm file.txt                     # ファイルを削除
rm -r folder/                   # ディレクトリを再帰的に削除
cp src.txt dst.txt
mv old_name.txt new_name.txt
```

### テキスト処理

```bash
cat file.txt                    # ファイル内容を表示
less file.txt                   # ファイルをスクロールして閲覧
head -n 20 file.txt             # 最初の 20 行
tail -n 20 file.txt             # 最後の 20 行
tail -f log.txt                 # 増加するログファイルを追跡
grep "pattern" file.txt         # パターンを検索
grep -r "pattern" ./src/        # 再帰的に検索
grep -i "pattern" file.txt      # 大文字小文字を区別しない
```

### パイプとリダイレクト

```bash
command1 | command2             # command1 の出力を command2 へパイプ
ls -la | grep ".py"             # Python ファイルのみを一覧表示
cat file.txt | wc -l            # 行数をカウント
command > output.txt            # 標準出力をファイルへリダイレクト（上書き）
command >> output.txt           # 標準出力をファイルへ追加
command 2>&1                    # 標準エラーを標準出力にマージ
```

### ネットワークとファイル転送

```bash
curl https://example.com                     # URL を取得
curl -o file.zip https://example.com/f.zip   # ファイルへダウンロード
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # wget でダウンロード
```

### パーミッション

```bash
chmod +x script.sh              # 実行可能にする
chmod 644 file.txt              # オーナーは読み書き、グループ/その他は読み取り
chown user:group file.txt       # オーナーとグループを変更
```

### プロセス管理

```bash
ps aux                          # 実行中のプロセスを一覧表示
kill <PID>                      # プロセスに SIGTERM を送信
kill -9 <PID>                   # 強制終了
top / htop                      # インタラクティブなプロセスモニター
```

---

## エディタと IDE

### VS Code

VS Code は軽量なクロスプラットフォームコードエディタで、豊富な拡張機能エコシステムを持ちます。

- フォルダを開く：`File > Open Folder` またはターミナルで `code .`
- コマンドパレット：`Ctrl+Shift+P`（macOS: `Cmd+Shift+P`）
- 統合ターミナル：`Ctrl+``（バッククォート）`
- マルチカーソル：`Alt+Click` で追加カーソルを配置
- 定義へ移動：`F12`
- シンボルの名前変更：`F2`
- ドキュメントのフォーマット：`Shift+Alt+F`
- 拡張機能：拡張機能パネル（`Ctrl+Shift+X`）から言語サポート（Python、Rust、Go など）、リンター、フォーマッターをインストール
- `settings.json`（ユーザーまたはワークスペース）でエディタの動作を制御
- `launch.json` でデバッガーを設定

### JetBrains IDEs (IntelliJ IDEA、PyCharm、WebStorm、CLion、GoLand)

- スマートコード補完とリファクタリングが主要機能です。
- 実行/デバッグ設定でワンクリックでプログラムを実行・デバッグできます。
- VCS メニューに Git サポートが組み込まれています。
- `Shift+Shift` で「Search Everywhere」ダイアログを開きます。
- `Ctrl+Alt+L`（macOS: `Cmd+Option+L`）でコードをフォーマットします。
- プラグインで言語サポートやツールを追加できます。

### ターミナルのヒント

- タブ補完を使ってファイル名やコマンドを素早く入力できます。
- `Ctrl+R` でコマンド履歴をインタラクティブに検索できます。
- `alias ll='ls -la'` のようにショートカットを作成 — `~/.bashrc` または `~/.zshrc` に追加します。
- `tmux` や `screen` を使って、リモートサーバーから切断された場合でもセッションを維持できます。
- `man <command>` で組み込みコマンドのマニュアルページを表示できます。

---

## Docker

Docker はアプリケーションとその依存関係をポータブルなコンテナにパッケージ化します。

### 主要概念

- **イメージ**: `Dockerfile` から構築される読み取り専用テンプレート
- **コンテナ**: イメージの実行中インスタンス
- **レジストリ**: イメージの保存・配信サービス（Docker Hub、GHCR）
- **ボリューム**: コンテナより長く存続する永続ストレージ

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

### Dockerfile example

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

Docker Compose manages multi-container applications と a `docker-compose.yml` file.

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
