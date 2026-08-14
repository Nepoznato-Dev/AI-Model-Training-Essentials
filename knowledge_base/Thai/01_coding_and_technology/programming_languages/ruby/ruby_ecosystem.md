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

# Ruby — คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศ Ruby
---

## การใช้งานทับทิม
| การนำไปปฏิบัติ | หมายเหตุ |
|---------|-------|
| **CRuby (MRI)** | ค่าเริ่มต้น ใช้กันอย่างแพร่หลายที่สุด |
| **เจรูบี้** | การทำงานร่วมกันของ Java บน JVM |
| **ทรัฟเฟิลรูบี้** | GraalVM ประสิทธิภาพสูง |
| **mruby** | น้ำหนักเบา ฝังได้ |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## การจัดการแพ็คเกจ
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **RubyGems** | ตัวจัดการแพ็คเกจอัญมณีในตัว |
| **บันเดิล** | การจัดการการพึ่งพา (Gemfile) |
| **rubygems.org** | แหล่งเก็บอัญมณีอย่างเป็นทางการ |
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

## กรอบงานเว็บ
| กรอบ | พิมพ์ | ดีที่สุดสำหรับ |
|----------|-|----------|
| **ราง** | เต็มกอง | แบบแผนมากกว่าการกำหนดค่า |
| **ซินาตร้า** | ไมโคร | API แบบง่าย แอปขนาดเล็ก |
| **ฮานามิ** | ซุ้มประตูที่สะอาด | แอพที่บำรุงรักษาและทดสอบได้ |
| **โรด้า** | ต้นไม้เส้นทาง | ประสิทธิภาพสูง ยืดหยุ่น |
| **องุ่น** | ส่วนที่เหลือ API | เฟรมเวิร์กที่เน้น API |
| **แร็ค** | อินเตอร์เฟซ | อินเทอร์เฟซเว็บเซิร์ฟเวอร์ระดับต่ำ |
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

## ฐานข้อมูลและ ORM
| เทคโนโลยี | พิมพ์ |
|------------|------|
| **บันทึกที่ใช้งานอยู่** | Rails ORM (ตามแบบแผน) |
| **ภาคต่อ** | ORM ที่ยืดหยุ่นและทรงพลัง |
| **ROM (ตัวทำแผนที่วัตถุ Ruby)** | ใช้งานได้จริง |
| **หน้า** | อะแดปเตอร์ PostgreSQL |
| **mysql2** | อะแดปเตอร์ MySQL |
| **SQLite3** | อะแดปเตอร์ SQLite |
| **มองโกด** | MongoDB ODM |
| **เรดิส** | ที่เก็บคีย์-ค่า |
---

## การทดสอบ
| กรอบ | วัตถุประสงค์ |
|----------|---------|
| **สเปก** | การทดสอบสไตล์ BDD (ยอดนิยมที่สุด) |
| **ขั้นต่ำ** | ในตัวน้ำหนักเบา |
| **คาปิบารา** | บูรณาการ/การทดสอบเบราว์เซอร์ |
| **FactoryBot** | ทดสอบโรงงานข้อมูล |
| **ของปลอม** | การสร้างข้อมูลปลอม |
| **เว็บจำลอง** | คำขอ HTTP สะดุด |
| **ซิมเพิลโคฟ** | ความครอบคลุมของโค้ด |
| **วีซีอาร์** | บันทึก/เล่นซ้ำการโต้ตอบ HTTP |
| **ไทม์ค็อป** | การปรับเปลี่ยนเวลาในการทดสอบ |
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

## คุณภาพรหัส
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **รูโบคอป** | Linter และฟอร์แมตเตอร์ |
| **มาตรฐานRB** | ความเห็นการกำหนดค่า RuboCop |
| **รีค** | รหัสตรวจจับกลิ่น |
| **เบรกแมน** | เครื่องสแกนช่องโหว่ด้านความปลอดภัย |
| **การตรวจสอบ Bundleler** | ตัวตรวจสอบช่องโหว่ของอัญมณี |
| **ซิมเพิลโคฟ** | ความครอบคลุมของโค้ด |
| **โซลาร์กราฟ** | เซิร์ฟเวอร์ภาษา เอกสาร YARD |
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

