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
# 工具使用
## Git — 版本控制
Git 是分散式版本控制系統。每個開發人員在其本機電腦上都有儲存庫歷史記錄的完整副本。
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

### 分支
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### 合併和變基
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### 拉取請求 (PR) 工作流程
1. 從`main`建立功能分支。
2. 在功能分支上進行提交。
3. 推送分支：`git push origin feature/new-thing`。
4. 在 GitHub / GitLab 上開啟拉取請求。
5. 透過額外提交解決程式碼審查回饋。
6. 獲得批准後合併 PR。
### 撤銷更改
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## 套件管理器
### 點（Python）
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

始終在虛擬環境中工作，以保持專案依賴隔離。
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

`package-lock.json` 記錄準確版本；將其提交給原始程式碼管理。
### 貨物（生鏽）
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

### Go 模組 (Go)
```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apt（Debian / Ubuntu Linux）
```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## 命令列基礎知識
＃＃＃ 導航
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

### 管道和重定向
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### 網路和檔案傳輸
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### 權限
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### 流程管理
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## 編輯器和 IDE
### VS 程式碼
VS Code 是一款輕量、跨平台的程式碼編輯器，具有豐富的擴展生態系統。
- 在終端機中開啟資料夾：`File > Open Folder` 或 `code .`。
- 命令調色板：`Ctrl+Shift+P`（macOS：`Cmd+Shift+P`）。
- 整合終端：`Ctrl+`` (backtick)`。
- 多重遊標：`Alt+Click` 用於放置附加遊標。
- 前往定義：`F12`。
- 重新命名符號：`F2`。
- 格式文件：`Shift+Alt+F`。
- 擴充：從擴充面板 (`Ctrl+Shift+X`) 安裝語言支援（Python、Rust、Go 等）、linter 和格式化程式。
- `settings.json`（使用者或工作區）控制編輯器行為。
-`launch.json`配置偵錯器。
### JetBrains IDE（IntelliJ IDEA、PyCharm、WebStorm、CLion、GoLand）
- 智慧型程式碼補全和重構是核心功能。
- 運行/調試配置讓您一鍵啟動和調試程序。
- VCS 選單內建 Git 支援。
-`Shift+Shift`開啟「搜尋無所不在」對話方塊。
- `Ctrl+Alt+L`（macOS：`Cmd+Option+L`）重新格式化程式碼。
- 外掛擴展了語言支援並添加了工具。
### 終端機提示
- 使用製表符完成快速完成檔案名稱和命令。
- 按`Ctrl+R`以互動方式搜尋指令歷史記錄。
-`alias ll='ls -la'`建立捷徑 - 將其新增至`~/.bashrc`或`~/.zshrc`。
- 使用`tmux`或`screen`在與遠端伺服器斷開連線時保持會話處於活動狀態。
-`man <command>`顯示任何內建指令的手冊頁。
---

## 碼頭工人
Docker 將應用程式及其相依性打包到可移植容器中。
### 核心概念
- **圖像**：從`Dockerfile`建構的唯讀模板。
- **容器**：映像檔的運作實例。
- **Registry**：鏡像的儲存和分發服務（Docker Hub、GHCR）。
- **卷**：比容器壽命更長的持久存儲。
### 常用指令
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

### Docker 組合
Docker Compose 使用`docker-compose.yml`檔案管理多容器應用程式。
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
