---
# Metadata
title: "Haskell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Haskell ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [haskell, ecosystem, tooling, cabal, stack, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---
# Haskell — Ecossistema e Guia de Ferramentas
Este guia cobre as ferramentas, estruturas e infraestrutura essenciais do ecossistema Haskell.
---

## Conjunto de ferramentas
| Ferramenta | Finalidade |
|------|---------|
| **GHC** | Compilador Glasgow Haskell (o compilador) |
| **GHCup** | Instalador do conjunto de ferramentas Haskell |
| **Cabal** | Construir sistema e formato de pacote |
| **Pilha** | Ferramenta de construção reproduzível |
| **instalar cabal** | Gerenciador de pacotes |
| **servidor de linguagem haskell (HLS)** | Servidor LSP |
| **ghcid** | Feedback de compilação rápida |
| **quatromolu** | Formatador de código |
| **ormolu** | Formatador de código |
| **hlint** | Linter / sugestões |
```bash
ghcup install ghc latest    # install GHC
ghcup install cabal latest  # install Cabal
ghcup install stack latest  # install Stack

cabal init                  # new project
cabal build                 # build
cabal test                  # run tests
cabal run myapp             # run
cabal repl                  # interactive REPL

stack new myapp             # new project
stack build                 # build
stack test                  # run tests
stack exec myapp            # run
```

---

## Gerenciamento de pacotes
| Ferramenta | Finalidade |
|------|---------|
| **Hackeamento** | Repositório central de pacotes (mais de 15.000 pacotes) |
| **Pilhagem** | Conjuntos de pacotes compatíveis e selecionados |
| **Cabal** | Formato de pacote e ferramenta de construção |
| **Pilha** | Construções reproduzíveis (instantâneos LTS) |
```cabal
-- myapp.cabal
cabal-version: 3.0
name:          myapp
version:       0.1.0.0
build-type:    Simple

executable myapp
  main-is:          Main.hs
  hs-source-dirs:   app
  default-language:  Haskell2010
  build-depends:     base >=4.18
                   , text
                   , aeson
                   , http-types
                   , warp
  ghc-options:      -Wall -Werror
```

```yaml
# stack.yaml
resolver: lts-22.12
packages:
  - .
extra-deps:
  - some-package-1.0.0
```

---

## Estruturas Web
| Estrutura | Tipo | Melhor para |
|-----------|------|----------|
| **Servo** | Nível de tipo | APIs de tipo seguro |
| **Sim,** | Pilha completa | Aplicativos da web com segurança de digitação |
| **Scotty** | Leve | APIs simples (semelhantes ao Sinatra) |
| **Spock** | Leve | Aplicativos da web |
| **IHP** | Baterias incluídas | Semelhante a Rails, Haskell |
| **Misô** | Interface | Interface tipo Elm |
```haskell
-- Servant API example
type UserAPI =
       "users" :> Get '[JSON] [User]
  :<|> "users" :> Capture "id" Int :> Get '[JSON] User
  :<|> "users" :> ReqBody '[JSON] User :> Post '[JSON] User

server :: Server UserAPI
server = listUsers :<|> getUser :<|> createUser

api :: Proxy UserAPI
api = Proxy

app :: Application
app = serve api server

main :: IO ()
main = run 8080 app
```

---

## Banco de dados
| Tecnologia | Tipo |
|------------|------|
| **persistente** | ORM (ecossistema Yesod) |
| **hasql** | PostgreSQL (alto desempenho) |
| **postgresql-simples** | PostgreSQL (simples) |
| **feixe** | SQL com segurança de tipo |
| **esqueleto** | ESQL de tipo seguro (em persistente) |
| **hedis** | Cliente Redis |
| **mongoDB** | Driver MongoDB |
```haskell
-- postgresql-simple example
import Database.PostgreSQL.Simple

main :: IO ()
main = do
  conn <- connect defaultConnectInfo { connectDatabase = "mydb" }
  users <- query_ conn "SELECT id, name, email FROM users" :: IO [User]
  mapM_ print users
```

---

