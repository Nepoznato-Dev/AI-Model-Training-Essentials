# Linux कमांड्स त्वरित संदर्भ

सिस्टम नेविगेशन और प्रशासन के लिए आवश्यक Linux/Unix कमांड्स।

---

## फ़ाइल और डायरेक्टरी ऑपरेशन्स

### नेविगेशन
```bash
pwd                     # वर्तमान कार्यशील डायरेक्टरी प्रिंट करें
ls                      # फ़ाइलों की सूची दिखाएँ
ls -la                  # सभी फ़ाइलें (छिपी हुई सहित) विवरण के साथ दिखाएँ
ls -lh                  # मानव-पठनीय आकार
cd /path/to/dir         # डायरेक्टरी बदलें
cd ..                   # एक डायरेक्टरी ऊपर जाएँ
cd ~                    # होम डायरेक्टरी पर जाएँ
cd -                    # पिछली डायरेक्टरी पर जाएँ
```

### फ़ाइल ऑपरेशन्स
```bash
touch file.txt          # खाली फ़ाइल बनाएँ
cp source dest          # फ़ाइल कॉपी करें
cp -r dir1 dir2         # डायरेक्टरी को पुनरावर्ती रूप से कॉपी करें
mv old new              # फ़ाइल को स्थानांतरित करें/नाम बदलें
rm file.txt             # फ़ाइल हटाएँ
rm -r directory         # डायरेक्टरी को पुनरावर्ती रूप से हटाएँ
rm -f file              # बलपूर्वक हटाएँ (बिना पूछे)
rm -rf directory        # डायरेक्टरी को बलपूर्वक हटाएँ (खतरनाक)
mkdir newdir            # डायरेक्टरी बनाएँ
mkdir -p path/to/dir    # नेस्टेड डायरेक्टरी बनाएँ
ln -s target link       # प्रतीकात्मक लिंक बनाएँ
```

### फ़ाइलें देखना
```bash
cat file.txt            # पूरी फ़ाइल दिखाएँ
less file.txt           # फ़ाइल को पेज दर पेज देखें (बाहर निकलने के लिए q)
head file.txt           # पहली 10 पंक्तियाँ
head -n 20 file.txt     # पहली 20 पंक्तियाँ
tail file.txt           # अंतिम 10 पंक्तियाँ
tail -n 20 file.txt     # अंतिम 20 पंक्तियाँ
tail -f logfile.log     # फ़ाइल को फ़ॉलो करें (लाइव अपडेट्स)
```

---

## फ़ाइल अनुमतियाँ

```bash
chmod 755 file          # अनुमतियाँ सेट करें (rwxr-xr-x)
chmod +x script.sh      # चलाने योग्य बनाएँ
chmod -R 755 dir        # अनुमतियों को पुनरावर्ती रूप से बदलें
chown user:group file   # स्वामी और समूह बदलें
chown user file         # केवल स्वामी बदलें
chgrp group file        # केवल समूह बदलें
umask                   # डिफ़ॉल्ट अनुमति mask दिखाएँ
```

### अनुमति संख्याएँ
- `7` = rwx (पढ़ें + लिखें + चलाएँ)
- `6` = rw- (पढ़ें + लिखें)
- `5` = r-x (पढ़ें + चलाएँ)
- `4` = r-- (केवल पढ़ें)

---

## टेक्स्ट प्रोसेसिंग

### खोज और प्रतिस्थापन
```bash
grep "pattern" file.txt                 # pattern खोजें
grep -r "pattern" dir/                  # पुनरावर्ती खोज
grep -i "pattern" file.txt              # केस-असंवेदनशील
grep -v "pattern" file.txt              # उल्टा मिलान
grep -l "pattern" *.txt                 # मेल खाने वाली फ़ाइलों की सूची
grep -c "pattern" file.txt              # मेलों की गिनती
grep -E "pattern1|pattern2" file.txt    # विस्तारित रेगेक्स
```

