<!-- 
This file was automatically translated from English to French.
Source: tool_usage.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Utilisation des outils

## Git — Contrôle de version

Git est un système de contrôle de version distribué. Chaque développeur possède une copie complète du dépôt et de l'historique sur sa machine locale.

### Flux de travail de base

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

### Branches

```bash
git branch feature/new-thing        # create a branch
git checkout feature/new-thing      # switch to it
# shortcut: git checkout -b feature/new-thing

git branch -d feature/new-thing     # delete branch after merging
```

### Fusion et rebasage

```bash
# Merge feature branch into main
git checkout main
git merge feature/new-thing

# Rebase keeps a linear history
git checkout feature/new-thing
git rebase main
```

### Flux de travail des pull requests (PR)

1. Créez une branche de fonctionnalité à partir de `main`.
2. Effectuez vos commits sur la branche de fonctionnalité.
3. Poussez la branche : `git push origin feature/new-thing`.
4. Ouvrez une pull request sur GitHub ou GitLab.
5. Répondez aux retours de revue de code avec des commits supplémentaires.
6. Fusionnez la PR une fois approuvée.

### Annuler des modifications

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage a file
git revert <commit-sha>        # create a new commit that undoes a previous one
git reset --soft HEAD~1        # undo last commit, keep changes staged
```

---

## Gestionnaires de paquets

### pip (Python)

```bash
pip install requests            # install a package
pip install "requests>=2.28"    # with version constraint
pip install -r requirements.txt # install from a file
pip uninstall requests
pip list                        # show installed packages
pip show requests               # info about a package
```

Travaillez toujours dans un environnement virtuel pour isoler les dépendances du projet.

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

`package-lock.json` enregistre les versions exactes ; validez-le dans le contrôle de version.

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

### Modules Go (Go)

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

## Bases de la ligne de commande

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

### Traitement de texte

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

### Pipelines et redirection

```bash
command1 | command2             # pipe output of command1 into command2
ls -la | grep ".py"             # list only Python files
cat file.txt | wc -l            # count lines
command > output.txt            # redirect stdout to a file (overwrite)
command >> output.txt           # append stdout to a file
command 2>&1                    # merge stderr into stdout
```

### Réseau et transfert de fichiers

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

### Gestion des processus

```bash
ps aux                          # list running processes
kill <PID>                      # send SIGTERM to a process
kill -9 <PID>                   # force kill
top / htop                      # interactive process monitor
```

---

## Éditeurs et IDE

### VS Code

VS Code est un éditeur de code léger et multiplateforme doté d'un riche écosystème d'extensions.

- Ouvrir un dossier : `File > Open Folder` ou `code .` dans le terminal.
- Palette de commandes : `Ctrl+Shift+P` (macOS : `Cmd+Shift+P`).
- Terminal intégré : `Ctrl+`` (accent grave).
- Multi-curseur : `Alt+Clic` pour placer des curseurs supplémentaires.
- Aller à la définition : `F12`.
- Renommer un symbole : `F2`.
- Formater le document : `Shift+Alt+F`.
- Extensions : installez l'assistance linguistique (Python, Rust, Go, etc.), les linters et les formatters depuis le panneau Extensions (`Ctrl+Shift+X`).
- `settings.json` (utilisateur ou espace de travail) contrôle le comportement de l'éditeur.
- `launch.json` configure le débogueur.

### IDE JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- L'auto-complétion intelligente et le refactoring sont des fonctionnalités clés.
- Les configurations d'exécution et de débogage permettent de lancer et déboguer des programmes en un clic.
- L'intégration de Git est disponible dans le menu VCS.
- `Shift+Shift` ouvre la boîte de dialogue Search Everywhere.
- `Ctrl+Alt+L` (macOS : `Cmd+Option+L`) reformate le code.
- Les plugins étendent l'assistance linguistique et ajoutent des outils.

### Astuces pour le terminal

- Utilisez l'auto-complétion par tabulation pour terminer rapidement les noms de fichiers et les commandes.
- Appuyez sur `Ctrl+R` pour rechercher de façon interactive dans l'historique des commandes.
- `alias ll='ls -la'` crée un raccourci — ajoutez-le à `~/.bashrc` ou `~/.zshrc`.
- Utilisez `tmux` ou `screen` pour maintenir les sessions actives lors de la déconnexion d'un serveur distant.
- `man <command>` affiche la page de manuel de n'importe quelle commande.

---

## Docker

Docker empaquette les applications et leurs dépendances dans des conteneurs portables.

### Concepts de base

- **Image** : modèle en lecture seule construit à partir d'un `Dockerfile`.
- **Conteneur** : instance en cours d'exécution d'une image.
- **Registre** : service de stockage et de distribution des images (Docker Hub, GHCR).
- **Volume** : stockage persistant qui survit au conteneur.

### Commandes courantes

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

### Exemple de Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

Docker Compose gère les applications multi-conteneurs à l'aide d'un fichier `docker-compose.yml`.

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
