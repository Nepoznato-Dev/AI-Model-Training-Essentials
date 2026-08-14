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
# Julia — Ekosistem ve Araç İşleme Kılavuzu
Bu kılavuz, Julia ekosistemindeki temel araçları, paketleri ve altyapıyı kapsar.
---

## Julia Versiyonları
| Sürüm | Notlar |
|-----------|----------|
| **Julia 1.10+** | Mevcut durum stabil |
| **Julia 1.11** | Yeni özelliklerle en son |
| **Julia gecelik** | Geliştirme yapıları |
```bash
julia --version           # check version
julia script.jl           # run script
julia                     # interactive REPL
julia -e 'println("Hi")'  # inline execution
julia --project=.         # activate project environment
```

---

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **Pkt** | Yerleşik paket yöneticisi |
| **Genel Kayıt** | Resmi paket kaydı (10.000+ paket) |
| **PkgŞablonları** | Proje iskelesi |
| **Yerel Kayıt** | Özel kayıtlar |
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

## Veri Bilimi ve Bilgi İşlem
| Paket | Amaç |
|-----------|-----------|
| **Veri Çerçeveleri** | Tablo verileri (pandalar gibi) |
| **CSV** | CSV dosyası okuma/yazma |
| **Tablolar** | Tablo arayüzü |
| **Sorgu** | Sorgu anlama |
| **DataFramesMeta** | dplyr benzeri sözdizimi |
| **Ok** | Apache Oku / Parke |
| **JSON3** | Hızlı JSON ayrıştırma |
| **Yapı Türleri** | Tip kararlı JSON |
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

## Bilimsel Hesaplama
| Paket | Amaç |
|-----------|-----------|
| **Diferansiyel Denklemler** | ODE/SDE çözücüler |
| **Optimum** | Optimizasyon |
| **Atlama** | Matematiksel programlama |
| **Lineer Cebir** | Yerleşik doğrusal cebir |
| **SparseArrays** | Seyrek matrisler |
| **İstatistik Tabanı** | Temel istatistikler |
| **Dağıtımlar** | Olasılık dağılımları |
| **Hipotez Testleri** | İstatistiksel testler |
| **GLM** | Genelleştirilmiş doğrusal modeller |
| **Karışık Modeller** | Karışık efektli modeller |
| **Turing** | Bayes çıkarımı (MCMC) |
| **GelişmişHMC** | Hamiltoniyen Monte Carlo |
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

## Makine Öğrenimi
| Paket | Amaç |
|-----------|-----------|
| **Akı** | Derin öğrenme çerçevesi |
| **MLJ** | Makine öğrenimi araç kutusu |
| **MLUtils** | Veri yardımcı programları |
| **BetaML** | Başlangıç ​​dostu ML |
| **XGBoost** | Gradyan artırma |
| **Karar Ağacı** | Karar ağaçları |
| **Kümelenme** | Kümeleme algoritmaları |
| **Çok Değişkenli İstatistikler** | Boyut azaltma |
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

## Görselleştirme
| Paket | Amaç |
|-----------|-----------|
| **Arsalar** | Meta paket çizimi |
| **Makie** | Yüksek performanslı (GLMakie, CairoMakie) |
| **Atsineği** | Grafiklerin dilbilgisi (ggplot2 benzeri) |
| **Entrikacı** | İnteraktif grafikler |
| **İstatistik Grafikleri** | İstatistiksel görselleştirmeler |
| **Grafik Cebiri** | Grafiklerin dilbilgisi (Makie) |
```julia
using Plots, StatsPlots

# Simple plot
plot(rand(10), title="Random Data", label="Series 1")
scatter!(rand(10), label="Points")

# Grouped violin plot
@df df violin(:category, :value, group=:gender)
```

---

## Web ve HTTP
| Paket | Amaç |
|-----------|-----------|
| **HTTP** | HTTP istemcisi ve sunucusu |
| **Cin** | Tam yığın web çerçevesi |
| **Merly** | Hafif web çerçevesi |
| **JSON3** | JSON ayrıştırma |
| **İndirilenler** | Yerleşik indirmeler |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **Test** | Yerleşik test çerçevesi |
| **Su** | Paket kalite testleri |
| **JET** | Tip çıkarım analizi |
| **Belgeleyici** | Dokümantasyon oluşturma |
| **BenchmarkAraçları** | Karşılaştırma |
| **PkgŞablonları** | Testlerle birlikte proje iskelesi |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **JuliaFormatter** | Kod biçimlendirme |
| **JET** | Tip çıkarım analizi |
| **Su** | Paket kalite kontrolleri |
| **Açık İçe Aktarmalar** | Find implicit imports |
| **Cthulhu** | Type inspection |
| **BenchmarkAraçları** | Performans kıyaslaması |
```julia
# JuliaFormatter configuration (.JuliaFormatter.toml)
indent = 4
margin = 120
always_for_in = true
whitespace_typedefs = false
```

---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **Base** | Standart kütüphane |
| **Konular** | Çoklu iş parçacıklı |
| **Dağıtıldı** | Çoklu işlem |
| **Görevler** | Yeşil iplikler (koroutinler) |
| **Kanal** | Görevler arası iletişim |
| **StaticArrays** | Hızlı sabit boyutlu diziler |
| **FillArrays** | Tembel dolu diziler |
| **Zincir** | Pipe operator |
| **ChainableAnchor** | Pipe macros |
| **Birimli** | Fiziksel birimler |
| **Ölçümler** | Hata yayılımı |
| **Belgeleyici** | Dokümantasyon |
| **Revise** | Canlı kod yeniden yükleniyor |
| **OhMyREPL** | Geliştirilmiş REPL |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + Julia** | Resmi Julia uzantısı |
| **Plüton** | Etkileşimli defterler |
| **Jüpyter + IJulia** | Dizüstü bilgisayar arayüzü |
| **Neovim + julia-vim** | Terminal tabanlı |
| **IntelliJ + Julia** | JetBrains desteği |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Paket Derleyicisi** | Bağımsız ikili dosyalar |
| **Docker** | Konteynerde |
| **Genie + Docker** | Web uygulaması dağıtımı |
| **Plüton + statik dışa aktarma** | Defter yayıncılığı |
| **JupyterHub** | Çok kullanıcılı dizüstü bilgisayarlar |
| **JuliaHub** | Bulut Julia platformu |
```julia
using PackageCompiler

create_app("MyProject", "myapp_compiled";
    precompile_execution_file = "precompile.jl"
)
# Produces standalone binary
```

---

## Özet
Julia'nın ekosistemi bilimsel hesaplama ve yüksek performanslı sayısal analiz için özel olarak tasarlanmıştır. Standart yığın şudur: Çalışma zamanı olarak **Julia 1.10+**, IDE olarak **VS Code** veya **Pluto**, veri işleme için **DataFrames**, görselleştirme için **Plots** veya **Makie**, ODE'ler için **DifferentialEquations**, derin öğrenme için **Flux**, test için **Test** ve biçimlendirme için **JuliaFormatter**. Julia'nın güçlü yönleri çoklu gönderim, JIT derlemesi (LLVM), tür çıkarımı ve şekillendirilebilirliktir; Python kadar etkileyici olmasının yanı sıra C benzeri bir performansa ulaşır. Ekosistem bilimsel hesaplama, optimizasyon, diferansiyel denklemler ve makine öğrenimi araştırmalarında öne çıkıyor.