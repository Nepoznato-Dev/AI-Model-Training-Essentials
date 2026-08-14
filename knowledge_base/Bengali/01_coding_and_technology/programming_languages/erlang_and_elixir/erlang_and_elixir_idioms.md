<!--
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

-->
# এরলাং এবং ইলিক্সির — ইডিওম্যাটিক প্যাটার্নস এবং সেরা অনুশীলন
এই নির্দেশিকাটি BEAM VM-এ Erlang এবং Elixir-এর জন্য বাহাদুরিমূলক নিদর্শন কভার করে।
---

## এলিক্সির ইডিয়ম
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

## এরলাং ইডিয়ম
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

## সারাংশ
এলিক্সির ইডিয়মগুলি জোর দেয়: পাইপ অপারেটর, প্যাটার্ন ম্যাচিং, ত্রুটি চেইনিংয়ের জন্য `with`, এবং`@spec`টাইপ স্পেক্স৷ Erlang বাগধারা জোর দেয়: প্যাটার্ন ম্যাচিং, তালিকা বোঝা, gen_server কলব্যাক, এবং "লেট ইট ক্র্যাশ" দর্শন। উভয়ই অপরিবর্তনীয়তা, বার্তা প্রেরণ এবং দোষ সহনশীলতাকে মূল্য দেয়।