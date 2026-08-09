---
# فراداده
عنوان: "پرل"
توضیحات: "مرجع جامع برای زبان برنامه نویسی Perl که شامل مرور کلی، مبادلات، اصول نحو، اکوسیستم و زمان استفاده از آن می شود."
دسته بندی: "کدنویسی و فناوری"
نسخه: "1.0.0"
وضعیت: "فعال"
# مشارکت
نویسندگان:
  - نام: "تیم آموزشی مدل AI"
    ایمیل: ""
    نقش: "نویسنده_اصلی"
مشارکت کنندگان: []
تغییرات ثبت شده:
  - نسخه: "1.0.0"
    تاریخ: "05-08-2026"
    نویسنده: "تیم آموزشی مدل هوش مصنوعی"
    تغییرات: "فراداده YAML frontmatter برای ردیابی مشارکت کنندگان اضافه شد"
# نقد و بررسی
ایجاد شده: "05-08-2026"
last_modified: "05-08-2026"
بازبینی_تاریخ: "05-02-2027"
reviewed_by: "تیم پایگاه دانش کدنویسی و فناوری"
next_review: "05-08-2027"
# طبقه بندی
برچسب ها: [پرل، زبان برنامه نویسی، نحو، اکوسیستم، کدگذاری و فناوری]
سطح سختی: "متوسط"
پیش نیاز: []
تخمینی_زمان_خواندن: "24 دقیقه"
# راهنمای مشارکت
مشارکت:
  مجوز: "MIT"
  feedback_channel: "مشکلات GitHub"
  how_to_contribute: "ارسال روابط عمومی با تغییرات و به روز رسانی تغییرات"
  review_process: "تغییرات توسط نگهبانان دسته قبل از ادغام بررسی می شود"
---
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
| **سیجیل متغیر** |  پیشوندهای `$`، `@`،`%`می توانند مبتدیان را گیج کنند | الگو را بیاموزید:`$scalar`,`@array`,`%hash`|
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
| `$_`متغیر پیش فرض | Ruby's `$_`، PowerShell's`$_`|
| `map`/`grep`/`reduce`| پایتون، روبی، جاوا اسکریپت، Rust |
| `use strict`/ پرده | TypeScript، نکات نوع پایتون |
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
| تبدیل سریع داده ها | تک لاینرها بی رقیب هستند |  `jq`،`awk`برای فرمت های ساخت یافته |
| توسعه وب | دوران CGI به پایان رسیده است | Python، Node.js، Go، PHP |
| پروژه های بزرگ مقیاس جدید | انجمن حرکت کرده است | برو، رست، پایتون |
| علم داده / ML | نه اکوسیستم | پایتون، R |
---

## خلاصه
دوران طلایی پرل گذشته است، اما تأثیر آن همه جا است. هر زبانی با عبارات منظم، هر مدیر بسته ای که بر اساس CPAN مدل شده است، و هر سیستمی با`map`/`grep`/`reduce`حامل DNA پرل است. برای پروژه های جدید، بیشتر توسعه دهندگان پایتون یا Go را دنبال می کنند. اما Perl همچنان ابزاری قدرتمند برای پردازش متن، اتوماسیون سریع و حفظ حجم عظیمی از کدهای پرل است که زیرساخت های حیاتی را در سراسر جهان اجرا می کند. درک پرل همچنین به معنای درک این است که برنامه نویسی مدرن از کجا آمده است - ابزارها و الگوهایی را که امروزه استفاده می کنیم شکل داده است.