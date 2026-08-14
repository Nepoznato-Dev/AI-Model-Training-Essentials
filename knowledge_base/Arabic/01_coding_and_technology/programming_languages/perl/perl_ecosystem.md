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
# بيرل - دليل النظام البيئي والأدوات
يغطي هذا الدليل الأدوات والأطر والبنية التحتية الأساسية في نظام Perl البيئي.
---

## إصدارات بيرل
| النسخة | ملاحظات |
|---------|------|
| ** بيرل 5.38+** | مستقر الحالي |
| ** بيرل 5.40 ** | الأحدث مع الميزات الجديدة |
| ** راكو (بيرل 6) ** | إعادة التصميم الحديث (لغة منفصلة) |
| **موس** | نظام OO الحديث |
| **مو** | موس خفيف الوزن |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## إدارة الحزم
| أداة | الغرض |
|------|---------|
| **CPAN** | شبكة أرشيف بيرل الشاملة (أكثر من 200.000 وحدة) |
| ** سي بانم ** | مثبت CPAN خفيف الوزن |
| **ملف cpan** | إعلان التبعية |
| **كرتونة** | مجمع التبعية (مثل Bundler) |
| **ديست::زيلا** | منشئ التوزيع |
| **التطبيق::cpanminus** | الحد الأدنى من عميل CPAN |
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

## أطر الويب
| الإطار | اكتب | الأفضل لـ |
|-----------|------|----------|
| **مرح** | مكدس كامل | حديثة ونظيفة، متضمنة البطاريات |
| **راقصة2** | مايكرو | مثل سيناترا، خفيف الوزن |
| **محفز** | مكدس كامل | مؤسسة، MVC |
| **بلاك** | مجموعة أدوات PSGI | واجهة ويب منخفضة المستوى |
| **ستارمان** | خادم HTTP | خادم PSGI |
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

##قاعدة البيانات
| تكنولوجيا | اكتب |
|------------|------|
| ** دي بي آي ** | واجهة قاعدة البيانات القياسية |
| **DBD::SQLite** | سائق سكليتي |
| **DBD::Pg** | برنامج تشغيل PostgreSQL |
| **DBD::mysql** | برنامج تشغيل MySQL |
| **DBIx::فئة** | ORM كامل |
| **موجو::صفحة** | بوستجري إس كيو إل (موجوليشيوس) |
| **ريديس** | عميل ريديس |
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

## الاختبار
| الإطار | الغرض |
|-----------|--------|
| **اختبار::المزيد** | إطار الاختبار القياسي |
| **الاختبار2::جناح** | الاختبارات الحديثة (مستحسن) |
| **اختبار::قاتل** | اختبار الاستثناء |
| **اختبار::MockModule** | استهزاء |
| **اختبار::عميق** | مقارنة البيانات المعقدة |
| **اختبار::الإخراج** | التقاط STDOUT/STDERR |
| **اثبت** | عداء الاختبار |
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

## جودة الكود
| أداة | الغرض |
|------|---------|
| **بيرلكريتيك** | فحص الكود والأسلوب |
| **بيرلتيدي** | تنسيق الكود |
| **التصميم::الغلاف** | تغطية الكود |
| ** بيرل::ناقد** | إنفاذ السياسات |
| **اختبار::بيرل::ناقد** | الناقد في الاختبارات |
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

## المكتبات الرئيسية
| مكتبة | الغرض |
|---------|--------|
| **موس/مو** | نظام الكائن الحديث |
| **مرح** | إطار الويب |
| ** دي بي آي ** | واجهة قاعدة البيانات |
| **DBIx::فئة** | أو آر إم |
| **JSON::XS / Cpanel::JSON::XS** | تحليل JSON |
| **يامل::XS** | تحليل YAML |
| **LWP::UserAgent** | عميل HTTP |
| **HTTP::صغير** | الحد الأدنى من عميل HTTP |
| **IO::Socket::SSL** | SSL/TLS |
| **بالتوازي::ForkManager** | المعالجة المتوازية |
| **إم سي إي** | محرك متعدد النواة |
| **جرب::صغيرة** | معالجة الاستثناء |
| **المسار::صغيرة** | مسارات الملفات |
| **القائمة::Util** | قائمة المرافق |
| **العددية::Util** | المرافق العددية |
| **التاريخ والوقت** | التعامل مع التاريخ/الوقت |
| **السجل::أي** | واجهة التسجيل |
| **التكوين::أي** | التكوين |
---

## معالجة النصوص
| أداة | الغرض |
|---------|--------|
| ** التعبيرات العادية ** | مدمج وقوي |
| **قالب::مجموعة الأدوات** | محرك القالب |
| **النص::CSV** | تحليل CSV |
| **XML::LibXML** | معالجة XML |
| **موجو::DOM** | تحليل HTML/XML |
---

## بيئة التطوير المتكاملة والمحررين
| بيئة تطوير متكاملة | نقاط القوة |
|-----|----------|
| ** كود VS + بيرل ** | دعم لغة بيرل |
| ** فيم بيرل ** | دعم فيم بيرل |
| ** إيماكس + وضع cperl ** | بيئة بيرل الكلاسيكية |
| **كومودو** | ActiveState بيرل IDE |
---

## النشر
| الطريقة | ملاحظات |
|--------|------|
| **ستارمان** | خادم الويب PSGI |
| **المنوم** | خادم موجوليشيوس |
| ** عامل الميناء ** | في حاويات |
| ** الاسمية :: باكر ** | الملفات التنفيذية المستقلة |
| **كرتونة** | تبعيات الحزمة |
| ** ملف cpanfile + كرتونة ** | عمليات النشر القابلة للتكرار |
---

## ملخص
يعد نظام Perl البيئي واسعًا وناضجًا، حيث تستضيف CPAN أكثر من 200000 وحدة. المكدس القياسي هو: **Perl 5.38+** كوقت تشغيل، **cpanm** للحزم، **Mojolicious** للويب، **DBI** + **DBIx::Class** لقواعد البيانات، **Test2::Suite** للاختبار، **perlcritic** للفحص، و **perltidy** للتنسيق. تتفوق لغة Perl في معالجة النصوص وإدارة النظام والمعلوماتية الحيوية وتطبيقات الويب القديمة. تعتبر لغة Perl الحديثة (5.38+) مع التوقيعات وإلغاء الإشارة اللاحقة للإصلاح ومحاولة/التقاط أكثر نظافة بكثير مما توحي به سمعتها. يعد النظام البيئي مثاليًا للبرمجة النصية لمسؤول النظام ومعالجة البيانات والنماذج الأولية السريعة.