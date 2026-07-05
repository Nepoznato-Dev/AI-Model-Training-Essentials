# Utilizzo dello strumento

## Git: controllo della versione

Git è un sistema di controllo della versione distribuito. Ogni sviluppatore ha una copia completa della cronologia del repository sul proprio computer locale.

### Flusso di lavoro principale

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

### Ramificazione

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Fusione e ribasamento

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Flusso di lavoro della richiesta pull (PR).

1. Crea un ramo di funzionalità da `main`.
2. Effettuare commit sul ramo della funzionalità.
3. Premere il ramo: `git push origin feature/new-thing`.
4. Apri una richiesta pull su GitHub/GitLab.
5. Affrontare il feedback sulla revisione del codice con commit aggiuntivi.
6. Unisci il PR una volta approvato.

### Annullamento delle modifiche

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Gestori di pacchetti

### pip (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Lavora sempre all'interno di un ambiente virtuale per mantenere isolate le dipendenze del progetto.

### npm (Node.js/JavaScript)

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

`package-lock.json` registra le versioni esatte; impegnarlo nel controllo del codice sorgente.

### Carico (Ruggine)

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

### Moduli Vai (Vai)

```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # remove unused dependencies
go build ./...
go test ./...
go vet ./...
```

### apt (Debian/Ubuntu Linux)

```bash
sudo apt update                 # refresh package lists
sudo apt install git curl wget  # install packages
sudo apt remove package-name
sudo apt upgrade                # upgrade all installed packages
apt search keyword              # search for packages
apt show package-name           # details about a package
```

---

## Nozioni di base sulla riga di comando

### Navigazione

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

### Elaborazione del testo

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

### Pipe e reindirizzamento

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Rete e trasferimento di file

```bash
curl https://example.com                     # fetch a URL
curl -o file.zip https://example.com/f.zip   # download to a file
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # download with wget
```

### Autorizzazioni

```bash
chmod +x script.sh              # make executable
chmod 644 file.txt              # owner read/write, group/others read
chown user:group file.txt       # change owner and group
```

### Gestione dei processi

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Editor e IDE

### Codice VS

VS Code è un editor di codice leggero e multipiattaforma con un ricco ecosistema di estensioni.

- Apri una cartella: `File > Open Folder` o `code .` nel terminale.
- Tavolozza dei comandi: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Terminale integrato: `Ctrl+`` (backtick)`.
- Multi-cursor: `Alt+clic` to place additional cursors.
- Go to definition: `F12`.
- Rename symbol: `F2`.
- Format document: `Maiusc+Alt+F`.
- Extensions: install language support (Python, Rust, Go, etc.), linters, and formatters from the Extensions panel (`Ctrl+Maiusc+X`).
- `settings.jso n` (user or workspace) controls editor behaviour.
- `launch.json` configures the debugger.

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Smart code completion and refactoring are core features.
- Run/debug configurations let you launch and debug programs with one click.
- Built-in Git support in the VCS menu.
- `Maiusc+Maiusc` opens the Search Everywhere dialog.
- `Ctrl+Alt+L` (macOS: `Cmd+Opzione+L`) reformats code.
- Plugins extend language support and add tools.

### Terminal tips

- Use tab completion to finish file names and commands quickly.
- Press `Ctrl+R` to search command history interactively.
- `alias ll='ls -la'` creates a shortcut — add it to `~/.bashrc` or `~/.zshrc`.
- Use `tmux` or `screen` to keep sessions alive when disconnected from a remote server.
- `man <comando>` shows the manual page for any built-in command.

---

## Docker

Docker packages applications and their dependencies into portable containers.

### Core concepts

- **Image**: a read-only template built from a `Dockerfile`.
- **Container**: a running instance of an image.
- **Registry**: a storage and distribution service for images (Docker Hub, GHCR).
- **Volume**: persistent storage that outlives a container.

### Common commands

<<<CODE_BLOCK_15>>>

### Dockerfile example

<<<CODE_BLOCK_16>>>

### Docker Compose

Docker Compose manages multi-container applications with a `docker-compose.yml`.

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