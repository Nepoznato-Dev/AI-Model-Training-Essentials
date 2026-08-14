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
#پرل
پرل توسط لری وال در سال 1987 به عنوان یک ابزار کاربردی برای پردازش متن ایجاد شد. این به ستون فقرات اولیه توسعه وب (اسکریپت های CGI)، مدیریت سیستم، بیوانفورماتیک و برنامه نویسی شبکه تبدیل شد. فلسفه پرل «بیش از یک راه برای انجام آن وجود دارد» (TMTOWTDI) است - این زبان رویکردهای متعددی را برای هر مشکلی به شما ارائه می‌دهد و بیانگر بودن را به یکنواختی ترجیح می‌دهد.
تأثیر پرل بر برنامه نویسی مدرن بسیار زیاد است، اما اغلب نامرئی است: عبارات منظم، تحت تأثیر تطبیق الگوی پرل، اکنون در پایتون، جاوا اسکریپت، جاوا و بسیاری از زبان های دیگر استاندارد هستند. CPAN (شبکه جامع بایگانی پرل) یکی از اولین مخازن بسته نرم افزاری بود و از سیستم های بعدی مانند PyPI پایتون و npm نود الهام گرفت.
در حالی که محبوبیت پرل از زمان اوج خود در اوایل دهه 2000 کاهش یافته است، همچنان به طور گسترده در سیستم های قدیمی، خطوط لوله پردازش متن و مدیریت سیستم استفاده می شود. پرل 6 (که اکنون **راکو** نامیده می شود) زبان جداگانه ای است که بسیاری از مفاهیم پرل را دوباره تصور می کند.
---

## چرا پرل مهم است
- **پردازش متن**: عبارات منظم پرل قوی ترین در بین زبان های رایج هستند.
- **CPAN**: بیش از 200000 ماژول - یکی از بزرگترین و قدیمی ترین مخازن بسته.
- **One-liners**: Perl در تبدیل سریع متن خط فرمان برتری دارد.
- ** زبان چسب **: سیستم ها را به هم متصل می کند، گزارش ها را تجزیه می کند، فایل های داده را پردازش می کند، وظایف را خودکار می کند.
- **در تولید ثابت شده**: قدرت بخشیدن به وب از قبل از وجود PHP. هنوز زیرساخت های حیاتی در حال اجرا است.
- **Raku (Perl 6)**: طراحی مجدد مدرن با دستور زبان، اتصالات و ارسال چندگانه.
## مبادلات
| محدودیت | جزئیات | راه حل معمولی |
|-----------|---------|-------------------|
| **خوانایی** | "Perl یک زبان فقط برای نوشتن است" - نحو مرموز و متراکم | از اخطار/سخت استفاده کنید. نوشتن کد مدولار استفاده از پرل مدرن (5.36+) |
| **جمعیت رو به زوال** | پروژه های جدید کمتری Perl | پایگاه کد بزرگ موجود نیاز به نگهداری دارد. جامعه فعال |
| **دو نسخه اصلی** | Perl 5 و Raku (Perl 6) زبان های مختلف هستند | از Perl 5 برای کارهای موجود استفاده کنید. راکو برای پروژه های جدید |
| ** مد روز نیست** | به ندرت در بوت کمپ یا دانشگاه تدریس می شود | مستندات گسترده و ماژول های CPAN |
| **سیجیل متغیر** |  پیشوندهای`$`,`@`,`%`می توانند مبتدیان را گیج کنند | آموزش الگو:`$scalar`,`@array`,`%hash`|
| **عملکرد** | کندتر از زبان های کامپایل شده برای کارهای محاسباتی سنگین | از پسوندهای C استفاده کنید. ابزار مناسبی برای HPC نیست |
---

## اصول نحو
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

## تأثیر پرل بر زبان های دیگر
| ویژگی | زبان هایی که آن را پذیرفتند |
|---------|-------------------------|
| عبارات منظم | پایتون، جاوا اسکریپت، جاوا، روبی، سی شارپ، پی اچ پی |
| مخازن بسته (CPAN) | PyPI، npm، RubyGems، crates.io |
| Heredocs | پایتون، روبی، پی اچ پی، شل، جاوا اسکریپت |
| `$_`متغیر پیش فرض | Ruby's`$_`, PowerShell's`$_`|
| `map`/`grep`/`reduce`| پایتون، روبی، جاوا اسکریپت، Rust |
| `use strict`/ linting | TypeScript، نکات نوع پایتون |
---

## نحو و الگوهای پیشرفته
### مراجع و ساختارهای داده پیچیده
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

### بسته شدن و عملکردهای بالاتر
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

### عبارات با قاعده پیشرفته
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

### پرل شی گرا (موس/مو)
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

## همزمانی و موازی
### فورک با Parallel::ForkManager
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

### Coro - Cooperative Coroutines
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

### IO::Async — برنامه نویسی رویداد محور
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

## پیکربندی پروژه و سیستم ساخت
### ساختار پروژه
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

### cpanfile — مدیریت وابستگی
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

### دستورات وابستگی
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### خط لوله CI/CD (اقدامات GitHub)
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

## تست
### تست::بیشتر
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### دستورات تست
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## قابلیت همکاری
### FFI:: Platypus
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS - C ادغام
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## الگوهای طراحی
### سینگلتون
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

### زنجیره مسئولیت
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

