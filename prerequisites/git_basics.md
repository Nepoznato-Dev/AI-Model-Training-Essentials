# Git Basics: Version Control for AI Projects 📦

**Time to complete:** 15 minutes  
**Prerequisites:** [Terminal Basics](./terminal_basics.md)

---

## What is Git?

**Git** is a version control system that tracks changes to your code. Think of it as "save points" for your projects.

**Why use it?**
- ✅ Track every change you make
- ✅ Undo mistakes easily
- ✅ Collaborate with others
- ✅ Backup your code online (GitHub)

---

## Installation

### Windows
1. Download from [git-scm.com](https://git-scm.com/download/win)
2. Run installer (default settings are fine)
3. Open "Git Bash" to use Git

### macOS
```bash
# Git is usually pre-installed, check with:
git --version

# If not installed:
xcode-select --install
```

### Linux
```bash
# Ubuntu/Debian
sudo apt install git

# Fedora/RHEL
sudo dnf install git
```

---

## First-Time Setup

Configure your identity (required!):

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"

# Verify settings
git config --list
```

---

## Core Concepts

### Repository (Repo)
A folder tracked by Git. Contains all your project files and history.

### Commit
A "save point" - a snapshot of your files at a moment in time.

### Branch
A parallel version of your project. Work on features without breaking main code.

### Remote
A copy of your repository on the internet (e.g., GitHub).

---

## Essential Commands

### 1. Create/Clone a Repository

```bash
# Initialize a new repo in current folder
git init

# Clone an existing repo (download from GitHub)
git clone https://github.com/username/project.git

# Clone into specific folder
git clone https://github.com/username/project.git my_folder
```

### 2. Check Status

```bash
# See what changed
git status

# See commit history
git log

# Compact history view
git log --oneline
```

### 3. Stage and Commit Changes

```bash
# Stage a specific file for commit
git add filename.py

# Stage all changes
git add .

# Stage all changes (including deletions)
git add -A

# Commit staged changes
git commit -m "Description of what you changed"

# Stage and commit in one step (tracked files only)
git commit -am "Quick fix"
```

### 4. Working with Remotes

```bash
# Connect local repo to remote
git remote add origin https://github.com/username/repo.git

# View remotes
git remote -v

# Upload commits to remote
git push origin main

# Download changes from remote
git pull origin main

# First-time push (set upstream)
git push -u origin main
```

### 5. Branching

```bash
# Create a new branch
git branch feature-name

# Switch to a branch
git checkout feature-name

# Create and switch in one command
git checkout -b feature-name

# List all branches
git branch

# Merge branch into current branch
git merge feature-name

# Delete a branch
git branch -d feature-name
```

### 6. Undoing Things

```bash
# Unstage a file (keep changes)
git reset HEAD filename.py

# Discard changes to a file
git checkout -- filename.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# ⚠️ Warning: --hard permanently deletes changes!
```

---

## Typical Workflow

### Starting a New Project

```bash
# 1. Create project folder
mkdir my_ai_project
cd my_ai_project

# 2. Initialize Git
git init

# 3. Create some files
echo "# My AI Project" > README.md

# 4. Stage and commit
git add README.md
git commit -m "Initial commit with README"

# 5. Create GitHub repo (do this on github.com)
# 6. Connect and push
git remote add origin https://github.com/yourusername/my_ai_project.git
git push -u origin main
```

### Daily Work Flow

```bash
# 1. Start work
cd my_project
git status                    # Check current state

# 2. Make changes to files...

# 3. Review changes
git diff                      # See what changed
git status                    # See which files changed

# 4. Stage related changes
git add file1.py file2.py

# 5. Commit with clear message
git commit -m "Add data preprocessing function"

# 6. Repeat steps 2-5 throughout the day

# 7. End of day: push to GitHub
git pull                      # Get any updates first
git push                      # Upload your work
```

---

## Writing Good Commit Messages

### Bad Examples ❌
```bash
git commit -m "fix"
git commit -m "stuff"
git commit -m "updated code"
```

### Good Examples ✅
```bash
git commit -m "Fix null pointer exception in data loader"
git commit -m "Add BERT model integration for text classification"
git commit -m "Refactor training loop for better readability"
```

### Commit Message Template
```
<type>: <subject>

<body - optional>

<footer - optional>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting (no logic changes)
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

---

## .gitignore: Files Git Should Ignore

Create a `.gitignore` file to exclude files from tracking:

```bash
# Python
__pycache__/
*.py[cod]
*.env
venv/
ai_env/

# Jupyter notebooks
.ipynb_checkpoints/

# Data files (usually too large)
*.csv
*.h5
data/

# Model checkpoints (too large)
checkpoints/
*.pth
*.pt
*.h5

# IDE files
.vscode/
.idea/
*.swp

# OS files
.DS_Store
Thumbs.db
```

---

## Common Errors & Fixes

### Error: "Please tell me who you are"
**Cause:** Haven't configured name/email  
**Fix:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Error: "fatal: remote origin already exists"
**Cause:** Remote already configured  
**Fix:**
```bash
# Update existing remote
git remote set-url origin https://github.com/newurl/repo.git

# Or remove and re-add
git remote remove origin
git remote add origin https://github.com/username/repo.git
```

### Error: "error: failed to push some refs"
**Cause:** Remote has commits you don't have locally  
**Fix:**
```bash
git pull --rebase
git push
```

### Error: "fatal: ref using is ambiguous"
**Cause:** Conflicting branch names  
**Fix:** Be more specific with branch name

---

## GitHub Quick Start

### Creating a Repository on GitHub

1. Go to [github.com](https://github.com)
2. Click "+" → "New repository"
3. Name it (e.g., `my-first-ai-project`)
4. Choose Public or Private
5. **Don't** initialize with README (you have local code)
6. Click "Create repository"
7. Follow the commands shown to connect your local repo

### Cloning Someone Else's Repo

```bash
# Clone this learning repository
git clone https://github.com/username/AI-Model-Training-Essentials.git

# Navigate into it
cd AI-Model-Training-Essentials

# Explore the guides!
```

---

## Practice Exercise

Let's practice the complete workflow:

```bash
# 1. Create and enter directory
mkdir git_practice
cd git_practice

# 2. Initialize Git
git init

# 3. Configure if needed
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 4. Create a file
echo "print('Hello AI World!')" > hello.py

# 5. Check status
git status

# 6. Stage the file
git add hello.py

# 7. Commit
git commit -m "Add Hello World script"

# 8. Create a branch
git checkout -b add-feature

# 9. Modify the file
echo "print('Now with features!')" >> hello.py

# 10. Commit the change
git add hello.py
git commit -m "Add new feature"

# 11. Switch back to main
git checkout main

# 12. Merge the feature
git merge add-feature

# 13. Clean up
git branch -d add-feature

# 14. View history
git log --oneline
```

---

## Git Cheat Sheet

| Command | What it does |
|---------|-------------|
| `git init` | Start a new repository |
| `git clone <url>` | Download a repository |
| `git status` | Show changed files |
| `git add <file>` | Stage file for commit |
| `git commit -m "msg"` | Save changes |
| `git push` | Upload to GitHub |
| `git pull` | Download from GitHub |
| `git branch` | List branches |
| `git checkout -b <name>` | Create and switch branch |
| `git merge <branch>` | Combine branches |
| `git log` | View commit history |
| `git diff` | See changes |

---

## Next Steps

✅ You now know Git basics!  
➡️ Ready to start the [RAG Guide](../guides/RAG/)  
➡️ Create your first AI project repository!

---

## Quick Quiz

**Q1:** What command stages all changes for commit?  
<details>
<summary>Click for answer</summary>
`git add .`
</details>

**Q2:** How do you create and switch to a new branch in one command?  
<details>
<summary>Click for answer</summary>
`git checkout -b branch-name`
</details>

**Q3:** What does `git push` do?  
<details>
<summary>Click for answer</summary>
Uploads your local commits to a remote repository (like GitHub)
</details>

**Q4:** Why use `.gitignore`?  
<details>
<summary>Click for answer</summary>
To tell Git which files/folders to ignore and not track
</details>

---

**Congratulations!** You're ready to use Git for your AI projects! 🎉
