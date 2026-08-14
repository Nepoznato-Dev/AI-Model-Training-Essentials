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
# रूबी - पारिस्थितिकी तंत्र और टूलींग गाइड
यह मार्गदर्शिका रूबी पारिस्थितिकी तंत्र में आवश्यक उपकरण, ढांचे और बुनियादी ढांचे को शामिल करती है।
---

## रूबी कार्यान्वयन
| कार्यान्वयन | नोट्स |
|----------------------|-------|
| **क्रूबी (एमआरआई)** | डिफ़ॉल्ट, सबसे व्यापक रूप से उपयोग किया जाने वाला |
| **रूबी** | जेवीएम-आधारित, जावा इंटरऑप |
| **ट्रफलरूबी** | GraalVM-आधारित, उच्च प्रदर्शन |
| **मरूबी** | हल्का, एम्बेड करने योग्य |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **रूबीजेम्स** | बिल्ट-इन जेम पैकेज मैनेजर |
| **बंडलर** | निर्भरता प्रबंधन (जेमफाइल) |
| **rubygems.org** | आधिकारिक रत्न भंडार |
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

## वेब फ्रेमवर्क
| ढाँचा | प्रकार | के लिए सर्वश्रेष्ठ |
|--------|------|-------|
| **रेल** | फुल-स्टैक | कॉन्फ़िगरेशन पर कन्वेंशन |
| **सिनात्रा** | सूक्ष्म | सरल एपीआई, छोटे ऐप्स |
| **हनमी** | स्वच्छ मेहराब. | रखरखाव योग्य, परीक्षण योग्य ऐप्स |
| **रोड़ा** | रूटिंग ट्री | उच्च प्रदर्शन, लचीला |
| **अंगूर** | बाकी एपीआई | एपीआई-केंद्रित ढांचा |
| **रैक** | इंटरफ़ेस | निम्न-स्तरीय वेब सर्वर इंटरफ़ेस |
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

## डेटाबेस और ओआरएम
| प्रौद्योगिकी | प्रकार |
|------|------|
| **सक्रिय रिकॉर्ड** | रेल ओआरएम (सम्मेलन-आधारित) |
| **अगली कड़ी** | लचीला, शक्तिशाली ओआरएम |
| **ROM (रूबी ऑब्जेक्ट मैपर)** | कार्यात्मक, रचनायोग्य |
| **पृष्ठ** | PostgreSQL एडाप्टर |
| **mysql2** | MySQL एडाप्टर |
| **SQLite3** | SQLite एडाप्टर |
| **मोंगोइड** | मोंगोडीबी ओडीएम |
| **रेडिस** | कुंजी-मूल्य स्टोर |
---

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **RSpec** | बीडीडी-शैली परीक्षण (सबसे लोकप्रिय) |
| **मिनीटेस्ट** | बिल्ट-इन, हल्का वजन |
| **कैपिबारा** | एकीकरण/ब्राउज़र परीक्षण |
| **फ़ैक्टरीबॉट** | परीक्षण डेटा फ़ैक्टरियाँ |
| **नकली** | नकली डेटा जनरेशन |
| **वेबमॉक** | HTTP अनुरोध स्टबिंग |
| **सिंपलकोव** | कोड कवरेज |
| **वीसीआर** | HTTP इंटरैक्शन रिकॉर्ड/रीप्ले करें |
| **टाइमकॉप** | परीक्षणों में समय का हेरफेर |
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

## कोड गुणवत्ता
| उपकरण | उद्देश्य |
|------|---------|
| **रूबोकॉप** | लिंटर और फॉर्मेटर |
| **मानकआरबी** | रूबोकॉप कॉन्फिगरेशन की राय |
| **रीक** | कोड गंध का पता लगाना |
| **ब्रेकमैन** | सुरक्षा भेद्यता स्कैनर |
| **बंडलर-ऑडिट** | रत्न भेद्यता जांचकर्ता |
| **सिंपलकोव** | कोड कवरेज |
| **सोलरग्राफ** | भाषा सर्वर, यार्ड दस्तावेज़ |
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

## टास्क रनर और सीएलआई
| उपकरण | उद्देश्य |
|------|---------|
| **रेक** | टास्क रनर (मेक-लाइक) |
| **थोर** | सीएलआई ढांचा |
| **रेल कंसोल** | इंटरैक्टिव रेल वातावरण |
| **थोर** | शक्तिशाली सीएलआई उपकरण बनाएं |
| **ड्रायरुन** | परीक्षण रत्न सीएलआई |
---

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **रेल** | फुल-स्टैक वेब फ्रेमवर्क |
| **साइडकीक** | पृष्ठभूमि कार्य प्रसंस्करण |
| **युक्ति** | प्रमाणीकरण |
| **पंडित** | प्राधिकरण |
| **प्यूमा** | वेब सर्वर |
| **रैक** | वेब सर्वर इंटरफ़ेस |
| **नोकोगिरी** | HTML/XML पार्सिंग |
| **फैराडे** | HTTP क्लाइंट |
| **एचपार्टी** | सरल HTTP अनुरोध |
| **सक्रिय समर्थन** | उपयोगिता वर्ग (रेल) |
| **ड्राई-आरबी** | कार्यात्मक रूबी लाइब्रेरी |
| **हनमी::उपयोग** | हल्की उपयोगिताएँ |
| **प्राइ** | डेवलपर कंसोल/डीबगर |
| **dotenv** | पर्यावरण चर |
| **फिगारो** | ऐप कॉन्फ़िगरेशन |
---

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **रूबीमाइन** | पूर्ण जेटब्रेन रूबी आईडीई |
| **वीएस कोड + सोलरग्राफ** | हल्का, एलएसपी-आधारित |
| **विम/नियोविम + रूबी-एलएसपी** | टर्मिनल-आधारित |
| **टेक्स्टमेट** | क्लासिक macOS संपादक |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **प्यूमा** | डिफ़ॉल्ट रेल वेब सर्वर |
| **यात्री** | अपाचे/Nginx मॉड्यूल |
| **कैपिस्ट्रानो** | रिमोट मल्टी-सर्वर परिनियोजन |
| **डॉकर** | कंटेनरीकृत परिनियोजन |
| **हेरोकू** | PaaS (रूबी-अनुकूल) |
| **Fly.io** | ऐप होस्टिंग प्लेटफॉर्म |
| **रेलवे** | आधुनिक PaaS |
| **कमल (बेसकैंप)** | डॉकर-आधारित परिनियोजन |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

## सारांश
रूबी का पारिस्थितिकी तंत्र डेवलपर की खुशी और कॉन्फ़िगरेशन पर सम्मेलन पर केंद्रित है। मानक स्टैक है: **रूबी 3.3+** रनटाइम के रूप में, **बंडलर** निर्भरता के लिए, **रेल** फुल-स्टैक वेब के लिए (या **सिनात्रा** माइक्रो ऐप्स के लिए), **RSpec** परीक्षण के लिए, **रूबोकॉप** लिंटिंग के लिए, **साइडकीक** पृष्ठभूमि नौकरियों के लिए, और **प्यूमा** वेब सर्वर के रूप में। रूबी रैपिड प्रोटोटाइपिंग, वेब एप्लिकेशन, स्क्रिप्टिंग और सीएलआई टूल्स में उत्कृष्ट है। रूबीजेम्स इकोसिस्टम में 170,000 से अधिक पैकेज हैं। रूबी 3.x समवर्तीता के लिए ट्रैक्टर्स, स्थिर टाइपिंग के लिए आरबीएस और पैटर्न मिलान लाता है।