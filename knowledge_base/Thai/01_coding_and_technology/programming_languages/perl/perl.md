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
#เพิร์ล
Perl ถูกสร้างขึ้นโดย Larry Wall ในปี 1987 เพื่อเป็นเครื่องมือประมวลผลข้อความที่ใช้งานได้จริง มันกลายเป็นแกนหลักของการพัฒนาเว็บในยุคแรก ๆ (สคริปต์ CGI) การบริหารระบบ ชีวสารสนเทศศาสตร์ และการเขียนโปรแกรมเครือข่าย ปรัชญาของ Perl คือ "มีมากกว่าหนึ่งวิธีที่จะทำ" (TMTOWTDI) - ภาษานี้ช่วยให้คุณมีแนวทางที่หลากหลายในทุกปัญหา โดยให้ความสำคัญกับการแสดงออกมากกว่าความสม่ำเสมอ
อิทธิพลของ Perl ต่อการเขียนโปรแกรมสมัยใหม่นั้นมีมากมายมหาศาลแต่มักมองไม่เห็น กล่าวคือ นิพจน์ทั่วไปที่ได้รับอิทธิพลจากการจับคู่รูปแบบของ Perl กลายเป็นมาตรฐานใน Python, JavaScript, Java และภาษาอื่นๆ ส่วนใหญ่แล้ว CPAN (Comprehensive Perl Archive Network) เป็นหนึ่งในที่เก็บแพ็คเกจซอฟต์แวร์แรกๆ และเป็นแรงบันดาลใจให้กับระบบรุ่นหลัง เช่น PyPI ของ Python และ npm ของ Node
แม้ว่าความนิยมของ Perl ลดลงนับตั้งแต่จุดสูงสุดในช่วงต้นปี 2000 แต่ยังคงใช้กันอย่างแพร่หลายในระบบเดิม ไปป์ไลน์การประมวลผลข้อความ และการดูแลระบบ Perl 6 (ปัจจุบันเรียกว่า **Raku**) เป็นภาษาที่แยกออกมาซึ่งนำแนวคิดต่างๆ ของ Perl มาใช้ใหม่
---

## ทำไม Perl ถึงมีความสำคัญ
- **การประมวลผลข้อความ**: สำนวนทั่วไปของ Perl เป็นภาษาที่ทรงพลังที่สุดในบรรดาภาษากระแสหลัก
- **CPAN**: มากกว่า 200,000 โมดูล — หนึ่งในที่เก็บแพ็คเกจที่ใหญ่ที่สุดและเก่าแก่ที่สุด
- **บรรทัดเดียว**: Perl เก่งในเรื่องการแปลงข้อความบรรทัดคำสั่งอย่างรวดเร็ว
- **ภาษากาว**: เชื่อมต่อระบบ แยกวิเคราะห์บันทึก ประมวลผลไฟล์ข้อมูล ทำงานอัตโนมัติ
- **ได้รับการพิสูจน์แล้วในการใช้งานจริง**: ขับเคลื่อนเว็บตั้งแต่ก่อนที่จะมี PHP ยังคงใช้งานโครงสร้างพื้นฐานที่สำคัญ
- **Raku (Perl 6)**: การออกแบบใหม่ที่ทันสมัยพร้อมไวยากรณ์ จุดเชื่อมต่อ และการจัดส่งหลายรายการ
## การแลกเปลี่ยน
| ข้อจำกัด | รายละเอียด | วิธีแก้ปัญหาทั่วไป |
|----------|---------|-------------------|
| **ความสามารถในการอ่าน** | "Perl เป็นภาษาเขียนเท่านั้น" — ไวยากรณ์ที่หนาแน่นและคลุมเครือ | ใช้เข้มงวด/คำเตือน; เขียนโค้ดโมดูลาร์ ใช้ Perl สมัยใหม่ (5.36+) |
| **ชุมชนเสื่อมถอย** | โครงการใหม่น้อยลงที่เลือก Perl | โค้ดเบสขนาดใหญ่ที่มีอยู่ต้องการการบำรุงรักษา ชุมชนที่ใช้งานอยู่ |
| **สองเวอร์ชันหลัก** | Perl 5 และ Raku (Perl 6) เป็นภาษาที่แตกต่างกัน | ใช้ Perl 5 สำหรับงานที่มีอยู่ Raku สำหรับโครงการใหม่ |
| **ไม่อินเทรนด์** | ไม่ค่อยมีการสอนใน bootcamps หรือมหาวิทยาลัย | เอกสารประกอบที่ครอบคลุมและโมดูล CPAN |
| **สัญลักษณ์ตัวแปร** |  คำนำหน้า`$`,`@`,`%`สามารถสร้างความสับสนให้กับผู้เริ่มต้น | เรียนรู้รูปแบบ:`$scalar`,`@array`,`%hash`|
| **ประสิทธิภาพ** | ช้ากว่าภาษาที่คอมไพล์สำหรับงานหนักด้านการประมวลผล | ใช้ส่วนขยาย C; ไม่ใช่เครื่องมือที่เหมาะสมสำหรับ HPC |
---

