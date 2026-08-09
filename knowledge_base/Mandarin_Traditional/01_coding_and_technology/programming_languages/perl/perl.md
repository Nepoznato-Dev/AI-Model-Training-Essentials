---
# Metadata
title: "Perl"
description: "Comprehensive reference for the Perl programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [perl, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "24 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# 珀爾
Perl 由 Larry Wall 於 1987 年創建，是一種實用的文字處理工具。它成為早期 Web 開發（CGI 腳本）、系統管理、生物資訊學和網路程式設計的支柱。 Perl 的哲學是「有不止一種方法可以做到這一點」（TMTOWTDI）——該語言為每個問題提供了多種方法，注重表現力而不是統一性。
Perl 對現代程式設計的影響是巨大的，但往往是無形的：受 Perl 模式匹配影響的正規表示式現在已成為 Python、JavaScript、Java 和大多數其他語言的標準。 CPAN（綜合 Perl 存檔網路）是最早的軟體包儲存庫之一，並啟發了後來的系統，例如 Python 的 PyPI 和 Node 的 npm。
雖然 Perl 的受歡迎程度自 2000 年代初期達到頂峰以來已經有所下降，但它仍然廣泛應用於遺留系統、文字處理管道和系統管理。 Perl 6（現在稱為 **Raku**）是一種獨立的語言，它重新構想了 Perl 的許多概念。
---

## 為什麼 Perl 很重要
- **文字處理**：Perl 的正規表示式是所有主流語言中最強大的。
- **CPAN**：超過 200,000 個模組 — 最大、最古老的軟體包儲存庫之一。
- **簡單**：Perl 擅長快速命令列文字轉換。
- **膠水語言**：連接系統、解析日誌、處理資料檔案、自動執行任務。
- **在生產中得到驗證**：在 PHP 出現之前就為網路提供了動力。仍在運作關鍵基礎設施。
- **Raku (Perl 6)**：具有語法、連接和多重調度的現代重新設計。
## 權衡
|限制|詳情 |典型解決方法|
|------------|---------|--------------------|
| **可讀性** | 「Perl 是一種只寫語言」—密集、神秘的語法 |使用嚴格/警告；編寫模組化程式碼；使用現代 Perl (5.36+) |
| **社區日漸沒落** |選擇 Perl 的新專案越來越少 |現有的大型程式碼庫需要維護；活躍社群 |
| **兩個主要版本** | Perl 5 和 Raku (Perl 6) 是不同的語言 |使用 Perl 5 進行現有工作； Raku 新專案 |
| **不時** |很少在訓練營或大學教授|豐富的文檔和 CPAN 模組 |
| **可變印記** |`$`、`@`、`%`前綴可能會讓初學者感到困惑 |學習圖案：`$scalar`、`@array`、`%hash`|
| **效能** |對於運算量大的任務來說比編譯語言慢 |使用C擴充；不是適合 HPC 的工具 |
---

