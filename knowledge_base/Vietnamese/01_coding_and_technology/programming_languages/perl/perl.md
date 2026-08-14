<!--
---
# Metadata
title: "Perl"
description: "Comprehensive reference for the Perl programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
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

-->
# Perl
Perl được Larry Wall tạo ra vào năm 1987 như một công cụ xử lý văn bản thực tế. Nó trở thành xương sống của quá trình phát triển web thời kỳ đầu (tập lệnh CGI), quản trị hệ thống, tin sinh học và lập trình mạng. Triết lý của Perl là "Có nhiều cách để làm" (TMTOWTDI) - ngôn ngữ cung cấp cho bạn nhiều cách tiếp cận cho mọi vấn đề, thiên về tính biểu đạt hơn là tính đồng nhất.
Ảnh hưởng của Perl đối với lập trình hiện đại là rất lớn nhưng thường vô hình: các biểu thức chính quy, bị ảnh hưởng bởi tính năng khớp mẫu của Perl, hiện đã trở thành tiêu chuẩn trong Python, JavaScript, Java và hầu hết các ngôn ngữ khác. CPAN (Mạng lưu trữ Perl toàn diện) là một trong những kho lưu trữ gói phần mềm đầu tiên và truyền cảm hứng cho các hệ thống sau này như PyPI của Python và npm của Node.
Mặc dù mức độ phổ biến của Perl đã giảm kể từ đỉnh cao vào đầu những năm 2000, nhưng nó vẫn được sử dụng rộng rãi trong các hệ thống cũ, quy trình xử lý văn bản và quản trị hệ thống. Perl 6 (hiện được gọi là **Raku**) là một ngôn ngữ riêng biệt mô phỏng lại nhiều khái niệm của Perl.
---

## Tại sao Perl lại quan trọng
- **Xử lý văn bản**: Biểu thức chính quy của Perl mạnh mẽ nhất so với bất kỳ ngôn ngữ chính thống nào.
- **CPAN**: Hơn 200.000 mô-đun — một trong những kho lưu trữ gói lớn nhất và lâu đời nhất.
- **Một dòng**: Perl vượt trội trong việc chuyển đổi văn bản dòng lệnh nhanh chóng.
- **Ngôn ngữ keo**: Kết nối hệ thống, phân tích nhật ký, xử lý tệp dữ liệu, tự động hóa tác vụ.
- **Đã được chứng minh trong sản xuất**: Cung cấp năng lượng cho web từ trước khi PHP tồn tại. Vẫn đang chạy cơ sở hạ tầng quan trọng.
- **Raku (Perl 6)**: Một thiết kế lại hiện đại với ngữ pháp, mối nối và nhiều công văn.
## Sự đánh đổi
| Hạn chế | Chi tiết | Cách giải quyết điển hình |
|----------|----------|-------------------|
| **Khả năng đọc** | "Perl là ngôn ngữ chỉ ghi" — cú pháp dày đặc, khó hiểu | Sử dụng nghiêm ngặt/cảnh báo; viết mã mô-đun; sử dụng Perl hiện đại (5.36+) |
| **Cộng đồng đang suy giảm** | Ít dự án mới chọn Perl | Cơ sở mã lớn hiện có cần được bảo trì; cộng đồng tích cực |
| **Hai phiên bản chính** | Perl 5 và Raku (Perl 6) là các ngôn ngữ khác nhau | Sử dụng Perl 5 cho công việc hiện có; Raku cho dự án mới |
| **Không hợp thời trang** | Hiếm khi được dạy trong trại đào tạo hoặc trường đại học | Tài liệu mở rộng và mô-đun CPAN |
| **Các dấu hiệu có thể thay đổi** |  Tiền tố`$`,`@`,`%`có thể gây nhầm lẫn cho người mới bắt đầu | Tìm hiểu mẫu:`$scalar`,`@array`,`%hash`|
| **Hiệu suất** | Chậm hơn các ngôn ngữ được biên dịch cho các tác vụ tính toán nặng | Sử dụng phần mở rộng C; không phải là công cụ phù hợp cho HPC |
---

##Cơ bản về cú pháp
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

## Ảnh hưởng của Perl đối với các ngôn ngữ khác
| Tính năng | Ngôn ngữ đã thông qua nó |
|----------|--------------------------|
| Biểu thức chính quy | Python, JavaScript, Java, Ruby, C#, PHP |
| Kho gói (CPAN) | PyPI, npm, RubyGems, thùng.io |
| Đâydocs | Python, Ruby, PHP, Shell, JavaScript |
|  Biến mặc định`$_`|`$_`của Ruby ,`$_`của PowerShell |
| `map`/`grep`/`reduce`| Python, Ruby, JavaScript, Rust |
| `use strict`/ linting | TypeScript, gợi ý kiểu của Python |
---

