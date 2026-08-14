---
# Metadata
title: "Erlang & Elixir — Common Mistakes & Anti-Patterns"
description: "Common pitfalls, traps, and anti-patterns in Erlang and Elixir with explanations and corrections."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial common mistakes document"
tags: [erlang, elixir, common-mistakes, anti-patterns, pitfalls, otp, coding-and-technology]
difficulty_level: "intermediate"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

# एरलांग और अमृत - सामान्य गलतियाँ और विरोधी पैटर्न
यह दस्तावेज़ सुधार के साथ एरलांग और एलिक्सिर में सबसे आम गलतियों, जाल और विरोधी पैटर्न को सूचीबद्ध करता है।
---

## 1. एकल असाइनमेंट (एरलांग)
```erlang
% ❌ WRONG — expecting reassignment
X = 1.
X = 2.  % exception! X is already bound to 1

% ✅ CORRECT — use different variables or shadow
X1 = 1,
X2 = X1 + 1,

% Or in a new scope (function clause)
f(X) ->
    X = compute(),  % new X in this scope
    use(X).
```

---

## 2. प्रक्रियाओं को लिंक/निगरानी नहीं करना (एरलांग)
```erlang
% ❌ WRONG — fire-and-forget process
spawn(fun() -> risky_operation() end).
% If it crashes, nobody knows

% ✅ CORRECT — link or monitor
Pid = spawn_link(fun() -> risky_operation() end),
% If it crashes, this process gets an exit signal

% ✅ CORRECT — monitor for non-linked observation
Ref = monitor(process, Pid),
receive
    {'DOWN', Ref, process, Pid, Reason} ->
        handle_crash(Reason)
end
```

---

## 3. जेनसर्वर कॉल बिना टाइमआउट (अमृत)
```elixir
# ❌ WRONG — default 5s timeout
GenServer.call(server, :slow_operation)
# crashes with :timeout if operation takes > 5s

# ✅ CORRECT — explicit timeout
GenServer.call(server, :slow_operation, :infinity)
# or appropriate timeout
GenServer.call(server, :operation, 30_000)
```

---

## 4. बिना टाइमआउट के`receive`में पैटर्न मैच (एरलांग)
```erlang
% ❌ WRONG — blocks forever
receive
    {ok, Data} -> process(Data)
end.

% ✅ CORRECT — always use timeout
receive
    {ok, Data} -> process(Data)
after 5000 ->
    handle_timeout()
end.
```

---

## 5. नेस्टेड पैटर्न मिलान (एलिक्सिर) के लिए`with`का उपयोग नहीं करना
```elixir
# ❌ WRONG — deeply nested case
case authenticate(user) do
  {:ok, token} ->
    case authorize(token) do
      {:ok, perms} ->
        case fetch_data(perms) do
          {:ok, data} -> {:ok, data}
          {:error, e} -> {:error, e}
        end
      {:error, e} -> {:error, e}
    end
  {:error, e} -> {:error, e}
end

# ✅ CORRECT — use with
with {:ok, token} <- authenticate(user),
     {:ok, perms} <- authorize(token),
     {:ok, data} <- fetch_data(perms) do
  {:ok, data}
end
```

---

## 6. एंटी-पैटर्न: लंबे समय तक चलने वाला जेनसर्वर कॉलबैक
```elixir
# ❌ WRONG — blocking GenServer
def handle_call(:slow_op, _from, state) do
  result = :timer.sleep(10_000)  # blocks the server!
  {:reply, result, state}
end

# ✅ CORRECT — async work
def handle_call(:slow_op, from, state) do
  Task.start(fn ->
    result = compute()
    GenServer.reply(from, result)
  end)
  {:noreply, state}
end
```

---

## सारांश
एरलांग/एलिक्सिर ट्रैप: वेरिएबल एकल-असाइनमेंट हैं, प्रक्रियाओं को लिंक/मॉनिटर की आवश्यकता होती है, जेनसर्वर कॉल के लिए स्पष्ट टाइमआउट की आवश्यकता होती है,`receive`बिना टाइमआउट के हमेशा के लिए ब्लॉक हो जाता है, और जेनसर्वर कॉलबैक को ब्लॉक नहीं होना चाहिए। BEAM तरीका है: इसे क्रैश होने दें (पर्यवेक्षण के साथ), साफ पैटर्न मिलान के लिए`with`का उपयोग करें, जेनसर्वर कॉलबैक को तेज़ रखें, और हमेशा प्रक्रिया विफलताओं को संभालें।