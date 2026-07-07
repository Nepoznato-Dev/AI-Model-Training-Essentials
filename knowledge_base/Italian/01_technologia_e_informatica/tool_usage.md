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

### rete e trasferimento di file

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

### gestione dei processi

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
- Multi-cursore: `Alt+Click` per posizionare cursori aggiuntivi.
- Vai alla definizione: `F12`.
- Rinomina il simbolo: `F2`.
- Formato documento: `Shift+Alt+F`.
- Estensioni: installa il supporto della lingua (Python, Rust, Go, ecc.), linter e formattatori dal pannello Estensioni (`Ctrl+Shift+X`).
- `settings.json` (utente o spazio di lavoro) controlla il comportamento dell'editor.
- `launch.json` configura il debugger.

### IDE JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- Il completamento intelligente del codice e il refactoring sono caratteristiche principali.
- Le configurazioni di esecuzione/debug ti consentono di avviare ed eseguire il debug dei programmi con un clic.
- Supporto Git integrato nel menu VCS.
- `Shift+Shift` apre la finestra di dialogo Cerca ovunque.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) riformatta il codice.
- I plugin estendono il supporto linguistico e aggiungono strumenti.

### Suggerimenti per il terminale

- Utilizza il completamento tramite tabulazione per completare rapidamente i nomi dei file e i comandi.
- Premere `Ctrl+R` per cercare la cronologia dei comandi in modo interattivo.
- `alias ll='ls -la'` crea un collegamento: aggiungilo a `~/.bashrc` o `~/.zshrc`.
- Utilizzare `tmux` o `screen` per mantenere attive le sessioni quando si è disconnessi da un server remoto.
- `man <command>` mostra la pagina di manuale per qualsiasi comando integrato.

---

##Docker

Docker impacchetta le applicazioni e le relative dipendenze in contenitori portatili.

### Concetti fondamentali

- **Immagine**: un modello di sola lettura creato da un `Dockerfile`.
- **Contenitore**: un'istanza in esecuzione di un'immagine.
- **Registry**: un servizio di archiviazione e distribuzione di immagini (Docker Hub, GHCR).
- **Volume**: spazio di archiviazione persistente che sopravvive a un contenitore.

### comandi comuni

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

### Esempio di file Docker

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Componi

Docker Compose gestisce applicazioni multi-contenitore con un file `docker-compose.yml`.

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