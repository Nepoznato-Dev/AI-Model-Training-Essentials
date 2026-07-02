# استخدام الأدوات

## Git — التحكم في الإصدارات

Git هو نظام موزّع للتحكم في الإصدارات. يمتلك كل مطور نسخة كاملة من سجل المستودع على جهازه المحلي.

### سير العمل الأساسي

```bash
# بدء مستودع جديد
git init

# استنساخ مستودع موجود
git clone https://github.com/owner/repo.git

# التحقق من الحالة والسجل الحديث
git status
git log --oneline -10

# تجهيز التغييرات
git add file.py            # تجهيز ملف محدد
git add .                  # تجهيز جميع التغييرات في دليل العمل

# إنشاء commit
git commit -m "Short, imperative description of change"

# الرفع إلى remote
git push origin main
```

### الفروع

```bash
git branch feature/new-thing        # إنشاء فرع
git checkout feature/new-thing      # التبديل إليه
# اختصار: git checkout -b feature/new-thing

git branch -d feature/new-thing     # حذف الفرع بعد الدمج
```

### الدمج و rebase

```bash
# دمج فرع الميزة في main
git checkout main
git merge feature/new-thing

# يحافظ Rebase على سجل خطي
git checkout feature/new-thing
git rebase main
```

### سير عمل طلب السحب (PR)

1. أنشئ فرع ميزة من `main`.
2. نفّذ commits على فرع الميزة.
3. ارفع الفرع: `git push origin feature/new-thing`.
4. افتح طلب سحب على GitHub / GitLab.
5. عالج ملاحظات مراجعة الكود عبر commits إضافية.
6. ادمج PR بعد الموافقة عليه.

### التراجع عن التغييرات

```bash
git restore file.py            # تجاهل التغييرات غير المجهزة
git restore --staged file.py   # إلغاء تجهيز ملف
git revert <commit-sha>        # إنشاء commit جديد يتراجع عن commit سابق
git reset --soft HEAD~1        # التراجع عن آخر commit مع إبقاء التغييرات مجهزة
```

---

## مديرو الحزم

### pip (Python)

```bash
pip install requests            # تثبيت حزمة
pip install "requests>=2.28"    # مع قيد إصدار
pip install -r requirements.txt # التثبيت من ملف
pip uninstall requests
pip list                        # عرض الحزم المثبتة
pip show requests               # معلومات عن حزمة
```

اعمل دائمًا داخل بيئة افتراضية للحفاظ على عزل تبعيات المشروع.

### npm (Node.js / JavaScript)

```bash
npm init -y                     # إنشاء package.json
npm install express             # التثبيت كتبعية وقت تشغيل
npm install --save-dev jest     # التثبيت كتبعية تطوير
npm uninstall express
npm update
npm run test                    # تشغيل السكربت "test" من package.json
npm run build
npx create-react-app my-app     # تشغيل حزمة دون تثبيتها على مستوى النظام
```

يسجل `package-lock.json` الإصدارات الدقيقة؛ قم بإضافته إلى التحكم بالمصدر.

### Cargo (Rust)

```bash
cargo new my_project            # مشروع binary جديد
cargo new --lib my_lib          # مشروع library جديد
cargo add serde --features derive
cargo build
cargo run
cargo test
cargo clippy                    # lint
cargo fmt                       # تنسيق
cargo update                    # تحديث التبعيات ضمن القيود
```

### وحدات Go (Go)

```bash
go mod init github.com/user/repo
go get github.com/some/package@v1.2.3
go mod tidy                     # إزالة التبعيات غير المستخدمة
go build ./...
go test ./...
go vet ./...
```

### apt (Debian / Ubuntu Linux)

```bash
sudo apt update                 # تحديث قوائم الحزم
sudo apt install git curl wget  # تثبيت الحزم
sudo apt remove package-name
sudo apt upgrade                # ترقية جميع الحزم المثبتة
apt search keyword              # البحث عن الحزم
apt show package-name           # تفاصيل عن حزمة
```

---

## أساسيات سطر الأوامر

### التنقل

```bash
pwd                             # طباعة دليل العمل الحالي
ls                              # عرض محتويات الدليل
ls -la                          # عرض تفصيلي يشمل الملفات المخفية
cd /path/to/dir                 # تغيير الدليل
cd ..                           # الصعود مستوى واحد
cd ~                            # الانتقال إلى الدليل الرئيسي
mkdir new_folder
rm file.txt                     # حذف ملف
rm -r folder/                   # حذف دليل بشكل متكرر
cp src.txt dst.txt
mv old_name.txt new_name.txt
```

### معالجة النصوص

```bash
cat file.txt                    # طباعة محتويات الملف
less file.txt                   # التمرير عبر ملف
head -n 20 file.txt             # أول 20 سطرًا
tail -n 20 file.txt             # آخر 20 سطرًا
tail -f log.txt                 # متابعة ملف سجل متزايد
grep "pattern" file.txt         # البحث عن نمط
grep -r "pattern" ./src/        # بحث بشكل متكرر
grep -i "pattern" file.txt      # دون حساسية لحالة الأحرف
```

