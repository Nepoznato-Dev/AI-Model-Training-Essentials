# 工具使用

## Git — 版本控制

Git 是一种分布式版本控制系统。每位开发者的本地机器上都保存着仓库历史的完整副本。

### 核心工作流

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

### 合并与变基

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Pull request（PR）工作流

1. 从 `main` 创建一个功能分支。
2. 在该功能分支上提交代码。
3. 推送该分支：`git push origin feature/new-thing`。
4. 在 GitHub / GitLab 上创建一个 pull request。
5. 根据代码评审反馈继续提交修改。
6. 获得批准后合并 PR。

### 撤销更改

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

始终在虚拟环境中工作，以确保项目依赖彼此隔离。

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

`package-lock.json` 会记录精确版本；请将其提交到版本控制中。

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

## 命令行基础

### 导航

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

### 管道与重定向

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### 网络与文件传输

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

### 进程管理

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## 编辑器与 IDE

### VS Code

VS Code 是一款轻量级、跨平台的代码编辑器，拥有丰富的扩展生态。

- 打开文件夹：`File > Open Folder`，或在终端中执行 `code .`。
- 命令面板：`Ctrl+Shift+P`（macOS：`Cmd+Shift+P`）。
- 集成终端：`Ctrl+``（backtick）。
- 多光标：`Alt+Click` 可放置额外光标。
- 跳转到定义：`F12`。
- 重命名符号：`F2`。
- 格式化文档：`Shift+Alt+F`。
- 扩展：可在 Extensions 面板（`Ctrl+Shift+X`）中安装语言支持（Python、Rust、Go 等）、lint 工具和格式化工具。
- `settings.json`（用户级或工作区级）用于控制编辑器行为。
- `launch.json` 用于配置调试器。

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- 智能代码补全和重构是其核心特性。
- 运行/调试配置让你可以一键启动并调试程序。
- VCS 菜单内置 Git 支持。
- `Shift+Shift` 可打开 Search Everywhere 对话框。
- `Ctrl+Alt+L`（macOS：`Cmd+Option+L`）可重新格式化代码。
- 插件可扩展语言支持并添加工具能力。

### 终端技巧

- 使用 Tab 补全可快速补齐文件名和命令。
- 按 `Ctrl+R` 可交互式搜索命令历史。
- `alias ll='ls -la'` 可以创建快捷方式——将其加入 `~/.bashrc` 或 `~/.zshrc`。
- 使用 `tmux` 或 `screen`，可在与远程服务器断开连接后保持会话存活。
- `man <command>` 会显示任意内置命令的手册页。

---

## Docker

Docker 会把应用及其依赖打包进可移植的容器中。

### 核心概念

- **Image**：由 `Dockerfile` 构建出的只读模板。
- **Container**：镜像的一个运行实例。
- **Registry**：用于存储和分发镜像的服务（Docker Hub、GHCR）。
- **Volume**：独立于容器生命周期之外的持久化存储。

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

### Docker Compose

Docker Compose 使用 `docker-compose.yml` 文件来管理多容器应用。

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
