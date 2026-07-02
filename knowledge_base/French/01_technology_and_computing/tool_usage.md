# Utilisation des outils

## Git — Contrôle de version

Git est un système de contrôle de version distribué. Chaque développeur possède une copie complète de l'historique du dépôt sur sa machine locale.

### Workflow de base

```bash
# Démarrer un nouveau dépôt
git init

# Cloner un dépôt existant
git clone https://github.com/owner/repo.git

# Vérifier l'état et l'historique récent
git status
git log --oneline -10

# Préparer les changements
git add file.py            # préparer un fichier spécifique
git add .                  # préparer tous les changements du répertoire de travail

# Commit
git commit -m "Short, imperative description of change"

# Push vers un dépôt distant
git push origin main
```

### Branching

```bash
git branch feature/new-thing        # créer une branche
git checkout feature/new-thing      # s'y déplacer
# raccourci : git checkout -b feature/new-thing

git branch -d feature/new-thing     # supprimer la branche après fusion
```

### Merging et rebasing

```bash
# Fusionner la branche de fonctionnalité dans main
git checkout main
git merge feature/new-thing

# Rebase conserve un historique linéaire
git checkout feature/new-thing
git rebase main
```

### Workflow de pull request (PR)

1. Créer une branche de fonctionnalité à partir de `main`.
2. Effectuer des commits sur la branche de fonctionnalité.
3. Envoyer la branche : `git push origin feature/new-thing`.
4. Ouvrir une pull request sur GitHub / GitLab.
5. Traiter les retours de code review avec des commits supplémentaires.
6. Fusionner la PR une fois approuvée.

### Annuler des changements

```bash
git restore file.py            # annuler les changements non indexés
git restore --staged file.py   # retirer un fichier de la zone de préparation
git revert <commit-sha>        # créer un nouveau commit qui annule un précédent
git reset --soft HEAD~1        # annuler le dernier commit, conserver les changements préparés
```

---

## Gestionnaires de packages

### pip (Python)

```bash
pip install requests            # installer un package
pip install "requests>=2.28"    # avec contrainte de version
pip install -r requirements.txt # installer depuis un fichier
pip uninstall requests
pip list                        # afficher les packages installés
pip show requests               # informations sur un package
```

Travaillez toujours dans un environnement virtuel pour garder les dépendances du projet isolées.

### npm (Node.js / JavaScript)

```bash
npm init -y                     # créer package.json
npm install express             # installer comme dépendance d'exécution
npm install --save-dev jest     # installer comme dépendance de développement
npm uninstall express
npm update
npm run test                    # exécuter le script "test" de package.json
npm run build
npx create-react-app my-app     # exécuter un package sans l'installer globalement
```

`package-lock.json` enregistre les versions exactes ; committez-le dans le contrôle de version.

### Cargo (Rust)

```bash
cargo new my_project            # nouveau projet binaire
cargo new --lib my_lib          # nouvelle bibliothèque
cargo add serde --features derive
cargo build
cargo run
cargo test
cargo clippy                    # lint
cargo fmt                       # formatage
cargo update                    # mettre à jour les dépendances selon les contraintes
```

### Go modules (Go)

```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # supprimer les dépendances inutilisées
go build ./...
go test ./...
go vet ./...
```

### apt (Debian / Ubuntu Linux)

```bash
sudo apt update                 # rafraîchir la liste des packages
sudo apt install git curl wget  # installer des packages
sudo apt remove package-name
sudo apt upgrade                # mettre à niveau tous les packages installés
apt search keyword              # rechercher des packages
apt show package-name           # détails sur un package
```

---

## Bases de la ligne de commande

### Navigation

```bash
pwd                             # afficher le répertoire de travail
ls                              # lister le contenu du répertoire
ls -la                          # liste détaillée incluant les fichiers cachés
cd /path/to/dir                 # changer de répertoire
cd ..                           # remonter d'un niveau
cd ~                            # aller au répertoire personnel
mkdir new_folder
rm file.txt                     # supprimer un fichier
rm -r folder/                   # supprimer un répertoire récursivement
cp src.txt dst.txt
mv old_name.txt new_name.txt
```

### Traitement de texte

```bash
cat file.txt                    # afficher le contenu d'un fichier
less file.txt                   # parcourir un fichier
head -n 20 file.txt             # 20 premières lignes
tail -n 20 file.txt             # 20 dernières lignes
tail -f log.txt                 # suivre un fichier log en croissance
grep "pattern" file.txt         # rechercher un motif
grep -r "pattern" ./src/        # recherche récursive
grep -i "pattern" file.txt      # insensible à la casse
```

