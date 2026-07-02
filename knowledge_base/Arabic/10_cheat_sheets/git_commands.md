# مرجع سريع لأوامر Git

أوامر Git الأساسية للتحكم في الإصدارات.

---

## الإعداد والتهيئة

```bash
# تهيئة معلومات المستخدم
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# عرض الإعدادات
git config --list
git config user.name

# تعيين اسم الفرع الافتراضي
git config --global init.defaultBranch main
```

---

## تهيئة المستودع

```bash
# تهيئة مستودع جديد
git init

# استنساخ مستودع موجود
git clone <url>
git clone <url> folder-name

# استنساخ فرع معين
git clone -b branch-name <url>
```

---

## سير العمل الأساسي

```bash
# التحقق من الحالة
git status

# عرض التغييرات
git diff
git diff --staged

# إضافة الملفات إلى منطقة التجهيز
git add file.txt          # ملف معين
git add .                 # جميع الملفات
git add *.py              # مطابقة نمط

# تثبيت التغييرات
git commit -m "Commit message"
git commit -am "Message"  # تجهيز وتثبيت الملفات المتتبعة

# عرض سجل الالتزامات
git log
git log --oneline
git log --graph --oneline --all
```

---

## التفريع (Branching)

```bash
# عرض الفروع
git branch                # الفروع المحلية
git branch -a             # جميع الفروع
git branch -r             # الفروع البعيدة

# إنشاء فرع
git branch branch-name
git checkout -b branch-name   # إنشاء والتبديل إليه

# التبديل بين الفروع
git checkout branch-name
git switch branch-name        # صياغة أحدث

# إعادة تسمية الفرع الحالي
git branch -m new-name

# حذف فرع
git branch -d branch-name     # حذف آمن (تم دمجه)
git branch -D branch-name     # حذف قسري

# دمج فرع
git merge branch-name

# إعادة تأسيس فرع (Rebase)
git rebase main
```

---

## العمليات البعيدة (Remote)

```bash
# عرض المستودعات البعيدة
git remote -v

# إضافة مستودع بعيد
git remote add origin <url>

# جلب البيانات من المستودع البعيد
git fetch origin
git fetch --all

# سحب التغييرات (جلب + دمج)
git pull origin main
git pull --rebase origin main

# دفع التغييرات
git push origin main
git push -u origin main     # تعيين الفرع الأعلى (upstream)
git push --force            # دفع قسري (استخدمه بحذر)
git push --force-with-lease # دفع قسري أكثر أماناً

# دفع الوسوم (Tags)
git push --tags
```

---

## التراجع عن التغييرات

```bash
# إلغاء تجهيز ملف (مع الاحتفاظ بالتغييرات)
git reset HEAD file.txt
git restore --staged file.txt

# تجاهل تغييرات منطقة العمل
git checkout -- file.txt
git restore file.txt

# تعديل آخر التزام
git commit --amend -m "New message"
git commit --amend --no-edit

# التراجع عن التزام (آمن للمستودعات المشتركة)
git revert commit-hash

# إعادة التعيين إلى التزام سابق
git reset --soft HEAD~1     # الاحتفاظ بالتغييرات في منطقة التجهيز
git reset --mixed HEAD~1    # الاحتفاظ بالتغييرات بدون تجهيز (الافتراضي)
git reset --hard HEAD~1     # تجاهل جميع التغييرات (خطير)
```

---

## التخزين المؤقت (Stashing)

```bash
# حفظ العمل الجاري
git stash
git stash save "message"

# عرض قائمة المخزنات المؤقتة
git stash list

# تطبيق مخزن مؤقت
git stash apply             # الأحدث
git stash apply stash@{1}   # مخزن معين

# تطبيق وإزالة
git stash pop

# إسقاط مخزن مؤقت
git stash drop stash@{1}

# مسح جميع المخزنات المؤقتة
git stash clear
```

---

## الوسوم (Tags)

