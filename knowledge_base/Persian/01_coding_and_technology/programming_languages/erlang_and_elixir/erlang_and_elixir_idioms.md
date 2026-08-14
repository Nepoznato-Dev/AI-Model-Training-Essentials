---
# Metadata
title: "Erlang & Elixir — Idiomatic Patterns & Best Practices"
description: "Idiomatic patterns and best practices for writing clean Erlang and Elixir code."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial idiomatic patterns guide"
tags: [erlang, elixir, idioms, patterns, best-practices, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Erlang & Elixir - الگوهای اصطلاحی و بهترین روش ها
این راهنما الگوهای اصطلاحی Erlang و Elixir را در BEAM VM پوشش می دهد.
---

## اصطلاحات اکسیر
```elixir
# ✅ Pipe operator
result = data
|> Enum.filter(&(&1.active))
|> Enum.map(&(&1.name))
|> Enum.sort()

# ✅ Pattern matching
{:ok, user} = find_user(1)
%{name: name, email: email} = user

# ✅ with for error chaining
with {:ok, user} <- find_user(id),
     {:ok, orders} <- get_orders(user) do
  {:ok, {user, orders}}
end

# ✅ Comprehensions
result = for item <- items, item.active, do: item.name

# ✅ defp for private functions
defmodule UserService do
  def find(id), do: Repo.get(User, id)
  defp validate(user), do: ...
end

# ✅ @spec for type specs
@spec find(pos_integer()) :: {:ok, User.t()} | {:error, :not_found}
```

---

## اصطلاحات ارلنگ
```erlang
%% ✅ Pattern matching
handle({ok, User}) -> process(User);
handle({error, Reason}) -> error(Reason).

%% ✅ List comprehensions
Adults = [U || U <- Users, U#user.age >= 18].

%% ✅ Case expressions
case find_user(Id) of
    {ok, User} -> process(User);
    {error, not_found} -> {error, not_found}
end.

%% ✅ try/catch for exceptions
try risky_operation() of
    Result -> handle(Result)
catch
    error:Reason -> {error, Reason}
end.

%% ✅ gen_server callback pattern
init(Args) -> {ok, State}.
handle_call(Msg, From, State) -> {reply, Response, NewState}.
handle_cast(Msg, State) -> {noreply, NewState}.
```

---

## خلاصه
اصطلاحات اکسیر تأکید دارند: عملگر لوله، تطبیق الگو،`with`برای زنجیره خطا، و مشخصات نوع `@spec`. اصطلاحات Erlang بر این موارد تاکید دارند: تطبیق الگو، درک لیست، بازخوانی سرور gen_server، و فلسفه "بگذار خراب شود". هر دو تغییر ناپذیری، ارسال پیام، و تحمل خطا ارزش دارند.