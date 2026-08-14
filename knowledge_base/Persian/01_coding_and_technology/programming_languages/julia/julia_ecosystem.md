<!--
---
# Metadata
title: "Julia — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Julia ecosystem including tools, packages, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [julia, ecosystem, tooling, packages, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# جولیا - راهنمای اکوسیستم و ابزار
این راهنما ابزارها، بسته‌ها و زیرساخت‌های ضروری در اکوسیستم جولیا را پوشش می‌دهد.
---

## نسخه های جولیا
| نسخه | یادداشت ها |
|---------|-------|
| **Julia 1.10+** | پایدار فعلی |
| **جولیا 1.11** | جدیدترین ها با ویژگی های جدید |
| **شب جولیا** | توسعه می سازد |
```bash
julia --version           # check version
julia script.jl           # run script
julia                     # interactive REPL
julia -e 'println("Hi")'  # inline execution
julia --project=.         # activate project environment
```

---

## مدیریت بسته
| ابزار | هدف |
|------|---------|
| **Pkg** | مدیریت بسته داخلی |
| **دفتر ثبت عمومی** | رجیستری بسته های رسمی (10000+ بسته) |
| **PkgTemplates** | داربست پروژه |
| **LocalRegistry** | ثبت خصوصی |
```julia
# Pkg REPL (press ] in Julia REPL)
pkg> add DataFrames
pkg> add Plots, CSV, JSON
pkg> update
pkg> status
pkg> instantiate        # install from Manifest.toml

# Or programmatically
using Pkg
Pkg.add("DataFrames")
Pkg.add(name="DataFrames", version="1.6")
```

```toml
# Project.toml
name = "MyProject"
uuid = "..."
version = "0.1.0"

[deps]
DataFrames = "a93c6f00-e57d-5684-b7b6-d8193f3466e0"
Plots = "91a5bcdd-55d7-5caf-9e0b-520d859cae80"

[compat]
DataFrames = "1.6"
julia = "1.10"
```

---

## علم داده و محاسبات
| پکیج | هدف |
|---------|---------|
| **DataFrames** | داده های جدولی (مانند پانداها) |
| **CSV** | خواندن/نوشتن فایل CSV |
| **جدول** | رابط جدول |
| **پرس و جو** | درک پرس و جو |
| **DataFramesMeta** | نحو dplyr مانند |
| **پیکان** | پیکان آپاچی / پارکت |
| **JSON3** | تجزیه سریع JSON |
| **StructTypes** | JSON پایدار تایپ |
```julia
using DataFrames, CSV, Statistics

# Load and manipulate data
df = CSV.read("data.csv", DataFrame)

# Data manipulation
result = combine(groupby(df, :category),
    :value => mean => :avg_value,
    :value => std => :std_value,
    :value => length => :count
)

# Filtering and selecting
filtered = df[df.age .> 18 .&& .!ismissing.(df.name), :]
selected = select(df, :name, :age, :city)
```

---

## محاسبات علمی
| پکیج | هدف |
|---------|---------|
| **معادلات دیفرانسیل** | حل کننده های ODE/SDE |
| **بهینه** | بهینه سازی |
| **جهش** | برنامه نویسی ریاضی |
| **جبر خطی** | جبر خطی داخلی |
| **SparseArrays** | ماتریس های پراکنده |
| **StatsBase** | آمار پایه |
| **توزیعات** | توزیع احتمال |
| **تست فرضیه** | آزمون های آماری |
| **GLM** | مدل های خطی تعمیم یافته |
| **مدل های ترکیبی** | مدل های با جلوه های ترکیبی |
| **تورینگ** | استنتاج بیزی (MCMC) |
| **AdvancedHMC** | همیلتونی مونت کارلو |
```julia
using DifferentialEquations, Plots

# Solve ODE: Lorenz system
function lorenz!(du, u, p, t)
    σ, ρ, β = p
    du[1] = σ * (u[2] - u[1])
    du[2] = u[1] * (ρ - u[3]) - u[2]
    du[3] = u[1] * u[2] - β * u[3]
end

u0 = [1.0, 0.0, 0.0]
tspan = (0.0, 100.0)
p = (10.0, 28.0, 8/3)

prob = ODEProblem(lorenz!, u0, tspan, p)
sol = solve(prob)
plot(sol, vars=(1,2,3), title="Lorenz Attractor")
```

---

## یادگیری ماشینی
| پکیج | هدف |
|---------|---------|
| **شار** | چارچوب یادگیری عمیق |
| **MLJ** | جعبه ابزار یادگیری ماشین |
| **MLUtils** | ابزارهای داده |
| **بتام ال** | ML مناسب برای مبتدیان |
| **XGBoost** | افزایش گرادیان |
| **DecisionTree** | درختان تصمیم |
| **خوشه بندی** | الگوریتم های خوشه بندی |
| **MultivariateStats** | کاهش ابعاد |
```julia
using Flux

# Neural network
model = Chain(
    Dense(784 => 128, relu),
    Dropout(0.2),
    Dense(128 => 64, relu),
    Dense(64 => 10),
    softmax
)

loss(x, y) = crossentropy(model(x), y)
opt = Adam(0.001)

# Training loop
for epoch in 1:100
    for (x, y) in dataloader
        grads = gradient(Flux.params(model)) do
            loss(x, y)
        end
        Flux.update!(opt, Flux.params(model), grads)
    end
end
```

---

