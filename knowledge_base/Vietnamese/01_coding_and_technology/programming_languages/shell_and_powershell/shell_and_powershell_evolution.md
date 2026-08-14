---
# Metadata
title: "Shell & PowerShell — Version History & Evolution"
description: "Comprehensive version history and evolution of Unix Shell and PowerShell from sh to modern shells."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [shell, powershell, bash, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Shell & PowerShell — Lịch sử phiên bản & Tiến hóa
## Dòng thời gian của Unix Shell
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| Thompson sh | 1971 | Shell Unix đầu tiên (Ken Thompson) |
| Bourne sh | 1977 | **`sh`** — tập lệnh, biến, luồng điều khiển |
| csh | 1978 | Cú pháp giống C, kiểm soát công việc, bí danh |
| ksh | 1983 | Vỏ Korn - tính năng`sh`+`csh`|
| bash | 1989 | **Bourne Again Shell** — Thay thế GNU`sh`|
| bash 2.0 | 1996 | `[[ ]]`,`(( ))`,`+=`|
| bash 3.0 | 2004 |  Biểu thức chính quy `=~`,`|&`|
| bash 4.0 | 2009 | **Mảng kết hợp**,`mapfile`,`declare -g`|
| bash 4.3 | 2014 | Lỗ hổng Shellshock được phát hiện |
| bash 5.0 | 2019 |  Giới thiệu tên `declare -n`,`printf %q`|
| bash 5.1 | 2020 | `wait -n`,`shopt`cải tiến |
| bash 5.2 | 2022 | `${var@U}`(chữ hoa),`shopt -s compat`|
| zsh | 1990 | Bash mở rộng — hoàn thành, chủ đề |
| cá | 2005 | **Thân thiện với người dùng** — tự động đề xuất, tô sáng cú pháp |
| vỏ bọc | 2019 | Dữ liệu có cấu trúc, đường dẫn của bảng |
| dầu/nước | 2020 | Tương thích Bash với ngữ nghĩa tốt hơn |
## Dòng thời gian PowerShell
| Phiên bản | Năm | Chủ đề chính |
|----------|------|----------|
| 1.0 | 2006 | Bản phát hành đầu tiên (Microsoft, Jeffrey Snover) |
| 2.0 | 2009 | **Mô-đun**, điều khiển từ xa, công việc nền, giao dịch |
| 3.0 | 2012 | Quy trình làm việc,`Invoke-RestMethod`, công việc theo lịch trình |
| 4.0 | 2013 | **Cấu hình trạng thái mong muốn (DSC)**, cải tiến`if`/`switch`|
| 5.0 | 2016 | **Các lớp**,`enum`,`using`,`using module`|
| 5.1 | 2017 | Phiên bản cuối cùng chỉ dành cho Windows |
| 6.0 | 2018 | **PowerShell Core** — đa nền tảng (Windows, Linux, macOS) |
| 6.1 | 2018 | `ForEach-Object -Parallel`(thử nghiệm) |
| 6.2 | 2019 |  Nhà khai thác chuỗi đường ống`&&`/`||`|
| 7.0 | 2020 | **Chính**:`?.`vô điều kiện,`??`hợp nhất vô giá trị,`using assembly`|
| 7.1 | 2020 | Toán tử bậc ba`? :`,`using module`cải tiến |
| 7.2 | 2021 | **Bản phát hành LTS**, cải tiến`using namespace`|
| 7.3 | 2022 |  Cải tiến `switch`, tùy chọn`ErrorView`|
| 7.4 | 2023 |  Cải tiến `using module`,`Get-Error`|
| 7,5 | 2024 | Cải tiến hiệu suất,`PSResourceGet`|
| 7.6 | 2025 | Đang phát triển |
## Các cột mốc quan trọng
### Di sản Unix Shell (1971–1989)
- **1971**: Thompson shell — shell Unix đầu tiên, thực thi lệnh đơn giản
- **1977**: Bourne shell (`sh`) — biến, luồng điều khiển (`if`,`while`), tài liệu tại đây
- **1978**: C shell (`csh`) — Cú pháp giống C, kiểm soát công việc, bí danh, lịch sử
- **1983**: Vỏ Korn (`ksh`) — tốt nhất trong`sh`+ `csh`
### bash — Tiêu chuẩn (1989–nay)
- **1989**: Brian Fox tạo bash cho dự án GNU — Bourne Again Shell
- **2.0 (1996)**: Kiểm tra `[[ ]]`, số học `(( ))`,`+=`
- **4.0 (2009)**: Mảng kết hợp (`declare -A`),`mapfile`
- **5.0 (2019)**: Tên giới thiệu,`printf %q`
- **5.2 (2022)**: Thao tác kiểu chuỗi
### zsh — Vỏ của người dùng quyền lực (1990–nay)
- **1990**: Paul Falstad tạo zsh — kết hợp các tính năng bash, ksh, tcsh
- **Những năm 2000**: khung oh-my-zsh — chủ đề, plugin, phần hoàn thiện
- **2019**: shell mặc định của macOS (thay thế bash)
### cá — Vỏ thân thiện (2005–nay)
- **2005**: Axel Liljankrantz tạo ra cá — "Cuối cùng, một lớp vỏ tương tác"
- Tự động gợi ý, tô sáng cú pháp, cấu hình dựa trên web
- Không tương thích với bash — ngôn ngữ kịch bản khác
### PowerShell — Shell của Microsoft (2006–nay)
- **2006**: PowerShell 1.0 — dựa trên .NET, đường dẫn đối tượng, lệnh ghép ngắn
- **2.0 (2009)**: Mô-đun, điều khiển từ xa, công việc nền
- **5.0 (2016)**: Lớp, enum
- **6.0 (2018)**: **Đa nền tảng** — PowerShell Core (được xây dựng trên .NET Core)
- **7.0 (2020)**:`?.`không có điều kiện,`??`không có điều kiện,`?:`ba ngôi
## Tiến hóa cú pháp
```bash
# Bourne shell (1977): Basic scripting
#!/bin/sh
name="World"
echo "Hello, $name"
for file in *.txt; do
  echo "Processing $file"
done

# bash 4.0: Associative arrays
declare -A colors
colors[red]="#FF0000"
colors[green]="#00FF00"
echo "${colors[red]}"

# bash 5.0+: Modern bash
mapfile -t lines < input.txt
for line in "${lines[@]}"; do
  echo "${line^^}"  # uppercase
done

# zsh + oh-my-zsh: Enhanced interactive
# Autosuggestions, syntax highlighting, git aliases

# fish: Modern interactive
# Autosuggestions, web config, not bash-compatible
function greet
    echo "Hello, $argv"
end
```

```powershell
# PowerShell 1.0: Basic cmdlets
Get-Process | Where-Object { $_.CPU -gt 100 }

# PowerShell 5.0: Classes
class Person {
    [string]$Name
    [int]$Age
    Person([string]$n, [int]$a) { $this.Name = $n; $this.Age = $a }
}

# PowerShell 7.0+: Modern syntax
$person = [Person]::new("Alice", 30)
$name = $person?.Name ?? "Unknown"  # null-conditional, null-coalescing
$result = $x -gt 0 ? "positive" : "non-positive"  # ternary

# PowerShell: Object pipeline (unique feature)
Get-ChildItem |
  Where-Object { $_.Extension -eq ".md" } |
  ForEach-Object { $_.FullName }
```

## Nguyên tắc thiết kế chính
```
Shell (bash/zsh):
1. "Text is the universal interface" — pipes connect everything
2. "Do one thing well" — small tools, compose via pipes
3. "Everything is a file" — Unix philosophy
4. "Backward compatible" — 40-year-old scripts still work

PowerShell:
1. "Objects, not text" — pipeline passes .NET objects
2. "Consistent" — Verb-Noun naming (Get-Process, Set-Location)
3. "Extensible" — modules, providers, remoting
4. "Cross-platform" — PowerShell 7+ runs everywhere
```

## Tăng trưởng hệ sinh thái
```
1971: Thompson shell — first Unix shell
1977: Bourne shell (sh) — scripting begins
1989: bash — GNU shell, becomes Linux default
1990: zsh — power user shell
2005: fish — user-friendly shell
2006: PowerShell 1.0 — Microsoft's object shell
2010: oh-my-zsh — zsh framework (themes, plugins)
2018: PowerShell 6.0 — cross-platform
2019: nushell — structured data shell
2020: PowerShell 7.0 — modern syntax
2025: bash remains the default on Linux/macOS
       PowerShell dominates Windows administration
       zsh is macOS default; fish gaining popularity
```
