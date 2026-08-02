# Terminal Basics for AI Development

**Time needed:** 5-10 minutes  
**Goal:** Learn to navigate your computer using the command line

---

## What is a Terminal?

The **terminal** (also called "command line" or "shell") is a text-based way to interact with your computer. Instead of clicking icons, you type commands.

**Why learn it?** Most AI tools and tutorials assume you can use the terminal. It's faster and more powerful than using a mouse!

---

## Opening the Terminal

### On Windows:
1. Press `Windows Key + R`
2. Type `cmd` or `powershell`
3. Press Enter

**Better option:** Install [Git Bash](https://git-scm.com/downloads) for a Unix-like experience.

### On Mac:
1. Press `Cmd + Space` (Spotlight search)
2. Type `Terminal`
3. Press Enter

### On Linux:
1. Press `Ctrl + Alt + T`
2. Or search for "Terminal" in your applications menu

---

## Essential Commands

### 1. See Where You Are: `pwd` (Print Working Directory)

```bash
pwd
```

**Output example:**
```
/home/username/documents
```

This shows your current folder location.

---

### 2. List Files: `ls` (List)

```bash
ls
```

**Output example:**
```
file1.txt  folder1  script.py
```

To see more details:
```bash
ls -la
```

---

### 3. Change Directory: `cd` (Change Directory)

**Go into a folder:**
```bash
cd folder_name
```

**Go up one level:**
```bash
cd ..
```

**Go to your home folder:**
```bash
cd ~
```

**Example navigation:**
```bash
pwd              # Shows: /home/username
cd documents     # Go into documents folder
pwd              # Shows: /home/username/documents
cd ..            # Go back up
pwd              # Shows: /home/username
```

---

### 4. Make a New Folder: `mkdir` (Make Directory)

```bash
mkdir my_project
```

Then go into it:
```bash
cd my_project
```

---

### 5. Create an Empty File: `touch`

```bash
touch myfile.py
```

Now verify it exists:
```bash
ls
```

---

### 6. Run a Python Script

```bash
python myfile.py
```

Or on some systems:
```bash
python3 myfile.py
```

---

### 7. Clear the Screen: `clear`

```bash
clear
```

Or press `Ctrl + L`

---

### 8. Get Help: `--help`

Most commands have built-in help:

```bash
python --help
pip --help
```

---

## Practice Exercise

Try this sequence (type each line and press Enter):

```bash
# 1. See where you are
pwd

# 2. Go to your home folder
cd ~

# 3. Create a practice folder
mkdir ai_practice

# 4. Go into it
cd ai_practice

# 5. Create a Python file
touch test.py

# 6. Verify it's there
ls

# 7. Go back up
cd ..

# 8. List to see your new folder
ls
```

**Expected final output:** You should see `ai_practice` in the list!

---

## Common Problems & Solutions

### Problem: "Command not found"
**Solution:** Check your spelling. Commands are case-sensitive!

### Problem: "No such file or directory"
**Solution:** Use `ls` to check what files/folders exist first.

### Problem: "Permission denied"
**Solution:** You're trying to modify a system folder. Stay in your home folder (`~`) or folders you created.

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Auto-complete (try typing `cd doc` then press Tab!) |
| `↑` (Up Arrow) | Previous command (very useful!) |
| `↓` (Down Arrow) | Next command |
| `Ctrl + C` | Stop a running command |
| `Ctrl + L` | Clear screen |

---

## Next Steps

✅ You now know the basics! Practice by:
1. Creating a folder structure for your AI projects
2. Navigating between folders without using your mouse
3. Running Python scripts from the terminal

**Ready for more?** Move on to [Python Basics](python_basics.md)

---

## Quick Reference Card

```bash
pwd          # Show current location
ls           # List files
cd folder    # Enter a folder
cd ..        # Go up one level
mkdir name   # Create a folder
touch file   # Create a file
python file.py  # Run Python
clear        # Clear screen
```

Keep this handy until the commands become muscle memory!
