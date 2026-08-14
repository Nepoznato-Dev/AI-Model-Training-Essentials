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
# Paggamit ng Tool
## Git — Kontrol sa Bersyon
Ang Git ay isang distributed version control system. Ang bawat developer ay may buong kopya ng kasaysayan ng repositoryo sa kanilang lokal na makina.
### Pangunahing daloy ng trabaho
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

### Sumasanga
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Pagsasama at muling pagbabawas
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Pull request (PR) workflow
1. Gumawa ng feature branch mula sa`main`.
2. Gumawa ng mga commit sa feature branch.
3. Itulak ang sangay:`git push origin feature/new-thing`.
4. Magbukas ng pull request sa GitHub / GitLab.
5. Feedback sa pagsusuri ng address code na may mga karagdagang commit.
6. Pagsamahin ang PR kapag naaprubahan.
### Ina-undo ang mga pagbabago
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Mga Tagapamahala ng Package
### pip (Python)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Palaging magtrabaho sa loob ng isang virtual na kapaligiran upang panatilihing nakahiwalay ang mga dependency ng proyekto.
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

Ang`package-lock.json`ay nagtatala ng mga eksaktong bersyon; i-commit ito sa source control.
### Cargo (Kalawang)
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

## Mga Pangunahing Kaalaman sa Command-Line
### Nabigasyon
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

### Pagproseso ng teksto
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

### Mga tubo at pag-redirect
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Paglipat ng network at file
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Mga Pahintulot
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Pamamahala ng proseso
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Mga editor at IDE
### VS Code
Ang VS Code ay isang magaan, cross-platform na code editor na may isang rich extension ecosystem.
- Magbukas ng folder:`File > Open Folder`o`code .`sa terminal.
- Command palette:`Ctrl+Shift+P`(macOS:`Cmd+Shift+P`).
- Pinagsamang terminal:`Ctrl+`` (backtick)` .
- Multi-cursor:`Alt+Click`upang maglagay ng mga karagdagang cursor.
- Pumunta sa kahulugan:`F12`.
- Palitan ang pangalan ng simbolo:`F2`.
- Format ng dokumento:`Shift+Alt+F`.
- Mga Extension: i-install ang suporta sa wika (Python, Rust, Go, atbp.), mga linter, at mga formatter mula sa panel ng Mga Extension (`Ctrl+Shift+X`).
- Kinokontrol ng`settings.json`(user o workspace) ang pag-uugali ng editor.
- Kino-configure ng`launch.json`ang debugger.
### Mga JetBrains IDE (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- Ang pagkumpleto ng matalinong code at refactoring ay mga pangunahing tampok.
- Hinahayaan ka ng mga configuration ng Run/debug na ilunsad at i-debug ang mga program sa isang click.
- Built-in na suporta sa Git sa VCS menu.
- Binubuksan ng`Shift+Shift`ang dialog ng Search Everywhere.
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) nire-reformat ang code.
- Ang mga plugin ay nagpapalawak ng suporta sa wika at magdagdag ng mga tool.
### Mga tip sa terminal
- Gamitin ang pagkumpleto ng tab upang mabilis na tapusin ang mga pangalan ng file at command.
- Pindutin ang`Ctrl+R`upang maghanap sa history ng command nang interactive.
- Lumilikha ang`alias ll='ls -la'`ng shortcut — idagdag ito sa`~/.bashrc`o`~/.zshrc`.
- Gamitin ang`tmux`o`screen`upang panatilihing buhay ang mga session kapag nadiskonekta mula sa isang malayuang server.
- Ipinapakita ng`man <command>`ang manual page para sa anumang built-in na command.
---

## Docker
Inilalagay ng Docker ang mga application at ang kanilang mga dependency sa mga portable na lalagyan.
### Mga pangunahing konsepto
- **Larawan**: isang read-only na template na binuo mula sa isang`Dockerfile`.
- **Container**: isang tumatakbong instance ng isang imahe.
- **Registry**: isang storage at distribution service para sa mga larawan (Docker Hub, GHCR).
- **Volume**: paulit-ulit na storage na hindi nabubuhay sa isang container.
### Mga karaniwang utos
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

### Halimbawa ng Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose
Ang Docker Compose ay namamahala ng mga multi-container na application na may`docker-compose.yml`file.
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