### फ़ाइलें ढूँढना
```bash
find /path -name "file.txt"             # नाम से खोजें
find /path -name "*.py"                 # एक्सटेंशन से खोजें
find /path -type d                      # डायरेक्टरी खोजें
find /path -type f                      # फ़ाइलें खोजें
find /path -size +100M                  # 100MB से बड़ी फ़ाइलें
find /path -mtime -7                    # पिछले 7 दिनों में संशोधित
find /path -perm 755                    # अनुमतियों के आधार पर खोजें
find /path -exec command {} \;          # परिणामों पर command चलाएँ
```

### टेक्स्ट में बदलाव
```bash
wc file.txt             # शब्द गणना (पंक्तियाँ, शब्द, बाइट्स)
wc -l file.txt          # केवल पंक्ति गणना
sort file.txt           # पंक्तियाँ क्रमबद्ध करें
sort -n file.txt        # संख्यात्मक क्रमबद्धता
sort -r file.txt        # उल्टा क्रमबद्ध करें
uniq file.txt           # पास-पास की डुप्लिकेट प्रविष्टियाँ हटाएँ
uniq -c file.txt        # आवृत्तियाँ गिनें
cut -d: -f1 /etc/passwd # डिलिमिटर के आधार पर फ़ील्ड्स काटें
paste file1 file2       # फ़ाइलों को साथ-साथ मिलाएँ
tr 'a-z' 'A-Z' < file   # अक्षरों का रूपांतरण करें
sed 's/old/new/g' file  # टेक्स्ट बदलें
awk '{print $1}' file   # पहला कॉलम प्रिंट करें
```

---

## प्रोसेस प्रबंधन

```bash
ps                      # चल रही प्रक्रियाएँ दिखाएँ
ps aux                  # सभी प्रक्रियाएँ विवरण सहित
ps aux | grep python    # प्रक्रियाओं को फ़िल्टर करें
top                     # इंटरैक्टिव प्रोसेस व्यूअर
htop                    # उन्नत top (यदि इंस्टॉल हो)
kill PID                # प्रक्रिया समाप्त करें
kill -9 PID             # बलपूर्वक प्रक्रिया समाप्त करें
killall process_name    # नाम के आधार पर समाप्त करें
pkill pattern           # pattern के आधार पर समाप्त करें
nice -n 10 command      # कम प्राथमिकता के साथ चलाएँ
renice 10 -p PID        # चल रही प्रक्रिया की प्राथमिकता बदलें
bg                      # जॉब को बैकग्राउंड में फिर शुरू करें
fg                      # जॉब को फ़ोरग्राउंड में लाएँ
jobs                    # बैकग्राउंड जॉब्स की सूची दिखाएँ
Ctrl+Z                  # वर्तमान जॉब को स्थगित करें
```

---

## सिस्टम जानकारी

```bash
uname -a                # सिस्टम जानकारी
uname -r                # कर्नेल संस्करण
hostname                # होस्टनेम दिखाएँ
whoami                  # वर्तमान उपयोगकर्ता
id                      # उपयोगकर्ता और समूह IDs
uptime                  # सिस्टम अपटाइम और लोड
date                    # वर्तमान तारीख/समय
cal                     # कैलेंडर
df -h                   # डिस्क स्थान (मानव-पठनीय)
du -sh directory        # डायरेक्टरी का आकार
free -h                 # मेमोरी उपयोग
lscpu                   # CPU जानकारी
lsblk                   # ब्लॉक डिवाइसेज़
fdisk -l                # डिस्क पार्टिशन्स (sudo आवश्यक)
```

---

## नेटवर्क कमांड्स

