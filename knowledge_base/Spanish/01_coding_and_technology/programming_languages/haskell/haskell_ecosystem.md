---
# Metadata
title: "Haskell — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Haskell ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
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

# Haskell: guía de ecosistemas y herramientas
Esta guía cubre las herramientas, marcos e infraestructura esenciales en el ecosistema de Haskell.
---

## Cadena de herramientas
| Herramienta | Propósito |
|------|---------|
| **GHC** | Compilador Haskell de Glasgow (el compilador) |
| **Copa GHC** | Instalador de cadena de herramientas Haskell |
| **Cábala** | Sistema de compilación y formato de paquete |
| **Pila** | Herramienta de construcción reproducible |
| **cabal-instalar** | Administrador de paquetes |
| **servidor de lenguaje haskell (HLS)** | Servidor LSP |
| **ghcid** | Comentarios de compilación rápida |
| **cuatromolu** | Formateador de código |
| **ormolu** | Formateador de código |
| **pedido** | Linter / sugerencias |
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

## Gestión de paquetes
| Herramienta | Propósito |
|------|---------|
| **Hackeo** | Repositorio central de paquetes (más de 15.000 paquetes) |
| **Apilamiento** | Conjuntos de paquetes seleccionados y compatibles |
| **Cábala** | Formato de paquete y herramienta de construcción |
| **Pila** | Construcciones reproducibles (instantáneas LTS) |
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

## Marcos web
| Marco | Tipo | Mejor para |
|-----------|------|----------|
| **Sirviente** | Nivel de tipo | API de tipo seguro |
| **Síod** | Pila completa | Aplicaciones web con seguridad de escritura |
| **Escocés** | Ligero | API simples (tipo Sinatra) |
| **Spock** | Ligero | Aplicaciones web |
| **PHI** | Pilas incluidas | Tipo rieles, Haskell |
| **Miso** | Interfaz | Frontal tipo olmo |
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

## Base de datos
| Tecnología | Tipo |
|------------|------|
| **persistente** | ORM (ecosistema Yesod) |
| **hasql** | PostgreSQL (alto rendimiento) |
| **postgresql-simple** | PostgreSQL (sencillo) |
| **haz** | SQL con seguridad de tipos |
| **esqueleto** | ESQL con seguridad de tipos (en persistente) |
| **hedis** | Cliente Redis |
| **mongoDB** | Controlador MongoDB |
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

## Pruebas
| Marco | Propósito |
|-----------|------------------|
| **Unidad HU** | Pruebas unitarias (estilo xUnit) |
| **sabroso** | Marco de prueba (componible) |
| **sabroso-hunit** | Integración HUnit para sabroso |
| **comprobación rápida y sabrosa** | Pruebas basadas en propiedades |
| **Comprobación rápida** | Pruebas basadas en propiedades |
| **erizo** | Basado en propiedad (moderno) |
| **hspec** | Pruebas estilo BDD |
| **prueba documental** | Ejemplos de prueba en Haddock |
| **sabroso-descubrir** | Pruebas de descubrimiento automático |
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

## Calidad del código
| Herramienta | Propósito |
|------|---------|
| **pedido** | Sugerencias y pelusa |
| **cuatromolu / ormolu** | Formato de código |
| **haskell con estilo** | Formato de código |
| **desyerbador** | Detección de código muerto |
| **stan** | Análisis estático |
| **servidor-idioma-haskell** | Diagnósticos, completaciones |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Bibliotecas clave
| Biblioteca | Propósito |
|---------|---------|
| **base** | Biblioteca estándar (Preludio) |
| **texto** | Tipos de texto eficientes |
| **cadena de bytes** | Datos binarios |
| **esón** | Biblioteca JSON |
| **contenedores** | Mapas, conjuntos, secuencias |
| **contenedores-desordenados** | Mapas hash, conjuntos hash |
| **vector** | Matrices eficientes |
| **stm** | Memoria transaccional de software |
| **asíncrono** | Cálculos asíncronos |
| **optparse-aplicativo** | Análisis de argumentos CLI |
| **optparse-genérico** | CLI derivada automáticamente |
| **deformación** | Servidor HTTP |
| **cliente http** | Cliente HTTP |
| **conducto** | Transmisión de datos |
| **tuberías** | Transmisión de datos |
| **transmisión** | Transmisión de datos |
| **lente** | Biblioteca de óptica |
| **megapársec** | Combinadores de analizadores |
| **pársec** | Combinadores de analizadores |
| **reludio** | Mejor Preludio |
| **reludio** | Preludio alternativo |
---

## IDE y editores
| IDE | Fortalezas |
|-----|-----------|
| **Código VS + HLS** | El mejor soporte LSP de Haskell |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Basado en terminal con LSP |
| **Emacs + modo haskell** | Entorno clásico de Haskell |
| **Vim + vim-haskell** | Integración Vim |
---

## Implementación
| Método | Notas |
|--------|-------|
| **Binario estático** | GHC produce binarios estáticos |
| **Acoplador** | Construcciones de varias etapas (imagen de Haskell) |
| **Nada** | Construcciones reproducibles |
| **Kubernetes** | Orquestación |
| **AWS Lambda** | Sin servidor (a través de hal) |
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

## Resumen
El ecosistema de Haskell es único en su énfasis en la corrección y la seguridad de tipos. La cadena de herramientas estándar es: **GHC** como compilador, **GHCup** para instalación, **Cabal** o **Stack** para compilaciones, **haskell-language-server** para soporte IDE, **hlint** para linting, **fourmolu** para formatear y **tasty + QuickCheck** para pruebas. Las bibliotecas clave incluyen **aeson** para JSON, **text** para cadenas, **servant** para API con seguridad de tipos, **lens** para óptica y **stm** para concurrencia. Haskell sobresale en compiladores, sistemas financieros, sistemas concurrentes y en cualquier lugar donde la corrección sea primordial. La curva de aprendizaje es pronunciada, pero la recompensa es un software que funciona correctamente desde el principio.