```bash
# عرض الوسوم
git tag
git tag -l "v1.*"

# إنشاء وسم
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # وسم موضح (annotated)

# الانتقال إلى وسم
git checkout v1.0.0

# حذف وسم
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## العرض والبحث

```bash
# عرض تفاصيل الالتزام
git show commit-hash
git show --stat commit-hash

# Blame (من غيّر ماذا)
git blame file.txt

# البحث في الالتزامات
git log --grep="keyword"
git log --author="name"

# البحث عن كود في السجل
git log -S"function_name"

# عرض ملف عند التزام معين
git show commit-hash:file.txt
```

---

## العمليات المتقدمة

```bash
# انتقاء التزام (Cherry-pick)
git cherry-pick commit-hash

# إعادة تأسيس تفاعلية (Interactive rebase)
git rebase -i HEAD~5

# دمج عدة التزامات (Squash) (أثناء rebase)
# غيّر 'pick' إلى 'squash' أو 's' في المحرر

# إنشاء رقعة (patch)
git format-patch -1 commit-hash

# تطبيق رقعة (patch)
git apply patch-file.patch
git am patch-file.patch

# الوحدات الفرعية (Submodules)
git submodule add <url> path
git submodule update --init --recursive
```

---

## التنظيف

```bash
# إزالة الملفات غير المتتبعة (تشغيل تجريبي)
git clean -n
git clean -f                # الإزالة فعلياً

# إزالة المجلدات غير المتتبعة
git clean -fd

# تقليم الفروع البعيدة المحذوفة
git fetch --prune
git remote prune origin
```

---

## سير العمل الشائعة

### بدء ميزة جديدة
```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... العمل ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# أنشئ طلب سحب (PR/MR) على المنصة
```

### المزامنة مع الفرع الرئيسي
```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# حل التعارضات إن وجدت
git push --force-with-lease
```

### سير عمل الإصلاح العاجل (Hotfix)
```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... الإصلاح ...
git commit -am "Fix critical bug"
git checkout main
git merge hotfix/urgent-fix
git push
git tag v1.0.1
git push --tags
```

---

## أنماط .gitignore

```gitignore
# تجاهل ملف معين
filename.txt

# تجاهل جميع ملفات .log
*.log

# تجاهل مجلد
node_modules/
__pycache__/

# نفي (تضمين رغم النمط السابق)
!important.log

# تعليق
# هذا تعليق
```

---

## اختصارات لوحة المفاتيح (Git Bash)

| الاختصار | الإجراء |
|----------|--------|
| `Ctrl+R` | بحث عكسي في السجل |
| `Tab` | إكمال تلقائي |
| `Ctrl+C` | إلغاء الأمر |
| `Ctrl+Z` | تعليق العملية |
| `fg` | استئناف العملية المعلقة |

---

## أفضل الممارسات

✅ **افعل:**
- اكتب رسائل التزام واضحة ووصفية
- ثبّت التغييرات بشكل متكرر مع تجميع منطقي
- استخدم الفروع للميزات/الإصلاحات
- اسحب التحديثات قبل بدء العمل
- راجع `git status` بشكل متكرر

❌ **لا تفعل:**
- تثبيت بيانات حساسة (مفاتيح API، كلمات المرور)
- الدفع القسري إلى الفروع المشتركة
- تثبيت ملفات ثنائية كبيرة
- تجاهل تعارضات الدمج
- العمل مباشرة على main/master

---

## اتفاقية رسالة الالتزام

```
type(scope): subject

body (optional)

footer (optional)
```

**الأنواع:**
- `feat`: ميزة جديدة
- `fix`: إصلاح خطأ
- `docs`: توثيق
- `style`: تنسيق
- `refactor`: إعادة هيكلة الكود
- `test`: اختبارات
- `chore`: صيانة

**مثال:**
```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*آخر تحديث: يونيو 2025 | Git 2.x*
