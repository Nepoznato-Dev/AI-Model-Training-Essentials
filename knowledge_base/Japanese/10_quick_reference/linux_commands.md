---
# Metadata
title: "Linux Commands Quick Reference"
description: "Linux command line reference"
category: "Quick Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
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

# Linux コマンドのクイック リファレンス
システムのナビゲーションと管理に不可欠な Linux/Unix コマンド。
---

## ファイルとディレクトリの操作
### ナビゲーション```bash
pwd                     # Print working directory
ls                      # List files
ls -la                  # List all files (including hidden) with details
ls -lh                  # Human-readable sizes
cd /path/to/dir         # Change directory
cd ..                   # Go up one directory
cd ~                    # Go to home directory
cd -                    # Go to previous directory
```

### ファイル操作```bash
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

### ファイルの表示```bash
cat file.txt            # Display entire file
less file.txt           # View file page by page (q to quit)
head file.txt           # First 10 lines
head -n 20 file.txt     # First 20 lines
tail file.txt           # Last 10 lines
tail -n 20 file.txt     # Last 20 lines
tail -f logfile.log     # Follow file (live updates)
```

---

## ファイルのアクセス許可
```bash
chmod 755 file          # Set permissions (rwxr-xr-x)
chmod +x script.sh      # Make executable
chmod -R 755 dir        # Recursive permission change
chown user:group file   # Change owner and group
chown user file         # Change owner only
chgrp group file        # Change group only
umask                   # Show default permission mask
```

### 許可番号
-`7`= rwx (読み取り + 書き込み + 実行)
-`6`= rw- (読み取り + 書き込み)
-`5`= r-x (読み取り + 実行)
-`4`= r-- (読み取り専用)
---

## テキスト処理
### 検索と置換```bash
grep "pattern" file.txt                 # Search for pattern
grep -r "pattern" dir/                  # Recursive search
grep -i "pattern" file.txt              # Case-insensitive
grep -v "pattern" file.txt              # Inverse match
grep -l "pattern" *.txt                 # List matching files
grep -c "pattern" file.txt              # Count matches
grep -E "pattern1|pattern2" file.txt    # Extended regex
```

### ファイルの検索```bash
find /path -name "file.txt"             # Find by name
find /path -name "*.py"                 # Find by extension
find /path -type d                      # Find directories
find /path -type f                      # Find files
find /path -size +100M                  # Files larger than 100MB
find /path -mtime -7                    # Modified in last 7 days
find /path -perm 755                    # Find by permissions
find /path -exec command {} \;          # Execute command on results
```

### テキストの操作```bash
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

## プロセス管理
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

## システム情報
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

## ネットワークコマンド
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

## アーカイブと圧縮
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

## パッケージ管理
### Debian/Ubuntu (apt)```bash
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

### macOS (ブリュー)```bash
brew update                             # Update brew
brew upgrade                            # Upgrade packages
brew install package_name               # Install package
brew uninstall package_name             # Remove package
brew search keyword                     # Search packages
brew list                               # List installed packages
```

---

## ユーザー管理
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

## ディスク管理
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

## シェル変数と環境
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

## 入力/出力リダイレクト
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

## 便利なワンライナー
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

## キーボード ショートカット
|ショートカット |アクション |
|----------|----------|
| `Tab`|オートコンプリート |
| `Ctrl+C`|現在のコマンドを強制終了 |
| `Ctrl+Z`|一時停止コマンド |
| `Ctrl+D`|シェルを終了/EOF |
| `Ctrl+L`|画面をクリア |
| `Ctrl+A`|行頭へ移動 |
| `Ctrl+E`|行末に移動 |
| `Ctrl+U`|行頭まで削除 |
| `Ctrl+K`|行末まで削除 |
| `Ctrl+R`|検索履歴 |
| `Ctrl+W`|カーソルの前の単語を削除 |
---

## ベストプラクティス
✅ **実行してください:**
-`sudo`は慎重かつ控えめに使用してください
- 最初に実行フラグなしで破壊的なコマンドをテストします。
- 大きな変更を加える前にバックアップを取っておく
- 意味のあるファイル名を使用してください (スペースは含まれません)
-`man`ページの使い方を学ぶ (`man command`)
❌ **してはいけないこと:**
-`rm -rf /`または同様の危険なコマンドを実行する
- 機密ファイルには`chmod 777`を使用します
- 警告メッセージを無視する
- バックアップなしでシステムファイルを編集
- 不明なスクリプトを root として実行する
---

*最終更新日: 2026 年 7 月 | Linux/Unix 互換*