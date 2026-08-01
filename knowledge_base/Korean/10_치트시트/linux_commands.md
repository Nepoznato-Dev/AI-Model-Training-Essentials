<!-- 
This file was automatically translated from English to Korean.
Source: linux_commands.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Linux 명령어 빠른 참조

시스템 탐색과 관리를 위해 자주 쓰는 Linux/Unix 명령어를 한곳에 정리한 문서입니다.

---

## 파일 및 디렉터리 작업

### 탐색
```bash
pwd                     # Print working directory
ls                      # List files
ls -la                  # List all files (including hidden) with details
ls -lh                  # Human-readable sizes
cd /path/to/dir         # Change directory
cd ..                   # Go up one directory
cd ~                    # Go to home directory
cd -                    # Go to previous directory
```

### 파일 작업
```bash
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

### 파일 보기
```bash
cat file.txt            # Display entire file
less file.txt           # View file page by page (q to quit)
head file.txt           # First 10 lines
head -n 20 file.txt     # First 20 lines
tail file.txt           # Last 10 lines
tail -n 20 file.txt     # Last 20 lines
tail -f logfile.log     # Follow file (live updates)
```

---

## 파일 권한

```bash
chmod 755 file          # Set permissions (rwxr-xr-x)
chmod +x script.sh      # Make executable
chmod -R 755 dir        # Recursive permission change
chown user:group file   # Change owner and group
chown user file         # Change owner only
chgrp group file        # Change group only
umask                   # Show default permission mask
```

### 권한 숫자
- `7` = rwx (read + write + execute)
- `6` = rw- (read + write)
- `5` = r-x (read + execute)
- `4` = r-- (read only)

---

## 텍스트 처리

### 검색 및 치환
```bash
grep "pattern" file.txt                 # Search for pattern
grep -r "pattern" dir/                  # Recursive search
grep -i "pattern" file.txt              # Case-insensitive
grep -v "pattern" file.txt              # Inverse match
grep -l "pattern" *.txt                 # List matching files
grep -c "pattern" file.txt              # Count matches
grep -E "pattern1|pattern2" file.txt    # Extended regex
```

### 파일 찾기
```bash
find /path -name "file.txt"             # Find by name
find /path -name "*.py"                 # Find by extension
find /path -type d                      # Find directories
find /path -type f                      # Find files
find /path -size +100M                  # Files larger than 100MB
find /path -mtime -7                    # Modified in last 7 days
find /path -perm 755                    # Find by permissions
find /path -exec command {} \;          # Execute command on results
```

### 텍스트 조작
```bash
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

## 프로세스 관리

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

## 시스템 정보

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

## 네트워크 명령

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

## 압축 및 보관

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

## 패키지 관리

### Debian/Ubuntu (apt)
```bash
sudo apt update                         # Update package list
sudo apt upgrade                        # Upgrade packages
sudo apt install package_name           # Install package
sudo apt remove package_name            # Remove package
sudo apt purge package_name             # Remove with config
sudo apt search keyword                 # Search packages
sudo apt show package_name              # Package details
```

### RHEL/CentOS (yum/dnf)
```bash
sudo yum update                         # Update packages
sudo yum install package_name           # Install package
sudo yum remove package_name            # Remove package
sudo yum search keyword                 # Search packages
```

### macOS (brew)
```bash
brew update                             # Update brew
brew upgrade                            # Upgrade packages
brew install package_name               # Install package
brew uninstall package_name             # Remove package
brew search keyword                     # Search packages
brew list                               # List installed packages
```

---

## 사용자 관리

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

## 디스크 관리

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

## 셸 변수 및 환경 변수

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

## 입출력 리디렉션

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

## 유용한 한 줄 명령

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

## 키보드 단축키

| 단축키 | 동작 |
|----------|--------|
| `Tab` | 자동 완성 |
| `Ctrl+C` | 현재 명령 종료 |
| `Ctrl+Z` | 명령 일시 중단 |
| `Ctrl+D` | 셸 종료/EOF |
| `Ctrl+L` | 화면 지우기 |
| `Ctrl+A` | 줄의 시작으로 이동 |
| `Ctrl+E` | 줄의 끝으로 이동 |
| `Ctrl+U` | 줄 시작까지 삭제 |
| `Ctrl+K` | 줄 끝까지 삭제 |
| `Ctrl+R` | 기록 검색 |
| `Ctrl+W` | 커서 앞 단어 삭제 |

---

## 모범 사례

✅ **권장 사항:**
- `sudo`는 꼭 필요할 때만 신중하게 사용합니다.
- 파괴적인 명령은 실제 실행 전에 먼저 안전한 옵션으로 확인합니다.
- 큰 변경을 하기 전에는 항상 백업을 준비합니다.
- 의미 있는 파일명을 사용하고 공백은 가능하면 피합니다.
- `man` 페이지(`man command`)를 활용해 명령어 사용법을 익힙니다.

❌ **주의할 점:**
- `rm -rf /` 같은 위험한 명령은 실행하지 않습니다.
- 민감한 파일에 `chmod 777`을 사용하지 않습니다.
- 경고 메시지를 무시하지 않습니다.
- 백업 없이 시스템 파일을 편집하지 않습니다.
- 출처를 모르는 스크립트를 root 권한으로 실행하지 않습니다.

---

*최종 업데이트: 2025년 6월 | Linux/Unix 호환*
