---
# Metadata
title: "Ruby — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ruby ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ruby, ecosystem, tooling, rails, gems, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# Ruby — 생태계 및 툴링 가이드
이 가이드에서는 Ruby 생태계의 필수 도구, 프레임워크 및 인프라를 다룹니다.
---

## Ruby 구현
| 구현 | 메모 |
|---------------|-------|
| **크루비(MRI)** | 기본값, 가장 널리 사용됨 |
| **J루비** | JVM 기반, Java 상호 운용성 |
| **트러플루비** | GraalVM 기반, 고성능 |
| **루비** | 경량, 내장 가능 |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## 패키지 관리
| 도구 | 목적 |
|------|---------|
| **RubyGems** | 내장 보석 패키지 관리자 |
| **번들러** | 종속성 관리(Gemfile) |
| **rubygems.org** | 공식 보석 저장소 |
```ruby
# Gemfile
source "https://rubygems.org"

gem "rails", "~> 7.1"
gem "pg", "~> 1.5"
gem "puma", "~> 6.0"
gem "redis", "~> 5.0"

group :development, :test do
  gem "rspec", "~> 3.12"
  gem "rubocop", "~> 1.50"
  gem "debug"
end
```

```bash
bundle install          # install dependencies
bundle update           # update gems
bundle exec rspec       # run with bundled gems
```

---

## 웹 프레임워크
| 프레임워크 | 유형 | 최고의 대상 |
|------------|------|----------|
| **레일** | 풀스택 | 구성에 대한 규칙 |
| **시나트라** | 마이크로 | 간단한 API, 작은 앱 |
| **하나미** | 아치를 청소하세요. | 유지 관리 및 테스트 가능한 앱 |
| **로다** | 라우팅 트리 | 고성능, 유연성 |
| **포도** | REST API | API 중심 프레임워크 |
| **랙** | 인터페이스 | 낮은 수준의 웹 서버 인터페이스 |
```ruby
# Sinatra example
require "sinatra"

get "/hello" do
  "Hello, #{params[:name] || 'World'}!"
end

get "/users/:id" do
  user = User.find(params[:id])
  json user
end
```

```ruby
# Rails controller example
class UsersController < ApplicationController
  def index
    @users = User.order(:name).page(params[:page])
    render json: @users
  end

  def create
    @user = User.new(user_params)
    if @user.save
      render json: @user, status: :created
    else
      render json: @user.errors, status: :unprocessable_entity
    end
  end
end
```

---

## 데이터베이스 및 ORM
| 기술 | 유형 |
|------------|------|
| **활성 레코드** | Rails ORM(컨벤션 기반) |
| **속편** | 유연하고 강력한 ORM |
| **ROM(루비 객체 매퍼)** | 기능성, 구성 가능 |
| **pg** | PostgreSQL 어댑터 |
| **mysql2** | MySQL 어댑터 |
| **SQLite3** | SQLite 어댑터 |
| **몽고이드** | 몽고DB ODM |
| **레디스** | 키-값 저장소 |
---

## 테스트
| 프레임워크 | 목적 |
|------------|---------|
| **RSpec** | BDD 스타일 테스트(가장 인기 있음) |
| **미니테스트** | 내장형, 경량 |
| **카피바라** | 통합/브라우저 테스트 |
| **팩토리봇** | 테스트 데이터 팩토리 |
| **페이커** | 가짜 데이터 생성 |
| **웹모크** | HTTP 요청 스텁 |
| **SimpleCov** | 코드 적용 범위 |
| **VCR** | HTTP 상호 작용 기록/재생 |
| **타임캅** | 테스트 중 시간 조작 |
```ruby
# RSpec example
RSpec.describe UserService do
  subject(:service) { described_class.new(repository) }

  describe "#find" do
    it "returns the user when found" do
      user = build(:user, name: "Alice")
      allow(repository).to receive(:find).with(1).and_return(user)

      result = service.find(1)

      expect(result.name).to eq("Alice")
    end

    it "raises NotFound when missing" do
      allow(repository).to receive(:find).and_raise(NotFound)

      expect { service.find(999) }.to raise_error(NotFound)
    end
  end
end
```

