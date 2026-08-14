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

# Erlang & Elixir: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, los marcos y la infraestructura esenciales en el ecosistema de Erlang y Elixir, compartiendo BEAM VM y OTP.
---

## Tiempo de ejecución y máquina virtual
| Componente | Propósito |
|-----------|------------------|
| **HAZ** | Máquina virtual Erlang |
| **OTP** | Plataforma abierta de telecomunicaciones (Erlang) |
| **Erlang/OTP** | Tiempo de ejecución de Erlang + bibliotecas |
| **Elíxir** | Lenguaje moderno en BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Herramientas de construcción
| Herramienta | Idioma | Propósito |
|------|----------|---------|
| **Mezclar** | Elixir | Herramienta de construcción, corredor de tareas |
| **barra de refuerzo3** | Erlang | Herramienta de compilación, administrador de dependencias |
| **hexadecimal** | Ambos | Administrador de paquetes |
| **hexadecimal.pm** | Ambos | Repositorio de paquetes |
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

## Marcos web
| Marco | Idioma | Tipo |
|-----------|----------|------|
| **Fénix** | Elixir | Web de pila completa (más popular) |
| **Phoenix LiveView** | Elixir | UI renderizada por servidor en tiempo real |
| **Bandido** | Elixir | Servidor HTTP Pure-Elixir |
| **Vaquero** | Erlang | Servidor HTTP |
| **Jefe de Chicago** | Erlang | Al estilo Django |
| **N2O** | Erlang | Marco WebSocket |
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

## Base de datos
| Tecnología | Idioma | Tipo |
|------------|----------|------|
| **Ecto** | Elixir | Envoltorio de base de datos + consulta |
| **Postgrex** | Elixir | Controlador PostgreSQL |
| **MiXQL** | Elixir | Controlador MySQL |
| **epgsql** | Erlang | Controlador PostgreSQL |
| **Mnesia** | Erlang | Base de datos distribuida incorporada |
| **Riak** | Erlang | Valor-clave distribuido |
| **SofáDB** | Erlang | Base de datos de documentos |
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

## Pruebas
| Marco | Idioma | Propósito |
|-----------|----------|---------|
| **ExUnidad** | Elixir | Marco de prueba incorporado |
| **Unidad UE** | Erlang | Pruebas unitarias de Erlang |
| **Prueba común** | Erlang | Marco de prueba de OTP |
| **PropCheck** | Elixir | Basado en propiedad (QuickCheck) |
| **Transmisión de datos** | Elixir | Pruebas basadas en propiedades |
| **Mox** | Elixir | Burlarse |
| **Ualabí** | Elixir | Pruebas del navegador |
| **Espec** | Elixir | Estilo BDD |
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

## Calidad del código
| Herramienta | Idioma | Propósito |
|------|----------|---------|
| **Credo** | Elixir | Linting y estilo |
| **dialixir** | Elixir | Integración del dializador |
| **Abajo** | Elixir | Análisis de seguridad |
| **erlang_ls** | Erlang | Servidor de idiomas |
| **elvis** | Erlang | Comprobador de estilo |
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

## Simultaneidad y distribución
| Característica | Propósito |
|---------|---------|
| **Procesos** | Ligero, aislado |
| **Pasar mensaje** | Enviar/recibir entre procesos |
| **GenServer** | Patrón cliente-servidor |
| **Supervisor** | Tolerancia a fallos |
| **Solicitud** | Componente OTP |
| **Distribución** | Comunicación multinodo |
| **Mnesia** | Base de datos distribuida |
| **libcluster** | Formación de conglomerados |
| **Horda** | Registro de procesos distribuidos |
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

## Bibliotecas clave
| Biblioteca | Idioma | Propósito |
|---------|----------|---------|
| **Fénix** | Elixir | Marco web |
| **Ecto** | Elixir | Base de datos |
| **Absenta** | Elixir | GráficoQL |
| **Broadway** | Elixir | Tuberías de datos |
| **Oban** | Elixir | Trabajos en segundo plano |
| **Tesla** | Elixir | Cliente HTTP |
| **Pinzón** | Elixir | Cliente HTTP |
| **Opciones ágiles** | Elixir | Validación de opciones |
| **Tiempo** | Elixir | Fecha/hora |
| **Jasón** | Elixir | JSON |
| **vaquero** | Erlang | Servidor HTTP |
| **rancho** | Erlang | Aceptador de enchufe |
| **lager** | Erlang | Registro |
| **jsx** | Erlang | JSON |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + ElixirLS** | Mejor soporte de Elixir |
| **IntelliJ + Elixir** | Soporte de JetBrains |
| **Vim + alquimista.vim** | Elixir Vim |
| **Emacs + modo erlang** | Erlang clásico |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Lanzamiento de mezcla** | Lanzamiento autónomo |
| **Acoplador** | En contenedores |
| **Gigalixir** | ElixirPaaS |
| **Fly.io** | Alojamiento distribuido |
| **Renderizar** | Alojamiento de aplicaciones |
| **Lanzamiento de Erlang** | Lanzamiento de OTP |
| **Actualización de código activo** | Actualizaciones sin tiempo de inactividad |
---

## Resumen
Erlang y Elixir comparten BEAM VM y OTP, lo que ofrece simultaneidad y tolerancia a fallos inigualables. La pila estándar de Elixir es: **Mix** para compilaciones, **Phoenix** para web, **Phoenix LiveView** para interfaz de usuario en tiempo real, **Ecto** para bases de datos, **ExUnit** para pruebas, **Credo** para linting y **Oban** para trabajos en segundo plano. Erlang usa **rebar3** para compilaciones, **Cowboy** para HTTP y **EUnit** o **Common Test** para pruebas. Ambos lenguajes destacan en sistemas distribuidos, aplicaciones en tiempo real (chat, juegos, IoT), telecomunicaciones y servicios de alta disponibilidad. Las fortalezas del ecosistema son la filosofía de "dejar que se bloquee", las actualizaciones de código activo, los procesos livianos y la transmisión de mensajes.