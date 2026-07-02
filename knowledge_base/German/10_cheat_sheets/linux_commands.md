# Linux-Befehle Kurzübersicht

Wesentliche Linux/Unix-Befehle für Systemnavigation und -verwaltung.

---

## Datei- & Verzeichnisoperationen

### Navigation
```bash
pwd                     # Arbeitsverzeichnis ausgeben
ls                      # Dateien auflisten
ls -la                  # Alle Dateien (einschließlich versteckter) mit Details auflisten
ls -lh                  # Menschlich lesbare Größen
cd /path/to/dir         # Verzeichnis wechseln
cd ..                   # Eine Ebene nach oben gehen
cd ~                    # Zum Home-Verzeichnis gehen
cd -                    # Zum vorherigen Verzeichnis gehen
```

### Dateioperationen
```bash
touch file.txt          # Leere Datei erstellen
cp source dest          # Datei kopieren
cp -r dir1 dir2         # Verzeichnis rekursiv kopieren
mv old new              # Datei verschieben/umbenennen
rm file.txt             # Datei entfernen
rm -r directory         # Verzeichnis rekursiv entfernen
rm -f file              # Erzwingt Entfernen (ohne Nachfrage)
rm -rf directory        # Verzeichnis zwangsweise entfernen (GEFÄHRLICH)
mkdir newdir            # Verzeichnis erstellen
mkdir -p path/to/dir    # Verschachtelte Verzeichnisse erstellen
ln -s target link       # Symbolischen Link erstellen
```

### Dateien anzeigen
```bash
cat file.txt            # Gesamte Datei anzeigen
less file.txt           # Datei seitenweise anzeigen (q zum Beenden)
head file.txt           # Erste 10 Zeilen
head -n 20 file.txt     # Erste 20 Zeilen
tail file.txt           # Letzte 10 Zeilen
tail -n 20 file.txt     # Letzte 20 Zeilen
tail -f logfile.log     # Datei verfolgen (Live-Updates)
```

---

## Dateiberechtigungen

```bash
chmod 755 file          # Berechtigungen setzen (rwxr-xr-x)
chmod +x script.sh      # Ausführbar machen
chmod -R 755 dir        # Rekursive Berechtigungsänderung
chown user:group file   # Eigentümer und Gruppe ändern
chown user file         # Nur Eigentümer ändern
chgrp group file        # Nur Gruppe ändern
umask                   # Standard-Berechtigungsmaske anzeigen
```

### Berechtigungszahlen
- `7` = rwx (lesen + schreiben + ausführen)
- `6` = rw- (lesen + schreiben)
- `5` = r-x (lesen + ausführen)
- `4` = r-- (nur lesen)

---

## Textverarbeitung

### Suchen & Ersetzen
```bash
grep "pattern" file.txt                 # Nach Muster suchen
grep -r "pattern" dir/                  # Rekursiv suchen
grep -i "pattern" file.txt              # Groß-/Kleinschreibung ignorieren
grep -v "pattern" file.txt              # Umgekehrter Treffer
grep -l "pattern" *.txt                 # Passende Dateien auflisten
grep -c "pattern" file.txt              # Treffer zählen
grep -E "pattern1|pattern2" file.txt    # Erweiterter Regex
```

### Dateien finden
```bash
find /path -name "file.txt"             # Nach Namen suchen
find /path -name "*.py"                 # Nach Dateiendung suchen
find /path -type d                      # Verzeichnisse finden
find /path -type f                      # Dateien finden
find /path -size +100M                  # Dateien größer als 100MB
find /path -mtime -7                    # In den letzten 7 Tagen geändert
find /path -perm 755                    # Nach Berechtigungen suchen
find /path -exec command {} \;          # Befehl auf Ergebnisse ausführen
```

### Textmanipulation
```bash
wc file.txt             # Wortanzahl (Zeilen, Wörter, Bytes)
wc -l file.txt          # Nur Zeilen zählen
sort file.txt           # Zeilen sortieren
sort -n file.txt        # Numerisch sortieren
sort -r file.txt        # Umgekehrt sortieren
uniq file.txt           # Benachbarte Duplikate entfernen
uniq -c file.txt        # Vorkommen zählen
cut -d: -f1 /etc/passwd # Felder nach Trennzeichen ausschneiden
paste file1 file2       # Dateien nebeneinander zusammenführen
tr 'a-z' 'A-Z' < file   # Zeichen umwandeln
sed 's/old/new/g' file  # Text ersetzen
awk '{print $1}' file   # Erste Spalte ausgeben
```

