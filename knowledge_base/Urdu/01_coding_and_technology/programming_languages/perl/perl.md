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

#پرل
پرل کو لیری وال نے 1987 میں ایک عملی ٹیکسٹ پروسیسنگ ٹول کے طور پر بنایا تھا۔ یہ ابتدائی ویب ڈویلپمنٹ (CGI اسکرپٹس)، سسٹم ایڈمنسٹریشن، بایو انفارمیٹکس، اور نیٹ ورک پروگرامنگ کی ریڑھ کی ہڈی بن گیا۔ پرل کا فلسفہ ہے "یہ کرنے کا ایک سے زیادہ راستہ ہے" (TMTOWTDI) - زبان آپ کو ہر مسئلے کے لیے متعدد نقطہ نظر فراہم کرتی ہے، یکسانیت پر اظہار خیال کی حمایت کرتی ہے۔
جدید پروگرامنگ پر پرل کا اثر بہت زیادہ ہے لیکن اکثر پوشیدہ ہے: پرل کے پیٹرن میچنگ سے متاثر ہونے والے ریگولر ایکسپریشنز اب ازگر، جاوا اسکرپٹ، جاوا، اور بیشتر دیگر زبانوں میں معیاری ہیں۔ CPAN (Comprehensive Perl Archive Network) پہلے سافٹ ویئر پیکج ریپوزٹریوں میں سے ایک تھا اور بعد میں Python's PyPI اور Node's npm جیسے سسٹمز کو متاثر کرتا تھا۔
اگرچہ 2000 کی دہائی کے اوائل میں پرل کی مقبولیت میں اس کے عروج کے بعد سے کمی واقع ہوئی ہے، لیکن یہ میراثی نظام، ٹیکسٹ پروسیسنگ پائپ لائنز، اور سسٹم ایڈمنسٹریشن میں وسیع پیمانے پر استعمال ہوتی ہے۔ پرل 6 (جسے اب **راکو** کہا جاتا ہے) ایک الگ زبان ہے جس نے پرل کے بہت سے تصورات کو دوبارہ تصور کیا ہے۔
---

## پرل کیوں اہمیت رکھتا ہے۔
- **ٹیکسٹ پروسیسنگ**: پرل کے ریگولر ایکسپریشنز کسی بھی مرکزی دھارے کی زبان میں سب سے زیادہ طاقتور ہوتے ہیں۔
- **CPAN**: 200,000 سے زیادہ ماڈیولز - سب سے بڑے اور پرانے پیکیج ریپوزٹریوں میں سے ایک۔
- **ون لائنرز**: پرل فوری کمانڈ لائن ٹیکسٹ ٹرانسفارمیشنز پر سبقت لے جاتا ہے۔
- **گلو لینگویج**: سسٹم کو جوڑتا ہے، لاگز کو پارس کرتا ہے، ڈیٹا فائلوں پر کارروائی کرتا ہے، کاموں کو خودکار کرتا ہے۔
- **پیداوار میں ثابت**: پی ایچ پی کے موجود ہونے سے پہلے سے ویب کو طاقتور بنانا۔ اب بھی اہم انفراسٹرکچر چل رہا ہے۔
- **Raku (Perl 6)**: گرامر، جنکشن اور متعدد ڈسپیچ کے ساتھ ایک جدید ری ڈیزائن۔
## ٹریڈ آف
| حد | تفصیلات | عام حل |
|------------|---------|-------------------|
| **پڑھنے کی اہلیت** | "پرل صرف لکھنے کی زبان ہے" - گھنے، خفیہ نحو | سخت/انتباہات کا استعمال کریں؛ ماڈیولر کوڈ لکھیں؛ جدید پرل استعمال کریں (5.36+) |
| **کمیونٹی ** | پرل کا انتخاب کرنے والے کم نئے منصوبے بڑے موجودہ کوڈ بیس کو دیکھ بھال کی ضرورت ہے۔ فعال کمیونٹی |
| **دو بڑے ورژن** | پرل 5 اور راکو (پرل 6) مختلف زبانیں ہیں۔ موجودہ کام کے لیے پرل 5 استعمال کریں۔ نئے منصوبوں کے لیے راکو |
| **رجحان نہیں** | بوٹ کیمپوں یا یونیورسٹیوں میں شاذ و نادر ہی پڑھایا جاتا ہے۔ وسیع دستاویزات اور CPAN ماڈیولز |
| **متغیر سگلز** | `$`,`@`,`%`کے سابقے ابتدائیوں کو الجھا سکتے ہیں | پیٹرن سیکھیں:`$scalar`,`@array`,`%hash`|
| **کارکردگی** | کمپیوٹ بھاری کاموں کے لیے مرتب شدہ زبانوں سے سست | سی ایکسٹینشنز کا استعمال کریں؛ HPC کے لیے صحیح ٹول نہیں ہے |
---

