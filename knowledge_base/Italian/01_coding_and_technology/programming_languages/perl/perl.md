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

#Perl
Perl è stato creato da Larry Wall nel 1987 come pratico strumento di elaborazione dei testi. È diventato la spina dorsale del primo sviluppo web (script CGI), dell'amministrazione di sistema, della bioinformatica e della programmazione di rete. La filosofia di Perl è "C'è più di un modo per farlo" (TMTOWTDI): il linguaggio offre molteplici approcci a ogni problema, favorendo l'espressività rispetto all'uniformità.
L'influenza di Perl sulla programmazione moderna è enorme ma spesso invisibile: le espressioni regolari, influenzate dal pattern match di Perl, sono ora standard in Python, JavaScript, Java e nella maggior parte degli altri linguaggi. Il CPAN (Comprehensive Perl Archive Network) è stato uno dei primi repository di pacchetti software e ha ispirato sistemi successivi come PyPI di Python e npm di Node.
Sebbene la popolarità di Perl sia diminuita rispetto al suo picco nei primi anni 2000, rimane ampiamente utilizzato nei sistemi legacy, nelle pipeline di elaborazione testi e nell'amministrazione di sistema. Perl 6 (ora chiamato **Raku**) è un linguaggio separato che ha reinventato molti dei concetti di Perl.
---

## Perché Perl è importante
- **Elaborazione del testo**: le espressioni regolari di Perl sono le più potenti di qualsiasi linguaggio tradizionale.
- **CPAN**: oltre 200.000 moduli: uno dei repository di pacchetti più grandi e antichi.
- **One-liner**: Perl eccelle nelle trasformazioni rapide del testo da riga di comando.
- **Lingua di colla**: collega sistemi, analizza registri, elabora file di dati, automatizza le attività.
- **Dimostrato in produzione**: alimenta il Web da prima che esistesse PHP. L'infrastruttura critica è ancora in funzione.
- **Raku (Perl 6)**: una riprogettazione moderna con grammatiche, giunzioni e invio multiplo.
## I compromessi
| Limitazione | Dettagli | Soluzione tipica |
|-----------|---------|-------------|
| **Leggibilità** | "Perl è un linguaggio di sola scrittura" — sintassi densa e criptica | Utilizzare rigorosi/avvertimenti; scrivere codice modulare; usa Perl moderno (5.36+) |
| **Comunità in declino** | Meno nuovi progetti scelgono Perl | La grande base di codice esistente necessita di manutenzione; comunità attiva |
| **Due versioni principali** | Perl 5 e Raku (Perl 6) sono linguaggi diversi | Utilizzare Perl 5 per il lavoro esistente; Raku per nuovi progetti |
| **Non trendy** | Raramente insegnato nei bootcamp o nelle università | Ampia documentazione e moduli CPAN |
| **Sigilli variabili** |  I prefissi`$`,`@`,`%`possono confondere i principianti | Impara lo schema:`$scalar`,`@array`,`%hash`|
| **Prestazioni** | Linguaggi più lenti dei linguaggi compilati per attività ad alto carico di calcolo | Utilizzare le estensioni C; non è lo strumento giusto per HPC |
---

## Fondamenti di sintassi
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

## L'influenza di Perl su altri linguaggi
| Caratteristica | Lingue che lo hanno adottato |
|---------|--------------------------|
| Espressioni regolari | Python, JavaScript, Java, Ruby, C#, PHP |
| Repository dei pacchetti (CPAN) | PyPI, npm, RubyGems, crates.io |
| Heredoc | Python, Ruby, PHP, Shell, JavaScript |
| `$_`variabile predefinita |`$_`di Ruby,`$_`di PowerShell |
| `map`/`grep`/`reduce`| Python, Ruby, JavaScript, Ruggine |
| `use strict`/ pelucchi | TypeScript, suggerimenti sul tipo di Python |
---

## Sintassi e modelli avanzati
### Riferimenti e strutture dati complesse
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

### Chiusure e funzioni di ordine superiore
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

### Espressioni regolari avanzate
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

### Perl orientato agli oggetti (Moose / Moo)
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

## Concorrenza e parallelismo
### Biforcazione con Parallel::ForkManager
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

### Coro — Coroutine cooperative
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

### IO::Async: programmazione guidata dagli eventi
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

## Configurazione del progetto e sistema di creazione
### Struttura del progetto
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

### cpanfile — Gestione delle dipendenze
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

### Comandi di dipendenza
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### Pipeline CI/CD (azioni GitHub)
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

## Test
### Prova::Altro
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### Comandi di prova
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## Interoperabilità
### FFI::Ornitorinco
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### Integrazione XS-C
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## Modelli di progettazione
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

### Catena di responsabilità
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

## Prestazioni e ottimizzazione
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

## Distribuzione
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

## Quando usare Perl
| Scenario | Perché Perl | Alternativa migliore |
|----------|---------|-------------|
| Elaborazione/analisi del testo | Motore regex migliore della categoria | Python per dati strutturati |
| Analisi del file di registro | Linee veloci, strumenti collaudati | `awk`/`sed`per casi semplici; Python per complesso |
| Amministrazione del sistema | Storicamente dominante | Bash/PowerShell per attività semplici; Python per complesso |
| Manutenzione del sistema legacy | Milioni di linee di Perl in produzione | — |
| Bioinformatica | Forte presenza storica (BioPerl) | Pitone (Biopython), R |
| Trasformazioni rapide dei dati | Le battute sono imbattibili | `jq`,`awk`per formati strutturati |
| Sviluppo web | L'era della CGI è finita | Python, Node.js, Go, PHP |
| Nuovi progetti su larga scala | La comunità è andata avanti | Vai, Ruggine, Python |
| Scienza dei dati/ML | Non l'ecosistema | Pitone, R |
---

## Riepilogo
L'epoca d'oro di Perl è passata, ma la sua influenza è ovunque. Ogni linguaggio con espressioni regolari, ogni gestore di pacchetti modellato su CPAN e ogni sistema con`map`/`grep`/`reduce`porta con sé il DNA di Perl. Per i nuovi progetti, la maggior parte degli sviluppatori ricorre a Python o Go. Ma Perl rimane uno strumento potente per l'elaborazione di testi, l'automazione rapida e il mantenimento della grande quantità di codice Perl che esegue infrastrutture critiche in tutto il mondo. Comprendere Perl significa anche capire da dove proviene la programmazione moderna: ha modellato gli strumenti e i modelli che utilizziamo oggi.