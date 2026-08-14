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
# پرل - ایکو سسٹم اور ٹولنگ گائیڈ
یہ گائیڈ پرل ماحولیاتی نظام میں ضروری ٹولز، فریم ورک اور انفراسٹرکچر کا احاطہ کرتا ہے۔
---

## پرل ورژن
| ورژن | نوٹس |
|---------|---------|
| **پرل 5.38+** | موجودہ مستحکم |
| **پرل 5.40** | نئی خصوصیات کے ساتھ تازہ ترین |
| **راکو (پرل 6)** | جدید ری ڈیزائن (علیحدہ زبان) |
| **موس** | جدید OO نظام |
| **مو** | ہلکا پھلکا موس |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## پیکیج مینجمنٹ
| ٹول | مقصد |
|------|---------|
| **CPAN** | جامع پرل آرکائیو نیٹ ورک (200,000+ ماڈیولز) |
| **cpanm** | ہلکا پھلکا CPAN انسٹالر |
| **cpanfile** | انحصار کا اعلان |
| **کارٹن** | انحصار بنڈلر (جیسے بنڈلر) |
| **Dist::Zilla** | ڈسٹری بیوشن بلڈر |
| **App::cpanminus** | کم سے کم CPAN کلائنٹ |
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

## ویب فریم ورک
| فریم ورک | قسم | کے لیے بہترین |
|------------|------|---------|
| **موجولیشیئس** | مکمل اسٹیک | جدید، صاف، بیٹریاں شامل ہیں۔
| **ڈانسر2** | مائیکرو | سناترا کی طرح، ہلکا پھلکا |
| **کیٹالسٹ** | مکمل اسٹیک | انٹرپرائز، MVC |
| **پلیک** | PSGI ٹول کٹ | کم سطح کا ویب انٹرفیس |
| **اسٹارمین** | HTTP سرور | PSGI سرور |
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

## ڈیٹا بیس
| ٹیکنالوجی | قسم |
|------------|------|
| **DBI** | ڈیٹا بیس انٹرفیس معیاری |
| **DBD::SQLite** | SQLite ڈرائیور |
| **DBD::Pg** | PostgreSQL ڈرائیور |
| **DBD::mysql** | MySQL ڈرائیور |
| **DBIx::Class** | مکمل ORM |
| **موجو::Pg** | PostgreSQL (Mojolicious) |
| **ریڈیس** | Redis کلائنٹ |
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

## ٹیسٹنگ
| فریم ورک | مقصد |
|------------|---------|
| **ٹیسٹ::مزید** | معیاری ٹیسٹ فریم ورک |
| **Test2::Suite** | جدید ٹیسٹنگ (تجویز کردہ) |
| **ٹیسٹ::مہلک** | استثناء کی جانچ |
| **Test::MockModule** | طنز |
| **ٹیسٹ::گہری** | پیچیدہ ڈیٹا کا موازنہ |
| **ٹیسٹ::آؤٹ پٹ** | کیپچر STDOUT/STDERR |
| **ثابت کریں** | ٹیسٹ رنر |
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

## کوڈ کا معیار
| ٹول | مقصد |
|------|---------|
| **پرل ناقد** | کوڈ linting اور انداز |
| **پرلٹیڈی** | کوڈ فارمیٹنگ |
| **ترقی::کور** | کوڈ کوریج |
| **پرل::نقد** | پالیسی کا نفاذ |
| **ٹیسٹ::پرل::نقد** | ٹیسٹ میں نقاد |
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

## کلیدی لائبریریاں
| لائبریری | مقصد |
|---------|---------|
| ** Moose / Moo** | جدید آبجیکٹ سسٹم |
| **موجولیشیئس** | ویب فریم ورک |
| **DBI** | ڈیٹا بیس انٹرفیس |
| **DBIx::Class** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | JSON پارسنگ |
| **YAML::XS** | YAML پارسنگ |
| **LWP::UserAgent** | HTTP کلائنٹ |
| **HTTP::Tiny** | کم سے کم HTTP کلائنٹ |
| **IO::Socket::SSL** | SSL/TLS |
| **متوازی::ForkManager** | متوازی پروسیسنگ |
| **MCE** | کئی کور انجن |
| **کوشش کریں::Tiny** | استثنیٰ ہینڈلنگ |
| **راستہ::چھوٹا** | فائل کے راستے |
| **فہرست::Util** | افادیت کی فہرست |
| **اسکیلر::Util** | اسکیلر یوٹیلیٹیز |
| **تاریخ کا وقت** | تاریخ/وقت ہینڈلنگ |
| **لاگ::کوئی** | لاگنگ اگواڑا |
| **تشکیل::کوئی** | ترتیب |
---

## ٹیکسٹ پروسیسنگ
| ٹول | مقصد |
|---------|---------|
| **باقاعدہ تاثرات** | بلٹ میں، طاقتور |
| **Template::Toolkit** | ٹیمپلیٹ انجن |
| **متن::CSV** | CSV پارسنگ |
| **XML::LibXML** | XML پروسیسنگ |
| **موجو::DOM** | HTML/XML پارسنگ |
---

## IDEs اور ایڈیٹرز
| IDE | طاقتیں |
|------|------------|
| **VS کوڈ + پرل** | پرل زبان کی حمایت |
| **vim-perl** | ویم پرل سپورٹ |
| **Emacs + cperl-mode** | کلاسیکی پرل ماحول |
| **کوموڈو** | ایکٹو اسٹیٹ پرل IDE |
---

## تعیناتی۔
| طریقہ | نوٹس |
|---------|-------|
| **اسٹارمین** | PSGI ویب سرور |
| **ہپنوٹوڈ** | Mojolicious سرور |
| **ڈوکر** | کنٹینرائزڈ |
| **PAR::Packer** | اسٹینڈ اسٹون ایگزیکیوٹیبلز |
| **کارٹن** | بنڈل انحصار |
| **cpanfile + کارٹن** | دوبارہ پیدا کرنے کے قابل تعیناتیاں |
---

## خلاصہ
پرل کا ماحولیاتی نظام وسیع اور پختہ ہے، جس میں CPAN 200,000+ ماڈیولز کی میزبانی کرتا ہے۔ معیاری اسٹیک یہ ہے: **پرل 5.38+** رن ٹائم کے طور پر، پیکجز کے لیے **cpanm**، ویب کے لیے **Mojolicious**، **DBI** + **DBIx::Class** ڈیٹا بیسز کے لیے، **Test2::Suite** ٹیسٹنگ کے لیے، **perlcritic** linting کے لیے، اور **perlcritic** کے لیے۔ پرل ٹیکسٹ پروسیسنگ، سسٹم ایڈمنسٹریشن، بائیو انفارمیٹکس، اور لیگیسی ویب ایپلیکیشنز پر سبقت لے جاتا ہے۔ دستخطوں کے ساتھ جدید پرل (5.38+)، پوسٹ فکس ڈیریفرنس، اور ٹرائی/کیچ اس کی ساکھ سے کہیں زیادہ صاف ہے۔ ماحولیاتی نظام sysadmin اسکرپٹنگ، ڈیٹا پروسیسنگ، اور تیز رفتار پروٹو ٹائپنگ کے لیے مثالی ہے۔