---

## 코드 품질
| 도구 | 목적 |
|------|---------|
| **루보캅** | 린터 및 포맷터 |
| **표준RB** | 독선적인 RuboCop 구성 |
| **악취** | 코드 냄새 감지 |
| **브레이크맨** | 보안 취약점 스캐너 |
| **번들러 감사** | 보석 취약점 검사기 |
| **SimpleCov** | 코드 적용 범위 |
| **태양전지** | 언어 서버, YARD 문서 |
```yaml
# .rubocop.yml
AllCops:
  TargetRubyVersion: 3.3
  NewCops: enable

Style/Documentation:
  Enabled: false

Layout/LineLength:
  Max: 120
```

---

## 작업 실행기 및 CLI
| 도구 | 목적 |
|------|---------|
| **갈퀴** | 태스크러너(Make-like) |
| **토르** | CLI 프레임워크 |
| **레일 콘솔** | 인터랙티브 레일스 환경 |
| **토르** | 강력한 CLI 도구 구축 |
| **드라이런** | gem CLI 테스트 |
---

## 주요 라이브러리
| 도서관 | 목적 |
|---------|---------|
| **레일** | 풀스택 웹 프레임워크 |
| **사이드킥** | 백그라운드 작업 처리 |
| **구상** | 인증 |
| **전문가** | 승인 |
| **푸마** | 웹 서버 |
| **랙** | 웹 서버 인터페이스 |
| **노코기리** | HTML/XML 구문 분석 |
| **패러데이** | HTTP 클라이언트 |
| **http파티** | 단순 HTTP 요청 |
| **활성지원** | 유틸리티 클래스(레일) |
| **드라이-RB** | 기능적인 Ruby 라이브러리 |
| **하나미::Utils** | 경량 유틸리티 |
| **프라이** | 개발자 콘솔/디버거 |
| **도텐브** | 환경 변수 |
| **피가로** | 앱 구성 |
---

## IDE 및 편집기
| IDE | 강점 |
|------|------------|
| **루비마인** | 전체 JetBrains Ruby IDE |
| **VS 코드 + 태양광 그래프** | 경량, LSP 기반 |
| **Vim/Neovim + ruby-lsp** | 터미널 기반 |
| **텍스트메이트** | 클래식 macOS 편집기 |
---

## 배포
| 방법 | 메모 |
|---------|-------|
| **푸마** | 기본 Rails 웹 서버 |
| **승객** | Apache/Nginx 모듈 |
| **카피스트라노** | 원격 다중 서버 배포 |
| **도커** | 컨테이너화된 배포 |
| **헤로쿠** | PaaS(Ruby 친화적) |
| **플라이.io** | 앱 호스팅 플랫폼 |
| **철도** | 최신 PaaS |
| **카말(베이스캠프)** | Docker 기반 배포 |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## 요약
Ruby 생태계는 개발자의 행복과 구성에 대한 관례에 중점을 두고 있습니다. 표준 스택은 런타임용 **Ruby 3.3+**, 종속성용 **Bundler**, 전체 스택 웹용 **Rails**(또는 마이크로 앱용 **Sinatra**), 테스트용 **RSpec**, Linting용 **RuboCop**, 백그라운드 작업용 **Sidekiq**, 웹 서버용 **Puma**입니다. Ruby는 신속한 프로토타이핑, 웹 애플리케이션, 스크립팅 및 CLI 도구에 탁월합니다. RubyGems 생태계에는 170,000개 이상의 패키지가 있습니다. Ruby 3.x는 동시성을 위한 Ractor, 정적 타이핑 및 패턴 일치를 위한 RBS를 제공합니다.