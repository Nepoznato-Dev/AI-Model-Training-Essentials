---
# Metadata
title: "Erlang & Elixir — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Erlang and Elixir ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [erlang, elixir, ecosystem, tooling, otp, beam, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Erlang と Elixir — エコシステムとツールのガイド
このガイドでは、Erlang および Elixir エコシステムの重要なツール、フレームワーク、インフラストラクチャについて説明し、BEAM VM と OTP を共有します。
---

## ランタイムと VM
|コンポーネント |目的 |
|----------|----------|
| **ビーム** | Erlang 仮想マシン |
| **OTP** |オープンテレコムプラットフォーム (Erlang) |
| **アーラン/OTP** | Erlang ランタイム + ライブラリ |
| **エリクサー** | BEAMの現代語 |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## ビルドツール
|ツール |言語 |目的 |
|------|----------|----------|
| **ミックス** |エリクサー |ビルドツール、タスクランナー |
| **鉄筋3** |アーラン |ビルドツール、依存関係マネージャー |
| **16 進数** |両方 |パッケージマネージャー |
| **hex.pm** |両方 |パッケージリポジトリ |
```bash
# Elixir / Mix
mix new myapp               # create project
mix deps.get                # install dependencies
mix compile                 # compile
mix test                    # run tests
mix run                     # run application
mix phx.new myapp           # Phoenix project
mix release                 # create release

# Erlang / rebar3
rebar3 new app myapp        # create project
rebar3 get-deps             # install dependencies
rebar3 compile              # compile
rebar3 eunit                # run tests
rebar3 release              # create release
```

```elixir
# mix.exs
defmodule Myapp.MixProject do
  use Mix.Project

  def project do
    [
      app: :myapp,
      version: "0.1.0",
      elixir: "~> 1.16",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  defp deps do
    [
      {:phoenix, "~> 1.7"},
      {:ecto_sql, "~> 3.11"},
      {:jason, "~> 1.4"},
      {:plug_cowboy, "~> 2.7"}
    ]
  end
end
```

---

## Web フレームワーク
|フレームワーク |言語 |タイプ |
|----------|----------|------|
| **フェニックス** |エリクサー |フルスタック Web (最も人気のある) |
| **フェニックス ライブビュー** |エリクサー |リアルタイムのサーバーレンダリング UI |
| **バンディット** |エリクサー | Pure-Elixir HTTP サーバー |
| **カウボーイ** |アーラン | HTTPサーバー |
| **シカゴ ボス** |アーラン |ジャンゴっぽい |
| **N2O** |アーラン | WebSocket フレームワーク |
```elixir
# Phoenix controller
defmodule MyAppWeb.UserController do
  use MyAppWeb, :controller

  def index(conn, _params) do
    users = Accounts.list_users()
    render(conn, :index, users: users)
  end

  def show(conn, %{"id" => id}) do
    user = Accounts.get_user!(id)
    render(conn, :show, user: user)
  end

  def create(conn, %{"user" => user_params}) do
    case Accounts.create_user(user_params) do
      {:ok, user} ->
        conn |> put_status(:created) |> render(:show, user: user)
      {:error, changeset} ->
        conn |> put_status(:unprocessable_entity) |> render(:error, changeset: changeset)
    end
  end
end
```

---

## データベース
|テクノロジー |言語 |タイプ |
|-----------|----------|------|
| **エクト** |エリクサー |データベース ラッパー + クエリ |
| **ポストグレックス** |エリクサー | PostgreSQLドライバー |
| **MyXQL** |エリクサー | MySQLドライバー |
| **epgsql** |アーラン | PostgreSQLドライバー |
| **記憶喪失** |アーラン |分散DB内蔵 |
| **リアク** |アーラン |分散キー値 |
| **CouchDB** |アーラン |文書データベース |
```elixir
# Ecto schema and query
defmodule MyApp.Accounts.User do
  use Ecto.Schema
  import Ecto.Changeset

  schema "users" do
    field :name, :string
    field :email, :string
    field :age, :integer
    timestamps()
  end

  def changeset(user, attrs) do
    user
    |> cast(attrs, [:name, :email, :age])
    |> validate_required([:name, :email])
    |> validate_format(:email, ~r/@/)
    |> unique_constraint(:email)
  end
end

# Query
import Ecto.Query

users = from(u in User,
  where: u.age > ^min_age,
  order_by: [asc: u.name],
  select: u
)
|> Repo.all()
```

---

## テスト
|フレームワーク |言語 |目的 |
|----------|----------|----------|
| **ユニット外** |エリクサー |組み込みのテスト フレームワーク |
| **EUユニット** |アーラン | Erlang 単体テスト |
| **共通テスト** |アーラン | OTP テスト フレームワーク |
| **プロップチェック** |エリクサー |プロパティベース (クイックチェック) |
| **ストリームデータ** |エリクサー |プロパティベースのテスト |
| **モックス** |エリクサー |嘲笑 |
| **ワラビー** |エリクサー |ブラウザのテスト |
| **Eスペック** |エリクサー | BDD スタイル |
```elixir
# ExUnit
defmodule MyApp.UserServiceTest do
  use ExUnit.Case, async: true

  describe "find/1" do
    test "returns user when found" do
      user = UserService.find(1)
      assert user.name == "Alice"
    end

    test "raises when not found" do
      assert_raise NotFoundError, fn ->
        UserService.find(999)
      end
    end
  end
end
```

