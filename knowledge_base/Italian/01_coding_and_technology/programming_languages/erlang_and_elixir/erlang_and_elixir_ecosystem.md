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
# Erlang & Elixir: guida all'ecosistema e agli strumenti
Questa guida copre gli strumenti, i framework e le infrastrutture essenziali nell'ecosistema Erlang ed Elixir, condividendo BEAM VM e OTP.
---

## Runtime e macchina virtuale
| Componente | Scopo |
|-----------|---------|
| **FASCIO** | Macchina virtuale Erlang |
| **OTP** | Piattaforma aperta per le telecomunicazioni (Erlang) |
| **Erlang/OTP** | Runtime Erlang + librerie |
| **Elisir** | Linguaggio moderno su BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Strumenti di creazione
| Strumento | Lingua | Scopo |
|------|----------|---------|
| **Mix** | Elisir | Strumento di creazione, task runner |
| **rebar3** | Erlang | Strumento di creazione, gestore delle dipendenze |
| **esadecimale** | Entrambi | Gestore pacchetti |
| **hex.pm** | Entrambi | Repository dei pacchetti |
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

## Framework Web
| Quadro | Lingua | Digitare |
|-----------|----------|------|
| **Fenice** | Elisir | Web full-stack (più popolare) |
| **Phoenix LiveView** | Elisir | Interfaccia utente con rendering su server in tempo reale |
| **Bandito** | Elisir | Server HTTP Pure-Elixir |
| **Cowboy** | Erlang | ServerHTTP |
| **Capo di Chicago** | Erlang | Simile a Django |
| **N2O** | Erlang | Quadro WebSocket |
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

##Banca dati
| Tecnologia | Lingua | Digitare |
|------------|----------|------|
| **Ecto** | Elisir | Wrapper database + query |
| **Postgrex** | Elisir | Driver PostgreSQL |
| **MyXQL** | Elisir | Driver MySQL |
| **epgsql** | Erlang | Driver PostgreSQL |
| **Mnesia** | Erlang | DB distribuito integrato |
| **Riak** | Erlang | Valore-chiave distribuito |
| **DivanoDB** | Erlang | Banca dati dei documenti |
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

## Test
| Quadro | Lingua | Scopo |
|-----------|----------|---------|
| **UnitàEx** | Elisir | Quadro di test integrato |
| **Unità UE** | Erlang | Test unitario Erlang |
| **Test comune** | Erlang | Quadro di test OTP |
| **PropCheck** | Elisir | Basato sulla proprietà (QuickCheck) |
| **StreamData** | Elisir | Test basati sulle proprietà |
| **Mox** | Elisir | Beffardo |
| **Wallaby** | Elisir | Test del browser |
| **ESpec** | Elisir | Stile BDD |
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

## Qualità del codice
| Strumento | Lingua | Scopo |
|------|----------|---------|
| **Credo** | Elisir | Fodera e stile |
| **dialisir** | Elisir | Integrazione dializzatore |
| **Qui sotto** | Elisir | Analisi della sicurezza |
| **erlang_ls** | Erlang | Server linguistico |
| **Elvis** | Erlang | Controllo dello stile |
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

## Concorrenza e distribuzione
| Caratteristica | Scopo |
|---------|---------|
| **Processi** | Leggero, isolato |
| **Messaggio in transito** | Invia/ricevi tra processi |
| **GenServer** | Modello client-server |
| **Supervisore** | Tolleranza ai guasti |
| **Applicazione** | Componente OTP |
| **Distribuzione** | Comunicazione multinodo |
| **Mnesia** | Database distribuito |
| **libcluster** | Formazione di cluster |
| **Orda** | Registro dei processi distribuiti |
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

## Biblioteche chiave
| Biblioteca | Lingua | Scopo |
|---------|----------|---------|
| **Fenice** | Elisir | Struttura Web |
| **Ecto** | Elisir | Banca dati |
| **Assenzio** | Elisir | GraphQL |
| **Broadway** | Elisir | Pipeline di dati |
| **Oban** | Elisir | Lavori in background |
| **Tesla** | Elisir | Client HTTP |
| **Fringillide** | Elisir | Client HTTP |
| **NimbleOptions** | Elisir | Convalida delle opzioni |
| **Timex** | Elisir | Data/ora |
| **Giasone** | Elisir | JSON |
| **cowboy** | Erlang | ServerHTTP |
| **ranch** | Erlang | Accettore presa |
| **birra** | Erlang | Registrazione |
| **jsx** | Erlang | JSON |
---

## IDE ed editor
| IDE | Punti di forza |
|-----|-----------|
| **Codice VS + ElisirLS** | Miglior supporto Elisir |
| **IntelliJ + Elisir** | Supporto JetBrains |
| **Vim + alchimista.vim** | Elisir Vim |
| **Emacs + modalità erlang** | Erlang classico |
---

## Distribuzione
| Metodo | Note |
|--------|-------|
| **Rilascio mix** | Versione autonoma |
| **Docker** | Containerizzato |
| **Gigalixir** | Elisir PaaS |
| **Fly.io** | Hosting distribuito |
| **Render** | Hosting dell'applicazione |
| **Versione Erlang** | Rilascio OTP |
| **Aggiornamento codice hot** | Aggiornamenti senza tempi di inattività |
---

## Riepilogo
Erlang ed Elixir condividono BEAM VM e OTP, offrendo concorrenza e tolleranza agli errori senza pari. Lo stack Elixir standard è: **Mix** per build, **Phoenix** per il Web, **Phoenix LiveView** per interfaccia utente in tempo reale, **Ecto** per database, **ExUnit** per test, **Credo** per linting e **Oban** per processi in background. Erlang utilizza **rebar3** per le build, **Cowboy** per HTTP e **EUnit** o **Common Test** per i test. Entrambi i linguaggi eccellono nei sistemi distribuiti, nelle applicazioni in tempo reale (chat, giochi, IoT), nelle telecomunicazioni e nei servizi ad alta disponibilità. I punti di forza dell'ecosistema sono la filosofia "let it crash", gli aggiornamenti del codice caldo, i processi leggeri e il passaggio di messaggi.