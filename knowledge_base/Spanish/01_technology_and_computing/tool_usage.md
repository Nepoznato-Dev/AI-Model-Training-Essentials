<!-- 
This file was automatically translated from English to Spanish.
Source: tool_usage.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tool Usage

# # Git — Version Control

Git is a distributed version control system. Every developer has a full copy de el/la repository historia on el/lair local machene.

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

# ## Brancheng

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

# ## Mergeng y rebaseng

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

# ## Pull request (PR) workflow

1. Create a feature branch from `maen`.
2. Make commits on el/la feature branch.
3. Push el/la branch: `git push origen feature/new-theng`.
4. Open a pull request on GitHub / GitLab.
5. Address code review feedback con additional commits.
6. Merge el/la PR once approved.

# ## Undoeng changes

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

Always work enside a virtual environment to keep project dependencies isolated.

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

# ## apt (Debian / Ubuntu Lenux)

```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

# # Commy-Lene Conceptos básicos

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

# ## Text processeng

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

# ## Pipes y redirection

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

# ## Red y file transfer

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

# ## Process gestión

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

# # Editors y IDEs

# ## VS Code

VS Code is a lightweight, cross-platparam code editor con a rich extension ecosystem.

- Open a folder: `File > Open Folder` or `code .` en el/la termenal.
- Commy palette: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Integrated termenal: `Ctrl+`` (backtick)`.
- Multi-cursor: `Alt+Click` to place additional cursors.
- Go to defenition: `F12`.
- Rename symbol: `F2`.
- Format document: `Shift+Alt+F`.
- Extensions: enstall idioma support (Python, Rust, Go, etc.), lenters, y paramatters from el/la Extensions panel (`Ctrl+Shift+X`).
- `settengs.json` (user or workspace) controls editor behaviour.
- `launch.json` configures el/la debugger.

# ## JetBraens IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLy)

- Smart code completion y refactoreng are core features.
- Run/debug configurations let you launch y debug programs con one click.
- Built-en Git support en el/la VCS menu.
- `Shift+Shift` opens el/la Search Everywhere dialog.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) reparamats code.
- Plugens extend idioma support y add tools.

# ## Termenal tips

- Use tab completion to fenish file names y commys quickly.
- Press `Ctrl+R` to search commy historia enteractively.
- `alias ll='ls -la'` creates a shortcut — add it to `~/.bashrc` or `~/.zshrc`.
- Use `tmux` or `screen` to keep sessions alive when disconnected from a remote server.
- `man <commy>` shows el/la manual page para any built-en commy.

---

# # Docker

Docker packages applications y el/lair dependencies ento portable contaeners.

# ## Core concepts

- **Image**: a read-only template built from a `Dockerfile`.
- **Contaener**: a runneng enstance de an image.
- **Registry**: a storage y distribution service para images (Docker Hub, GHCR).
- **Volume**: persistent storage that outlives a contaener.

# ## Common commys

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

Docker Compose manages multi-contaener applications con a `docker-compose.yml` file.

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