## 文法基礎知識
```perl
#!/usr/bin/env perl
use strict;
use warnings;
use feature 'say';  # Modern Perl

# Variables
my $name = "Alice";          # Scalar (single value)
my @colors = ("red", "green", "blue");  # Array
my %user = (                  # Hash (key-value pairs)
    name  => "Alice",
    age   => 30,
    email => "alice@example.com",
);

# Access
say $name;                    # Alice
say $colors[0];               # red
say $user{name};              # Alice

# String operations
my $greeting = "Hello, $name!";
my $upper = uc($name);        # "ALICE"
my $length = length($name);   # 5

# Regular expressions (Perl's superpower)
my $text = "Error 404: Page not found on 2024-01-15";

if ($text =~ /Error (\d+): (.+)/) {
    say "Code: $1";    # 404
    say "Message: $2"; # Page not found on 2024-01-15
}

# Substitution
$text =~ s/not found/missing/;
# "Error 404: Page missing on 2024-01-15"

# Global replacement
my $data = "foo bar foo baz foo";
$data =~ s/foo/qux/g;    # "qux bar qux baz qux"

# Extracting with regex
my @numbers = $text =~ /(\d+)/g;  # Extract all numbers

# Conditionals
if ($name eq "Alice") {
    say "Welcome back!";
} elsif ($name eq "Bob") {
    say "Hello Bob!";
} else {
    say "Who are you?";
}

# Loops
for my $color (@colors) {
    say "Color: $color";
}

foreach my $key (keys %user) {
    say "$key => $user{$key}";
}

# While loop (read file line by line)
open my $fh, '<', 'data.txt' or die "Cannot open: $!";
while (my $line = <$fh>) {
    chomp $line;
    say "Line: $line";
}
close $fh;

# Subroutines (functions)
sub greet {
    my ($name, $greeting) = @_;
    $greeting //= "Hello";  # Default value
    return "$greeting, $name!";
}

say greet("Alice", "Hi");   # Hi, Alice!
say greet("Bob");            # Hello, Bob!

# List processing (Perl's other strength)
my @numbers = (1..100);
my @evens = grep { $_ % 2 == 0 } @numbers;
my @doubled = map { $_ * 2 } @evens;
my $sum = reduce { $a + $b } @numbers;

# Hash references (complex data structures)
my $team = {
    name    => "Engineering",
    members => [
        { name => "Alice", role => "Lead" },
        { name => "Bob",   role => "Dev" },
    ],
};

say $team->{members}[0]{name};  # Alice

# Error handling
eval {
    die "Something went wrong";
};
if ($@) {
    say "Caught error: $@";
}

# Perl one-liners (command line)
# perl -ne 'print if /ERROR/' access.log
# perl -pe 's/old/new/g' file.txt
# perl -lane 'print $F[0]' data.csv  # Print first column
```

---

## Perl 對其他語言的影響
|特色 |採用它的語言 |
|---------|--------------------------------|
|正規表示式| Python、JavaScript、Java、Ruby、C#、PHP |
|套件儲存庫 (CPAN) | PyPI、npm、RubyGems、crates.io |
|此處文檔 | Python、Ruby、PHP、Shell、JavaScript |
|`$_`預設變數 | Ruby 的`$_`、PowerShell 的`$_`|
|`map`/`grep`/`reduce`| Python、Ruby、JavaScript、Rust |
|`use strict`/ 掉毛 | TypeScript，Python 的型別提示 |
---

## 進階語法和模式
### 引用與複雜資料結構
```perl
use strict;
use warnings;
use feature 'say';
use Data::Dumper;

# References — pointers to variables
my $scalar_ref = \42;
my $array_ref  = [1, 2, 3];       # Anonymous array reference
my $hash_ref   = { name => "Alice" };  # Anonymous hash reference

# Dereferencing
say $$scalar_ref;        # 42
say $array_ref->[0];     # 1
say $hash_ref->{name};   # Alice

# Complex nested structures
my $company = {
    name => "TechCorp",
    departments => [
        {
            name    => "Engineering",
            members => [
                { name => "Alice", skills => ["Perl", "Python"] },
                { name => "Bob",   skills => ["Perl", "Go"] },
            ],
        },
        {
            name    => "Marketing",
            members => [
                { name => "Charlie", skills => ["SEO", "Analytics"] },
            ],
        },
    ],
};

say $company->{departments}[0]{members}[0]{name};  # Alice
say $company->{departments}[0]{members}[0]{skills}[1];  # Python
```

### 閉包與高階函數
```perl
# Closures — subroutines that capture their lexical environment
sub make_counter {
    my $count = 0;
    return sub {
        $count++;
        return $count;
    };
}

my $counter = make_counter();
say $counter->();  # 1
say $counter->();  # 2
say $counter->();  # 3

# Higher-order functions
sub apply {
    my ($func, $value) = @_;
    return $func->($value);
}

my $double = sub { $_[0] * 2 };
say apply($double, 21);  # 42

# Sort with custom comparators
my @users = (
    { name => "Charlie", age => 25 },
    { name => "Alice",   age => 30 },
    { name => "Bob",     age => 20 },
);

my @sorted_by_name = sort { $a->{name} cmp $b->{name} } @users;
my @sorted_by_age    = sort { $a->{age} <=> $b->{age} } @users;
```

