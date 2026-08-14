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
# Perł
Perl został stworzony przez Larry'ego Walla w 1987 roku jako praktyczne narzędzie do przetwarzania tekstu. Stało się podstawą wczesnego tworzenia stron internetowych (skrypty CGI), administrowania systemami, bioinformatyki i programowania sieciowego. Filozofia Perla brzmi: „Jest więcej niż jeden sposób, aby to zrobić” (TMTOWTDI) — język zapewnia wiele podejść do każdego problemu, przedkładając ekspresję nad jednolitość.
Wpływ Perla na współczesne programowanie jest ogromny, ale często niewidoczny: wyrażenia regularne, na które wpływa dopasowywanie wzorców Perla, są obecnie standardem w Pythonie, JavaScript, Javie i większości innych języków. CPAN (Comprehensive Perl Archive Network) była jednym z pierwszych repozytoriów pakietów oprogramowania i zainspirowała późniejsze systemy, takie jak PyPI Pythona i npm Node'a.
Chociaż popularność Perla spadła od jego szczytu na początku XXI wieku, pozostaje on szeroko stosowany w starszych systemach, potokach przetwarzania tekstu i administracji systemami. Perl 6 (obecnie nazywany **Raku**) to odrębny język, w którym na nowo zdefiniowano wiele koncepcji Perla.
---

## Dlaczego Perl ma znaczenie
- **Przetwarzanie tekstu**: Wyrażenia regularne Perla są najpotężniejszymi ze wszystkich języków głównego nurtu.
- **CPAN**: Ponad 200 000 modułów — jedno z największych i najstarszych repozytoriów pakietów.
- **Jednoliniowe**: Perl wyróżnia się szybkim przekształcaniem tekstu w wierszu poleceń.
- **Język klejenia**: łączy systemy, analizuje logi, przetwarza pliki danych, automatyzuje zadania.
- **Sprawdzone w produkcji**: Zasilanie sieci WWW jeszcze przed pojawieniem się PHP. Nadal działa infrastruktura krytyczna.
- **Raku (Perl 6)**: Nowoczesne przeprojektowanie z gramatyką, skrzyżowaniami i wielokrotnym wysyłaniem.
## Kompromisy
| Ograniczenie | Szczegóły | Typowe obejście |
|----------|---------|--------------------------------|
| **Czytelność** | „Perl jest językiem przeznaczonym tylko do zapisu” — gęsta, tajemnicza składnia | Użyj rygorystycznych/ostrzeżeń; napisać kod modułowy; użyj nowoczesnego Perla (5.36+) |
| **Spadająca społeczność** | Mniej nowych projektów wybiera Perl | Duża istniejąca baza kodu wymaga konserwacji; aktywna społeczność |
| **Dwie główne wersje** | Perl 5 i Raku (Perl 6) to różne języki | Użyj Perla 5 do istniejącej pracy; Raku na nowe projekty |
| **Nie modne** | Rzadko uczy się na obozach lub na uniwersytetach | Obszerna dokumentacja i moduły CPAN |
| **Zmienne pieczęcie** |  Przedrostki`$`,`@`,`%`mogą dezorientować początkujących | Naucz się wzoru:`$scalar`,`@array`,`%hash`|
| **Wydajność** | Wolniejsze niż języki skompilowane do zadań wymagających dużej mocy obliczeniowej | Użyj rozszerzeń C; nie jest właściwym narzędziem dla HPC |
---

## Podstawy składni
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

## Wpływ Perla na inne języki
| Funkcja | Języki, które to przyjęły |
|--------|------------------------------|
| Wyrażenia regularne | Python, JavaScript, Java, Ruby, C#, PHP |
| Repozytoria pakietów (CPAN) | PyPI, npm, RubyGems, crates.io |
| Heredoki | Python, Ruby, PHP, Shell, JavaScript |
|  Zmienna domyślna`$_`| Ruby `$_`, PowerShell`$_`|
| `map`/`grep`/`reduce`| Python, Ruby, JavaScript, Rdza |
| `use strict`/ linting | TypeScript, wskazówki dotyczące typów Pythona |
---

## Zaawansowana składnia i wzorce
### Odniesienia i złożone struktury danych
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

### Zamknięcia i funkcje wyższego rzędu
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

### Zaawansowane wyrażenia regularne
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

### Perl obiektowy (Moose / Muu)
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

## Współbieżność i równoległość
### Rozwidlanie za pomocą Parallel::ForkManager
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

### Coro — współprogramy kooperacyjne
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

### IO::Async — programowanie sterowane zdarzeniami
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

## Konfiguracja projektu i budowanie systemu
### Struktura projektu
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

### cpanfile — Zarządzanie zależnościami
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

### Polecenia zależności
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### Potok CI/CD (akcje w GitHub)
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

## Testowanie
### Test::Więcej
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### Polecenia testowe
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## Interoperacyjność
### FFI::Dziobak
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — Integracja z C
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## Wzorce projektowe
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

### Łańcuch odpowiedzialności
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

