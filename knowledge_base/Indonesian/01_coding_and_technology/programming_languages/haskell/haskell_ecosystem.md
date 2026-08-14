<!--
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

-->
# Haskell — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem Haskell.
---

## Rantai Alat
| Alat | Tujuan |
|------|---------|
| **GHC** | Glasgow Haskell Compiler (kompiler) |
| **GHCup** | Penginstal rantai alat Haskell |
| **komplotan rahasia** | Bangun sistem dan format paket |
| **Tumpukan** | Alat pembangunan yang dapat direproduksi |
| **komplotan rahasia-instal** | Manajer paket |
| **server-bahasa-haskell (HLS)** | Server LSP |
| **ghcid** | Umpan balik kompilasi cepat |
| **empatmolu** | Pemformat kode |
| **ormolu** | Pemformat kode |
| **petunjuk** | Linter / saran |
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

## Manajemen Paket
| Alat | Tujuan |
|------|---------|
| **Peretasan** | Repositori paket pusat (15.000+ paket) |
| **Tumpukan** | Kumpulan paket yang dikuratori dan kompatibel |
| **komplotan rahasia** | Format paket dan alat pembuatan |
| **Tumpukan** | Build yang dapat direproduksi (snapshot LTS) |
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

## Kerangka Web
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Pelayan** | Tingkat tipe | API yang aman untuk tipe |
| **Iya** | Tumpukan penuh | Aplikasi web yang aman untuk mengetik |
| **Scotty** | Ringan | API Sederhana (seperti Sinatra) |
| **Spok** | Ringan | Aplikasi web |
| **IHP** | Sudah termasuk baterai | Seperti rel, Haskell |
| **Miso** | Bagian depan | Bagian depan seperti elm |
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

## Basis Data
| Teknologi | Ketik |
|------------|------|
| **gigih** | ORM (ekosistem Yesod) |
| **hasql** | PostgreSQL (kinerja tinggi) |
| **postgresql-sederhana** | PostgreSQL (sederhana) |
| **balok** | SQL yang aman untuk mengetik |
| **esqueleto** | ESQL yang aman untuk tipe (aktif persisten) |
| **hedis** | Klien Redis |
| **mongoDB** | Sopir MongoDB |
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

## Pengujian
| Kerangka | Tujuan |
|-----------|---------|
| **Satuan** | Pengujian unit (gaya xUnit) |
| **enak** | Kerangka pengujian (dapat disusun) |
| **perburuan lezat** | Integrasi HUnit untuk lezat |
| **cek cepat enak** | Pengujian berbasis properti |
| **Periksa Cepat** | Pengujian berbasis properti |
| **landak** | Berbasis properti (modern) |
| **spesifikasi** | Pengujian gaya BDD |
| **tes dokter** | Contoh uji di Haddock |
| **temukan lezat** | Tes penemuan otomatis |
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

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **petunjuk** | Saran dan linting |
| **empatmolu / ormolu** | Pemformatan kode |
| **haskell bergaya** | Pemformatan kode |
| **penyiangi** | Deteksi kode mati |
| **stan** | Analisis statis |
| **server-bahasa-haskell** | Diagnostik, penyelesaian |
```yaml
# .hlint.yaml
- ignore: {name: "Use newtype instead of data"}
- warn: {name: "Reduce duplication"}
```

---

## Perpustakaan Utama
| Perpustakaan | Tujuan |
|---------|---------|
| **basis** | Pustaka standar (Pendahuluan) |
| **teks** | Jenis teks yang efisien |
| **bytestring** | Data biner |
| **ason** | Perpustakaan JSON |
| **wadah** | Peta, himpunan, barisan |
| **kontainer tak berurutan** | Peta hash, kumpulan hash |
| **vektor** | Array yang efisien |
| **stm** | Memori transaksional perangkat lunak |
| **asinkron** | Perhitungan asinkron |
| **optparse-aplikatif** | Penguraian argumen CLI |
| **optparse-generik** | CLI yang diturunkan secara otomatis |
| **melengkung** | Server HTTP |
| **klien http** | Klien HTTP |
| **saluran** | Streaming data |
| **pipa** | Streaming data |
| **pengaliran** | Streaming data |
| **lensa** | Perpustakaan optik |
| **megaparsec** | Kombinator parser |
| **parsec** | Kombinator parser |
| **relude** | Pendahuluan yang Lebih Baik |
| **relude** | Pendahuluan Alternatif |
---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS + HLS** | Dukungan Haskell LSP terbaik |
| **IntelliJ + IntelliJ-Haskforce** | JetBrains Haskell |
| **Neovim + HLS** | Berbasis terminal dengan LSP |
| **Emacs + mode haskell** | Lingkungan Haskell klasik |
| **Vim + vim-haskell** | Integrasi Vim |
---

## Penerapan
| Metode | Catatan |
|--------|-------|
| **Biner statis** | GHC menghasilkan biner statis |
| **Buruh pelabuhan** | Pembangunan multi-tahap (gambar haskell) |
| **Nix** | Bangunan yang dapat direproduksi |
| **Kubernetes** | Orkestrasi |
| **AWS Lambda** | Tanpa server (melalui hal) |
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

## Ringkasan
Ekosistem Haskell unik dalam penekanannya pada kebenaran dan keamanan jenis. Toolchain standarnya adalah: **GHC** sebagai compiler, **GHCup** untuk instalasi, **Cabal** atau **Stack** untuk build, **haskell-lingual-server** untuk dukungan IDE, **hlint** untuk linting, **fourmolu** untuk pemformatan, dan **tasty + QuickCheck** untuk pengujian. Pustaka utama mencakup **aeson** untuk JSON, **teks** untuk string, **servant** untuk API yang aman untuk tipe, **lens** untuk optik, dan **stm** untuk konkurensi. Haskell unggul dalam kompiler, sistem keuangan, sistem konkuren, dan di mana pun kebenaran adalah yang terpenting. Kurva pembelajarannya curam, namun imbalannya adalah perangkat lunak yang berfungsi dengan benar dalam konstruksi.