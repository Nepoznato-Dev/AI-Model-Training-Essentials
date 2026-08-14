---
# Metadata
title: "Shell & PowerShell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Shell and PowerShell ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [shell, powershell, bash, ecosystem, tooling, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Shell & PowerShell — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu cho tập lệnh shell (Bash/Zsh) và PowerShell.
---

## Triển khai Shell
| Vỏ | Nền tảng | Ghi chú |
|-------|----------|-------|
| **Bùng nổ** | Unix/Linux/macOS | Được sử dụng rộng rãi nhất |
| **Zsh** | mặc định macOS | Bash nâng cao |
| **Cá** | Đa nền tảng | Thân thiện với người dùng |
| **dấu gạch ngang** | Debian/Ubuntu | Nhanh chóng, tuân thủ POSIX |
| **ksh** | Unix | Vỏ Korn |
| **PowerShell** | Đa nền tảng | Hướng đối tượng (pwsh) |
| **Không có gì** | Đa nền tảng | Vỏ dữ liệu có cấu trúc |
```bash
bash --version            # check Bash version
echo $SHELL               # current shell
zsh --version             # Zsh version
pwsh --version            # PowerShell version
```

---

## Trình quản lý gói (Shell Tools)
| Công cụ | Mục đích |
|------|----------|
| **Homebrew** | trình quản lý gói macOS/Linux |
| **apt / yum / dnf** | Trình quản lý gói Linux |
| **pkg** | Trình quản lý gói FreeBSD |
| **Tin sốt dẻo** | Trình cài đặt Windows CLI |
| **Sô cô la** | Trình quản lý gói Windows |
| **cánh** | Trình quản lý gói Windows |
```bash
# Homebrew
brew install jq ripgrep fd bat    # install tools
brew upgrade                      # upgrade all

# apt (Debian/Ubuntu)
sudo apt update && sudo apt install -y jq curl

# PowerShell
Install-Module -Name PSReadLine -Force
```

---

## Công cụ CLI cần thiết
| Công cụ | Mục đích |
|------|----------|
| **jq** | Xử lý JSON |
| **yq** | Xử lý YAML |
| **ripgrep (rg)** | Nhanh chóng |
| **fd** | Tìm nhanh |
| **dơi** | Mèo nâng cao |
| **exa / eza** | ls nâng cao |
| **fzf** | Công cụ tìm mờ |
| **htop** | Trình xem quy trình |
| **tmux** | Bộ ghép kênh đầu cuối |
| **curl / wget** | Yêu cầu HTTP |
| **sed / awk** | Xử lý văn bản |
| **xargs** | Xây dựng lệnh từ đầu vào |
| **làm** | Người chạy nhiệm vụ |
| **nhập** | Chạy lệnh khi thay đổi tập tin |
| **song song** | Thực hiện song song |
| **kiểm tra shell** | Shell script kẻ nói dối |
---

## Khung và cải tiến Shell
| Công cụ | Mục đích |
|------|----------|
| **Ôi Zsh của tôi** | Khung Zsh (chủ đề, plugin) |
| **Prezto** | Khung Zsh (nhanh hơn) |
| **Tàu vũ trụ** | Dấu nhắc chéo |
| **zsh-tự động đề xuất** | Tự động đề xuất |
| **zsh-cú pháp-tô sáng** | Làm nổi bật cú pháp |
| **bực mình** | Khung Bash |
| **tuin** | Lịch sử Shell (SQLite) |
```bash
# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Starship prompt (cross-shell)
curl -sS https://starship.rs/install.sh | sh
```

---

## Mô-đun PowerShell
| Mô-đun | Mục đích |
|--------|----------|
| **PSReadLine** | Chỉnh sửa dòng lệnh nâng cao |
| **Quấy rối** | Khung kiểm tra |
| **Trình phân tích PSScript** | Lining |
| **sang trọng** | Tích hợp Git |
| **Biểu tượng thiết bị đầu cuối** | Biểu tượng tập tin |
| **Cập nhật PSWindows** | Cập nhật Windows |
| **Az** | Quản lý Azure |
| **AWSPowerShell** | Quản lý AWS |
| **Máy chủ SQL** | Quản lý máy chủ SQL |
| **Pode** | Khung web |
| **Bảng điều khiển chung** | Bảng điều khiển web |
```powershell
# Install modules
Install-Module -Name PSReadLine -Force
Install-Module -Name Pester -Force
Install-Module -Name PSScriptAnalyzer -Force
Install-Module -Name Az -Force

# Import module
Import-Module Az
```

---

##Thử nghiệm
| Khung | Vỏ | Mục đích |
|----------|-------|-------|---------|
| **Dơi** | Đánh | Kiểm tra tự động Bash |
| **shunit2** | Vỏ | thử nghiệm kiểu xUnit |
| **Quấy rối** | PowerShell | Kiểm tra và chế giễu |
| **khẳng định.sh** | Đánh | Thư viện khẳng định |
```bash
# Bats example
#!/usr/bin/env bats

@test "addition" {
  result=$((2 + 3))
  [ "$result" -eq 5 ]
}

@test "file exists" {
  [ -f "/etc/passwd" ]
}

@test "command succeeds" {
  run echo "hello"
  [ "$status" -eq 0 ]
  [ "$output" = "hello" ]
}
```