### الأنابيب وإعادة التوجيه

```bash
command1 | command2             # تمرير خرج command1 إلى command2
ls -la | grep ".py"             # عرض ملفات Python فقط
cat file.txt | wc -l            # عدّ الأسطر
command > output.txt            # إعادة توجيه stdout إلى ملف (استبدال)
command >> output.txt           # إلحاق stdout بملف
command 2>&1                    # دمج stderr في stdout
```

### الشبكات ونقل الملفات

```bash
curl https://example.com                     # جلب URL
curl -o file.zip https://example.com/f.zip   # تنزيل إلى ملف
curl -X POST -d '{"key":"val"}' -H "Content-Type: application/json" https://api.example.com/endpoint

wget https://example.com/file.zip            # تنزيل باستخدام wget
```

### الأذونات

```bash
chmod +x script.sh              # جعله قابلاً للتنفيذ
chmod 644 file.txt              # المالك قراءة/كتابة، المجموعة/الآخرون قراءة
chown user:group file.txt       # تغيير المالك والمجموعة
```

### إدارة العمليات

```bash
ps aux                          # عرض العمليات قيد التشغيل
kill <PID>                      # إرسال SIGTERM إلى عملية
kill -9 <PID>                   # قتل إجباري
top / htop                      # مراقب عمليات تفاعلي
```

---

## المحررات و IDEs

### VS Code

VS Code هو محرر أكواد خفيف ومتعدد المنصات مع منظومة غنية من الإضافات.

- فتح مجلد: `File > Open Folder` أو `code .` في الطرفية.
- لوحة الأوامر: `Ctrl+Shift+P` (macOS: `Cmd+Shift+P`).
- الطرفية المدمجة: `Ctrl+`` (backtick)`.
- المؤشرات المتعددة: `Alt+Click` لإضافة مؤشرات إضافية.
- الانتقال إلى التعريف: `F12`.
- إعادة تسمية الرمز: `F2`.
- تنسيق المستند: `Shift+Alt+F`.
- الإضافات: ثبّت دعم اللغات (Python و Rust و Go وغيرها)، وأدوات lint وأدوات التنسيق من لوحة Extensions (`Ctrl+Shift+X`).
- يتحكم `settings.json` (للمستخدم أو مساحة العمل) في سلوك المحرر.
- يضبط `launch.json` أداة التصحيح.

### JetBrains IDEs (IntelliJ IDEA, PyCharm, WebStorm, CLion, GoLand)

- الإكمال الذكي للكود وإعادة الهيكلة من الميزات الأساسية.
- تتيح إعدادات التشغيل/التصحيح تشغيل البرامج وتصحيحها بنقرة واحدة.
- دعم Git مدمج في قائمة VCS.
- يفتح `Shift+Shift` نافذة Search Everywhere.
- يعيد `Ctrl+Alt+L` (macOS: `Cmd+Option+L`) تنسيق الكود.
- توسّع Plugins دعم اللغات وتضيف أدوات.

### نصائح الطرفية

- استخدم الإكمال باستخدام Tab لإتمام أسماء الملفات والأوامر بسرعة.
- ينشئ `alias ll='ls -la'` اختصارًا — أضفه إلى `~/.bashrc` أو `~/.zshrc`.
- استخدم `tmux` أو `screen` للحفاظ على الجلسات فعالة عند انقطاع الاتصال عن خادم بعيد.
- يعرض `man <command>` صفحة الدليل لأي أمر مدمج.

---

## Docker

يقوم Docker بتغليف التطبيقات وتبعياتها داخل حاويات محمولة.

### المفاهيم الأساسية

- **Image**: قالب للقراءة فقط يُبنى من `Dockerfile`.
- **Container**: نسخة قيد التشغيل من image.
- **Registry**: خدمة تخزين وتوزيع للصور (Docker Hub, GHCR).
- **Volume**: تخزين دائم يستمر بعد انتهاء الحاوية.

### أوامر شائعة

```bash
# الصور
docker pull ubuntu:22.04
docker images
docker rmi ubuntu:22.04

# الحاويات
docker run -it ubuntu:22.04 bash        # shell تفاعلي
docker run -d -p 8080:80 nginx          # في الخلفية مع ربط المنافذ
docker ps                               # الحاويات قيد التشغيل
docker ps -a                            # جميع الحاويات
docker stop <container_id>
docker rm <container_id>
docker logs <container_id>
docker exec -it <container_id> bash     # فتح shell داخل حاوية قيد التشغيل

# البناء
docker build -t myapp:1.0 .
docker push myrepo/myapp:1.0
```

### مثال على Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### Docker Compose

يدير Docker Compose التطبيقات متعددة الحاويات باستخدام ملف `docker-compose.yml`.

```yaml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://db:5432/mydb
    depends_on:
      - db
  db:
    image: postgres:15
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

```bash
docker compose up -d       # بدء جميع الخدمات في الخلفية
docker compose down        # إيقاف الحاويات وإزالتها
docker compose logs -f     # بث السجلات
docker compose build       # إعادة بناء الصور
```
