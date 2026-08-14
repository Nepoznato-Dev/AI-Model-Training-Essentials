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

# Erlang at Elixir — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang tool, frameworks, at imprastraktura sa Erlang at Elixir ecosystem, na nagbabahagi ng BEAM VM at OTP.
---

## Runtime at VM
| Bahagi | Layunin |
|-----------|---------|
| **BEAM** | Erlang virtual machine |
| **OTP** | Buksan ang Telecom Platform (Erlang) |
| **Erlang/OTP** | Erlang runtime + mga aklatan |
| **Elixir** | Modernong wika sa BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Bumuo ng Mga Tool
| Tool | Wika | Layunin |
|------|----------|---------|
| **Paghalo** | Elixir | Build tool, task runner |
| **rebar3** | Erlang | Build tool, dependency manager |
| **hex** | Parehong | Tagapamahala ng package |
| **hex.pm** | Parehong | Imbakan ng package |
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

## Mga Web Framework
| Balangkas | Wika | Uri |
|-----------|----------|------|
| **Phoenix** | Elixir | Full-stack na web (pinakatanyag) |
| **Phoenix LiveView** | Elixir | Real-time na server-render na UI |
| **Bandera** | Elixir | Pure-Elixir HTTP server |
| **Cowboy** | Erlang | HTTP server |
| **Chicago Boss** | Erlang | Parang Django |
| **N2O** | Erlang | Framework ng WebSocket |
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
| Teknolohiya | Wika | Uri |
|------------|----------|------|
| **Ecto** | Elixir | Database wrapper + query |
| **Postgrex** | Elixir | PostgreSQL driver |
| **MyXQL** | Elixir | MySQL driver |
| **epgsql** | Erlang | PostgreSQL driver |
| **Mnesia** | Erlang | Built-in na ipinamahagi na DB |
| **Riak** | Erlang | Ibinahagi ang key-value |
| **CouchDB** | Erlang | Database ng dokumento |
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

## Pagsubok
| Balangkas | Wika | Layunin |
|-----------|----------|---------|
| **ExUnit** | Elixir | Built-in na balangkas ng pagsubok |
| **EUnit** | Erlang | Erlang unit testing |
| **Karaniwang Pagsusulit** | Erlang | OTP testing framework |
| **PropCheck** | Elixir | Batay sa ari-arian (QuickCheck) |
| **StreamData** | Elixir | Pagsubok na nakabatay sa ari-arian |
| **Mox** | Elixir | Nanunuya |
| **Wallaby** | Elixir | Pagsubok sa browser |
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

## Kalidad ng Code
| Tool | Wika | Layunin |
|------|----------|---------|
| **Credo** | Elixir | Linting at istilo |
| **dialyxir** | Elixir | Pagsasama ng Dialyzer |
| **Sobelow** | Elixir | Pagsusuri sa seguridad |
| **erlang_ls** | Erlang | Server ng wika |
| **elvis** | Erlang | Tagasuri ng istilo |
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

## Kasabay at Pamamahagi
| Tampok | Layunin |
|---------|---------|
| **Mga Proseso** | Magaan, nakahiwalay |
| **Pagpapasa ng mensahe** | Magpadala/ tumanggap sa pagitan ng mga proseso |
| **GenServer** | Pattern ng Client-server |
| **Supervisor** | Fault tolerance |
| **Aplikasyon** | bahagi ng OTP |
| **Pamamahagi** | Multi-node na komunikasyon |
| **Mnesia** | Ibinahagi database |
| **libcluster** | Pagbubuo ng kumpol |
| **Horde** | Naipamahagi na proseso ng pagpapatala |
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

## Mga Pangunahing Aklatan
| Aklatan | Wika | Layunin |
|---------|----------|---------|
| **Phoenix** | Elixir | Web framework |
| **Ecto** | Elixir | Database |
| **Absinthe** | Elixir | GraphQL |
| **Broadway** | Elixir | Mga pipeline ng data |
| **Oban** | Elixir | Mga trabaho sa background |
| **Tesla** | Elixir | HTTP client |
| **Finch** | Elixir | HTTP client |
| **NimbleOptions** | Elixir | Pagpapatunay ng mga opsyon |
| **Timex** | Elixir | Petsa/oras |
| **Jason** | Elixir | JSON |
| **koboy** | Erlang | HTTP server |
| **rancho** | Erlang | Socket acceptor |
| **lager** | Erlang | Pag-log |
| **jsx** | Erlang | JSON |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code + ElixirLS** | Pinakamahusay na suporta sa Elixir |
| **IntelliJ + Elixir** | Suporta sa JetBrains |
| **Vim + alchemist.vim** | Vim Elixir |
| **Emacs + erlang-mode** | Klasikong Erlang |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **Mix release** | Self-contained release |
| **Docker** | Naka-container |
| **Gigalixir** | Elixir PaaS |
| **Fly.io** | Ibinahagi na pagho-host |
| **I-render** | Pagho-host ng app |
| **Paglabas ni Erlang** | Paglabas ng OTP |
| **Pag-upgrade ng hot code** | Zero-downtime na mga upgrade |
---

## Buod
Sina Erlang at Elixir ay nagbabahagi ng BEAM VM at OTP, na nag-aalok ng walang kaparis na concurrency at fault tolerance. Ang karaniwang Elixir stack ay: **Mix** para sa mga build, **Phoenix** para sa web, **Phoenix LiveView** para sa real-time na UI, **Ecto** para sa mga database, **ExUnit** para sa pagsubok, **Credo** para sa linting, at **Oban** para sa mga background na trabaho. Gumagamit si Erlang ng **rebar3** para sa mga build, **Cowboy** para sa HTTP, at **EUnit** o **Common Test** para sa pagsubok. Parehong mahusay ang dalawang wika sa mga distributed system, real-time na application (chat, gaming, IoT), telecom, at mga serbisyong may mataas na kakayahang magamit. Ang mga kalakasan ng ecosystem ay ang pilosopiya na "hayaan itong bumagsak", maiinit na pag-upgrade ng code, magaan na proseso, at pagpasa ng mensahe.