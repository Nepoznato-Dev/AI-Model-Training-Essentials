---
# Metadata
title: "Perl — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Perl ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [perl, ecosystem, tooling, cpan, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "13 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Perl — Przewodnik po ekosystemie i narzędziach
W tym przewodniku omówiono podstawowe narzędzia, struktury i infrastrukturę w ekosystemie Perla.
---

## Wersje Perla
| Wersja | Notatki |
|--------|-------|
| **Perla 5,38+** | Obecna stabilna |
| **5,40 perla** | Najnowsze z nowymi funkcjami |
| **Raku (Perl 6)** | Nowoczesne przeprojektowanie (oddzielny język) |
| **Łoś** | Nowoczesny system OO |
| **Muu** | Lekki łoś |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Zarządzanie pakietami
| Narzędzie | Cel |
|------|-------------|
| **CPAN** | Kompleksowa sieć archiwów Perla (ponad 200 000 modułów) |
| **cpanm** | Lekki instalator CPAN |
| **plik cpan** | Deklaracja zależności |
| **Karton** | Pakiet zależności (jak Bundler) |
| **Odległość::Zilla** | Kreator dystrybucji |
| **Aplikacja::cpanminus** | Minimalny klient CPAN |
```bash
cpanm Module::Name          # install module
cpanm --installdeps .       # install from cpanfile
cpanm --self-upgrade        # upgrade cpanm
carton install              # install from cpanfile (Carton)
carton exec perl script.pl  # run with bundled deps
```

```perl
# cpanfile
requires 'perl', '5.038';
requires 'Mojolicious', '>= 9.0';
requires 'DBI', '>= 1.643';
requires 'JSON::XS';

on 'test' => sub {
    requires 'Test::More', '>= 1.302';
    requires 'Test::Fatal';
    requires 'Test::MockModule';
};
```

---

## Struktury internetowe
| Ramy | Wpisz | Najlepsze dla |
|----------|------|---------|
| **Wesoły** | Pełny stos | Nowoczesne, czyste, na baterie |
| **Tancerz2** | Mikro | W stylu Sinatry, lekki |
| **Katalizator** | Pełny stos | Przedsiębiorstwo, MVC |
| **Plac** | Zestaw narzędzi PSGI | Interfejs sieciowy niskiego poziomu |
| **Gwiezdny** | Serwer HTTP | Serwer PSGI |
```perl
# Mojolicious::Lite example
use Mojolicious::Lite -signatures;

get '/hello' => sub ($c) {
    $c->render(text => 'Hello, World!');
};

get '/users/:id' => sub ($c) {
    my $id = $c->param('id');
    my $user = $c->users->find($id);
    $c->render(json => $user);
};

post '/users' => sub ($c) {
    my $data = $c->req->json;
    my $user = $c->users->create($data);
    $c->render(json => $user, status => 201);
};

app->start;
```

```perl
# Dancer2 example
use Dancer2;

get '/hello' => sub {
    return "Hello, World!";
};

get '/users/:id' => sub {
    my $id = route_parameters->get('id');
    my $user = schema->resultset('User')->find($id);
    return to_json($user);
};

dance;
```

---

## Baza danych
| Technologia | Wpisz |
|------------|------|
| **DBI** | Standard interfejsu bazy danych |
| **DBD::SQLite** | Sterownik SQLite |
| **DBD::Pg** | Sterownik PostgreSQL |
| **DBD::mysql** | Sterownik MySQL |
| **DBIx::Klasa** | Pełny ORM |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Redis** | Klient Redisa |
```perl
# DBI example
use DBI;

my $dbh = DBI->connect("dbi:SQLite:dbname=mydb.sqlite", "", "", {
    RaiseError => 1,
    PrintError => 0,
});

my $sth = $dbh->prepare("SELECT * FROM users WHERE age > ?");
$sth->execute(18);

while (my $row = $sth->fetchrow_hashref) {
    print "$row->{name} ($row->{email})\n";
}
```

```perl
# DBIx::Class example
package MyApp::Schema::Result::User;
use base 'DBIx::Class::Core';
__PACKAGE__->table('users');
__PACKAGE__->add_columns(qw/id name email age/);
__PACKAGE__->set_primary_key('id');

# Usage
my @adults = $schema->resultset('User')->search(
    { age => { '>' => 18 } },
    { order_by => 'name' }
);
```

---

