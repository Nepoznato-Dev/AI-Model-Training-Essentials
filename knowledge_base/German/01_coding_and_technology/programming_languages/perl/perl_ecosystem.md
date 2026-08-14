<!--
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

-->
# Perl – Ökosystem- und Tooling-Leitfaden
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Perl-Ökosystem.
---

## Perl-Versionen
| Version | Notizen |
|---------|-------|
| **Perl 5.38+** | Derzeit stabil |
| **Perl 5,40** | Neueste mit neuen Funktionen |
| **Raku (Perl 6)** | Modernes Redesign (separate Sprache) |
| **Elch** | Modernes OO-System |
| **Muh** | Leichter Elch |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Paketverwaltung
| Werkzeug | Zweck |
|------|---------|
| **CPAN** | Umfassendes Perl-Archivnetzwerk (über 200.000 Module) |
| **cpanm** | Leichtes CPAN-Installationsprogramm |
| **cpanfile** | Abhängigkeitserklärung |
| **Karton** | Abhängigkeits-Bundler (wie Bundler) |
| **Dist::Zilla** | Vertriebsentwickler |
| **App::cpanminus** | Minimaler CPAN-Client |
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

## Web-Frameworks
| Rahmen | Geben Sie | ein Am besten für |
|-----------|------|----------|
| **Mojolicious** | Full-Stack | Modern, sauber, Batterien inklusive |
| **Tänzer2** | Mikro | Sinatra-artig, leicht |
| **Katalysator** | Full-Stack | Unternehmen, MVC |
| **Plack** | PSGI-Toolkit | Low-Level-Webschnittstelle |
| **Starman** | HTTP-Server | PSGI-Server |
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

## Datenbank
| Technologie | Geben Sie | ein
|------------|------|
| **DBI** | Datenbankschnittstellenstandard |
| **DBD::SQLite** | SQLite-Treiber |
| **DBD::Pg** | PostgreSQL-Treiber |
| **DBD::mysql** | MySQL-Treiber |
| **DBIx::Class** | Vollständiges ORM |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Redis** | Redis-Client |
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

## Testen
| Rahmen | Zweck |
|-----------|---------|
| **Test::Mehr** | Standardtest-Framework |
| **Test2::Suite** | Moderne Tests (empfohlen) |
| **Test::Fatal** | Ausnahmetest |
| **Test::MockModule** | Spott |
| **Test::Deep** | Komplexer Datenvergleich |
| **Test::Ausgabe** | Erfassen Sie STDOUT/STDERR |
| **beweisen** | Testläufer |
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

## Codequalität
| Werkzeug | Zweck |
|------|---------|
| **Perlkritiker** | Code-Linting und -Stil |
| **perltidy** | Codeformatierung |
| **Devel::Cover** | Codeabdeckung |
| **Perl::Critic** | Durchsetzung von Richtlinien |
| **Test::Perl::Critic** | Kritiker in Tests |
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

## Wichtige Bibliotheken
| Bibliothek | Zweck |
|---------|---------|
| **Elch / Muh** | Modernes Objektsystem |
| **Mojolicious** | Web-Framework |
| **DBI** | Datenbankschnittstelle |
| **DBIx::Class** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | JSON-Analyse |
| **YAML::XS** | YAML-Analyse |
| **LWP::UserAgent** | HTTP-Client |
| **HTTP::Tiny** | Minimaler HTTP-Client |
| **IO::Socket::SSL** | SSL/TLS |
| **Parallel::ForkManager** | Parallelverarbeitung |
| **MCE** | Many-Core-Engine |
| **Versuchen Sie::Tiny** | Ausnahmebehandlung |
| **Pfad::Tiny** | Dateipfade |
| **List::Util** | Dienstprogramme auflisten |
| **Scalar::Util** | Skalare Dienstprogramme |
| **DatumUhrzeit** | Datums-/Uhrzeitverarbeitung |
| **Log::Any** | Protokollierungsfassade |
| **Config::Any** | Konfiguration |
---

## Textverarbeitung
| Werkzeug | Zweck |
|---------|---------|
| **Reguläre Ausdrücke** | Eingebaut, leistungsstark |
| **Vorlage::Toolkit** | Template-Engine |
| **Text::CSV** | CSV-Analyse |
| **XML::LibXML** | XML-Verarbeitung |
| **Mojo::DOM** | HTML/XML-Analyse |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS-Code + Perl** | Perl-Sprachunterstützung |
| **vim-perl** | Vim Perl-Unterstützung |
| **Emacs + Cperl-Modus** | Klassische Perl-Umgebung |
| **Komodo** | ActiveState Perl IDE |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Starman** | PSGI-Webserver |
| **Hypnotröte** | Mojolicious-Server |
| **Docker** | Containerisiert |
| **PAR::Packer** | Eigenständige ausführbare Dateien |
| **Karton** | Bundle-Abhängigkeiten |
| **cpanfile + Karton** | Reproduzierbare Bereitstellungen |
---

## Zusammenfassung
Das Perl-Ökosystem ist umfangreich und ausgereift. CPAN hostet mehr als 200.000 Module. Der Standard-Stack ist: **Perl 5.38+** als Laufzeit, **cpanm** für Pakete, **Mojolicious** für das Web, **DBI** + **DBIx::Class** für Datenbanken, **Test2::Suite** zum Testen, **perlcritic** für Linting und **perltidy** für die Formatierung. Perl zeichnet sich durch Textverarbeitung, Systemadministration, Bioinformatik und ältere Webanwendungen aus. Modernes Perl (5.38+) mit Signaturen, Postfix-Dereferenzierung und Try/Catch ist deutlich sauberer, als sein Ruf vermuten lässt. Das Ökosystem eignet sich ideal für Systemadministrator-Skripterstellung, Datenverarbeitung und schnelles Prototyping.