```bash
mix test                    # run tests
mix test --trace            # verbose
mix test test/user_test.exs # specific file
```

---

## コードの品質
|ツール |言語 |目的 |
|------|----------|----------|
| **信条** |エリクサー |リンティングとスタイル |
| **ダイアリキシル** |エリクサー |ダイアライザーの統合 |
| **以下** |エリクサー |セキュリティ分析 |
| **erlang_ls** |アーラン |言語サーバー |
| **エルヴィス** |アーラン |スタイルチェッカー |
```elixir
# .credo.exs
%{
  configs: [
    %{
      name: "default",
      strict: true,
      checks: [
        {Credo.Check.Readability.MaxLineLength, max_length: 120},
        {Credo.Check.Design.TagTODO, false}
      ]
    }
  ]
}
```

```bash
mix credo                   # lint
mix dialyzer                # type checking
mix sobelow -r .            # security scan
```

---

## 同時実行性と分散性
|特集 |目的 |
|----------|----------|
| **プロセス** |軽量、分離 |
| **メッセージパッシング** |プロセス間の送受信 |
| **GenServer** |クライアントサーバーパターン |
| **スーパーバイザー** |フォールトトレランス |
| **アプリケーション** | OTP コンポーネント |
| **配布** |マルチノード通信 |
| **記憶喪失** |分散データベース |
| **libcluster** |クラスター形成 |
| **大群** |分散プロセスレジストリ |
```elixir
# GenServer example
defmodule UserService do
  use GenServer

  def start_link(_) do
    GenServer.start_link(__MODULE__, %{}, name: __MODULE__)
  end

  def find(id) do
    GenServer.call(__MODULE__, {:find, id})
  end

  @impl true
  def init(state), do: {:ok, state}

  @impl true
  def handle_call({:find, id}, _from, state) do
    case Map.get(state, id) do
      nil -> {:reply, {:error, :not_found}, state}
      user -> {:reply, {:ok, user}, state}
    end
  end
end
```

---

## 主要なライブラリ
|図書館 |言語 |目的 |
|----------|----------|----------|
| **フェニックス** |エリクサー |ウェブフレームワーク |
| **エクト** |エリクサー |データベース |
| **アブサン** |エリクサー |グラフQL |
| **ブロードウェイ** |エリクサー |データパイプライン |
| **オーバン** |エリクサー |バックグラウンドジョブ |
| **テスラ** |エリクサー | HTTPクライアント |
| **フィンチ** |エリクサー | HTTPクライアント |
| **ニンブルオプション** |エリクサー |オプションの検証 |
| **タイメックス** |エリクサー |日付/時刻 |
| **ジェイソン** |エリクサー | JSON |
| **カウボーイ** |アーラン | HTTPサーバー |
| **牧場** |アーラン |ソケットアクセプター |
| **ラガー** |アーラン |ロギング |
| **jsx** |アーラン | JSON |
---

## IDE とエディター
| IDE |強み |
|-----|----------|
| **VS コード + ElixirLS** |最高の Elixir サポート |
| **IntelliJ + Elixir** | JetBrains サポート |
| **Vim + alchemist.vim** |ヴィムエリクサー |
| **Emacs + erlang モード** |クラシック Erlang |
---

## デプロイメント
|方法 |メモ |
|------|------|
| **ミックスリリース** |自己完結型リリース |
| **ドッカー** |コンテナ化 |
| **ギガリクシル** | Elixir PaaS |
| **Fly.io** |分散ホスティング |
| **レンダリング** |アプリホスティング |
| **Erlang リリース** | OTP リリース |
| **ホットコードのアップグレード** |ダウンタイムゼロのアップグレード |
---

＃＃ まとめ
Erlang と Elixir は BEAM VM と OTP を共有し、比類のない同時実行性とフォールト トレランスを提供します。標準の Elixir スタックは、ビルド用 **Mix**、Web 用 **Phoenix**、リアルタイム UI 用 **Phoenix LiveView**、データベース用 **Ecto**、テスト用 **ExUnit**、リンティング用 **Credo**、およびバックグラウンド ジョブ用 **Oban** です。 Erlang はビルドに **rebar3**、HTTP に **Cowboy**、テストに **EUnit** または **Common Test** を使用します。どちらの言語も、分散システム、リアルタイム アプリケーション (チャット、ゲーム、IoT)、通信、および高可用性サービスに優れています。このエコシステムの強みは、「クラッシュさせる」哲学、ホット コード アップグレード、軽量プロセス、メッセージ パッシングです。