## نحوی بنیادی باتیں
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

## دوسری زبانوں پر پرل کا اثر
| خصوصیت | زبانیں جنہوں نے اسے اپنایا |
|---------|--------------------------------------|
| باقاعدہ اظہار | Python, JavaScript, Java, Ruby, C#, PHP |
| پیکیج ریپوزٹریز (CPAN) | PyPI, npm, RubyGems, crates.io |
| ہیروڈکس | ازگر، روبی، پی ایچ پی، شیل، جاوا اسکرپٹ |
| `$_`ڈیفالٹ متغیر | روبی کا`$_`, PowerShell's`$_`|
| `map`/`grep`/`reduce`| Python, Ruby, JavaScript, Rust |
| `use strict`/ linting | TypeScript، ازگر کی قسم کے اشارے |
---

## اعلی درجے کی نحو اور نمونے۔
### حوالہ جات اور پیچیدہ ڈیٹا سٹرکچر
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

### بندش اور اعلی آرڈر کے افعال
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

### ایڈوانسڈ ریگولر ایکسپریشنز
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

### آبجیکٹ اورینٹڈ پرل (Moose / Moo)
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

## ہم آہنگی اور ہم آہنگی
### متوازی کے ساتھ فورکنگ::فورک مینجر
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

### کورو - کوآپریٹو کوروٹینز
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

### IO::Async - ایونٹ سے چلنے والا پروگرامنگ
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

## پروجیکٹ کنفیگریشن اینڈ بلڈ سسٹم
### پروجیکٹ کا ڈھانچہ
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

### cpanfile — انحصار کا انتظام
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

### انحصار کے احکامات
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### CI/CD پائپ لائن (GitHub ایکشنز)
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

## ٹیسٹنگ
### ٹیسٹ::مزید
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### ٹیسٹ کمانڈز
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## انٹرآپریبلٹی
### FFI::Platypus
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — C انٹیگریشن
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## ڈیزائن پیٹرن
### سنگلٹن
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

### ذمہ داری کا سلسلہ
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

## کارکردگی اور اصلاح
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

## تعیناتی۔
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

## پرل کب استعمال کریں۔
| منظر نامہ | کیوں پرل | بہتر متبادل |
|------------|---------|-------------------|
| ٹیکسٹ پروسیسنگ / پارسنگ | بہترین درجے کا ریجیکس انجن | سٹرکچرڈ ڈیٹا کے لیے ازگر |
| لاگ فائل کا تجزیہ | تیز ون لائنرز، ثابت شدہ ٹولز | `awk`/`sed`سادہ مقدمات کے لیے؛ پیچیدہ کے لیے ازگر |
| سسٹم ایڈمنسٹریشن | تاریخی طور پر غالب | آسان کاموں کے لیے Bash/PowerShell؛ پیچیدہ کے لیے ازگر |
| میراثی نظام کی بحالی | پیداوار میں پرل کی لاکھوں لائنیں | - |
| بایو انفارمیٹکس | مضبوط تاریخی موجودگی (BioPerl) | Python (Biopython)، R |
| ڈیٹا کی فوری تبدیلیاں | ون لائنرز ناقابل شکست ہیں | `jq`,`awk`سٹرکچرڈ فارمیٹس کے لیے |
| ویب ڈویلپمنٹ | CGI کا دور ختم ہو گیا ہے | Python, Node.js, Go, PHP |
| نئے بڑے پیمانے پر منصوبے | کمیونٹی آگے بڑھ گئی ہے | جاؤ، زنگ آلود، ازگر |
| ڈیٹا سائنس / ایم ایل | ماحولیاتی نظام نہیں | ازگر، آر |
---

## مصنوعی سوال و جواب
### Q1: `my`، `our`، اور`local`میں کیا فرق ہے؟
**A:** یہ مطلوبہ الفاظ متغیر اسکوپنگ کو کنٹرول کرتے ہیں:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### Q2: میں پرل میں ٹیکسٹ فائلوں کو مؤثر طریقے سے کیسے پروسیس کروں؟
**A:** پرل ٹیکسٹ پروسیسنگ میں بہترین ہے۔ ڈائمنڈ آپریٹر اور ریجیکس استعمال کریں:
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

