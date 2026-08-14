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

# Perl
Ang Perl ay nilikha ni Larry Wall noong 1987 bilang isang praktikal na tool sa pagproseso ng teksto. Ito ang naging backbone ng maagang web development (CGI scripts), system administration, bioinformatics, at network programming. Ang pilosopiya ni Perl ay "There's More than One Way To Do It" (TMTOWTDI) — ang wika ay nagbibigay sa iyo ng maraming diskarte sa bawat problema, na pinapaboran ang pagpapahayag kaysa pagkakapareho.
Ang impluwensya ni Perl sa modernong programming ay napakalaki ngunit kadalasang hindi nakikita: ang mga regular na expression, na naiimpluwensyahan ng pagtutugma ng pattern ng Perl, ay pamantayan na ngayon sa Python, JavaScript, Java, at karamihan sa iba pang mga wika. Ang CPAN (Comprehensive Perl Archive Network) ay isa sa mga unang software package repository at nagbigay inspirasyon sa mga susunod na sistema tulad ng Python's PyPI at Node's npm.
Bagama't bumaba ang kasikatan ng Perl mula nang tumama ito noong unang bahagi ng 2000s, nananatili itong malawakang ginagamit sa mga legacy system, mga pipeline sa pagpoproseso ng text, at pangangasiwa ng system. Ang Perl 6 (tinatawag na **Raku**) ay isang hiwalay na wika na muling naglarawan sa marami sa mga konsepto ni Perl.
---

## Bakit Mahalaga ang Perl
- **Pagproseso ng teksto**: Ang mga regular na expression ng Perl ay ang pinakamakapangyarihan sa anumang pangunahing wika.
- **CPAN**: Higit sa 200,000 modules — isa sa pinakamalaki at pinakamatandang package repository.
- **One-liners**: Ang Perl ay mahusay sa mabilis na pagbabago ng text-line ng command.
- **Glue language**: Nag-uugnay sa mga system, nag-parse ng mga log, nagpoproseso ng mga file ng data, nag-o-automate ng mga gawain.
- **Napatunayan sa produksyon**: Pinapaandar ang web mula noong bago pa umiral ang PHP. Nagpapatakbo pa rin ng kritikal na imprastraktura.
- **Raku (Perl 6)**: Isang modernong muling disenyo na may mga grammar, junction, at maramihang dispatch.
## Ang mga Trade-off
| Limitasyon | Mga Detalye | Karaniwang Workaround |
|-----------|---------|-------------------|
| **Kakayahang mabasa** | "Ang Perl ay isang write-only na wika" — siksik, misteryosong syntax | Gumamit ng mahigpit/babala; sumulat ng modular code; gumamit ng modernong Perl (5.36+) |
| **Tumababa na komunidad** | Mas kaunting mga bagong proyekto ang pumipili sa Perl | Malaking umiiral na codebase ay nangangailangan ng pagpapanatili; aktibong komunidad |
| **Dalawang pangunahing bersyon** | Ang Perl 5 at Raku (Perl 6) ay magkaibang wika | Gamitin ang Perl 5 para sa kasalukuyang trabaho; Raku para sa mga bagong proyekto |
| **Hindi uso** | Bihirang ituro sa mga bootcamp o unibersidad | Malawak na dokumentasyon at CPAN modules |
| **Mga variable na sigil** |  Ang mga prefix na`$`,`@`,`%`ay maaaring malito ang mga nagsisimula | Alamin ang pattern:`$scalar`,`@array`,`%hash`|
| **Pagganap** | Mas mabagal kaysa sa mga pinagsama-samang wika para sa mga gawaing mabibigat sa compute | Gumamit ng mga extension ng C; hindi ang tamang tool para sa HPC |
---

## Syntax Fundamentals
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

## Impluwensiya ni Perl sa Iba pang mga Wika
| Tampok | Mga Wikang Nagpatibay Nito |
|---------|------------------------|
| Mga regular na expression | Python, JavaScript, Java, Ruby, C#, PHP |
| Mga imbakan ng package (CPAN) | PyPI, npm, RubyGems, crates.io |
| Heredocs | Python, Ruby, PHP, Shell, JavaScript |
| `$_`default na variable | Ruby's`$_`, PowerShell's`$_`|
| `map`/`grep`/`reduce`| Python, Ruby, JavaScript, Rust |
| `use strict`/ linting | TypeScript, mga pahiwatig ng uri ng Python |
---

## Advanced na Syntax at Mga Pattern
### Mga Sanggunian at Kumplikadong Istruktura ng Data
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

### Mga Pagsasara at Mga Pag-andar na Mas Mataas ang Order
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

### Advanced na Regular Expression
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

### Object-Oriented Perl (Moose / Moo)
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

## Concurrency at Paralelismo
### Forking na may Parallel::ForkManager
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

### Coro — Cooperative Coroutines
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

### IO::Async — Programming na Batay sa Kaganapan
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

## Project Configuration at Build System
### Istraktura ng Proyekto
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

### cpanfile — Pamamahala ng Dependency
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

### Mga Utos ng Dependency
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### CI/CD Pipeline (GitHub Actions)
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

## Pagsubok
### Pagsubok::Higit pa
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### Mga Utos ng Pagsubok
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## Interoperability
### FFI::Platypus
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — C Integration
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## Mga Pattern ng Disenyo
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

### Kadena ng Pananagutan
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

