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
# パール
Perl は、実用的なテキスト処理ツールとして 1987 年にラリー ウォールによって作成されました。これは、初期の Web 開発 (CGI スクリプト)、システム管理、バイオインフォマティクス、ネットワーク プログラミングのバックボーンとなりました。 Perl の哲学は「There's More Than One Way To Do It」(TMTOWTDI) です。この言語はあらゆる問題に対して複数のアプローチを提供し、統一性よりも表現力を優先します。
Perl が現代のプログラミングに与えた影響は多大ですが、目に見えないことも多くあります。Perl のパターン マッチングの影響を受けた正規表現は、現在、Python、JavaScript、Java、およびその他のほとんどの言語で標準となっています。 CPAN (Comprehensive Perl Archive Network) は最初のソフトウェア パッケージ リポジトリの 1 つで、Python の PyPI や Node の npm などの後のシステムに影響を与えました。
Perl の人気は 2000 年代初頭のピークに比べて低下していますが、レガシー システム、テキスト処理パイプライン、およびシステム管理では依然として広く使用されています。 Perl 6 (現在は **Raku** と呼ばれています) は、Perl の概念の多くを再考した別の言語です。
---

## Perl が重要な理由
- **テキスト処理**: Perl の正規表現は、主流の言語の中で最も強力です。
- **CPAN**: 200,000 を超えるモジュール - 最大かつ最も古いパッケージ リポジトリの 1 つ。
- **ワンライナー**: Perl は、コマンドラインのテキスト変換を迅速に行うことに優れています。
- **Glue 言語**: システムの接続、ログの解析、データ ファイルの処理、タスクの自動化を行います。
- **運用環境で実証済み**: PHP が存在する前から Web に力を与えてきました。重要なインフラストラクチャは依然として稼働しています。
- **Raku (Perl 6)**: 文法、ジャンクション、および複数のディスパッチを備えた最新の再設計。
## トレードオフ
|制限 |詳細 |一般的な回避策 |
|----------|-----------|--------|
| **可読性** | 「Perl は書き込み専用言語です」 - 緻密で不可解な構文 |厳密/警告を使用します。モジュール式コードを作成します。最新の Perl (5.36 以降) を使用する |
| **衰退するコミュニティ** | Perl を選択する新規プロジェクトの減少 |大規模な既存のコードベースにはメンテナンスが必要です。アクティブなコミュニティ |
| **2 つのメジャー バージョン** | Perl 5 とraku (Perl 6) は異なる言語です |既存の作業には Perl 5 を使用してください。新規プロジェクトの楽 |
| **トレンドではありません** |ブートキャンプや大学で教えられることはほとんどありません。広範なドキュメントと CPAN モジュール |
| **可変シジル** | `$`、`@`、`%`プレフィックスは初心者を混乱させる可能性があります。パターンを学習します:`$scalar`、`@array`、`%hash`|
| **パフォーマンス** |計算量の多いタスクではコンパイル言語よりも遅い | C 拡張機能を使用します。 HPC には適切なツールではありません |
---

## 構文の基礎
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

## Perl が他の言語に与えた影響
|特集 |それを採用した言語 |
|----------|--------------------------|
|正規表現 | Python、JavaScript、Java、Ruby、C#、PHP |
|パッケージリポジトリ (CPAN) | PyPI、npm、RubyGems、crates.io |
|ヒアドキュメント | Python、Ruby、PHP、シェル、JavaScript |
| `$_`デフォルト変数 | Ruby の`$_`、PowerShell の`$_`|
| `map`/`grep`/`reduce`| Python、Ruby、JavaScript、Rust |
| `use strict`/ 糸くず | TypeScript、Python の型ヒント |
---

## 高度な構文とパターン
### 参照と複雑なデータ構造
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

### クロージャと高階関数
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

### 高度な正規表現
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

### オブジェクト指向 Perl (Moose / Moo)
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

## 同時実行性と並列処理
### Parallel::ForkManager によるフォーク
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

### Coro — 協調的なコルーチン
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

### IO::Async — イベント駆動型プログラミング
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

## プロジェクトの構成とシステムの構築
### プロジェクトの構造
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

### cpanfile — 依存関係の管理
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

### 依存関係コマンド
```bash
cpanm --installdeps .       # Install from cpanfile
cpanm Mojolicious           # Install specific module
cpanm --notest Mojolicious  # Skip tests for speed
carton install              # Bundler-like dependency pinning
carton exec -- perl app.pl  # Run with pinned deps
```

### CI/CD パイプライン (GitHub アクション)
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

## テスト
### テスト::詳細
```perl
use Test::More;
ok(1, 'basic test');
is(2+2, 4, 'math works');
done_testing();
```

### テストコマンド
```bash
prove -lrv t/
prove -l t/user_service.t
```

---

## 相互運用性
### FFI::カモノハシ
```perl
use FFI::Platypus;
my $ffi = FFI::Platypus->new(api => 2);
$ffi->lib(undef);  # libc
$ffi->attach(sqrt => ['double'] => 'double');
say sqrt(144.0);  # 12.0
```

