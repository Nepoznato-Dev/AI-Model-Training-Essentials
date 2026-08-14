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
# Perl — 생태계 및 툴링 가이드
이 가이드는 Perl 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## 펄 버전
| 버전 | 메모 |
|---------|---------|
| **펄 5.38+** | 현재 안정 |
| **펄 5.40** | 새로운 기능을 갖춘 최신 |
| **라쿠(Perl 6)** | 현대적인 재설계(별도의 언어) |
| **무스** | 현대적인 OO 시스템 |
| **무** | 경량 무스 |
```bash
perl -v                   # check version
perl script.pl            # run script
perl -e 'print "Hello\n"' # inline execution
perlbrew list             # manage Perl versions
perlbrew install 5.40.0   # install version
```

---

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **CPAN** | 포괄적인 Perl 아카이브 네트워크(200,000개 이상의 모듈) |
| **cpanm** | 경량 CPAN 설치 프로그램 |
| **cpanfile** | 종속성 선언 |
| **판지** | 종속성 번들러(예: 번들러) |
| **거리::질라** | 유통 빌더 |
| **앱::cpanminus** | 최소 CPAN 클라이언트 |
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

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **모졸리셔스** | 풀스택 | 현대적이고 깨끗하며 배터리 포함 |
| **댄서2** | 마이크로 | Sinatra와 유사한 경량 |
| **촉매** | 풀스택 | 엔터프라이즈, MVC |
| **플랙** | PSGI 툴킷 | 낮은 수준의 웹 인터페이스 |
| **스타맨** | HTTP 서버 | PSGI 서버 |
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

## 데이터베이스
| 기술 | 유형 |
|------------|------|
| **DBI** | 데이터베이스 인터페이스 표준 |
| **DBD::SQLite** | SQLite 드라이버 |
| **DBD::Pg** | PostgreSQL 드라이버 |
| **DBD::mysql** | MySQL 드라이버 |
| **DBIx::클래스** | 전체 ORM |
| **모조::Pg** | PostgreSQL(모졸리셔스) |
| **레디스** | Redis 클라이언트 |
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

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **테스트::자세히** | 표준 테스트 프레임워크 |
| **테스트2::스위트** | 최신 테스트(권장) |
| **테스트::치명적** | 예외 테스트 |
| **테스트::모의모듈** | 조롱 |
| **테스트::깊은** | 복잡한 데이터 비교 |
| **테스트::출력** | STDOUT/STDERR 캡처 |
| **증명** | 테스트러너 |
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

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **펄크리틱** | 코드 린팅 및 스타일 |
| **변덕** | 코드 서식 |
| **개발::표지** | 코드 적용 범위 |
| **펄::비평가** | 정책 시행 |
| **테스트::Perl::비평가** | 테스트 비평가 |
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

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **무스 / 무** | 현대 개체 시스템 |
| **모졸리셔스** | 웹 프레임워크 |
| **DBI** | 데이터베이스 인터페이스 |
| **DBIx::클래스** | ORM |
| **JSON::XS / C패널::JSON::XS** | JSON 구문 분석 |
| **YAML::XS** | YAML 구문 분석 |
| **LWP::UserAgent** | HTTP 클라이언트 |
| **HTTP::작음** | 최소 HTTP 클라이언트 |
| **IO::소켓::SSL** | SSL/TLS |
| **병렬::ForkManager** | 병렬 처리 |
| **MCE** | 다중 코어 엔진 |
| **해 보세요::작습니다** | 예외 처리 |
| **경로::Tiny** | 파일 경로 |
| **목록::유틸리티** | 유틸리티 나열 |
| **스칼라::Util** | 스칼라 유틸리티 |
| **날짜시간** | 날짜/시간 처리 |
| **로그::모두** | 로깅 외관 |
| **구성::모두** | 구성 |
---

## 텍스트 처리
| 도구 | 목적 |
|---------|---------|
| **정규 표현식** | 내장형, 강력한 |
| **템플릿::툴킷** | 템플릿 엔진 |
| **텍스트::CSV** | CSV 파싱 |
| **XML::LibXML** | XML 처리 |
| **모조::DOM** | HTML/XML 구문 분석 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **VS 코드 + 펄** | Perl 언어 지원 |
| **vim-펄** | 빔 펄 지원 |
| **Emacs + cperl 모드** | 클래식 Perl 환경 |
| **코모도** | 액티브스테이트 펄 IDE |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **스타맨** | PSGI 웹 서버 |
| **최면두꺼비** | 모졸리셔스 서버 |
| **도커** | 컨테이너화 |
| **PAR::패커** | 독립형 실행 파일 |
| **판지** | 번들 종속성 |
| **cpanfile + 상자** | 재현 가능한 배포 |
---

## 요약
Perl의 생태계는 CPAN이 200,000개 이상의 모듈을 호스팅하는 방대하고 성숙합니다. 표준 스택은 런타임용 **Perl 5.38+**, 패키지용 **cpanm**, 웹용 **Mojolicious**, 데이터베이스용 **DBI** + **DBIx::Class**, 테스트용 **Test2::Suite**, Linting용 **perlcritic**, 서식 지정용 **perltidy**입니다. Perl은 텍스트 처리, 시스템 관리, 생물정보학 및 레거시 웹 애플리케이션에 탁월합니다. 서명, 후위 역참조 및 try/catch를 갖춘 최신 Perl(5.38+)은 평판에서 알 수 있는 것보다 훨씬 깔끔합니다. 생태계는 시스템 관리 스크립팅, 데이터 처리 및 신속한 프로토타이핑에 이상적입니다.