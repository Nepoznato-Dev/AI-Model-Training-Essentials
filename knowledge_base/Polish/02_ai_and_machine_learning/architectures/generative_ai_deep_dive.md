---
# Metadata
title: "Generative AI Deep Dive"
description: "GANs, VAEs, diffusion models, LLMs, generative AI applications"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [generative, ai, deep, dive, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Głębokie nurkowanie generatywnej AI
Generatywna sztuczna inteligencja odnosi się do modeli, które tworzą nową treść – obrazy, tekst, dźwięk, wideo, kod – zamiast po prostu klasyfikować lub przewidywać istniejące dane. Podczas gdy większość uwagi poświęca się dużym modelom językowym, krajobraz generatywnej sztucznej inteligencji jest znacznie szerszy. Ten plik opisuje architektury, techniki i kompromisy stojące za nowoczesnymi systemami generatywnymi, od modeli dyfuzyjnych, przez wariacyjne autoenkodery, po modele przepływu.
---

## Co sprawia, że ​​model jest „generatywny”?
| Wpisz | Co to robi | Przykład |
|------|------------|--------|
| **Dyskryminacja** | Poznaj granicę pomiędzy klasami | „Czy ten obraz przedstawia kota czy psa?” |
| **Generatywny** | Dowiedz się o rozkładzie samych danych | „Wygeneruj nowy wizerunek kota” |
Modele generatywne rejestrują *sposób wytwarzania danych*, a nie tylko sposób ich kategoryzowania. To sprawia, że ​​są zasadniczo potężniejsi i trudniejsi do wyszkolenia.
---

## Główne architektury generatywne
### Autoenkodery wariacyjne (VAE)
VAE uczą się skompresowanej, ustrukturyzowanej reprezentacji (przestrzeni ukrytej) danych, a następnie generują nowe próbki, pobierając próbki z tej przestrzeni.
| Składnik | Rola |
|----------|------|
| **Koder** | Mapuje dane wejściowe na rozkład w przestrzeni utajonej (średnia i wariancja) |
| **Ukryta przestrzeń** | Ciągła, niskowymiarowa przestrzeń, w której podobne punkty danych znajdują się blisko siebie |
| **Dekoder** | Mapuje punkty w przestrzeni ukrytej z powrotem do przestrzeni danych |
| **Rozbieżność KL** | Termin regularyzacyjny, który utrzymuje utajony rozkład blisko standardowej normalnej |
**Jak działa generowanie**: próbkuj losowy wektor z przestrzeni utajonej → przepuść go przez dekoder → uzyskaj nowy punkt danych.
| siła | słabość |
|---------|----------|
| Gładka, ciągła przestrzeń ukryta | Wyniki są zwykle rozmyte |
| Podstawowe ramy matematyczne | Ograniczone możliwościami architektury |
| Potrafi interpolować między przykładami | Mniej ostre niż wyjścia dyfuzyjne lub GAN |
VAE są często używane jako komponenty w innych modelach (np. Stable Diffusion wykorzystuje VAE jako część swojego rurociągu).
### Generacyjne sieci przeciwstawne (GAN)
W sieciach GAN rywalizują ze sobą dwie sieci: **generator**, który tworzy fałszywe dane i **dyskryminator**, który próbuje odróżnić prawdziwe od fałszywych.
| Składnik | Cel |
|----------|------|
| **Generator** | Wygeneruj dane, które oszukają dyskryminator |
| **Dyskryminator** | Prawidłowo klasyfikuj dane rzeczywiste i wygenerowane |
Trenują jednocześnie, wzajemnie popychając się do doskonalenia. Teoretycznie generator ostatecznie generuje dane nie do odróżnienia od danych rzeczywistych.
| Wariant GAN | Kluczowa innowacja |
|------------|-------------|
| **DCGAN** | Architektury splotowe; stabilny trening |
| **StyleGAN / StylGAN2 / StylGAN3** | Generowanie oparte na stylu; fotorealistyczne twarze; sterowalne atrybuty |
| **CyklGAN** | Niesparowane tłumaczenie obrazu na obraz (koń → zebra) |
| **Pix2Pix** | Sparowane tłumaczenie obrazu na obraz (szkic → zdjęcie) |
| **ProGAN** | Progresywne uprawy dla obrazów o wysokiej rozdzielczości |
| **Wielki GAN** | Generowanie warunkowe klas na dużą skalę |
**Dlaczego GAN spadły**: Trening jest notorycznie niestabilny (załamanie trybu, zanikające gradienty). Modele dyfuzyjne zapewniają teraz lepszą jakość w przypadku większości zadań związanych z generowaniem obrazu. Sieci GAN są nadal używane w zastosowaniach czasu rzeczywistego (szybko wnioskowują) i do określonych zadań, takich jak superrozdzielczość.
### Modele dyfuzyjne
Modele dyfuzyjne stanowią aktualny stan wiedzy w zakresie generowania obrazów i wideo. Działają poprzez stopniowe dodawanie szumu do danych, aż staną się czystym szumem losowym, a następnie uczą się odwracać ten proces.
| Faza | Co się dzieje |
|-------|------------|
| **Proces dalszego rozwoju (szkolenia)** | Powoli dodawaj szum Gaussa przez setki/tysiące kroków, aż dane zostaną zniszczone |
| **Proces odwrotny (generacja)** | Naucz się odszumiać krok po kroku, zaczynając od czystego szumu, aż do uzyskania czystego obrazu |
| Modelka | Deweloper | Godna uwagi funkcja |
|-------|------|--------------------------------|
| **DDPM** (Model probabilistyczny dyfuzji odszumiającej) | Ho i in., 2020 | Pokazane modele dyfuzji mogą generować obrazy o wysokiej jakości |
| **Stabilna dyfuzja** | Stabilność AI | Dyfuzja utajona (działa w skompresowanej przestrzeni); open source |
| **DALL-E 3** | OpenAI | Zintegrowany z ChatGPT w celu zrozumienia tekstu |
| **W połowie podróży** | W połowie podróży | Jakość artystyczna; zamknięte źródło |
| **Obraz** | Google DeepMind | Wysoka wierność zamiany tekstu na obraz |
| **Sora** | OpenAI | Generowanie wideo za pomocą transformatorów dyfuzyjnych |
| **STRUMIEŃ** | Laboratoria Czarnego Lasu | Otwarty następca Stable Diffusion |
### Dlaczego modele dyfuzyjne zwyciężyły
| Zaleta | Wyjaśnienie |
|---------------|------------|
| **Stabilność treningu** | Znacznie bardziej stabilne niż sieci GAN; brak szkolenia kontradyktoryjnego |
| **Jakość wyjściowa** | Najnowocześniejsza jakość i różnorodność obrazu |
| **Sterowanie** | Można kierować tekstem (poprzez CLIP), malowaniem masek lub innymi warunkami |
| **Różnorodność** | Mniej załamań trybu niż sieci GAN; generuje różnorodne wyniki |
| Wada | Wyjaśnienie |
|------------|------------|
| **Powolne wnioskowanie** | Wymaga wielu etapów odszumiania (typowo 20–50) |
| **Intensywne obliczenia** | Każdy krok to pełne przejście do przodu przez duży model |
### Ukryta dyfuzja
Uruchamianie dyfuzji w przestrzeni pikseli jest kosztowne. **Dyfuzja utajona** (używana przez Stable Diffusion) zamiast tego uruchamia proces dyfuzji w skompresowanej przestrzeni utajonej.
| Krok | Co się dzieje |
|------|------------|
| 1. Kompresuj | Wstępnie wyszkolony VAE koduje obraz w mniejszą ukrytą reprezentację |
| 2. Rozproszone | Model dyfuzyjny dodaje/usuwa szum w przestrzeni ukrytej |
| 3. Dekoduj | Dekoder VAE przekształca ukryty obraz z powrotem w pełny obraz |
Dzięki temu wytwarzanie jest znacznie szybsze i tańsze, przy jednoczesnym zachowaniu jakości.
---

## Generowanie warunkowane tekstem
Większość nowoczesnych systemów generatywnych opiera się na podpowiedziach tekstowych — opisujesz, czego chcesz, a model to generuje.
### CLIP (kontrastowy trening językowy i obrazowy)
CLIP uczy się wspólnej przestrzeni do osadzania tekstu i obrazów. Został przeszkolony na miliardach par obraz-tekst z Internetu.
| Zdolność | Opis |
|------------|------------|
| **Klasyfikacja zero-shot** | Klasyfikuj obrazy za pomocą opisów tekstowych bez żadnego szkolenia |
| **Wyszukiwanie obrazu i tekstu** | Znajdź najbardziej odpowiedni obraz dla zapytania tekstowego |
| **Przewodnictwo dyfuzyjne** | Skieruj generowanie obrazu w stronę podpowiedzi tekstowej |
### Wytyczne bez klasyfikatorów (CFG)
CFG kontroluje, jak bardzo wygenerowany obraz odpowiada podpowiedzi tekstowej.
| Skala CFG | Efekt |
|----------|--------|
| **1,0** | Brak wskazówek; zróżnicowane, ale mogą nie odpowiadać podpowiedzi |
| **5,0–7,5** | Zrównoważony; dobra jakość i szybka przyczepność |
| **10,0+** | Silna przyczepność; może generować obrazy przesycone lub zawierające dużo artefaktów |
---

## Inne podejścia generatywne
### Normalizowanie przepływów
| Funkcja | Opis |
|--------|------------|
| **Jak to działa** | Naucz się odwracalnego mapowania danych i prostej dystrybucji |
| **Siła** | Dokładne obliczenie prawdopodobieństwa; szybkie pobieranie próbek |
| **Słabość** | Wymaga starannie zaprojektowanych architektur; mniej elastyczny |
| **Przypadki użycia** | Wykrywanie anomalii, szacowanie gęstości |
### Modele autoregresyjne
| Funkcja | Opis |
|--------|------------|
| **Jak to działa** | Generuj dane po jednym elemencie na raz, uwzględniając wszystkie poprzednie elementy |
| **Siła** | Naturalne dla danych sekwencyjnych (tekst, kod, muzyka) |
| **Słabość** | Powolne generowanie (musi być sekwencyjne); ograniczone przez dystrybucję danych treningowych |
| **Przykłady** | GPT (tekst), WaveNet (audio), ImageGPT (obrazy) |
### Modele oparte na energii
| Funkcja | Opis |
|--------|------------|
| **Jak to działa** | Naucz się funkcji energetycznej; niska energia = realistyczne dane |
| **Siła** | Elastyczny; nie wymaga normalizacji |
| **Słabość** | Trening jest trudny; pobieranie próbek wymaga MCMC |
| **Przypadki użycia** | Badania teoretyczne; niektóre zastosowania robotyki |
---

## Metryki oceny
Jak mierzyć jakość generowanych danych? To trudniejsze niż myślisz.
| Metryczne | Dla | Co to mierzy | Ograniczenie |
|--------|-----|----------------|------------|
| **FID** (Odległość początkowa Frécheta) | Obrazy | Odległość pomiędzy rozkładami obrazu rzeczywistego i generowanego | Niższe jest lepsze; nie oddaje dobrze różnorodności |
| **IS** (punktacja początkowa) | Obrazy | Jakość i różnorodność generowanych obrazów | Kontrowersyjny; można grać |
| **Wynik CLIP** | Tekst na obraz | Jak dobrze obraz pasuje do podpowiedzi tekstowej | Zależy od uprzedzeń CLIP |
| **Zakłopotanie** | Tekst | Jak dobrze model przewiduje następny token | Niższe jest lepsze; nie mierzy spójności |
| **BLUE / RÓŻOWY** | Generacja tekstu | Pokrywają się z tekstem referencyjnym | Słabe zastępstwo dla ludzkiego osądu |
| **FAD** (odległość audio Frécheta) | Dźwięk | Odległość pomiędzy dystrybucjami rzeczywistymi i generowanymi audio | Analogicznie do FID dla audio |
---

## Kontrolowana generacja
Nowoczesne systemy pozwalają kontrolować to, co jest generowane, a nie tylko podpowiedzi tekstowe.
| Metoda | Typ kontroli | Przykład |
|------------|------------|--------|
| **Malarstwo** | Wypełnij zamaskowane obszary | Usuń obiekt ze zdjęcia |
| **Przemalowanie** | Wykraczaj poza granice obrazu | Poszerz krajobraz |
| **Sieć kontrolna** | Wskazówki konstrukcyjne (krawędzie, głębokość, ułożenie) | Wygeneruj obraz pasujący do określonej pozy |
| **Adapter IP** | Styl lub treść obrazu referencyjnego | „Spraw, żeby to wyglądało jak ten obraz” |
| **LoRA** | Dopracowany styl lub koncepcja | Dodaj konkretną postać lub styl graficzny |
| **Img2Img** | Przekształć istniejący obraz | Zamień szkic w fotorealistyczny obraz |
---

## Generowanie wideo
Generowanie wideo to kolejna granica po obrazach. Dodaje wymiaru czasu i ruchu.
| Modelka | Podejście | Godna uwagi funkcja |
|-------|----------|--------------------------------|
| **Sora** (OpenAI) | Transformator dyfuzyjny | Do 1080p; rozumie fizykę w miarę dobrze |
| **Pas startowy Gen-3** | Oparte na dyfuzji | Komercyjne narzędzie do generowania wideo |
| **Pika** | Oparte na dyfuzji | Krótkie klipy wideo z tekstu |
| **Kling** | Autoregresja + dyfuzja | Generowanie wideo w długiej formie |
| **Veo 2** (Google) | Transformator dyfuzyjny | Wysokiej jakości, fizycznie spójne wideo |
### Wyzwania w generowaniu wideo
| Wyzwanie | Dlaczego to jest trudne |
|----------|-------------|
| **Tymczasowa spójność** | Obiekty powinny wyglądać tak samo w różnych klatkach |
| **Fizyka** | Grawitacja, zderzenia, dynamika płynów muszą być w przybliżeniu prawidłowe |
| **Długość** | Wygenerowanie minut spójnego wideo jest znacznie trudniejsze niż pojedynczego obrazu |
| **Oblicz** | Wideo to zasadniczo wiele obrazów; skala kosztów z liczbą ramek |
| **Ocena** | Żaden standardowy wskaźnik nie odzwierciedla dobrze jakości wideo |
---

## Generowanie dźwięku
| Modelka | Wpisz | Aplikacja |
|-------|------|------------|
| **WaveNet** (DeepMind) | Autoregresja | Wysokiej jakości synteza mowy |
| **VALL-E** (Microsoft) | Kodek neuronowy | Zamiana tekstu na mowę z 3-sekundowej próbki głosu |
| **MusicGen** (Meta) | Oparte na transformatorze | Generowanie tekstu na muzykę |
| **AudioLDM** | Ukryta dyfuzja | Generowanie efektów dźwiękowych |
| **JedenaścieLab** | Komercyjne | Klonowanie i synteza głosu |
---

## Ekonomia generacji
| Czynnik | Wpływ |
|------------|------------|
| **Koszt szkolenia** | Modele dyfuzji: 100 tys. – 10 mln dolarów + w zależności od skali |
| **Koszt wnioskowania** | Generowanie obrazu: ~ 0,01–0,05 USD za obraz w skali |
| **Sprzęt** | Szkolenie: wiele procesorów graficznych A100/H100; Wniosek: możliwy pojedynczy procesor graficzny |
| **Otwarte czy zamknięte** | Modele otwarte (Stable Diffusion, FLUX) mogą działać lokalnie; modele zamknięte (DALL-E, Midjourney) obsługują wyłącznie API |
---

## Streszczenie
Generatywna sztuczna inteligencja ewoluowała od GAN, poprzez VAE, po modele dyfuzyjne i nie tylko. Kluczowy pogląd we wszystkich tych architekturach jest taki sam: poznaj rozkład danych, a następnie próbkuj z nich, aby utworzyć nową treść. Modele dyfuzyjne dominują obecnie w generowaniu obrazów i wideo ze względu na ich stabilność uczenia się i jakość wyjściową. VAE służą jako kluczowe elementy składowe. Modele autoregresyjne dominują w tekście i kodzie. Dziedzina zmierza w kierunku generacji multimodalnej — systemów, które mogą wytwarzać tekst, obrazy, dźwięk i wideo z dowolnej kombinacji wejść — oraz w kierunku szybszego, tańszego i łatwiejszego do kontrolowania generowania.