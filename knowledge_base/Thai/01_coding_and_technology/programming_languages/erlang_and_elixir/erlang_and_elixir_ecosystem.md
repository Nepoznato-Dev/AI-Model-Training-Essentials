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

# Erlang & Elixir - คู่มือระบบนิเวศและเครื่องมือ
คู่มือนี้ครอบคลุมถึงเครื่องมือ เฟรมเวิร์ก และโครงสร้างพื้นฐานที่จำเป็นในระบบนิเวศ Erlang และ Elixir การแบ่งปัน BEAM VM และ OTP
---

## รันไทม์และ VM
| ส่วนประกอบ | วัตถุประสงค์ |
|----------|---------|
| **บีม** | เครื่องเสมือน Erlang |
| **สนข.** | เปิดแพลตฟอร์มโทรคมนาคม (Erlang) |
| **เออร์แลง/OTP** | รันไทม์ Erlang + ไลบรารี |
| **ยาอายุวัฒนะ** | ภาษาสมัยใหม่บน BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## สร้างเครื่องมือ
| เครื่องมือ | ภาษา | วัตถุประสงค์ |
|------|----------|---------|
| **มิกซ์** | ยาอายุวัฒนะ | เครื่องมือสร้างตัวรันงาน |
| **เหล็กเส้น3** | เออร์ลัง | เครื่องมือสร้าง ตัวจัดการการพึ่งพา |
| **เลขฐานสิบหก** | ทั้งสอง | ผู้จัดการแพ็คเกจ |
| **hex.pm** | ทั้งสอง | พื้นที่เก็บข้อมูลแพ็กเกจ |
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

## กรอบงานเว็บ
| กรอบ | ภาษา | พิมพ์ |
|----------|-----------|-|
| **ฟีนิกซ์** | ยาอายุวัฒนะ | เว็บเต็มกอง (ยอดนิยมที่สุด) |
| **ฟีนิกซ์ LiveView** | ยาอายุวัฒนะ | UI ที่แสดงผลบนเซิร์ฟเวอร์แบบเรียลไทม์ |
| **โจร** | ยาอายุวัฒนะ | เซิร์ฟเวอร์ Pure-Elixir HTTP |
| **คาวบอย** | เออร์ลัง | เซิร์ฟเวอร์ HTTP |
| **ชิคาโก้บอส** | เออร์ลัง | เหมือนจังโก้ |
| **N2O** | เออร์ลัง | กรอบงาน WebSocket |
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

## ฐานข้อมูล
| เทคโนโลยี | ภาษา | พิมพ์ |
|------------|-----------|-|
| **เอคโต** | ยาอายุวัฒนะ | wrapper ฐานข้อมูล + แบบสอบถาม |
| **Postgrex** | ยาอายุวัฒนะ | ไดรเวอร์ PostgreSQL |
| **MyXQL** | ยาอายุวัฒนะ | ไดรเวอร์ MySQL |
| **epgsql** | เออร์ลัง | ไดรเวอร์ PostgreSQL |
| **ความจำเสื่อม** | เออร์ลัง | DB แบบกระจายในตัว |
| **เรียค** | เออร์ลัง | คีย์-ค่าแบบกระจาย |
| **CouchDB** | เออร์ลัง | ฐานข้อมูลเอกสาร |
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

## การทดสอบ
| กรอบ | ภาษา | วัตถุประสงค์ |
|----------|----------|---------|
| **ทางออกยูนิต** | ยาอายุวัฒนะ | กรอบการทดสอบในตัว |
| **หน่วย** | เออร์ลัง | การทดสอบหน่วย Erlang |
| **การทดสอบทั่วไป** | เออร์ลัง | กรอบการทดสอบ OTP |
| **พร็อพเช็ค** | ยาอายุวัฒนะ | ตามคุณสมบัติ (QuickCheck) |
| **สตรีมข้อมูล** | ยาอายุวัฒนะ | การทดสอบตามคุณสมบัติ |
| **ม็อกซ์** | ยาอายุวัฒนะ | ล้อเลียน |
| **วอลลาบี** | ยาอายุวัฒนะ | การทดสอบเบราว์เซอร์ |
| **อีสเปค** | ยาอายุวัฒนะ | สไตล์ BDD |
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

## คุณภาพรหัส
| เครื่องมือ | ภาษา | วัตถุประสงค์ |
|------|----------|---------|
| **ลัทธิ** | ยาอายุวัฒนะ | ผ้าสำลีและสไตล์ |
| **ไดอะลีซีร์** | ยาอายุวัฒนะ | บูรณาการตัวฟอกไต |
| **ด้านล่าง** | ยาอายุวัฒนะ | การวิเคราะห์ความปลอดภัย |
| **erlang_ls** | เออร์ลัง | เซิร์ฟเวอร์ภาษา |
| **เอลวิส** | เออร์ลัง | ตัวตรวจสอบสไตล์ |
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

