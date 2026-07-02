# مرجع سريع لأوامر لينكس

أوامر Linux/Unix الأساسية للتنقل في النظام وإدارته.

---

## عمليات الملفات والمجلدات

### التنقل
```bash
pwd                     # طباعة مجلد العمل الحالي
ls                      # عرض قائمة الملفات
ls -la                  # عرض جميع الملفات (بما فيها المخفية) بالتفصيل
ls -lh                  # أحجام قابلة للقراءة البشرية
cd /path/to/dir         # تغيير المجلد
cd ..                   # الانتقال إلى المجلد الأعلى
cd ~                    # الانتقال إلى المجلد الرئيسي
cd -                    # الانتقال إلى المجلد السابق
```

### عمليات الملفات
```bash
touch file.txt          # إنشاء ملف فارغ
cp source dest          # نسخ ملف
cp -r dir1 dir2         # نسخ مجلد بشكل تكراري
mv old new              # نقل/إعادة تسمية ملف
rm file.txt             # حذف ملف
rm -r directory         # حذف مجلد بشكل تكراري
rm -f file              # حذف قسري (بدون تأكيد)
rm -rf directory        # حذف قسري لمجلد (خطير)
mkdir newdir            # إنشاء مجلد
mkdir -p path/to/dir    # إنشاء مجلدات متداخلة
ln -s target link       # إنشاء رابط رمزي
```

### عرض الملفات
```bash
cat file.txt            # عرض الملف بالكامل
less file.txt           # عرض الملف صفحة بصفحة (اضغط q للخروج)
head file.txt           # أول 10 أسطر
head -n 20 file.txt     # أول 20 سطر
tail file.txt           # آخر 10 أسطر
tail -n 20 file.txt     # آخر 20 سطر
tail -f logfile.log     # متابعة الملف (تحديثات مباشرة)
```

---

## أذونات الملفات

```bash
chmod 755 file          # تعيين الأذونات (rwxr-xr-x)
chmod +x script.sh      # جعله قابلاً للتنفيذ
chmod -R 755 dir        # تغيير الأذونات بشكل تكراري
chown user:group file   # تغيير المالك والمجموعة
chown user file         # تغيير المالك فقط
chgrp group file        # تغيير المجموعة فقط
umask                   # عرض قناع الأذونات الافتراضي
```

### أرقام الأذونات
- `7` = rwx (قراءة + كتابة + تنفيذ)
- `6` = rw- (قراءة + كتابة)
- `5` = r-x (قراءة + تنفيذ)
- `4` = r-- (قراءة فقط)

---

## معالجة النصوص

### البحث والاستبدال
```bash
grep "pattern" file.txt                 # البحث عن نمط
grep -r "pattern" dir/                  # بحث تكراري
grep -i "pattern" file.txt              # غير حساس لحالة الأحرف
grep -v "pattern" file.txt              # مطابقة عكسية
grep -l "pattern" *.txt                 # عرض الملفات المطابقة
grep -c "pattern" file.txt              # عد المطابقات
grep -E "pattern1|pattern2" file.txt    # تعبير نمطي موسّع
```

### البحث عن الملفات
```bash
find /path -name "file.txt"             # البحث بالاسم
find /path -name "*.py"                 # البحث بالامتداد
find /path -type d                      # البحث عن المجلدات
find /path -type f                      # البحث عن الملفات
find /path -size +100M                  # الملفات الأكبر من 100 ميجابايت
find /path -mtime -7                    # المعدّلة خلال آخر 7 أيام
find /path -perm 755                    # البحث حسب الأذونات
find /path -exec command {} \;          # تنفيذ أمر على النتائج
```

### معالجة النصوص
```bash
wc file.txt             # عدد الكلمات (أسطر، كلمات، بايتات)
wc -l file.txt          # عدد الأسطر فقط
sort file.txt           # ترتيب الأسطر
sort -n file.txt        # ترتيب رقمي
sort -r file.txt        # ترتيب عكسي
uniq file.txt           # إزالة التكرارات المتجاورة
uniq -c file.txt        # عد التكرارات
cut -d: -f1 /etc/passwd # قطع الحقول حسب الفاصل
paste file1 file2       # دمج الملفات جنباً إلى جنب
tr 'a-z' 'A-Z' < file   # ترجمة/تحويل الأحرف
sed 's/old/new/g' file  # استبدال نص
awk '{print $1}' file   # طباعة العمود الأول
```

---

## إدارة العمليات

