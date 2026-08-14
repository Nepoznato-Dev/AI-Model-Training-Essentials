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
# Erlang & Elixir — Руководство по экосистеме и инструментам
В этом руководстве описаны основные инструменты, платформы и инфраструктура экосистемы Erlang и Elixir, а также общие виртуальная машина BEAM и OTP.
---

## Время выполнения и виртуальная машина
| Компонент | Цель |
|-----------|---------|
| **ЛУЧ** | Виртуальная машина Эрланга |
| **ОТП** | Открытая телекоммуникационная платформа (Эрланг) |
| **Эрланг/OTP** | Среда выполнения Erlang + библиотеки |
| **Эликсир** | Современный язык на BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Инструменты сборки
| Инструмент | Язык | Цель |
|------|----------|---------|
| **Микс** | Эликсир | Инструмент для сборки, средство запуска задач |
| **арматура3** | Эрланг | Инструмент сборки, менеджер зависимостей |
| **шестнадцатеричный** | Оба | Менеджер пакетов |
| **шестнадцатеричный.pm** | Оба | Репозиторий пакетов |
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

## Веб-фреймворки
| Рамочная | Язык | Тип |
|-----------|----------|------|
| **Феникс** | Эликсир | Полнофункциональный веб-сайт (самый популярный) |
| **Феникс LiveView** | Эликсир | Пользовательский интерфейс, отображаемый на сервере в реальном времени |
| **Бандит** | Эликсир | HTTP-сервер Pure-Elixir |
| **Ковбой** | Эрланг | HTTP-сервер |
| **Чикаго Босс** | Эрланг | Джангоподобный |
| **N2O** | Эрланг | Платформа WebSocket |
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

## База данных
| Технология | Язык | Тип |
|------------|----------|------|
| **Экто** | Эликсир | Оболочка базы данных + запрос |
| **Постгрекс** | Эликсир | Драйвер PostgreSQL |
| **MyXQL** | Эликсир | Драйвер MySQL |
| **epgsql** | Эрланг | Драйвер PostgreSQL |
| **Мнезия** | Эрланг | Встроенная распределенная БД |
| **Риак** | Эрланг | Распределенный ключ-значение |
| **CouchDB** | Эрланг | База данных документов |
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

## Тестирование
| Рамочная | Язык | Цель |
|-----------|----------|---------|
| **ExUnit** | Эликсир | Встроенная среда тестирования |
| **Юнит** | Эрланг | Модульное тестирование Erlang |
| **Общий тест** | Эрланг | Система тестирования OTP |
| **ПропПроверка** | Эликсир | На основе свойств (QuickCheck) |
| **СтримДанные** | Эликсир | Тестирование на основе свойств |
| **Мокс** | Эликсир | Издевательство |
| **Валлаби** | Эликсир | Тестирование браузера |
| **ЭСпец** | Эликсир | BDD-стиль |
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

## Качество кода
| Инструмент | Язык | Цель |
|------|----------|---------|
| **Кредо** | Эликсир | Линтинг и стиль |
| **диаликсир** | Эликсир | Интеграция диализатора |
| **Сонилоу** | Эликсир | Анализ безопасности |
| **erlang_ls** | Эрланг | Языковой сервер |
| **Элвис** | Эрланг | Проверка стиля |
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

## Параллелизм и распространение
| Особенность | Цель |
|---------|---------|
| **Процессы** | Легкий, изолированный |
| **Передача сообщений** | Отправка/получение между процессами |
| **ГенСервер** | Шаблон клиент-сервер |
| **Супервайзер** | Отказоустойчивость |
| **Приложение** | OTP-компонент |
| **Распространение** | Многоузловая связь |
| **Мнезия** | Распределенная база данных |
| **libcluster** | Формирование кластера |
| **Орда** | Распределенный реестр процессов |
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

## Ключевые библиотеки
| Библиотека | Язык | Цель |
|---------|----------|---------|
| **Феникс** | Эликсир | Веб-фреймворк |
| **Экто** | Эликсир | База данных |
| **Абсент** | Эликсир | ГрафQL |
| **Бродвей** | Эликсир | Конвейеры данных |
| **Обан** | Эликсир | Фоновые вакансии |
| **Тесла** | Эликсир | HTTP-клиент |
| **Финч** | Эликсир | HTTP-клиент |
| **ПроворныеПараметры** | Эликсир | Проверка параметров |
| **Тимекс** | Эликсир | Дата/время |
| **Джейсон** | Эликсир | JSON |
| **ковбой** | Эрланг | HTTP-сервер |
| **ранчо** | Эрланг | Розеточный акцептор |
| **лагер** | Эрланг | Ведение журнала |
| **jsx** | Эрланг | JSON |
---

## IDE и редакторы
| IDE | Сильные стороны |
|-----|-----------|
| **VS Code + ElixirLS** | Лучшая поддержка Эликсира |
| **IntelliJ + Эликсир** | Поддержка JetBrains |
| **Вим + alchemist.vim** | Вим Эликсир |
| **Emacs + режим erlang** | Классический Эрланг |
---

## Развертывание
| Метод | Заметки |
|--------|-------|
| **Смешанный выпуск** | Автономный выпуск |
| **Докер** | Контейнерный |
| **Гигаликсир** | Эликсир PaaS |
| **Fly.io** | Распределенный хостинг |
| **Рендеринг** | Хостинг приложений |
| **Релиз Erlang** | OTP-релиз |
| **Горячее обновление кода** | Обновления без простоев |
---

## Краткое содержание
Erlang и Elixir используют виртуальную машину BEAM и OTP, обеспечивая непревзойденный параллелизм и отказоустойчивость. Стандартный стек Elixir: **Mix** для сборок, **Phoenix** для Интернета, **Phoenix LiveView** для пользовательского интерфейса в реальном времени, **Ecto** для баз данных, **ExUnit** для тестирования, **Credo** для анализа и **Oban** для фоновых заданий. Erlang использует **rebar3** для сборок, **Cowboy** для HTTP и **EUnit** или **Common Test** для тестирования. Оба языка превосходны в распределенных системах, приложениях реального времени (чат, игры, Интернет вещей), телекоммуникациях и услугах высокой доступности. Сильными сторонами экосистемы являются философия «пусть выйдет из строя», «горячие» обновления кода, упрощенные процессы и передача сообщений.