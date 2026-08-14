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
# Erlang & Elixir — Przewodnik po ekosystemie i narzędziach
Ten przewodnik omawia podstawowe narzędzia, frameworki i infrastrukturę w ekosystemie Erlang i Elixir, współdzieląc BEAM VM i OTP.
---

## Środowisko wykonawcze i maszyna wirtualna
| Składnik | Cel |
|---------------|--------|
| **BELKA** | Maszyna wirtualna Erlanga |
| **OTP** | Otwarta platforma telekomunikacyjna (Erlang) |
| **Erlang/OTP** | Środowisko wykonawcze Erlang + biblioteki |
| **Eliksir** | Współczesny język na BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Narzędzia do tworzenia
| Narzędzie | Język | Cel |
|------|----------|--------|
| **Wymieszaj** | Eliksir | Narzędzie do tworzenia, uruchamianie zadań |
| **zbrojenie3** | Erlang | Narzędzie do budowania, menedżer zależności |
| **szesnast** | Obydwa | Menedżer pakietów |
| **hex.pm** | Obydwa | Repozytorium pakietów |
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

## Struktury internetowe
| Ramy | Język | Wpisz |
|----------|----------|------|
| **Feniks** | Eliksir | Sieć z pełnym stosem (najbardziej popularna) |
| **Podgląd na żywo w Phoenix** | Eliksir | Interfejs użytkownika renderowany przez serwer w czasie rzeczywistym |
| **Bandyta** | Eliksir | Serwer HTTP Pure-Elixir |
| **Kowboj** | Erlang | Serwer HTTP |
| **Szef Chicago** | Erlang | Podobny do Django |
| **N2O** | Erlang | Framework WebSocket |
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

## Baza danych
| Technologia | Język | Wpisz |
|------------|---------|------|
| **Ekto** | Eliksir | Opakowanie bazy danych + zapytanie |
| **Postgrex** | Eliksir | Sterownik PostgreSQL |
| **MójXQL** | Eliksir | Sterownik MySQL |
| **epgsql** | Erlang | Sterownik PostgreSQL |
| **Mnezja** | Erlang | Wbudowana rozproszona baza danych |
| **Riak** | Erlang | Rozproszona para klucz-wartość |
| **KanapaDB** | Erlang | Baza dokumentów |
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

## Testowanie
| Ramy | Język | Cel |
|----------|----------|---------|
| **Wyjście** | Eliksir | Wbudowane środowisko testowe |
| **EUjednostka** | Erlang | Testowanie jednostkowe Erlanga |
| **Wspólny test** | Erlang | Ramy testowania OTP |
| **Sprawdzanie rekwizytów** | Eliksir | Oparte na właściwościach (QuickCheck) |
| **Dane strumienia** | Eliksir | Testowanie oparte na właściwościach |
| **Mox** | Eliksir | Kpiąco |
| **Walaby** | Eliksir | Testowanie przeglądarki |
| **Specyfikacja** | Eliksir | w stylu BDD |
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

## Jakość kodu
| Narzędzie | Język | Cel |
|------|----------|--------|
| **Kredo** | Eliksir | Linting i styl |
| **dialiksir** | Eliksir | Integracja dializatora |
| **Soponiżej** | Eliksir | Analiza bezpieczeństwa |
| **erlang_ls** | Erlang | Serwer językowy |
| **Elvis** | Erlang | Sprawdzanie stylu |
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

## Współbieżność i dystrybucja
| Funkcja | Cel |
|--------|---------|
| **Procesy** | Lekki, izolowany |
| **Przekazywanie wiadomości** | Wysyłaj/odbieraj pomiędzy procesami |
| **Serwer Generujący** | Wzór klient-serwer |
| **Nadzorca** | Tolerancja błędów |
| **Aplikacja** | Składnik OTP |
| **Dystrybucja** | Komunikacja wielowęzłowa |
| **Mnezja** | Rozproszona baza danych |
| **libcluster** | Tworzenie klastrów |
| **Horda** | Rejestr procesów rozproszonych |
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

## Kluczowe biblioteki
| Biblioteka | Język | Cel |
|--------|----------|--------|
| **Feniks** | Eliksir | Struktura internetowa |
| **Ekto** | Eliksir | Baza danych |
| **Absynt** | Eliksir | WykresQL |
| **Broadway** | Eliksir | Potoki danych |
| **Oban** | Eliksir | Zadania w tle |
| **Tesli** | Eliksir | Klient HTTP |
| **Zięba** | Eliksir | Klient HTTP |
| **Opcje zwinne** | Eliksir | Walidacja opcji |
| **Timex** | Eliksir | Data/godzina |
| **Jason** | Eliksir | JSON |
| **kowboj** | Erlang | Serwer HTTP |
| **ranczo** | Erlang | Akceptor gniazda |
| **lager** | Erlang | Rejestrowanie |
| **js** | Erlang | JSON |
---

## IDE i redaktorzy
| IDE | Mocne strony |
|-----|-----------|
| **Kod VS + EliksirLS** | Najlepsze wsparcie Elixiru |
| **IntelliJ + Eliksir** | Wsparcie JetBrains |
| **Vim + alchemist.vim** | Eliksir Vima |
| **Emacs + tryb Erlang** | Klasyczny Erlang |
---

## Zastosowanie
| Metoda | Notatki |
|------------|-------|
| **Wydanie miksu** | Samodzielne wydanie |
| **Doker** | Kontenerowy |
| **Gigaliksir** | Eliksir PaaS |
| **Fly.io** | Hosting rozproszony |
| **Renderowanie** | Hosting aplikacji |
| **Wydanie Erlanga** | Wydanie OTP |
| **Aktualizacja gorącego kodu** | Aktualizacje bez przestojów |
---

## Streszczenie
Erlang i Elixir współdzielą BEAM VM i OTP, oferując niezrównaną współbieżność i odporność na błędy. Standardowy stos Elixir to: **Mix** do kompilacji, **Phoenix** do Internetu, **Phoenix LiveView** do interfejsu użytkownika w czasie rzeczywistym, **Ecto** do baz danych, **ExUnit** do testowania, **Credo** do lintingu i **Oban** do zadań w tle. Erlang używa **rebar3** do kompilacji, **Cowboy** do HTTP i **EUnit** lub **Common Test** do testowania. Obydwa języki wyróżniają się w systemach rozproszonych, aplikacjach czasu rzeczywistego (czaty, gry, IoT), telekomunikacji i usługach wysokiej dostępności. Mocnymi stronami ekosystemu są filozofia „pozwól mu się zawiesić”, aktualizacje gorącego kodu, lekkie procesy i przekazywanie komunikatów.