```bash
ps                      # عرض العمليات الجارية
ps aux                  # جميع العمليات بالتفصيل
ps aux | grep python    # تصفية العمليات
top                     # عارض عمليات تفاعلي
htop                    # نسخة محسّنة من top (إن كانت مثبتة)
kill PID                # إنهاء عملية معينة عبر رقم المعرف (PID)
kill -9 PID             # إنهاء قسري
killall process_name    # إنهاء حسب الاسم
pkill pattern           # إنهاء حسب النمط
nice -n 10 command      # التشغيل بأولوية أقل
renice 10 -p PID        # تغيير أولوية عملية جارية
bg                      # استئناف المهمة في الخلفية
fg                      # إحضار المهمة إلى الواجهة
jobs                    # عرض المهام الخلفية
Ctrl+Z                  # تعليق المهمة الحالية
```

---

## معلومات النظام

```bash
uname -a                # معلومات النظام
uname -r                # إصدار النواة (kernel)
hostname                # عرض اسم المضيف
whoami                  # المستخدم الحالي
id                       # معرّفات المستخدم والمجموعة
uptime                  # مدة تشغيل النظام والحمل
date                    # التاريخ/الوقت الحالي
cal                     # التقويم
df -h                   # مساحة القرص (قابلة للقراءة البشرية)
du -sh directory        # حجم المجلد
free -h                 # استخدام الذاكرة
lscpu                   # معلومات المعالج
lsblk                   # أجهزة الكتل (Block devices)
fdisk -l                # أقسام القرص (يتطلب sudo)
```

---

## أوامر الشبكة

```bash
ifconfig                # واجهات الشبكة (قديم/متوقف الاستخدام)
ip addr show            # عناوين IP (حديث)
ip route show           # جدول التوجيه
ping google.com         # اختبار الاتصال
traceroute google.com   # تتبع مسار الشبكة
tracepath google.com    # بديل لـ traceroute
netstat -tulpn          # المنافذ المستمعة (قديم)
ss -tulpn               # إحصائيات المقابس (Socket) (حديث)
dig domain.com          # استعلام DNS
nslookup domain.com     # استعلام DNS (أقدم)
curl http://example.com # طلب HTTP
wget http://file.url    # تنزيل ملف
ssh user@host           # اتصال SSH
scp file user@host:path # نسخ آمن
rsync -av src/ dest/    # مزامنة الملفات/المجلدات
```

---

## الأرشفة والضغط

```bash
tar -cvf archive.tar file1 file2        # إنشاء أرشيف tar
tar -xvf archive.tar                    # استخراج أرشيف tar
tar -czvf archive.tar.gz dir/           # إنشاء tar مضغوط بـ gzip
tar -xzvf archive.tar.gz                # استخراج tar مضغوط بـ gzip
tar -cjvf archive.tar.bz2 dir/          # إنشاء tar مضغوط بـ bzip2
tar -xjvf archive.tar.bz2               # استخراج tar مضغوط بـ bzip2
gzip file.txt                           # ضغط ملف
gunzip file.txt.gz                      # فك ضغط ملف
zip -r archive.zip dir/                 # إنشاء أرشيف zip
unzip archive.zip                       # استخراج أرشيف zip
```

---

## إدارة الحزم

### Debian/Ubuntu (apt)
```bash
sudo apt update                         # تحديث قائمة الحزم
sudo apt upgrade                        # ترقية الحزم
sudo apt install package_name           # تثبيت حزمة
sudo apt remove package_name            # إزالة حزمة
sudo apt purge package_name             # إزالة مع الإعدادات
sudo apt search keyword                 # البحث عن حزم
sudo apt show package_name              # تفاصيل الحزمة
```

### RHEL/CentOS (yum/dnf)
```bash
sudo yum update                         # تحديث الحزم
sudo yum install package_name           # تثبيت حزمة
sudo yum remove package_name            # إزالة حزمة
sudo yum search keyword                 # البحث عن حزم
```

### macOS (brew)
```bash
brew update                             # تحديث brew
brew upgrade                            # ترقية الحزم
brew install package_name               # تثبيت حزمة
brew uninstall package_name             # إزالة حزمة
brew search keyword                     # البحث عن حزم
brew list                               # عرض الحزم المثبتة
```

---

## إدارة المستخدمين

