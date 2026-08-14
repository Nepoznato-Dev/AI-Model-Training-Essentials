---
# Metadata
title: "Ruby — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ruby ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
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
# Ruby — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Ruby.
---

## Implementasi Ruby
| Implementasi | Catatan |
|---------------|-------|
| **CRuby (MRI)** | Default, paling banyak digunakan |
| **JRuby** | Interop Java berbasis JVM |
| **TruffleRuby** | Berbasis GraalVM, kinerja tinggi |
| **mruby** | Ringan, dapat disematkan |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **Permata Ruby** | Manajer paket permata bawaan |
| **Bundler** | Manajemen ketergantungan (Gemfile) |
| **rubygems.org** | Repositori permata resmi |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Rel** | Tumpukan penuh | Konvensi mengenai konfigurasi |
| **Sinatra** | Mikro | API sederhana, aplikasi kecil |
| **Hanami** | Lengkungan bersih. | Aplikasi yang dapat dipelihara dan diuji |
| **Roda** | Pohon perutean | Performa tinggi, fleksibel |
| **Anggur** | API REST | Kerangka kerja yang berfokus pada API |
| **Rak** | Antarmuka | Antarmuka server web tingkat rendah |
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

## Basis Data & ORM
| Teknologi | Ketik |
|------------|------|
| **Rekaman Aktif** | Rails ORM (berbasis konvensi) |
| **Sekuel** | ORM yang fleksibel dan kuat |
| **ROM (Pemeta Objek Ruby)** | Fungsional, dapat disusun |
| **hal** | Adaptor PostgreSQL |
| **mysql2** | Adaptor MySQL |
| **SQLite3** | Adaptor SQLite |
| **Mongoid** | MongoDB ODM |
| **Redis** | Penyimpanan nilai kunci |
---

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Spesifikasi RS** | Pengujian gaya BDD (paling populer) |
| **Terkecil** | Bawaan, ringan |
| **Kapibara** | Pengujian integrasi/browser |
| **Bot Pabrik** | Pabrik data uji |
| **Pemalsu** | Pembuatan data palsu |
| **WebMock** | Permintaan HTTP terhenti |
| **SederhanaCov** | Cakupan kode |
| **VCR** | Rekam/putar ulang interaksi HTTP |
| **Jadwal** | Manipulasi waktu dalam tes |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **RuboCop** | Linter dan pemformat |
| **RBStandar** | Konfigurasi RuboCop yang disetujui |
| **Bau** | Deteksi bau kode |
| **Tukang Rem** | Pemindai kerentanan keamanan |
| **Audit bundel** | Pemeriksa kerentanan permata |
| **SederhanaCov** | Cakupan kode |
| **Grafik Surya** | Server bahasa, dokumen YARD |
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

## Pelari Tugas & CLI
| Alat | Tujuan |
|------|---------|
| **Raih** | Pelari tugas (Buat seperti) |
| **Thor** | Kerangka CLI |
| **Konsol rel** | Lingkungan Rails Interaktif |
| **Thor** | Bangun alat CLI yang kuat |
| **Pengeringan** | Uji permata CLI |
---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **Rel** | Kerangka web tumpukan penuh |
| **Sidekiq** | Pemrosesan pekerjaan latar belakang |
| **Rancangan** | Otentikasi |
| **Pakar** | Otorisasi |
| **Puma** | Server web |
| **Rak** | Antarmuka server web |
| **Nokogiri** | Penguraian HTML/XML |
| **Faraday** | Klien HTTP |
| **pesta http** | Permintaan HTTP sederhana |
| **Dukungan Aktif** | Kelas utilitas (Rel) |
| **Kering-rb** | Perpustakaan Ruby fungsional |
| **Hanami::Utilitas** | Utilitas ringan |
| **Cungkil** | Konsol pengembang / debugger |
| **dotenv** | Variabel lingkungan |
| **figaro** | Konfigurasi aplikasi |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Tambang Ruby** | IDE Ruby JetBrains Lengkap |
| **Kode VS + Grafik Surya** | Ringan, berbasis LSP |
| **Vim/Neovim + ruby-lsp** | Berbasis terminal |
| **Teman Teks** | Editor macOS klasik |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Puma** | Server web Rails bawaan |
| **Penumpang** | Modul Apache/Nginx |
| **Capistrano** | Penerapan multi-server jarak jauh |
| **Buruh pelabuhan** | Penerapan dalam container |
| **Pahlawanku** | PaaS (ramah Ruby) |
| **Terbang.io** | Platform hosting aplikasi |
| **Kereta Api** | PaaS modern |
| **Kamal (Basecamp)** | Penerapan berbasis Docker |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Ringkasan
Ekosistem Ruby berpusat pada kebahagiaan pengembang dan konvensi atas konfigurasi. Tumpukan standarnya adalah: **Ruby 3.3+** sebagai runtime, **Bundler** untuk dependensi, **Rails** untuk web tumpukan penuh (atau **Sinatra** untuk aplikasi mikro), **RSpec** untuk pengujian, **RuboCop** untuk linting, **Sidekiq** untuk pekerjaan latar belakang, dan **Puma** sebagai server web. Ruby unggul dalam pembuatan prototipe cepat, aplikasi web, pembuatan skrip, dan alat CLI. Ekosistem RubyGems memiliki lebih dari 170.000 paket. Ruby 3.x menghadirkan Ractors untuk konkurensi, RBS untuk pengetikan statis, dan pencocokan pola.