### XS - C の統合
```perl
# XS allows Perl to call C functions directly
# Build with: perl Makefile.PL && make && make install
use MyModule;
say MyModule::fast_factorial(10);  # 3628800
```

---

## デザインパターン
### シングルトン
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

### 責任の連鎖
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

## パフォーマンスと最適化
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

## デプロイメント
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

## Perl を使用する場合
|シナリオ |なぜ Perl |より良い代替案 |
|----------|----------|----------|
|テキスト処理/解析 |クラス最高の正規表現エンジン |構造化データのための Python |
|ログファイルの分析 |高速ワンライナー、実績のあるツール |  単純な場合は`awk`/ `sed`。複雑なPython |
|システム管理 |歴史的に支配的な |単純なタスクには Bash/PowerShell。複雑なPython |
|レガシー システムのメンテナンス |実稼働中の数百万行の Perl | — |
|バイオインフォマティクス |歴史的に強い存在感 (BioPerl) | Python (バイオパイソン)、R |
|素早いデータ変換 |ワンライナーは無敵です |  構造化フォーマットの場合は`jq`、`awk`|
|ウェブ開発 | CGI の時代は終わった | Python、Node.js、Go、PHP |
|新規大型プロジェクト |コミュニティは前進しました | Go、Rust、Python |
|データ サイエンス / ML |エコシステムではありません |パイソン、R |
---

## 総合的な Q&A
### Q1:`my`、`our`、および`local`の違いは何ですか?
**A:** これらのキーワードは変数のスコープを制御します。
```perl
# my — lexical scope (preferred)
my $x = 10;  # visible only in current block

# our — package global with lexical alias
our $VERSION = '1.0';  # package variable, accessible as $main::VERSION

# local — temporarily change a global
local $/ = undef;  # temporarily undefine input record separator
# original value restored when block exits
```

### Q2: Perl でテキスト ファイルを効率的に処理するにはどうすればよいですか?
**A:** Perl はテキスト処理に優れています。ダイヤモンド演算子と正規表現を使用します。
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

### Q3: 参照と複雑なデータ構造を使用するにはどうすればよいですか?
**A:** 参照は、Perl が入れ子構造を作成する方法です。
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

### Q4: 知っておくべき Perl の特殊変数は何ですか?
**A:** Perl には多くの特殊変数があります。最も重要なこと:
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

### Q5: 最新の保守可能な Perl を作成するにはどうすればよいですか?
**A:** 最新の Perl のベスト プラクティス:
- 常に`strict`および`warnings`を使用してください 
- すべての変数に`my`を使用します
- 字句ファイルハンドルを使用します:`open my $fh, '<', $file`
- CPAN のモジュールを使用します (OOP には Moo/Moose、エラーには Try::Tiny)
-`print`の代わりに`say`を使用します (`feature 'say'`を使用)
- `perltidy`でフォーマットする
---

## 思考連鎖による問題解決
### 問題 1: ログ ファイルの分析
**ステップ 1: 問題を理解する**
Apache アクセス ログを解析し、IP アドレスごとにリクエストをカウントします。
**ステップ 2: アプローチを特定する**
正規表現を使用して IP アドレスを抽出し、ハッシュを使用して出現回数をカウントします。
**ステップ 3: 実装**```perl
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

**ステップ 4: 延長**
日付フィルタリング、ステータスコード解析を追加し、CSVとして出力します。
### 問題 2: Regex を使用したバッチ ファイルの名前変更
**ステップ 1: 問題を理解する**
正規表現を使用してファイル名を変換し、パターンに一致するファイルの名前を変更します。
**ステップ 2: アプローチを特定する**
ファイルを検索するには`glob`または`opendir`を使用し、名前を変換するには正規表現を使用します。
**ステップ 3: 実装**```perl
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

**ステップ 4: 確認**
最初に`--dry-run`フラグを指定して実行します (印刷するだけで、移動しないでください)。
### 問題 3: 単純な Web スクレイパーの構築
**ステップ 1: 問題を理解する**
Web ページを取得し、すべてのリンクを抽出します。
**ステップ 2: アプローチを特定する**
取得と正規表現には`LWP::Simple`を使用し、解析には`HTML::LinkExtor`を使用します。
**ステップ 3: 実装**```perl
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

**ステップ 4: 延長**
相対 URL を処理し、ドメインでフィルターし、ページネーションに従います。
---

＃＃ まとめ
Perl の黄金時代は過ぎましたが、その影響はどこにでもあります。正規表現を使用するすべての言語、CPAN をモデルとしたすべてのパッケージ マネージャー、および`map`/`grep`/`reduce`を使用するすべてのシステムには Perl の DNA が受け継がれています。新しいプロジェクトの場合、ほとんどの開発者は Python または Go に手を伸ばします。しかし、Perl は依然として、テキスト処理、迅速な自動化、および世界中の重要なインフラストラクチャを実行する膨大な量の Perl コードの保守のための強力なツールです。 Perl を理解するということは、現代のプログラミングがどこから来たのかを理解することも意味します。Perl は、今日私たちが使用するツールやパターンを形作ったのです。