## ความเห็นพ้องต้องกันและการกระจาย
| คุณสมบัติ | วัตถุประสงค์ |
|---------|---------|
| **กระบวนการ** | น้ำหนักเบา โดดเดี่ยว |
| **ข้อความที่ส่งผ่าน** | ส่ง/รับระหว่างกระบวนการ |
| **เจนเซิร์ฟเวอร์** | รูปแบบไคลเอ็นต์ - เซิร์ฟเวอร์ |
| **หัวหน้างาน** | ความทนทานต่อข้อผิดพลาด |
| **ใบสมัคร** | องค์ประกอบ OTP |
| **การจัดจำหน่าย** | การสื่อสารแบบหลายโหนด |
| **ความจำเสื่อม** | ฐานข้อมูลแบบกระจาย |
| **ไลบรารี่** | การก่อตัวของคลัสเตอร์ |
| **ฝูงชน** | รีจิสทรีกระบวนการแบบกระจาย |
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

## ห้องสมุดที่สำคัญ
| ห้องสมุด | ภาษา | วัตถุประสงค์ |
|---------|----------|---------|
| **ฟีนิกซ์** | ยาอายุวัฒนะ | กรอบงานเว็บ |
| **เอคโต** | ยาอายุวัฒนะ | ฐานข้อมูล |
| **แอ๊บซินท์** | ยาอายุวัฒนะ | GraphQL |
| **บรอดเวย์** | ยาอายุวัฒนะ | ไปป์ไลน์ข้อมูล |
| **โอบัน** | ยาอายุวัฒนะ | งานพื้นหลัง |
| **เทสลา** | ยาอายุวัฒนะ | ไคลเอ็นต์ HTTP |
| **ฟินช์** | ยาอายุวัฒนะ | ไคลเอ็นต์ HTTP |
| **NimbleOptions** | ยาอายุวัฒนะ | การตรวจสอบตัวเลือก |
| **ไทม์เม็กซ์** | ยาอายุวัฒนะ | วันที่/เวลา |
| **เจสัน** | ยาอายุวัฒนะ | เจสัน |
| **คาวบอย** | เออร์ลัง | เซิร์ฟเวอร์ HTTP |
| **ฟาร์ม** | เออร์ลัง | ตัวรับซ็อกเก็ต |
| **ลาเกอร์** | เออร์ลัง | การบันทึก |
| **jsx** | เออร์ลัง | เจสัน |
---

## IDE และบรรณาธิการ
| ไอดี | จุดแข็ง |
|-----|-----------|
| **VS Code + ElixirLS** | การสนับสนุน Elixir ที่ดีที่สุด |
| **IntelliJ + Elixir** | การสนับสนุน JetBrains |
| **Vim + alchemist.vim** | Vim Elixir |
| **Emacs + โหมด erlang** | คลาสสิค Erlang |
---

## การปรับใช้
| วิธีการ | หมายเหตุ |
|--------|--------|
| **ปล่อยมิกซ์** | การปล่อยที่มีอยู่ในตัวเอง |
| **นักเทียบท่า** | บรรจุในตู้คอนเทนเนอร์ |
| **กิกาลิซีร์** | ยาอายุวัฒนะ PaaS |
| **Fly.io** | โฮสติ้งแบบกระจาย |
| **เรนเดอร์** | แอพโฮสติ้ง |
| **Erlang ปล่อย** | ปล่อย OTP |
| **อัพเกรดโค้ดสุดฮอต** | การอัพเกรดแบบไม่ต้องหยุดทำงาน |
---

## สรุป
Erlang และ Elixir แบ่งปัน BEAM VM และ OTP ซึ่งนำเสนอการทำงานพร้อมกันและความทนทานต่อข้อผิดพลาดที่ไม่มีใครเทียบได้ สแต็ค Elixir มาตรฐานคือ: **Mix** สำหรับบิลด์, **Phoenix** สำหรับเว็บ, **Phoenix LiveView** สำหรับ UI แบบเรียลไทม์, **Ecto** สำหรับฐานข้อมูล, **ExUnit** สำหรับการทดสอบ, **Credo** สำหรับ Linting และ **Oban** สำหรับงานเบื้องหลัง Erlang ใช้ **rebar3** สำหรับบิลด์ **คาวบอย** สำหรับ HTTP และ **EUnit** หรือ **การทดสอบทั่วไป** สำหรับการทดสอบ ทั้งสองภาษามีความเป็นเลิศในด้านระบบแบบกระจาย แอปพลิเคชันแบบเรียลไทม์ (แชท เกม IoT) โทรคมนาคม และบริการที่มีความพร้อมใช้งานสูง จุดแข็งของระบบนิเวศคือปรัชญา "ปล่อยให้มันพัง" การอัพเกรดโค้ดด่วน กระบวนการที่ไม่ซับซ้อน และการส่งข้อความ