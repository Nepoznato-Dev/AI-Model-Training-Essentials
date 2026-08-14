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
# بيرل
تم إنشاء لغة Perl بواسطة Larry Wall في عام 1987 كأداة عملية لمعالجة النصوص. لقد أصبح العمود الفقري لتطوير الويب المبكر (نصوص CGI)، وإدارة النظام، والمعلوماتية الحيوية، وبرمجة الشبكات. فلسفة بيرل هي "هناك أكثر من طريقة واحدة للقيام بذلك" (TMTOWTDI) - تمنحك اللغة أساليب متعددة لكل مشكلة، وتفضل التعبير عن التوحيد.
تأثير بيرل على البرمجة الحديثة هائل ولكنه غالبًا ما يكون غير مرئي: التعبيرات العادية، المتأثرة بمطابقة أنماط بيرل، أصبحت الآن قياسية في بايثون، وجافا سكريبت، وجافا، ومعظم اللغات الأخرى. كانت CPAN (شبكة أرشيف Perl الشاملة) واحدة من أولى مستودعات حزم البرامج وألهمت أنظمة لاحقة مثل Python's PyPI وNode's npm.
على الرغم من انخفاض شعبية لغة Perl منذ ذروتها في أوائل العقد الأول من القرن الحادي والعشرين، إلا أنها لا تزال تستخدم على نطاق واسع في الأنظمة القديمة، وخطوط معالجة النصوص، وإدارة النظام. تعد لغة Perl 6 (التي تسمى الآن **Raku**) لغة منفصلة أعادت تصور العديد من مفاهيم Perl.
---

## لماذا تعتبر لغة بيرل مهمة؟
- **معالجة النص**: تعد التعبيرات العادية لـ Perl هي الأقوى من أي لغة سائدة.
- **CPAN**: أكثر من 200000 وحدة - واحدة من أكبر وأقدم مستودعات الحزم.
- **السطور الواحدة**: تتفوق لغة Perl في التحويلات السريعة لنصوص سطر الأوامر.
- **لغة الغراء**: تربط الأنظمة، وتوزع السجلات، وتعالج ملفات البيانات، وتقوم بأتمتة المهام.
- **مثبت في الإنتاج**: تشغيل الويب منذ ما قبل وجود PHP. لا تزال تعمل على البنية التحتية الحيوية.
- **Raku (Perl 6)**: إعادة تصميم حديثة تتضمن القواعد النحوية والوصلات والإرسالات المتعددة.
##المقايضات
| الحد | التفاصيل | الحل النموذجي |
|-----------|------------------------|---|
| ** سهولة القراءة ** | "Perl هي لغة للكتابة فقط" - بناء جملة كثيف ومبهم | استخدم تحذيرات/صارمة؛ كتابة التعليمات البرمجية المعيارية؛ استخدم لغة بيرل الحديثة (5.36+) |
| **مجتمع متدهور** | عدد أقل من المشاريع الجديدة تختار لغة Perl | تحتاج قاعدة التعليمات البرمجية الكبيرة الموجودة إلى الصيانة؛ مجتمع نشط |
| **إصداران رئيسيان** | Perl 5 وRaku (Perl 6) لغتان مختلفتان | استخدم Perl 5 للعمل الحالي؛ راكو للمشاريع الجديدة |
| **ليست عصرية** | نادرًا ما يتم تدريسه في المعسكرات التدريبية أو الجامعات | وثائق واسعة النطاق ووحدات CPAN |
| **العلامات المتغيرة** |  البادئات`$`,`@`,`%`يمكن أن تربك المبتدئين | تعلم النمط:`$scalar`,`@array`,`%hash`|
| **الأداء** | أبطأ من اللغات المترجمة لمهام الحوسبة الثقيلة | استخدام ملحقات C؛ ليست الأداة المناسبة لـ HPC |
---

## أساسيات بناء الجملة
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

## تأثير بيرل على اللغات الأخرى
| ميزة | اللغات التي اعتمدته |
|---------|-------------------------|
| التعابير العادية | بايثون، جافا سكريبت، جافا، روبي، C#، PHP |
| مستودعات الحزم (CPAN) | PyPI، npm، RubyGems، صناديق.io |
| الزنادقة | بايثون، روبي، PHP، شل، جافا سكريبت |
| `$_`المتغير الافتراضي | روبي `$_`، PowerShell's`$_`|
| `map`/`grep`/`reduce`| بايثون، روبي، جافا سكريبت، الصدأ |
| `use strict`/ فحص | TypeScript، تلميحات عن نوع Python |
---

## بناء الجملة والأنماط المتقدمة
### المراجع وهياكل البيانات المعقدة
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

### عمليات الإغلاق والوظائف ذات الترتيب الأعلى
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

### التعبيرات العادية المتقدمة
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

### لغة بيرل كائنية التوجه (Moose / Moo)
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

## التزامن والتوازي
### التفرع مع Parallel::ForkManager
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

### كورو — كوروتين التعاونية
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

### IO::Async — برمجة تعتمد على الأحداث
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

## تكوين المشروع ونظام البناء
### هيكل المشروع
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

### cpanfile — إدارة التبعيات
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

### أوامر التبعية
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### خط أنابيب CI/CD (إجراءات GitHub)
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

## الاختبار
### اختبار::المزيد
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### أوامر الاختبار
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## إمكانية التشغيل البيني
### FFI::خلد الماء
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — تكامل C
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## أنماط التصميم
### سينجلتون
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

