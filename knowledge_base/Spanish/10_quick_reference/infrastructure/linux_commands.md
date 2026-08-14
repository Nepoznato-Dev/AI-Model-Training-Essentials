---
# Metadata
title: "Linux Commands Quick Reference"
description: "Linux command line reference"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [linux, commands, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Referencia rápida de comandos de Linux
Comandos esenciales de Linux/Unix para la navegación y administración del sistema.
---

## Operaciones de archivos y directorios
### Navegación```bash
pwd                     # Print working directory
ls                      # List files
ls -la                  # List all files (including hidden) with details
ls -lh                  # Human-readable sizes
cd /path/to/dir         # Change directory
cd ..                   # Go up one directory
cd ~                    # Go to home directory
cd -                    # Go to previous directory
```

### Operaciones de archivos```bash
touch file.txt          # Create empty file
cp source dest          # Copy file
cp -r dir1 dir2         # Copy directory recursively
mv old new              # Move/rename file
rm file.txt             # Remove file
rm -r directory         # Remove directory recursively
rm -f file              # Force remove (no prompt)
rm -rf directory        # Force remove directory (DANGEROUS)
mkdir newdir            # Create directory
mkdir -p path/to/dir    # Create nested directories
ln -s target link       # Create symbolic link
```

### Ver archivos```bash
cat file.txt            # Display entire file
less file.txt           # View file page by page (q to quit)
head file.txt           # First 10 lines
head -n 20 file.txt     # First 20 lines
tail file.txt           # Last 10 lines
tail -n 20 file.txt     # Last 20 lines
tail -f logfile.log     # Follow file (live updates)
```

---

## Permisos de archivos
```bash
chmod 755 file          # Set permissions (rwxr-xr-x)
chmod +x script.sh      # Make executable
chmod -R 755 dir        # Recursive permission change
chown user:group file   # Change owner and group
chown user file         # Change owner only
chgrp group file        # Change group only
umask                   # Show default permission mask
```

### Números de permiso
-`7`= rwx (leer + escribir + ejecutar)
-`6`= rw- (lectura + escritura)
-`5`= r-x (leer + ejecutar)
-`4`= r-- (solo lectura)
---

## Procesamiento de texto
### Buscar y reemplazar```bash
grep "pattern" file.txt                 # Search for pattern
grep -r "pattern" dir/                  # Recursive search
grep -i "pattern" file.txt              # Case-insensitive
grep -v "pattern" file.txt              # Inverse match
grep -l "pattern" *.txt                 # List matching files
grep -c "pattern" file.txt              # Count matches
grep -E "pattern1|pattern2" file.txt    # Extended regex
```

### Buscar archivos```bash
find /path -name "file.txt"             # Find by name
find /path -name "*.py"                 # Find by extension
find /path -type d                      # Find directories
find /path -type f                      # Find files
find /path -size +100M                  # Files larger than 100MB
find /path -mtime -7                    # Modified in last 7 days
find /path -perm 755                    # Find by permissions
find /path -exec command {} \;          # Execute command on results
```

### Manipulación de texto```bash
wc file.txt             # Word count (lines, words, bytes)
wc -l file.txt          # Line count only
sort file.txt           # Sort lines
sort -n file.txt        # Numeric sort
sort -r file.txt        # Reverse sort
uniq file.txt           # Remove adjacent duplicates
uniq -c file.txt        # Count occurrences
cut -d: -f1 /etc/passwd # Cut fields by delimiter
paste file1 file2       # Merge files side by side
tr 'a-z' 'A-Z' < file   # Translate characters
sed 's/old/new/g' file  # Replace text
awk '{print $1}' file   # Print first column
```

---

## Gestión de procesos
```bash
ps                      # Show running processes
ps aux                  # All processes with details
ps aux | grep python    # Filter processes
top                     # Interactive process viewer
htop                    # Enhanced top (if installed)
kill PID                # Terminate process
kill -9 PID             # Force kill
killall process_name    # Kill by name
pkill pattern           # Kill by pattern
nice -n 10 command      # Run with lower priority
renice 10 -p PID        # Change priority of running process
bg                      # Resume job in background
fg                      # Bring job to foreground
jobs                    # List background jobs
Ctrl+Z                  # Suspend current job
```

---

## Información del sistema
```bash
uname -a                # System information
uname -r                # Kernel version
hostname                # Show hostname
whoami                  # Current user
id                      # User and group IDs
uptime                  # System uptime and load
date                    # Current date/time
cal                     # Calendar
df -h                   # Disk space (human-readable)
du -sh directory        # Directory size
free -h                 # Memory usage
lscpu                   # CPU information
lsblk                   # Block devices
fdisk -l                # Disk partitions (requires sudo)
```

---

## Comandos de red
```bash
ifconfig                # Network interfaces (deprecated)
ip addr show            # IP addresses (modern)
ip route show           # Routing table
ping google.com         # Test connectivity
traceroute google.com   # Trace network path
tracepath google.com    # Alternative traceroute
netstat -tulpn          # Listening ports (deprecated)
ss -tulpn               # Socket statistics (modern)
dig domain.com          # DNS lookup
nslookup domain.com     # DNS lookup (older)
curl http://example.com # HTTP request
wget http://file.url    # Download file
ssh user@host           # SSH connection
scp file user@host:path # Secure copy
rsync -av src/ dest/    # Sync files/directories
```

---

## Archivo y compresión
```bash
tar -cvf archive.tar file1 file2        # Create tar archive
tar -xvf archive.tar                    # Extract tar archive
tar -czvf archive.tar.gz dir/           # Create gzipped tar
tar -xzvf archive.tar.gz                # Extract gzipped tar
tar -cjvf archive.tar.bz2 dir/          # Create bzip2 tar
tar -xjvf archive.tar.bz2               # Extract bzip2 tar
gzip file.txt                           # Compress file
gunzip file.txt.gz                      # Decompress file
zip -r archive.zip dir/                 # Create zip archive
unzip archive.zip                       # Extract zip archive
```

---

## Gestión de paquetes
### Debian/Ubuntu (apto)```bash
sudo apt update                         # Update package list
sudo apt upgrade                        # Upgrade packages
sudo apt install package_name           # Install package
sudo apt remove package_name            # Remove package
sudo apt purge package_name             # Remove with config
sudo apt search keyword                 # Search packages
sudo apt show package_name              # Package details
```

### RHEL/CentOS (yum/dnf)```bash
sudo yum update                         # Update packages
sudo yum install package_name           # Install package
sudo yum remove package_name            # Remove package
sudo yum search keyword                 # Search packages
```

### macOS (brebaje)```bash
brew update                             # Update brew
brew upgrade                            # Upgrade packages
brew install package_name               # Install package
brew uninstall package_name             # Remove package
brew search keyword                     # Search packages
brew list                               # List installed packages
```

---

## Gestión de usuarios
```bash
sudo adduser username                   # Create new user
sudo deluser username                   # Delete user
sudo usermod -aG group username         # Add user to group
passwd username                         # Change user password
sudo passwd username                    # Change another's password
su - username                           # Switch user
sudo command                            # Run as root
groups username                         # Show user groups
```

---

## Gestión de discos
```bash
mount /dev/sda1 /mnt                    # Mount filesystem
umount /mnt                             # Unmount filesystem
lsblk                                   # List block devices
blkid                                   # Show block device attributes
mkfs.ext4 /dev/sda1                     # Format as ext4
fsck /dev/sda1                          # Check filesystem
dd if=/dev/sda of=backup.img            # Disk image (careful!)
```

---

## Variables de Shell y entorno
```bash
echo $HOME              # Show environment variable
export VAR=value        # Set environment variable
env                     # List all environment variables
unset VAR               # Remove variable
alias ll='ls -la'       # Create alias
unalias ll              # Remove alias
history                 # Command history
!123                    # Run command #123 from history
!!                      # Run last command
!$                      # Last argument of previous command
Ctrl+R                  # Search history
```

---

## Redirección de entrada/salida
```bash
command > file.txt      # Redirect output (overwrite)
command >> file.txt     # Redirect output (append)
command < file.txt      # Redirect input
command 2> error.log    # Redirect stderr
command &> all.log      # Redirect stdout and stderr
command | grep pattern  # Pipe output to another command
tee file.txt            # Output to file and screen
```

---

## Frases útiles
```bash
# Count files in directory
ls -1 | wc -l

# Find largest files
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -10

# Check which process uses a port
lsof -i :8080

# Monitor file changes
watch -n 1 'ls -la'

# Extract unique IPs from log
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log | sort -u

# Backup with timestamp
tar -czf backup_$(date +%Y%m%d).tar.gz /path/to/backup

# Find and delete old files
find /path -type f -mtime +30 -delete

# Check disk hogs
du -ah | sort -hr | head -20
```

---

## Atajos de teclado
| Atajo | Acción |
|----------|--------|
| `Tab`| Autocompletar |
| `Ctrl+C`| Matar el comando actual |
| `Ctrl+Z`| Suspender comando |
| `Ctrl+D`| Salir del caparazón/EOF |
| `Ctrl+L`| Borrar pantalla |
| `Ctrl+A`| Ir al inicio de la línea |
| `Ctrl+E`| Ir al final de la línea |
| `Ctrl+U`| Eliminar al inicio de la línea |
| `Ctrl+K`| Eliminar al final de la línea |
| `Ctrl+R`| Historial de búsqueda |
| `Ctrl+W`| Eliminar palabra antes del cursor |
---

## Mejores prácticas
✅ **Hacer:**
- Utilice`sudo`con moderación y cuidado
- Pruebe primero los comandos destructivos sin indicadores de ejecución
- Mantenga copias de seguridad antes de cambios importantes.
- Utilice nombres de archivos significativos (sin espacios)
- Aprenda a utilizar las páginas`man`(`man command`)
❌ **No:**
- Ejecute`rm -rf /`o comandos peligrosos similares
- Utilice`chmod 777`en archivos confidenciales
- Ignorar mensajes de advertencia
- Editar archivos del sistema sin copias de seguridad
- Ejecutar scripts desconocidos como root
---

*Última actualización: julio de 2026 | Compatible con Linux/Unix*