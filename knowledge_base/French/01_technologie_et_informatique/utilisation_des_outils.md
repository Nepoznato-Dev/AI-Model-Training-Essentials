<!-- 
Ce fichier a été traduit automatiquement de l'anglais vers le français.
Source: tool_usage.md
Note: Les termes techniques, exemples de code et noms propres peuvent rester en anglais.
Pour améliorer la précision, veuillez contribuer avec des modifications via des pull requests.
-->

# Utilisation des Outils

## Git — Gestion de Version

Git est un système de gestion de version distribué. Chaque développeur possède une copie complète de l'historique du dépôt sur sa machine locale.

### Flux de travail de base

```bash
# Démarrer un nouveau dépôt
git init

# Cloner un dépôt existant
git clone https://github.com/owner/repo.git

# Vérifier l'état et l'historique récent
git status
git log --oneline -10

# Ajouter des modifications (staging)
git add file.py            # ajouter un fichier spécifique
git add .                  # ajouter toutes les modifications dans le répertoire de travail

# Valider (commit)
git commit -m "Description courte et impérative du changement"

# Pousser vers un dépôt distant
git push origin main
```

### Gestion des branches

```bash
git branch feature/new-thing        # créer une branche
git checkout feature/new-thing      # basculer vers cette branche
# raccourci: git checkout -b feature/new-thing

git branch -d feature/new-thing     # supprimer la branche après fusion
```

### Fusion et rebasage

```bash
# Fusionner une branche de fonctionnalité dans main
git checkout main
git merge feature/new-thing

# Le rebasage conserve un historique linéaire
git checkout feature/new-thing
git rebase main
```

### Flux de travail des pull requests (PR)

1. Créer une branche de fonctionnalité depuis `main`.
2. Effectuer des commits sur la branche de fonctionnalité.
3. Pousser la branche: `git push origin feature/new-thing`.
4. Ouvrir une pull request sur GitHub / GitLab.
5. Répondre aux commentaires de revue de code avec des commits supplémentaires.
6. Fusionner la PR une fois approuvée.

### Annuler des modifications

```bash
git restore file.py            # ignorer les modifications non validées
git restore --staged file.py   # retirer un fichier de la zone de staging
git revert <commit-sha>        # créer un nouveau commit qui annule un précédent
git reset --soft HEAD~1        # annuler le dernier commit, garder les modifications en staging
```

---

## Gestionnaires de Paquets

### pip (Python)

```bash
pip install requests            # installer un paquet
pip install "requests>=2.28"    # avec contrainte de version
pip install -r requirements.txt # installer depuis un fichier
pip uninstall requests
pip list                        # afficher les paquets installés
pip show requests               # informations sur un paquet
```

Travaillez toujours dans un environnement virtuel pour isoler les dépendances du projet.

### npm (Node.js / JavaScript)

```bash
npm init -y                     # créer package.json
npm install express             # installer comme dépendance d'exécution
npm install --save-dev jest     # installer comme dépendance de développement
npm uninstall express
npm update
npm run test                    # exécuter le script "test" depuis package.json
npm run build
npx create-react-app my-app     # exécuter un paquet sans installation globale
```

`package-lock.json` enregistre les versions exactes; commitez-le dans le contrôle de source.

### Cargo (Rust)

```bash
cargo new my_project            # nouveau projet binaire
cargo new --lib my_lib          # nouvelle bibliothèque
cargo add serde --features derive
cargo build
cargo run
cargo test
cargo clippy                    # linting
cargo fmt                       # formatage
cargo update                    # mettre à jour les dépendances dans les contraintes
```

