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
# Perl — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Perl.
---

## Versi Perl
| Versi | Catatan |
|---------|-------|
| **Perl 5.38+** | Stabil saat ini |
| **Perl 5.40** | Terbaru dengan fitur baru |
| **Raku (Perl 6)** | Desain ulang modern (bahasa terpisah) |
| **rusa besar** | Sistem OO modern |
| **Moo** | Rusa Ringan |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **CPAN** | Jaringan Arsip Perl Komprehensif (200.000+ modul) |
| **cpanm** | Pemasang CPAN ringan |
| **cpanfile** | Deklarasi ketergantungan |
| **Karton** | Bundler ketergantungan (seperti Bundler) |
| **Dist::Zilla** | Pembangun distribusi |
| **Aplikasi::cpanminus** | Klien CPAN minimal |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Sangat gembira** | Tumpukan penuh | Modern, bersih, termasuk baterai |
| **Penari2** | Mikro | Seperti Sinatra, ringan |
| **Katalis** | Tumpukan penuh | Perusahaan, MVC |
| **Plak** | Perangkat PSGI | Antarmuka web tingkat rendah |
| **Starman** | Server HTTP | server PSGI |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **DBI** | Standar antarmuka basis data |
| **DBD::SQLite** | Pengandar SQLite |
| **DBD::Hal** | Pengandar PostgreSQL |
| **DBD::mysql** | Pengandar MySQL |
| **DBIx::Kelas** | ORM penuh |
| **Mojo::Hal** | PostgreSQL (Mojolicious) |
| **Redis** | Klien Redis |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Tes::Selengkapnya** | Kerangka uji standar |
| **Tes2::Suite** | Pengujian modern (disarankan) |
| **Tes::Fatal** | Pengujian pengecualian |
| **Tes::MockModule** | Mengejek |
| **Tes::Dalam** | Perbandingan data yang kompleks |
| **Uji::Keluaran** | Tangkap STDOUT/STDERR |
| **buktikan** | Pelari ujian |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **perlkritik** | Linting kode dan gaya |
| **perltidy** | Pemformatan kode |
| **Pengembangan::Sampul** | Cakupan kode |
| **Perl::Kritik** | Penegakan kebijakan |
| **Tes::Perl::Kritik** | Kritikus dalam tes |
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

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Moose / Moo** | Sistem objek modern |
| **Sangat gembira** | Kerangka web |
| **DBI** | Antarmuka basis data |
| **DBIx::Kelas** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | Penguraian JSON |
| **YAML::XS** | Penguraian YAML |
| **LWP::Agen Pengguna** | Klien HTTP |
| **HTTP::Kecil** | Klien HTTP minimal |
| **IO::Soket::SSL** | SSL/TLS |
| **Paralel::ForkManager** | Pemrosesan paralel |
| **MCE** | Mesin banyak inti |
| **Coba::Mungil** | Penanganan pengecualian |
| **Jalur::Mungil** | Jalur file |
| **Daftar::Util** | Daftar utilitas |
| **Skalar::Util** | Utilitas skalar |
| **TanggalWaktu** | Penanganan tanggal/waktu |
| **Log::Apa saja** | Penebangan fasad |
| **Konfigurasi::Apa saja** | Konfigurasi |
---

## Pemrosesan Teks
| Alat | Tujuan |
|---------|---------|
| **Ekspresi reguler** | Bawaan, kuat |
| **Templat::Perangkat** | Mesin templat |
| **Teks::CSV** | Penguraian CSV |
| **XML::LibXML** | Pemrosesan XML |
| **Mojo::DOM** | Penguraian HTML/XML |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + Perl** | Dukungan bahasa Perl |
| **vim-perl** | Dukungan Vim Perl |
| **Emacs + mode cperl** | Lingkungan Perl klasik |
| **Komodo** | IDE Perl Status Aktif |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Starman** | Server web PSGI |
| **Hipnotoad** | Server yang menyenangkan |
| **Buruh pelabuhan** | dalam kontainer |
| **PAR::Pembungkus** | Eksekusi mandiri |
| **Karton** | Ketergantungan bundel |
| **cpanfile + Karton** | Penerapan yang dapat direproduksi |
---

## Ringkasan
Ekosistem Perl sangat luas dan matang, dengan CPAN yang menampung lebih dari 200.000 modul. Tumpukan standarnya adalah: **Perl 5.38+** sebagai runtime, **cpanm** untuk paket, **Mojolicious** untuk web, **DBI** + **DBIx::Class** untuk database, **Test2::Suite** untuk pengujian, **perlcritic** untuk linting, dan **perltidy** untuk pemformatan. Perl unggul dalam pemrosesan teks, administrasi sistem, bioinformatika, dan aplikasi web lama. Perl modern (5.38+) dengan tanda tangan, dereferensi postfix, dan coba/tangkap jauh lebih bersih daripada reputasinya. Ekosistem ini ideal untuk pembuatan skrip sysadmin, pemrosesan data, dan pembuatan prototipe cepat.