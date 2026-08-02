# Terminal Basics: Your First Steps 🖥️

**Time to complete:** 10 minutes  
**Prerequisites:** None - absolute beginners start here!

---

## What is a Terminal?

A **terminal** (also called command line, shell, or console) is a text-based way to talk to your computer. Instead of clicking icons, you type commands.

**Why learn it?** AI tools and servers often require terminal commands. It's faster and more powerful than clicking!

---

## Opening the Terminal

### Windows
1. Press `Windows Key + R`
2. Type `cmd` and press Enter
3. Or search for "Command Prompt" or "PowerShell"

### macOS
1. Press `Cmd + Space` (Spotlight)
2. Type `Terminal` and press Enter
3. Or find it in Applications → Utilities → Terminal

### Linux
1. Press `Ctrl + Alt + T`
2. Or search for "Terminal" in your applications menu

---

## Essential Commands

### 1. Where Am I? (`pwd`)
```bash
pwd
```
**Output:** Shows your current directory (folder)  
**Example:** `/home/username` or `C:\Users\username`

### 2. What's Here? (`ls` or `dir`)
```bash
# Mac/Linux
ls

# Windows
dir
```
**Output:** Lists all files and folders in current location

**Pro tip:** `ls -la` (Mac/Linux) shows hidden files and details

### 3. Change Directory (`cd`)
```bash
# Go to a folder
cd Documents

# Go up one level
cd ..

# Go home
cd ~    # Mac/Linux
cd %USERPROFILE%  # Windows

# Go to specific path
cd /path/to/folder
```

### 4. Make a New Folder (`mkdir`)
```bash
mkdir my_project
```

### 5. Remove Files/Folders (`rm` or `del`)
```bash
# Mac/Linux - remove file
rm filename.txt

# Mac/Linux - remove folder (CAREFUL!)
rm -rf foldername

# Windows - remove file
del filename.txt

# Windows - remove folder
rmdir /s foldername
```

⚠️ **Warning:** Terminal deletions are permanent! No recycle bin!

### 6. Copy Files (`cp` or `copy`)
```bash
# Mac/Linux
cp source.txt destination.txt

# Windows
copy source.txt destination.txt
```

### 7. Move/Rename Files (`mv` or `move`)
```bash
# Mac/Linux - move
mv file.txt /other/folder/

# Mac/Linux - rename
mv old_name.txt new_name.txt

# Windows - move
move file.txt C:\other\folder\

# Windows - rename
ren old_name.txt new_name.txt
```

### 8. View File Contents (`cat` or `type`)
```bash
# Mac/Linux
cat filename.txt

# Windows
type filename.txt
```

---

## Navigation Quick Reference

```
Current directory     →  .
Parent directory      →  ..
Home directory        →  ~ (Mac/Linux) or %USERPROFILE% (Windows)
Root directory        →  / (Mac/Linux) or C:\ (Windows)
```

---

## Practice Exercise

Try this sequence:

```bash
# 1. Check where you are
pwd

# 2. List what's here
ls

# 3. Create a practice folder
mkdir terminal_practice

# 4. Go into it
cd terminal_practice

# 5. Create an empty file
touch test.txt          # Mac/Linux
type nul > test.txt     # Windows

# 6. Verify it exists
ls

# 7. Go back
cd ..

# 8. Remove the practice folder
rm -rf terminal_practice    # Mac/Linux
rmdir /s terminal_practice  # Windows
```

---

## Common Errors & Fixes

### Error: "No such file or directory"
**Cause:** You're trying to access something that doesn't exist  
**Fix:** Check spelling with `ls` first

### Error: "Permission denied"
**Cause:** You don't have rights to modify this file/folder  
**Fix:** Don't use `sudo` unless you know what you're doing!

### Error: "command not found"
**Cause:** Typo or command doesn't exist  
**Fix:** Check spelling, remember Mac/Linux commands differ from Windows

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Auto-complete (magic time-saver!) |
| `Ctrl + C` | Stop running command |
| `Ctrl + D` | Exit terminal |
| `↑` / `↓` | Previous/next commands |
| `Clear` or `Ctrl + L` | Clear screen |

---

## Next Steps

✅ You now know terminal basics!  
➡️ Next: [Python Basics](./python_basics.md)  
➡️ Then: [Git Basics](./git_basics.md)

---

## Quick Quiz

**Q1:** What command shows your current directory?  
<details>
<summary>Click for answer</summary>
`pwd` (Mac/Linux) or `cd` (Windows)
</details>

**Q2:** How do you list files in a folder?  
<details>
<summary>Click for answer</summary>
`ls` (Mac/Linux) or `dir` (Windows)
</details>

**Q3:** What does `cd ..` do?  
<details>
<summary>Click for answer</summary>
Moves up one directory level
</details>

---

**Congratulations!** You've learned the essential terminal commands used by every developer! 🎉