## Cú pháp & Mẫu nâng cao
### Tài liệu tham khảo và cấu trúc dữ liệu phức tạp
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

### Closure và các hàm bậc cao hơn
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

### Biểu thức chính quy nâng cao
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

### Perl hướng đối tượng (Moose / Moo)
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

## Đồng thời & Song song
### Forking với Parallel::ForkManager
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

### Coro — Coroutine hợp tác
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

### IO::Async — Lập trình hướng sự kiện
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

## Cấu hình dự án & xây dựng hệ thống
### Cấu trúc dự án
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

### cpanfile — Quản lý phụ thuộc
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

### Lệnh phụ thuộc
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### Đường dẫn CI/CD (Hành động trên GitHub)
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

##Thử nghiệm
### Kiểm tra::Thêm
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### Lệnh kiểm tra
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## Khả năng tương tác
### FFI::Thú mỏ vịt
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — Tích hợp C
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## Mẫu thiết kế
### Singleton
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

### Chuỗi trách nhiệm
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

## Hiệu suất & Tối ưu hóa
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

## Triển khai
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

## Khi nào nên sử dụng Perl
| Kịch bản | Tại sao Perl | Thay thế tốt hơn |
|----------|----------|-------------------|
| Xử lý/phân tích văn bản | Công cụ biểu thức chính quy tốt nhất trong lớp | Python cho dữ liệu có cấu trúc |
| Phân tích tệp nhật ký | Hướng dẫn nhanh, công cụ đã được chứng minh | `awk`/`sed`dành cho các trường hợp đơn giản; Python cho phức tạp |
| Quản trị hệ thống | Thống trị về mặt lịch sử | Bash/PowerShell cho các tác vụ đơn giản; Python cho phức tạp |
| Bảo trì hệ thống cũ | Hàng triệu dòng Perl đang được sản xuất | — |
| Tin sinh học | Sự hiện diện lịch sử mạnh mẽ (BioPerl) | Python (Biopython), R |
| Chuyển đổi dữ liệu nhanh | Một lớp lót là không thể đánh bại | `jq`,`awk`cho các định dạng có cấu trúc |
| Phát triển web | Kỷ nguyên CGI đã qua | Python, Node.js, Go, PHP |
| Dự án mới quy mô lớn | Cộng đồng đã tiếp tục | Đi, Rust, Python |
| Khoa học dữ liệu / ML | Không phải hệ sinh thái | Python, R |
---

## Hỏi đáp tổng hợp
### Câu 1: Sự khác biệt giữa`my`,`our`và`local`là gì?
**A:** Những từ khóa này kiểm soát phạm vi biến:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### Câu hỏi 2: Làm cách nào để xử lý các tệp văn bản một cách hiệu quả trong Perl?
**A:** Perl vượt trội trong việc xử lý văn bản. Sử dụng toán tử kim cương và biểu thức chính quy:
```perl
# Line-by-line processing
while (my $line = <STDIN>) {
    chomp $line;
    $line =~ s/old/new/g;
    print "$line\n";
}

# One-liner (the classic Perl superpower)
# perl -pe 's/foo/bar/g' file.txt
# perl -ne 'print if /error/i' logfile.txt
# perl -lane 'print $F[0]' file.txt  # split on whitespace

# Slurp entire file
local $/;
my $content = <FILE>;
```

### Câu 3: Làm cách nào để sử dụng tài liệu tham khảo và cấu trúc dữ liệu phức tạp?
**A:** Tham chiếu là cách Perl tạo ra các cấu trúc lồng nhau:
```perl
# Array reference
my $aref = [1, 2, 3];
print $aref->[0];  # 1

# Hash reference
my $href = { name => 'Alice', age => 30 };
print $href->{name};  # Alice

# Nested structures
my $data = {
    users => [
        { name => 'Alice', scores => [95, 87, 92] },
        { name => 'Bob',   scores => [78, 88, 91] },
    ],
};
print $data->{users}[0]{scores}[2];  # 92
```

### Q4: Tôi nên biết những biến đặc biệt nào của Perl?
**A:** Perl có nhiều biến đặc biệt. Điều quan trọng nhất:
```perl
$_     # default variable (topic)
$!     # system error message
$@     # eval error
$$     # process ID
$.     # current line number in last filehandle
$/     # input record separator (\n by default)
$\     # output record separator
$|     # autoflush (1 = on)
@ARGV  # command-line arguments
%ENV   # environment variables
```