## تجسم
| پکیج | هدف |
|---------|---------|
| **قطعه** | طراحی متا پکیج |
| **مکی** | عملکرد بالا (GLMakie، CairoMakie) |
| **گادفلای** | گرامر گرافیک (مانند ggplot2) |
| **طرح** | طرح های تعاملی |
| **StatsPlots** | تجسم های آماری |
| **جبر گرافیک** | گرامر گرافیک (Makie) |
```julia
using Plots, StatsPlots

# Simple plot
plot(rand(10), title="Random Data", label="Series 1")
scatter!(rand(10), label="Points")

# Grouped violin plot
@df df violin(:category, :value, group=:gender)
```

---

## وب و HTTP
| پکیج | هدف |
|---------|---------|
| **HTTP** | سرویس گیرنده و سرور HTTP |
| **جن** | چارچوب وب تمام پشته |
| **مرلی** | چارچوب وب سبک |
| **JSON3** | تجزیه JSON |
| **دانلود** | دانلودهای داخلی |
```julia
using HTTP, JSON3

# HTTP server
HTTP.listen!("0.0.0.0", 8080) do req
    if req.target == "/hello"
        HTTP.Response(200, "Hello, World!")
    elseif startswith(req.target, "/users/")
        id = parse(Int, split(req.target, "/")[3])
        JSON3.json(Dict("id" => id, "name" => "User $id"))
    else
        HTTP.Response(404, "Not Found")
    end
end
```

---

## تست
| چارچوب | هدف |
|-----------|---------|
| **تست** | چارچوب تست داخلی |
| **آکوا** | تست کیفیت بسته بندی |
| **JET** | تحلیل استنتاج نوع |
| **مستندگر** | تولید مستندات |
| **BenchmarkTools** | محک زدن |
| **PkgTemplates** | پروژه داربست با تست |
```julia
using Test

@testset "UserService" begin
    @testset "find user" begin
        service = UserService()
        add_user!(service, User(1, "Alice"))
        
        user = find_user(service, 1)
        @test user.name == "Alice"
        
        @test isnothing(find_user(service, 999))
    end
    
    @testset "type stability" begin
        service = UserService()
        @inferred find_user(service, 1)
    end
end
```

```bash
julia --project -e 'using Pkg; Pkg.test()'
julia --project -e 'using Pkg; Pkg.test(coverage=true)'
```

---

## کیفیت کد
| ابزار | هدف |
|------|---------|
| **JuliaFormatter** | قالب بندی کد |
| **JET** | تحلیل استنتاج نوع |
| **آکوا** | بررسی کیفیت بسته بندی |
| **ExplicitImports** | واردات ضمنی را پیدا کنید |
| **Cthulhu** | بازرسی نوع |
| **BenchmarkTools** | معیار عملکرد |
```julia
# JuliaFormatter configuration (.JuliaFormatter.toml)
indent = 4
margin = 120
always_for_in = true
whitespace_typedefs = false
```

---

## کتابخانه های کلیدی
| کتابخانه | هدف |
|---------|---------|
| **پایه** | کتابخانه استاندارد |
| **موضوع** | چند رشته ای |
| **توزیع** | پردازش چندگانه |
| **وظایف** | نخ های سبز (کوروتین) |
| **کانال** | ارتباط بین وظایف |
| **StaticArrays** | آرایه های با اندازه ثابت سریع |
| **FillArrays** | آرایه های پر تنبل |
| **زنجیره** | اپراتور لوله |
| **Chainable Anchor** | ماکروهای لوله |
| **یکپارچه** | واحدهای فیزیکی |
| **اندازه گیری** | انتشار خطا |
| **مستندگر** | مستندات |
| **بازبینی** | بارگذاری مجدد کد زنده |
| **OhMyREPL** | REPL پیشرفته |
---

## IDE ها و ویرایشگرها
| IDE | نقاط قوت |
|-----|-----------|
| **VS Code + جولیا** | پسوند رسمی جولیا |
| **پلوتون** | نوت بوک های تعاملی |
| **ژوپیتر + ایجولیا** | رابط نوت بوک |
| **Neovim + julia-vim** | مبتنی بر ترمینال |
| **IntelliJ + جولیا** | پشتیبانی JetBrains |
---

## استقرار
| روش | یادداشت ها |
|--------|-------|
| **PackageCompiler** | باینری های مستقل |
| **داکر** | کانتینری |
| **جن + داکر** | استقرار برنامه وب |
| **پلوتون + صادرات استاتیک** | انتشارات نوت بوک |
| **JupyterHub** | نوت بوک چند کاربره |
| **JuliaHub** | پلت فرم ابر جولیا |
```julia
using PackageCompiler

create_app("MyProject", "myapp_compiled";
    precompile_execution_file = "precompile.jl"
)
# Produces standalone binary
```

---

## خلاصه
اکوسیستم جولیا برای محاسبات علمی و تحلیل عددی با کارایی بالا ساخته شده است. پشته استاندارد عبارتند از: **Julia 1.10+** به عنوان زمان اجرا، **VS Code** یا **Pluto** به عنوان IDE، **DataFrames** برای دستکاری داده ها، **Plots** یا **Makie** برای تجسم، **DifferentialEquations** برای ODE، **Flux*********J برای قالب بندی عمیق، آزمون Test. نقاط قوت جولیا شامل ارسال چندگانه، کامپایل JIT (LLVM)، استنتاج نوع و ترکیب‌پذیری است – عملکردی شبیه به زبان C را به دست می‌آورد در حالی که به اندازه پایتون گویا است. این اکوسیستم در محاسبات علمی، بهینه سازی، معادلات دیفرانسیل و تحقیقات یادگیری ماشین برتری دارد.