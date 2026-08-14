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
# Haskell - Mfumo wa Ikolojia na Mwongozo wa zana
Mwongozo huu unashughulikia zana muhimu, mifumo, na miundombinu katika mfumo ikolojia wa Haskell.
---

##Mnyororo wa zana
| Zana | Kusudi |
|------|----------|
| **GHC** | Mkusanyaji wa Glasgow Haskell (mkusanyaji) |
| **GHCup** | Kisakinishi cha zana za Haskell |
| **Kabali** | Jenga mfumo na umbizo la kifurushi |
| **Randi** | Zana ya kujenga inayoweza kuzaa |
| **cabal-sakinisha** | Kidhibiti kifurushi |
| **haskell-language-server (HLS)** | Seva ya LSP |
| **ghcid** | Haraka kukusanya maoni |
| **fourmolu** | Mpangilio wa msimbo |
| **ormolu** | Mpangilio wa msimbo |
| **kipande** | Linter / mapendekezo |
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

## Usimamizi wa Kifurushi
| Zana | Kusudi |
|------|----------|
| **Udukuzi** | Hifadhi ya kifurushi cha kati (vifurushi 15,000+) |
| **Stackage** | Seti za vifurushi vilivyoratibiwa, vinavyooana |
| **Kabali** | Umbizo la kifurushi na zana ya kuunda |
| **Randi** | Miundo inayoweza kuzaliana (Picha za LTS) |
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

## Mifumo ya Wavuti
| Mfumo | Andika | Bora Kwa |
|-----------|------|-----------|
| **Mtumishi** | Aina ya kiwango | API za aina-salama |
| **Yesod** | Rafu kamili | Programu za wavuti za aina salama |
| **Skoti** | Nyepesi | API Rahisi (Sinatra-kama) |
| **Spock** | Nyepesi | Programu za wavuti |
| **IHP** | Betri-imejumuishwa | Reli-kama, Haskell |
| **Miso** | Mbele | Elm-kama frontend |
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

## Hifadhidata
| Teknolojia | Andika |
|------------|------|
| **inayoendelea** | ORM (mfumo wa ikolojia wa Yesod) |
| **hasql** | PostgreSQL (utendaji wa juu) |
| **postgresql-rahisi** | PostgreSQL (rahisi) |
| **boriti** | SQL ya aina-salama |
| **esqueleto** | ESQL ya aina-salama (kwenye kuendelea) |
| **hedi** | Redis mteja |
| **mongoDB** | Dereva wa MongoDB |
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

##Upimaji
| Mfumo | Kusudi |
|-----------|---------|
| **Hunit** | Upimaji wa kitengo (mtindo wa xUnit) |
| **kitamu** | Mfumo wa mtihani (unaoweza kutumika) |
| ** kitamu-hunit** | Ushirikiano wa HUnit kwa kitamu |
| **kitamu-cheki haraka** | Upimaji kulingana na mali |
| **Angalia Haraka** | Upimaji kulingana na mali |
| **Nguruwe** | Kulingana na mali (kisasa) |
| **hspec** | Upimaji wa mtindo wa BDD |
| **daktari** | Mifano ya majaribio katika Haddock |
| **kitamu-gundua** | Gundua kiotomatiki majaribio |
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

## Ubora wa Kanuni
| Zana | Kusudi |
|------|----------|
| **kipande** | Mapendekezo na lining |
| **fourmolu / ormolu** | Uumbizaji wa msimbo |
| **stylish-haskell** | Uumbizaji wa msimbo |
| **kupalilia** | Utambuzi wa msimbo uliokufa |
| **stan** | Uchambuzi tuli |
| **haskell-language-server** | Uchunguzi, ukamilishaji |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Maktaba Muhimu
| Maktaba | Kusudi |
|---------|---------|
| **msingi** | Maktaba ya kawaida (Dibaji) |
| **maandishi** | Aina za maandishi bora |
| **bytestring** | Data ya binary |
| **aeson** | Maktaba ya JSON |
| **vyombo** | Ramani, seti, mfuatano |
| **vyombo-vilivyoagizwa** | Ramani za hashi, seti za heshi |
| **vekta** | Safu zenye ufanisi |
| **stm** | Kumbukumbu ya shughuli ya programu |
| **async** | Mahesabu ya Async |
| **optparse-applicative** | Uchanganuzi wa hoja ya CLI |
| **optparse-generic** | CLI inayotokana otomatiki |
| **kukunja** | Seva ya HTTP |
| **http-mteja** | mteja wa HTTP |
| **mfereji** | Data ya kutiririsha |
| **mabomba** | Data ya kutiririsha |
| **inatiririsha** | Data ya kutiririsha |
| **lenzi** | Maktaba ya macho |
| **megaparsec** | Vichanganuzi vya kuchanganua |
| **parsec** | Vichanganuzi vya kuchanganua |
| **rudi** | Utangulizi Bora |
| **rudi** | Dibaji Mbadala |
---

## Vitambulisho na Vihariri
| ID | Nguvu |
|-----|------------|
| **Msimbo wa VS + HLS** | Msaada bora wa Haskell LSP |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Msingi wa kituo na LSP |
| **Emacs + hali-haskell** | Mazingira ya Haskell ya kawaida |
| **Vim + vim-haskell** | Ujumuishaji wa Vim |
---

## Usambazaji
| Mbinu | Vidokezo |
|--------|-------|
| **Binary tuli** | GHC inazalisha jozi tuli |
| **Docker** | Muundo wa hatua nyingi (picha ya haskell) |
| **Nix** | Miundo inayoweza kuzaliana |
| **Kubernetes** | Okestra |
| **AWS Lambda** | Isiyo na seva (kupitia hal) |
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

## Muhtasari
Mfumo ikolojia wa Haskell ni wa kipekee katika msisitizo wake juu ya usahihi na usalama wa aina. Msururu wa zana wa kawaida ni: **GHC** kama mkusanyaji, **GHCup** ya kusakinisha, **Cabal** au **Stack** ya miundo, **haskell-language-server** kwa usaidizi wa IDE, **hlint** ya kuweka, **fourmolu** ya uumbizaji, na **kitamu + QuickCheck** ya majaribio. Maktaba muhimu ni pamoja na **aeson** ya JSON, **maandishi** ya mifuatano, **servant** ya API za aina-salama, **lenzi** ya macho, na **stm** ya concurrency. Haskell anafaulu katika wakusanyaji, mifumo ya fedha, mifumo inayofanana, na mahali popote usahihi ni muhimu. Njia ya kujifunza ni mwinuko, lakini faida ni programu ambayo inafanya kazi kwa usahihi na ujenzi.