```bash
ifconfig                # नेटवर्क इंटरफेसेज़ (डिप्रिकेटेड)
ip addr show            # IP पते (आधुनिक)
ip route show           # रूटिंग टेबल
ping google.com         # कनेक्टिविटी जाँचें
traceroute google.com   # नेटवर्क पाथ ट्रेस करें
tracepath google.com    # वैकल्पिक traceroute
netstat -tulpn          # सुनने वाले पोर्ट्स (डिप्रिकेटेड)
ss -tulpn               # सॉकेट आँकड़े (आधुनिक)
dig domain.com          # DNS lookup
nslookup domain.com     # DNS lookup (पुराना)
curl http://example.com # HTTP अनुरोध
wget http://file.url    # फ़ाइल डाउनलोड करें
ssh user@host           # SSH कनेक्शन
scp file user@host:path # सुरक्षित कॉपी
rsync -av src/ dest/    # फ़ाइलें/डायरेक्टरी sync करें
```

---

## आर्काइव और संपीड़न

```bash
tar -cvf archive.tar file1 file2        # tar आर्काइव बनाएँ
tar -xvf archive.tar                    # tar आर्काइव निकालें
tar -czvf archive.tar.gz dir/           # gzip की हुई tar फ़ाइल बनाएँ
tar -xzvf archive.tar.gz                # gzip की हुई tar फ़ाइल निकालें
tar -cjvf archive.tar.bz2 dir/          # bzip2 tar फ़ाइल बनाएँ
tar -xjvf archive.tar.bz2               # bzip2 tar फ़ाइल निकालें
gzip file.txt                           # फ़ाइल संपीड़ित करें
gunzip file.txt.gz                      # फ़ाइल असंपीड़ित करें
zip -r archive.zip dir/                 # zip आर्काइव बनाएँ
unzip archive.zip                       # zip आर्काइव निकालें
```

---

## पैकेज प्रबंधन

### डेबियन/उबुन्टू (apt)
```bash
sudo apt update                         # पैकेज सूची अपडेट करें
sudo apt upgrade                        # पैकेज अपग्रेड करें
sudo apt install package_name           # पैकेज इंस्टॉल करें
sudo apt remove package_name            # पैकेज हटाएँ
sudo apt purge package_name             # कॉन्फ़िगरेशन सहित हटाएँ
sudo apt search keyword                 # पैकेज खोजें
sudo apt show package_name              # पैकेज विवरण
```

### RHEL/CentOS (yum/dnf)
```bash
sudo yum update                         # पैकेज अपडेट करें
sudo yum install package_name           # पैकेज इंस्टॉल करें
sudo yum remove package_name            # पैकेज हटाएँ
sudo yum search keyword                 # पैकेज खोजें
```

### macOS (brew)
```bash
brew update                             # brew अपडेट करें
brew upgrade                            # पैकेज अपग्रेड करें
brew install package_name               # पैकेज इंस्टॉल करें
brew uninstall package_name             # पैकेज हटाएँ
brew search keyword                     # पैकेज खोजें
brew list                               # इंस्टॉल किए गए पैकेजों की सूची दिखाएँ
```

---

## उपयोगकर्ता प्रबंधन

```bash
sudo adduser username                   # नया उपयोगकर्ता बनाएँ
sudo deluser username                   # उपयोगकर्ता हटाएँ
sudo usermod -aG group username         # उपयोगकर्ता को समूह में जोड़ें
passwd username                         # उपयोगकर्ता का पासवर्ड बदलें
sudo passwd username                    # किसी दूसरे का पासवर्ड बदलें
su - username                           # उपयोगकर्ता बदलें
sudo command                            # root के रूप में चलाएँ
groups username                         # उपयोगकर्ता के समूह दिखाएँ
```

---

## डिस्क प्रबंधन

```bash
mount /dev/sda1 /mnt                    # फ़ाइलसिस्टम mount करें
umount /mnt                             # फ़ाइलसिस्टम unmount करें
lsblk                                   # ब्लॉक डिवाइसेज़ की सूची दिखाएँ
blkid                                   # ब्लॉक डिवाइस attributes दिखाएँ
mkfs.ext4 /dev/sda1                     # ext4 के रूप में format करें
fsck /dev/sda1                          # फ़ाइलसिस्टम जाँचें
dd if=/dev/sda of=backup.img            # डिस्क इमेज (सावधानी रखें!)
```

