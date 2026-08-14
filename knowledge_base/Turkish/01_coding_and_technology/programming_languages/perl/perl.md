<!--
---
# Metadata
title: "Perl"
description: "Comprehensive reference for the Perl programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [perl, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "24 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
#Perl
Perl, 1987 yılında Larry Wall tarafından pratik bir metin işleme aracı olarak yaratıldı. İlk web geliştirmenin (CGI komut dosyaları), sistem yönetiminin, biyoenformatik ve ağ programlamanın omurgası haline geldi. Perl'ün felsefesi "Bunu Yapmanın Birden Fazla Yolu Vardır" (TMTOWTDI)'dır - dil size her soruna birden fazla yaklaşım sunar ve tekdüzelik yerine ifadeyi tercih eder.
Perl'ün modern programlama üzerindeki etkisi muazzamdır ancak çoğu zaman görünmez: Perl'ün kalıp eşleştirmesinden etkilenen düzenli ifadeler artık Python, JavaScript, Java ve diğer birçok dilde standarttır. CPAN (Kapsamlı Perl Arşiv Ağı) ilk yazılım paketi depolarından biriydi ve Python'un PyPI ve Node'un npm'si gibi daha sonraki sistemlere ilham kaynağı oldu.
Perl'ün popülaritesi 2000'li yılların başındaki zirveden bu yana azalmış olsa da eski sistemlerde, metin işleme hatlarında ve sistem yönetiminde yaygın olarak kullanılmaya devam ediyor. Perl 6 (şimdi **Raku** olarak adlandırılıyor), Perl'ün birçok konseptini yeniden tasarlayan ayrı bir dildir.
---

## Perl Neden Önemlidir
- **Metin işleme**: Perl'ün düzenli ifadeleri ana diller arasında en güçlü olanıdır.
- **CPAN**: 200.000'den fazla modül — en büyük ve en eski paket depolarından biri.
- **Tek satırlar**: Perl hızlı komut satırı metin dönüştürmelerinde üstündür.
- **Tutkal dili**: Sistemleri bağlar, günlükleri ayrıştırır, veri dosyalarını işler, görevleri otomatikleştirir.
- **Üretimde kanıtlanmıştır**: PHP'nin ortaya çıkışından bu yana web'e güç vermektedir. Kritik altyapıyı hâlâ çalıştırıyoruz.
- **Raku (Perl 6)**: Dilbilgisi, kavşaklar ve çoklu gönderimle modern bir yeniden tasarım.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **Okunabilirlik** | "Perl salt okunur bir dildir" — yoğun, şifreli sözdizimi | Kesin ifadeler/uyarılar kullanın; modüler kod yazın; modern Perl'i kullanın (5.36+) |
| **Topluluğun azalması** | Perl'ü seçen daha az yeni proje | Mevcut büyük kod tabanının bakıma ihtiyacı var; aktif topluluk |
| **İki ana versiyon** | Perl 5 ve Raku (Perl 6) farklı dillerdir | Mevcut işler için Perl 5'i kullanın; Yeni projeler için Raku |
| **Modaya uygun değil** | Eğitim kamplarında veya üniversitelerde nadiren öğretilir | Kapsamlı belgeler ve CPAN modülleri |
| **Değişken işaretler** | `$`,`@`,`%`önekleri yeni başlayanların kafasını karıştırabilir | Modeli öğrenin:`$scalar`,`@array`,`%hash`|
| **Performans** | Yoğun işlem gerektiren görevler için derlenmiş dillerden daha yavaş | C uzantılarını kullanın; HPC için doğru araç değil |
---

## Söz Diziminin Temelleri
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

## Perl'ün Diğer Diller Üzerindeki Etkisi
| Özellik | Languages That Adopted It |
|---------|--------------------------|
| Düzenli ifadeler | Python, JavaScript, Java, Ruby, C#, PHP |
| Package repositories (CPAN) | PyPI, npm, RubyGems, crates.io |
| Heredocs | Python, Ruby, PHP, Shell, JavaScript |
| `$_` default variable | Ruby'nin `$_`'si, PowerShell'in `$_`'si |
| `map`/`grep`/`reduce` | Python, Ruby, JavaScript, Rust |
| `use strict` / linting | TypeScript, Python's type hints |
---