## عملکرد و بهینه سازی
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

## استقرار
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

## چه زمانی از پرل استفاده کنیم
| سناریو | چرا پرل | جایگزین بهتر |
|----------|---------|-------------------|
| پردازش متن / تجزیه | بهترین موتور regex در کلاس | پایتون برای داده های ساخت یافته |
| تجزیه و تحلیل فایل لاگ | تک لاینرهای سریع، ابزارهای اثبات شده | `awk`/`sed`برای موارد ساده؛ پایتون برای پیچیده |
| مدیریت سیستم | از نظر تاریخی غالب | Bash/PowerShell برای کارهای ساده؛ پایتون برای پیچیده |
| تعمیر و نگهداری سیستم قدیمی | میلیون ها خط پرل در حال تولید | — |
| بیوانفورماتیک | حضور قوی تاریخی (BioPerl) | پایتون (Biopython)، R |
| تبدیل سریع داده ها | تک لاینرها بی رقیب هستند | `jq`,`awk`برای فرمت های ساخت یافته |
| توسعه وب | دوران CGI به پایان رسیده است | Python، Node.js، Go، PHP |
| پروژه های بزرگ مقیاس جدید | انجمن حرکت کرده است | برو، رست، پایتون |
| علم داده / ML | نه اکوسیستم | پایتون، R |
---

## پرسش و پاسخ مصنوعی
### Q1: تفاوت بین `my`،`our`و`local`چیست؟
**A:** این کلمات کلیدی محدوده متغیر را کنترل می کنند:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### Q2: چگونه فایل های متنی را به طور موثر در پرل پردازش کنم؟
**A:** پرل در پردازش متن برتری دارد. از عملگر الماس و regex استفاده کنید:
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

### Q3: چگونه از مراجع و ساختارهای داده پیچیده استفاده کنم؟
**A:** مراجع راه پرل برای ایجاد ساختارهای تودرتو هستند:
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

### Q4: متغیرهای خاص پرل که باید بدانم چیست؟
**A:** Perl دارای متغیرهای ویژه زیادی است. مهم ترین:
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

### Q5: چگونه Perl مدرن و قابل نگهداری بنویسم؟
**A:** بهترین روش ها برای پرل مدرن:
- همیشه از`strict`و`warnings`استفاده کنید 
- از`my`برای همه متغیرها استفاده کنید
- از فایل‌های واژگانی استفاده کنید:`open my $fh, '<', $file`
- از ماژول های CPAN استفاده کنید (Moo/Moose برای OOP، سعی کنید::Tiny برای خطاها)
- از`say`به جای`print`(با `feature 'say'`) استفاده کنید
- فرمت با `perltidy`
---

## حل مسئله زنجیره ای از فکر
### مشکل 1: تجزیه و تحلیل فایل لاگ
**مرحله 1: مشکل را درک کنید**
گزارش دسترسی آپاچی را تجزیه کنید و درخواست ها را در هر آدرس IP بشمارید.
**مرحله 2: رویکرد را شناسایی کنید**
از regex برای استخراج آدرس های IP، هش برای شمارش رخدادها استفاده کنید.
**مرحله 3: پیاده سازی **```perl
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

**مرحله 4: تمدید**
فیلتر تاریخ، تجزیه و تحلیل کد وضعیت، و خروجی را به عنوان CSV اضافه کنید.
### مشکل 2: تغییر نام دسته ای فایل با Regex
**مرحله 1: مشکل را درک کنید**
تغییر نام فایل های مطابق با یک الگو، تبدیل نام فایل ها با regex.
**مرحله 2: رویکرد را شناسایی کنید**
برای یافتن فایل‌ها از`glob`یا`opendir`و برای تبدیل نام‌ها از regex استفاده کنید.
**مرحله 3: پیاده سازی **```perl
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

**مرحله 4: تایید **
ابتدا با پرچم`--dry-run`اجرا کنید (فقط چاپ کنید، حرکت نکنید).
### مشکل 3: ساختن یک Web Scraper ساده
**مرحله 1: مشکل را درک کنید**
یک صفحه وب را واکشی کنید و همه پیوندها را استخراج کنید.
**مرحله 2: رویکرد را شناسایی کنید**
از`LWP::Simple`برای واکشی و regex یا`HTML::LinkExtor`برای تجزیه استفاده کنید.
**مرحله 3: پیاده سازی **```perl
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

**مرحله 4: تمدید**
URL های نسبی را مدیریت کنید، بر اساس دامنه فیلتر کنید و صفحه بندی را دنبال کنید.
---

## خلاصه
دوران طلایی پرل گذشته است، اما تأثیر آن همه جا است. هر زبانی با عبارات منظم، هر مدیر بسته‌ای که بر اساس CPAN مدل شده است، و هر سیستمی با`map`/`grep`/`reduce`DNA پرل را حمل می‌کند. برای پروژه های جدید، بیشتر توسعه دهندگان پایتون یا Go را دنبال می کنند. اما Perl همچنان ابزاری قدرتمند برای پردازش متن، اتوماسیون سریع و حفظ حجم عظیمی از کدهای پرل است که زیرساخت های حیاتی را در سراسر جهان اجرا می کند. درک پرل همچنین به معنای درک این است که برنامه نویسی مدرن از کجا آمده است - ابزارها و الگوهایی را که امروزه استفاده می کنیم شکل داده است.