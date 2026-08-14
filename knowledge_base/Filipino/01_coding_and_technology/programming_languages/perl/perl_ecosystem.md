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
# Perl — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, framework, at imprastraktura sa Perl ecosystem.
---

## Mga Bersyon ng Perl
| Bersyon | Mga Tala |
|---------|-------|
| **Perl 5.38+** | Kasalukuyang kuwadra |
| **Perl 5.40** | Pinakabagong may mga bagong feature |
| **Raku (Perl 6)** | Makabagong disenyo (nakahiwalay na wika) |
| **Moose** | Modernong sistema ng OO |
| **Moo** | Magaang Moose |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **CPAN** | Comprehensive Perl Archive Network (200,000+ module) |
| **cpanm** | Magaang CPAN installer |
| **cpanfile** | Deklarasyon ng dependency |
| **Carton** | Dependency bundler (tulad ng Bundler) |
| **Dist::Zilla** | Tagabuo ng pamamahagi |
| **App::cpanminus** | Minimal CPAN client |
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

## Mga Web Framework
| Balangkas | Uri | Pinakamahusay Para sa |
|-----------|------|----------|
| **Mojolicious** | Full-stack | Moderno, malinis, may kasamang mga baterya |
| **Mananayaw2** | Micro | Parang Sinatra, magaan ang timbang |
| **Catalyst** | Full-stack | Enterprise, MVC |
| **Plack** | Toolkit ng PSGI | Mababang antas ng web interface |
| **Starman** | HTTP server | PSGI server |
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

## Database
| Teknolohiya | Uri |
|------------|------|
| **DBI** | Pamantayan ng interface ng database |
| **DBD::SQLite** | SQLite driver |
| **DBD::Pg** | PostgreSQL driver |
| **DBD::mysql** | MySQL driver |
| **DBix::Class** | Buong ORM |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Redis** | Redis client |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **Pagsubok::Higit pa** | Standard na balangkas ng pagsubok |
| **Test2::Suite** | Modernong pagsubok (inirerekomenda) |
| **Pagsubok::Fatal** | Exception testing |
| **Pagsubok::MockModule** | Nanunuya |
| **Pagsubok::Malalim** | Kumplikadong paghahambing ng data |
| **Pagsubok::Output** | Kunin ang STDOUT/STDERR |
| **patunayan** | Test runner |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **perlcritic** | Code linting at istilo |
| **perltidy** | Pag-format ng code |
| **Devel::Pabalat** | Saklaw ng code |
| **Perl::Manunuri** | Pagpapatupad ng patakaran |
| **Test::Perl::Critic** | Kritiko sa mga pagsusulit |
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

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **Moose / Moo** | Modern object system |
| **Mojolicious** | Web framework |
| **DBI** | Interface ng database |
| **DBix::Class** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | Pag-parse ng JSON |
| **YAML::XS** | YAML parsing |
| **LWP::UserAgent** | HTTP client |
| **HTTP::Maliit** | Minimal na HTTP client |
| **IO::Socket::SSL** | SSL/TLS |
| **Parallel::ForkManager** | Parallel processing |
| **MCE** | Maraming-core na makina |
| **Subukan::Maliit** | Exception handling |
| **Path::Tiny** | Mga path ng file |
| **Listahan::Util** | Listahan ng mga utility |
| **Scalar::Util** | Mga kagamitan sa scaler |
| **PetsaOras** | Petsa/oras ng pangangasiwa |
| **Log::Anumang** | Pag-log facade |
| **Config::Any** | Configuration |
---

## Pagproseso ng Teksto
| Tool | Layunin |
|---------|---------|
| **Mga regular na expression** | Built-in, makapangyarihan |
| **Template::Toolkit** | Template engine |
| **Text::CSV** | Pag-parse ng CSV |
| **XML::LibXML** | Pagproseso ng XML |
| **Mojo::DOM** | Pag-parse ng HTML/XML |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code + Perl** | Suporta sa wikang Perl |
| **vim-perl** | Suporta sa Vim Perl |
| **Emacs + cperl-mode** | Klasikong Perl na kapaligiran |
| **Komodo** | ActiveState Perl IDE |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Starman** | PSGI web server |
| **Hypnotoad** | Mojolicious server |
| **Docker** | Naka-container |
| **PAR::Packer** | Mga standalone executable |
| **Carton** | Bundle dependencies |
| **cpanfile + Carton** | Reproducible deployment |
---

## Buod
Ang ecosystem ng Perl ay malawak at nasa hustong gulang, na may CPAN na nagho-host ng 200,000+ module. Ang karaniwang stack ay: **Perl 5.38+** bilang runtime, **cpanm** para sa mga package, **Mojolicious** para sa web, **DBI** + **DBix::Class** para sa mga database, **Test2::Suite** para sa pagsubok, **perlcritic** para sa linting, at **perltidy** para sa pag-format. Napakahusay ng Perl sa pagpoproseso ng text, pangangasiwa ng system, bioinformatics, at mga legacy na web application. Ang modernong Perl (5.38+) na may mga lagda, postfix dereference, at try/catch ay mas malinis kaysa sa iminumungkahi ng reputasyon nito. Ang ecosystem ay perpekto para sa sysadmin scripting, pagpoproseso ng data, at mabilis na prototyping.