## Teste
| Estrutura | Finalidade |
|-----------|---------|
| **HUunidade** | Teste unitário (estilo xUnit) |
| **saboroso** | Estrutura de teste (combinável) |
| ** caça saborosa ** | Integração HUnit para saboroso |
| **verificação rápida saborosa** | Testes baseados em propriedades |
| **Verificação Rápida** | Testes baseados em propriedades |
| **ouriço** | Baseado em propriedade (moderno) |
| **hspec** | Teste estilo BDD |
| **docteste** | Exemplos de teste em Haddock |
| **descoberta saborosa** | Testes de descoberta automática |
```haskell
-- hspec example
module UserServiceSpec (spec) where

import Test.Hspec
import UserService

spec :: Spec
spec = describe "UserService" $ do
  describe "find" $ do
    it "returns user when found" $ do
      let repo = mkRepo [(1, "Alice")]
          service = mkService repo
      findUser service 1 `shouldReturn` Just (User 1 "Alice")

    it "returns Nothing when not found" $ do
      let repo = mkRepo []
          service = mkService repo
      findUser service 999 `shouldReturn` Nothing

-- QuickCheck property
prop_reverse :: [Int] -> Bool
prop_reverse xs = reverse (reverse xs) == xs
```

---

## Qualidade do código
| Ferramenta | Finalidade |
|------|---------|
| **hlint** | Sugestões e linting |
| **quatromolu / ormolu** | Formatação de código |
| **haskell estiloso** | Formatação de código |
| **capinador** | Detecção de código morto |
| **stan** | Análise estática |
| **servidor de linguagem haskell** | Diagnósticos, conclusões |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Bibliotecas principais
| Biblioteca | Finalidade |
|--------|---------|
| **base** | Biblioteca padrão (Prelude) |
| **texto** | Tipos de texto eficientes |
| **bytestring** | Dados binários |
| **ason** | Biblioteca JSON |
| **contêineres** | Mapas, conjuntos, sequências |
| **contêineres não encomendados** | Mapas de hash, conjuntos de hash |
| **vetor** | Matrizes eficientes |
| **estm** | Memória transacional de software |
| **assíncrono** | Cálculos assíncronos |
| **optparse-aplicativo** | Análise de argumento CLI |
| **optparse-genérico** | CLI derivada automaticamente |
| **distorção** | Servidor HTTP |
| **cliente http** | Cliente HTTP |
| **conduíte** | Transmissão de dados |
| **tubos** | Transmissão de dados |
| **transmissão** | Transmissão de dados |
| **lente** | Biblioteca óptica |
| **megaparsec** | Combinadores de analisador |
| **parsec** | Combinadores de analisador |
| **reludir** | Melhor Prelúdio |
| **reludir** | Prelúdio Alternativo |
---

## IDEs e editores
| IDE | Pontos fortes |
|-----|-----------|
| **Código VS + HLS** | Melhor suporte Haskell LSP |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Baseado em terminal com LSP |
| **Emacs + modo haskell** | Ambiente Haskell clássico |
| **Vim + vim-haskell** | Integração Vim |
---

## Implantação
| Método | Notas |
|-------|-------|
| **Binário estático** | GHC produz binários estáticos |
| **Docker** | Construções em vários estágios (imagem haskell) |
| **Nix** | Construções reproduzíveis |
| **Kubernetes** | Orquestração |
| **AWS Lambda** | Sem servidor (via hal) |
```dockerfile
# Multi-stage Docker build
FROM haskell:9.6 AS builder
WORKDIR /app
COPY . .
RUN cabal build --only-dependencies
RUN cabal build

FROM debian:bookworm-slim
COPY --from=builder /app/dist-newstyle/build/*/myapp /usr/local/bin/
CMD ["myapp"]
```

---

## Resumo
O ecossistema de Haskell é único em sua ênfase na correção e segurança de tipo. O conjunto de ferramentas padrão é: **GHC** como compilador, **GHCup** para instalação, **Cabal** ou **Stack** para compilações, **haskell-language-server** para suporte IDE, **hlint** para linting, **fourmolu** para formatação e **tasty + QuickCheck** para testes. As principais bibliotecas incluem **aeson** para JSON, **text** para strings, **servant** para APIs de tipo seguro, **lens** para óptica e **stm** para simultaneidade. Haskell é excelente em compiladores, sistemas financeiros, sistemas simultâneos e em qualquer lugar que a correção seja fundamental. A curva de aprendizado é íngreme, mas a recompensa é um software que funciona corretamente por construção.