## พื้นฐานไวยากรณ์
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

## อิทธิพลของ Perl ในภาษาอื่น
| คุณสมบัติ | ภาษาที่นำมาใช้ |
|---------|--------------------------|
| นิพจน์ทั่วไป | Python, JavaScript, Java, Ruby, C#, PHP |
| ที่เก็บแพ็กเกจ (CPAN) | PyPI, npm, RubyGems, crates.io |
| เฮริดอกซ์ | Python, Ruby, PHP, Shell, JavaScript |
| `$_`ตัวแปรดีฟอลต์ |`$_`ของ Ruby,`$_`ของ PowerShell
| `map`/`grep`/`reduce`| Python, Ruby, JavaScript, Rust |
| `use strict`/ ขุย | TypeScript คำแนะนำประเภทของ Python |
---

## ไวยากรณ์และรูปแบบขั้นสูง
### การอ้างอิงและโครงสร้างข้อมูลที่ซับซ้อน
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

### การปิดและฟังก์ชันลำดับที่สูงกว่า
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

### นิพจน์ทั่วไปขั้นสูง
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

### Perl เชิงวัตถุ (Moose / Moo)
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

## การเห็นพ้องต้องกันและความเท่าเทียม
### การฟอร์กด้วย Parallel::ForkManager
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

### Coro — Coroutines แบบร่วมมือ
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

### IO::Async — การเขียนโปรแกรมที่ขับเคลื่อนด้วยเหตุการณ์
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

## การกำหนดค่าโครงการ & ระบบการสร้าง
### โครงสร้างโครงการ
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

### cpanfile - การจัดการการพึ่งพา
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

### คำสั่งการพึ่งพา
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### ไปป์ไลน์ CI/CD (การดำเนินการ GitHub)
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

## การทดสอบ
### ทดสอบ::เพิ่มเติม
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### คำสั่งทดสอบ
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## การทำงานร่วมกัน
### FFI::ตุ่นปากเป็ด
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — บูรณาการ C
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## รูปแบบการออกแบบ
### ซิงเกิลตัน
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

### ห่วงโซ่แห่งความรับผิดชอบ
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

## ประสิทธิภาพและการเพิ่มประสิทธิภาพ
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

## การปรับใช้
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

## เมื่อใดจึงควรใช้ Perl
| สถานการณ์ | ทำไมต้องเพิร์ล | ทางเลือกที่ดีกว่า |
|----------|---------|-------------------|
| การประมวลผลข้อความ / การแยกวิเคราะห์ | เครื่องมือ regex ที่ดีที่สุดในระดับเดียวกัน | Python สำหรับข้อมูลที่มีโครงสร้าง |
| การวิเคราะห์ไฟล์บันทึก | รวดเร็วในหนึ่งบรรทัด เครื่องมือที่ได้รับการพิสูจน์แล้ว | `awk`/`sed`สำหรับกรณีธรรมดา Python สำหรับคอมเพล็กซ์ |
| การดูแลระบบ | โดดเด่นทางประวัติศาสตร์ | Bash/PowerShell สำหรับงานง่ายๆ Python สำหรับคอมเพล็กซ์ |
| การบำรุงรักษาระบบเดิม | Perl หลายล้านบรรทัดในการผลิต | — |
| ชีวสารสนเทศศาสตร์ | การปรากฏตัวทางประวัติศาสตร์ที่แข็งแกร่ง (BioPerl) | หลาม (Biopython), R |
| การแปลงข้อมูลอย่างรวดเร็ว | ซับในหนึ่งเดียวที่ไม่มีใครเทียบได้ | `jq`,`awk`สำหรับรูปแบบที่มีโครงสร้าง |
| การพัฒนาเว็บ | หมดยุค CGI แล้ว | Python, Node.js, Go, PHP |
| โครงการขนาดใหญ่ใหม่ | ชุมชนได้ย้ายไปแล้ว | ไป, สนิม, Python |
| วิทยาศาสตร์ข้อมูล / ML | ไม่ใช่ระบบนิเวศ | หลาม, อาร์ |
---

## คำถามและคำตอบสังเคราะห์
### Q1: อะไรคือความแตกต่างระหว่าง`my`,`our`และ`local`?
**ตอบ:** คำหลักเหล่านี้ควบคุมการกำหนดขอบเขตของตัวแปร:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### Q2: ฉันจะประมวลผลไฟล์ข้อความอย่างมีประสิทธิภาพในภาษา Perl ได้อย่างไร
**ตอบ:** Perl เชี่ยวชาญด้านการประมวลผลข้อความ ใช้ตัวดำเนินการเพชรและ regex:
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

