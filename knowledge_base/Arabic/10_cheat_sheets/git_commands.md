# مرجع أوامر Git السريع

أوامر Git الأساسية للتحكم في الإصدارات.

---

## الإعداد والتكوين

```bash
# تكوين معلومات المستخدم
git config --global user.name "اسمك"
git config --global user.email "your.email@example.com"

# عرض التكوين
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

# استنساخ فرع محدد
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

# مرحلة الملفات
git add file.txt          # ملف محدد
git add .                 # جميع الملفات
git add *.py              # مطابقة النمط

# تأكيد التغييرات
git commit -m "رسالة الالتزام"
git commit -am "رسالة"  # مرحلة والتزام الملفات المتتبعة

# عرض سجل الالتزامات
git log
git log --oneline
git log --graph --oneline --all
```

---

## الفروع

```bash
# سرد الفروع
git branch                # الفروع المحلية
git branch -a             # جميع الفروع
git branch -r             # الفروع البعيدة

# إنشاء فرع
git branch branch-name
git checkout -b branch-name   # إنشاء والتبديل

# التبديل بين الفروع
git checkout branch-name
git switch branch-name        # صيغة أحدث

# إعادة تسمية الفرع الحالي
git branch -m new-name

# حذف فرع
git branch -d branch-name     # حذف آمن (مدمج)
git branch -D branch-name     # فرض الحذف

# دمج فرع
git merge branch-name

# إعادة أساس الفرع
git rebase main
```

---

## عمليات remote

```bash
# عرض remote
git remote -v

# إضافة remote
git remote add origin <url>

# جلب من remote
git fetch origin
git fetch --all

# سحب التغييرات (جلب + دمج)
git pull origin main
git pull --rebase origin main

# دفع التغييرات
git push origin main
git push -u origin main     # تعيين upstream
git push --force            # فرض الدفع (استخدم بحذر)
git push --force-with-lease # فرض دفع أكثر أمانًا

# دفع العلامات
git push --tags
```

---

## التراجع عن التغييرات

```bash
# إلغاء مرحلة الملف (الاحتفاظ بالتغييرات)
git reset HEAD file.txt
git restore --staged file.txt

# تجاهل تغييرات العمل
git checkout -- file.txt
git restore file.txt

# تعديل آخر التزام
git commit --amend -m "رسالة جديدة"
git commit --amend --no-edit

# عكس الالتزام (آمن للمستودعات المشتركة)
git revert commit-hash

# إعادة التعيين إلى الالتزام السابق
git reset --soft HEAD~1     # الاحتفاظ بالتغييرات مرحّلة
git reset --mixed HEAD~1    # الاحتفاظ بالتغييرات غير مرحّلة (افتراضي)
git reset --hard HEAD~1     # تجاهل جميع التغييرات (خطير)
```

---

## التخزين المؤقت

```bash
# حفظ العمل قيد التقدم
git stash
git stash save "رسالة"

# سرد المخزونات
git stash list

# تطبيق المخزون
git stash apply             # الأحدث
git stash apply stash@{1}   # مخزون محدد

# تطبيق وإزالة
git stash pop

# إسقاط المخزون
git stash drop stash@{1}

# مسح جميع المخزونات
git stash clear
```

---

## العلامات

```bash
# سرد العلامات
git tag
git tag -l "v1.*"

# إنشاء علامة
git tag v1.0.0
git tag -a v1.0.0 -m "الإصدار 1.0.0"  # علامة مشروحة

# 체크아웃 علامة
git checkout v1.0.0

# حذف علامة
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## العرض والبحث

```bash
# عرض تفاصيل الالتزام
git show commit-hash
git show --stat commit-hash

# اللوم (من غيّر ماذا)
git blame file.txt

# البحث في الالتزامات
git log --grep="كلمة مفتاحية"
git log --author="اسم"

# البحث عن كود في السجل
git log -S"اسم_الدالة"

# عرض ملف في التزام محدد
git show commit-hash:file.txt
```

---

## العمليات المتقدمة

```bash
# انتقاء الكرز
git cherry-pick commit-hash

# إعادة أساس تفاعلية
git rebase -i HEAD~5

# ضغط الالتزامات (أثناء إعادة الأساس)
# تغيير 'pick' إلى 'squash' أو 's' في المحرر

# إنشاء رقعة
git format-patch -1 commit-hash

# تطبيق رقعة
git apply patch-file.patch
git am patch-file.patch

# الوحدات الفرعية
git submodule add <url> path
git submodule update --init --recursive
```

---

## التنظيف

```bash
# إزالة الملفات غير المتتبعة (تجربة جافة)
git clean -n
git clean -f                # إزالة فعلية

# إزالة الدلائل غير المتتبعة
git clean -fd

# تشذيب الفروع البعيدة المحذوفة
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
# ... عمل ...
git add .
git commit -m "إضافة ميزة جديدة"
git push -u origin feature/new-feature
# إنشاء PR/MR على المنصة
```

### المزامنة مع Main
```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# حل التعارضات إن وجدت
git push --force-with-lease
```

### سير عمل الإصلاح العاجل
```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... إصلاح ...
git commit -am "إصلاح خلل حرج"
git checkout main
git merge hotfix/urgent-fix
git push
git tag v1.0.1
git push --tags
```

---

## أنماط .gitignore

```gitignore
# تجاهل ملف محدد
filename.txt

# تجاهل جميع ملفات .log
*.log

# تجاهل دليل
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
- التزم بشكل متكرر مع تجميعات منطقية
- استخدم الفروع للميزات/الإصلاحات
- اسحب قبل البدء في العمل
- راجع `git status` غالبًا

❌ **لا تفعل:**
- التزم ببيانات حساسة (مفاتيح API، كلمات مرور)
- افرض الدفع إلى الفروع المشتركة
- التزم بملفات ثنائية كبيرة
- تجاهل تعارضات الدمج
- اعمل مباشرة على main/master

---

## اتفاقية رسالة الالتزام

```\nالنوع(النطاق): الموضوع\n\nالجسم (اختياري)\n\nالتذييل (اختياري)\n```\n\n**الأنواع:**
- `feat`: ميزة جديدة
- `fix`: إصلاح خلل
- `docs`: توثيق
- `style`: تنسيق
- `refactor`: إعادة هيكلة الكود
- `test`: اختبارات
- `chore`: صيانة

**مثال:**
```\nfeat(auth): إضافة وظيفة إعادة تعيين كلمة المرور\n\nتنفيذ إعادة تعيين كلمة المرور عبر البريد الإلكتروني مع\nرمز قائم على التحقق. تنتهي صلاحية الرمز بعد 24 ساعة.\n\nيغلق #123\n```\n

---

*آخر تحديث: يونيو 2025 | Git 2.x*