```bash
sudo adduser username                   # إنشاء مستخدم جديد
sudo deluser username                   # حذف مستخدم
sudo usermod -aG group username         # إضافة مستخدم إلى مجموعة
passwd username                         # تغيير كلمة مرور المستخدم
sudo passwd username                    # تغيير كلمة مرور مستخدم آخر
su - username                           # التبديل إلى مستخدم آخر
sudo command                            # التشغيل كمستخدم root
groups username                         # عرض مجموعات المستخدم
```

---

## إدارة الأقراص

```bash
mount /dev/sda1 /mnt                    # تركيب نظام الملفات
umount /mnt                             # إلغاء تركيب نظام الملفات
lsblk                                   # عرض أجهزة الكتل
blkid                                   # عرض سمات أجهزة الكتل
mkfs.ext4 /dev/sda1                     # التهيئة بصيغة ext4
fsck /dev/sda1                          # فحص نظام الملفات
dd if=/dev/sda of=backup.img            # نسخة صورة للقرص (كن حذراً!)
```

---

## متغيرات الصدفة والبيئة

```bash
echo $HOME              # عرض متغير بيئي
export VAR=value        # تعيين متغير بيئي
env                     # عرض جميع المتغيرات البيئية
unset VAR               # إزالة متغير
alias ll='ls -la'       # إنشاء اسم مستعار (alias)
unalias ll              # إزالة اسم مستعار
history                 # سجل الأوامر
!123                    # تشغيل الأمر رقم 123 من السجل
!!                      # تشغيل آخر أمر
!$                      # آخر وسيط للأمر السابق
Ctrl+R                  # البحث في السجل
```

---

## إعادة توجيه الإدخال/الإخراج

```bash
command > file.txt      # إعادة توجيه الإخراج (استبدال)
command >> file.txt     # إعادة توجيه الإخراج (إلحاق)
command < file.txt      # إعادة توجيه الإدخال
command 2> error.log    # إعادة توجيه stderr
command &> all.log      # إعادة توجيه stdout و stderr معاً
command | grep pattern  # تمرير الإخراج إلى أمر آخر (pipe)
tee file.txt            # الإخراج إلى ملف وإلى الشاشة معاً
```

---

## أوامر مفيدة من سطر واحد

```bash
# عد الملفات في مجلد
ls -1 | wc -l

# البحث عن أكبر الملفات
find . -type f -exec ls -lh {} \; | sort -k5 -hr | head -10

# التحقق من العملية التي تستخدم منفذاً معيناً
lsof -i :8080

# مراقبة تغييرات الملفات
watch -n 1 'ls -la'

# استخراج عناوين IP الفريدة من سجل
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' access.log | sort -u

# نسخة احتياطية بختم زمني
tar -czf backup_$(date +%Y%m%d).tar.gz /path/to/backup

# البحث عن الملفات القديمة وحذفها
find /path -type f -mtime +30 -delete

# التحقق من أكبر مستهلكي مساحة القرص
du -ah | sort -hr | head -20
```

---

## اختصارات لوحة المفاتيح

| الاختصار | الإجراء |
|----------|--------|
| `Tab` | إكمال تلقائي |
| `Ctrl+C` | إنهاء الأمر الحالي |
| `Ctrl+Z` | تعليق الأمر |
| `Ctrl+D` | الخروج من الصدفة/نهاية الملف (EOF) |
| `Ctrl+L` | مسح الشاشة |
| `Ctrl+A` | الانتقال إلى بداية السطر |
| `Ctrl+E` | الانتقال إلى نهاية السطر |
| `Ctrl+U` | حذف حتى بداية السطر |
| `Ctrl+K` | حذف حتى نهاية السطر |
| `Ctrl+R` | البحث في السجل |
| `Ctrl+W` | حذف الكلمة قبل المؤشر |

---

## أفضل الممارسات

✅ **افعل:**
- استخدم `sudo` بحذر وباعتدال
- اختبر الأوامر المدمّرة بدون علامات التنفيذ أولاً
- احتفظ بنسخ احتياطية قبل التغييرات الكبيرة
- استخدم أسماء ملفات ذات معنى (بدون مسافات)
- تعلّم استخدام صفحات `man` (`man command`)

❌ **لا تفعل:**
- تشغيل `rm -rf /` أو أوامر خطيرة مشابهة
- استخدام `chmod 777` على الملفات الحساسة
- تجاهل رسائل التحذير
- تعديل ملفات النظام بدون نسخ احتياطية
- تشغيل نصوص برمجية مجهولة كمستخدم root

---

*آخر تحديث: يونيو 2025 | متوافق مع Linux/Unix*
