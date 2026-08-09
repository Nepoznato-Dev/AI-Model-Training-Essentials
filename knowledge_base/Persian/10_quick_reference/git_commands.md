---
# فراداده
عنوان: "مرجع سریع دستورات Git"
توضیحات: "فرمان های Git و گردش کار"
دسته بندی: "مرجع سریع"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش مرجع سریع"
next_review: "05-08-2027"
# طبقه بندی
برچسب‌ها: [git، دستورات، مرجع سریع]
سطح سختی: "مبتدی"
پیش نیاز: []
تخمینی_زمان_خواندن: "16 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
# مرجع سریع دستورات Git
دستورات ضروری Git برای کنترل نسخه.
---

## راه اندازی و پیکربندی
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

## مقداردهی اولیه مخزن
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

## گردش کار پایه
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

## انشعاب
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

## عملیات از راه دور
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

## لغو تغییرات
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

## پنهان کردن
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

## برچسب ها
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

## مشاهده و جستجو
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

## عملیات پیشرفته
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

## پاکسازی
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

## گردش کار رایج
### ویژگی جدید را شروع کنید```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... work ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# Create PR/MR on platform
```

### همگام سازی با اصلی```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# Resolve conflicts if any
git push --force-with-lease
```

### گردش کار رفع فوری```bash
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

## الگوهای gitignore
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

## میانبرهای صفحه کلید (Git Bash)
| میانبر | اقدام |
|----------|--------|
| `Ctrl+R`| تاریخچه جستجو معکوس |
|  __محافظت شده_1__ | تکمیل خودکار |
| `Ctrl+C`| فرمان لغو |
|  __محافظت شده_3__ | تعلیق فرآیند |
| `fg`| از سرگیری روند معلق |
---

## بهترین شیوه ها
✅ ** انجام:**
- پیام های تعهدی واضح و توصیفی بنویسید
- به طور مکرر با گروه بندی های منطقی متعهد شوید
- از شاخه ها برای ویژگی ها/اصلاحات استفاده کنید
- قبل از شروع کار بکشید
- اغلب`git status`را مرور کنید
❌ **نکن:**
- داده های حساس (کلیدهای API، کلمه عبور)
- فشار اجباری به شاخه های مشترک
- فایل های باینری بزرگ را متعهد کنید
- تضادهای ادغام را نادیده بگیرید
- مستقیماً روی main/master کار کنید
---

## کنوانسیون پیام متعهد
```
type(scope): subject

body (optional)

footer (optional)
```

**انواع:**
-`feat`: ویژگی جدید
- `fix`: رفع اشکال
-`docs`: مستندات
-`style`: قالب بندی
- `refactor`: بازسازی کد
-`test`: تست ها
-`chore`: تعمیر و نگهداری
**مثال:**```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*آخرین به روز رسانی: جولای 2026 | Git 2.x*