## Pagganap at Pag-optimize
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

## Deployment
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

## Kailan Gamitin ang Perl
| Sitwasyon | Bakit Perl | Mas mahusay na Alternatibo |
|----------|---------|-------------------|
| Pagproseso / pag-parse ng teksto | Pinakamahusay sa klase na regex engine | Python para sa structured data |
| Pagsusuri ng log file | Mabilis na one-liner, napatunayang mga tool | `awk`/`sed`para sa mga simpleng kaso; Python para sa kumplikadong |
| Pangangasiwa ng system | Makasaysayang nangingibabaw | Bash/PowerShell para sa mga simpleng gawain; Python para sa kumplikadong |
| Pagpapanatili ng legacy system | Milyun-milyong linya ng Perl sa produksyon | — |
| Bioinformatics | Malakas na presensya sa kasaysayan (BioPerl) | Python (Biopython), R |
| Mabilis na pagbabago ng data | Ang mga one-liner ay walang kapantay | `jq`,`awk`para sa mga structured na format |
| Pagbuo ng web | Tapos na ang panahon ng CGI | Python, Node.js, Go, PHP |
| Mga bagong malakihang proyekto | Ang komunidad ay lumipat sa | Go, Rust, Python |
| Data science / ML | Hindi ang ecosystem | Python, R |
---

## Synthetic na Q&A
### Q1: Ano ang pagkakaiba ng`my`,`our`, at`local`?
**S:** Kinokontrol ng mga keyword na ito ang variable scoping:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### Q2: Paano ko mapoproseso nang mahusay ang mga text file sa Perl?
**A:** Ang Perl ay mahusay sa pagpoproseso ng text. Gamitin ang diamond operator at regex:
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

### Q3: Paano ko gagamitin ang mga sanggunian at kumplikadong istruktura ng data?
**A:** Ang mga sanggunian ay ang paraan ni Perl upang lumikha ng mga nested na istruktura:
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

### Q4: Ano ang mga espesyal na variable ng Perl na dapat kong malaman?
**A:** Maraming espesyal na variable ang Perl. Ang pinakamahalaga:
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

### Q5: Paano ako magsusulat ng moderno, napapanatiling Perl?
**S:** Pinakamahuhusay na kagawian para sa modernong Perl:
- Palaging gamitin ang`strict`at`warnings`
- Gamitin ang`my`para sa lahat ng mga variable
- Gumamit ng lexical filehandles:`open my $fh, '<', $file`
- Gumamit ng mga module mula sa CPAN (Moo/Moose para sa OOP, Subukan::Maliit para sa mga error)
- Gamitin ang`say`sa halip na`print`(na may`feature 'say'`)
- Format gamit ang `perltidy`
---

## Paglutas ng Problema ng Chain-of-Thought
### Problema 1: Pagsusuri ng Log File
**Hakbang 1: Unawain ang Problema**
I-parse ang isang Apache access log at bilangin ang mga kahilingan sa bawat IP address.
**Hakbang 2: Tukuyin ang Diskarte**
Gumamit ng regex upang kunin ang mga IP address, hash upang mabilang ang mga pangyayari.
**Hakbang 3: Ipatupad**```perl
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

**Hakbang 4: Palawakin**
Magdagdag ng pag-filter ng petsa, pagsusuri ng status code, at output bilang CSV.
### Problema 2: Batch File Renaming gamit ang Regex
**Hakbang 1: Unawain ang Problema**
Palitan ang pangalan ng mga file na tumutugma sa isang pattern, binabago ang mga filename gamit ang regex.
**Hakbang 2: Tukuyin ang Diskarte**
Gamitin ang`glob`o`opendir`upang maghanap ng mga file, regex upang baguhin ang mga pangalan.
**Hakbang 3: Ipatupad**```perl
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

**Hakbang 4: I-verify**
Patakbuhin muna gamit ang`--dry-run`flag (i-print lang, huwag gumalaw).
### Problema 3: Pagbuo ng Simpleng Web Scraper
**Hakbang 1: Unawain ang Problema**
Kumuha ng web page at kunin ang lahat ng link.
**Hakbang 2: Tukuyin ang Diskarte**
Gamitin ang`LWP::Simple`para sa pagkuha at regex o`HTML::LinkExtor`para sa pag-parse.
**Hakbang 3: Ipatupad**```perl
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

**Hakbang 4: Palawakin**
Pangasiwaan ang mga kaugnay na URL, i-filter ayon sa domain, at sundin ang pagination.
---

## Buod
Ang ginintuang panahon ni Perl ay lumipas na, ngunit ang impluwensya nito ay nasa lahat ng dako. Ang bawat wika na may mga regular na expression, bawat manager ng package na namodelo sa CPAN, at bawat system na may`map`/`grep`/`reduce`ay nagdadala ng DNA ni Perl. Para sa mga bagong proyekto, karamihan sa mga developer ay umaabot sa Python o Go. Ngunit ang Perl ay nananatiling isang mahusay na tool para sa pagpoproseso ng teksto, mabilis na pag-automate, at pagpapanatili ng napakaraming Perl code na nagpapatakbo ng kritikal na imprastraktura sa buong mundo. Ang pag-unawa sa Perl ay nangangahulugan din ng pag-unawa kung saan nanggaling ang modernong programming — humubog ito sa mga tool at pattern na ginagamit natin ngayon.