### سلسلة المسؤولية
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

## الأداء والتحسين
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

## النشر
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

## متى تستخدم لغة بيرل
| السيناريو | لماذا بيرل | البديل الأفضل |
|----------|--------|------------------|
| معالجة النصوص/التحليل | أفضل محرك regex في فئته | بايثون للبيانات المنظمة |
| تحليل ملف السجل | بطانات سريعة وأدوات مجربة | `awk`/`sed`للحالات البسيطة؛ بايثون للمعقدة |
| إدارة النظام | المهيمنة تاريخيا | Bash/PowerShell للمهام البسيطة؛ بايثون للمعقدة |
| صيانة النظام القديم | ملايين خطوط بيرل قيد الإنتاج | — |
| المعلوماتية الحيوية | حضور تاريخي قوي (BioPerl) | بايثون (بيوبيثون)، R |
| تحويلات سريعة للبيانات | الخطوط المفردة لا تقبل المنافسة | `jq`,`awk`للتنسيقات المنظمة |
| تطوير الويب | انتهى عصر CGI | بايثون، Node.js، Go، PHP |
| مشاريع جديدة واسعة النطاق | لقد انتقل المجتمع | اذهب يا رست، بايثون |
| علم البيانات / تعلم الآلة | ليس النظام البيئي | بايثون، ر |
---

## أسئلة وأجوبة اصطناعية
### س1: ما الفرق بين`my`و`our`و `local`؟
**أ:** تتحكم هذه الكلمات الرئيسية في النطاق المتغير:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### السؤال الثاني: كيف يمكنني معالجة الملفات النصية بكفاءة في لغة Perl؟
**ج:** تتفوق لغة Perl في معالجة النصوص. استخدم عامل الماس والتعبير العادي:
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

### س3: كيف يمكنني استخدام المراجع وهياكل البيانات المعقدة؟
**أ:** المراجع هي طريقة بيرل لإنشاء بنيات متداخلة:
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

### س4: ما هي متغيرات لغة Perl الخاصة التي يجب أن أعرفها؟
**أ:** لدى لغة Perl العديد من المتغيرات الخاصة. الأهم:
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

### س5: كيف أكتب لغة بيرل حديثة وقابلة للصيانة؟
**ج:** أفضل ممارسات لغة Perl الحديثة:
- استخدم دائمًا`strict`و`warnings` 
- استخدم`my`لجميع المتغيرات
- استخدم مقابض الملفات المعجمية:`open my $fh, '<', $file`
- استخدام الوحدات النمطية من CPAN (Moo/Moose لـ OOP، حاول::Tiny للأخطاء)
- استخدم`say`بدلاً من`print`(مع `feature 'say'`)
- التنسيق باستخدام `perltidy`
---

## حل المشكلات المتعلقة بسلسلة الأفكار
### المشكلة الأولى: تحليل ملف السجل
**الخطوة الأولى: فهم المشكلة**
تحليل سجل وصول Apache واحتساب الطلبات لكل عنوان IP.
**الخطوة 2: تحديد النهج**
استخدم regex لاستخراج عناوين IP والتجزئة لحساب التكرارات.
**الخطوة 3: التنفيذ**```perl
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

**الخطوة 4: تمديد**
أضف تصفية التاريخ وتحليل رمز الحالة والإخراج كملف CSV.
### المشكلة الثانية: إعادة تسمية الملفات الدفعية باستخدام Regex
**الخطوة الأولى: فهم المشكلة**
إعادة تسمية الملفات المطابقة للنمط، وتحويل أسماء الملفات باستخدام regex.
**الخطوة 2: تحديد النهج**
استخدم`glob`أو`opendir`للعثور على الملفات، والتعبير العادي لتحويل الأسماء.
**الخطوة 3: التنفيذ**```perl
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

**الخطوة 4: التحقق**
قم بالتشغيل باستخدام علامة`--dry-run`أولاً (اطبع فقط، لا تحرك).
### المشكلة 3: إنشاء مكشطة ويب بسيطة
**الخطوة الأولى: فهم المشكلة**
جلب صفحة ويب واستخراج كافة الروابط.
**الخطوة 2: تحديد النهج**
استخدم`LWP::Simple`للجلب والتعبير العادي أو`HTML::LinkExtor`للتحليل.
**الخطوة 3: التنفيذ**```perl
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

**الخطوة 4: تمديد**
تعامل مع عناوين URL النسبية، وقم بالتصفية حسب المجال، واتبع ترقيم الصفحات.
---

## ملخص
لقد مر عصر بيرل الذهبي، ولكن تأثيره موجود في كل مكان. كل لغة ذات تعبيرات عادية، وكل مدير حزم مصمم على CPAN، وكل نظام به`map`/`grep`/`reduce`يحمل DNA الخاص بـ Perl. بالنسبة للمشاريع الجديدة، يستخدم معظم المطورين Python أو Go. لكن تظل لغة Perl أداة قوية لمعالجة النصوص، والأتمتة السريعة، والحفاظ على الكم الهائل من أكواد Perl التي تدير البنية التحتية الحيوية في جميع أنحاء العالم. إن فهم لغة Perl يعني أيضًا فهم مصدر البرمجة الحديثة، فهي التي شكلت الأدوات والأنماط التي نستخدمها اليوم.