### Câu hỏi 5: Làm cách nào để viết Perl hiện đại, có thể bảo trì được?
**A:** Các phương pháp hay nhất cho Perl hiện đại:
- Luôn sử dụng`strict`và`warnings`
- Sử dụng`my`cho tất cả các biến
- Sử dụng các tước hiệu tệp từ vựng:`open my $fh, '<', $file`
- Sử dụng các module từ CPAN (Moo/Moose cho OOP, Try::Tiny cho lỗi)
- Sử dụng`say`thay vì`print`(với`feature 'say'`)
- Định dạng với `perltidy`
---

## Giải quyết vấn đề theo chuỗi suy nghĩ
### Vấn đề 1: Phân tích tệp nhật ký
**Bước 1: Tìm hiểu vấn đề**
Phân tích nhật ký truy cập Apache và đếm số yêu cầu trên mỗi địa chỉ IP.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng biểu thức chính quy để trích xuất địa chỉ IP, hàm băm để đếm số lần xuất hiện.
**Bước 3: Thực hiện**```perl
use strict;
use warnings;

my %counts;
while (my $line = <>) {
    if ($line =~ /^(\S+)/) {
        $counts{$1}++;
    }
}

# Sort by count (descending)
for my $ip (sort { $counts{$b} <=> $counts{$a} } keys %counts) {
    printf "%-15s %d\n", $ip, $counts{$ip};
}
```

**Bước 4: Gia hạn**
Thêm tính năng lọc ngày, phân tích mã trạng thái và xuất dưới dạng CSV.
### Vấn đề 2: Đổi tên file hàng loạt bằng Regex
**Bước 1: Tìm hiểu vấn đề**
Đổi tên tệp phù hợp với mẫu, chuyển đổi tên tệp bằng biểu thức chính quy.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`glob`hoặc`opendir`để tìm tệp, biểu thức chính quy để chuyển đổi tên.
**Bước 3: Thực hiện**```perl
use strict;
use warnings;
use File::Copy;

my $dir = shift @ARGV || '.';
opendir my $dh, $dir or die "Cannot open $dir: $!";

for my $file (sort readdir $dh) {
    next unless $file =~ /^(\d{4})-(\d{2})-(\d{2})_(.+)$/;
    my $new_name = "$3-$2-$1_$4";  # Rearrange date format
    my $old = "$dir/$file";
    my $new = "$dir/$new_name";
    print "Renaming: $file -> $new_name\n";
    move($old, $new) or warn "Failed: $!";
}
closedir $dh;
```

**Bước 4: Xác minh**
Trước tiên hãy chạy với cờ`--dry-run`(chỉ in, không di chuyển).
### Vấn đề 3: Xây dựng một Web Scraper đơn giản
**Bước 1: Tìm hiểu vấn đề**
Tìm nạp một trang web và trích xuất tất cả các liên kết.
**Bước 2: Xác định phương pháp tiếp cận**
Sử dụng`LWP::Simple`để tìm nạp và biểu thức chính quy hoặc`HTML::LinkExtor`để phân tích cú pháp.
**Bước 3: Thực hiện**```perl
use strict;
use warnings;
use LWP::Simple;
use HTML::LinkExtor;

my $url = 'https://example.com';
my $html = get($url) or die "Cannot fetch $url";

my $parser = HTML::LinkExtor->new;
$parser->parse($html);

for my $link ($parser->links) {
    my ($tag, %attrs) = @$link;
    print "$attrs{href}\n" if $attrs{href};
}
```

**Bước 4: Gia hạn**
Xử lý các URL tương đối, lọc theo tên miền và theo dõi phân trang.
---

## Bản tóm tắt
Thời đại hoàng kim của Perl đã qua nhưng ảnh hưởng của nó vẫn còn ở khắp mọi nơi. Mọi ngôn ngữ có biểu thức chính quy, mọi trình quản lý gói được mô hình hóa trên CPAN và mọi hệ thống có`map`/`grep`/`reduce`đều mang DNA của Perl. Đối với các dự án mới, hầu hết các nhà phát triển đều sử dụng Python hoặc Go. Nhưng Perl vẫn là một công cụ mạnh mẽ để xử lý văn bản, tự động hóa nhanh chóng và duy trì số lượng lớn mã Perl chạy cơ sở hạ tầng quan trọng trên toàn thế giới. Hiểu Perl cũng có nghĩa là hiểu lập trình hiện đại đến từ đâu - nó định hình các công cụ và mẫu mà chúng ta sử dụng ngày nay.