```powershell
# Pester example
Describe "UserService" {
    It "finds user by id" {
        $user = Get-User -Id 1
        $user.Name | Should -Be "Alice"
    }
    
    It "throws when user not found" {
        { Get-User -Id 999 } | Should -Throw
    }
}
```

---

## Chất lượng mã
| Công cụ | Vỏ | Mục đích |
|------|-------|---------|
| **ShellCheck** | Bash/Zsh | Linting và phân tích tĩnh |
| **shfmt** | Bash/Zsh | Định dạng mã |
| **Trình phân tích PSScript** | PowerShell | Lining |
| **Cài đặt PSScript** | PowerShell | Định dạng |
```bash
# ShellCheck
shellcheck script.sh        # lint
shellcheck -s bash script.sh  # specify shell

# shfmt
shfmt -w script.sh          # format
shfmt -d script.sh          # diff (check only)
```

```powershell
# PSScriptAnalyzer
Invoke-ScriptAnalyzer -Path .\script.ps1
Invoke-ScriptAnalyzer -Path .\script.ps1 -Fix  # auto-fix
```

---

## Thư viện và mẫu chính
### Đánh
| Mẫu | Mục đích |
|----------|----------|
| **đặt -euo pipefail** | Chế độ nghiêm ngặt |
| **cái bẫy** | Xử lý tín hiệu |
| **nguồn / .** | Bao gồm các tập tin |
| **có được** | Phân tích đối số |
| **đâydoc** | Chuỗi nhiều dòng |
| **thay thế quy trình** | `<()`và`>()`|
| **mảng** | Được lập chỉ mục và liên kết |
```bash
#!/usr/bin/env bash
set -euo pipefail

# Functions
log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"; }

# Argument parsing
while getopts "hn:v" opt; do
  case $opt in
    h) echo "Usage: $0 [-h] [-n name] [-v]"; exit 0 ;;
    n) NAME="$OPTARG" ;;
    v) VERBOSE=true ;;
  esac
done

# Cleanup trap
cleanup() { rm -rf "$TMPDIR"; }
trap cleanup EXIT
```

### PowerShell
| Mẫu | Mục đích |
|----------|----------|
| **Binding Cmdlet** | Chức năng nâng cao |
| **Thông số** | Thuộc tính tham số |
| **Đường ống** | Đường dẫn đối tượng |
| **Thử/Bắt** | Xử lý lỗi |
| **Lớp học** | OO |
```powershell
function Get-User {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$Id,
        
        [ValidateSet("json", "xml")]
        [string]$Format = "json"
    )
    
    try {
        $user = Invoke-RestMethod -Uri "https://api.example.com/users/$Id"
        return $user
    }
    catch {
        Write-Error "Failed to get user: $_"
    }
}
```

---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS** | Hỗ trợ Shell/PowerShell |
| **Neovim** | Dựa trên thiết bị đầu cuối |
| **Thiết bị đầu cuối Windows** | Thiết bị đầu cuối hiện đại (PowerShell) |
| **iTerm2** | thiết bị đầu cuối macOS |
| **Làm cong** | Thiết bị đầu cuối hỗ trợ AI |
| **Nhanh nhẹn** | Thiết bị đầu cuối tăng tốc GPU |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Cron** | Nhiệm vụ theo lịch trình (Unix) |
| **systemd** | Quản lý dịch vụ (Linux) |
| ** Lập lịch tác vụ ** | Nhiệm vụ theo lịch trình của Windows |
| **ĐIỂM VÀO Docker** | Tập lệnh vùng chứa |
| **Đường dẫn CI/CD** | Hành động GitHub, GitLab CI |
| **Ansible** | Quản lý cấu hình |
| **Địa hình** | Cơ sở hạ tầng dưới dạng mã |
---

## Bản tóm tắt
Hệ sinh thái của tập lệnh Shell rất đa dạng: **Bash** vẫn là tiêu chuẩn phổ quát, **Zsh** là mặc định hiện đại cho mục đích sử dụng tương tác và **PowerShell** thống trị quản trị Windows. Ngăn xếp tiêu chuẩn là: **Bash/Zsh** dành cho tập lệnh, **ShellCheck** dành cho linting, **shfmt** dành cho định dạng, **Bats** dành cho thử nghiệm, **jq** dành cho JSON, **ripgrep** dành cho tìm kiếm và **tmux** dành cho ghép kênh thiết bị đầu cuối. Đối với PowerShell: **Pester** để kiểm tra, **PSScriptAnalyzer** để tìm lỗi mã nguồn và **PSReadLine** để chỉnh sửa nâng cao. Tập lệnh Shell rất cần thiết cho tự động hóa, CI/CD, quản trị hệ thống và quy trình làm việc DevOps.