## Gelişmiş Sözdizimi ve Desenler
### Referanslar ve Karmaşık Veri Yapıları
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

### Kapanışlar ve Üst Düzey İşlevler
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

### Gelişmiş Normal İfadeler
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

### Nesneye Yönelik Perl (Geyik / Moo)
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

## Eşzamanlılık ve Paralellik
### Paralel::ForkManager ile çatallama
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

### Coro — İşbirlikçi Günlükler
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

### IO::Async — Olay Odaklı Programlama
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Proje Yapısı
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

### cpanfile — Bağımlılık Yönetimi
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

### Bağımlılık Komutları
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### CI/CD İşlem Hattı (GitHub Eylemleri)
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

## Test etme
### Test::Daha Fazla
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### Test Komutları
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## Birlikte Çalışabilirlik
### FFI::Ornitorenk
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS — C Entegrasyonu
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## Tasarım Desenleri
### Tekil
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

### Sorumluluk Zinciri
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

## Performans ve Optimizasyon
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

## Dağıtım
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

## Perl Ne Zaman Kullanılmalı
| Senaryo | Neden Perl | Daha İyi Alternatif |
|----------|------------|-----------|
| Metin işleme / ayrıştırma | Sınıfının en iyisi normal ifade motoru | Yapılandırılmış veriler için Python |
| Günlük dosyası analizi | Hızlı tek gömlekler, kanıtlanmış araçlar |  Basit durumlar için`awk`/ `sed`; Karmaşık için Python |
| Sistem yönetimi | Tarihsel olarak baskın | Basit görevler için Bash/PowerShell; Karmaşık için Python |
| Eski sistem bakımı | Milyonlarca satırlık Perl üretimde | — |
| Biyoenformatik | Güçlü tarihsel varlık (BioPerl) | Python (Biopython), R |
| Hızlı veri dönüşümleri | Tek gömlekler rakipsizdir |  Yapılandırılmış formatlar için `jq`,`awk`|
| Web geliştirme | CGI dönemi bitti | Python, Node.js, Git, PHP |
| Yeni büyük ölçekli projeler | Topluluk yoluna devam etti | Git, Pas, Python |
| Veri bilimi / ML | Ekosistem değil | Python, R |
---

## Sentetik Soru-Cevap
### S1: `my`,`our`ve`local`arasındaki fark nedir?
**C:** Bu anahtar kelimeler değişken kapsamını kontrol eder:
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### S2: Perl'de metin dosyalarını verimli bir şekilde nasıl işlerim?
**C:** Perl metin işlemede üstündür. Elmas operatörünü ve normal ifadeyi kullanın:
```perl
# Line-by-line processing
while (my $line = <STDIN>) {
    chomp $line;
    $line =~ s/old/new/g;
    print "$line\n";
}

# One-liner (the classic Perl superpower)
# perl -pe 's/foo/bar/g' file.txt
# perl -ne 'print if /error/i' logfile.txt
# perl -lane 'print $F[0]' file.txt  # split on whitespace

# Slurp entire file
local $/;
my $content = <FILE>;
```

### S3: Referansları ve karmaşık veri yapılarını nasıl kullanırım?
**C:** Referanslar Perl'ün iç içe yapılar yaratma yöntemidir:
```perl
# Array reference
my $aref = [1, 2, 3];
print $aref->[0];  # 1

# Hash reference
my $href = { name => 'Alice', age => 30 };
print $href->{name};  # Alice

# Nested structures
my $data = {
    users => [
        { name => 'Alice', scores => [95, 87, 92] },
        { name => 'Bob',   scores => [78, 88, 91] },
    ],
};
print $data->{users}[0]{scores}[2];  # 92
```

### S4: Perl'ün bilmem gereken özel değişkenleri nelerdir?
**C:** Perl'de birçok özel değişken vardır. En önemlisi:
```perl
$_     # default variable (topic)
$!     # system error message
$@     # eval error
$$     # process ID
$.     # current line number in last filehandle
$/     # input record separator (\n by default)
$\     # output record separator
$|     # autoflush (1 = on)
@ARGV  # command-line arguments
%ENV   # environment variables
```

