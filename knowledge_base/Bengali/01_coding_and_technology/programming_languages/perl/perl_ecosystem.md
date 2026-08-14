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
# পার্ল — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি পার্ল ইকোসিস্টেমের প্রয়োজনীয় টুল, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## পার্ল সংস্করণ
| সংস্করণ | নোট |
|---------|---------|
| **পার্ল ৫.৩৮+** | বর্তমান স্থিতিশীল |
| **পার্ল 5.40** | নতুন বৈশিষ্ট্য সহ সর্বশেষ |
| **রাকু (পার্ল 6)** | আধুনিক রিডিজাইন (পৃথক ভাষা) |
| **মোজ** | আধুনিক ওও সিস্টেম |
| **মু** | লাইটওয়েট মুস |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **CPAN** | ব্যাপক পার্ল আর্কাইভ নেটওয়ার্ক (200,000+ মডিউল) |
| **cpanm** | লাইটওয়েট CPAN ইনস্টলার |
| **cpanfile** | নির্ভরতা ঘোষণা |
| **কার্টন** | নির্ভরতা বান্ডলার (বান্ডলারের মতো) |
| **জেলা::জিলা** | ডিস্ট্রিবিউশন নির্মাতা |
| **অ্যাপ::cpanminus** | ন্যূনতম CPAN ক্লায়েন্ট |
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

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **মোজোলিসিয়াস** | ফুল-স্ট্যাক | আধুনিক, পরিষ্কার, ব্যাটারি-অন্তর্ভুক্ত |
| **নর্তকী2** | মাইক্রো | সিনাত্রার মত, হালকা |
| **অনুঘটক** | ফুল-স্ট্যাক | এন্টারপ্রাইজ, MVC |
| **প্ল্যাক** | PSGI টুলকিট | নিম্ন-স্তরের ওয়েব ইন্টারফেস |
| **স্টারম্যান** | HTTP সার্ভার | PSGI সার্ভার |
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

## ডাটাবেস
| প্রযুক্তি | প্রকার |
|------------|------|
| **DBI** | ডাটাবেস ইন্টারফেস স্ট্যান্ডার্ড |
| **DBD::SQLite** | SQLite ড্রাইভার |
| **DBD::Pg** | PostgreSQL ড্রাইভার |
| **DBD::mysql** | মাইএসকিউএল ড্রাইভার |
| **DBIx::শ্রেণী** | সম্পূর্ণ ORM |
| **মোজো::Pg** | PostgreSQL (Mojolicious) |
| **রেডিস** | Redis ক্লায়েন্ট |
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

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **পরীক্ষা::আরো** | স্ট্যান্ডার্ড টেস্ট ফ্রেমওয়ার্ক |
| **Test2::Suite** | আধুনিক পরীক্ষা (প্রস্তাবিত) |
| **পরীক্ষা::মারাত্মক** | ব্যতিক্রম পরীক্ষা |
| **পরীক্ষা::মকমডিউল** | উপহাস |
| **পরীক্ষা::গভীর** | জটিল তথ্য তুলনা |
| **পরীক্ষা::আউটপুট** | STDOUT/STDERR ক্যাপচার করুন |
| **প্রমাণ** | টেস্ট রানার |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **পার্ল সমালোচক** | কোড লিন্টিং এবং শৈলী |
| **অনেক** | কোড ফরম্যাটিং |
| **ডেভেল::কভার** | কোড কভারেজ |
| **পার্ল::সমালোচক** | নীতি প্রয়োগ |
| **পরীক্ষা::পার্ল::সমালোচক** | পরীক্ষায় সমালোচক |
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

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **মুস/মু** | আধুনিক অবজেক্ট সিস্টেম |
| **মোজোলিসিয়াস** | ওয়েব ফ্রেমওয়ার্ক |
| **DBI** | ডাটাবেস ইন্টারফেস |
| **DBIx::শ্রেণী** | ORM |
| **JSON::XS / Cpanel::JSON::XS** | JSON পার্সিং |
| **YAML::XS** | YAML পার্সিং |
| **LWP::UserAgent** | HTTP ক্লায়েন্ট |
| **HTTP::ক্ষুদ্র** | ন্যূনতম HTTP ক্লায়েন্ট |
| **IO::সকেট::SSL** | SSL/TLS |
| **সমান্তরাল::ফর্ক ম্যানেজার** | সমান্তরাল প্রক্রিয়াকরণ |
| **MCE** | বহু-কোর ইঞ্জিন |
| **চেষ্টা করুন::ক্ষুদ্র** | ব্যতিক্রম হ্যান্ডলিং |
| **পথ::ক্ষুদ্র** | ফাইল পাথ |
| **তালিকা::Util** | তালিকা ইউটিলিটি |
| **স্ক্যালার::ইউটিল** | স্কেলার ইউটিলিটি |
| **তারিখ সময়** | তারিখ/সময় পরিচালনা |
| **লগ::যেকোনো** | লগিং সম্মুখভাগ |
| **কনফিগ::যেকোনো** | কনফিগারেশন |
---

