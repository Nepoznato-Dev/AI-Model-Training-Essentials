# Référence rapide des commandes Git

Commandes Git essentielles pour le contrôle de version.

---

## Installation et configuration

```bash
# Configurer les informations utilisateur
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Afficher la configuration
git config --list
git config user.name

# Définir le nom de la branche par défaut
git config --global init.defaultBranch main
```

---

## Initialisation du dépôt

```bash
# Initialiser un nouveau dépôt
git init

# Cloner un dépôt existant
git clone <url>
git clone <url> folder-name

# Cloner une branche spécifique
git clone -b branch-name <url>
```

---

## Flux de travail de base

```bash
# Vérifier l'état
git status

# Voir les modifications
git diff
git diff --staged

# Indexer des fichiers
git add file.txt          # Fichier spécifique
git add .                 # Tous les fichiers
git add *.py              # Correspondance par motif

# Valider les modifications
git commit -m "Commit message"
git commit -am "Message"  # Indexer et valider les fichiers suivis

# Afficher l'historique des commits
git log
git log --oneline
git log --graph --oneline --all
```

---

## Branches

```bash
# Lister les branches
git branch                # Branches locales
git branch -a             # Toutes les branches
git branch -r             # Branches distantes

# Créer une branche
git branch branch-name
git checkout -b branch-name   # Créer et basculer

# Changer de branche
git checkout branch-name
git switch branch-name        # Syntaxe plus récente

# Renommer la branche actuelle
git branch -m new-name

# Supprimer une branche
git branch -d branch-name     # Suppression sûre (fusionnée)
git branch -D branch-name     # Suppression forcée

# Fusionner une branche
git merge branch-name

# Rebaser une branche
git rebase main
```

---

## Opérations distantes

```bash
# Afficher les remotes
git remote -v

# Ajouter un remote
git remote add origin <url>

# Récupérer depuis le remote
git fetch origin
git fetch --all

# Rapatrier les modifications (fetch + merge)
git pull origin main
git pull --rebase origin main

# Pousser les modifications
git push origin main
git push -u origin main     # Définir la branche upstream
git push --force            # Forcer l'envoi (à utiliser avec prudence)
git push --force-with-lease # Forçage plus sûr

# Pousser les tags
git push --tags
```

---

## Annuler des modifications

```bash
# Retirer un fichier de l'index (conserver les modifications)
git reset HEAD file.txt
git restore --staged file.txt

# Abandonner les modifications locales
git checkout -- file.txt
git restore file.txt

# Modifier le dernier commit
git commit --amend -m "New message"
git commit --amend --no-edit

# Annuler un commit (sûr pour les dépôts partagés)
git revert commit-hash

# Revenir au commit précédent
git reset --soft HEAD~1     # Conserver les modifications indexées
git reset --mixed HEAD~1    # Conserver les modifications hors index (par défaut)
git reset --hard HEAD~1     # Abandonner toutes les modifications (dangereux)
```

---

## Stash

```bash
# Sauvegarder le travail en cours
git stash
git stash save "message"

# Lister les stashs
git stash list

# Appliquer un stash
git stash apply             # Le plus récent
git stash apply stash@{1}   # Stash spécifique

# Appliquer et supprimer
git stash pop

# Supprimer un stash
git stash drop stash@{1}

# Effacer tous les stashs
git stash clear
```

---

## Tags

```bash
# Lister les tags
git tag
git tag -l "v1.*"

# Créer un tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # Tag annoté

# Se placer sur un tag
git checkout v1.0.0

# Supprimer un tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## Affichage et recherche

```bash
# Afficher les détails d'un commit
git show commit-hash
git show --stat commit-hash

# Blame (qui a modifié quoi)
git blame file.txt

# Rechercher des commits
git log --grep="keyword"
git log --author="name"

# Rechercher du code dans l'historique
git log -S"function_name"

# Afficher un fichier à un commit spécifique
git show commit-hash:file.txt
```

---

## Opérations avancées

```bash
# Cherry-pick d'un commit
git cherry-pick commit-hash

# Rebase interactif
git rebase -i HEAD~5

# Squasher des commits (pendant le rebase)
# Remplacer 'pick' par 'squash' ou 's' dans l'éditeur

# Créer un patch
git format-patch -1 commit-hash

# Appliquer un patch
git apply patch-file.patch
git am patch-file.patch

# Submodules
git submodule add <url> path
git submodule update --init --recursive
```

---

## Nettoyage

```bash
# Supprimer les fichiers non suivis (simulation)
git clean -n
git clean -f                # Supprime réellement

# Supprimer les répertoires non suivis
git clean -fd

# Élaguer les branches distantes supprimées
git fetch --prune
git remote prune origin
```

---

## Workflows courants

### Démarrer une nouvelle fonctionnalité
```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... travail ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# Créer une PR/MR sur la plateforme
```

### Se synchroniser avec `main`
```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# Résoudre les conflits si nécessaire
git push --force-with-lease
```

### Flux de travail de hotfix
```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... correction ...
git commit -am "Fix critical bug"
git checkout main
git merge hotfix/urgent-fix
git push
git tag v1.0.1
git push --tags
```

---

## Motifs `.gitignore`

```gitignore
# Ignorer un fichier spécifique
filename.txt

# Ignorer tous les fichiers .log
*.log

# Ignorer un répertoire
node_modules/
__pycache__/

# Négation (inclure malgré un motif précédent)
!important.log

# Commentaire
# Ceci est un commentaire
```

---

## Raccourcis clavier (Git Bash)

| Raccourci | Action |
|----------|--------|
| `Ctrl+R` | Recherche inversée dans l'historique |
| `Tab` | Auto-complétion |
| `Ctrl+C` | Annuler la commande |
| `Ctrl+Z` | Suspendre le processus |
| `fg` | Reprendre un processus suspendu |

---

## Bonnes pratiques

✅ **À faire :**
- Écrire des messages de commit clairs et descriptifs
- Commiter fréquemment avec des regroupements logiques
- Utiliser des branches pour les fonctionnalités/corrections
- Faire un `pull` avant de commencer à travailler
- Vérifier souvent `git status`

❌ **À éviter :**
- Commiter des données sensibles (clés API, mots de passe)
- Forcer l'envoi sur des branches partagées
- Commiter de gros fichiers binaires
- Ignorer les conflits de fusion
- Travailler directement sur `main`/`master`

---

## Convention de message de commit

```
type(scope): subject

body (optional)

footer (optional)
```

**Types :**
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation
- `style`: Mise en forme
- `refactor`: Restructuration du code
- `test`: Tests
- `chore`: Maintenance

**Exemple :**
```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*Dernière mise à jour : juin 2025 | Git 2.x*
