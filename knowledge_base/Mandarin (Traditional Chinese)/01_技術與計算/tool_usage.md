# 工具使用

## Git — 版本控制

Git 是一種分散式版本控制系統。每位開發者的本地機器上都儲存著倉庫歷史的完整副本。

### 核心工作流程

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

### 分支管理

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### 合併與變基

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Pull request（PR）工作流程

1. 從 `main` 建立一個功能分支。
2. 在該功能分支上提交程式碼。
3. 推送該分支：`git push origin feature/new-thing`。
4. 在 GitHub / GitLab 上建立一個 pull request。
5. 根據程式碼評審反饋繼續提交修改。
6. 獲得批准後合併 PR。

### 撤銷更改

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Package Managers

### pip (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

始終在虛擬環境中工作，以確保專案依賴彼此隔離。

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

`package-lock.json` 會記錄精確版本；請將其提交到版本控制中。

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

## 命令列基礎

### 導航

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

### 文字處理

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

### 管道與重定向

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### 網路與檔案傳輸

```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Permissions

```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### 程序管理

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## 編輯器與 IDE

### VS Code

VS Code 是一款輕量級、跨平台的程式碼編輯器，擁有豐富的擴充套件生態。

- 開啟資料夾：`File > Open Folder`，或在終端中執行 `code .`。
- 命令面板：`Ctrl+Shift+P`（macOS：`Cmd+Shift+P`）。
- 整合終端：`Ctrl+``（backtick）。
- 多游標：`Alt+Click` 可放置額外游標。
- 跳轉到定義：`F12`。
- 重新命名符號：`F2`。
- 格式化文件：`Shift+Alt+F`。
- 擴充套件：可在 Extensions 面板（`Ctrl+Shift+X`）中安裝語言支援（Python、Rust、Go 等）、lint 工具和格式化工具。
- `settings.json`（使用者級或工作區級）用於控制編輯器行為。
- `launch.json` 用於設定偵錯程式。

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- 智慧程式碼補全和重構是其核心特性。
- 執行/除錯設定讓你可以一鍵啟動並除錯程式。
- VCS 選單內建 Git 支援。
- `Shift+Shift` 可開啟 Search Everywhere 對話方塊。
- `Ctrl+Alt+L`（macOS：`Cmd+Option+L`）可重新格式化程式碼。
- 外掛可擴充套件語言支援並新增工具能力。

### 終端技巧

- 使用 Tab 補全可快速補齊檔名和命令。
- 按 `Ctrl+R` 可互動式搜尋命令歷史。
- `alias ll='ls -la'` 可以建立快捷方式——將其加入 `~/.bashrc` 或 `~/.zshrc`。
- 使用 `tmux` 或 `screen`，可在與遠端伺服器斷開連線後保持會話存活。
- `man <command>` 會顯示任意內建命令的手冊頁。

---

## Docker

Docker 會把應用及其依賴打包進可移植的容器中。

### 核心概念

- **Image**：由 `Dockerfile` 構建出的只讀模板。
- **Container**：映象的一個執行例項。
- **Registry**：用於儲存和分發映象的服務（Docker Hub、GHCR）。
- **Volume**：獨立於容器生命週期之外的持久化儲存。

### 常用命令

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

### Dockerfile 範例

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

Docker Compose 使用 `docker-compose.yml` 檔案來管理多容器應用。

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