### Q3: ฉันจะใช้การอ้างอิงและโครงสร้างข้อมูลที่ซับซ้อนได้อย่างไร
**A:** การอ้างอิงเป็นวิธีของ Perl ในการสร้างโครงสร้างแบบซ้อน:
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

### Q4: ตัวแปรพิเศษของ Perl ที่ฉันควรรู้คืออะไร
**A:** Perl มีตัวแปรพิเศษมากมาย ที่สำคัญที่สุด:
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

### Q5: ฉันจะเขียน Perl ที่ทันสมัยและบำรุงรักษาได้อย่างไร
**ตอบ:** แนวทางปฏิบัติที่ดีที่สุดสำหรับ Perl สมัยใหม่:
- ใช้`strict`และ`warnings`เสมอ 
- ใช้`my`สำหรับตัวแปรทั้งหมด
- ใช้ตัวจัดการไฟล์ศัพท์:`open my $fh, '<', $file`
- ใช้โมดูลจาก CPAN (Moo/Moose สำหรับ OOP ลอง :: Tiny สำหรับข้อผิดพลาด)
- ใช้`say`แทน`print`(กับ`feature 'say'`)
- ฟอร์แมตด้วย `perltidy`
---

## การแก้ปัญหาลูกโซ่แห่งความคิด
### ปัญหาที่ 1: การวิเคราะห์ไฟล์บันทึก
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
แยกวิเคราะห์บันทึกการเข้าถึง Apache และนับจำนวนคำขอต่อที่อยู่ IP
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้ regex เพื่อแยกที่อยู่ IP แฮชเพื่อนับจำนวนครั้ง
**ขั้นตอนที่ 3: นำไปใช้**```perl
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

**ขั้นตอนที่ 4: ขยาย**
เพิ่มการกรองวันที่ การวิเคราะห์รหัสสถานะ และเอาต์พุตเป็น CSV
### ปัญหาที่ 2: การเปลี่ยนชื่อไฟล์แบทช์ด้วย Regex
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
เปลี่ยนชื่อไฟล์ที่ตรงกับรูปแบบ เปลี่ยนชื่อไฟล์ด้วย regex
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้`glob`หรือ`opendir`เพื่อค้นหาไฟล์ regex เพื่อเปลี่ยนชื่อ
**ขั้นตอนที่ 3: นำไปใช้**```perl
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

**ขั้นตอนที่ 4: ยืนยัน**
วิ่งด้วยแฟล็ก`--dry-run`ก่อน (แค่พิมพ์ ห้ามขยับ)
### ปัญหาที่ 3: การสร้าง Web Scraper อย่างง่าย
**ขั้นตอนที่ 1: ทำความเข้าใจปัญหา**
ดึงข้อมูลหน้าเว็บและแยกลิงก์ทั้งหมด
**ขั้นตอนที่ 2: ระบุแนวทาง**
ใช้`LWP::Simple`สำหรับการดึงข้อมูลและ regex หรือใช้`HTML::LinkExtor`สำหรับการแยกวิเคราะห์
**ขั้นตอนที่ 3: นำไปใช้**```perl
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

**ขั้นตอนที่ 4: ขยาย**
จัดการ URL ที่เกี่ยวข้อง กรองตามโดเมน และติดตามการแบ่งหน้า
---

## สรุป
ยุคทองของ Perl ได้ผ่านไปแล้ว แต่อิทธิพลของมันมีอยู่ทุกหนทุกแห่ง ทุกภาษาที่มีนิพจน์ทั่วไป ทุกตัวจัดการแพ็คเกจที่สร้างแบบจำลองบน CPAN และทุกระบบที่มี`map`/`grep`/`reduce`ล้วนมี DNA ของ Perl สำหรับโปรเจ็กต์ใหม่ นักพัฒนาส่วนใหญ่เข้าถึง Python หรือ Go แต่ Perl ยังคงเป็นเครื่องมือที่ทรงพลังสำหรับการประมวลผลข้อความ ระบบอัตโนมัติที่รวดเร็ว และการรักษาโค้ด Perl จำนวนมหาศาลที่ใช้โครงสร้างพื้นฐานที่สำคัญทั่วโลก การทำความเข้าใจ Perl ยังหมายถึงการทำความเข้าใจว่าการเขียนโปรแกรมสมัยใหม่มาจากไหน — มันกำหนดรูปแบบเครื่องมือและรูปแบบที่เราใช้ในปัจจุบัน