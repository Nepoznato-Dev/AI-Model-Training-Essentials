---
# Metadata
title: "Perl — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Perl ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Perl — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème Perl.
---

## Versions Perl
| Version | Remarques |
|---------|-------|
| **Perl 5.38+** | Stable actuel |
| **Perl 5.40** | Dernières avec de nouvelles fonctionnalités |
| **Raku (Perl 6)** | Refonte moderne (langue séparée) |
| **Orignal** | Système OO moderne |
| **Meuh** | Orignal léger |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Gestion des paquets
| Outil | Objectif |
|------|--------------|
| **CPAN** | Réseau d'archives Perl complet (plus de 200 000 modules) |
| **cpanm** | Installateur CPAN léger |
| **fichiercpan** | Déclaration de dépendance |
| **Carton** | Bundler de dépendances (comme Bundler) |
| **Dist::Zilla** | Constructeur de distribution |
| **App::cpanminus** | Client CPAN minimal |
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

## Cadres Web
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **Mojolicieux** | Pile complète | Moderne, propre, piles incluses |
| **Danseur2** | Micro | De type Sinatra, léger |
| **Catalyseur** | Pile complète | Entreprise, MVC |
| **Plac** | Boîte à outils PSGI | Interface Web de bas niveau |
| **Homme étoilé** | Serveur HTTP | Serveur PSGI |
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

## Base de données
| Technologie | Tapez |
|------------|------|
| **DBI** | Norme d'interface de base de données |
| **DBD::SQLite** | Pilote SQLite |
| **DBD::Page** | Pilote PostgreSQL |
| **DBD::mysql** | Pilote MySQL |
| **DBix::Class** | ORM complet |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Redis** | Client Redis |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **Test ::Plus** | Cadre de test standard |
| **Test2::Suite** | Tests modernes (recommandés) |
| **Test ::Fatal** | Tests d'exceptions |
| **Test ::MockModule** | Moqueur |
| **Test ::Profond** | Comparaison de données complexes |
| **Test::Sortie** | Capturer STDOUT/STDERR |
| **prouver** | Testeur |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **perlcritique** | Code peluchage et style |
| **perfidie** | Formatage des codes |
| **Développement ::Couverture** | Couverture du code |
| **Perl::Critique** | Application des politiques |
| **Test::Perl::Critique** | Critique dans les tests |
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

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **Orignal / Meuh** | Système d'objets moderne |
| **Mojolicieux** | Cadre Web |
| **DBI** | Interface de base de données |
| **DBix::Class** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | Analyse JSON |
| **YAML::XS** | Analyse YAML |
| **LWP::UserAgent** | Client HTTP |
| **HTTP::Petit** | Client HTTP minimal |
| **IO::Socket::SSL** | SSL/TLS |
| **Parallèle ::ForkManager** | Traitement parallèle |
| **MCE** | Moteur multicœur |
| **Essayez ::Petit** | Gestion des exceptions |
| **Chemin ::Petit** | Chemins de fichiers |
| **Liste::Util** | Liste des utilitaires |
| **Scalaire::Util** | Utilitaires scalaires |
| **DateHeure** | Gestion date/heure |
| **Journal ::Tout** | Façade forestière |
| **Config::Tout** | Configuration |
---

## Traitement de texte
| Outil | Objectif |
|---------|---------|
| **Expressions régulières** | Intégré et puissant |
| **Modèle ::Boîte à outils** | Moteur de modèles |
| **Texte ::CSV** | Analyse CSV |
| **XML::LibXML** | Traitement XML |
| **Mojo::DOM** | Analyse HTML/XML |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Code VS + Perl** | Prise en charge du langage Perl |
| **vim-perl** | Prise en charge de Vim Perl |
| **Emacs + mode cperl** | Environnement Perl classique |
| **Komodo** | EDI ActiveState Perl |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Homme étoilé** | Serveur web PSGI |
| **Hypnocrapaud** | Serveur Mojolicious |
| **Docker** | Conteneurisé |
| **PAR::Emballeur** | Exécutables autonomes |
| **Carton** | Regrouper les dépendances |
| **cpanfile + Carton** | Déploiements reproductibles |
---

## Résumé
L'écosystème de Perl est vaste et mature, avec CPAN hébergeant plus de 200 000 modules. La pile standard est : **Perl 5.38+** pour l'exécution, **cpanm** pour les packages, **Mojolicious** pour le Web, **DBI** + **DBIx::Class** pour les bases de données, **Test2::Suite** pour les tests, **perlcritic** pour le peluchage et **perltidy** pour le formatage. Perl excelle dans le traitement de texte, l'administration système, la bioinformatique et les applications Web existantes. Le Perl moderne (5.38+) avec signatures, déréférencement postfix et try/catch est nettement plus propre que ne le suggère sa réputation. L'écosystème est idéal pour les scripts d'administration système, le traitement des données et le prototypage rapide.