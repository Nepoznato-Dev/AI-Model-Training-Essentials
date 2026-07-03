# Git 指令快速參考

版本控制的必備 Git 指令。

---

## 設定與配置

```bash
# 配置使用者資訊
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 檢視配置
git config --list
git config user.name

# 設定預設分支名稱
git config --global init.defaultBranch main
```

---

## 儲存庫初始化

```bash
# 初始化新儲存庫
git init

# 複製現有儲存庫
git clone <url>
git clone <url> folder-name

# 複製特定分支
git clone -b branch-name <url>
```

---

## 基本工作流程

```bash
# 檢查狀態
git status

# 檢視變更
git diff
git diff --staged

# 暫存檔案
git add file.txt          # 特定檔案
git add .                 # 所有檔案
git add *.py              # 模式匹配

# 提交變更
git commit -m "Commit message"
git commit -am "Message"  # 暫存並提交已追蹤的檔案

# 檢視提交歷史
git log
git log --oneline
git log --graph --oneline --all
```

---

## 分支操作

```bash
# 列出分支
git branch                # 本地分支
git branch -a             # 所有分支
git branch -r             # 遠端分支

# 建立分支
git branch branch-name
git checkout -b branch-name   # 建立並切換

# 切換分支
git checkout branch-name
git switch branch-name        # 較新的語法

# 重新命名目前分支
git branch -m new-name

# 刪除分支
git branch -d branch-name     # 安全刪除（已合併）
git branch -D branch-name     # 強制刪除

# 合併分支
git merge branch-name

# 變基分支
git rebase main
```

---

## 遠端操作

```bash
# 檢視遠端儲存庫
git remote -v

# 新增遠端儲存庫
git remote add origin <url>

# 從遠端獲取
git fetch origin
git fetch --all

# 拉取變更（獲取 + 合併）
git pull origin main
git pull --rebase origin main

# 推送變更
git push origin main
git push -u origin main     # 設定上游
git push --force            # 強制推送（謹慎使用）
git push --force-with-lease # 更安全的強制推送

# 推送標籤
git push --tags
```

---

## 復原變更

```bash
# 取消暫存檔案（保留變更）
git reset HEAD file.txt
git restore --staged file.txt

# 捨棄工作區變更
git checkout -- file.txt
git restore file.txt

# 修改最後一次提交
git commit --amend -m "New message"
git commit --amend --no-edit

# 還原提交（適用於共享儲存庫）
git revert commit-hash

# 重設至先前提交
git reset --soft HEAD~1     # 保留變更為已暫存
git reset --mixed HEAD~1    # 保留變更為未暫存（預設）
git reset --hard HEAD~1     # 捨棄所有變更（危險）
```

---

## 暫存

```bash
# 儲存進行中的工作
git stash
git stash save "message"

# 列出暫存
git stash list

# 套用暫存
git stash apply             # 最近的暫存
git stash apply stash@{1}   # 特定暫存

# 套用並移除
git stash pop

# 丟棄暫存
git stash drop stash@{1}

# 清除所有暫存
git stash clear
```

---

## 標籤

```bash
# 列出標籤
git tag
git tag -l "v1.*"

# 建立標籤
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"  # 附註標籤

# 檢出標籤
git checkout v1.0.0

# 刪除標籤
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## 檢視與搜尋

```bash
# 顯示提交詳情
git show commit-hash
git show --stat commit-hash

# Blame（誰改了什麼）
git blame file.txt

# 搜尋提交
git log --grep="keyword"
git log --author="name"

# 在歷史記錄中搜尋程式碼
git log -S"function_name"

# 檢視特定提交的檔案
git show commit-hash:file.txt
```

---

## 進階操作

```bash
# Cherry-pick 提交
git cherry-pick commit-hash

# 互動式變基
git rebase -i HEAD~5

# 壓縮提交（在變基過程中）
# 在編輯器中將 'pick' 改為 'squash' 或 's'

# 建立補丁
git format-patch -1 commit-hash

# 套用補丁
git apply patch-file.patch
git am patch-file.patch

# 子模組
git submodule add <url> path
git submodule update --init --recursive
```

---

## 清理

```bash
# 移除未追蹤的檔案（模擬執行）
git clean -n
git clean -f                # 實際移除

# 移除未追蹤的目錄
git clean -fd

# 清理已刪除的遠端分支
git fetch --prune
git remote prune origin
```

---

## 常見工作流程

### 開始新功能
```bash
git checkout main
git pull
git checkout -b feature/new-feature
# ... 工作 ...
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
# 在平台上建立 PR/MR
```

### 與主分支同步
```bash
git checkout feature-branch
git fetch origin
git rebase origin/main
# 如有衝突則解決
git push --force-with-lease
```

### 熱修復工作流程
```bash
git checkout main
git pull
git checkout -b hotfix/urgent-fix
# ... 修復 ...
git commit -am "Fix critical bug"
git checkout main
git merge hotfix/urgent-fix
git push
git tag v1.0.1
git push --tags
```

---

## .gitignore 模式

```gitignore
# 忽略特定檔案
filename.txt

# 忽略所有 .log 檔案
*.log

# 忽略目錄
node_modules/
__pycache__/

# 否定（包含，儘管有先前的模式）
!important.log

# 註解
# 這是註解
```

---

## 鍵盤快捷鍵（Git Bash）

| 快捷鍵 | 動作 |
|----------|--------|
| `Ctrl+R` | 反向搜尋歷史記錄 |
| `Tab` | 自動完成 |
| `Ctrl+C` | 取消指令 |
| `Ctrl+Z` | 暫停程序 |
| `fg` | 恢復暫停的程序 |

---

## 最佳實踐

✅ **應該做的：**
- 撰寫清晰、描述性的提交訊息
- 經常以邏輯分組方式提交
- 使用分支進行功能/修復
- 開始工作前先拉取
- 經常檢視 `git status`

❌ **不應該做的：**
- 提交敏感資料（API 金鑰、密碼）
- 強制推送到共享分支
- 提交大型二進位檔案
- 忽略合併衝突
- 直接在 main/master 上工作

---

## 提交訊息慣例

```
type(scope): subject

body (選填)

footer (選填)
```

**類型：**
- `feat`：新功能
- `fix`：錯誤修復
- `docs`：文件
- `style`：格式化
- `refactor`：程式碼重構
- `test`：測試
- `chore`：維護

**範例：**
```
feat(auth): add password reset functionality

Implement password reset via email with token-based
verification. Token expires after 24 hours.

Closes #123
```

---

*最後更新：2025年6月 | Git 2.x*