## นักวิ่งงานและ CLI
| เครื่องมือ | วัตถุประสงค์ |
|------|---------|
| **คราด** | นักวิ่งงาน (Make-like) |
| **ธอร์** | กรอบงาน CLI |
| **รางคอนโซล** | สภาพแวดล้อม Rails แบบโต้ตอบ |
| **ธอร์** | สร้างเครื่องมือ CLI อันทรงพลัง |
| **ดรายรัน** | ทดสอบ gem CLIs |
---

## ห้องสมุดที่สำคัญ
| ห้องสมุด | วัตถุประสงค์ |
|---------|---------|
| **ราง** | กรอบงานเว็บแบบเต็มสแต็ค |
| **ไซด์คิค** | การประมวลผลงานเบื้องหลัง |
| **ประดิษฐ์** | การรับรองความถูกต้อง |
| **บัณฑิต** | การอนุญาต |
| **เสือพูมา** | เว็บเซิร์ฟเวอร์ |
| **แร็ค** | ส่วนต่อประสานเว็บเซิร์ฟเวอร์ |
| **โนโคกิริ** | การแยกวิเคราะห์ HTML/XML |
| **ฟาราเดย์** | ไคลเอ็นต์ HTTP |
| **httpปาร์ตี้** | คำขอ HTTP แบบง่าย |
| **การสนับสนุนที่ใช้งานอยู่** | คลาสยูทิลิตี้ (Rails) |
| **ดราย-rb** | ไลบรารี Ruby ที่ใช้งานได้ |
| **ฮานามิ::ยูทิลิตี้** | ยูทิลิตี้น้ำหนักเบา |
| **แงะ** | คอนโซลนักพัฒนาซอฟต์แวร์ / ดีบักเกอร์ |
| **dotenv** | ตัวแปรสภาพแวดล้อม |
| **ฟิกาโร** | การกำหนดค่าแอป |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **รูบี้ไมน์** | JetBrains Ruby IDE แบบเต็ม |
| **VS Code + Solargraph** | น้ำหนักเบา ใช้ LSP |
| **Vim/Neovim + ruby-lsp** | บนเทอร์มินัล |
| **เท็กซ์เมท** | ตัวแก้ไข macOS แบบคลาสสิก |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **เสือพูมา** | เว็บเซิร์ฟเวอร์ Rails เริ่มต้น |
| **ผู้โดยสาร** | โมดูล Apache/Nginx |
| **คาปิสตราโน** | การปรับใช้หลายเซิร์ฟเวอร์ระยะไกล |
| **นักเทียบท่า** | การปรับใช้แบบคอนเทนเนอร์ |
| **เฮโรกุ** | PaaS (เป็นมิตรกับทับทิม) |
| **Fly.io** | แพลตฟอร์มการโฮสต์แอป |
| **ทางรถไฟ** | PaaS สมัยใหม่ |
| **คามาล (Basecamp)** | การปรับใช้แบบอิงนักเทียบท่า |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## สรุป
ระบบนิเวศของ Ruby มุ่งเน้นไปที่ความสุขของนักพัฒนาและการประชุมมากกว่าการกำหนดค่า สแต็กมาตรฐานคือ: **Ruby 3.3+** สำหรับรันไทม์, **Bundler** สำหรับการอ้างอิง, **Rails** สำหรับเว็บฟูลสแตก (หรือ **Sinatra** สำหรับแอปขนาดเล็ก), **RSpec** สำหรับการทดสอบ, **RuboCop** สำหรับ Linting, **Sidekiq** สำหรับงานพื้นหลัง และ **Puma** เป็นเว็บเซิร์ฟเวอร์ Ruby เป็นเลิศในด้านการสร้างต้นแบบอย่างรวดเร็ว เว็บแอปพลิเคชัน การเขียนสคริปต์ และเครื่องมือ CLI ระบบนิเวศ RubyGems มีแพ็คเกจมากกว่า 170,000 รายการ Ruby 3.x นำ Ractors มาใช้พร้อมกัน, RBS สำหรับการพิมพ์แบบคงที่ และการจับคู่รูปแบบ