### S5: Modern, bakımı kolay Perl'ü nasıl yazarım?
**C:** Modern Perl için en iyi uygulamalar:
- Her zaman`strict`ve`warnings`kullanın 
- Tüm değişkenler için`my`kullanın
- Sözcüksel dosya tanıtıcıları kullanın:`open my $fh, '<', $file`
- CPAN'daki modülleri kullanın (OOP için Moo/Moose, hatalar için deneyin::Tiny)
-`print`yerine`say`kullanın (`feature 'say'` ile)
-`perltidy`ile biçimlendirin
---

## Düşünce Zinciri Problem Çözme
### Sorun 1: Günlük Dosyası Analizi
**1. Adım: Sorunu Anlayın**
Apache erişim günlüğünü ayrıştırın ve IP adresi başına istekleri sayın.
**2. Adım: Yaklaşımı Belirleyin**
IP adreslerini çıkarmak için regex'i, oluşumları saymak için karma'yı kullanın.
**3. Adım: Uygulama**```perl
use strict;
use warnings;

my %counts;
while (my $line = <>) {
    if ($line =~ /^(\S+)/) {
        $counts{$1}++;
    }
}

# Sort by count (descending)
for my $ip (sort { $counts{$b} <=> $counts{$a} } keys %counts) {
    printf "%-15s %d\n", $ip, $counts{$ip};
}
```

**4. Adım: Genişletin**
Tarih filtreleme, durum kodu analizi ve çıktıyı CSV olarak ekleyin.
### Sorun 2: Toplu Dosyayı Regex ile Yeniden Adlandırma
**1. Adım: Sorunu Anlayın**
Bir kalıpla eşleşen dosyaları yeniden adlandırın, dosya adlarını regex ile dönüştürün.
**2. Adım: Yaklaşımı Belirleyin**
Dosyaları bulmak için`glob`veya `opendir`'yi, adları dönüştürmek için normal ifadeyi kullanın.
**3. Adım: Uygulama**```perl
use strict;
use warnings;
use File::Copy;

my $dir = shift @ARGV || '.';
opendir my $dh, $dir or die "Cannot open $dir: $!";

for my $file (sort readdir $dh) {
    next unless $file =~ /^(\d{4})-(\d{2})-(\d{2})_(.+)$/;
    my $new_name = "$3-$2-$1_$4";  # Rearrange date format
    my $old = "$dir/$file";
    my $new = "$dir/$new_name";
    print "Renaming: $file -> $new_name\n";
    move($old, $new) or warn "Failed: $!";
}
closedir $dh;
```

**4. Adım: Doğrulayın**
Önce`--dry-run`bayrağıyla çalıştırın (yalnızca yazdırın, hareket etmeyin).
### Sorun 3: Basit bir Web Kazıyıcı Oluşturma
**1. Adım: Sorunu Anlayın**
Bir web sayfasını getirin ve tüm bağlantıları çıkarın.
**2. Adım: Yaklaşımı Belirleyin**
Getirme ve regex için`LWP::Simple`veya ayrıştırma için`HTML::LinkExtor`kullanın.
**3. Adım: Uygulama**```perl
use strict;
use warnings;
use LWP::Simple;
use HTML::LinkExtor;

my $url = 'https://example.com';
my $html = get($url) or die "Cannot fetch $url";

my $parser = HTML::LinkExtor->new;
$parser->parse($html);

for my $link ($parser->links) {
    my ($tag, %attrs) = @$link;
    print "$attrs{href}\n" if $attrs{href};
}
```

**4. Adım: Genişletin**
Göreli URL'leri yönetin, etki alanına göre filtreleyin ve sayfalandırmayı takip edin.
---

## Özet
Perl'ün altın çağı geçti ama etkisi her yerde. Düzenli ifadelere sahip her dil, CPAN üzerinde modellenen her paket yöneticisi ve`map`/`grep`/`reduce`içeren her sistem Perl'ün DNA'sını taşır. Yeni projeler için çoğu geliştirici Python veya Go'ya yöneliyor. Ancak Perl, metin işleme, hızlı otomasyon ve dünya çapında kritik altyapıyı çalıştıran büyük miktardaki Perl kodunun bakımı için güçlü bir araç olmaya devam ediyor. Perl'ü anlamak aynı zamanda modern programlamanın nereden geldiğini anlamak anlamına da gelir; bugün kullandığımız araçları ve kalıpları o şekillendirdi.