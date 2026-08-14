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
# Julia — Gabay sa Ecosystem at Tooling
Sinasaklaw ng gabay na ito ang mahahalagang kasangkapan, pakete, at imprastraktura sa Julia ecosystem.
---

## Mga Bersyon ng Julia
| Bersyon | Mga Tala |
|---------|-------|
| **Julia 1.10+** | Kasalukuyang kuwadra |
| **Julia 1.11** | Pinakabagong may mga bagong feature |
| **Julia gabi-gabi** | Binubuo ang pag-unlad |
```bash
julia --version           # check version
julia script.jl           # run script
julia                     # interactive REPL
julia -e 'println("Hi")'  # inline execution
julia --project=.         # activate project environment
```

---

## Pamamahala ng Package
| Tool | Layunin |
|------|---------|
| **Pkg** | Built-in na manager ng package |
| **Pangkalahatang Rehistro** | Opisyal na pagpapatala ng package (10,000+ package) |
| **PkgTemplates** | Project scaffolding |
| **LocalRegistry** | Mga pribadong rehistro |
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

## Data Science at Computing
| Package | Layunin |
|---------|---------|
| **DataFrames** | Tabular data (tulad ng mga pandas) |
| **CSV** | Pagbabasa/pagsusulat ng CSV file |
| **Mga Talahanayan** | Interface ng talahanayan |
| **Query** | Pag-unawa sa query |
| **DataFramesMeta** | dplyr-like syntax |
| **Arrow** | Apache Arrow / Parquet |
| **JSON3** | Mabilis na pag-parse ng JSON |
| **StructTypes** | Type-stable na JSON |
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

## Scientific Computing
| Package | Layunin |
|---------|---------|
| **DifferentialEquation** | Mga solver ng ODE/SDE |
| **Optim** | Pag-optimize |
| **JuMP** | Mathematical programming |
| **LinearAlgebra** | Built-in na linear algebra |
| **SparseArrays** | Kalat-kalat na matrice |
| **StatsBase** | Pangunahing istatistika |
| **Mga Pamamahagi** | Mga pamamahagi ng posibilidad |
| **Mga Pagsusulit sa Hypothesis** | Mga pagsusulit sa istatistika |
| **GLM** | Mga pangkalahatang linear na modelo |
| **Mga MixedModel** | Mixed-effects na mga modelo |
| **Turing** | Bayesian inference (MCMC) |
| **AdvancedHMC** | Hamiltonian Monte Carlo |
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

## Machine Learning
| Package | Layunin |
|---------|---------|
| **Pagbabago** | Deep learning framework |
| **MLJ** | Machine learning toolbox |
| **MLUtils** | Mga kagamitan sa data |
| **BetaML** | Beginner-friendly ML |
| **XGBoost** | Pagpapalakas ng gradient |
| **DecisionTree** | Mga puno ng desisyon |
| **Clustering** | Mga algorithm ng clustering |
| **MultivariateStats** | Pagbabawas ng dimensyon |
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

## Visualization
| Package | Layunin |
|---------|---------|
| **Mga Plot** | Pag-plot ng meta-package |
| **Makie** | Mataas na pagganap (GLMakie, CairoMakie) |
| **Gadfly** | Grammar ng mga graphics (ggplot2-like) |
| **Plotly** | Mga interactive na plot |
| **StatsPlots** | Mga visualization ng istatistika |
| **AlgebraOfGraphics** | Grammar ng mga graphics (Makie) |
```julia
using Plots, StatsPlots

# Simple plot
plot(rand(10), title="Random Data", label="Series 1")
scatter!(rand(10), label="Points")

# Grouped violin plot
@df df violin(:category, :value, group=:gender)
```

---

## Web at HTTP
| Package | Layunin |
|---------|---------|
| **HTTP** | HTTP client at server |
| **Genie** | Full-stack na web framework |
| **Merly** | Magaan na web framework |
| **JSON3** | Pag-parse ng JSON |
| **Mga Download** | Mga built-in na download |
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

