<!--
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

-->
# রুবি — ইকোসিস্টেম এবং টুলিং গাইড
এই নির্দেশিকাটি রুবি ইকোসিস্টেমের প্রয়োজনীয় টুল, ফ্রেমওয়ার্ক এবং অবকাঠামো কভার করে।
---

## রুবি বাস্তবায়ন
| বাস্তবায়ন | নোট |
|---------------|---------|
| **ক্রুবি (MRI)** | ডিফল্ট, সর্বাধিক ব্যবহৃত |
| **JRuby** | JVM-ভিত্তিক, জাভা ইন্টারপ |
| **TruffleRuby** | GraalVM-ভিত্তিক, উচ্চ কর্মক্ষমতা |
| **মরুবি** | লাইটওয়েট, এম্বেডযোগ্য |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## প্যাকেজ ব্যবস্থাপনা
| টুল | উদ্দেশ্য |
|------|---------|
| **রুবি জেমস** | অন্তর্নির্মিত রত্ন প্যাকেজ ম্যানেজার |
| **বান্ডলার** | নির্ভরতা ব্যবস্থাপনা (জেমফাইল) |
| **rubygems.org** | অফিসিয়াল রত্ন ভান্ডার |
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

## ওয়েব ফ্রেমওয়ার্ক
| ফ্রেমওয়ার্ক | প্রকার | জন্য সেরা |
|------------|------|----------|
| **রেলস** | ফুল-স্ট্যাক | কনফিগারেশন ওভার কনভেনশন |
| **সিনাট্রা** | মাইক্রো | সাধারণ API, ছোট অ্যাপস |
| **হানামি** | পরিষ্কার খিলান। | রক্ষণাবেক্ষণযোগ্য, পরীক্ষাযোগ্য অ্যাপস |
| **রোদা** | রাউটিং গাছ | উচ্চ কর্মক্ষমতা, নমনীয় |
| **আঙ্গুর** | REST API | API-কেন্দ্রিক কাঠামো |
| **র্যাক** | ইন্টারফেস | নিম্ন-স্তরের ওয়েব সার্ভার ইন্টারফেস |
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

## ডাটাবেস এবং ওআরএম
| প্রযুক্তি | প্রকার |
|------------|------|
| **সক্রিয় রেকর্ড** | রেল ওআরএম (সম্মেলন-ভিত্তিক) |
| **সিক্যুয়েল** | নমনীয়, শক্তিশালী ORM |
| **ROM (রুবি অবজেক্ট ম্যাপার)** | কার্যকরী, রচনাযোগ্য |
| **pg** | PostgreSQL অ্যাডাপ্টার |
| **mysql2** | মাইএসকিউএল অ্যাডাপ্টার |
| **SQLite3** | SQLite অ্যাডাপ্টার |
| **মঙ্গয়েড** | MongoDB ODM |
| **রেডিস** | মূল-মূল্যের দোকান |
---

## পরীক্ষা
| ফ্রেমওয়ার্ক | উদ্দেশ্য |
|------------|---------|
| **আরএসপিক** | বিডিডি-স্টাইল টেস্টিং (সবচেয়ে জনপ্রিয়) |
| **নিম্নতম** | অন্তর্নির্মিত, লাইটওয়েট |
| **ক্যাপিবারা** | ইন্টিগ্রেশন/ব্রাউজার টেস্টিং |
| **ফ্যাক্টরিবট** | টেস্ট ডাটা কারখানা |
| **ফেকার** | জাল ডেটা জেনারেশন |
| **ওয়েবমক** | HTTP অনুরোধ স্টাবিং |
| **SimpleCov** | কোড কভারেজ |
| **ভিসিআর** | HTTP মিথস্ক্রিয়া রেকর্ড/পুনরায় চালান |
| **টাইমকপ** | পরীক্ষায় সময়ের হেরফের |
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

## কোড কোয়ালিটি
| টুল | উদ্দেশ্য |
|------|---------|
| **রুবোকপ** | লিন্টার এবং ফরম্যাটার |
| **স্ট্যান্ডার্ডআরবি** | মতামতযুক্ত RuboCop কনফিগারেশন |
| **রিক** | কোড গন্ধ সনাক্তকরণ |
| **ব্রেকম্যান** | নিরাপত্তা দুর্বলতা স্ক্যানার |
| **বান্ডলার-অডিট** | মণি দুর্বলতা পরীক্ষক |
| **SimpleCov** | কোড কভারেজ |
| **সোলারগ্রাফ** | ভাষা সার্ভার, YARD ডক্স |
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

