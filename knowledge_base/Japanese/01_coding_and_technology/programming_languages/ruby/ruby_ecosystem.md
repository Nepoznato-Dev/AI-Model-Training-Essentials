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

# Ruby — エコシステムとツールのガイド
このガイドでは、Ruby エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明します。
---

## Ruby の実装
|実装 |メモ |
|---------------|------|
| **CRuby (MRI)** |デフォルト、最も広く使用されています |
| **JRuby** | JVM ベースの Java 相互運用性 |
| **トリュフルビー** | GraalVM ベースの高性能 |
| **mruby** |軽量、埋め込み可能 |
```bash
ruby -v                 # check version
ruby script.rb          # run script
irb                     # interactive REPL
gem list                # list installed gems
```

---

## パッケージ管理
|ツール |目的 |
|-----|----------|
| **ルビージェム** |組み込みの gem パッケージ マネージャー |
| **バンドラー** |依存関係管理 (Gemfile) |
| **rubygems.org** |公式宝石リポジトリ |
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

## Web フレームワーク
|フレームワーク |タイプ |最適な用途 |
|----------|------|----------|
| **レール** |フルスタック |設定よりも規約 |
| **シナトラ** |マイクロ |シンプルな API、小規模なアプリ |
| **お花見** |きれいなアーチ。 |保守可能でテスト可能なアプリ |
| **ロダ** |ルーティングツリー |高性能、柔軟 |
| **ブドウ** | REST API | API を中心としたフレームワーク |
| **ラック** |インターフェース |低レベルの Web サーバー インターフェイス |
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

## データベースと ORM
|テクノロジー |タイプ |
|-----------|------|
| **アクティブな記録** | Rails ORM (規約ベース) |
| **続編** |柔軟で強力な ORM |
| **ROM (Ruby オブジェクト マッパー)** |機能的、構成可能 |
| **ページ** | PostgreSQLアダプター |
| **mysql2** | MySQLアダプター |
| **SQLite3** | SQLite アダプター |
| **モンゴイド** | MongoDB ODM |
| **Redis** |キーと値のストア |
---

## テスト
|フレームワーク |目的 |
|----------|----------|
| **Rスペック** | BDD スタイルのテスト (最も一般的) |
| **ミニテスト** |内蔵、軽量 |
| **カピバラ** |統合/ブラウザのテスト |
| **ファクトリーボット** |テスト データ ファクトリ |
| **フェイカー** |偽のデータの生成 |
| **ウェブモック** | HTTP リクエストのスタブ化 |
| **SimpleCov** |コードカバレッジ |
| **ビデオデッキ** | HTTP インタラクションを記録/再生する |
| **タイムコップ** |テストでの時間操作 |
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

## コードの品質
|ツール |目的 |
|-----|----------|
| **ルーボコップ** |リンターとフォーマッタ |
| **標準RB** |独自の RuboCop 設定 |
| **リーク** |コードの臭いの検出 |
| **ブレーキマン** |セキュリティ脆弱性スキャナ |
| **バンドラー監査** | Gem 脆弱性チェッカー |
| **SimpleCov** |コードカバレッジ |
| **ソーラーグラフ** |言語サーバー、YARD ドキュメント |
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

## タスク ランナーと CLI
|ツール |目的 |
|-----|----------|
| **レーキ** |タスクランナー (Make-like) |
| **トール** | CLI フレームワーク |
| **Rails コンソール** |インタラクティブな Rails 環境 |
| **トール** |強力な CLI ツールを構築する |
| **ドライラン** | gem CLI をテストする |
---

## 主要なライブラリ
|図書館 |目的 |
|----------|----------|
| **レール** |フルスタック Web フレームワーク |
| **サイドキック** |バックグラウンドジョブ処理 |
| **工夫** |認証 |
| **評論家** |認可 |
| **プーマ** |ウェブサーバー |
| **ラック** | Webサーバーインターフェース |
| **鋸山** | HTML/XML 解析 |
| **ファラデー** | HTTPクライアント |
| **httpパーティー** |単純な HTTP リクエスト |
| **アクティブサポート** |ユーティリティ クラス (Rails) |
| **ドライRB** |機能的な Ruby ライブラリ |
| **花見::ユーティリティ** |軽量ユーティリティ |
| **こじ開け** |開発者コンソール/デバッガー |
| **dotenv** |環境変数 |
| **フィガロ** |アプリの設定 |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **ルビーマイン** |完全な JetBrains Ruby IDE |
| **VS コード + ソーラーグラフ** |軽量、LSP ベース |
| **Vim/Neovim + Ruby-lsp** |ターミナルベース |
| **テキストメイト** |クラシック macOS エディタ |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **プーマ** |デフォルトの Rails Web サーバー |
| **乗客** | Apache/Nginx モジュール |
| **カピストラーノ** |リモートマルチサーバー展開 |
| **ドッカー** |コンテナ化された展開 |
| **ヒーローク** | PaaS (Ruby フレンドリー) |
| **Fly.io** |アプリホスティングプラットフォーム |
| **鉄道** |最新の PaaS |
| **カマル (ベースキャンプ)** | Docker ベースのデプロイメント |
```ruby
# config/puma.rb (Rails)
workers Integer(ENV.fetch("WEB_CONCURRENCY", 2))
threads_count = Integer(ENV.fetch("RAILS_MAX_THREADS", 5))
threads threads_count, threads_count
port ENV.fetch("PORT", 3000)
```

---

＃＃ まとめ
Ruby のエコシステムは、構成よりも開発者の幸福と慣例を中心にしています。標準スタックは次のとおりです。ランタイムとして **Ruby 3.3+**、依存関係として **Bundler**、フルスタック Web として **Rails** (またはマイクロ アプリとして **Sinatra**)、テスト用として **RSpec**、リンティング用として **RuboCop**、バックグラウンド ジョブとして **Sidekiq**、Web サーバーとして **Puma** です。 Ruby は、ラピッド プロトタイピング、Web アプリケーション、スクリプト作成、および CLI ツールに優れています。 RubyGems エコシステムには 170,000 を超えるパッケージがあります。 Ruby 3.x では、同時実行のための Ractor、静的型付けのための RBS、およびパターン マッチングが提供されます。