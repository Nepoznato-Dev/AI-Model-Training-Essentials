# Référence rapide des commandes Linux

Commandes Linux/Unix essentielles pour la navigation système et l'administration.

---

## Opérations sur les fichiers et répertoires

### Navigation
```bash
pwd                     # Afficher le répertoire de travail
ls                      # Lister les fichiers
ls -la                  # Lister tous les fichiers (y compris cachés) avec détails
ls -lh                  # Tailles lisibles par l'humain
cd /path/to/dir         # Changer de répertoire
cd ..                   # Remonter d'un répertoire
cd ~                    # Aller au répertoire personnel
cd -                    # Revenir au répertoire précédent
```

### Opérations sur les fichiers
```bash
touch file.txt          # Créer un fichier vide
cp source dest          # Copier un fichier
cp -r dir1 dir2         # Copier un répertoire récursivement
mv old new              # Déplacer/renommer un fichier
rm file.txt             # Supprimer un fichier
rm -r directory         # Supprimer un répertoire récursivement
rm -f file              # Forcer la suppression (sans invite)
rm -rf directory        # Forcer la suppression du répertoire (DANGEREUX)
mkdir newdir            # Créer un répertoire
mkdir -p path/to/dir    # Créer des répertoires imbriqués
ln -s target link       # Créer un lien symbolique
```

### Afficher les fichiers
```bash
cat file.txt            # Afficher tout le fichier
less file.txt           # Afficher le fichier page par page (q pour quitter)
head file.txt           # 10 premières lignes
head -n 20 file.txt     # 20 premières lignes
tail file.txt           # 10 dernières lignes
tail -n 20 file.txt     # 20 dernières lignes
tail -f logfile.log     # Suivre le fichier (mises à jour en direct)
```

---

## Permissions de fichiers

```bash
chmod 755 file          # Définir les permissions (rwxr-xr-x)
chmod +x script.sh      # Rendre exécutable
chmod -R 755 dir        # Changement de permissions récursif
chown user:group file   # Changer le propriétaire et le groupe
chown user file         # Changer seulement le propriétaire
chgrp group file        # Changer seulement le groupe
umask                   # Afficher le masque de permissions par défaut
```

### Valeurs numériques des permissions
- `7` = rwx (lecture + écriture + exécution)
- `6` = rw- (lecture + écriture)
- `5` = r-x (lecture + exécution)
- `4` = r-- (lecture seule)

---

## Traitement de texte

### Recherche et remplacement
```bash
grep "pattern" file.txt                 # Rechercher un motif
grep -r "pattern" dir/                  # Recherche récursive
grep -i "pattern" file.txt              # Insensible à la casse
grep -v "pattern" file.txt              # Correspondance inverse
grep -l "pattern" *.txt                 # Lister les fichiers correspondants
grep -c "pattern" file.txt              # Compter les correspondances
grep -E "pattern1|pattern2" file.txt    # Regex étendue
```

### Rechercher des fichiers
```bash
find /path -name "file.txt"             # Trouver par nom
find /path -name "*.py"                 # Trouver par extension
find /path -type d                      # Trouver les répertoires
find /path -type f                      # Trouver les fichiers
find /path -size +100M                  # Fichiers de plus de 100MB
find /path -mtime -7                    # Modifiés au cours des 7 derniers jours
find /path -perm 755                    # Trouver par permissions
find /path -exec command {} \;          # Exécuter une commande sur les résultats
```

### Manipulation de texte
```bash
wc file.txt             # Nombre de mots (lignes, mots, octets)
wc -l file.txt          # Nombre de lignes uniquement
sort file.txt           # Trier les lignes
sort -n file.txt        # Tri numérique
sort -r file.txt        # Tri inverse
uniq file.txt           # Supprimer les doublons adjacents
uniq -c file.txt        # Compter les occurrences
cut -d: -f1 /etc/passwd # Découper les champs par délimiteur
paste file1 file2       # Fusionner les fichiers côte à côte
tr 'a-z' 'A-Z' < file   # Convertir des caractères
sed 's/old/new/g' file  # Remplacer du texte
awk '{print $1}' file   # Afficher la première colonne
```

