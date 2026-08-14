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
#पर्ल
पर्ल को लैरी वॉल द्वारा 1987 में एक व्यावहारिक टेक्स्ट-प्रोसेसिंग टूल के रूप में बनाया गया था। यह प्रारंभिक वेब विकास (सीजीआई स्क्रिप्ट), सिस्टम प्रशासन, जैव सूचना विज्ञान और नेटवर्क प्रोग्रामिंग की रीढ़ बन गया। पर्ल का दर्शन है "ऐसा करने के एक से अधिक तरीके हैं" (टीएमटीओडब्ल्यूटीडीआई) - भाषा आपको हर समस्या के लिए कई दृष्टिकोण प्रदान करती है, एकरूपता के बजाय अभिव्यक्ति को प्राथमिकता देती है।
आधुनिक प्रोग्रामिंग पर पर्ल का प्रभाव बहुत बड़ा है लेकिन अक्सर अदृश्य है: पर्ल के पैटर्न मिलान से प्रभावित नियमित अभिव्यक्तियाँ, अब पायथन, जावास्क्रिप्ट, जावा और अधिकांश अन्य भाषाओं में मानक हैं। सीपीएएन (कॉम्प्रिहेंसिव पर्ल आर्काइव नेटवर्क) पहले सॉफ्टवेयर पैकेज रिपॉजिटरी में से एक था और इसने पायथन के पीईपीआई और नोड के एनपीएम जैसे बाद के सिस्टम को प्रेरित किया।
जबकि 2000 के दशक की शुरुआत में अपने चरम के बाद से पर्ल की लोकप्रियता में गिरावट आई है, यह विरासत प्रणालियों, टेक्स्ट प्रोसेसिंग पाइपलाइनों और सिस्टम प्रशासन में व्यापक रूप से उपयोग किया जाता है। पर्ल 6 (जिसे अब **राकू** कहा जाता है) एक अलग भाषा है जिसने पर्ल की कई अवधारणाओं की फिर से कल्पना की है।
---

## पर्ल क्यों मायने रखता है
- **पाठ प्रसंस्करण**: पर्ल की नियमित अभिव्यक्तियाँ किसी भी मुख्यधारा की भाषा में सबसे शक्तिशाली हैं।
- **सीपीएएन**: 200,000 से अधिक मॉड्यूल - सबसे बड़े और सबसे पुराने पैकेज रिपॉजिटरी में से एक।
- **वन-लाइनर्स**: पर्ल त्वरित कमांड-लाइन टेक्स्ट ट्रांसफ़ॉर्मेशन में उत्कृष्टता प्राप्त करता है।
- **ग्लू भाषा**: सिस्टम को जोड़ता है, लॉग को पार्स करता है, डेटा फ़ाइलों को संसाधित करता है, कार्यों को स्वचालित करता है।
- **उत्पादन में सिद्ध**: PHP के अस्तित्व में आने से पहले से ही वेब को सशक्त बनाना। अभी भी महत्वपूर्ण बुनियादी ढांचा चल रहा है।
- **राकू (पर्ल 6)**: व्याकरण, जंक्शन और एकाधिक प्रेषण के साथ एक आधुनिक नया स्वरूप।
## समझौता
| सीमा | विवरण | विशिष्ट समाधान |
|----|---|-----|
| **पठनीयता** | "पर्ल केवल लिखने योग्य भाषा है" - सघन, गूढ़ वाक्यविन्यास | सख्त/चेतावनी का प्रयोग करें; मॉड्यूलर कोड लिखें; आधुनिक पर्ल (5.36+) का उपयोग करें |
| **घटता हुआ समुदाय** | पर्ल को चुनने वाले कम नए प्रोजेक्ट | बड़े मौजूदा कोडबेस को रखरखाव की आवश्यकता है; सक्रिय समुदाय |
| **दो प्रमुख संस्करण** | पर्ल 5 और राकू (पर्ल 6) अलग-अलग भाषाएँ हैं | मौजूदा कार्य के लिए पर्ल 5 का उपयोग करें; नई परियोजनाओं के लिए राकू |
| **फैशनेबल नहीं** | बूटकैंप या विश्वविद्यालयों में शायद ही कभी पढ़ाया जाता है | व्यापक दस्तावेज़ीकरण और सीपीएएन मॉड्यूल |
| **परिवर्तनीय सिगिल्स** | `$`,`@`,`%`उपसर्ग शुरुआती लोगों को भ्रमित कर सकते हैं | पैटर्न सीखें:`$scalar`,`@array`,`%hash`|
| **प्रदर्शन** | गणना-भारी कार्यों के लिए संकलित भाषाओं की तुलना में धीमी | सी एक्सटेंशन का प्रयोग करें; एचपीसी के लिए सही उपकरण नहीं |
---

