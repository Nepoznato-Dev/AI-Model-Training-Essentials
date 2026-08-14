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
# Erlang & Elixir — Guide de l'écosystème et des outils
Ce guide couvre les outils, frameworks et infrastructures essentiels de l'écosystème Erlang et Elixir, partageant la VM BEAM et l'OTP.
---

## Runtime et VM
| Composant | Objectif |
|-----------|---------|
| **POUTRE** | Machine virtuelle Erlang |
| **OTP** | Plateforme Télécom Ouverte (Erlang) |
| **Erlang/OTP** | Runtime Erlang + bibliothèques |
| **Élixir** | Langage moderne sur BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Outils de création
| Outil | Langue | Objectif |
|------|----------|---------|
| **Mélanger** | Élixir | Outil de construction, exécuteur de tâches |
| **barre d'armature3** | Erlang | Outil de build, gestionnaire de dépendances |
| **hexadécimal** | Les deux | Gestionnaire de paquets |
| **hex.pm** | Les deux | Dépôt de packages |
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

## Cadres Web
| Cadre | Langue | Tapez |
|-----------|----------|------|
| **Phénix** | Élixir | Web full-stack (le plus populaire) |
| **Phoenix LiveView** | Élixir | Interface utilisateur rendue par le serveur en temps réel |
| **Bandits** | Élixir | Serveur HTTP Pure-Elixir |
| **Cowboy** | Erlang | Serveur HTTP |
| **Patron de Chicago** | Erlang | Comme Django |
| **N2O** | Erlang | Cadre WebSocket |
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

## Base de données
| Technologie | Langue | Tapez |
|------------|----------|------|
| **Ecto** | Élixir | Wrapper de base de données + requête |
| **Postgrex** | Élixir | Pilote PostgreSQL |
| **MonXQL** | Élixir | Pilote MySQL |
| **epgsql** | Erlang | Pilote PostgreSQL |
| **Mnésie** | Erlang | Base de données distribuée intégrée |
| **Riak** | Erlang | Valeur-clé distribuée |
| **CoucheDB** | Erlang | Base de données documentaire |
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

## Tests
| Cadre | Langue | Objectif |
|-----------|----------|---------|
| **ExUnit** | Élixir | Cadre de test intégré |
| **Unité EU** | Erlang | Tests unitaires Erlang |
| **Test commun** | Erlang | Cadre de test OTP |
| **PropCheck** | Élixir | Basé sur la propriété (QuickCheck) |
| **StreamData** | Élixir | Tests basés sur les propriétés |
| **Mox** | Élixir | Moqueur |
| **Wallaby** | Élixir | Test du navigateur |
| **ESpéc** | Élixir | Style BDD |
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

## Qualité du code
| Outil | Langue | Objectif |
|------|----------|---------|
| **Crédo** | Élixir | Pelucheux et style |
| **dialyxir** | Élixir | Intégration du dialyseur |
| **Soci-dessous** | Élixir | Analyse de sécurité |
| **erlang_ls** | Erlang | Serveur de langue |
| **Elvis** | Erlang | Vérificateur de style |
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

## Concurrence et distribution
| Fonctionnalité | Objectif |
|---------|---------|
| **Processus** | Léger, isolé |
| **Passage de message** | Envoyer/recevoir entre processus |
| **GenServeur** | Modèle client-serveur |
| **Superviseur** | Tolérance aux pannes |
| **Candidature** | Composant OTP |
| **Distribution** | Communication multi-nœuds |
| **Mnésie** | Base de données distribuée |
| **libcluster** | Formation de clusters |
| **Horde** | Registre des processus distribués |
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

## Bibliothèques clés
| Bibliothèque | Langue | Objectif |
|---------|----------|---------|
| **Phénix** | Élixir | Cadre Web |
| **Ecto** | Élixir | Base de données |
| **Absinthe** | Élixir | GraphQL |
| **Broadway** | Élixir | Pipelines de données |
| **Oban** | Élixir | Emplois en arrière-plan |
| **Tesla** | Élixir | Client HTTP |
| **Pinson** | Élixir | Client HTTP |
| **Options agiles** | Élixir | Validation des options |
| **Timex** | Élixir | Date/heure |
| **Jason** | Élixir | JSON |
| **cow-boy** | Erlang | Serveur HTTP |
| **ranch** | Erlang | Accepteur de prise |
| **bière blonde** | Erlang | Journalisation |
| **jsx** | Erlang | JSON |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Code VS + ElixirLS** | Meilleur support Elixir |
| **IntelliJ + Élixir** | Prise en charge de JetBrains |
| **Vim + alchimiste.vim** | Élixir Vim |
| **Emacs + mode erlang** | Erlang classique |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Version Mix** | Libération autonome |
| **Docker** | Conteneurisé |
| **Gigalixir** | Élixir PaaS |
| **Fly.io** | Hébergement distribué |
| **Rendu** | Hébergement d'applications |
| **Version Erlang** | Libération du Bureau du Procureur |
| **Mise à niveau du code à chaud** | Mises à niveau sans temps d'arrêt |
---

## Résumé
Erlang et Elixir partagent la VM BEAM et l'OTP, offrant une concurrence et une tolérance aux pannes inégalées. La pile Elixir standard est : **Mix** pour les builds, **Phoenix** pour le Web, **Phoenix LiveView** pour l'interface utilisateur en temps réel, **Ecto** pour les bases de données, **ExUnit** pour les tests, **Credo** pour le peluchage et **Oban** pour les tâches en arrière-plan. Erlang utilise **rebar3** pour les builds, **Cowboy** pour HTTP et **EUnit** ou **Common Test** pour les tests. Les deux langages excellent dans les systèmes distribués, les applications en temps réel (chat, jeux, IoT), les télécommunications et les services à haute disponibilité. Les points forts de l'écosystème sont la philosophie « laissez-le planter », les mises à niveau de code à chaud, les processus légers et la transmission de messages.