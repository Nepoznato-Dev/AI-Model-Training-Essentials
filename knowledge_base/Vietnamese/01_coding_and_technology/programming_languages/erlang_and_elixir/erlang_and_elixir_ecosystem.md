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
# Erlang & Elixir — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Erlang và Elixir, chia sẻ BEAM VM và OTP.
---

## Thời gian chạy & VM
| Thành phần | Mục đích |
|----------||----------|
| **CHIA** | Máy ảo Erlang |
| **OTP** | Nền tảng viễn thông mở (Erlang) |
| **Erlang/OTP** | Thời gian chạy Erlang + thư viện |
| **Thuốc tiên** | Ngôn ngữ hiện đại trên BEAM |
```bash
erl -version              # Erlang version
elixir --version          # Elixir version
iex                       # Elixir interactive
erl                       # Erlang interactive
```

---

## Công cụ xây dựng
| Công cụ | Ngôn ngữ | Mục đích |
|------|----------|----------|
| **Trộn** | Thuốc tiên | Công cụ xây dựng, người chạy nhiệm vụ |
| **cốt thép3** | Erlang | Công cụ xây dựng, trình quản lý phụ thuộc |
| **hex** | Cả hai | Quản lý gói |
| **hex.pm** | Cả hai | Kho gói |
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

## Khung web
| Khung | Ngôn ngữ | Loại |
|----------|----------|------|
| **Phượng Hoàng** | Thuốc tiên | Web đầy đủ (phổ biến nhất) |
| **Chế độ xem trực tiếp của Phoenix** | Thuốc tiên | Giao diện người dùng kết xuất máy chủ thời gian thực |
| **Kẻ cướp** | Thuốc tiên | Máy chủ HTTP Pure-Elixir |
| **Cao bồi** | Erlang | Máy chủ HTTP |
| **Ông chủ Chicago** | Erlang | Giống Django |
| **N2O** | Erlang | Khung WebSocket |
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

## Cơ sở dữ liệu
| Công nghệ | Ngôn ngữ | Loại |
|----------||----------|------|
| **Ecto** | Thuốc tiên | Trình bao bọc cơ sở dữ liệu + truy vấn |
| **Postgrex** | Thuốc tiên | Trình điều khiển PostgreSQL |
| **MyXQL** | Thuốc tiên | Trình điều khiển MySQL |
| **epgsql** | Erlang | Trình điều khiển PostgreSQL |
| **Mnesia** | Erlang | DB phân tán tích hợp |
| **Riak** | Erlang | Khóa-giá trị được phân phối |
| **CouchDB** | Erlang | Cơ sở dữ liệu tài liệu |
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

##Thử nghiệm
| Khung | Ngôn ngữ | Mục đích |
|----------|----------|----------|
| **ExUnit** | Thuốc tiên | Khung kiểm tra tích hợp |
| **EUĐơn vị** | Erlang | Kiểm tra đơn vị Erlang |
| **Kiểm tra chung** | Erlang | Khung kiểm tra OTP |
| **PropCheck** | Thuốc tiên | Dựa trên thuộc tính (QuickCheck) |
| **Dữ liệu truyền phát** | Thuốc tiên | Thử nghiệm dựa trên tài sản |
| **Mox** | Thuốc tiên | Chế giễu |
| **Wallaby** | Thuốc tiên | Kiểm tra trình duyệt |
| **Đặc biệt** | Thuốc tiên | Phong cách BDD |
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

## Chất lượng mã
| Công cụ | Ngôn ngữ | Mục đích |
|------|----------|----------|
| **Tín ngưỡng** | Thuốc tiên | Linting và phong cách |
| **dialyxir** | Thuốc tiên | Tích hợp máy lọc máu |
| **Dưới đây** | Thuốc tiên | Phân tích bảo mật |
| **erlang_ls** | Erlang | Máy chủ ngôn ngữ |
| **elvis** | Erlang | Kiểm tra phong cách |
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

## Đồng thời và phân phối
| Tính năng | Mục đích |
|----------|----------|
| **Quy trình** | Nhẹ, biệt lập |
| **Truyền tin nhắn** | Gửi/nhận giữa các tiến trình |
| **GenServer** | Mẫu máy khách-máy chủ |
| **Giám sát** | Khả năng chịu lỗi |
| **Ứng tuyển** | Thành phần OTP |
| **Phân phối** | Giao tiếp đa nút |
| **Mnesia** | Cơ sở dữ liệu phân tán |
| **libcluster** | Hình thành cụm |
| **Bầy đàn** | Đăng ký quy trình phân tán |
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

## Thư viện chính
| Thư viện | Ngôn ngữ | Mục đích |
|----------|----------|---------|
| **Phượng Hoàng** | Thuốc tiên | Khung web |
| **Ecto** | Thuốc tiên | Cơ sở dữ liệu |
| **Absinthe** | Thuốc tiên | Đồ thịQL |
| **Sân khấu Broadway** | Thuốc tiên | Đường ống dữ liệu |
| **Oban** | Thuốc tiên | Công việc nền tảng |
| **Tesla** | Thuốc tiên | Máy khách HTTP |
| **Chim sẻ** | Thuốc tiên | Máy khách HTTP |
| **Tùy chọn nhanh nhẹn** | Thuốc tiên | Xác thực tùy chọn |
| **Timex** | Thuốc tiên | Ngày/giờ |
| **Jason** | Thuốc tiên | JSON |
| **cao bồi** | Erlang | Máy chủ HTTP |
| **trang trại** | Erlang | Chấp nhận ổ cắm |
| **lager** | Erlang | Ghi nhật ký |
| **jsx** | Erlang | JSON |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS + ElixirLS** | Hỗ trợ Elixir tốt nhất |
| **IntelliJ + Elixir** | Hỗ trợ JetBrains |
| **Vim + nhà giả kim.vim** | Thuốc tiên Vim |
| **Emacs + chế độ erlang** | Erlang cổ điển |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Bản phát hành hỗn hợp** | Bản phát hành khép kín |
| **Docker** | Được đóng gói |
| **Gigalixir** | Thuốc tiên PaaS |
| **Fly.io** | Lưu trữ phân phối |
| **Kết xuất** | Lưu trữ ứng dụng |
| **Phát hành Erlang** | Phát hành OTP |
| **Nâng cấp mã nóng** | Nâng cấp không có thời gian ngừng hoạt động |
---

## Bản tóm tắt
Erlang và Elixir chia sẻ BEAM VM và OTP, cung cấp khả năng xử lý đồng thời và khả năng chịu lỗi chưa từng có. Ngăn xếp Elixir tiêu chuẩn là: **Mix** cho bản dựng, **Phoenix** cho web, **Phoenix LiveView** cho giao diện người dùng thời gian thực, **Ecto** cho cơ sở dữ liệu, **ExUnit** cho thử nghiệm, **Credo** cho linting và **Oban** cho các tác vụ nền. Erlang sử dụng **rebar3** cho các bản dựng, **Cowboy** cho HTTP và **EUnit** hoặc **Common Test** để thử nghiệm. Cả hai ngôn ngữ đều vượt trội ở các hệ thống phân tán, ứng dụng thời gian thực (trò chuyện, chơi game, IoT), viễn thông và các dịch vụ có tính sẵn sàng cao. Điểm mạnh của hệ sinh thái là triết lý "hãy để nó sụp đổ", nâng cấp mã nóng, quy trình nhẹ và truyền thông điệp.