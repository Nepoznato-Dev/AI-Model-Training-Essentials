# Guide de Référence Rapide des commandes Git

commandes Git essentielles pour le contrôle de version.

---

## Configuration et Initialisation

```bash
# Configurer les informations utilisateur
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@exemple.com"

# Voir la configuration
git config --list
git config user.name

# Définir le nom de branche par défaut
git config --global init.defaultBranch main
```

---

## Initialisation du Dépôt

```bash
# Initialiser un nouveau dépôt
git init

# Cloner un dépôt existant
git clone <url>
git clone <url> nom-dossier

# Cloner une branche spécifique
git clone -b nom-branche <url>
```

---

## Flux de Travail de Base

```bash
# Vérifier le statut
git status

# Voir les modifications
git diff
git diff --staged

# Ajouter des fichiers à l'index
git add fichier.txt          # Fichier spécifique
git add .                    # Tous les fichiers
git add *.py                 # Motif correspondant

# Valider les modifications
git commit -m "Message de commit"
git commit -am "Message"     # Ajouter et valider les fichiers suivis

# Voir l'historique des commits
git log
git log --oneline
git log --graph --oneline --all
```

---

## Branches

```bash
# Lister les branches
git branch                   # Branches locales
git branch -a                # Toutes les branches
git branch -r                # Branches distantes

# Créer une branche
git branch nom-branche
git checkout -b nom-branche  # Créer et basculer

# Changer de branche
git checkout nom-branche
git switch nom-branche       # Nouvelle syntaxe

# Renommer la branche actuelle
git branch -m nouveau-nom

# Supprimer une branche
git branch -d nom-branche    # Suppression sûre (fusionnée)
git branch -D nom-branche    # Forcer la suppression

# Fusionner une branche
git merge nom-branche

# Rebase une branche
git rebase main
```

---

## Opérations Distantes

```bash
# Voir les dépôts distants
git remote -v

# Ajouter un distant
git remote add origin <url>

# Récupérer depuis le distant
git fetch origin
git fetch --all

# Tirer les modifications (fetch + merge)
git pull origin main
git pull --rebase origin main

# Pousser les modifications
git push origin main
git push -u origin main      # Définir upstream
git push --force             # Force push (à utiliser avec prudence)
git push --force-with-lease  # Force push plus sûr

# Pousser les tags
git push --tags
```

---

## Annuler des Modifications

```bash
# Désindexer un fichier (garder les modifications)
git reset HEAD fichier.txt
git restore --staged fichier.txt

# Ignorer les modifications de travail
git checkout -- fichier.txt
git restore fichier.txt

# Modifier le dernier commit
git commit --amend -m "Nouveau message"
git commit --amend --no-edit

# Annuler un commit (sûr pour les dépôts partagés)
git revert commit-hash

# Réinitialiser au commit précédent
git reset --soft HEAD~1      # Garder les modifications indexées
git reset --mixed HEAD~1     # Garder les modifications non indexées (défaut)
git reset --hard HEAD~1      # Ignorer toutes les modifications (dangereux)
```

---

## Stash (Remise)

```bash
# Sauvegarder le travail en cours
git stash
git stash save "message"

# Lister les stashes
git stash list

# Appliquer un stash
git stash apply              # Le plus récent
git stash apply stash@{1}    # Stash spécifique

# Appliquer et supprimer
git stash pop

# Supprimer un stash
git stash drop stash@{1}

# Effacer tous les stashes
git stash clear
```

---

## Tags (Étiquettes)

```bash
# Lister les tags
git tag
git tag -l "v1.*"

# Créer un tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # Tag annoté

# Checkout un tag
git checkout v1.0.0

# Supprimer un tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## Visualisation et Recherche

```bash
# Afficher les détails d'un commit
git show commit-hash
git show --stat commit-hash

# Blame (qui a modifié quoi)
git blame fichier.txt

# Rechercher dans les commits
git log --grep="mot-clé"
git log --author="nom"

# Rechercher du code dans l'historique
git log -S"nom_fonction"

# Voir un fichier à un commit spécifique
git show commit-hash:fichier.txt
```

---

## Opérations Avancées

```bash
# Cherry-pick un commit
git cherry-pick commit-hash

# Rebase interactif
git rebase -i HEAD~5

# Compresser les commits (pendant rebase)
# Changer 'pick' en 'squash' ou 's' dans l'éditeur

# Créer un patch
git format-patch -1 commit-hash

# Appliquer un patch
git apply fichier-patch.patch
git am fichier-patch.patch

# Sous-modules
git submodule add <url> chemin
git submodule update --init --recursive
```

---

## Nettoyage

```bash
# Supprimer les fichiers non suivis (simulation)
git clean -n
git clean -f                 # Suppression réelle

# Supprimer les dossiers non suivis
git clean -fd

# Élaguer les branches distantes supprimées
git fetch --prune
git remote prune origin
```

---

## Flux de Travail Courants

### Démarrer une Nouvelle Fonctionnalité
```bash
git checkout main
git pull
git checkout -b feature/nouvelle-fonctionnalite
# ... travail ...
git add .
git commit -m "Ajouter nouvelle fonctionnalité"
git push -u origin feature/nouvelle-fonctionnalite
# Créer une PR/MR sur la plateforme
```

### Synchroniser avec Main
```bash
git checkout feature-branche
git fetch origin
git rebase origin/main
# Résoudre les conflits si nécessaire
git push --force-with-lease
```

### Flux de Travail Hotfix
```bash
git checkout main
git pull
git checkout -b hotfix/correction-urgente
# ... correction ...
git commit -am "Correction bug critique"
git checkout main
git merge hotfix/correction-urgente
git push
git tag v1.0.1
git push --tags
```

---

## Motifs .gitignore

```gitignore
# Ignorer un fichier spécifique
nomfichier.txt

# Ignorer tous les fichiers .log
*.log

# Ignorer un dossier
node_modules/
__pycache__/

# Nier (inclure malgré le motif précédent)
!important.log

# Commentaire
# Ceci est un commentaire
```

---

## Raccourcis Clavier (Git Bash)

| Raccourci | Action |
|----------|--------|
| `Ctrl+R` | Recherche inversée dans l'historique |
| `Tab` | Auto-complétion |
| `Ctrl+C` | Annuler la commande |
| `Ctrl+Z` | Suspendre le processus |
| `fg` | Reprendre le processus suspendu |

---

## Bonnes Pratiques

✅ **À faire:**
- Écrire des messages de commit clairs et descriptifs
- Committer fréquemment avec des regroupements logiques
- Utiliser des branches pour les fonctionnalités/corrections
- Tirer avant de commencer le travail
- Vérifier souvent `git status`

❌ **À ne pas faire:**
- Committer des données sensibles (clés API, mots de passe)
- Force push sur des branches partagées
- Committer de gros fichiers binaires
- Ignorer les conflits de fusion
- Travailler directement sur main/master

---

## Convention de Message de Commit

```
type(portée): sujet

corps (optionnel)

pied de page (optionnel)
```

**Types:**
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation
- `style`: Formatage
- `refactor`: Refactoring de code
- `test`: Tests
- `chore`: Maintenance

**Exemple:**
```
feat(auth): ajouter la fonctionnalité de réinitialisation de mot de passe

Implémenter la réinitialisation de mot de passe par email avec
vérification par token. Le token expire après 24 heures.

Ferme #123
```

---

*Dernière mise à jour: Juin 2025 | Git 2.x*