---

## Gestion des processus

```bash
ps                      # Afficher les processus en cours
ps aux                  # Tous les processus avec détails
ps aux | grep python    # Filtrer les processus
top                     # Visualiseur interactif des processus
htop                    # Version améliorée de top (si installée)
kill PID                # Terminer un processus
kill -9 PID             # Forcer l'arrêt
killall process_name    # Tuer par nom
pkill pattern           # Tuer par motif
nice -n 10 command      # Exécuter avec une priorité plus faible
renice 10 -p PID        # Changer la priorité d'un processus en cours
bg                      # Reprendre une tâche en arrière-plan
fg                      # Ramener une tâche au premier plan
jobs                    # Lister les tâches en arrière-plan
Ctrl+Z                  # Suspendre la tâche actuelle
```

---

## Informations système

```bash
uname -a                # Informations système
uname -r                # Version du noyau
hostname                # Afficher le nom d'hôte
whoami                  # Utilisateur actuel
id                      # IDs utilisateur et groupe
uptime                  # Temps de fonctionnement et charge
date                    # Date/heure actuelle
cal                     # Calendrier
df -h                   # Espace disque (lisible)
du -sh directory        # Taille du répertoire
free -h                 # Utilisation mémoire
lscpu                   # Informations CPU
lsblk                   # Périphériques bloc
fdisk -l                # Partitions disque (nécessite sudo)
```

---

## Commandes réseau

```bash
ifconfig                # Interfaces réseau (obsolète)
ip addr show            # Adresses IP (moderne)
ip route show           # Table de routage
ping google.com         # Tester la connectivité
traceroute google.com   # Tracer le chemin réseau
tracepath google.com    # Alternative à traceroute
netstat -tulpn          # Ports en écoute (obsolète)
ss -tulpn               # Statistiques des sockets (moderne)
dig domain.com          # Recherche DNS
nslookup domain.com     # Recherche DNS (plus ancien)
curl http://example.com # Requête HTTP
wget http://file.url    # Télécharger un fichier
ssh user@host           # Connexion SSH
scp file user@host:path # Copie sécurisée
rsync -av src/ dest/    # Synchroniser des fichiers/répertoires
```

---

## Archive et compression

```bash
tar -cvf archive.tar file1 file2        # Créer une archive tar
tar -xvf archive.tar                    # Extraire une archive tar
tar -czvf archive.tar.gz dir/           # Créer un tar gzippé
tar -xzvf archive.tar.gz                # Extraire un tar gzippé
tar -cjvf archive.tar.bz2 dir/          # Créer un tar bzip2
tar -xjvf archive.tar.bz2               # Extraire un tar bzip2
gzip file.txt                           # Compresser un fichier
gunzip file.txt.gz                      # Décompresser un fichier
zip -r archive.zip dir/                 # Créer une archive zip
unzip archive.zip                       # Extraire une archive zip
```

---

## Gestion des paquets

### Debian/Ubuntu (apt)
```bash
sudo apt update                         # Mettre à jour la liste des paquets
sudo apt upgrade                        # Mettre à niveau les paquets
sudo apt install package_name           # Installer un paquet
sudo apt remove package_name            # Supprimer un paquet
sudo apt purge package_name             # Supprimer avec la configuration
sudo apt search keyword                 # Rechercher des paquets
sudo apt show package_name              # Détails du paquet
```

### RHEL/CentOS (yum/dnf)
```bash
sudo yum update                         # Mettre à jour les paquets
sudo yum install package_name           # Installer un paquet
sudo yum remove package_name            # Supprimer un paquet
sudo yum search keyword                 # Rechercher des paquets
```

### macOS (brew)
```bash
brew update                             # Mettre à jour brew
brew upgrade                            # Mettre à niveau les paquets
brew install package_name               # Installer un paquet
brew uninstall package_name             # Supprimer un paquet
brew search keyword                     # Rechercher des paquets
brew list                               # Lister les paquets installés
```

---

## Gestion des utilisateurs

