# Git Basics for AI Development

**Time needed:** 10-15 minutes  
**Goal:** Learn to clone, navigate, and manage code repositories

---

## What is Git?

**Git** is a version control system that tracks changes to your code over time. Think of it as "save points" for your projects.

**Why learn it?**
- ✅ Download AI projects from GitHub
- ✅ Track your own code changes
- ✅ Collaborate with others
- ✅ Revert mistakes easily

---

## Installing Git

### On Windows:
1. Download from [git-scm.com](https://git-scm.com/downloads)
2. Run the installer (default settings are fine)
3. Open **Git Bash** after installation

### On Mac:
```bash
# Open Terminal and run:
git --version
# If not installed, it will prompt you to install
```

Or install with Homebrew:
```bash
brew install git
```

### On Linux:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install git

# Fedora/CentOS
sudo dnf install git
```

### Verify Installation:
```bash
git --version
# Output example: git version 2.40.1
```

---

## First-Time Setup

Configure your identity (only do this once):

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email (use the one associated with GitHub)
git config --global user.email "your.email@example.com"

# Verify settings
git config --list
```

---

## Essential Git Commands

### 1. Clone a Repository (Download Code)

This is what you'll use most often!

```bash
# Clone this AI training repository
cd ~
mkdir ai_projects
cd ai_projects

git clone https://github.com/username/repo-name.git

# Navigate into the cloned folder
cd repo-name

# See what's inside
ls
```

**Example with our repository:**
```bash
git clone https://github.com/yourusername/AI-Model-Training-Essentials.git
cd AI-Model-Training-Essentials
```

---

### 2. Check Status

See what files have changed:

```bash
git status
```

**Output example:**
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

If you've made changes:
```
Changes not staged for commit:
  modified:   README.md

Untracked files:
  my_new_file.py
```

---

### 3. View History

See past changes:

```bash
# Show recent commits
git log

# Show last 5 commits
git log -5

# Compact view
git log --oneline
```

**Output example:**
```
commit a1b2c3d (HEAD -> main, origin/main)
Author: Your Name <your.email@example.com>
Date:   Mon Jan 15 10:30:00 2026

    Add RAG project files
```

---

### 4. Pull Latest Changes

Update your local copy with the latest from GitHub:

```bash
git pull
```

**When to use:** Before starting work or if someone else updated the repository.

---

### 5. Create a New Branch

Work on features without breaking the main code:

```bash
# Create and switch to a new branch
git checkout -b my-feature

# Modern alternative
git switch -c my-feature
```

**Why branch?** 
- Experiment safely
- Work on multiple features
- Keep main stable

---

### 6. Stage and Commit Changes

Save your work:

```bash
# Stage a specific file
git add myfile.py

# Stage all changed files
git add .

# Commit with a message
git commit -m "Add new feature: data preprocessing"
```

**Commit message tips:**
- ✅ "Fix bug in data loader"
- ✅ "Add CNN architecture chapter"
- ❌ "stuff"
- ❌ "update"

---

### 7. Push Changes to GitHub

Upload your commits:

```bash
# Push current branch
git push origin my-feature

# If it's your first time pushing a new branch
git push -u origin my-feature
```

---

## Common Workflows

### Workflow 1: Downloading and Updating a Project

```bash
# 1. Clone the repository
git clone https://github.com/username/project.git
cd project

# 2. Make your changes (edit files, add code, etc.)

# 3. Check what changed
git status

# 4. Save your changes
git add .
git commit -m "My improvements"

# 5. Get latest from remote first
git pull

# 6. Upload your changes
git push
```

---

### Workflow 2: Starting a New Feature

```bash
# 1. Make sure you're on main branch
git checkout main

# 2. Update to latest
git pull

# 3. Create a feature branch
git checkout -b add-rag-examples

# 4. Work on your feature (edit files)

# 5. Commit your progress
git add .
git commit -m "Add RAG example 1"

# 6. Push your branch
git push -u origin add-rag-examples
```

---

### Workflow 3: Fixing Conflicts

Sometimes Git can't automatically merge changes. Don't panic!

```bash
# 1. Try to pull
git pull

# You might see:
# CONFLICT (content): Merge conflict in myfile.py

# 2. Open the conflicted file
# Look for markers like this:
# <<<<<<< HEAD
# Your changes
# =======
# Their changes
# >>>>>>> branch-name

# 3. Edit the file to keep what you want
# Remove the marker lines (<<<<<<, ======, >>>>>>)

# 4. Stage the resolved file
git add myfile.py

# 5. Complete the merge
git commit -m "Resolve merge conflict"
```

---

## .gitignore Files

Some files shouldn't be tracked (like large datasets or passwords).

Create a `.gitignore` file:

```bash
# Create the file
touch .gitignore

# Edit it to add patterns to ignore
```

**Common .gitignore entries:**
```
# Python
__pycache__/
*.py[cod]
.env
venv/

# Jupyter notebooks
.ipynb_checkpoints/

# Large data files
*.h5
*.pkl
data/*.csv

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db
```

---

## Undoing Mistakes

### Undo staged changes (before commit):
```bash
git restore --staged myfile.py
```

### Discard local changes (be careful!):
```bash
git restore myfile.py
```

### Undo last commit (keep changes):
```bash
git reset --soft HEAD~1
```

### Go back to a previous version:
```bash
# Find the commit hash
git log --oneline

# Reset to that commit
git reset --hard abc1234
```

⚠️ **Warning:** `--hard` permanently deletes changes!

---

## Git with GitHub

### Create a GitHub Account:
1. Go to [github.com](https://github.com)
2. Sign up for free
3. Verify your email

### Connect Git to GitHub:

**Option 1: HTTPS (easier)**
```bash
git clone https://github.com/username/repo.git
# Will ask for username/password or token
```

**Option 2: SSH (more convenient long-term)**
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Copy the public key
cat ~/.ssh/id_ed25519.pub

# Add to GitHub: Settings → SSH and GPG keys → New SSH key
```

---

## Practice Exercise

Let's practice the complete workflow:

```bash
# 1. Create a test repository on GitHub (go to github.com/new)
# Name it "git-practice"

# 2. Clone it
cd ~
git clone https://github.com/yourusername/git-practice.git
cd git-practice

# 3. Create a file
echo "# My Git Practice" > README.md
echo "print('Hello, AI World!')" > hello.py

# 4. Check status
git status

# 5. Stage and commit
git add .
git commit -m "Initial commit: add README and hello script"

# 6. Push to GitHub
git push -u origin main

# 7. Refresh GitHub in your browser - you should see your files!
```

---

## Quick Reference Card

```bash
# Setup (one-time)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Getting code
git clone <url>              # Download repository
git pull                     # Update local copy

# Checking status
git status                   # See changed files
git log                      # View history
git log --oneline           # Compact history

# Making changes
git add <file>              # Stage a file
git add .                   # Stage all files
git commit -m "message"     # Save changes

# Branches
git branch                  # List branches
git checkout -b <name>      # Create & switch to branch
git checkout <name>         # Switch to branch
git branch -d <name>        # Delete branch

# Sharing
git push                    # Upload commits
git push -u origin <branch> # First push of new branch

# Undoing
git restore <file>          # Discard local changes
git reset --soft HEAD~1     # Undo last commit
```

---

## Common Problems & Solutions

### Problem: "Permission denied (publickey)"
**Solution:** Set up SSH keys or use HTTPS instead.

### Problem: "error: failed to push some refs"
**Solution:** Run `git pull` first, resolve conflicts, then push again.

### Problem: "fatal: not a git repository"
**Solution:** You're not in a git folder. Use `cd` to navigate to the cloned repository.

### Problem: Forgot to add a file before committing
**Solution:** 
```bash
git add forgotten_file.py
git commit --amend --no-edit
```

---

## Next Steps

✅ You now know Git basics! Continue by:

1. **Practice:** Complete the exercise above
2. **Explore:** Browse GitHub for AI projects
3. **Contribute:** Fork a project and make improvements
4. **Move forward:** Start your first AI guide!

---

## Helpful Resources

- [GitHub Docs](https://docs.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Learn Git Branching (Interactive)](https://learngitbranching.js.org/)
- [Visual Git Reference](https://marklodato.github.io/visual-git-guide/index-en.html)

---

**Congratulations!** You're ready to work with Git and GitHub. 🎉

Now you can clone this repository and start learning AI!

```bash
git clone https://github.com/yourusername/AI-Model-Training-Essentials.git
```
