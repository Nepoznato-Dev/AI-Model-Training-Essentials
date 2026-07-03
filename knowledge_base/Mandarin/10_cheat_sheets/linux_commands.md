# Linux 指令快速參考

系統導覽和管理的必備 Linux/Unix 指令。

---

## 檔案與目錄操作

### 導覽
```bash
pwd                     # 印出當前工作目錄
ls                      # 列出檔案
ls -la                  # 列出所有檔案（包括隱藏檔）及詳細資訊
ls -lh                  # 人類可讀的大小
cd /path/to/dir         # 切換目錄
cd ..                   # 上一層目錄
cd ~                    # 前往主目錄
cd -                    # 前往先前的目錄
```

### 檔案操作
```bash
touch file.txt          # 建立空白檔案
cp source dest          # 複製檔案
cp -r dir1 dir2         # 遞迴複製目錄
mv old new              # 移動/重新命名檔案
rm file.txt             # 移除檔案
rm -r directory         # 遞迴移除目錄
rm -f file              # 強制移除（無提示）
rm -rf directory        # 強制移除目錄（危險）
mkdir newdir            # 建立目錄
mkdir -p path/to/dir    # 建立巢狀目錄
ln -s target link       # 建立符號連結
```

### 檢視檔案
```bash
cat file.txt            # 顯示整個檔案
less file.txt           # 分頁檢視檔案（按 q 退出）
head file.txt           # 前 10 行
head -n 20 file.txt     # 前 20 行
tail file.txt           # 後 10 行
tail -n 20 file.txt     # 後 20 行
tail -f logfile.log     # 追蹤檔案（即時更新）
```

---

## 檔案權限

```bash
chmod 755 file          # 設定權限（rwxr-xr-x）
chmod +x script.sh      # 設為可執行
chmod -R 755 dir        # 遞迴變更權限
chown user:group file   # 變更擁有者和群組
chown user file         # 僅變更擁有者
chgrp group file        # 變更群組
umask                   # 顯示預設權限遮罩
```

### 權限數字
- `7` = rwx（讀 + 寫 + 執行）
- `6` = rw-（讀 + 寫）
- `5` = r-x（讀 + 執行）
- `4` = r--（僅讀）

---

## 文字處理

### 搜尋與替換
```bash
grep "pattern" file.txt                 # 搜尋模式
grep -r "pattern" dir/                  # 遞迴搜尋
grep -i "pattern" file.txt              # 不分大小寫
grep -v "pattern" file.txt              # 反向匹配
grep -l "pattern" *.txt                 # 列出匹配的檔案
grep -c "pattern" file.txt              # 計數匹配數
grep -E "pattern1|pattern2" file.txt    # 延伸正規表示式
```

### 尋找檔案
```bash
find /path -name "file.txt"             # 按名稱尋找
find /path -name "*.py"                 # 按副檔名尋找
find /path -type d                      # 尋找目錄
find /path -type f                      # 尋找檔案
find /path -size +100M                  # 大於 100MB 的檔案
find /path -mtime -7                    # 最近 7 天修改的檔案
find /path -perm 755                    # 按權限尋找
find /path -exec command {} \;          # 對結果執行指令
```

### 文字處理
```bash
wc file.txt             # 字數統計（行數、字數、位元組數）
wc -l file.txt          # 僅行數
sort file.txt           # 排序行
sort -n file.txt        # 數值排序
sort -r file.txt        # 反向排序
uniq file.txt           # 移除相鄰的重複項
uniq -c file.txt        # 計算出現次數
cut -d: -f1 /etc/passwd # 按分隔符號切割欄位
paste file1 file2       # 並排合併檔案
tr 'a-z' 'A-Z' < file   # 轉換字元
sed 's/old/new/g' file  # 替換文字
awk '{print $1}' file   # 印出第一欄
```

---

## 程序管理

```bash
ps                      # 顯示執行中的程序
ps aux                  # 所有程序及詳細資訊
ps aux | grep python    # 過濾程序
top                     # 互動式程序檢視器
htop                    # 增強版 top（如已安裝）
kill PID                # 終止程序
kill -9 PID             # 強制終止
killall process_name    # 按名稱終止
pkill pattern           # 按模式終止
nice -n 10 command      # 以較低優先權執行
renice 10 -p PID        # 變更執行中程序的優先權
bg                      # 在背景恢復作業
fg                      # 將作業帶到前景
jobs                    # 列出背景作業
Ctrl+Z                  # 暫停目前作業
```

---

## 系統資訊

```bash
uname -a                # 系統資訊
uname -r                # 核心版本
hostname                # 顯示主機名稱
whoami                  # 目前使用者
id                      # 使用者和群組 ID
uptime                  # 系統運作時間和負載
date                    # 目前日期/時間
cal                     # 日曆
df -h                   # 磁碟空間（人類可讀）
du -sh directory        # 目錄大小
free -h                 # 記憶體使用量
lscpu                   # CPU 資訊
lsblk                   # 區塊裝置
fdisk -l                # 磁碟分割區（需要 sudo）
```

---

## 網路指令

```bash
ifconfig                # 網路介面（已棄用）
ip addr show            # IP 位址（現代）
ip route show           # 路由表
ping google.com         # 測試連線
traceroute google.com   # 追蹤網路路徑
tracepath google.com    # 替代 traceroute
netstat -tulpn          # 監聽埠（已棄用）
ss -tulpn               # Socket 統計資料（現代）
dig domain.com          # DNS 查詢
nslookup domain.com     # DNS 查詢（較舊）
curl http://example.com # HTTP 請求
wget http://file.url    # 下載檔案
ssh user@host           # SSH 連線
scp file user@host:path # 安全複製
rsync -av src/ dest/    # 同步檔案/目錄
```

