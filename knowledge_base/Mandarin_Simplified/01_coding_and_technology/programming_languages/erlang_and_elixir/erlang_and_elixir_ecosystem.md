---
# Metadata
title: "Erlang & Elixir — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Erlang and Elixir ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Erlang 和 Elixir — 生态系统和工具指南
本指南涵盖了 Erlang 和 Elixir 生态系统中的基本工具、框架和基础设施，共享 BEAM VM 和 OTP。
---

## 运行时和虚拟机
|组件|目的|
|------------|---------|
| **光束** | Erlang虚拟机|
| **一次性密码** |开放电信平台 (Erlang) |
| **Erlang/OTP** | Erlang 运行时 + 库 |
| **长生不老药** | BEAM 上的现代语言 |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## 构建工具
|工具|语言 |目的|
|------|----------|---------|
| **混合** |长生不老药 |构建工具、任务运行器 |
| **钢筋3** |二郎 |构建工具、依赖管理器 |
| **十六进制** |两者 |包管理器 |
| **hex.pm** |两者 |包存储库 |
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

## 网络框架
|框架|语言 |类型 |
|------------|----------|------|
| **凤凰** |长生不老药 |全栈网络（最受欢迎）|
| **凤凰直播** |长生不老药 |实时服务器渲染 UI |
| **强盗** |长生不老药 | Pure-Elixir HTTP 服务器 |
| **牛仔** |二郎 | HTTP 服务器 |
| **芝加哥老板** |二郎 |类似姜戈 |
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

＃＃ 数据库
|技术 |语言 |类型 |
|------------|----------|------|
| **埃克托** |长生不老药 |数据库包装+查询|
| **Postgrex** |长生不老药 | PostgreSQL 驱动程序 |
| **MyXQL** |长生不老药 | MySQL 驱动程序 |
| **epgsql** |二郎 | PostgreSQL 驱动程序 |
| **记忆力** |二郎 |内置分布式DB |
| **里亚克** |二郎 |分布式键值|
| **CouchDB** |二郎 |文档数据库 |
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

## 测试
|框架|语言 |目的|
|------------|----------|---------|
| **ExUnit** |长生不老药 |内置测试框架 |
| **EUnit** |二郎 | Erlang 单元测试 |
| **常见测试** |二郎 | OTP测试框架|
| **道具检查** |长生不老药 |基于财产（快速检查）|
| **流数据** |长生不老药 |基于属性的测试 |
| **莫克斯** |长生不老药 |嘲笑|
| **小袋鼠** |长生不老药 |浏览器测试 |
| **E规格** |长生不老药 | BDD 风格 |
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

## 代码质量
|工具|语言 |目的|
|------|----------|---------|
| **信条** |长生不老药 |绒毛和风格 |
| **dialyxir** |长生不老药 |透析器集成 |
| **如下** |长生不老药 |证券分析|
| **erlang_ls** |二郎 |语言服务器|
| **猫王** |二郎 |风格检查器 |
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

## 并发与分布
|特色 |目的|
|---------|---------|
| **流程** |轻量、隔离|
| **消息传递** |进程之间发送/接收 |
| **GenServer** |客户端-服务器模式 |
| **主管** |容错|
| **应用** | OTP 组件 |
| **分布** |多节点通讯 |
| **记忆力** |分布式数据库 |
| **libcluster** |集群形成|
| **部落** |分布式进程注册|
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

## 关键库
|图书馆 |语言 |目的|
|---------|----------|---------|
| **凤凰** |长生不老药 |网页框架|
| **埃克托** |长生不老药 |数据库|
| **苦艾酒** |长生不老药 | GraphQL |
| **百老汇** |长生不老药 |数据管道|
| **奥本** |长生不老药 |后台工作 |
| **特斯拉** |长生不老药 | HTTP 客户端 |
| **芬奇** |长生不老药 | HTTP 客户端 |
| **灵活选项** |长生不老药 |选项验证 |
| **天美时** |长生不老药 |日期/时间 |
| **杰森** |长生不老药 | JSON |
| **牛仔** |二郎 | HTTP 服务器 |
| **牧场** |二郎 |插座接受器|
| **啤酒** |二郎 |记录 |
| **jsx** |二郎 | JSON |
---

## IDE 和编辑器
| IDE |优势 |
|-----|------------|
| **VS Code + ElixirLS** |最佳 Elixir 支持 |
| **IntelliJ + Elixir** | JetBrains 支持 |
| **Vim + alchemist.vim** | Vim 灵丹妙药 |
| **Emacs + erlang 模式** |经典Erlang |
---

## 部署
|方法|笔记|
|--------|--------|
| **混合发布** |独立发布 |
| **码头工人** |集装箱式|
| **吉加利西尔** | Elixir 平台即服务 |
| **Fly.io** |分布式托管 |
| **渲染** |应用程序托管 |
| **Erlang 版本** |一次性密码发布 |
| **代码热升级** |零停机升级|
---

＃＃ 概括
Erlang 和 Elixir 共享 BEAM VM 和 OTP，提供无与伦比的并发性和容错能力。标准 Elixir 堆栈是：用于构建的 **Mix**、用于 Web 的 **Phoenix**、用于实时 UI 的 **Phoenix LiveView**、用于数据库的 **Ecto**、用于测试的 **ExUnit**、用于 linting 的 **Credo** 以及用于后台作业的 **Oban**。 Erlang 使用 **rebar3** 进行构建，使用 **Cowboy** 进行 HTTP，使用 **EUnit** 或 **Common Test** 进行测试。这两种语言都擅长分布式系统、实时应用程序（聊天、游戏、物联网）、电信和高可用性服务。该生态系统的优势在于“让它崩溃”理念、热代码升级、轻量级流程和消息传递。