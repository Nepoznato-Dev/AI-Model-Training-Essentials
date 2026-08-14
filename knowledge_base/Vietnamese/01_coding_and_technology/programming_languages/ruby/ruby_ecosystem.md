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

# Ruby — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Ruby.
---

## Triển khai Ruby
| Thực hiện | Ghi chú |
|--------------|-------|
| **CRuby (MRI)** | Mặc định, được sử dụng rộng rãi nhất |
| **JRuby** | Tương tác Java, dựa trên JVM |
| **TruffleRuby** | Dựa trên GraalVM, hiệu suất cao |
| **mruby** | Nhẹ, có thể nhúng |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## Quản lý gói
| Công cụ | Mục đích |
|------|----------|
| **RubyGem** | Trình quản lý gói đá quý tích hợp |
| **Bộ gói** | Quản lý phụ thuộc (Gemfile) |
| **rubygems.org** | Kho đá quý chính thức |
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

## Khung web
| Khung | Loại | Tốt nhất cho |
|----------|------|----------|
| **Đường ray** | Toàn ngăn xếp | Quy ước về cấu hình |
| **Sinatra** | Vi mô | API đơn giản, ứng dụng nhỏ |
| **Hanami** | Vòm sạch. | Ứng dụng có thể bảo trì, có thể kiểm tra |
| **Roda** | Cây định tuyến | Hiệu suất cao, linh hoạt |
| **Nho** | API REST | Khung tập trung vào API |
| **Giá đỡ** | Giao diện | Giao diện máy chủ web cấp thấp |
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

## Cơ sở dữ liệu & ORM
| Công nghệ | Loại |
|----------||------|
| **Bản ghi hoạt động** | Rails ORM (dựa trên quy ước) |
| **Phần tiếp theo** | ORM linh hoạt, mạnh mẽ |
| **ROM (Trình ánh xạ đối tượng Ruby)** | Chức năng, có thể kết hợp |
| **trang** | Bộ điều hợp PostgreSQL |
| **mysql2** | Bộ chuyển đổi MySQL |
| **SQLite3** | Bộ chuyển đổi SQLite |
| **Mongoid** | MongoDB ODM |
| **Làm lại** | Lưu trữ khóa-giá trị |
---

##Thử nghiệm
| Khung | Mục đích |
|----------||----------|
| **RSpec** | Thử nghiệm kiểu BDD (phổ biến nhất) |
| **Tối thiểu** | Tích hợp, nhẹ |
| **Capybara** | Tích hợp/thử nghiệm trình duyệt |
| **FactoryBot** | Nhà máy dữ liệu thử nghiệm |
| **Kẻ giả mạo** | Tạo dữ liệu giả mạo |
| **WebMock** | Sơ khai yêu cầu HTTP |
| **SimpleCov** | Bảo hiểm mã |
| **VCR** | Ghi/phát lại các tương tác HTTP |
| **Timecop** | Thao tác thời gian trong các bài kiểm tra |
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

## Chất lượng mã
| Công cụ | Mục đích |
|------|----------|
| **RuboCop** | Linter và định dạng |
| **RB tiêu chuẩn** | Cấu hình RuboCop có ý kiến ​​|
| **Hôi** | Phát hiện mùi mã |
| **Người phanh** | Máy quét lỗ hổng bảo mật |
| **Kiểm toán gói** | Trình kiểm tra lỗ hổng đá quý |
| **SimpleCov** | Bảo hiểm mã |
| **Ảnh chụp năng lượng mặt trời** | Máy chủ ngôn ngữ, tài liệu YARD |
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

## Người chạy tác vụ & CLI
| Công cụ | Mục đích |
|------|----------|
| **Cào** | Người chạy tác vụ (Make-like) |
| **Thor** | Khung CLI |
| **Bảng điều khiển Rails** | Môi trường Rails tương tác |
| **Thor** | Xây dựng các công cụ CLI mạnh mẽ |
| **Chạy khô** | Kiểm tra đá quý CLI |
---

## Thư viện chính
| Thư viện | Mục đích |
|----------|----------|
| **Đường ray** | Khung web đầy đủ |
| **Bên cạnh** | Xử lý công việc nền |
| **Đưa ra** | Xác thực |
| **Bác học** | Ủy quyền |
| **Puma** | Máy chủ web |
| **Giá đỡ** | Giao diện máy chủ web |
| **Nokogiri** | Phân tích cú pháp HTML/XML |
| **Faraday** | Máy khách HTTP |
| **httparty** | Yêu cầu HTTP đơn giản |
| **Hỗ trợ tích cực** | Các lớp tiện ích (Rails) |
| **Rb khô** | Thư viện Ruby chức năng |
| **Hanami::Công dụng** | Tiện ích nhẹ |
| **Cẩn thận** | Bảng điều khiển / trình gỡ lỗi dành cho nhà phát triển |
| **dotenv** | Biến môi trường |
| **hình** | Cấu hình ứng dụng |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **RubyMine** | JetBrains Ruby IDE đầy đủ |
| **Mã VS + Solargraph** | Nhẹ, dựa trên LSP |
| **Vim/Neovim + ruby-lsp** | Dựa trên thiết bị đầu cuối |
| **TextMate** | Trình chỉnh sửa macOS cổ điển |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Puma** | Máy chủ web Rails mặc định |
| **Hành khách** | Mô-đun Apache/Nginx |
| **Capistrano** | Triển khai đa máy chủ từ xa |
| **Docker** | Triển khai trong container |
| **Heroku** | PaaS (Thân thiện với Ruby) |
| **Fly.io** | Nền tảng lưu trữ ứng dụng |
| **Đường sắt** | PaaS hiện đại |
| **Kamal (Căn cứ)** | Triển khai dựa trên Docker |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## Bản tóm tắt
Hệ sinh thái của Ruby tập trung vào sự hài lòng của nhà phát triển và quy ước về cấu hình. Ngăn xếp tiêu chuẩn là: **Ruby 3.3+** làm thời gian chạy, **Bundler** cho các phần phụ thuộc, **Rails** cho web toàn ngăn xếp (hoặc **Sinatra** cho các ứng dụng vi mô), **RSpec** cho thử nghiệm, **RuboCop** cho linting, **Sidekiq** cho các tác vụ nền và **Puma** làm máy chủ web. Ruby vượt trội trong việc tạo mẫu nhanh, ứng dụng web, viết kịch bản và các công cụ CLI. Hệ sinh thái RubyGems có hơn 170.000 gói. Ruby 3.x mang đến Ractors để xử lý đồng thời, RBS để gõ tĩnh và khớp mẫu.