## Testowanie
| Ramy | Cel |
|---------------|--------|
| **Test::Więcej** | Standardowe ramy testów |
| **Test2::Apartament** | Nowoczesne testowanie (zalecane) |
| **Test::Śmiertelny** | Testowanie wyjątków |
| **Test::MockModule** | Kpiąco |
| **Test::Głęboki** | Złożone porównanie danych |
| **Test::Wyjście** | Przechwyć STDOUT/STDERR |
| **udowodnij** | Biegacz testowy |
```perl
# Test2::V0 example
use Test2::V0;
use MyApp::UserService;

my $service = MyApp::UserService->new();

subtest 'find user' => sub {
    my $user = $service->find(1);
    is($user->name, 'Alice', 'found user by id');
    ok(defined $user, 'user is defined');
};

subtest 'not found' => sub {
    my $user = $service->find(999);
    is($user, undef, 'returns undef for missing user');
};

done_testing();
```

```bash
prove -lrv t/             # run tests (verbose)
prove -j4 t/              # parallel testing
```

---

## Jakość kodu
| Narzędzie | Cel |
|------|-------------|
| **perlkrytyczny** | Linting i styl kodu |
| **przewrotność** | Formatowanie kodu |
| **Rozwój::Okładka** | Pokrycie kodu |
| **Perl::Krytyk** | Egzekwowanie zasad |
| **Test::Perl::Krytyk** | Krytyk w testach |
```perl
# .perlcriticrc
severity = 3
[Variables::ProhibitPunctuationVars]
severity = 4
```

```bash
perlcritic --brutal lib/  # lint
perltidy -b lib/          # format
```

---

## Kluczowe biblioteki
| Biblioteka | Cel |
|--------|---------|
| **Łoś / Muu** | Nowoczesny system obiektowy |
| **Wesoły** | Struktura internetowa |
| **DBI** | Interfejs bazy danych |
| **DBIx::Klasa** | ORMO |
| **JSON::XS / Cpanel::JSON::XS** | Analiza JSON |
| **YAML::XS** | Analiza YAML |
| **LWP::UserAgent** | Klient HTTP |
| **HTTP::Mały** | Minimalny klient HTTP |
| **IO::Socket::SSL** | SSL/TLS |
| **Równolegle::ForkManager** | Przetwarzanie równoległe |
| **MCE** | Silnik wielordzeniowy |
| **Spróbuj::Mały** | Obsługa wyjątków |
| **Ścieżka::Mały** | Ścieżki plików |
| **Lista::Użytek** | Lista narzędzi |
| **Skalar::Narzędzie** | Narzędzia skalarne |
| **Data i godzina** | Obsługa daty/godziny |
| **Dziennik::Dowolny** | Logowanie fasady |
| **Konfiguracja::Dowolna** | Konfiguracja |
---

## Przetwarzanie tekstu
| Narzędzie | Cel |
|--------|---------|
| **Wyrażenia regularne** | Wbudowany, mocny |
| **Szablon::Zestaw narzędzi** | Silnik szablonów |
| **Tekst::CSV** | Analiza CSV |
| **XML::LibXML** | Przetwarzanie XML |
| **Mojo::DOM** | Analiza HTML/XML |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + Perl** | Obsługa języka Perl |
| **vim-perl** | Obsługa Vima Perla |
| **Emacs + tryb cperl** | Klasyczne środowisko Perla |
| **Komoda** | Stan aktywny Perla IDE |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Gwiezdny** | Serwer WWW PSGI |
| **Hipnotoada** | Serwer Mojolicious |
| **Doker** | Kontenerowy |
| **PAR::Paker** | Samodzielne pliki wykonywalne |
| **Karton** | Zależności pakietu |
| **cpanfile + karton** | Powtarzalne wdrożenia |
---

## Streszczenie
Ekosystem Perla jest rozległy i dojrzały, a CPAN obsługuje ponad 200 000 modułów. Standardowy stos to: **Perl 5.38+** jako środowisko uruchomieniowe, **cpanm** dla pakietów, **Mojolicious** dla Internetu, **DBI** + **DBIx::Class** dla baz danych, **Test2::Suite** do testowania, **perlcritic** do lintingu i **perltidy** do formatowania. Perl przoduje w przetwarzaniu tekstu, administrowaniu systemami, bioinformatyce i starszych aplikacjach internetowych. Nowoczesny Perl (5.38+) z sygnaturami, dereferencją do postfiksów i funkcją try/catch jest znacznie czystszy, niż sugeruje jego reputacja. Ekosystem jest idealny do tworzenia skryptów administratora systemu, przetwarzania danych i szybkiego tworzenia prototypów.