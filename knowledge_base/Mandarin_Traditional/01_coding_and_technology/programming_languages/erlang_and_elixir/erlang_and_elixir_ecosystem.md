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
# Erlang 和 Elixir — 生態系統和工具指南
本指南涵蓋了 Erlang 和 Elixir 生態系統中的基本工具、框架和基礎設施，共享 BEAM VM 和 OTP。
---

## 運行時和虛擬機
|組件|目的|
|------------|---------|
| **光束** | Erlang虛擬機器|
| **一次性密碼** |開放電信平台 (Erlang) |
| **Erlang/OTP** | Erlang 運行時 + 庫 |
| **長生不老藥** | BEAM 上的現代語言 |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## 建置工具
|工具|語言 |目的|
|------|----------|---------|
| **混合** |長生不老藥 |建置工具、任務運行器 |
| **鋼筋3** |二郎 |建造工具、依賴管理器 |
| **十六進位** |兩者 |套件管理器 |
| **hex.pm** |兩者 |套件儲存庫 |
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

## 網路框架
|框架|語言 |類型 |
|------------|----------|------|
| **鳳凰** |長生不老藥 |全端網路（最受歡迎）|
| **鳳凰直播** |長生不老藥 |即時伺服器渲染 UI |
| **強盜** |長生不老藥 | Pure-Elixir HTTP 伺服器 |
| **牛仔** |二郎 | HTTP 伺服器 |
| **芝加哥老闆** |二郎 |類似姜戈 |
| **N2O** |二郎 | WebSocket 框架 |
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

## 資料庫
|技術 |語言 |類型 |
|------------|----------|------|
| **埃克托** |長生不老藥 |資料庫包裝+查詢|
| **Postgrex** |長生不老藥 | PostgreSQL 驅動程式 |
| **MyXQL** |長生不老藥 | MySQL 驅動程式 |
| **epgsql** |二郎 | PostgreSQL 驅動程式 |
| **記憶力** |二郎 |內建分散式DB |
| **裡亞克** |二郎 |分散式鍵值|
| **CouchDB** |二郎 |文檔資料庫 |
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

## 測試
|框架|語言 |目的|
|------------|----------|---------|
| **ExUnit** |長生不老藥 |內建測試框架 |
| **EUnit** |二郎 | Erlang 單元測試 |
| **常見測試** |二郎 | OTP測試框架|
| **道具檢查** |長生不老藥 |基於財產（快速檢查）|
| **流資料** |長生不老藥 |基於屬性的測試 |
| **莫克斯** |長生不老藥 |嘲笑|
| **小袋鼠** |長生不老藥 |瀏覽器測驗 |
| **E規格** |長生不老藥 | BDD 款式 |
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

## 程式碼品質
|工具|語言 |目的|
|------|----------|---------|
| **信條** |長生不老藥 |絨毛與風格 |
| **dialyxir** |長生不老藥 |透析器整合 |
| **如下** |長生不老藥 |證券分析|
| **erlang_ls** |二郎 |語言伺服器|
| **貓王** |二郎 |風格檢查器 |
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

## 並發與分佈
|特色 |目的|
|---------|---------|
| **流程** |輕量、隔離|
| **訊息傳遞** |進程之間發送/接收 |
| **GenServer** |客戶端-伺服器模式 |
| **主管** |容錯|
| **應用** | OTP 元件 |
| **分佈** |多節點通訊 |
| **記憶力** |分散式資料庫 |
| **libcluster** |集群形成|
| **部落** |分散式程序註冊|
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

## 關鍵庫
|圖書館 |語言 |目的|
|---------|----------|---------|
| **鳳凰** |長生不老藥 |網頁框架|
| **埃克托** |長生不老藥 |資料庫|
| **苦艾酒** |長生不老藥 | GraphQL |
| **百老匯** |長生不老藥 |資料管道|
| **奧本** |長生不老藥 |後台工作 |
| **特斯拉** |長生不老藥 | HTTP 用戶端 |
| **芬奇** |長生不老藥 | HTTP 用戶端 |
| **彈性選項** |長生不老藥 |選項驗證 |
| **天美時** |長生不老藥 |日期/時間 |
| **傑森** |長生不老藥 | JSON |
| **牛仔** |二郎 | HTTP 伺服器 |
| **牧場** |二郎 |插座接受器|
| **啤酒** |二郎 |記錄 |
| **jsx** |二郎 | JSON |
---

## IDE 和編輯器
| IDE |優勢 |
|-----|------------|
| **VS Code + ElixirLS** |最佳 Elixir 支援 |
| **IntelliJ + Elixir** | JetBrains 支援 |
| **Vim + alchemist.vim** | Vim 靈丹妙藥 |
| **Emacs + erlang 模式** |經典Erlang |
---

## 部署
|方法|筆記|
|--------|--------|
| **混合發布** |獨立發布 |
| **碼頭工人** |貨櫃式|
| **吉加利西爾** | Elixir 平台即服務 |
| **Fly.io** |分散式託管 |
| **渲染** |應用程式託管 |
| **Erlang 版本** |一次性密碼發布 |
| **代碼熱升級** |零停機升級|
---

＃＃ 概括
Erlang 和 Elixir 共享 BEAM VM 和 OTP，提供無與倫比的並發性和容錯能力。標準 Elixir 堆疊是：用於建立的 **Mix**、用於 Web 的 **Phoenix**、用於即時 UI 的 **Phoenix LiveView**、用於資料庫的 **Ecto**、用於測試的 **ExUnit**、用於 linting 的 **Credo** 以及用於後台作業的 **Oban**。 Erlang 使用 **rebar3** 進行構建，使用 **Cowboy** 進行 HTTP，使用 **EUnit** 或 **Common Test** 進行測試。這兩種語言都擅長分散式系統、即時應用程式（聊天、遊戲、物聯網）、電信和高可用性服務。這個生態系統的優勢在於「讓它崩潰」理念、熱代碼升級、輕量級流程和訊息傳遞。