## টেক্সট প্রসেসিং
| টুল | উদ্দেশ্য |
|---------|---------|
| **নিয়মিত অভিব্যক্তি** | অন্তর্নির্মিত, শক্তিশালী |
| **টেমপ্লেট::টুলকিট** | টেমপ্লেট ইঞ্জিন |
| **টেক্সট::CSV** | CSV পার্সিং |
| **XML::LibXML** | XML প্রক্রিয়াকরণ |
| **মোজো::ডোম** | HTML/XML পার্সিং |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **ভিএস কোড + পার্ল** | পার্ল ভাষা সমর্থন |
| **ভিম-পার্ল** | ভিম পার্ল সমর্থন |
| **Emacs + cperl-মোড** | ক্লাসিক পার্ল পরিবেশ |
| **কোমোডো** | ActiveState পার্ল IDE |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **স্টারম্যান** | PSGI ওয়েব সার্ভার |
| **হিপনোটোড** | মোজোলিসিয়াস সার্ভার |
| **ডকার** | কন্টেইনারাইজড |
| **PAR::Packer** | স্বতন্ত্র এক্সিকিউটেবল |
| **কার্টন** | বান্ডিল নির্ভরতা |
| **cpanfile + শক্ত কাগজ** | প্রজননযোগ্য স্থাপনা |
---

## সারাংশ
CPAN হোস্টিং 200,000+ মডিউল সহ পার্লের ইকোসিস্টেম বিশাল এবং পরিপক্ক। স্ট্যান্ডার্ড স্ট্যাক হল: রানটাইম হিসাবে **Perl 5.38+**, প্যাকেজের জন্য **cpanm**, ওয়েবের জন্য **Mojolicious**, **DBI** + **DBIx::Class** ডেটাবেসের জন্য, **Test2::Suite** পরীক্ষার জন্য, **perlcritic** linting-এর জন্য এবং **perlttidy-এর জন্য। পার্ল টেক্সট প্রসেসিং, সিস্টেম অ্যাডমিনিস্ট্রেশন, বায়োইনফরমেটিক্স, এবং লিগ্যাসি ওয়েব অ্যাপ্লিকেশনগুলিতে পারদর্শী। স্বাক্ষর, পোস্টফিক্স ডিরেফারেন্স এবং চেষ্টা/ক্যাচ সহ আধুনিক পার্ল (5.38+) এটির খ্যাতির পরামর্শের চেয়ে উল্লেখযোগ্যভাবে পরিষ্কার। ইকোসিস্টেমটি সিসাডমিন স্ক্রিপ্টিং, ডেটা প্রসেসিং এবং দ্রুত প্রোটোটাইপিংয়ের জন্য আদর্শ।