## Wydajność i optymalizacja
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

## Zastosowanie
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

## Kiedy używać Perla
| Scenariusz | Dlaczego Perl | Lepsza alternatywa |
|---------|---------|--------------------------------|
| Przetwarzanie / analizowanie tekstu | Najlepszy w swojej klasie silnik regex | Python dla danych strukturalnych |
| Analiza pliku dziennika | Szybkie jednowierszowe, sprawdzone narzędzia | `awk`/`sed`dla prostych przypadków; Python dla złożonych |
| Administracja systemem | Historycznie dominujący | Bash/PowerShell do prostych zadań; Python dla złożonych |
| Konserwacja starszych systemów | Miliony linii Perla w produkcji | — |
| Bioinformatyka | Silna obecność historyczna (BioPerl) | Python (Biopython), R |
| Szybkie transformacje danych | Jednolinijkowe są nie do pobicia | `jq`,`awk`dla formatów strukturalnych |
| Tworzenie stron internetowych | Era CGI dobiegła końca | Python, Node.js, Go, PHP |
| Nowe projekty na dużą skalę | Społeczność poszła dalej | Idź, Rust, Python |
| Nauka o danych / ML | Nie ekosystem | Python, R |
---

## Syntetyczne pytania i odpowiedzi
### P1: Jaka jest różnica między`my`,`our`i`local`?
**O:** Te słowa kluczowe kontrolują zakres zmiennych:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### P2: Jak efektywnie przetwarzać pliki tekstowe w Perlu?
**O:** Perl przoduje w przetwarzaniu tekstu. Użyj operatora diamentu i wyrażenia regularnego:
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

### P3: Jak używać referencji i złożonych struktur danych?
**O:** Referencje to sposób Perla na tworzenie zagnieżdżonych struktur:
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

### P4: Jakie specjalne zmienne Perla powinienem znać?
**O:** Perl ma wiele specjalnych zmiennych. Najważniejsze:
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

### P5: Jak napisać nowoczesny, łatwy w utrzymaniu Perl?
**A:** Najlepsze praktyki dotyczące współczesnego Perla:
- Zawsze używaj`strict`i`warnings`
- Użyj`my`dla wszystkich zmiennych
- Użyj leksykalnych uchwytów plików:`open my $fh, '<', $file`
- Użyj modułów z CPAN (Moo/Moose dla OOP, Try::Tiny dla błędów)
- Użyj`say`zamiast`print`(z`feature 'say'`)
- Sformatuj za pomocą `perltidy`
---

## Rozwiązywanie problemów na podstawie łańcucha myślowego
### Problem 1: Analiza pliku dziennika
**Krok 1: Zrozum problem**
Przeanalizuj dziennik dostępu Apache i zlicz żądania na adres IP.
**Krok 2: Zidentyfikuj podejście**
Użyj wyrażenia regularnego do wyodrębnienia adresów IP, skrótu do zliczenia wystąpień.
**Krok 3: Wdróż**```perl
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

**Krok 4: Przedłuż**
Dodaj filtrowanie dat, analizę kodów stanu i dane wyjściowe w formacie CSV.
### Problem 2: Wsadowa zmiana nazwy pliku za pomocą wyrażenia regularnego
**Krok 1: Zrozum problem**
Zmień nazwę plików pasujących do wzorca, przekształcając nazwy plików za pomocą wyrażenia regularnego.
**Krok 2: Zidentyfikuj podejście**
Użyj`glob`lub `opendir`, aby znaleźć pliki, a wyrażenie regularne, aby przekształcić nazwy.
**Krok 3: Wdróż**```perl
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

**Krok 4: Zweryfikuj**
Najpierw uruchom z flagą`--dry-run`(po prostu wydrukuj, nie ruszaj się).
### Problem 3: Budowa prostego skrobaka sieciowego
**Krok 1: Zrozum problem**
Pobierz stronę internetową i wyodrębnij wszystkie linki.
**Krok 2: Zidentyfikuj podejście**
Użyj`LWP::Simple`do pobierania i wyrażenia regularnego lub`HTML::LinkExtor`do analizowania.
**Krok 3: Wdróż**```perl
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

**Krok 4: Przedłuż**
Obsługuj względne adresy URL, filtruj według domeny i śledź paginację.
---

## Streszczenie
Złota era Perla minęła, ale jego wpływ jest wszędzie. Każdy język z wyrażeniami regularnymi, każdy menedżer pakietów wzorowany na CPAN i każdy system z`map`/`grep`/`reduce`ma w sobie DNA Perla. W przypadku nowych projektów większość programistów sięga po Python lub Go. Jednak Perl pozostaje potężnym narzędziem do przetwarzania tekstu, szybkiej automatyzacji i utrzymywania ogromnej ilości kodu Perla obsługującego infrastrukturę krytyczną na całym świecie. Zrozumienie Perla oznacza także zrozumienie, skąd wzięło się współczesne programowanie — ukształtowało ono narzędzia i wzorce, których używamy dzisiaj.