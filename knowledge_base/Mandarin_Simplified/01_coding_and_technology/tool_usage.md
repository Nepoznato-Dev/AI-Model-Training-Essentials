---
# Metadata
title: "Tool Usage"
description: "Development tools and utilities"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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
Git 是一个分布式版本控制系统。每个开发人员在其本地计算机上都有存储库历史记录的完整副本。
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

### 合并和变基
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### 拉取请求 (PR) 工作流程
1. 从`main`创建功能分支。
2. 在功能分支上进行提交。
3. 推送分支：`git push origin feature/new-thing`。
4. 在 GitHub / GitLab 上打开拉取请求。
5. 通过额外提交解决代码审查反馈。
6. 获得批准后合并 PR。
### 撤消更改
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## 包管理器
### 点（Python）
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

始终在虚拟环境中工作，以保持项目依赖关系隔离。
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

`package-lock.json` 记录准确版本；将其提交给源代码管理。
### 货物（生锈）
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

### Go 模块 (Go)
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

## 命令行基础知识
＃＃＃ 导航
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

### 文本处理
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

### 网络和文件传输
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### 权限
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

## 编辑器和 IDE
### VS 代码
VS Code 是一款轻量级、跨平台的代码编辑器，具有丰富的扩展生态系统。
- 在终端中打开文件夹：`File > Open Folder` 或 `code .`。
- 命令调色板：`Ctrl+Shift+P`（macOS：`Cmd+Shift+P`）。
- 集成终端：`Ctrl+`` (backtick)`。
- 多光标：`Alt+Click` 用于放置附加光标。
- 转到定义：`F12`。
- 重命名符号：`F2`。
- 格式文档：`Shift+Alt+F`。
- 扩展：从扩展面板 (`Ctrl+Shift+X`) 安装语言支持（Python、Rust、Go 等）、linter 和格式化程序。
- `settings.json`（用户或工作区）控制编辑器行为。
-`launch.json`配置调试器。
### JetBrains IDE（IntelliJ IDEA、PyCharm、WebStorm、CLion、GoLand）
- 智能代码补全和重构是核心功能。
- 运行/调试配置让您一键启动和调试程序。
- VCS 菜单中内置 Git 支持。
-`Shift+Shift`打开“搜索无处不在”对话框。
- `Ctrl+Alt+L`（macOS：`Cmd+Option+L`）重新格式化代码。
- 插件扩展了语言支持并添加了工具。
### 终端提示
- 使用制表符完成快速完成文件名和命令。
- 按`Ctrl+R`以交互方式搜索命令历史记录。
-`alias ll='ls -la'`创建快捷方式 - 将其添加到`~/.bashrc`或`~/.zshrc`。
- 使用`tmux`或`screen`在与远程服务器断开连接时保持会话处于活动状态。
-`man <command>`显示任何内置命令的手册页。
---

## 码头工人
Docker 将应用程序及其依赖项打包到可移植容器中。
### 核心概念
- **图像**：从`Dockerfile`构建的只读模板。
- **容器**：图像的运行实例。
- **Registry**：镜像的存储和分发服务（Docker Hub、GHCR）。
- **卷**：比容器寿命更长的持久存储。
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

### Dockerfile 示例
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker 组合
Docker Compose 使用`docker-compose.yml`文件管理多容器应用程序。
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
