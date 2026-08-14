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
# Perl — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz Perl ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Perl Sürümleri
| Sürüm | Notlar |
|-----------|----------|
| **Perl 5.38+** | Mevcut durum stabil |
| **Perl 5.40** | Yeni özelliklerle en son |
| **Raku (Perl 6)** | Modern yeniden tasarım (ayrı dil) |
| **Geyik** | Modern OO sistemi |
| **Möö** | Hafif Geyik |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **CPAN** | Kapsamlı Perl Arşiv Ağı (200.000+ modül) |
| **cpanm** | Hafif CPAN yükleyicisi |
| **cpan dosyası** | Bağımlılık beyanı |
| **Karton** | Bağımlılık paketleyicisi (Bundler gibi) |
| **Dist::Zilla** | Dağıtım oluşturucu |
| **Uygulama::cpanminus** | Minimum CPAN istemcisi |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Neşeli** | Tam yığın | Modern, temiz, piller dahil |
| **Dansçı2** | Mikro | Sinatra benzeri, hafif |
| **Katalizör** | Tam yığın | Kurumsal, MVC |
| **Plak** | PSGI araç seti | Düşük seviyeli web arayüzü |
| **Yıldız Adam** | HTTP sunucusu | PSGI sunucusu |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **DBI** | Veritabanı arayüzü standardı |
| **DBD::SQLite** | SQLite sürücüsü |
| **DBD::Pg** | PostgreSQL sürücüsü |
| **DBD::mysql** | MySQL sürücüsü |
| **DBIx::Sınıf** | Tam ORM |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Redis** | Redis istemcisi |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **Test::Daha Fazla** | Standart test çerçevesi |
| **Test2::Süit** | Modern testler (önerilir) |
| **Test::Ölümcül** | İstisna testi |
| **Test::MockModule** | Alaycı |
| **Test::Derin** | Karmaşık veri karşılaştırması |
| **Test::Çıktı** | STDOUT/STDERR'yi Yakala |
| **kanıtla** | Test çalıştırıcısı |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **perlkritik** | Kod astarı ve stili |
| **perltidy** | Kod biçimlendirme |
| **Geliştir::Kapak** | Kod kapsamı |
| **Perl::Eleştirmen** | Politika uygulaması |
| **Test::Perl::Eleştirmen** | Testlerde Eleştirmen |
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

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **Geyik / Möö** | Modern nesne sistemi |
| **Neşeli** | Web çerçevesi |
| **DBI** | Veritabanı arayüzü |
| **DBIx::Sınıf** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | JSON ayrıştırma |
| **YAML::XS** | YAML ayrıştırma |
| **LWP::UserAgent** | HTTP istemcisi |
| **HTTP::Küçük** | Minimal HTTP istemcisi |
| **IO::Socket::SSL** | SSL/TLS |
| **Paralel::ForkManager** | Paralel işleme |
| **MCE** | Çok çekirdekli motor |
| **Deneyin::Tiny** | İstisna yönetimi |
| **Yol::Küçük** | Dosya yolları |
| **Liste::Kullanım** | Yardımcı programları listele |
| **Skaler::Util** | Skaler yardımcı programlar |
| **TarihSaat** | Tarih/saat kullanımı |
| **Günlük::Herhangi biri** | Tomruk cephesi |
| **Yapılandırma::Herhangi biri** | Yapılandırma |
---

## Metin İşleme
| Araç | Amaç |
|-----------|-----------|
| **Normal ifadeler** | Yerleşik, güçlü |
| **Şablon::Araç seti** | Şablon motoru |
| **Metin::CSV** | CSV ayrıştırma |
| **XML::LibXML** | XML işleme |
| **Mojo::DOM** | HTML/XML ayrıştırma |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + Perl** | Perl dil desteği |
| **vim-perl** | Vim Perl desteği |
| **Emacs + cperl modu** | Klasik Perl ortamı |
| **Komodo** | ActiveState Perl IDE |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Yıldız Adam** | PSGI web sunucusu |
| **Hipnotoad** | Mojolicious sunucusu |
| **Docker** | Konteynerde |
| **PAR::Paketleyici** | Bağımsız yürütülebilir dosyalar |
| **Karton** | Paket bağımlılıkları |
| **cpanfile + Karton** | Tekrarlanabilir dağıtımlar |
---

## Özet
Perl'ün ekosistemi geniş ve olgundur; CPAN 200.000'den fazla modüle ev sahipliği yapar. Standart yığın şudur: Çalışma zamanı olarak **Perl 5.38+**, paketler için **cpanm**, web için **Mojolicious**, veritabanları için **DBI** + **DBIx::Class**, test için **Test2::Suite**, linting için **perlcritic** ve biçimlendirme için **perltidy**. Perl, metin işleme, sistem yönetimi, biyoinformatik ve eski web uygulamalarında uzmandır. İmzalar, sonek referansı ve try/catch özellikleriyle modern Perl (5.38+), itibarının gösterdiğinden çok daha temizdir. Ekosistem, sistem yöneticisi komut dosyası oluşturma, veri işleme ve hızlı prototip oluşturma için idealdir.