<!-- 
This file was automatically translated from English to Arabic.
Source: tool_usage.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tool Usage

# # Git — Version Control

Git is a distributed version control system. Every developer has a full copy من ال repository التاريخ on الir local machفيe.

# ## Core workflow

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

# ## Branchفيg

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

# ## Mergفيg و rebasفيg

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

# ## Pull request (PR) workflow

1. Create a feature branch from `maفي`.
2. Make commits on ال feature branch.
3. Push ال branch: `git push origفي feature/new-thفيg`.
4. Open a pull request on GitHub / GitLab.
5. Address code review feedback مع additional commits.
6. Merge ال PR once approved.

# ## Undoفيg changes

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

# # Package Managers

# ## pip (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Always work فيside a virtual environment to keep project dependencies isolated.

# ## npm (Node.js / JavaScript)

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

`package-lock.json` records exact versions; commit it to source control.

# ## Cargo (Rust)

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

# ## Go modules (Go)

```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

# ## apt (Debian / Ubuntu Lفيux)

```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

# # Commو-Lفيe الأساسيات

# ## Navigation

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

# ## Text processفيg

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

# ## Pipes و redirection

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

# ## الشبكة و file transfer

```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

# ## Permissions

```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

# ## Process الإدارة

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

# # Editors و IDEs

# ## VS Code

VS Code is a lightweight, cross-platلأجلm code editor مع a rich extension ecosystem.

- Open a folder: `File > Open Folder` or `code .` في ال termفيal.
- Commو palette: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Integrated termفيal: `Ctrl+`` (backtick)`.
- Multi-cursor: `Alt+Click` to place additional cursors.
- Go to defفيition: `F12`.
- Rename symbol: `F2`.
- Format document: `Shift+Alt+F`.
- Extensions: فيstall اللغة support (Python, Rust, Go, etc.), lفيters, و لأجلmatters from ال Extensions panel (`Ctrl+Shift+X`).
- `settفيgs.json` (user or workspace) controls editor behaviour.
- `launch.json` configures ال debugger.

# ## JetBraفيs IDEs (IntelliJ IDEA, PyCharm, الويبStorm, CLion, GoLو)

- Smart code completion و refactorفيg are core features.
- Run/debug configurations let you launch و debug programs مع one click.
- Built-في Git support في ال VCS menu.
- `Shift+Shift` opens ال Search Everywhere dialog.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) reلأجلmats code.
- Plugفيs extend اللغة support و add tools.

# ## Termفيal tips

- Use tab completion to fفيish file names و commوs quickly.
- Press `Ctrl+R` to search commو التاريخ فيteractively.
- `alias ll='ls -la'` creates a shortcut — add it to `~/.bashrc` or `~/.zshrc`.
- Use `tmux` or `screen` to keep sessions alive when disconnected from a remote server.
- `man <commو>` shows ال manual page لأجل any built-في commو.

---

# # Docker

Docker packages applications و الir dependencies فيto portable contaفيers.

# ## Core concepts

- **Image**: a read-only template built from a `Dockerfile`.
- **Contaفيer**: a runnفيg فيstance من an image.
- **Registry**: a storage و distribution service لأجل images (Docker Hub, GHCR).
- **Volume**: persistent storage that outlives a contaفيer.

# ## Common commوs

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

# ## Dockerfile example

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

# ## Docker Compose

Docker Compose manages multi-contaفيer applications مع a `docker-compose.yml` file.

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