## Pagsubok
| Balangkas | Layunin |
|-----------|---------|
| **Pagsubok** | Built-in na balangkas ng pagsubok |
| **Aqua** | Mga pagsubok sa kalidad ng package |
| **JET** | Uri ng pagsusuri ng hinuha |
| **Docuenter** | Pagbuo ng dokumentasyon |
| **BenchmarkTools** | Pag-benchmark |
| **PkgTemplates** | Project scaffolding na may mga pagsubok |
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

## Kalidad ng Code
| Tool | Layunin |
|------|---------|
| **JuliaFormatter** | Pag-format ng code |
| **JET** | Uri ng pagsusuri ng hinuha |
| **Aqua** | Mga pagsusuri sa kalidad ng package |
| **ExplicitImports** | Maghanap ng mga implicit na pag-import |
| **Cthulhu** | Uri ng inspeksyon |
| **BenchmarkTools** | Pag-benchmark ng pagganap |
```julia
# JuliaFormatter configuration (.JuliaFormatter.toml)
indent = 4
margin = 120
always_for_in = true
whitespace_typedefs = false
```

---

## Mga Pangunahing Aklatan
| Aklatan | Layunin |
|---------|---------|
| **Base** | Karaniwang aklatan |
| **Mga Thread** | Multi-threading |
| **Ibinahagi** | Multi-processing |
| **Mga Gawain** | Mga berdeng thread (coroutine) |
| **Channel** | Komunikasyon sa pagitan ng mga gawain |
| **Mga StaticArray** | Mabilis na fixed-size array |
| **FillArrays** | Lazy filled arrays |
| **Kadena** | Operator ng tubo |
| **ChainableAnchor** | Mga pipe macro |
| **Unitful** | Mga pisikal na yunit |
| **Mga Pagsukat** | Error sa pagpapalaganap |
| **Docuenter** | Dokumentasyon |
| **Baguhin** | Live code reloading |
| **OhMyREPL** | Pinahusay na REPL |
---

## Mga IDE at Editor
| IDE | Mga Lakas |
|-----|-----------|
| **VS Code + Julia** | Opisyal na extension ni Julia |
| **Pluto** | Mga interactive na notebook |
| **Jupyter + IJulia** | Interface ng notebook |
| **Neovim + julia-vim** | Nakabatay sa terminal |
| **IntelliJ + Julia** | Suporta sa JetBrains |
---

## Deployment
| Paraan | Mga Tala |
|--------|-------|
| **PackageCompiler** | Mga standalone na binary |
| **Docker** | Naka-container |
| **Genie + Docker** | Pag-deploy ng web app |
| **Pluto + static na pag-export** | Pag-publish ng notebook |
| **JupyterHub** | Mga multi-user na notebook |
| **JuliaHub** | Cloud Julia platform |
```julia
using PackageCompiler

create_app("MyProject", "myapp_compiled";
    precompile_execution_file = "precompile.jl"
)
# Produces standalone binary
```

---

## Buod
Ang ecosystem ni Julia ay sadyang binuo para sa siyentipikong pag-compute at mataas na pagganap ng numerical analysis. Ang karaniwang stack ay: **Julia 1.10+** bilang runtime, **VS Code** o **Pluto** bilang IDE, **DataFrames** para sa pagmamanipula ng data, **Plots** o **Makie** para sa visualization, **DifferentialEquations** para sa ODEs, **Flux** para sa malalim na pag-aaral, **Test** para sa pagsubok, at **JuliatingFormatter** Ang mga lakas ni Julia ay maramihang dispatch, JIT compilation (LLVM), type inference, at composability — nakakamit nito ang tulad-C na pagganap habang nagpapahayag ng Python. Ang ecosystem ay mahusay sa scientific computing, optimization, differential equation, at machine learning research.