---

## Prozessverwaltung

```bash
ps                      # Laufende Prozesse anzeigen
ps aux                  # Alle Prozesse mit Details
ps aux | grep python    # Prozesse filtern
top                     # Interaktive Prozessansicht
htop                    # Erweiterte top-Ansicht (falls installiert)
kill PID                # Prozess beenden
kill -9 PID             # Erzwingt Beenden
killall process_name    # Nach Name beenden
pkill pattern           # Nach Muster beenden
nice -n 10 command      # Mit niedrigerer Priorität ausführen
renice 10 -p PID        # Priorität eines laufenden Prozesses ändern
bg                      # Job im Hintergrund fortsetzen
fg                      # Job in den Vordergrund holen
jobs                    # Hintergrund-Jobs auflisten
Ctrl+Z                  # Aktuellen Job anhalten
```

---

## Systeminformationen

```bash
uname -a                # Systeminformationen
uname -r                # Kernel-Version
hostname                # Hostname anzeigen
whoami                  # Aktueller Benutzer
id                      # Benutzer- und Gruppen-IDs
uptime                  # Systemlaufzeit und Last
date                    # Aktuelles Datum/Uhrzeit
cal                     # Kalender
df -h                   # Speicherplatz (menschlich lesbar)
du -sh directory        # Verzeichnisgröße
free -h                 # Speichernutzung
lscpu                   # CPU-Informationen
lsblk                   # Blockgeräte
fdisk -l                # Festplattenpartitionen (erfordert sudo)
```

---

## Netzwerkbefehle

```bash
ifconfig                # Netzwerkschnittstellen (veraltet)
ip addr show            # IP-Adressen (modern)
ip route show           # Routing-Tabelle
ping google.com         # Konnektivität testen
traceroute google.com   # Netzwerkpfad verfolgen
tracepath google.com    # Alternative zu traceroute
netstat -tulpn          # Lauschende Ports (veraltet)
ss -tulpn               # Socket-Statistiken (modern)
dig domain.com          # DNS-Abfrage
nslookup domain.com     # DNS-Abfrage (älter)
curl http://example.com # HTTP-Anfrage
wget http://file.url    # Datei herunterladen
ssh user@host           # SSH-Verbindung
scp file user@host:path # Sichere Kopie
rsync -av src/ dest/    # Dateien/Verzeichnisse synchronisieren
```

---

## Archivierung & Komprimierung

```bash
tar -cvf archive.tar file1 file2        # tar-Archiv erstellen
tar -xvf archive.tar                    # tar-Archiv entpacken
tar -czvf archive.tar.gz dir/           # Gzip-komprimiertes tar erstellen
tar -xzvf archive.tar.gz                # Gzip-komprimiertes tar entpacken
tar -cjvf archive.tar.bz2 dir/          # bzip2-komprimiertes tar erstellen
tar -xjvf archive.tar.bz2               # bzip2-komprimiertes tar entpacken
gzip file.txt                           # Datei komprimieren
gunzip file.txt.gz                      # Datei dekomprimieren
zip -r archive.zip dir/                 # zip-Archiv erstellen
unzip archive.zip                       # zip-Archiv entpacken
```

---

## Paketverwaltung

### Debian/Ubuntu (apt)
```bash
sudo apt update                         # Paketliste aktualisieren
sudo apt upgrade                        # Pakete aktualisieren
sudo apt install package_name           # Paket installieren
sudo apt remove package_name            # Paket entfernen
sudo apt purge package_name             # Mit Konfiguration entfernen
sudo apt search keyword                 # Pakete suchen
sudo apt show package_name              # Paketdetails
```

### RHEL/CentOS (yum/dnf)
```bash
sudo yum update                         # Pakete aktualisieren
sudo yum install package_name           # Paket installieren
sudo yum remove package_name            # Paket entfernen
sudo yum search keyword                 # Pakete suchen
```

### macOS (brew)
```bash
brew update                             # brew aktualisieren
brew upgrade                            # Pakete aktualisieren
brew install package_name               # Paket installieren
brew uninstall package_name             # Paket entfernen
brew search keyword                     # Pakete suchen
brew list                               # Installierte Pakete auflisten
```

