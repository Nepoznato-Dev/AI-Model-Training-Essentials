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

# Ruby — Ekosistem ve Araç Kullanma Kılavuzu
Bu kılavuz Ruby ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Ruby Uygulamaları
| Uygulama | Notlar |
|---------------|----------|
| **CRuby (MRI)** | Varsayılan, en yaygın kullanılan |
| **JRuby** | JVM tabanlı, Java birlikte çalışma |
| **TruffleYakut** | GraalVM tabanlı, yüksek performanslı |
| **mruby** | Hafif, yerleştirilebilir |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **RubyGems** | Yerleşik mücevher paket yöneticisi |
| **Paketleyici** | Bağımlılık yönetimi (Gemfile) |
| **rubygems.org** | Resmi mücevher deposu |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Raylar** | Tam yığın | Yapılandırmaya ilişkin kural |
| **Sinatra** | Mikro | Basit API'ler, küçük uygulamalar |
| **Hanami** | Kemeri temizleyin. | Bakımı yapılabilir, test edilebilir uygulamalar |
| **Roda** | Yönlendirme ağacı | Yüksek performanslı, esnek |
| **Üzüm** | REST API'si | API odaklı çerçeve |
| **Raf** | Arayüz | Düşük seviyeli web sunucusu arayüzü |
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

## Veritabanı ve ORM
| Teknoloji | Tür |
|---------------|------|
| **Aktif Kayıt** | Raylar ORM (kurallara dayalı) |
| **Devam filmi** | Esnek, güçlü ORM |
| **ROM (Ruby Nesne Eşleyicisi)** | İşlevsel, şekillendirilebilir |
| **sayfa** | PostgreSQL bağdaştırıcısı |
| **mysql2** | MySQL bağdaştırıcısı |
| **SQLite3** | SQLite bağdaştırıcısı |
| **Mongoid** | MongoDB ODM |
| **Redis** | Anahtar/değer deposu |
---

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **RSpec** | BDD tarzı testler (en popüler) |
| **Minitest** | Yerleşik, hafif |
| **Kapibara** | Entegrasyon/tarayıcı testi |
| **FabrikaBot** | Test verileri fabrikaları |
| **Sahtekar** | Sahte veri üretimi |
| **WebMock** | HTTP isteğinin engellenmesi |
| **BasitCov** | Kod kapsamı |
| **VCR** | HTTP etkileşimlerini kaydedin/tekrar oynatın |
| **Zaman polisi** | Testlerde zaman manipülasyonu |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **RuboCop** | Linter ve biçimlendirici |
| **StandartRB** | Görüşleriniz RuboCop yapılandırması |
| **Pis koku** | Kod kokusu algılama |
| **Frenci** | Güvenlik açığı tarayıcısı |
| **Bundler denetimi** | Gem güvenlik açığı denetleyicisi |
| **BasitCov** | Kod kapsamı |
| **Güneş grafiği** | Dil sunucusu, YARD belgeleri |
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

## Görev Çalıştırıcıları ve CLI
| Araç | Amaç |
|------|------------|
| **Tırmık** | Görev çalıştırıcı (Make benzeri) |
| **Thor** | CLI çerçevesi |
| **Ray konsolu** | İnteraktif Raylar ortamı |
| **Thor** | Güçlü CLI araçları oluşturun |
| **Kuru çalıştırma** | Gem CLI'lerini test edin |
---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **Raylar** | Tam yığın web çerçevesi |
| **Sidekiq** | Arka planda iş işleme |
| **Tasarlayın** | Kimlik Doğrulama |
| **Açıklama** | Yetkilendirme |
| **Puma** | Web sunucusu |
| **Raf** | Web sunucusu arayüzü |
| **Nokogiri** | HTML/XML ayrıştırma |
| **Faraday** | HTTP istemcisi |
| **httpparti** | Basit HTTP istekleri |
| **Aktif Destek** | Fayda sınıfları (Raylar) |
| **Kuru-rb** | İşlevsel Ruby kütüphaneleri |
| **Hanami::Yardımcı Programlar** | Hafif yardımcı programlar |
| **gözetleyin** | Geliştirici konsolu / hata ayıklayıcı |
| **dotenv** | Ortam değişkenleri |
| **figaro** | Uygulama yapılandırması |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **RubyMine** | Tam JetBrains Ruby IDE |
| **VS Kodu + Solargraf** | Hafif, LSP tabanlı |
| **Vim/Neovim + ruby-lsp** | Terminal tabanlı |
| **Metin Arkadaşı** | Klasik macOS düzenleyici |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Puma** | Varsayılan Rails web sunucusu |
| **Yolcu** | Apache/Nginx modülü |
| **Capistrano** | Uzaktan çoklu sunucu dağıtımı |
| **Docker** | Konteynerli dağıtım |
| **Heroku** | PaaS (Ruby dostu) |
| **Fly.io** | Uygulama barındırma platformu |
| **Demiryolu** | Modern PaaS |
| **Kamal (Basecamp)** | Docker tabanlı dağıtım |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Özet
Ruby'nin ekosistemi, yapılandırmadan ziyade geliştirici mutluluğu ve gelenek üzerine kuruludur. Standart yığın şunlardır: Çalışma zamanı olarak **Ruby 3.3+**, bağımlılıklar için **Bundler**, tam yığın web için **Rails** (veya mikro uygulamalar için **Sinatra**), test için **RSpec**, linting için **RuboCop**, arka plan işleri için **Sidekiq** ve web sunucusu olarak **Puma**. Ruby hızlı prototipleme, web uygulamaları, komut dosyası oluşturma ve CLI araçlarında uzmandır. RubyGems ekosisteminde 170.000'den fazla paket bulunmaktadır. Ruby 3.x, eşzamanlılık için Ractors'ı, statik yazma için RBS'yi ve desen eşleştirmeyi getiriyor.