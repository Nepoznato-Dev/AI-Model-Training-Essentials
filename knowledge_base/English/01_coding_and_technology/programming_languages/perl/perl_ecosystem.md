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
# Perl — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the Perl ecosystem.

---

## Perl Versions

| Version | Notes |
|---------|-------|
| **Perl 5.38+** | Current stable |
| **Perl 5.40** | Latest with new features |
| **Raku (Perl 6)** | Modern redesign (separate language) |
| **Moose** | Modern OO system |
| **Moo** | Lightweight Moose |

```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Package Management

| Tool | Purpose |
|------|---------|
| **CPAN** | Comprehensive Perl Archive Network (200,000+ modules) |
| **cpanm** | Lightweight CPAN installer |
| **cpanfile** | Dependency declaration |
| **Carton** | Dependency bundler (like Bundler) |
| **Dist::Zilla** | Distribution builder |
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

## Web Frameworks

| Framework | Type | Best For |
|-----------|------|----------|
| **Mojolicious** | Full-stack | Modern, clean, batteries-included |
| **Dancer2** | Micro | Sinatra-like, lightweight |
| **Catalyst** | Full-stack | Enterprise, MVC |
| **Plack** | PSGI toolkit | Low-level web interface |
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

| Technology | Type |
|------------|------|
| **DBI** | Database interface standard |
| **DBD::SQLite** | SQLite driver |
| **DBD::Pg** | PostgreSQL driver |
| **DBD::mysql** | MySQL driver |
| **DBIx::Class** | Full ORM |
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

## Testing

| Framework | Purpose |
|-----------|---------|
| **Test::More** | Standard test framework |
| **Test2::Suite** | Modern testing (recommended) |
| **Test::Fatal** | Exception testing |
| **Test::MockModule** | Mocking |
| **Test::Deep** | Complex data comparison |
| **Test::Output** | Capture STDOUT/STDERR |
| **prove** | Test runner |

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

## Code Quality

| Tool | Purpose |
|------|---------|
| **perlcritic** | Code linting and style |
| **perltidy** | Code formatting |
| **Devel::Cover** | Code coverage |
| **Perl::Critic** | Policy enforcement |
| **Test::Perl::Critic** | Critic in tests |

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

## Key Libraries

| Library | Purpose |
|---------|---------|
| **Moose / Moo** | Modern object system |
| **Mojolicious** | Web framework |
| **DBI** | Database interface |
| **DBIx::Class** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | JSON parsing |
| **YAML::XS** | YAML parsing |
| **LWP::UserAgent** | HTTP client |
| **HTTP::Tiny** | Minimal HTTP client |
| **IO::Socket::SSL** | SSL/TLS |
| **Parallel::ForkManager** | Parallel processing |
| **MCE** | Many-core engine |
| **Try::Tiny** | Exception handling |
| **Path::Tiny** | File paths |
| **List::Util** | List utilities |
| **Scalar::Util** | Scalar utilities |
| **DateTime** | Date/time handling |
| **Log::Any** | Logging facade |
| **Config::Any** | Configuration |

---

## Text Processing

| Tool | Purpose |
|---------|---------|
| **Regular expressions** | Built-in, powerful |
| **Template::Toolkit** | Template engine |
| **Text::CSV** | CSV parsing |
| **XML::LibXML** | XML processing |
| **Mojo::DOM** | HTML/XML parsing |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **VS Code + Perl** | Perl language support |
| **vim-perl** | Vim Perl support |
| **Emacs + cperl-mode** | Classic Perl environment |
| **Komodo** | ActiveState Perl IDE |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Starman** | PSGI web server |
| **Hypnotoad** | Mojolicious server |
| **Docker** | Containerized |
| **PAR::Packer** | Standalone executables |
| **Carton** | Bundle dependencies |
| **cpanfile + Carton** | Reproducible deployments |

---

## Summary

Perl's ecosystem is vast and mature, with CPAN hosting 200,000+ modules. The standard stack is: **Perl 5.38+** as runtime, **cpanm** for packages, **Mojolicious** for web, **DBI** + **DBIx::Class** for databases, **Test2::Suite** for testing, **perlcritic** for linting, and **perltidy** for formatting. Perl excels at text processing, system administration, bioinformatics, and legacy web applications. Modern Perl (5.38+) with signatures, postfix dereference, and try/catch is significantly cleaner than its reputation suggests. The ecosystem is ideal for sysadmin scripting, data processing, and rapid prototyping.
