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

# Perl - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศ Perl
---

## เวอร์ชัน Perl
| เวอร์ชั่น | หมายเหตุ |
|---------|-------|
| **เพิร์ล 5.38+** | ปัจจุบันมีเสถียรภาพ |
| **เพิร์ล 5.40** | ล่าสุดด้วยคุณสมบัติใหม่ |
| **ราคุ (Perl 6)** | ออกแบบใหม่ทันสมัย ​​(แยกภาษา) |
| **มูส** | ระบบ OO สมัยใหม่ |
| **หมู** | มูสน้ำหนักเบา |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **ซีปัน** | เครือข่ายการเก็บถาวร Perl ที่ครอบคลุม (200,000+ โมดูล) |
| **cpanm** | ตัวติดตั้ง CPAN แบบน้ำหนักเบา |
| **cpanfile** | การประกาศการพึ่งพา |
| **กล่อง** | Bundler การพึ่งพา (เช่น Bundler) |
| **Dist::Zilla** | ผู้สร้างการจัดจำหน่าย |
| **แอป::cpanminus** | ไคลเอนต์ CPAN ขั้นต่ำ |
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

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **โมโจลิเชียส** | เต็มกอง | ทันสมัย ​​สะอาด รวมแบตเตอรี่ |
| **แดนเซอร์2** | ไมโคร | คล้ายซินาตร้า น้ำหนักเบา |
| **ตัวเร่งปฏิกิริยา** | เต็มกอง | องค์กร MVC |
| **ปลัก** | ชุดเครื่องมือ PSGI | เว็บอินเตอร์เฟสระดับต่ำ |
| **สตาร์แมน** | เซิร์ฟเวอร์ HTTP | เซิร์ฟเวอร์ PSGI |
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

## ฐานข้อมูล
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **ดีบีไอ** | มาตรฐานอินเตอร์เฟสฐานข้อมูล |
| **DBD::SQLite** | ไดรเวอร์ SQLite |
| **DBD::Pg** | ไดรเวอร์ PostgreSQL |
| **DBD::mysql** | ไดรเวอร์ MySQL |
| **DBIx::คลาส** | ORM เต็ม |
| **โมโจ::Pg** | PostgreSQL (Mojolicious) |
| **เรดิส** | ลูกค้า Redis |
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

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **ทดสอบ::เพิ่มเติม** | กรอบการทดสอบมาตรฐาน |
| **Test2::ชุด** | การทดสอบสมัยใหม่ (แนะนำ) |
| **ทดสอบ::ร้ายแรง** | การทดสอบข้อยกเว้น |
| **ทดสอบ::MockModule** | ล้อเลียน |
| **ทดสอบ::ลึก** | การเปรียบเทียบข้อมูลที่ซับซ้อน |
| **ทดสอบ::เอาท์พุต** | จับภาพ STDOUT/STDERR |
| **พิสูจน์** | นักวิ่งทดสอบ |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **นักวิจารณ์** | รหัสขุยและสไตล์ |
| **สกปรก** | การจัดรูปแบบโค้ด |
| **การพัฒนา::ปก** | ความครอบคลุมของโค้ด |
| **Perl::นักวิจารณ์** | การบังคับใช้นโยบาย |
| **ทดสอบ::Perl::นักวิจารณ์** | นักวิจารณ์ในการทดสอบ |
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

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **มูส/มู** | ระบบวัตถุสมัยใหม่ |
| **โมโจลิเชียส** | กรอบงานเว็บ |
| **ดีบีไอ** | ส่วนต่อประสานฐานข้อมูล |
| **DBIx::คลาส** | ออม |
| **JSON::XS / Cpanel::JSON::XS** | การแยกวิเคราะห์ JSON |
| **YAML::XS** | การแยกวิเคราะห์ YAML |
| **LWP::UserAgent** | ไคลเอ็นต์ HTTP |
| **HTTP::จิ๋ว** | ไคลเอนต์ HTTP ขั้นต่ำ |
| **IO::Socket::SSL** | SSL/TLS |
| **ขนาน::ForkManager** | การประมวลผลแบบขนาน |
| **เอ็มซีอี** | เครื่องยนต์หลายคอร์ |
| **ลอง::จิ๋ว** | การจัดการข้อยกเว้น |
| **เส้นทาง::จิ๋ว** | เส้นทางไฟล์ |
| **รายการ::ยูทิลิตี้** | รายการยูทิลิตี้ |
| **สเกลาร์::Util** | ยูทิลิตี้เกลา |
| **วันที่และเวลา** | การจัดการวันที่/เวลา |
| **บันทึก::ใดๆ** | ซุ้มไม้ซุง |
| **Config::ใดๆ** | การกำหนดค่า |
---

## การประมวลผลข้อความ
| เครื่องมือ | วัตถุประสงค์ |
|---------|---------|
| **สำนวนปกติ** | ในตัวทรงพลัง |
| **แม่แบบ::ชุดเครื่องมือ** | เอ็นจิ้นเทมเพลต |
| **ข้อความ::CSV** | การแยกวิเคราะห์ CSV |
| **XML::LibXML** | การประมวลผล XML |
| **โมโจ::DOM** | การแยกวิเคราะห์ HTML/XML |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **รหัส VS + Perl** | รองรับภาษา Perl |
| **vim-perl** | การสนับสนุน Vim Perl |
| **Emacs + โหมด cperl** | สภาพแวดล้อม Perl แบบคลาสสิก |
| **โคโมโด** | ActiveState Perl IDE |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **สตาร์แมน** | เว็บเซิร์ฟเวอร์ PSGI |
| **สะกดจิต** | เซิร์ฟเวอร์โมโจลิเชียส |
| **นักเทียบท่า** | บรรจุในตู้คอนเทนเนอร์ |
| **PAR::Packer** | ไฟล์ปฏิบัติการแบบสแตนด์อโลน |
| **กล่อง** | การพึ่งพาบันเดิล |
| **cpanfile + กล่อง** | การปรับใช้ที่ทำซ้ำได้ |
---

## สรุป
ระบบนิเวศของ Perl นั้นกว้างใหญ่และสมบูรณ์ โดย CPAN มีโฮสต์มากกว่า 200,000 โมดูล สแต็กมาตรฐานคือ: **Perl 5.38+** สำหรับรันไทม์, **cpanm** สำหรับแพ็คเกจ, **Mojolicious** สำหรับเว็บ, **DBI** + **DBIx::Class** สำหรับฐานข้อมูล, **Test2::Suite** สำหรับการทดสอบ, **perlcritic** สำหรับ Linting และ **perltidy** สำหรับการจัดรูปแบบ Perl เชี่ยวชาญด้านการประมวลผลข้อความ การบริหารระบบ ชีวสารสนเทศศาสตร์ และเว็บแอปพลิเคชันรุ่นเก่า Modern Perl (5.38+) พร้อมลายเซ็นต์ การอ้างอิงแบบ postfix และ try/catch นั้นสะอาดกว่าที่ชื่อเสียงแนะนำอย่างมาก ระบบนิเวศนี้เหมาะอย่างยิ่งสำหรับการเขียนสคริปต์ดูแลระบบ การประมวลผลข้อมูล และการสร้างต้นแบบอย่างรวดเร็ว