### 高階正規表示式
```perl
# Named captures
my $log = "2024-01-15 ERROR: Connection timeout on server-01";
if ($log =~ /(?<date>\d{4}-\d{2}-\d{2})\s+(?<level>\w+):\s+(?<msg>.+)/) {
    say "Date:  $+{date}";   # 2024-01-15
    say "Level: $+{level}";  # ERROR
    say "Msg:   $+{msg}";    # Connection timeout on server-01
}

# Lookahead and lookbehind
my $text = "price: $100, cost: $50";
my @prices = $text =~ /(?<=\$)\d+/g;  # (100, 50) — match digits after $

# Recursive patterns for nested structures
my $nested = "a(b(c)d)e";
if ($nested =~ /(\w+(??{(?1)?)\w*)/) {
    say "Matched: $&";
}

# /x modifier — readable regex with comments
my $email_re = qr{
    ^
    [a-zA-Z0-9._%+-]+   # local part
    @
    [a-zA-Z0-9.-]+       # domain
    \.
    [a-zA-Z]{2,}         # TLD
    $
}x;

say "test@example.com" =~ $email_re ? "Valid" : "Invalid";
```

### 物件導向的 Perl (Moose / Moo)
```perl
# Modern Perl OOP with Moose
package Animal;
use Moose;

has 'name' => (is => 'ro', isa => 'Str', required => 1);
has 'age'  => (is => 'rw', isa => 'Int', default => 0);

sub speak { return "$_[0]->name makes a sound" }

__PACKAGE__->meta->make_immutable;
no Moose;

package Dog;
use Moose;
extends 'Animal';

override 'speak' => sub {
    return super() . " — woof!";
};

__PACKAGE__->meta->make_immutable;
no Moose;

# Usage
my $rex = Dog->new(name => "Rex", age => 3);
say $rex->speak();  # Rex makes a sound — woof!
```

---

## 並發與平行
### 使用 Parallel::ForkManager 進行分叉
```perl
use Parallel::ForkManager;

my $pm = Parallel::ForkManager->new(4);  # 4 parallel workers

my @urls = ("http://example.com/1", "http://example.com/2",
            "http://example.com/3", "http://example.com/4");

foreach my $url (@urls) {
    $pm->start and next;  # Parent continues
    # Child process
    my $result = `curl -s $url`;
    $pm->finish(0, { url => $url, result => $result });
}

$pm->wait_all_children;
```

### Coro — 協作協程
```perl
use Coro;

my $ready = new Coro::Channel;

async {
    while (my $item = $ready->get) {
        say "Processing: $item";
        schedule;  # Yield to other coroutines
    }
};

$ready->put("item1");
$ready->put("item2");
$ready->put("item3");
```

### IO::Async — 事件驅動編程
```perl
use IO::Async;

my $loop = IO::Async::Loop->new;
my $http = IO::Async::HTTP->new;

foreach my $url (@urls) {
    $http->do_request(
        uri => $url,
        on_response => sub {
            my ($response) = @_;
            say "$url: " . $response->code;
        },
    );
}

$loop->run;
```

---

## 專案配置與建置系統
### 專案結構
```
my-perl-project/
├── lib/
│   └── MyApp/
│       ├── Controller/
│       ├── Model/
│       └── View/
├── t/
│   ├── 00-load.t
│   ├── basic.t
│   └── controller/
├── bin/
│   └── myapp.pl
├── cpanfile
├── Makefile.PL
├── dist.ini        # If using Dist::Zilla
└── README.md
```

