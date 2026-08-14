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
# Erlang & Elixir - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، چارچوب‌ها و زیرساخت‌های ضروری در اکوسیستم Erlang و Elixir را پوشش می‌دهد و BEAM VM و OTP را به اشتراک می‌گذارد.
---

## زمان اجرا و ماشین مجازی
| جزء | هدف |
|-----------|---------|
| **پرتو** | ماشین مجازی ارلنگ |
| **OTP** | Open Telecom Platform (Erlang) |
| **ارلنگ/OTP** | زمان اجرا Erlang + کتابخانه ها |
| **اکسیر** | زبان مدرن در BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## ابزارهای ساخت
| ابزار | زبان | هدف |
|------|----------|---------|
| **میکس** | اکسیر | ابزار ساخت، اجرای وظیفه |
| **میلگرد3** | ارلنگ | ابزار ساخت، مدیر وابستگی |
| **هگز** | هر دو | مدیر بسته |
| **hex.pm** | هر دو | مخزن بسته |
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

## چارچوب های وب
| چارچوب | زبان | نوع |
|-----------|----------|------|
| **ققنوس** | اکسیر | وب تمام پشته (محبوب ترین) |
| **ققنوس LiveView** | اکسیر | UI ارائه شده توسط سرور در زمان واقعی |
| **راهزن** | اکسیر | سرور HTTP Pure-Elixir |
| **کابویی** | ارلنگ | سرور HTTP |
| **رئیس شیکاگو** | ارلنگ | جنگو مانند |
| **N2O** | ارلنگ | چارچوب WebSocket |
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

## پایگاه داده
| فناوری | زبان | نوع |
|------------|----------|------|
| **اکتو** | اکسیر | بسته بندی پایگاه داده + پرس و جو |
| **پست گرکس** | اکسیر | درایور PostgreSQL |
| **MyXQL** | اکسیر | درایور MySQL |
| **epgsql** | ارلنگ | درایور PostgreSQL |
| **منزیا** | ارلنگ | DB توزیع شده داخلی |
| **ریاک** | ارلنگ | کلید-مقدار توزیع شده |
| **CouchDB** | ارلنگ | پایگاه اسناد |
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

## تست
| چارچوب | زبان | هدف |
|-----------|----------|---------|
| **ExUnit** | اکسیر | چارچوب تست داخلی |
| **یونیت** | ارلنگ | تست واحد ارلنگ |
| **تست مشترک** | ارلنگ | چارچوب تست OTP |
| **PropCheck** | اکسیر | مبتنی بر اموال (QuickCheck) |
| **StreamData** | اکسیر | تست مبتنی بر اموال |
| **موکس** | اکسیر | تمسخر |
| **والبی** | اکسیر | تست مرورگر |
| **ESpec** | اکسیر | سبک BDD |
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

## کیفیت کد
| ابزار | زبان | هدف |
|------|----------|---------|
| **اعتقاد** | اکسیر | لینتینگ و سبک |
| **دیالکسیر** | اکسیر | ادغام دیالیز |
| **پایین** | اکسیر | تحلیل امنیتی |
| **erlang_ls** | ارلنگ | سرور زبان |
| **الویس** | ارلنگ | جستجوگر سبک |
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

## همزمانی و توزیع
| ویژگی | هدف |
|---------|---------|
| **فرایندها** | سبک، ایزوله |
| **پیغام در حال عبور** | ارسال/دریافت بین فرآیندها |
| **GenServer** | الگوی سرویس گیرنده-سرور |
| **سرپرست** | تحمل خطا |
| **برنامه** | جزء OTP |
| **توزیع** | ارتباط چند گرهی |
| **منزیا** | پایگاه داده توزیع شده |
| **libcluster** | تشکیل خوشه |
| **هورد ** | رجیستری فرآیند توزیع شده |
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

## کتابخانه های کلیدی
| کتابخانه | زبان | هدف |
|---------|----------|---------|
| **ققنوس** | اکسیر | چارچوب وب |
| **اکتو** | اکسیر | پایگاه داده |
| **آبسنت** | اکسیر | GraphQL |
| **برادوی** | اکسیر | خطوط لوله داده |
| **اوبان** | اکسیر | مشاغل پیشینه |
| **تسلا** | اکسیر | سرویس گیرنده HTTP |
| **فینچ** | اکسیر | سرویس گیرنده HTTP |
| **NimbleOptions** | اکسیر | اعتبار سنجی گزینه ها |
| **Timex** | اکسیر | تاریخ/زمان |
| **جیسون** | اکسیر | JSON |
| **کابویی** | ارلنگ | سرور HTTP |
| **مزرعه** | ارلنگ | سوکت گیرنده |
| **لگر** | ارلنگ | ورود به سیستم |
| **jsx** | ارلنگ | JSON |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + ElixirLS** | بهترین پشتیبانی اکسیر |
| **IntelliJ +Elixir** | پشتیبانی JetBrains |
| **ویم + کیمیاگر.vim** | ویم اکسیر |
| **Emacs + erlang-mode** | ارلنگ کلاسیک |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **میکس انتشار** | انتشار خودکفا |
| **داکر** | کانتینری |
| **گیگالیکسیر** | اکسیر PaaS |
| **Fly.io** | هاست توزیع شده |
| **رندر** | میزبانی اپلیکیشن |
| **ارلنگ انتشار** | انتشار OTP |
| ** ارتقاء کد داغ** | ارتقاء بدون توقف |
---

## خلاصه
Erlang و Elixir BEAM VM و OTP را به اشتراک می گذارند که همزمانی و تحمل خطا بی بدیل را ارائه می دهند. پشته استاندارد Elixir عبارت است از: **Mix** برای ساخت، **Phoenix** برای وب، **Phoenix LiveView** برای رابط کاربری بلادرنگ، **Ecto** برای پایگاه داده، **ExUnit** برای آزمایش، **Credo** برای linting، و **Oban** برای کارهای پس زمینه. Erlang از **rebar3** برای بیلدها، **Cowboy** برای HTTP و **EUnit** یا **Common Test** برای تست استفاده می کند. هر دو زبان در سیستم‌های توزیع‌شده، برنامه‌های کاربردی بلادرنگ (چت، بازی، اینترنت اشیا)، مخابرات و سرویس‌های در دسترس برتر هستند. نقاط قوت اکوسیستم عبارتند از فلسفه "بگذار خراب شود"، ارتقاء کد داغ، فرآیندهای سبک وزن و ارسال پیام.