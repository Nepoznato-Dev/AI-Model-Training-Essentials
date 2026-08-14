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
# Perl — エコシステムとツールのガイド
このガイドでは、Perl エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## Perl のバージョン
|バージョン |メモ |
|----------|----------|
| **Perl 5.38+** |現在安定 |
| **Perl 5.40** |新機能を備えた最新の |
| **楽 (Perl 6)** |モダンな再デザイン (別の言語) |
| **ヘラジカ** |最新の OO システム |
| **ムー** |軽量ムース |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## パッケージ管理
|ツール |目的 |
|-----|----------|
| **CPAN** |包括的な Perl アーカイブ ネットワーク (200,000+ モジュール) |
| **cpanm** |軽量の CPAN インストーラー |
| **cpanfile** |依存関係の宣言 |
| **カートン** |依存関係バンドラー (バンドラーのような) |
| **距離::ジラ** |ディストリビューションビルダー |
| **アプリ::cpanminus** |最小限の CPAN クライアント |
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

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **モジョリシャス** |フルスタック |モダン、クリーン、電池付属 |
| **ダンサー2** |マイクロ |シナトラ風、軽量 |
| **触媒** |フルスタック |エンタープライズ、MVC |
| **プラック** | PSGI ツールキット |低レベルの Web インターフェイス |
| **スターマン** | HTTPサーバー | PSGIサーバー |
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

## データベース
|テクノロジー |タイプ |
|-----------|------|
| **DBI** |データベースインターフェース標準 |
| **DBD::SQLite** | SQLite ドライバー |
| **DBD::PG** | PostgreSQLドライバー |
| **DBD::mysql** | MySQLドライバー |
| **DBIx::クラス** |完全な ORM |
| **モジョ::Pg** | PostgreSQL (Mojolicious) |
| **Redis** | Redis クライアント |
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

## テスト
|フレームワーク |目的 |
|----------|----------|
| **テスト::詳細** |標準テストフレームワーク |
| **テスト 2::スイート** |最新のテスト (推奨) |
| **テスト::致命的** |例外テスト |
| **テスト::モックモジュール** |嘲笑 |
| **テスト::ディープ** |複雑なデータの比較 |
| **テスト::出力** | STDOUT/STDERR をキャプチャ |
| **証明** |テストランナー |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **perlcritic** |コードのリンティングとスタイル |
| **無能** |コードのフォーマット |
| **開発::カバー** |コードカバレッジ |
| **Perl::批評家** |ポリシーの施行 |
| **テスト::Perl::批評家** |テストの批評家 |
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

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **ムース / ムー** |最新のオブジェクト システム |
| **モジョリシャス** |ウェブフレームワーク |
| **DBI** |データベースインターフェース |
| **DBIx::クラス** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | JSON 解析 |
| **YAML::XS** | YAML 解析 |
| **LWP::ユーザーエージェント** | HTTPクライアント |
| **HTTP::Tiny** |最小限の HTTP クライアント |
| **IO::Socket::SSL** | SSL/TLS |
| **Parallel::ForkManager** |並列処理 |
| **MCE** |メニーコアエンジン |
| **試してください::Tiny** |例外処理 |
| **パス::Tiny** |ファイルパス |
| **リスト::ユーティリティ** |ユーティリティのリスト |
| **スカラー::ユーティリティ** |スカラーユーティリティ |
| **日付時刻** |日付/時刻の処理 |
| **ログ::任意** |伐採ファサード |
| **構成::任意** |構成 |
---

## テキスト処理
|ツール |目的 |
|----------|----------|
| **正規表現** |内蔵の強力な |
| **テンプレート::ツールキット** |テンプレートエンジン |
| **テキスト::CSV** | CSV 解析 |
| **XML::LibXML** | XML 処理 |
| **モジョ::DOM** | HTML/XML 解析 |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + Perl** | Perl 言語のサポート |
| **vim-perl** | Vim Perl のサポート |
| **Emacs + cperl モード** |クラシック Perl 環境 |
| **コモド** | ActiveState Perl IDE |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **スターマン** | PSGI Web サーバー |
| **ヒプノトード** |モジョリシャスサーバー |
| **ドッカー** |コンテナ化 |
| **PAR::パッカー** |スタンドアロンの実行可能ファイル |
| **カートン** |バンドルの依存関係 |
| **cpanfile + カートン** |再現可能な展開 |
---

＃＃ まとめ
Perl のエコシステムは広大で成熟しており、CPAN は 200,000 以上のモジュールをホストしています。標準スタックは、ランタイムとして **Perl 5.38+**、パッケージに対して **cpanm**、Web に対して **Mojolicious**、データベースに対して **DBI** + **DBIx::Class**、テストに対して **Test2::Suite**、lint に対して **perlcritic**、およびフォーマットに対して **perltidy** です。 Perl は、テキスト処理、システム管理、バイオインフォマティクス、レガシー Web アプリケーションに優れています。シグネチャ、後置逆参照、try/catch を備えた最新の Perl (5.38 以降) は、評判よりも大幅にクリーンです。このエコシステムは、システム管理者のスクリプト作成、データ処理、ラピッド プロトタイピングに最適です。