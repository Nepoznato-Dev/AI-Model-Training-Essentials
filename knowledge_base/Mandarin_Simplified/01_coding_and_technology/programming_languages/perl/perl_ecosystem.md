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

# Perl — 生态系统和工具指南
本指南涵盖了 Perl 生态系统中的基本工具、框架和基础设施。
---

## Perl 版本
|版本 |笔记|
|--------|--------|
| **Perl 5.38+** |目前稳定|
| **Perl 5.40** |最新的新功能 |
| **Raku (Perl 6)** |现代重新设计（单独语言）|
| **驼鹿** |现代面向对象系统|
| **哞** |轻量级驼鹿 |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## 包管理
|工具|目的|
|------|---------|
| **CPAN** |全面的 Perl 存档网络（200,000+ 模块）|
| **cpanm** |轻量级 CPAN 安装程序 |
| **cpan文件** |依赖声明 |
| **纸箱** |依赖项捆绑器（如 Bundler）|
| **距离::Zilla** |分销建设者|
| **应用程序::cpanminus** |最小 CPAN 客户端 |
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

## 网络框架
|框架|类型 |最适合 |
|------------|------|----------|
| **Mojolicious** |全栈|现代、干净、含电池 |
| **舞者2** |微|类似 Sinatra 的轻量级 |
| **催化剂** |全栈|企业、MVC |
| **普拉克** | PSGI 工具包 |低级 Web 界面 |
| **星人** | HTTP 服务器 | PSGI 服务器 |
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

＃＃ 数据库
|技术 |类型 |
|------------|------|
| **DBI** |数据库接口标准|
| **DBD::SQLite** | SQLite 驱动程序 |
| **DBD::Pg** | PostgreSQL 驱动程序 |
| **DBD::mysql** | MySQL 驱动程序 |
| **DBIx::类** |完整的 ORM |
| **Mojo::Pg** | PostgreSQL (Mojolicious) |
| **Redis** | Redis 客户端 |
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

## 测试
|框架|目的|
|------------|---------|
| **测试::更多** |标准测试框架 |
| **测试2::套件** |现代测试（推荐）|
| **测试::致命** |异常测试 |
| **测试::MockModule** |嘲笑|
| **测试::深度** |复杂数据对比 |
| **测试::输出** |捕获 STDOUT/STDERR |
| **证明** |测试运行者 |
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

## 代码质量
|工具|目的|
|------|---------|
| **perlcritic** |代码检查和风格 |
| **完美** |代码格式化 |
| **开发::封面** |代码覆盖率|
| **Perl::评论家** |政策执行|
| **测试::Perl::Critic** |测试中的批评者|
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

## 关键库
|图书馆 |目的|
|---------|---------|
| **驼鹿/哞** |现代对象系统|
| **Mojolicious** |网页框架|
| **DBI** |数据库接口|
| **DBIx::类** |对象关系管理 |
| **JSON::XS / Cpanel::JSON::XS** | JSON解析|
| **YAML::XS** | YAML 解析 |
| **LWP::UserAgent** | HTTP 客户端 |
| **HTTP::微小** |最小 HTTP 客户端 |
| **IO::Socket::SSL** | SSL/TLS |
| **并行::ForkManager** |并行处理 |
| **MCE** |多核引擎 |
| **尝试::小** |异常处理 |
| **路径::微小** |文件路径 |
| **列表::实用程序** |列出实用程序 |
| **标量::Util** |标量实用程序 |
| **日期时间** |日期/时间处理 |
| **日志::任何** |伐木门面 |
| **配置::任意** |配置|
---

## 文本处理
|工具|目的|
|---------|---------|
| **正则表达式** |内置，功能强大 |
| **模板::工具包** |模板引擎|
| **文本::CSV** | CSV 解析 |
| **XML::LibXML** | XML 处理 |
| **Mojo::DOM** | HTML/XML 解析 |
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **VS 代码 + Perl** | Perl 语言支持 |
| **vim-perl** | Vim Perl 支持 |
| **Emacs + cperl 模式** |经典 Perl 环境 |
| **科莫多** | ActiveState Perl IDE | ActiveState Perl IDE
---

## 部署
|方法|笔记|
|--------|--------|
| **星人** | PSGI 网络服务器 |
| **催眠蟾蜍** | Mojolicious 服务器 |
| **码头工人** |集装箱式|
| **PAR::打包机** |独立的可执行文件|
| **纸箱** |捆绑依赖项 |
| **cpanfile + 纸箱** |可重复部署 |
---

＃＃ 概括
Perl 的生态系统庞大而成熟，CPAN 托管着 200,000 多个模块。标准堆栈是：**Perl 5.38+** 作为运行时，**cpanm** 用于包，**Mojolicious** 用于 Web，**DBI** + **DBIx::Class** 用于数据库，**Test2::Suite** 用于测试，**perlcritic** 用于 linting，以及 **perltidy** 用于格式化。 Perl 擅长文本处理、系统管理、生物信息学和遗留 Web 应用程序。具有签名、后缀取消引用和 try/catch 的现代 Perl（5.38+）比其声誉所暗示的要干净得多。该生态系统非常适合系统管理脚本、数据处理和快速原型设计。