### Pipes et redirections

```bash
command1 | command2             # envoyer la sortie de command1 vers command2
ls -la | grep ".py"             # lister uniquement les fichiers Python
cat file.txt | wc -l            # compter les lignes
command > output.txt            # rediriger stdout vers un fichier (écrase)
command >> output.txt           # ajouter stdout à un fichier
command 2>&1                    # fusionner stderr dans stdout
```

### Réseau et transfert de fichiers

```bash
curl https://example.com                     # récupérer une URL
curl -o file.zip https://example.com/f.zip   # télécharger dans un fichier
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # télécharger avec wget
```

### Permissions

```bash
chmod +x script.sh              # rendre exécutable
chmod 644 file.txt              # propriétaire lecture/écriture, groupe/autres lecture
chown user:group file.txt       # changer le propriétaire et le groupe
```

### Gestion des processus

```bash
ps aux                          # lister les processus en cours
kill <PID>                      # envoyer SIGTERM à un processus
kill -9 <PID>                   # forcer l'arrêt
top / htop                      # moniteur interactif des processus
```

---

## Éditeurs et IDEs

### VS Code

VS Code est un éditeur de code léger, multiplateforme, avec un riche écosystème d'extensions.

- Ouvrir un dossier : `File > Open Folder` ou `code .` dans le terminal.
- Palette de commandes : `Ctrl+Shift+P` (macOS : `Cmd+Shift+P`).
- Terminal intégré : `Ctrl+`` (backtick)`.
- Multi-cursor : `Alt+Click` pour placer des curseurs supplémentaires.
- Aller à la définition : `F12`.
- Renommer un symbole : `F2`.
- Formater le document : `Shift+Alt+F`.
- Extensions : installez la prise en charge des langages (Python, Rust, Go, etc.), des linters et des formatters depuis le panneau Extensions (`Ctrl+Shift+X`).
- `settings.json` (utilisateur ou workspace) contrôle le comportement de l'éditeur.
- `launch.json` configure le débogueur.

### IDEs JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- L'autocomplétion intelligente et le refactoring sont des fonctionnalités centrales.
- Les configurations d'exécution/de débogage permettent de lancer et déboguer les programmes en un clic.
- Prise en charge Git intégrée dans le menu VCS.
- `Shift+Shift` ouvre la boîte de dialogue Search Everywhere.
- `Ctrl+Alt+L` (macOS : `Cmd+Option+L`) reformate le code.
- Les plugins étendent la prise en charge des langages et ajoutent des outils.

### Astuces terminal

- Utilisez l'autocomplétion par tabulation pour terminer rapidement les noms de fichiers et les commandes.
- Appuyez sur `Ctrl+R` pour rechercher l'historique des commandes de manière interactive.
- `alias ll='ls -la'` crée un raccourci — ajoutez-le à `~/.bashrc` ou `~/.zshrc`.
- Utilisez `tmux` ou `screen` pour conserver les sessions actives lors d'une déconnexion d'un serveur distant.
- `man <command>` affiche la page de manuel de toute commande intégrée.

---

## Docker

Docker regroupe les applications et leurs dépendances dans des conteneurs portables.

### Concepts fondamentaux

- **Image** : modèle en lecture seule construit à partir d'un `Dockerfile`.
- **Container** : instance en cours d'exécution d'une image.
- **Registry** : service de stockage et de distribution d'images (Docker Hub, GHCR).
- **Volume** : stockage persistant qui survit à un conteneur.

### Commandes courantes

```bash
# Images
docker pull ubuntu:22.04
docker images
docker rmi ubuntu:22.04

# Conteneurs
docker run -it ubuntu:22.04 bash        # shell interactif
docker run -d -p 8080:80 nginx          # détaché, mapping de port
docker ps                               # conteneurs en cours d'exécution
docker ps -a                            # tous les conteneurs
docker stop <container_id>
docker rm <container_id>
docker logs <container_id>
docker exec -it <container_id> bash     # ouvrir un shell dans un conteneur en cours d'exécution

# Construction
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

Docker Compose gère les applications multi-conteneurs avec un fichier `docker-compose.yml`.

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
docker compose up -d       # démarrer tous les services en arrière-plan
docker compose down        # arrêter et supprimer les conteneurs
docker compose logs -f     # diffuser les logs
docker compose build       # reconstruire les images
```
