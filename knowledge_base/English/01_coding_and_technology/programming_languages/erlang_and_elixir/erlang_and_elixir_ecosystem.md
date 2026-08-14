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

# Erlang & Elixir — Ecosystem & Tooling Guide

This guide covers the essential tools, frameworks, and infrastructure in the Erlang and Elixir ecosystem, sharing the BEAM VM and OTP.

---

## Runtime & VM

| Component | Purpose |
|-----------|---------|
| **BEAM** | Erlang virtual machine |
| **OTP** | Open Telecom Platform (Erlang) |
| **Erlang/OTP** | Erlang runtime + libraries |
| **Elixir** | Modern language on BEAM |

```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Build Tools

| Tool | Language | Purpose |
|------|----------|---------|
| **Mix** | Elixir | Build tool, task runner |
| **rebar3** | Erlang | Build tool, dependency manager |
| **hex** | Both | Package manager |
| **hex.pm** | Both | Package repository |

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

## Web Frameworks

| Framework | Language | Type |
|-----------|----------|------|
| **Phoenix** | Elixir | Full-stack web (most popular) |
| **Phoenix LiveView** | Elixir | Real-time server-rendered UI |
| **Bandit** | Elixir | Pure-Elixir HTTP server |
| **Cowboy** | Erlang | HTTP server |
| **Chicago Boss** | Erlang | Django-like |
| **N2O** | Erlang | WebSocket framework |

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

## Database

| Technology | Language | Type |
|------------|----------|------|
| **Ecto** | Elixir | Database wrapper + query |
| **Postgrex** | Elixir | PostgreSQL driver |
| **MyXQL** | Elixir | MySQL driver |
| **epgsql** | Erlang | PostgreSQL driver |
| **Mnesia** | Erlang | Built-in distributed DB |
| **Riak** | Erlang | Distributed key-value |
| **CouchDB** | Erlang | Document database |

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

## Testing

| Framework | Language | Purpose |
|-----------|----------|---------|
| **ExUnit** | Elixir | Built-in test framework |
| **EUnit** | Erlang | Erlang unit testing |
| **Common Test** | Erlang | OTP testing framework |
| **PropCheck** | Elixir | Property-based (QuickCheck) |
| **StreamData** | Elixir | Property-based testing |
| **Mox** | Elixir | Mocking |
| **Wallaby** | Elixir | Browser testing |
| **ESpec** | Elixir | BDD-style |

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

## Code Quality

| Tool | Language | Purpose |
|------|----------|---------|
| **Credo** | Elixir | Linting and style |
| **dialyxir** | Elixir | Dialyzer integration |
| **Sobelow** | Elixir | Security analysis |
| **erlang_ls** | Erlang | Language server |
| **elvis** | Erlang | Style checker |

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

## Concurrency & Distribution

| Feature | Purpose |
|---------|---------|
| **Processes** | Lightweight, isolated |
| **Message passing** | Send/receive between processes |
| **GenServer** | Client-server pattern |
| **Supervisor** | Fault tolerance |
| **Application** | OTP component |
| **Distribution** | Multi-node communication |
| **Mnesia** | Distributed database |
| **libcluster** | Cluster formation |
| **Horde** | Distributed process registry |

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

## Key Libraries

| Library | Language | Purpose |
|---------|----------|---------|
| **Phoenix** | Elixir | Web framework |
| **Ecto** | Elixir | Database |
| **Absinthe** | Elixir | GraphQL |
| **Broadway** | Elixir | Data pipelines |
| **Oban** | Elixir | Background jobs |
| **Tesla** | Elixir | HTTP client |
| **Finch** | Elixir | HTTP client |
| **NimbleOptions** | Elixir | Options validation |
| **Timex** | Elixir | Date/time |
| **Jason** | Elixir | JSON |
| **cowboy** | Erlang | HTTP server |
| **ranch** | Erlang | Socket acceptor |
| **lager** | Erlang | Logging |
| **jsx** | Erlang | JSON |

---

## IDEs & Editors

| IDE | Strengths |
|-----|-----------|
| **VS Code + ElixirLS** | Best Elixir support |
| **IntelliJ + Elixir** | JetBrains support |
| **Vim + alchemist.vim** | Vim Elixir |
| **Emacs + erlang-mode** | Classic Erlang |

---

## Deployment

| Method | Notes |
|--------|-------|
| **Mix release** | Self-contained release |
| **Docker** | Containerized |
| **Gigalixir** | Elixir PaaS |
| **Fly.io** | Distributed hosting |
| **Render** | App hosting |
| **Erlang release** | OTP release |
| **Hot code upgrade** | Zero-downtime upgrades |

---

## Summary

Erlang and Elixir share the BEAM VM and OTP, offering unmatched concurrency and fault tolerance. The standard Elixir stack is: **Mix** for builds, **Phoenix** for web, **Phoenix LiveView** for real-time UI, **Ecto** for databases, **ExUnit** for testing, **Credo** for linting, and **Oban** for background jobs. Erlang uses **rebar3** for builds, **Cowboy** for HTTP, and **EUnit** or **Common Test** for testing. Both languages excel at distributed systems, real-time applications (chat, gaming, IoT), telecom, and high-availability services. The ecosystem's strengths are "let it crash" philosophy, hot code upgrades, lightweight processes, and message passing.