## টাস্ক রানার এবং CLI
| টুল | উদ্দেশ্য |
|------|---------|
| **রেক** | টাস্ক রানার (মেক-লাইক) |
| **থর** | CLI ফ্রেমওয়ার্ক |
| **রেল কনসোল** | ইন্টারেক্টিভ রেল পরিবেশ |
| **থর** | শক্তিশালী CLI টুল তৈরি করুন |
| **ড্রাইরান** | পরীক্ষা রত্ন CLIs |
---

## মূল লাইব্রেরি
| লাইব্রেরি | উদ্দেশ্য |
|---------|---------|
| **রেলস** | ফুল-স্ট্যাক ওয়েব ফ্রেমওয়ার্ক |
| **Sidekiq** | পটভূমি কাজের প্রক্রিয়াকরণ |
| **ডিভাইস** | প্রমাণীকরণ |
| **পন্ডিত** | অনুমোদন |
| **পুমা** | ওয়েব সার্ভার |
| **র্যাক** | ওয়েব সার্ভার ইন্টারফেস |
| **নোকোগিরি** | HTML/XML পার্সিং |
| **ফ্যারাডে** | HTTP ক্লায়েন্ট |
| **httpপার্টি** | সহজ HTTP অনুরোধ |
| **অ্যাকটিভ সাপোর্ট** | ইউটিলিটি ক্লাস (রেল) |
| **শুষ্ক-আরবি** | কার্যকরী রুবি লাইব্রেরি |
| **হানামি::ইউটিলস** | লাইটওয়েট ইউটিলিটি |
| **প্রায়** | বিকাশকারী কনসোল / ডিবাগার |
| **dotenv** | পরিবেশ পরিবর্তনশীল |
| **ফিগারো** | অ্যাপ কনফিগারেশন |
---

## আইডিই এবং সম্পাদক
| IDE | শক্তি |
|------|------------|
| **রুবিমাইন** | সম্পূর্ণ JetBrains রুবি IDE |
| **ভিএস কোড + সোলারগ্রাফ** | লাইটওয়েট, LSP-ভিত্তিক |
| **ভিম/নিওভিম + রুবি-এলএসপি** | টার্মিনাল ভিত্তিক |
| **টেক্সটমেট** | ক্লাসিক macOS সম্পাদক |
---

## স্থাপনা
| পদ্ধতি | নোট |
|---------|-------|
| **পুমা** | ডিফল্ট রেল ওয়েব সার্ভার |
| **যাত্রী** | Apache/Nginx মডিউল |
| **ক্যাপিস্ট্রানো** | দূরবর্তী মাল্টি সার্ভার স্থাপনা |
| **ডকার** | কন্টেইনারাইজড স্থাপনা |
| **হেরোকু** | PaaS (রুবি-বান্ধব) |
| **Fly.io** | অ্যাপ হোস্টিং প্ল্যাটফর্ম |
| **রেলওয়ে** | আধুনিক PaaS |
| **কামাল (বেসক্যাম্প)** | ডকার-ভিত্তিক স্থাপনা |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## সারাংশ
রুবির ইকোসিস্টেম বিকাশকারীর সুখ এবং কনফিগারেশনের উপর কনভেনশনকে কেন্দ্র করে। স্ট্যান্ডার্ড স্ট্যাক হল: **Ruby 3.3+** রানটাইম হিসেবে, **বান্ডলার** নির্ভরতার জন্য, **Rails** ফুল-স্ট্যাক ওয়েবের জন্য (বা **সিনাট্রা** মাইক্রো অ্যাপের জন্য), **RSpec** পরীক্ষার জন্য, **RuboCop** লিন্টিংয়ের জন্য, **Sidekiq** ব্যাকগ্রাউন্ড কাজের জন্য, এবং **Peruma হিসেবে। রুবি দ্রুত প্রোটোটাইপিং, ওয়েব অ্যাপ্লিকেশন, স্ক্রিপ্টিং, এবং CLI সরঞ্জামগুলিতে দক্ষতা অর্জন করে। RubyGems ইকোসিস্টেমে 170,000 এর বেশি প্যাকেজ রয়েছে। Ruby 3.x একযোগে Ractors, স্ট্যাটিক টাইপিংয়ের জন্য RBS এবং প্যাটার্ন ম্যাচিং নিয়ে আসে।