---

## शेल वेरिएबल्स और एनवायरनमेंट

```bash
echo $HOME              # environment variable दिखाएँ
export VAR=value        # environment variable सेट करें
env                     # सभी environment variables की सूची दिखाएँ
unset VAR               # variable हटाएँ
alias ll='ls -la'       # alias बनाएँ
unalias ll              # alias हटाएँ
history                 # कमांड इतिहास
!123                    # इतिहास से command #123 चलाएँ
!!                      # पिछली command चलाएँ
!$                      # पिछली command का अंतिम argument
Ctrl+R                  # इतिहास खोजें
```

---

## इनपुट/आउटपुट रीडायरेक्शन

```bash
command > file.txt      # आउटपुट रीडायरेक्ट करें (overwrite)
command >> file.txt     # आउटपुट रीडायरेक्ट करें (append)
command < file.txt      # इनपुट रीडायरेक्ट करें
command 2> error.log    # stderr रीडायरेक्ट करें
command &> all.log      # stdout और stderr रीडायरेक्ट करें
command | grep pattern  # आउटपुट को दूसरी command में pipe करें
tee file.txt            # आउटपुट को फ़ाइल और स्क्रीन दोनों पर भेजें
```

---

## उपयोगी वन-लाइनर्स

```bash
# डायरेक्टरी में फ़ाइलों की गिनती करें
ls -1 | wc -l

# सबसे बड़ी फ़ाइलें खोजें
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -10

# जाँचें कि कौन-सी प्रक्रिया कोई port उपयोग कर रही है
lsof -i :8080

# फ़ाइल परिवर्तनों की निगरानी करें
watch -n 1 'ls -la'

# log से अद्वितीय IPs निकालें
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log | sort -u

# timestamp के साथ बैकअप बनाएँ
tar -czf backup_$(date +%Y%m%d).tar.gz /path/to/backup

# पुरानी फ़ाइलें खोजें और हटाएँ
find /path -type f -mtime +30 -delete

# डिस्क hogs जाँचें
du -ah | sort -hr | head -20
```

---

## कीबोर्ड शॉर्टकट्स

| शॉर्टकट | क्रिया |
|----------|--------|
| `Tab` | स्वतः-पूर्ण |
| `Ctrl+C` | वर्तमान command रोकें |
| `Ctrl+Z` | command को स्थगित करें |
| `Ctrl+D` | shell/EOF से बाहर निकलें |
| `Ctrl+L` | स्क्रीन साफ़ करें |
| `Ctrl+A` | पंक्ति की शुरुआत पर जाएँ |
| `Ctrl+E` | पंक्ति के अंत पर जाएँ |
| `Ctrl+U` | पंक्ति की शुरुआत तक हटाएँ |
| `Ctrl+K` | पंक्ति के अंत तक हटाएँ |
| `Ctrl+R` | इतिहास खोजें |
| `Ctrl+W` | cursor से पहले का शब्द हटाएँ |

---

## सर्वोत्तम अभ्यास

✅ **करें:**
- `sudo` का कम और सावधानी से उपयोग करें
- विनाशकारी कमांड्स को पहले execution flags के बिना जाँचें
- बड़े बदलावों से पहले बैकअप रखें
- अर्थपूर्ण filenames का उपयोग करें (बिना spaces)
- `man` pages का उपयोग करना सीखें (`man command`)

❌ **न करें:**
- `rm -rf /` या इसी तरह की खतरनाक कमांड्स न चलाएँ
- संवेदनशील फ़ाइलों पर `chmod 777` का उपयोग न करें
- चेतावनी संदेशों को अनदेखा न करें
- बैकअप के बिना सिस्टम फ़ाइलें संपादित न करें
- अज्ञात scripts को root के रूप में न चलाएँ

---

*अंतिम अपडेट: जून 2025 | Linux/Unix संगत*
