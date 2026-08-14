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
# Perl - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم پرل را پوشش می‌دهد.
---

## نسخه های پرل
| نسخه | یادداشت ها |
|---------|-------|
| **پرل 5.38+** | پایدار فعلی |
| **پرل 5.40** | جدیدترین ها با ویژگی های جدید |
| **راکو (پرل 6)** | طراحی مجدد مدرن (زبان جداگانه) |
| **گوزن** | سیستم OO مدرن |
| **مو** | گوزن سبک |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **CPAN** | شبکه جامع آرشیو پرل (200000+ ماژول) |
| **cpanm** | نصب کننده سبک CPAN |
| **cpanfile** | اعلامیه وابستگی |
| **کارتن** | بسته‌بندی وابستگی (مانند باندلر) |
| **Dist::Zilla** | سازنده توزیع |
| **برنامه::cpanminus** | حداقل مشتری CPAN |
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

## چارچوب های وب
| چارچوب | نوع | بهترین برای |
|-----------|------|----------|
| **مژولیکوس** | تمام پشته | مدرن، تمیز، دارای باتری |
| **رقصنده2** | میکرو | سیناترا مانند، سبک |
| **کاتالیزور** | تمام پشته | Enterprise, MVC |
| **پلاک** | جعبه ابزار PSGI | رابط وب سطح پایین |
| **استارمن** | سرور HTTP | سرور PSGI |
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

## پایگاه داده
| فناوری | نوع |
|------------|------|
| **DBI** | استاندارد رابط پایگاه داده |
| **DBD::SQLite** | درایور SQLite |
| **DBD::Pg** | درایور PostgreSQL |
| **DBD::mysql** | درایور MySQL |
| **DBIx::Class** | ORM کامل |
| **موجو::صفحه** | PostgreSQL (Mojolicious) |
| **ردیس** | مشتری Redis |
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

## تست
| چارچوب | هدف |
|-----------|---------|
| **تست::بیشتر** | چارچوب آزمون استاندارد |
| **Test2::Suite** | تست مدرن (توصیه می شود) |
| **تست::کشنده** | تست استثنا |
| **تست::MockModule** | تمسخر |
| **تست::عمیق** | مقایسه داده های پیچیده |
| **تست::خروجی** | گرفتن STDOUT/STDERR |
| **اثبات** | دونده تست |
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

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **perlcritic** | کد لینتینگ و سبک |
| **perltidy** | قالب بندی کد |
| **توسعه:: جلد** | پوشش کد |
| **پرل::نقد ** | اجرای سیاست |
| **تست::Perl::Critic** | منتقد در آزمون ها |
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

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **گوزن / مو** | سیستم شی مدرن |
| **مژولیکوس** | چارچوب وب |
| **DBI** | رابط پایگاه داده |
| **DBIx::Class** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | تجزیه JSON |
| **YAML::XS** | تجزیه YAML |
| **LWP::UserAgent** | سرویس گیرنده HTTP |
| **HTTP::کوچک** | حداقل مشتری HTTP |
| **IO::Socket::SSL** | SSL/TLS |
| **موازی::ForkManager** | پردازش موازی |
| **MCE** | موتور چند هسته ای |
| **امتحان کنید::کوچک** | رسیدگی به استثنا |
| **مسیر::کوچک** | مسیرهای فایل |
| **لیست::Util** | فهرست برنامه های کاربردی |
| **اسکالار::Util** | ابزارهای اسکالر |
| **تاریخ ساعت** | رسیدگی به تاریخ/زمان |
| **Log::هر** | نمای چوبی |
| **Config::Any** | پیکربندی |
---

## پردازش متن
| ابزار | هدف |
|---------|---------|
| **عبارات منظم** | داخلی، قدرتمند |
| **قالب::Toolkit** | موتور قالب |
| **متن::CSV** | تجزیه CSV |
| **XML::LibXML** | پردازش XML |
| **موجو::DOM** | تجزیه HTML/XML |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + Perl** | پشتیبانی از زبان پرل |
| **vim-perl** | پشتیبانی از Vim Perl |
| **Emacs + cperl-mode** | محیط کلاسیک پرل |
| **کومودو** | ActiveState Perl IDE |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **استارمن** | وب سرور PSGI |
| **Hypnotoad** | سرور Mojolicious |
| **داکر** | کانتینری |
| **PAR::Packer** | فایل های اجرایی مستقل |
| **کارتن** | بسته های وابسته |
| **cpanfile + کارتن** | استقرارهای تکراری |
---

## خلاصه
اکوسیستم پرل گسترده و بالغ است و CPAN میزبان بیش از 200000 ماژول است. پشته استاندارد عبارتند از: **Perl 5.38+** به عنوان زمان اجرا، **cpanm** برای بسته ها، **Mojolicious** برای وب، **DBI** + **DBIx::Class** برای پایگاه های داده، **Test2::Suite** برای آزمایش، **perlcritic** برای linting، و **perltidy**. پرل در پردازش متن، مدیریت سیستم، بیوانفورماتیک و برنامه های کاربردی وب قدیمی برتری دارد. پرل مدرن (5.38+) با امضاها، پسوند پسوند، و امتحان/گرفتن به طور قابل توجهی تمیزتر از آن چیزی است که شهرت آن نشان می دهد. این اکوسیستم برای اسکریپت نویسی sysadmin، پردازش داده ها و نمونه سازی سریع ایده آل است.