## सिंटेक्स बुनियादी बातें
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

## अन्य भाषाओं पर पर्ल का प्रभाव
| फ़ीचर | वे भाषाएँ जिन्होंने इसे अपनाया |
|------|---------------------------------|
| नियमित अभिव्यक्ति | पायथन, जावास्क्रिप्ट, जावा, रूबी, सी#, पीएचपी |
| पैकेज रिपॉजिटरी (सीपीएएन) | पीईपीआई, एनपीएम, रूबीजेम्स, क्रेट्स.आईओ |
| हेरडॉक्स | पायथन, रूबी, पीएचपी, शेल, जावास्क्रिप्ट |
| `$_`डिफ़ॉल्ट वैरिएबल | रूबी का `$_`, पॉवरशेल का`$_`|
| `map`/`grep`/`reduce`| पायथन, रूबी, जावास्क्रिप्ट, जंग |
| `use strict`/ लिंटिंग | टाइपस्क्रिप्ट, पायथन के प्रकार के संकेत |
---

## उन्नत सिंटैक्स और पैटर्न
### संदर्भ और जटिल डेटा संरचनाएं
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

### क्लोजर और उच्च-क्रम के कार्य
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

### उन्नत नियमित अभिव्यक्तियाँ
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

### ऑब्जेक्ट-ओरिएंटेड पर्ल (मूस/मू)
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

## समवर्ती एवं समांतरता
### समानांतर के साथ फोर्किंग::फोर्कमैनेजर
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

### कोरो - सहकारी कोरटाइन्स
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

### IO::Async - इवेंट-संचालित प्रोग्रामिंग
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

## परियोजना विन्यास एवं निर्माण प्रणाली
### परियोजना संरचना
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

### cpanfile - निर्भरता प्रबंधन
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

### निर्भरता आदेश
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### सीआई/सीडी पाइपलाइन (गिटहब क्रियाएँ)
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

## परीक्षण
### टेस्ट::अधिक
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### टेस्ट कमांड
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## अंतरसंचालनीयता
### एफएफआई::प्लैटिपस
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### एक्सएस - सी एकीकरण
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## डिज़ाइन पैटर्न
### सिंगलटन
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

###जिम्मेदारी की जंजीर
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

## प्रदर्शन एवं अनुकूलन
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

## तैनाती
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

## पर्ल का उपयोग कब करें
| परिदृश्य | पर्ल क्यों | बेहतर विकल्प |
|---|---|-----|
| पाठ प्रसंस्करण / पार्सिंग | श्रेणी में सर्वोत्तम रेगेक्स इंजन | संरचित डेटा के लिए पायथन |
| लॉग फ़ाइल विश्लेषण | तेज़ वन-लाइनर, सिद्ध उपकरण |  साधारण मामलों के लिए`awk`/ `sed`; कॉम्प्लेक्स के लिए पायथन |
| सिस्टम प्रशासन | ऐतिहासिक दृष्टि से प्रभावशाली | सरल कार्यों के लिए बैश/पावरशेल; कॉम्प्लेक्स के लिए पायथन |
| विरासत प्रणाली रखरखाव | पर्ल की लाखों लाइनें उत्पादन में हैं | — |
| जैव सूचना विज्ञान | सशक्त ऐतिहासिक उपस्थिति (बायोपर्ल) | पायथन (बायोपिथॉन), आर |
| त्वरित डेटा परिवर्तन | वन-लाइनर्स अपराजेय हैं |  संरचित प्रारूपों के लिए`jq`,`awk`|
| वेब विकास | सीजीआई युग समाप्त हो गया है | पायथन, नोड.जेएस, गो, पीएचपी |
| नई बड़े पैमाने की परियोजनाएँ | समुदाय आगे बढ़ गया है | जाओ, जंग, अजगर |
| डेटा साइंस/एमएल | पारिस्थितिकी तंत्र नहीं | पायथन, आर |
---

## सिंथेटिक प्रश्नोत्तर
### Q1:`my`,`our`और`local`के बीच क्या अंतर है?
**ए:** ये कीवर्ड वेरिएबल स्कोपिंग को नियंत्रित करते हैं:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### Q2: मैं पर्ल में टेक्स्ट फ़ाइलों को कुशलतापूर्वक कैसे संसाधित करूं?
**ए:** पर्ल टेक्स्ट प्रोसेसिंग में उत्कृष्ट है। डायमंड ऑपरेटर और रेगेक्स का उपयोग करें:
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