### Q3: میں حوالہ جات اور پیچیدہ ڈیٹا ڈھانچے کو کیسے استعمال کروں؟
**A:** حوالہ جات پرل کا گھریلو ڈھانچے بنانے کا طریقہ ہیں:
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

### Q4: پرل کے خصوصی متغیرات کیا ہیں جن کے بارے میں مجھے معلوم ہونا چاہیے؟
**A:** پرل میں بہت سے خاص متغیرات ہیں۔ سب سے اہم:
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

### Q5: میں جدید، برقرار رکھنے کے قابل پرل کیسے لکھوں؟
**A:** جدید پرل کے لیے بہترین طریقے:
- ہمیشہ`strict`اور`warnings`استعمال کریں۔ 
- تمام متغیرات کے لیے`my`استعمال کریں۔
- لغوی فائل ہینڈلز استعمال کریں:`open my $fh, '<', $file`
- CPAN سے ماڈیولز استعمال کریں (OOP کے لیے Moo/Moose، Try::Tiny for errors)
-`print`کی بجائے`say`استعمال کریں (`feature 'say'` کے ساتھ)
-`perltidy`کے ساتھ فارمیٹ کریں۔
---

## سوچ کا مسئلہ حل کرنا
### مسئلہ 1: لاگ فائل کا تجزیہ
**مرحلہ 1: مسئلہ کو سمجھیں**
اپاچی رسائی لاگ پارس کریں اور فی IP ایڈریس کی درخواستوں کو شمار کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
آئی پی ایڈریس نکالنے کے لیے ریجیکس کا استعمال کریں، واقعات کو گننے کے لیے ہیش۔
**مرحلہ 3: نافذ کریں**```perl
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

**مرحلہ 4: توسیع کریں**
تاریخ کی فلٹرنگ، اسٹیٹس کوڈ کا تجزیہ، اور آؤٹ پٹ بطور CSV شامل کریں۔
### مسئلہ 2: بیچ فائل کا نام ریجیکس کے ساتھ تبدیل کرنا
**مرحلہ 1: مسئلہ کو سمجھیں**
پیٹرن سے مماثل فائلوں کا نام تبدیل کریں، فائل ناموں کو ریجیکس کے ساتھ تبدیل کریں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
فائلیں تلاش کرنے کے لیے`glob`یا `opendir`، ناموں کو تبدیل کرنے کے لیے regex استعمال کریں۔
**مرحلہ 3: نافذ کریں**```perl
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

**مرحلہ 4: تصدیق کریں**
پہلے`--dry-run`پرچم کے ساتھ چلائیں (صرف پرنٹ کریں، حرکت نہ کریں)۔
### مسئلہ 3: ایک سادہ ویب سکریپر بنانا
**مرحلہ 1: مسئلہ کو سمجھیں**
ایک ویب صفحہ حاصل کریں اور تمام لنکس نکالیں۔
**مرحلہ 2: نقطہ نظر کی شناخت کریں**
بازیافت کرنے کے لیے`LWP::Simple`استعمال کریں اور ریجیکس یا تجزیہ کرنے کے لیے`HTML::LinkExtor`استعمال کریں۔
**مرحلہ 3: نافذ کریں**```perl
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

**مرحلہ 4: توسیع کریں**
متعلقہ یو آر ایل کو ہینڈل کریں، ڈومین کے لحاظ سے فلٹر کریں، اور صفحہ بندی کی پیروی کریں۔
---

## خلاصہ
پرل کا سنہری دور گزر چکا ہے لیکن اس کا اثر ہر جگہ ہے۔ ریگولر ایکسپریشنز والی ہر زبان، CPAN پر وضع کردہ ہر پیکیج مینیجر، اور`map`/`grep`/`reduce`والا ہر سسٹم پرل کا ڈی این اے رکھتا ہے۔ نئے پروجیکٹس کے لیے، زیادہ تر ڈویلپرز Python یا Go تک پہنچ جاتے ہیں۔ لیکن پرل ٹیکسٹ پروسیسنگ، فوری آٹومیشن، اور دنیا بھر میں اہم انفراسٹرکچر چلانے والے پرل کوڈ کی وسیع مقدار کو برقرار رکھنے کے لیے ایک طاقتور ٹول ہے۔ پرل کو سمجھنے کا مطلب یہ بھی ہے کہ یہ سمجھنا کہ جدید پروگرامنگ کہاں سے آئی ہے - اس نے ان ٹولز اور پیٹرن کو شکل دی جنہیں ہم آج استعمال کرتے ہیں۔