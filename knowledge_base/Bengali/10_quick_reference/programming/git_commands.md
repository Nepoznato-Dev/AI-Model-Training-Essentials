---
# Metadata
title: "Git Commands Quick Reference"
description: "Git commands and workflows"
category: "Quick Reference"
subcategory: "Programming"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to programming/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [git, commands, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "16 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# গিট কমান্ড দ্রুত রেফারেন্স
সংস্করণ নিয়ন্ত্রণের জন্য প্রয়োজনীয় গিট কমান্ড।
---

## সেটআপ এবং কনফিগারেশন
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

## রিপোজিটরি ইনিশিয়ালাইজেশন
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

## মৌলিক কর্মপ্রবাহ
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

## শাখা প্রশাখা
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

## দূরবর্তী অপারেশন
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

## পরিবর্তনগুলি পূর্বাবস্থায় ফিরিয়ে আনা হচ্ছে
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

## লুকিয়ে রাখা
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

## ট্যাগ
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

## দেখা এবং অনুসন্ধান করা
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

## উন্নত অপারেশন
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

## পরিচ্ছন্নতা
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

## সাধারণ কর্মপ্রবাহ
### নতুন বৈশিষ্ট্য শুরু করুন```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... work ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# Create PR/MR on platform
```

### প্রধানের সাথে সিঙ্ক করুন```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# Resolve conflicts if any
git push --force-with-lease
```

### হটফিক্স ওয়ার্কফ্লো```bash
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

## .gitignore প্যাটার্নস
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

## কীবোর্ড শর্টকাট (গিট ব্যাশ)
| শর্টকাট | কর্ম |
|------------|---------|
| `Ctrl+R`| বিপরীত অনুসন্ধান ইতিহাস |
| `Tab`| স্বয়ংসম্পূর্ণ |
| `Ctrl+C`| কমান্ড বাতিল করুন |
| `Ctrl+Z`| প্রক্রিয়া স্থগিত করুন |
| `fg`| স্থগিত প্রক্রিয়া পুনরায় শুরু করুন |
---

## সর্বোত্তম অভ্যাস
✅ **করুন:**
- স্পষ্ট, বর্ণনামূলক কমিট বার্তা লিখুন
- লজিক্যাল গ্রুপিংয়ের সাথে ঘন ঘন কমিট করুন
- বৈশিষ্ট্য/ফিক্সের জন্য শাখা ব্যবহার করুন
- কাজ শুরু করার আগে টানুন
- প্রায়ই`git status`পর্যালোচনা করুন
❌ **করবেন না:**
- সংবেদনশীল ডেটা কমিট করুন (API কী, পাসওয়ার্ড)
- ভাগ করা শাখায় জোর করে পুশ করুন
- বড় বাইনারি ফাইল কমিট
- মার্জ দ্বন্দ্ব উপেক্ষা করুন
- সরাসরি প্রধান/মাস্টারে কাজ করুন
---

## কমিট মেসেজ কনভেনশন
```
type(scope): subject

body (optional)

footer (optional)
```

**প্রকার:**
-`feat`: নতুন বৈশিষ্ট্য
-`fix`: বাগ ফিক্স
-`docs`: ডকুমেন্টেশন
-`style`: ফরম্যাটিং
-`refactor`: কোড পুনর্গঠন
-`test`: পরীক্ষা
-`chore`: রক্ষণাবেক্ষণ
**উদাহরণ:**```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*শেষ আপডেট: জুলাই 2026 | Git 2.x*