```bash
sudo adduser username                   # Créer un nouvel utilisateur
sudo deluser username                   # Supprimer un utilisateur
sudo usermod -aG group username         # Ajouter un utilisateur à un groupe
passwd username                         # Changer le mot de passe d'un utilisateur
sudo passwd username                    # Changer le mot de passe d'un autre utilisateur
su - username                           # Changer d'utilisateur
sudo command                            # Exécuter en tant que root
groups username                         # Afficher les groupes de l'utilisateur
```

---

## Gestion des disques

```bash
mount /dev/sda1 /mnt                    # Monter un système de fichiers
umount /mnt                             # Démonter un système de fichiers
lsblk                                   # Lister les périphériques bloc
blkid                                   # Afficher les attributs des périphériques bloc
mkfs.ext4 /dev/sda1                     # Formater en ext4
fsck /dev/sda1                          # Vérifier le système de fichiers
dd if=/dev/sda of=backup.img            # Image disque (prudence !)
```

---

## Variables du shell et environnement

```bash
echo $HOME              # Afficher une variable d'environnement
export VAR=value        # Définir une variable d'environnement
env                     # Lister toutes les variables d'environnement
unset VAR               # Supprimer une variable
alias ll='ls -la'       # Créer un alias
unalias ll              # Supprimer un alias
history                 # Historique des commandes
!123                    # Exécuter la commande n°123 depuis l'historique
!!                      # Exécuter la dernière commande
!$                      # Dernier argument de la commande précédente
Ctrl+R                  # Rechercher dans l'historique
```

---

## Redirection d'entrée/sortie

```bash
command > file.txt      # Rediriger la sortie (écrasement)
command >> file.txt     # Rediriger la sortie (ajout)
command < file.txt      # Rediriger l'entrée
command 2> error.log    # Rediriger stderr
command &> all.log      # Rediriger stdout et stderr
command | grep pattern  # Envoyer la sortie vers une autre commande
tee file.txt            # Écrire dans un fichier et à l'écran
```

---

## Commandes en une ligne utiles

```bash
# Compter les fichiers dans le répertoire
ls -1 | wc -l

# Trouver les plus gros fichiers
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -10

# Vérifier quel processus utilise un port
lsof -i :8080

# Surveiller les changements de fichiers
watch -n 1 'ls -la'

# Extraire les IP uniques d'un log
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log | sort -u

# Sauvegarde horodatée
tar -czf backup_$(date +%Y%m%d).tar.gz /path/to/backup

# Trouver et supprimer les anciens fichiers
find /path -type f -mtime +30 -delete

# Vérifier les gros consommateurs d'espace disque
du -ah | sort -hr | head -20
```

---

## Raccourcis clavier

| Raccourci | Action |
|----------|--------|
| `Tab` | Auto-complétion |
| `Ctrl+C` | Tuer la commande actuelle |
| `Ctrl+Z` | Suspendre la commande |
| `Ctrl+D` | Quitter le shell/EOF |
| `Ctrl+L` | Effacer l'écran |
| `Ctrl+A` | Aller au début de la ligne |
| `Ctrl+E` | Aller à la fin de la ligne |
| `Ctrl+U` | Supprimer jusqu'au début de la ligne |
| `Ctrl+K` | Supprimer jusqu'à la fin de la ligne |
| `Ctrl+R` | Rechercher dans l'historique |
| `Ctrl+W` | Supprimer le mot avant le curseur |

---

## Bonnes pratiques

✅ **À faire :**
- Utiliser `sudo` avec parcimonie et prudence
- Tester d'abord les commandes destructrices sans les options d'exécution
- Conserver des sauvegardes avant les modifications importantes
- Utiliser des noms de fichiers explicites (sans espaces)
- Apprendre à utiliser les pages `man` (`man command`)

❌ **À éviter :**
- Exécuter `rm -rf /` ou des commandes dangereuses similaires
- Utiliser `chmod 777` sur des fichiers sensibles
- Ignorer les messages d'avertissement
- Modifier des fichiers système sans sauvegardes
- Exécuter des scripts inconnus en tant que root

---

*Dernière mise à jour : juin 2025 | Compatible Linux/Unix*
