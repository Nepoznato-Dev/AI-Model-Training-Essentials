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

# Haskell — Ekosistem ve Takım Kılavuzu
Bu kılavuz Haskell ekosistemindeki temel araçları, çerçeveleri ve altyapıyı kapsar.
---

## Alet Zinciri
| Araç | Amaç |
|------|------------|
| **GHC** | Glasgow Haskell Derleyicisi (derleyici) |
| **GHCup** | Haskell takım zinciri yükleyicisi |
| **Kabil** | Sistemi ve paket formatını oluşturun |
| **Yığın** | Tekrarlanabilir yapı aracı |
| **cabal kurulumu** | Paket yöneticisi |
| **haskell-dil-sunucusu (HLS)** | LSP sunucusu |
| **ghcid** | Hızlı derleme geribildirimi |
| **dörtmolu** | Kod biçimlendirici |
| **ormolu** | Kod biçimlendirici |
| **hint** | Linter / öneriler |
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

## Paket Yönetimi
| Araç | Amaç |
|------|------------|
| **Hackaj** | Merkezi paket deposu (15.000+ paket) |
| **İstifleme** | Seçilmiş, uyumlu paket setleri |
| **Kabil** | Paket formatı ve derleme aracı |
| **Yığın** | Tekrarlanabilir yapılar (LTS anlık görüntüleri) |
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

## Web Çerçeveleri
| Çerçeve | Tür | En İyisi |
|-----------|----------|----------|
| **Hizmetçi** | Tür düzeyinde | Tür açısından güvenli API'ler |
| **Evet** | Tam yığın | Tür uyumlu web uygulamaları |
| **Scotty** | Hafif | Basit API'ler (Sinatra benzeri) |
| **Spock** | Hafif | Web uygulamaları |
| **IHP** | Piller dahil | Raylara benzer, Haskell |
| **Miso** | Ön Uç | Karaağaç benzeri ön uç |
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

## Veritabanı
| Teknoloji | Tür |
|---------------|------|
| **kalıcı** | ORM (Yesod ekosistemi) |
| **hasql** | PostgreSQL (yüksek performanslı) |
| **postgresql-basit** | PostgreSQL (basit) |
| **kiriş** | Tür açısından güvenli SQL |
| **esqueleto** | Tür açısından güvenli ESQL (kalıcı olarak) |
| **hedi** | Redis istemcisi |
| **mongoDB** | MongoDB sürücüsü |
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

## Test etme
| Çerçeve | Amaç |
|-----------|------------|
| **HBirim** | Birim testi (xUnit tarzı) |
| **lezzetli** | Test çerçevesi (birleştirilebilir) |
| **lezzetli av** | Lezzet için HUnit entegrasyonu |
| **lezzetli-hızlı kontrol** | Mülkiyet bazlı testler |
| **Hızlı Kontrol** | Mülkiyet bazlı testler |
| **kirpi** | Mülkiyet bazlı (modern) |
| **hspec** | BDD tarzı testler |
| **doktor testi** | Haddock'ta test örnekleri |
| **lezzetli-keşfet** | Testleri otomatik keşfetme |
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

## Kod Kalitesi
| Araç | Amaç |
|------|------------|
| **hint** | Öneriler ve linting |
| **dörtmolu / ormolu** | Kod biçimlendirme |
| **şık-haskell** | Kod biçimlendirme |
| **ot sökücü** | Ölü kod tespiti |
| **stan** | Statik analiz |
| **haskell-dil-sunucusu** | Teşhis, tamamlamalar |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Anahtar Kitaplıklar
| Kütüphane | Amaç |
|-----------|-----------|
| **taban** | Standart kütüphane (Prelude) |
| **metin** | Verimli metin türleri |
| **bytestring** | İkili veriler |
| **son** | JSON kitaplığı |
| **konteynerler** | Haritalar, setler, sekanslar |
| **sıralanmamış konteynerler** | Hash haritaları, hash kümeleri |
| **vektör** | Verimli diziler |
| **stm** | Yazılım işlem belleği |
| **eşzamansız** | Eşzamansız hesaplamalar |
| **optparse-uygulanabilir** | CLI bağımsız değişkeni ayrıştırma |
| **optparse-jenerik** | Otomatik türetilmiş CLI |
| **çözgü** | HTTP sunucusu |
| **http-istemcisi** | HTTP istemcisi |
| **kanal** | Veri akışı |
| **borular** | Veri akışı |
| **akış** | Veri akışı |
| **lens** | Optik kütüphanesi |
| **megaparsek** | Ayrıştırıcı birleştiriciler |
| **parsek** | Ayrıştırıcı birleştiriciler |
| **relüde** | Daha İyi Başlangıç ​​|
| **relüde** | Alternatif Prelüd |
---

## IDE'ler ve Düzenleyiciler
| IDE | Güçlü Yönler |
|-----|-----------|
| **VS Kodu + HLS** | En iyi Haskell LSP desteği |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | LSP ile terminal tabanlı |
| **Emacs + haskell modu** | Klasik Haskell ortamı |
| **Vim + vim-haskell** | Vim entegrasyonu |
---

## Dağıtım
| Yöntem | Notlar |
|----------|----------|
| **Statik ikili** | GHC statik ikili dosyalar üretir |
| **Docker** | Çok aşamalı yapılar (haskell görüntüsü) |
| **Nix** | Tekrarlanabilir yapılar |
| **Kubernetes** | Orkestrasyon |
| **AWS Lambda** | Sunucusuz (hal aracılığıyla) |
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

## Özet
Haskell'in ekosistemi, doğruluk ve tür güvenliğine verdiği önem açısından benzersizdir. Standart araç zinciri şöyledir: derleyici olarak **GHC**, kurulum için **GHCup**, derlemeler için **Cabal** veya **Stack**, IDE desteği için **haskell-language-server**, linting için **hlint**, biçimlendirme için **fourmolu** ve test için **tasty + QuickCheck**. Anahtar kitaplıklar arasında JSON için **aeson**, dizeler için **text**, tür uyumlu API'ler için **servant**, optik için **lens** ve eşzamanlılık için **stm** yer alır. Haskell derleyicilerde, finansal sistemlerde, eşzamanlı sistemlerde ve doğruluğun en önemli olduğu her yerde uzmandır. Öğrenme eğrisi diktir, ancak getirisi, yapısı itibarıyla doğru şekilde çalışan bir yazılımdır.