### Modules Go (Go)

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
sudo apt update                 # rafraîchir les listes de paquets
sudo apt install git curl wget  # installer des paquets
sudo apt remove package-name
sudo apt upgrade                # mettre à jour tous les paquets installés
apt search keyword              # rechercher des paquets
apt show package-name           # détails sur un paquet
```

---

## Bases de la Ligne de Commande

### Navigation

```bash
pwd                             # afficher le répertoire de travail actuel
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
less file.txt                   # parcourir un fichier avec défilement
head -n 20 file.txt             # 20 premières lignes
tail -n 20 file.txt             # 20 dernières lignes
tail -f log.txt                 # suivre un fichier journal en croissance
grep "pattern" file.txt         # rechercher un motif
grep -r "pattern" ./src/        # recherche récursive
grep -i "pattern" file.txt      # insensible à la casse
```

### Pipes et redirections

```bash
command1 | command2             # rediriger la sortie de command1 vers command2
ls -la | grep ".py"             # lister uniquement les fichiers Python
cat file.txt | wc -l            # compter les lignes
command > output.txt            # rediriger stdout vers un fichier (écraser)
command >> output.txt           # ajouter stdout à un fichier
command 2>&1                    # fusionner stderr dans stdout
```

### Réseau et transfert de fichiers

```bash
curl https://example.com                     # récupérer une URL
curl -o file.zip https://example.com/f.zip   # télécharger vers un fichier
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # télécharger avec wget
```

### Permissions

```bash
chmod +x script.sh              # rendre exécutable
chmod 644 file.txt              # propriétaire lecture/écriture, groupe/autres lecture
chown user:group file.txt       # changer propriétaire et groupe
```

### Gestion des processus

```bash
ps aux                          # lister les processus en cours d'exécution
kill <PID>                      # envoyer SIGTERM à un processus
kill -9 <PID>                   # forcer l'arrêt
top / htop                      # moniteur de processus interactif
```

---

## Éditeurs et IDEs

### VS Code

VS Code est un éditeur de code léger et multiplateforme avec un riche écosystème d'extensions.

- Ouvrir un dossier: `File > Open Folder` ou `code .` dans le terminal.
- Palette de commandes: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- Terminal intégré: `Ctrl+`` (accent grave)`.
- Multi-curseur: `Alt+Clic` pour placer des curseurs supplémentaires.
- Aller à la définition: `F12`.
- Renommer un symbole: `F2`.
- Formater le document: `Shift+Alt+F`.
- Extensions: installez le support linguistique (Python, Rust, Go, etc.), linters et formatters depuis le panneau Extensions (`Ctrl+Shift+X`).
- `settings.json` (utilisateur ou espace de travail) contrôle le comportement de l'éditeur.
- `launch.json` configure le débogueur.

### IDEs JetBrains (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- La complétion intelligente du code et le refactoring sont des fonctionnalités principales.
- Les configurations d'exécution/débogage permettent de lancer et déboguer des programmes en un clic.
- Support Git intégré dans le menu VCS.
- `Shift+Shift` ouvre la boîte de dialogue Rechercher partout.
- `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) reformate le code.
- Les plugins étendent le support des langages et ajoutent des outils.

### Astuces pour le terminal

- Utilisez la complétion par tabulation pour terminer rapidement les noms de fichiers et commandes.
- Appuyez sur `Ctrl+R` pour rechercher dans l'historique des commandes de manière interactive.
- `alias ll='ls -la'` crée un raccourci — ajoutez-le à `~/.bashrc` ou `~/.zshrc`.
- Utilisez `tmux` ou `screen` pour maintenir les sessions actives lors de la déconnexion d'un serveur distant.
- `man <commande>` affiche la page de manuel pour toute commande intégrée.

---

## Docker

Docker empaquette les applications et leurs dépendances dans des conteneurs portables.

### Concepts de base

- **Image**: un modèle en lecture seule construit à partir d'un `Dockerfile`.
- **Conteneur**: une instance en cours d'exécution d'une image.
- **Registre**: un service de stockage et de distribution pour les images (Docker Hub, GHCR).
- **Volume**: stockage persistant qui survit au conteneur.

### Commandes courantes

```bash
# Images
docker pull ubuntu:22.04
docker images
docker rmi ubuntu:22.04

# Conteneurs
docker run -it ubuntu:22.04 bash        # shell interactif
docker run -d -p 8080:80 nginx          # détaché, mappage de port
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
docker compose logs -f     # flux des journaux
docker compose build       # reconstruire les images
```
