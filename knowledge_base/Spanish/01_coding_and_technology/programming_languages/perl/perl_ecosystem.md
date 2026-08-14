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
# Perl: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, marcos e infraestructura esenciales en el ecosistema Perl.
---

## Versiones de Perl
| Versión | Notas |
|---------|-------|
| **Perl 5.38+** | Estable actual |
| **Perla 5.40** | Lo último con nuevas funciones |
| **Raku (Perl 6)** | Rediseño moderno (idioma separado) |
| **Alce** | Sistema OO moderno |
| **Muuu** | Alce ligero |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **CPAN** | Red integral de archivos Perl (más de 200.000 módulos) |
| **cpanm** | Instalador CPAN ligero |
| **archivocpan** | Declaración de dependencia |
| **Cartón** | Paquete de dependencia (como Bundler) |
| **Distrito::Zilla** | Constructor de distribución |
| **Aplicación::cpanminus** | Cliente CPAN mínimo |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Mojolicious** | Pila completa | Moderno, limpio, con pilas incluidas |
| **Bailarina2** | micro | Estilo Sinatra, ligero |
| **Catalizador** | Pila completa | Empresa, MVC |
| **Placar** | Kit de herramientas del PSGI | Interfaz web de bajo nivel |
| **Hombre estrella** | Servidor HTTP | Servidor PSGI |
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

## Base de datos
| Tecnología | Tipo |
|------------|------|
| **DBI** | Estándar de interfaz de base de datos |
| **DBD::SQLite** | Controlador SQLite |
| **DBD::Pág** | Controlador PostgreSQL |
| **DBD::mysql** | Controlador MySQL |
| **DBIx::Clase** | ORM completo |
| **Mojo::Pág** | PostgreSQL (Mojolicioso) |
| **Redis** | Cliente Redis |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **Prueba::Más** | Marco de prueba estándar |
| **Prueba2::Suite** | Pruebas modernas (recomendadas) |
| **Prueba::Fatal** | Pruebas de excepción |
| **Prueba::MockModule** | Burlarse |
| **Prueba::Profunda** | Comparación de datos complejos |
| **Prueba::Salida** | Captura STDOUT/STDERR |
| **probar** | Corredor de prueba |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **perlcrítico** | Linting y estilo de código |
| **perlita** | Formato de código |
| **Desarrolla::Portada** | Cobertura de código |
| **Perl::Crítico** | Aplicación de políticas |
| **Prueba::Perl::Crítica** | Crítico en pruebas |
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

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **Alce / Moo** | Sistema de objetos moderno |
| **Mojolicious** | Marco web |
| **DBI** | Interfaz de base de datos |
| **DBIx::Clase** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | Análisis JSON |
| **YAML::XS** | Análisis YAML |
| **LWP::Agente de usuario** | Cliente HTTP |
| **HTTP::Pequeño** | Cliente HTTP mínimo |
| **IO::Socket::SSL** | SSL/TLS |
| **Paralelo::ForkManager** | Procesamiento paralelo |
| **MCE** | Motor de muchos núcleos |
| **Prueba::Pequeño** | Manejo de excepciones |
| **Ruta::Pequeña** | Rutas de archivos |
| **Lista::Util** | Listar utilidades |
| **Escalar::Util** | Utilidades escalares |
| **FechaHora** | Manejo de fecha/hora |
| **Registro::Cualquiera** | Fachada de registro |
| **Configuración::Cualquiera** | Configuración |
---

## Procesamiento de texto
| Herramienta | Propósito |
|---------|---------|
| **Expresiones regulares** | Incorporado, potente |
| **Plantilla::Kit de herramientas** | Motor de plantillas |
| **Texto::CSV** | Análisis CSV |
| **XML::LibXML** | Procesamiento XML |
| **Mojo::DOM** | Análisis HTML/XML |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + Perl** | Soporte de lenguaje Perl |
| **vim-perl** | Soporte para Vim Perl |
| **Emacs + modo cperl** | Entorno Perl clásico |
| **Komodo** | IDE de ActiveState Perl |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Hombre estrella** | Servidor web PSGI |
| **Hipnotsapo** | Servidor Mojolicious |
| **Acoplador** | En contenedores |
| **PAR::Empaquetador** | Ejecutables independientes |
| **Cartón** | Dependencias del paquete |
| **cpanfile + Caja** | Implementaciones reproducibles |
---

## Resumen
El ecosistema de Perl es vasto y maduro, y CPAN alberga más de 200.000 módulos. La pila estándar es: **Perl 5.38+** como tiempo de ejecución, **cpanm** para paquetes, **Mojolicious** para web, **DBI** + **DBIx::Class** para bases de datos, **Test2::Suite** para pruebas, **perlcritic** para linting y **perltidy** para formatear. Perl destaca en procesamiento de textos, administración de sistemas, bioinformática y aplicaciones web heredadas. El Perl moderno (5.38+) con firmas, desreferencia de postfijo y try/catch es significativamente más limpio de lo que sugiere su reputación. El ecosistema es ideal para scripts de administradores de sistemas, procesamiento de datos y creación rápida de prototipos.