### cpanfile — 依賴管理
```perl
# cpanfile
requires 'perl', '5.036';
requires 'Mojolicious', '>= 9.0';
requires 'DBIx::Class', '>= 0.08';
requires 'JSON::XS';
requires 'Log::Log4perl';

on 'test' => sub {
    requires 'Test::More', '>= 1.3';
    requires 'Test::Deep';
    requires 'Mock::Sub';
};

on 'develop' => sub {
    requires 'Perl::Critic';
    requires 'Perl::Tidy';
};
```

### 依賴指令
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### CI/CD 管道 (GitHub Actions)
```yaml
name: Perl CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    strategy:
      matrix:
        perl: ['5.36', '5.38']
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: shogo82148/actions-setup-perl@v1
        with:
          perl-version: ${{ matrix.perl }}
      - run: cpanm --installdeps --with-develop .
      - run: perl Makefile.PL && make test
      - run: perlcritic lib/
```
---

## 測試
### 測試::更多
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### 測試命令
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## 互通性
### FFI::鴨嘴獸
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — C 集成
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## 設計模式
### 單例
```perl
package Database;
use Moose;
has 'connection' => (is => 'ro', lazy => 1, builder => '_build_conn');
sub _build_conn { return "db_handle"; }
my $instance;
sub instance { $instance //= Database->new }
__PACKAGE__->meta->make_immutable;
no Moose;
```

### 責任鏈
```perl
package Middleware::Pipeline;
sub new { bless { handlers => [] }, shift }
sub add { my ($s, $h) = @_; push @{$s->{handlers}}, $h; $s }
sub execute {
    my ($self, $req) = @_;
    my $i = 0;
    my $n; $n = sub {
        $i < @{$self->{handlers}} ? $self->{handlers}[$i++]->($req, $n) : $req
    };
    $n->();
}
```
---

## 效能與最佳化
```bash
# Devel::NYTProf profiler
perl -d:NYTProf script.pl && nytprofhtml --open
```

```perl
# Hash lookups instead of array scans
my %lookup = map { $_->{id} => $_ } @users;
my $user = $lookup{42};  # O(1) instead of O(n)

# Precompile regexes
my $pattern = qr/\b[A-Z]{2,}\b/;
```

---

## 部署
```bash
# FatPacker — self-contained scripts
fatpack pack script.pl > fatpacked.pl

# Starman production server
starman --workers 8 --port 5000 bin/app.pl
```

```dockerfile
FROM perl:5.38-slim
WORKDIR /app
COPY cpanfile* ./
RUN cpanm --installdeps --notest .
COPY . .
CMD ["perl", "bin/myapp.pl"]
```

---

## 何時使用 Perl
|場景 |為什麼選擇 Perl |更好的選擇|
|----------|---------|--------------------|
|文字處理/解析|一流的正規表示式引擎 |用於結構化資料的 Python |
|日誌檔分析 |快速單行、經過驗證的工具 |`awk`/`sed`適用於簡單情況；複雜的Python |
|系統管理|歷史上占主導地位| Bash/PowerShell 用於簡單任務；複雜的Python |
|舊系統維護 |生產中的數百萬行 Perl | — |
|生物資訊學|強大的歷史影響力 (BioPerl) | Python (Biopython)、R |
|快速資料轉換 |單行是無與倫比的 | 用於結構化格式的`jq`、`awk`|
|網頁開發| CGI時代結束了 | Python、Node.js、Go、PHP |
|新大型專案|社群繼續前進 | Go、Rust、Python |
|資料科學/機器學習 |不是生態系| Python、R |
---

＃＃ 概括
Perl 的黃金時代已經過去，但它的影響卻無處不在。每種具有正規表示式的語言、每種基於 CPAN 的套件管理器以及每種帶有`map`/`grep`/`reduce`的系統都帶有 Perl 的 DNA。對於新項目，大多數開發人員都會選擇 Python 或 Go。但 Perl 仍然是文字處理、快速自動化和維護在全球關鍵基礎設施上運行的大量 Perl 程式碼的強大工具。了解 Perl 也意味著了解現代程式設計的起源——它塑造了我們今天使用的工具和模式。