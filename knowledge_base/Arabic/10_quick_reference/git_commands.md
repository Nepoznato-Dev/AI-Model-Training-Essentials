---
# البيانات الوصفية
العنوان: "مرجع سريع لأوامر Git"
الوصف: "أوامر Git ومهام سير العمل"
الفئة: "مرجع سريع"
الإصدار: "1.0.0"
الحالة: "نشط"
#مساهمة
المؤلفين:
  - الاسم: "فريق تدريب نموذج الذكاء الاصطناعي"
    البريد الإلكتروني: ""
    الدور: "original_author"
المساهمين: []
سجل التغيير:
  - الإصدار: "1.0.0"
    التاريخ: "2026-08-05"
    المؤلف: "فريق تدريب نموذج الذكاء الاصطناعي"
    التغييرات: "تمت إضافة بيانات تعريف YAML الأمامية لتتبع المساهمين"
# مراجعة
تم الإنشاء: "05-08-2026"
آخر_تعديل: "05-08-2026"
تاريخ_المراجعة: "05-02-2027"
review_by: "فريق قاعدة المعرفة المرجعية السريعة"
next_review: "2027-08-05"
# التصنيف
العلامات: [جيت، أوامر، مرجع سريع]
مستوى الصعوبة: "مبتدئ"
المتطلبات الأساسية: []
وقت_القراءة المقدر: "16 دقيقة"
# دليل المساهمة
المساهمة:
  الترخيص: "MIT"
  Feedback_channel: "مشكلات GitHub"
  how_to_contribute: "أرسل رسالة عامة تحتوي على التغييرات وقم بتحديث سجل التغييرات"
  review_process: "تتم مراجعة التغييرات بواسطة مشرفي الفئة قبل الدمج"
---
# مرجع سريع لأوامر Git
أوامر Git الأساسية للتحكم في الإصدار.
---

## الإعداد والتكوين
```bash
# Configure user info
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# View configuration
git config --list
git config user.name

# Set default branch name
git config --global init.defaultBranch main
```

---

## تهيئة المستودع
```bash
# Initialize new repository
git init

# Clone existing repository
git clone <url>
git clone <url> folder-name

# Clone specific branch
git clone -b branch-name <url>
```

---

## سير العمل الأساسي
```bash
# Check status
git status

# View changes
git diff
git diff --staged

# Stage files
git add file.txt          # Specific file
git add .                 # All files
git add *.py              # Pattern match

# Commit changes
git commit -m "Commit message"
git commit -am "Message"  # Stage and commit tracked files

# View commit history
git log
git log --oneline
git log --graph --oneline --all
```

---

## المتفرعة
```bash
# List branches
git branch                # Local branches
git branch -a             # All branches
git branch -r             # Remote branches

# Create branch
git branch branch-name
git checkout -b branch-name   # Create and switch

# Switch branches
git checkout branch-name
git switch branch-name        # Newer syntax

# Rename current branch
git branch -m new-name

# Delete branch
git branch -d branch-name     # Safe delete (merged)
git branch -D branch-name     # Force delete

# Merge branch
git merge branch-name

# Rebase branch
git rebase main
```

---

## العمليات عن بعد
```bash
# View remotes
git remote -v

# Add remote
git remote add origin <url>

# Fetch from remote
git fetch origin
git fetch --all

# Pull changes (fetch + merge)
git pull origin main
git pull --rebase origin main

# Push changes
git push origin main
git push -u origin main     # Set upstream
git push --force            # Force push (use carefully)
git push --force-with-lease # Safer force push

# Push tags
git push --tags
```

---

## التراجع عن التغييرات
```bash
# Unstage file (keep changes)
git reset HEAD file.txt
git restore --staged file.txt

# Discard working changes
git checkout -- file.txt
git restore file.txt

# Amend last commit
git commit --amend -m "New message"
git commit --amend --no-edit

# Revert commit (safe for shared repos)
git revert commit-hash

# Reset to previous commit
git reset --soft HEAD~1     # Keep changes staged
git reset --mixed HEAD~1    # Keep changes unstaged (default)
git reset --hard HEAD~1     # Discard all changes (dangerous)
```

---

## التخبئة
```bash
# Save work in progress
git stash
git stash save "message"

# List stashes
git stash list

# Apply stash
git stash apply             # Most recent
git stash apply stash@{1}   # Specific stash

# Apply and remove
git stash pop

# Drop stash
git stash drop stash@{1}

# Clear all stashes
git stash clear
```

---

## العلامات
```bash
# List tags
git tag
git tag -l "v1.*"

# Create tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # Annotated tag

# Checkout tag
git checkout v1.0.0

# Delete tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## المشاهدة والبحث
```bash
# Show commit details
git show commit-hash
git show --stat commit-hash

# Blame (who changed what)
git blame file.txt

# Search commits
git log --grep="keyword"
git log --author="name"

# Search code in history
git log -S"function_name"

# View file at specific commit
git show commit-hash:file.txt
```

---

## العمليات المتقدمة
```bash
# Cherry-pick commit
git cherry-pick commit-hash

# Interactive rebase
git rebase -i HEAD~5

# Squash commits (during rebase)
# Change 'pick' to 'squash' or 's' in editor

# Create patch
git format-patch -1 commit-hash

# Apply patch
git apply patch-file.patch
git am patch-file.patch

# Submodules
git submodule add <url> path
git submodule update --init --recursive
```

---

## تنظيف
```bash
# Remove untracked files (dry run)
git clean -n
git clean -f                # Actually remove

# Remove untracked directories
git clean -fd

# Prune deleted remote branches
git fetch --prune
git remote prune origin
```

---

## سير العمل المشترك
### بدء ميزة جديدة```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... work ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# Create PR/MR on platform
```

### المزامنة مع Main```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# Resolve conflicts if any
git push --force-with-lease
```

### سير عمل الإصلاح العاجل```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... fix ...
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
# Ignore specific file
filename.txt

# Ignore all .log files
*.log

# Ignore directory
node_modules/
__pycache__/

# Negate (include despite earlier pattern)
!important.log

# Comment
# This is a comment
```

---

## اختصارات لوحة المفاتيح (Git Bash)
| الاختصار | العمل |
|----------|--------|
|  __محمي_0__ | عكس سجل البحث |
|  __محمي_1__ | الإكمال التلقائي |
|  __محمي_2__ | إلغاء الأمر |
|  __محمي_3__ | تعليق العملية |
|  __محمي_4__ | استئناف العملية المعلقة |
---

## أفضل الممارسات
✅ **افعل:**
- كتابة رسائل التزام واضحة ووصفية
- الالتزام بشكل متكرر بالمجموعات المنطقية
- استخدم الفروع للميزات/الإصلاحات
- السحب قبل البدء بالعمل
- قم بمراجعة`git status`كثيرًا
❌ **لا تفعل:**
- ارتكاب البيانات الحساسة (مفاتيح API وكلمات المرور)
- دفع القوة إلى الفروع المشتركة
- ارتكاب ملفات ثنائية كبيرة
- تجاهل تعارضات الدمج
- العمل مباشرة على الرئيسي/الماجستير
---

## الالتزام باتفاقية الرسالة
```
type(scope): subject

body (optional)

footer (optional)
```

**الأنواع:**
- __محمي_0__ : ميزة جديدة
- __محمي_1__ : إصلاح الخلل
- __محمي_2__ : التوثيق
- __محمي_3__ : التنسيق
- __محمي_4__: إعادة هيكلة الكود
- __محمي_5__ : الاختبارات
- __محمي_6__ : الصيانة
**مثال:**```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*آخر تحديث: يوليو 2026 | بوابة 2.x*