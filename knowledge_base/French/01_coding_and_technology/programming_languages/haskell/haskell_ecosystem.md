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

# Haskell — Guide de l'écosystème et des outils
Ce guide couvre les outils, cadres et infrastructures essentiels de l'écosystème Haskell.
---

## Chaîne d'outils
| Outil | Objectif |
|------|--------------|
| **GHC** | Compilateur Glasgow Haskell (le compilateur) |
| **GHCup** | Programme d'installation de la chaîne d'outils Haskell |
| **Cabale** | Système de construction et format de package |
| **Pile** | Outil de construction reproductible |
| **cabale-install** | Gestionnaire de paquets |
| **serveur de langue haskell (HLS)** | Serveur LSP |
| **ghcid** | Commentaires sur la compilation rapide |
| **fourmolu** | Formateur de code |
| **ormolu** | Formateur de code |
| **indice** | Linters / suggestions |
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

## Gestion des paquets
| Outil | Objectif |
|------|--------------|
| **Piratage** | Dépôt central de packages (plus de 15 000 packages) |
| **Empilage** | Ensembles de packages sélectionnés et compatibles |
| **Cabale** | Format de package et outil de construction |
| **Pile** | Constructions reproductibles (instantanés LTS) |
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

## Cadres Web
| Cadre | Tapez | Idéal pour |
|---------------|------|--------------|
| **Serviteur** | Niveau de type | API de type sécurisé |
| **Ouisod** | Pile complète | Applications Web sécurisées |
| **Scotty** | Léger | API simples (de type Sinatra) |
| **Spock** | Léger | Applications Web |
| **PHI** | Piles incluses | De type rails, Haskell |
| **Miso** | Front-end | Frontend de type Elm |
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

## Base de données
| Technologie | Tapez |
|------------|------|
| **persistant** | ORM (écosystème Yesod) |
| **hasql** | PostgreSQL (hautes performances) |
| **postgresql-simple** | PostgreSQL (simple) |
| **poutre** | SQL de type sécurisé |
| **esquelette** | ESQL de type sécurisé (sur persistant) |
| **hédis** | Client Redis |
| **mongoDB** | Pilote MongoDB |
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

## Tests
| Cadre | Objectif |
|-----------|---------|
| **Unité** | Tests unitaires (style xUnit) |
| **savoureux** | Cadre de test (composable) |
| **unité-savoureuse** | Intégration HUnit pour savoureux |
| **savoureux-quickcheck** | Tests basés sur les propriétés |
| **Vérification rapide** | Tests basés sur les propriétés |
| **hérisson** | Basé sur la propriété (moderne) |
| **hspec** | Tests de style BDD |
| **doctest** | Exemples de tests dans Haddock |
| **découverte-savoureuse** | Tests de découverte automatique |
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

## Qualité du code
| Outil | Objectif |
|------|--------------|
| **indice** | Suggestions et peluchage |
| **fourmolu / ormolu** | Formatage des codes |
| **élégant-haskell** | Formatage des codes |
| **sarcleur** | Détection de code mort |
| **stan** | Analyse statique |
| **serveur-de-langue-haskell** | Diagnostics, complétions |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Bibliothèques clés
| Bibliothèque | Objectif |
|---------|---------|
| **base** | Bibliothèque standard (Prélude) |
| **texte** | Types de texte efficaces |
| **chaîne d'octets** | Données binaires |
| **aeson** | Bibliothèque JSON |
| **conteneurs** | Cartes, ensembles, séquences |
| **conteneurs-non-commandés** | Cartes de hachage, ensembles de hachage |
| **vecteur** | Baies efficaces |
| **stm** | Mémoire transactionnelle logicielle |
| **asynchrone** | Calculs asynchrones |
| **optparse-applicatif** | Analyse des arguments CLI |
| **optparse-générique** | CLI dérivée automatiquement |
| **déformation** | Serveur HTTP |
| **client http** | Client HTTP |
| **conduit** | Données en streaming |
| **tuyaux** | Données en streaming |
| **diffusion** | Données en streaming |
| **objectif** | Bibliothèque d'optique |
| **mégaparsec** | Combinateurs d'analyseurs |
| **parsec** | Combinateurs d'analyseurs |
| **rélude** | Meilleur prélude |
| **rélude** | Prélude alternatif |
---

## IDE et éditeurs
| EDI | Points forts |
|-----|-----------|
| **Code VS + HLS** | Meilleur support Haskell LSP |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Néovim + HLS** | Basé sur un terminal avec LSP |
| **Emacs + mode haskell** | Environnement Haskell classique |
| **Vim + vim-haskell** | Intégration Vim |
---

## Déploiement
| Méthode | Remarques |
|--------|-------|
| **Binaire statique** | GHC produit des binaires statiques |
| **Docker** | Constructions en plusieurs étapes (image Haskell) |
| **Non** | Constructions reproductibles |
| **Kubernetes** | Orchestration |
| **AWS Lambda** | Sans serveur (via hal) |
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

## Résumé
L'écosystème de Haskell est unique dans la mesure où il met l'accent sur l'exactitude et la sécurité des types. La chaîne d'outils standard est la suivante : **GHC** comme compilateur, **GHCup** pour l'installation, **Cabal** ou **Stack** pour les builds, **haskell-lingual-server** pour la prise en charge de l'IDE, **hlint** pour le peluchage, **fourmolu** pour le formatage et **tasty + QuickCheck** pour les tests. Les bibliothèques de clés incluent **aeson** pour JSON, **text** pour les chaînes, **servant** pour les API de type sécurisé, **lens** pour l'optique et **stm** pour la concurrence. Haskell excelle dans les compilateurs, les systèmes financiers, les systèmes concurrents et partout où l'exactitude est primordiale. La courbe d'apprentissage est abrupte, mais la récompense est un logiciel qui fonctionne correctement par construction.