### Q3: मैं संदर्भों और जटिल डेटा संरचनाओं का उपयोग कैसे करूं?
**ए:** संदर्भ नेस्टेड संरचनाएं बनाने का पर्ल का तरीका है:
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

### Q4: पर्ल के कौन से विशेष वेरिएबल्स मुझे पता होने चाहिए?
**ए:** पर्ल में कई विशेष चर हैं। सबसे महत्वपूर्ण:
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

### Q5: मैं आधुनिक, रखरखाव योग्य पर्ल कैसे लिखूं?
**ए:** आधुनिक पर्ल के लिए सर्वोत्तम अभ्यास:
- हमेशा`strict`और`warnings`का उपयोग करें 
- सभी वेरिएबल के लिए`my`का उपयोग करें
- शाब्दिक फ़ाइल हैंडल का उपयोग करें:`open my $fh, '<', $file`
- सीपीएएन से मॉड्यूल का उपयोग करें (ओओपी के लिए मू/मूस, त्रुटियों के लिए ट्राई::टिनी)
-`print`के बजाय`say`का उपयोग करें (`feature 'say'` के साथ)
-`perltidy`के साथ प्रारूप
---

## चेन-ऑफ़-थॉट समस्या का समाधान
### समस्या 1: लॉग फ़ाइल विश्लेषण
**चरण 1: समस्या को समझें**
अपाचे एक्सेस लॉग को पार्स करें और प्रति आईपी पते पर अनुरोधों की गणना करें।
**चरण 2: दृष्टिकोण को पहचानें**
आईपी पते निकालने के लिए रेगेक्स का उपयोग करें, घटनाओं की गणना करने के लिए हैश का उपयोग करें।
**चरण 3: कार्यान्वयन**```perl
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

**चरण 4: विस्तार करें**
सीएसवी के रूप में दिनांक फ़िल्टरिंग, स्थिति कोड विश्लेषण और आउटपुट जोड़ें।
### समस्या 2: रेगेक्स के साथ बैच फ़ाइल का नाम बदलना
**चरण 1: समस्या को समझें**
पैटर्न से मेल खाते हुए फ़ाइलों का नाम बदलें, रेगेक्स के साथ फ़ाइल नाम बदलें।
**चरण 2: दृष्टिकोण को पहचानें**
फ़ाइलें ढूंढने के लिए`glob`या`opendir`का उपयोग करें, नाम बदलने के लिए रेगेक्स का उपयोग करें।
**चरण 3: कार्यान्वयन**```perl
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

**चरण 4: सत्यापित करें**
पहले`--dry-run`ध्वज के साथ चलाएँ (सिर्फ प्रिंट करें, हिलें नहीं)।
### समस्या 3: एक साधारण वेब स्क्रैपर का निर्माण
**चरण 1: समस्या को समझें**
एक वेब पेज प्राप्त करें और सभी लिंक निकालें।
**चरण 2: दृष्टिकोण को पहचानें**
लाने और रेगेक्स के लिए`LWP::Simple`या पार्सिंग के लिए`HTML::LinkExtor`का उपयोग करें।
**चरण 3: कार्यान्वयन**```perl
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

**चरण 4: विस्तार करें**
संबंधित यूआरएल संभालें, डोमेन के आधार पर फ़िल्टर करें और पेजिनेशन का पालन करें।
---

## सारांश
पर्ल का स्वर्ण युग बीत चुका है, लेकिन इसका प्रभाव हर जगह है। नियमित अभिव्यक्तियों वाली प्रत्येक भाषा, CPAN पर आधारित प्रत्येक पैकेज मैनेजर, और`map`/`grep`/`reduce`वाले प्रत्येक सिस्टम में पर्ल का डीएनए होता है। नई परियोजनाओं के लिए, अधिकांश डेवलपर्स पायथन या गो का सहारा लेते हैं। लेकिन पर्ल टेक्स्ट प्रोसेसिंग, त्वरित स्वचालन और दुनिया भर में महत्वपूर्ण बुनियादी ढांचे को चलाने वाले पर्ल कोड की विशाल मात्रा को बनाए रखने के लिए एक शक्तिशाली उपकरण बना हुआ है। पर्ल को समझने का मतलब यह समझना भी है कि आधुनिक प्रोग्रामिंग कहां से आई - इसने हमारे द्वारा आज उपयोग किए जाने वाले टूल और पैटर्न को आकार दिया।