---

## Benutzerverwaltung

```bash
sudo adduser username                   # Neuen Benutzer erstellen
sudo deluser username                   # Benutzer löschen
sudo usermod -aG group username         # Benutzer zu Gruppe hinzufügen
passwd username                         # Benutzerpasswort ändern
sudo passwd username                    # Passwort eines anderen ändern
su - username                           # Benutzer wechseln
sudo command                            # Als root ausführen
groups username                         # Benutzergruppen anzeigen
```

---

## Datenträgerverwaltung

```bash
mount /dev/sda1 /mnt                    # Dateisystem einhängen
umount /mnt                             # Dateisystem aushängen
lsblk                                   # Blockgeräte auflisten
blkid                                   # Attribute von Blockgeräten anzeigen
mkfs.ext4 /dev/sda1                     # Als ext4 formatieren
fsck /dev/sda1                          # Dateisystem prüfen
dd if=/dev/sda of=backup.img            # Datenträgerabbild (vorsichtig!)
```

---

## Shell-Variablen & Umgebung

```bash
echo $HOME              # Umgebungsvariable anzeigen
export VAR=value        # Umgebungsvariable setzen
env                     # Alle Umgebungsvariablen auflisten
unset VAR               # Variable entfernen
alias ll='ls -la'       # Alias erstellen
unalias ll              # Alias entfernen
history                 # Befehlsverlauf
!123                    # Befehl #123 aus dem Verlauf ausführen
!!                      # Letzten Befehl ausführen
!$                      # Letztes Argument des vorherigen Befehls
Ctrl+R                  # Verlauf durchsuchen
```

---

## Ein-/Ausgabeumleitung

```bash
command > file.txt      # Ausgabe umleiten (überschreiben)
command >> file.txt     # Ausgabe umleiten (anhängen)
command < file.txt      # Eingabe umleiten
command 2> error.log    # stderr umleiten
command &> all.log      # stdout und stderr umleiten
command | grep pattern  # Ausgabe in anderen Befehl pipen
tee file.txt            # Ausgabe in Datei und auf Bildschirm
```

---

## Nützliche Einzeiler

```bash
# Dateien im Verzeichnis zählen
ls -1 | wc -l

# Größte Dateien finden
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -10

# Prüfen, welcher Prozess einen Port verwendet
lsof -i :8080

# Dateiänderungen überwachen
watch -n 1 'ls -la'

# Eindeutige IPs aus Log extrahieren
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log | sort -u

# Backup mit Zeitstempel
tar -czf backup_$(date +%Y%m%d).tar.gz /path/to/backup

# Alte Dateien finden und löschen
find /path -type f -mtime +30 -delete

# Speicherfresser prüfen
du -ah | sort -hr | head -20
```

---

## Tastenkombinationen

| Shortcut | Aktion |
|----------|--------|
| `Tab` | Automatisch vervollständigen |
| `Ctrl+C` | Aktuellen Befehl beenden |
| `Ctrl+Z` | Befehl anhalten |
| `Ctrl+D` | Shell/EOF beenden |
| `Ctrl+L` | Bildschirm löschen |
| `Ctrl+A` | Zum Zeilenanfang gehen |
| `Ctrl+E` | Zum Zeilenende gehen |
| `Ctrl+U` | Bis zum Zeilenanfang löschen |
| `Ctrl+K` | Bis zum Zeilenende löschen |
| `Ctrl+R` | Verlauf durchsuchen |
| `Ctrl+W` | Wort vor dem Cursor löschen |

---

## Best Practices

✅ **Tun:**
- Verwenden Sie `sudo` sparsam und vorsichtig
- Testen Sie zerstörerische Befehle zuerst ohne Ausführungs-Flags
- Erstellen Sie Backups vor größeren Änderungen
- Verwenden Sie aussagekräftige Dateinamen (keine Leerzeichen)
- Lernen Sie den Umgang mit `man`-Seiten (`man command`)

❌ **Nicht tun:**
- `rm -rf /` oder ähnliche gefährliche Befehle ausführen
- `chmod 777` auf sensible Dateien anwenden
- Warnmeldungen ignorieren
- Systemdateien ohne Backups bearbeiten
- Unbekannte Skripte als root ausführen

---

*Zuletzt aktualisiert: Juni 2025 | Linux/Unix-kompatibel*