---

## 封存與壓縮

```bash
tar -cvf archive.tar file1 file2        # 建立 tar 封存
tar -xvf archive.tar                    # 解壓 tar 封存
tar -czvf archive.tar.gz dir/           # 建立 gzip 壓縮的 tar
tar -xzvf archive.tar.gz                # 解壓 gzip 壓縮的 tar
tar -cjvf archive.tar.bz2 dir/          # 建立 bzip2 壓縮的 tar
tar -xjvf archive.tar.bz2               # 解壓 bzip2 壓縮的 tar
gzip file.txt                           # 壓縮檔案
gunzip file.txt.gz                      # 解壓縮檔案
zip -r archive.zip dir/                 # 建立 zip 封存
unzip archive.zip                       # 解壓 zip 封存
```

---

## 套件管理

### Debian/Ubuntu (apt)
```bash
sudo apt update                         # 更新套件清單
sudo apt upgrade                        # 升級套件
sudo apt install package_name           # 安裝套件
sudo apt remove package_name            # 移除套件
sudo apt purge package_name             # 移除套件及配置
sudo apt search keyword                 # 搜尋套件
sudo apt show package_name              # 套件詳情
```

### RHEL/CentOS (yum/dnf)
```bash
sudo yum update                         # 更新套件
sudo yum install package_name           # 安裝套件
sudo yum remove package_name            # 移除套件
sudo yum search keyword                 # 搜尋套件
```

### macOS (brew)
```bash
brew update                             # 更新 brew
brew upgrade                            # 升級套件
brew install package_name               # 安裝套件
brew uninstall package_name             # 移除套件
brew search keyword                     # 搜尋套件
brew list                               # 列出已安裝的套件
```

---

## 使用者管理

```bash
sudo adduser username                   # 建立新使用者
sudo deluser username                   # 刪除使用者
sudo usermod -aG group username         # 將使用者加入群組
passwd username                         # 變更使用者密碼
sudo passwd username                    # 變更其他人的密碼
su - username                           # 切換使用者
sudo command                            # 以 root 身份執行
groups username                         # 顯示使用者群組
```

---

## 磁碟管理

```bash
mount /dev/sda1 /mnt                    # 掛載檔案系統
umount /mnt                             # 卸載檔案系統
lsblk                                   # 列出區塊裝置
blkid                                   # 顯示區塊裝置屬性
mkfs.ext4 /dev/sda1                     # 格式化為 ext4
fsck /dev/sda1                          # 檢查檔案系統
dd if=/dev/sda of=backup.img            # 磁碟映像（小心！）
```

---

## Shell 變數與環境

```bash
echo $HOME              # 顯示環境變數
export VAR=value        # 設定環境變數
env                     # 列出所有環境變數
unset VAR               # 移除變數
alias ll='ls -la'       # 建立別名
unalias ll              # 移除別名
history                 # 指令歷史記錄
!123                    # 執行歷史記錄中的指令 #123
!!                      # 執行最後一個指令
!$                      # 上一個指令的最後一個參數
Ctrl+R                  # 搜尋歷史記錄
```

---

## 輸入/輸出重新導向

```bash
command > file.txt      # 重新導向輸出（覆寫）
command >> file.txt     # 重新導向輸出（附加）
command < file.txt      # 重新導向輸入
command 2> error.log    # 重新導向 stderr
command &> all.log      # 重新導向 stdout 和 stderr
command | grep pattern  # 將輸出導向另一個指令
tee file.txt            # 輸出至檔案和螢幕
```

---

## 實用單行指令

```bash
# 計算目錄中的檔案數
ls -1 | wc -l

# 尋找最大的檔案
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -10

# 檢查哪個程序使用某個埠
lsof -i :8080

# 監控檔案變更
watch -n 1 'ls -la'

# 從日誌中提取唯一 IP
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log | sort -u

# 備份並加上時間戳記
tar -czf backup_$(date +%Y%m%d).tar.gz /path/to/backup

# 尋找並刪除舊檔案
find /path -type f -mtime +30 -delete

# 檢查磁碟佔用大戶
du -ah | sort -hr | head -20
```

---

## 鍵盤快捷鍵

| 快捷鍵 | 動作 |
|----------|--------|
| `Tab` | 自動完成 |
| `Ctrl+C` | 終止目前指令 |
| `Ctrl+Z` | 暫停指令 |
| `Ctrl+D` | 退出 Shell/EOF |
| `Ctrl+L` | 清除螢幕 |
| `Ctrl+A` | 移至行首 |
| `Ctrl+E` | 移至行尾 |
| `Ctrl+U` | 刪除至行首 |
| `Ctrl+K` | 刪除至行尾 |
| `Ctrl+R` | 搜尋歷史記錄 |
| `Ctrl+W` | 刪除游標前的單字 |

---

## 最佳實踐

✅ **應該做的：**
- 謹慎節制地使用 `sudo`
- 在執行破壞性指令前先進行測試，不使用執行標記
- 在重大變更前保留備份
- 使用有意義的檔案名稱（無空格）
- 學習使用 `man` 頁面（`man command`）

❌ **不應該做的：**
- 執行 `rm -rf /` 或類似危險指令
- 對敏感檔案使用 `chmod 777`
- 忽略警告訊息
- 在無備份的情況下編輯系統檔案
- 以 root 身份執行未知腳本

---

*最後更新：2025年6月 | Linux/Unix 相容*
