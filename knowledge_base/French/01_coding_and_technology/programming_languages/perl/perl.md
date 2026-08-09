---
# Métadonnées
titre : "Perl"
description : "Référence complète sur le langage de programmation Perl couvrant la présentation, les compromis, les principes fondamentaux de la syntaxe, l'écosystème et quand l'utiliser."
catégorie : "Codage et technologie"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
balises : [perl, langage de programmation, syntaxe, écosystème, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "24 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
#Perl
Perl a été créé par Larry Wall en 1987 comme outil pratique de traitement de texte. Il est devenu l'épine dorsale des premiers développements Web (scripts CGI), de l'administration système, de la bioinformatique et de la programmation réseau. La philosophie de Perl est « Il y a plus d'une façon de le faire » (TMTOWTDI) : le langage vous propose plusieurs approches pour chaque problème, privilégiant l'expressivité plutôt que l'uniformité.
L'influence de Perl sur la programmation moderne est énorme mais souvent invisible : les expressions régulières, influencées par la correspondance de modèles de Perl, sont désormais standard dans Python, JavaScript, Java et la plupart des autres langages. Le CPAN (Comprehensive Perl Archive Network) a été l'un des premiers référentiels de progiciels et a inspiré des systèmes ultérieurs tels que PyPI de Python et npm de Node.
Bien que la popularité de Perl ait diminué depuis son apogée au début des années 2000, il reste largement utilisé dans les systèmes existants, les pipelines de traitement de texte et l'administration système. Perl 6 (maintenant appelé **Raku**) est un langage distinct qui a réinventé de nombreux concepts de Perl.
---

## Pourquoi Perl est important
- **Traitement de texte** : les expressions régulières de Perl sont les plus puissantes de tous les langages grand public.
- **CPAN** : plus de 200 000 modules — l'un des référentiels de packages les plus grands et les plus anciens.
- **One-liners** : Perl excelle dans les transformations rapides de texte en ligne de commande.
- **Langage Glue** : connecte les systèmes, analyse les journaux, traite les fichiers de données, automatise les tâches.
- **Prouvé en production** : alimenter le Web avant même que PHP n'existe. Fonctionne toujours avec une infrastructure critique.
- **Raku (Perl 6)** : Une refonte moderne avec des grammaires, des jonctions et une répartition multiple.
## Les compromis
| Limitation | Détails | Solution de contournement typique |
|-----------|---------|-------------------|
| **Lisibilité** | "Perl est un langage en écriture seule" — syntaxe dense et énigmatique | Utilisez strict/warnings ; écrire du code modulaire ; utiliser Perl moderne (5.36+) |
| **Communauté en déclin** | Moins de nouveaux projets choisissant Perl | Une grande base de code existante nécessite une maintenance ; communauté active |
| **Deux versions majeures** | Perl 5 et Raku (Perl 6) sont des langages différents | Utilisez Perl 5 pour le travail existant ; Raku pour de nouveaux projets |
| **Pas tendance** | Rarement enseigné dans les bootcamps ou les universités | Documentation complète et modules CPAN |
| **Sigils variables** |  Les préfixes`$`,`@`,`%`peuvent dérouter les débutants | Apprenez le modèle :`$scalar`,`@array`,`%hash`|
| **Performances** | Plus lent que les langages compilés pour les tâches gourmandes en calcul | Utilisez les extensions C ; pas le bon outil pour HPC |
---

## Fondamentaux de la syntaxe
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

## L'influence de Perl sur d'autres langages
| Fonctionnalité | Langues qui l'ont adopté |
|---------|--------------------------|
| Expressions régulières | Python, JavaScript, Java, Ruby, C#, PHP |
| Dépôts de packages (CPAN) | PyPI, npm, RubyGems, caisses.io |
| Hérédocs | Python, Ruby, PHP, Shell, JavaScript |
| `$_`variable par défaut |`$_`de Ruby,`$_`de PowerShell |
| `map`/`grep`/`reduce`| Python, Ruby, JavaScript, Rouille |
| `use strict`/ pelucheux | TypeScript, les astuces de type Python |
---

## Syntaxe et modèles avancés
### Références et structures de données complexes
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

### Fermetures et fonctions d'ordre supérieur
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

### Expressions régulières avancées
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

### Perl orienté objet (Moose / Moo)
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

## Concurrence et parallélisme
### Forking avec Parallel::ForkManager
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

### Coro — Coroutines coopératives
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

### IO::Async — Programmation basée sur les événements
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

## Configuration du projet et système de construction
### Structure du projet
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

### cpanfile — Gestion des dépendances
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

### Commandes de dépendance
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### Pipeline CI/CD (actions GitHub)
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

## Tests
### Test ::Plus
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### Tester les commandes
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## Interopérabilité
### FFI::Ornithorynque
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — Intégration C
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## Modèles de conception
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

### Chaîne de responsabilité
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

## Performances et optimisation
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

## Déploiement
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

## Quand utiliser Perl
| Scénario | Pourquoi Perl | Meilleure alternative |
|--------------|---------|-------------------|
| Traitement/analyse de texte | Le meilleur moteur d'expression régulière de sa catégorie | Python pour les données structurées |
| Analyse des fichiers journaux | Des lignes simples rapides, des outils éprouvés | `awk`/`sed`pour les cas simples ; Python pour les complexes |
| Administration système | Historiquement dominant | Bash/PowerShell pour les tâches simples ; Python pour les complexes |
| Maintenance du système existant | Des millions de lignes de Perl en production | — |
| Bioinformatique | Forte présence historique (BioPerl) | Python (Biopython), R |
| Transformations rapides des données | Les one-liners sont imbattables | `jq`,`awk`pour les formats structurés |
| Développement Web | L'ère CGI est révolue | Python, Node.js, Go, PHP |
| Nouveaux projets à grande échelle | La communauté a évolué | Allez, Rouille, Python |
| Science des données / ML | Pas l'écosystème | Python, R |
---

## Résumé
L'âge d'or de Perl est révolu, mais son influence est partout. Chaque langage avec des expressions régulières, chaque gestionnaire de paquets calqué sur CPAN et chaque système avec`map`/`grep`/`reduce`porte l'ADN de Perl. Pour les nouveaux projets, la plupart des développeurs optent pour Python ou Go. Mais Perl reste un outil puissant pour le traitement de texte, l'automatisation rapide et la maintenance de la grande quantité de code Perl exécutant les infrastructures critiques dans le monde entier. Comprendre Perl signifie également comprendre d'où vient la programmation moderne : elle a façonné les outils et les modèles que nous utilisons aujourd'hui.