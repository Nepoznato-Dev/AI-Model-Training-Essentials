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
# Perl — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Perl.
---

## Versões Perl
| Versão | Notas |
|--------|-------|
| **Perl 5.38+** | Atual estável |
| **Perl 5.40** | Mais recente com novos recursos |
| **Raku (Perl 6)** | Redesenho moderno (linguagem separada) |
| **Alce** | Sistema OO moderno |
| **Moo** | Alce leve |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **CPAN** | Rede abrangente de arquivos Perl (mais de 200.000 módulos) |
| **cpanm** | Instalador CPAN leve |
| **cpanfile** | Declaração de dependência |
| **Caixa** | Bundler de dependência (como Bundler) |
| **Dist::Zilla** | Construtor de distribuição |
| **Aplicativo::cpanminus** | Cliente CPAN mínimo |
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

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Mojolicioso** | Pilha completa | Moderno, limpo, com baterias incluídas |
| **Dançarino2** | Micro | Tipo Sinatra, leve |
| **Catalisador** | Pilha completa | Empresa, MVC |
| **Placa** | Kit de ferramentas PSGI | Interface web de baixo nível |
| **Homem das Estrelas** | Servidor HTTP | Servidor PSGI |
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

## Banco de dados
| Tecnologia | Tipo |
|------------|------|
| **DBI** | Padrão de interface de banco de dados |
| **DBD::SQLite** | Driver SQLite |
| **DBD::Pg** | Driver PostgreSQL |
| **DBD::mysql** | Driver MySQL |
| **DBIx::Classe** | ORM completo |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Redes** | Cliente Redis |
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

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **Teste::Mais** | Estrutura de teste padrão |
| **Teste2::Suite** | Testes modernos (recomendado) |
| **Teste::Fatal** | Teste de exceção |
| **Teste::MockModule** | Zombando |
| **Teste::Profundo** | Comparação de dados complexos |
| **Teste::Saída** | Capturar STDOUT/STDERR |
| **provar** | Executor de testes |
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

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **perlcrítico** | Linting e estilo de código |
| **perl arrumado** | Formatação de código |
| **Desenvolvimento::Capa** | Cobertura de código |
| **Perl::Crítico** | Aplicação de políticas |
| **Teste::Perl::Critic** | Crítica em testes |
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

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **Alce / Moo** | Sistema de objetos moderno |
| **Mojolicioso** | Estrutura web |
| **DBI** | Interface de banco de dados |
| **DBIx::Classe** | ORM |
| **JSON::XS/Cpanel::JSON::XS** | Análise JSON |
| **YAML::XS** | Análise YAML |
| **LWP::UserAgent** | Cliente HTTP |
| **HTTP::Pequeno** | Cliente HTTP mínimo |
| **IO::Soquete::SSL** | SSL/TLS |
| **Paralelo::ForkManager** | Processamento paralelo |
| **MCE** | Motor de muitos núcleos |
| **Experimente::Tiny** | Tratamento de exceções |
| **Caminho::Tiny** | Caminhos de arquivo |
| **Lista::Util** | Listar utilitários |
| **Escalar::Util** | Utilitários escalares |
| **DataHora** | Tratamento de data/hora |
| **Registro::Qualquer** | Fachada de madeira |
| **Config::Qualquer** | Configuração |
---

## Processamento de texto
| Ferramenta | Finalidade |
|--------|---------|
| **Expressões regulares** | Integrado, poderoso |
| **Modelo::Kit de ferramentas** | Mecanismo de modelo |
| **Texto::CSV** | Análise de CSV |
| **XML::LibXML** | Processamento XML |
| **Mojo::DOM** | Análise HTML/XML |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Código VS + Perl** | Suporte à linguagem Perl |
| **vim-perl** | Suporte Vim Perl |
| **Emacs + modo cperl** | Ambiente Perl clássico |
| **Komodo** | IDE ActiveState Perl |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Homem das Estrelas** | Servidor web PSGI |
| ** Hipnotoad ** | Servidor Mojolicioso |
| **Docker** | Contentorizado |
| **PAR::Embalador** | Executáveis ​​independentes |
| **Caixa** | Dependências de pacote |
| **cpanfile + caixa** | Implantações reproduzíveis |
---

## Resumo
O ecossistema Perl é vasto e maduro, com CPAN hospedando mais de 200.000 módulos. A pilha padrão é: **Perl 5.38+** como tempo de execução, **cpanm** para pacotes, **Mojolicious** para web, **DBI** + **DBIx::Class** para bancos de dados, **Test2::Suite** para testes, **perlcritic** para linting e **perltidy** para formatação. Perl é excelente em processamento de texto, administração de sistemas, bioinformática e aplicações web legadas. Perl moderno (5.38+) com assinaturas, desreferência de postfix e try/catch é significativamente mais limpo do que sua reputação sugere. O ecossistema é ideal para scripts de administração de sistemas, processamento de dados e prototipagem rápida.