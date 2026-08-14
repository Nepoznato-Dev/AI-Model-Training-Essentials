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

# Perl — 生態系與工具指南
本指南涵蓋了 Perl 生態系統中的基本工具、框架和基礎設施。
---

## Perl 版本
|版本 |筆記|
|--------|--------|
| **Perl 5.38+** |目前穩定|
| **Perl 5.40** |最新的新功能 |
| **Raku (Perl 6)** |現代重新設計（單獨語言）|
| **駝鹿** |現代物件導向系統|
| **哞** |輕量級駝鹿 |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## 套件管理
|工具|目的|
|------|---------|
| **CPAN** |全面的 Perl 存檔網路（200,000+ 模組）|
| **cpanm** |輕量級 CPAN 安裝程式 |
| **cpan檔案** |依賴聲明 |
| **紙箱** |依賴項捆綁器（如 Bundler）|
| **距離::Zilla** |分銷建設者|
| **應用程式::cpanminus** |最小 CPAN 用戶端 |
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

## 網路框架
|框架|類型 |最適合 |
|------------|------|----------|
| **Mojolicious** |全端|現代、乾淨、含電池 |
| **舞者2** |微|類似 Sinatra 的輕量級 |
| **催化劑** |全端|企業、MVC |
| **普拉克** | PSGI 工具包 |低階 Web 介面 |
| **星人** | HTTP 伺服器 | PSGI 伺服器 |
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

## 資料庫
|技術 |類型 |
|------------|------|
| **DBI** |資料庫介面標準|
| **DBD::SQLite** | SQLite 驅動程式 |
| **DBD::Pg** | PostgreSQL 驅動程式 |
| **DBD::mysql** | MySQL 驅動程式 |
| **DBIx::類別** |完整的 ORM |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Redis** | Redis 用戶端 |
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

## 測試
|框架|目的|
|------------|---------|
| **測試::更多** |標準測試框架 |
| **測試2::套件** |現代測試（建議）|
| **測試::致命** |異常測試 |
| **測試::MockModule** |嘲笑|
| **測試::深度** |複雜資料比較 |
| **測試::輸出** |捕獲 STDOUT/STDERR |
| **證明** |測試運行者 |
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

## 程式碼品質
|工具|目的|
|------|---------|
| **perlcritic** |程式碼檢查與風格 |
| **完美** |程式碼格式化 |
| **開發::封面** |程式碼覆蓋率|
| **Perl::評論家** |政策執行|
| **測試::Perl::Critic** |測試中的批評者|
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

## 關鍵庫
|圖書館 |目的|
|---------|---------|
| **駝鹿/哞** |現代物件系統|
| **Mojolicious** |網頁框架|
| **DBI** |資料庫介面|
| **DBIx::類別** |物件關係管理 |
| **JSON::XS / Cpanel::JSON::XS** | JSON解析|
| **YAML::XS** | YAML 解析 |
| **LWP::UserAgent** | HTTP 用戶端 |
| **HTTP::微小** |最小 HTTP 用戶端 |
| **IO::Socket::SSL** | SSL/TLS |
| **並行::ForkManager** |並行處理 |
| **MCE** |多核心引擎 |
| **嘗試::小** |異常處理 |
| **路徑::微小** |檔案路徑 |
| **列表::實用程式** |列出實用程式 |
| **標量::Util** |標量公用程式 |
| **日期時間** |日期/時間處理 |
| **日誌::任何** |伐木門面 |
| **配置::任意** |配置|
---

## 文字處理
|工具|目的|
|---------|---------|
| **正規表示式** |內置，功能強大 |
| **模板::工具包** |模板引擎|
| **文字::CSV** | CSV 解析 |
| **XML::LibXML** | XML 處理 |
| **Mojo::DOM** | HTML/XML 解析 |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS 代碼 + Perl** | Perl 語言支援 |
| **vim-perl** | Vim Perl 支援 |
| **Emacs + cperl 模式** |經典 Perl 環境 |
| **科莫多** | ActiveState Perl IDE | ActiveState Perl IDE
---

## 部署
|方法|筆記|
|--------|--------|
| **星人** | PSGI 網路伺服器 |
| **催眠蟾蜍** | Mojolicious 伺服器 |
| **碼頭工人** |貨櫃式|
| **PAR::打包機** |獨立的可執行檔|
| **紙箱** |捆綁依賴項 |
| **cpanfile + 紙箱** |可重複部署 |
---

＃＃ 概括
Perl 的生態系統龐大且成熟，CPAN 託管著 200,000 多個模組。標準堆疊是：**Perl 5.38+** 作為運行時，**cpanm** 用於包，**Mojolicious** 用於 Web，**DBI** + **DBIx::Class** 用於數據庫，**Test2::Suite** 用於測試，**perlcritic** 用於 linting，以及 **perltidy** 用於格式化。 Perl 擅長文字處理、系統管理、生物資訊學和遺留 Web 應用程式。具有簽名、後綴取消引用和 try/catch 的現代 Perl（5.38+）比其聲譽所暗示的要乾淨得多。此生態系統非常適合系統管理腳本、資料處理和快速原型設計。