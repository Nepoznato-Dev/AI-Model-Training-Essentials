<!--
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

-->
# Erlang & Elixir – Leitfaden für Ökosysteme und Werkzeuge
Dieser Leitfaden behandelt die wesentlichen Tools, Frameworks und Infrastruktur im Erlang- und Elixir-Ökosystem und teilt die BEAM-VM und das OTP.
---

## Laufzeit und VM
| Komponente | Zweck |
|-----------|---------|
| **STRAHL** | Virtuelle Erlang-Maschine |
| **OTP** | Offene Telekommunikationsplattform (Erlang) |
| **Erlang/OTP** | Erlang-Laufzeit + Bibliotheken |
| **Elixier** | Moderne Sprache auf BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Build-Tools
| Werkzeug | Sprache | Zweck |
|------|----------|---------|
| **Mischen** | Elixier | Build-Tool, Task-Runner |
| **Bewehrungsstab3** | Erlang | Build-Tool, Abhängigkeitsmanager |
| **hex** | Beide | Paketmanager |
| **hex.pm** | Beide | Paket-Repository |
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

## Web-Frameworks
| Rahmen | Sprache | Geben Sie | ein
|-----------|----------|------|
| **Phönix** | Elixier | Full-Stack-Web (am beliebtesten) |
| **Phoenix LiveView** | Elixier | Vom Server in Echtzeit gerenderte Benutzeroberfläche |
| **Bandit** | Elixier | Pure-Elixir HTTP-Server |
| **Cowboy** | Erlang | HTTP-Server |
| **Chicago Boss** | Erlang | Django-artig |
| **N2O** | Erlang | WebSocket-Framework |
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

## Datenbank
| Technologie | Sprache | Geben Sie | ein
|------------|----------|------|
| **Ekto** | Elixier | Datenbank-Wrapper + Abfrage |
| **Postgrex** | Elixier | PostgreSQL-Treiber |
| **MyXQL** | Elixier | MySQL-Treiber |
| **epgsql** | Erlang | PostgreSQL-Treiber |
| **Mnesia** | Erlang | Integrierte verteilte Datenbank |
| **Riak** | Erlang | Verteilter Schlüsselwert |
| **CouchDB** | Erlang | Dokumentendatenbank |
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

## Testen
| Rahmen | Sprache | Zweck |
|-----------|----------|---------|
| **ExUnit** | Elixier | Integriertes Test-Framework |
| **EUnit** | Erlang | Erlang-Unit-Tests |
| **Allgemeiner Test** | Erlang | OTP-Test-Framework |
| **PropCheck** | Elixier | Eigenschaftsbasiert (QuickCheck) |
| **StreamData** | Elixier | Eigenschaftsbasiertes Testen |
| **Mox** | Elixier | Spott |
| **Wallaby** | Elixier | Browsertests |
| **ESpec** | Elixier | BDD-Stil |
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

## Codequalität
| Werkzeug | Sprache | Zweck |
|------|----------|---------|
| **Credo** | Elixier | Fusseln und Stylen |
| **dialyxir** | Elixier | Dialysator-Integration |
| **Sounten** | Elixier | Sicherheitsanalyse |
| **erlang_ls** | Erlang | Sprachserver |
| **Elvis** | Erlang | Stilprüfer |
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

## Parallelität und Verteilung
| Funktion | Zweck |
|---------|---------|
| **Prozesse** | Leicht, isoliert |
| **Nachrichtenübermittlung** | Senden/Empfangen zwischen Prozessen |
| **GenServer** | Client-Server-Muster |
| **Vorgesetzter** | Fehlertoleranz |
| **Bewerbung** | OTP-Komponente |
| **Verteilung** | Multi-Knoten-Kommunikation |
| **Mnesia** | Verteilte Datenbank |
| **libcluster** | Clusterbildung |
| **Horde** | Verteilte Prozessregistrierung |
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

## Wichtige Bibliotheken
| Bibliothek | Sprache | Zweck |
|---------|----------|---------|
| **Phönix** | Elixier | Web-Framework |
| **Ekto** | Elixier | Datenbank |
| **Absinth** | Elixier | GraphQL |
| **Broadway** | Elixier | Datenpipelines |
| **Oban** | Elixier | Hintergrundjobs |
| **Tesla** | Elixier | HTTP-Client |
| **Fink** | Elixier | HTTP-Client |
| **NimbleOptions** | Elixier | Optionsvalidierung |
| **Timex** | Elixier | Datum/Uhrzeit |
| **Jason** | Elixier | JSON |
| **Cowboy** | Erlang | HTTP-Server |
| **Ranch** | Erlang | Socket-Akzeptor |
| **Lagerbier** | Erlang | Protokollierung |
| **jsx** | Erlang | JSON |
---

## IDEs und Editoren
| IDE | Stärken |
|-----|-----------|
| **VS Code + ElixirLS** | Beste Elixir-Unterstützung |
| **IntelliJ + Elixier** | JetBrains-Unterstützung |
| **Vim + alchemist.vim** | Vim-Elixier |
| **Emacs + Erlang-Modus** | Klassisches Erlang |
---

## Bereitstellung
| Methode | Notizen |
|--------|-------|
| **Mix-Veröffentlichung** | Eigenständige Veröffentlichung |
| **Docker** | Containerisiert |
| **Gigalixir** | Elixir PaaS |
| **Fly.io** | Verteiltes Hosting |
| **Rendern** | App-Hosting |
| **Erlang-Veröffentlichung** | OTP-Veröffentlichung |
| **Hot-Code-Upgrade** | Upgrades ohne Ausfallzeiten |
---

## Zusammenfassung
Erlang und Elixir teilen sich die BEAM-VM und das OTP und bieten unübertroffene Parallelität und Fehlertoleranz. Der Standard-Elixir-Stack ist: **Mix** für Builds, **Phoenix** für das Web, **Phoenix LiveView** für Echtzeit-UI, **Ecto** für Datenbanken, **ExUnit** für Tests, **Credo** für Linting und **Oban** für Hintergrundjobs. Erlang verwendet **rebar3** für Builds, **Cowboy** für HTTP und **EUnit** oder **Common Test** zum Testen. Beide Sprachen zeichnen sich durch verteilte Systeme, Echtzeitanwendungen (Chat, Spiele, IoT), Telekommunikation und Hochverfügbarkeitsdienste aus. Die Stärken des Ökosystems sind die „Let it crash“-Philosophie, Hot-Code-Upgrades, leichtgewichtige Prozesse und die Weitergabe von Nachrichten.