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
# Werkzeugnutzung
## Git – Versionskontrolle
Git ist ein verteiltes Versionskontrollsystem. Jeder Entwickler verfügt über eine vollständige Kopie des Repository-Verlaufs auf seinem lokalen Computer.
### Kernworkflow
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

### Verzweigung
```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Zusammenführen und Umbasieren
```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Pull-Request-Workflow (PR).
1. Erstellen Sie einen Feature-Zweig aus`main`.
2. Nehmen Sie Commits für den Feature-Zweig vor.
3. Drücken Sie den Zweig:`git push origin feature/new-thing`.
4. Öffnen Sie eine Pull-Anfrage auf GitHub / GitLab.
5. Behandeln Sie das Feedback zur Codeüberprüfung mit zusätzlichen Commits.
6. Führen Sie die PR nach der Genehmigung zusammen.
### Änderungen rückgängig machen
```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Paketmanager
### pip (Python)
```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Arbeiten Sie immer in einer virtuellen Umgebung, um Projektabhängigkeiten isoliert zu halten.
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

`package-lock.json` zeichnet genaue Versionen auf; Übergeben Sie es an die Quellcodeverwaltung.
### Fracht (Rost)
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

### Go-Module (Go)
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

## Befehlszeilen-Grundlagen
### Navigation
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

### Textverarbeitung
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

### Rohre und Umleitung
```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Netzwerk- und Dateiübertragung
```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Berechtigungen
```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Prozessmanagement
```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Editoren und IDEs
### VS-Code
VS Code ist ein leichter, plattformübergreifender Code-Editor mit einem umfangreichen Erweiterungsökosystem.
- Öffnen Sie einen Ordner:`File > Open Folder`oder`code .`im Terminal.
- Befehlspalette:`Ctrl+Shift+P`(macOS:`Cmd+Shift+P`).
- Integriertes Terminal:`Ctrl+`` (backtick)` .
- Multi-Cursor:`Alt+Click`zum Platzieren zusätzlicher Cursor.
- Gehe zur Definition:`F12`.
- Symbol umbenennen:`F2`.
- Dokument formatieren:`Shift+Alt+F`.
- Erweiterungen: Installieren Sie Sprachunterstützung (Python, Rust, Go usw.), Linters und Formatter über das Bedienfeld „Erweiterungen“ (`Ctrl+Shift+X`).
-`settings.json`(Benutzer oder Arbeitsbereich) steuert das Editorverhalten.
-`launch.json`konfiguriert den Debugger.
### JetBrains-IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)
- Intelligente Code-Vervollständigung und Refactoring sind Kernfunktionen.
- Mit Ausführungs-/Debug-Konfigurationen können Sie Programme mit einem Klick starten und debuggen.
- Integrierte Git-Unterstützung im VCS-Menü.
-`Shift+Shift`öffnet das Dialogfeld „Überall suchen“.
-`Ctrl+Alt+L`(macOS:`Cmd+Option+L`) formatiert den Code neu.
- Plugins erweitern die Sprachunterstützung und fügen Tools hinzu.
### Terminal-Tipps
- Verwenden Sie die Tab-Vervollständigung, um Dateinamen und Befehle schnell abzuschließen.
- Drücken Sie `Ctrl+R`, um den Befehlsverlauf interaktiv zu durchsuchen.
-`alias ll='ls -la'`erstellt eine Verknüpfung – fügen Sie sie zu`~/.bashrc`oder`~/.zshrc`hinzu.
– Verwenden Sie`tmux`oder `screen`, um Sitzungen aufrechtzuerhalten, wenn die Verbindung zu einem Remote-Server getrennt wird.
-`man <command>`zeigt die Handbuchseite für jeden integrierten Befehl.
---

## Docker
Docker verpackt Anwendungen und ihre Abhängigkeiten in tragbare Container.
### Kernkonzepte
- **Bild**: eine schreibgeschützte Vorlage, die aus einem`Dockerfile`erstellt wurde.
- **Container**: eine laufende Instanz eines Bildes.
- **Registrierung**: ein Speicher- und Verteilungsdienst für Bilder (Docker Hub, GHCR).
- **Volume**: persistenter Speicher, der einen Container überdauert.
### Allgemeine Befehle
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

### Dockerfile-Beispiel
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose
Docker Compose verwaltet Multi-Container-Anwendungen mit einer `docker-compose.yml`-Datei.
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
