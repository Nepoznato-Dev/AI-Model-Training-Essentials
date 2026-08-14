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

# पर्ल - इकोसिस्टम और टूलींग गाइड
यह मार्गदर्शिका पर्ल पारिस्थितिकी तंत्र में आवश्यक उपकरण, ढांचे और बुनियादी ढांचे को शामिल करती है।
---

## पर्ल संस्करण
| संस्करण | नोट्स |
|------|-------|
| **पर्ल 5.38+** | वर्तमान स्थिर |
| **पर्ल 5.40** | नई सुविधाओं के साथ नवीनतम |
| **राकू (पर्ल 6)** | आधुनिक रीडिज़ाइन (अलग भाषा) |
| **मूस** | आधुनिक OO प्रणाली |
| **मू** | हल्का मूस |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **सीपीएएन** | व्यापक पर्ल आर्काइव नेटवर्क (200,000+ मॉड्यूल) |
| **cpanm** | हल्के वजन वाला सीपीएएन इंस्टॉलर |
| **cpanfile** | निर्भरता घोषणा |
| **कार्टन** | निर्भरता बंडलर (बंडलर की तरह) |
| **जिला::जिला** | वितरण निर्माता |
| **ऐप::cpanminus** | न्यूनतम सीपीएएन क्लाइंट |
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

## वेब फ्रेमवर्क
| ढाँचा | प्रकार | के लिए सर्वश्रेष्ठ |
|--------|------|-------|
| **मोजोलिशियस** | फुल-स्टैक | आधुनिक, स्वच्छ, बैटरी सहित |
| **डांसर2** | सूक्ष्म | सिनात्रा जैसा, हल्का |
| **उत्प्रेरक** | फुल-स्टैक | एंटरप्राइज़, एमवीसी |
| **प्लैक** | पीएसजीआई टूलकिट | निम्न-स्तरीय वेब इंटरफ़ेस |
| **स्ट्रैटन** | HTTP सर्वर | पीएसजीआई सर्वर |
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

## डेटाबेस
| प्रौद्योगिकी | प्रकार |
|------|------|
| **डीबीआई** | डेटाबेस इंटरफ़ेस मानक |
| **डीबीडी::एसक्यूलाइट** | SQLite ड्राइवर |
| **डीबीडी::पीजी** | PostgreSQL ड्राइवर |
| **DBD::mysql** | MySQL ड्राइवर |
| **DBIx::क्लास** | पूर्ण ओआरएम |
| **मोजो::पृ** | पोस्टग्रेएसक्यूएल (मोजोलिशियस) |
| **रेडिस** | रेडिस क्लाइंट |
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

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **टेस्ट::अधिक** | मानक परीक्षण रूपरेखा |
| **टेस्ट2::सुइट** | आधुनिक परीक्षण (अनुशंसित) |
| **परीक्षण::घातक** | अपवाद परीक्षण |
| **टेस्ट::मॉकमॉड्यूल** | उपहास |
| **परीक्षण::गहरा** | जटिल डेटा तुलना |
| **टेस्ट::आउटपुट** | STDOUT/STDERR कैप्चर करें |
| **साबित** | टेस्ट धावक |
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

## कोड गुणवत्ता
| उपकरण | उद्देश्य |
|------|---------|
| **पर्लक्रिटिक** | कोड लिंटिंग और स्टाइल |
| **perltidy** | कोड फ़ॉर्मेटिंग |
| **डेवेल::कवर** | कोड कवरेज |
| **पर्ल::आलोचक** | नीति प्रवर्तन |
| **टेस्ट::पर्ल::क्रिटिक** | परीक्षणों में आलोचक |
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

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **मूस/मू** | आधुनिक वस्तु प्रणाली |
| **मोजोलिशियस** | वेब ढाँचा |
| **डीबीआई** | डेटाबेस इंटरफ़ेस |
| **DBIx::क्लास** | ओआरएम |
| **JSON::XS / Cpanel::JSON::XS** | JSON पार्सिंग |
| **YAML::XS** | YAML पार्सिंग |
| **LWP::UserAgent** | HTTP क्लाइंट |
| **HTTP::छोटा** | न्यूनतम HTTP क्लाइंट |
| **आईओ::सॉकेट::एसएसएल** | एसएसएल/टीएलएस |
| **समानांतर::फोर्कमैनेजर** | समानांतर प्रसंस्करण |
| **एमसीई** | कई-कोर इंजन |
| **कोशिश करें::छोटा** | अपवाद हैंडलिंग |
| **पथ::छोटा** | फ़ाइल पथ |
| **सूची::उपयोग** | उपयोगिताओं की सूची |
| **अदिश::उपयोग** | अदिश उपयोगिताएँ |
| **दिनांकसमय** | दिनांक/समय प्रबंधन |
| **लॉग::कोई भी** | लॉगिंग मुखौटा |
| **कॉन्फिग::कोई भी** | विन्यास |
---

## टेक्स्ट प्रोसेसिंग
| उपकरण | उद्देश्य |
|---------|---------|
| **नियमित अभिव्यक्ति** | अंतर्निर्मित, शक्तिशाली |
| **टेम्पलेट::टूलकिट** | टेम्पलेट इंजन |
| **पाठ::CSV** | सीएसवी पार्सिंग |
| **XML::LibXML** | एक्सएमएल प्रोसेसिंग |
| **मोजो::डोम** | HTML/XML पार्सिंग |
---

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **वीएस कोड + पर्ल** | पर्ल भाषा समर्थन |
| **विम-पर्ल** | विम पर्ल समर्थन |
| **Emacs + cperl-मोड** | क्लासिक पर्ल पर्यावरण |
| **कोमोडो** | एक्टिवस्टेट पर्ल आईडीई |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **स्ट्रैटन** | पीएसजीआई वेब सर्वर |
| **सम्मोहन** | मस्त सर्वर |
| **डॉकर** | कंटेनरीकृत |
| **PAR::पैकर** | स्टैंडअलोन निष्पादनयोग्य |
| **कार्टन** | बंडल निर्भरताएँ |
| **cpanfile + कार्टन** | प्रतिलिपि प्रस्तुत करने योग्य परिनियोजन |
---

## सारांश
पर्ल का पारिस्थितिकी तंत्र विशाल और परिपक्व है, जिसमें सीपीएएन 200,000+ मॉड्यूल की मेजबानी करता है। मानक स्टैक है: ** रनटाइम के रूप में पर्ल 5.38+**, पैकेज के लिए **cpanm**, वेब के लिए **मोजोलिशियस**, डेटाबेस के लिए **DBI** + **DBIx::Class**, परीक्षण के लिए **Test2::Suite**, लिंटिंग के लिए **perlcritic** और फ़ॉर्मेटिंग के लिए **perltidy**। पर्ल टेक्स्ट प्रोसेसिंग, सिस्टम एडमिनिस्ट्रेशन, बायोइनफॉरमैटिक्स और लीगेसी वेब अनुप्रयोगों में उत्कृष्टता प्राप्त करता है। आधुनिक पर्ल (5.38+) हस्ताक्षर, पोस्टफिक्स डीरेफरेंस और ट्राई/कैच के साथ अपनी प्रतिष्ठा से काफी साफ-सुथरा है। पारिस्थितिकी तंत्र सिस्टम एडमिन स्क्रिप्टिंग, डेटा प्रोसेसिंग और रैपिड प्रोटोटाइपिंग के लिए आदर्श है।