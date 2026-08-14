---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [local, ai, architecture, ai-and-machine-learning]
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
# Lokalna architektura AI
Praktyczny przewodnik po uruchamianiu dużych modeli językowych całkowicie na urządzeniu — kwestie sprzętowe, silniki wnioskowania, optymalizacja pamięci i projektowanie systemów pod kątem wdrażania brzegowego.
---

## Po co uruchamiać sztuczną inteligencję lokalnie?
- **Prywatność**: Żadne dane nie opuszczają urządzenia.
- **Koszt**: Brak opłat API za token.
- **Opóźnienie**: Przewidywalne wnioskowanie bez konieczności korzystania z sieci.
- **Dostępność offline**: Działa bez Internetu.
- **Kontrola**: Pełna kontrola nad wersją modelu, dostosowywaniem i dostrajaniem.
---

## Wymagania sprzętowe
### Pamięć GPU (VRAM)
Najbardziej krytyczny zasób. Rozmiar modelu w pamięci ≈ **parametry × bajty na parametr**.
| Precyzja | Bajty na parametr | Model 3.8B | Model 7B | Model 13B | model 70B |
|-----------|-------|------------|---------------|----------------|----------------|
| FP32 | 4 | ~15 GB | ~28 GB | ~52 GB | ~280 GB |
| FP16 | 2 | ~7,6 GB | ~14 GB | ~26 GB | ~140 GB |
| INT8 (8-bitowy) | 1 | ~3,8 GB | ~7 GB | ~13 GB | ~70 GB |
| INT4 (4-bitowy) | 0,5 | ~1,9 GB | ~3,5 GB | ~6,5 GB | ~35 GB |
**Praktyczne wskazówki:**
- 8 GB VRAM → modele do 7B przy 4-bitach.
- 12 GB VRAM → do 13B modeli w trybie 4-bitowym.
- 24 GB VRAM → modele do 70B przy 4-bitach (lub 13B przy 8-bitach).
- Apple Silicon (ujednolicona pamięć) może obsługiwać modele 70B w systemach 64 GB+.
### RAM (pamięć systemowa)
- Do wnioskowania o procesorze potrzebna jest wystarczająca ilość systemowej pamięci RAM, aby załadować model (podobnie jak numery VRAM).
— W przypadku procesora graficznego pamięć systemowa RAM ma znaczenie przy ładowaniu modelu do pamięci przed przeniesieniem do VRAM.
### Przechowywanie
- Skwantowane wagi modeli zajmują kilka GB (np. 4-bitowy 7B ≈ 4 GB na dysku). Zapewnij co najmniej 20–50 GB wolnego miejsca dla wielu modeli.
### Procesor
- Do szybkiego przetwarzania (wstępnego napełniania) i odciążania procesora pomaga nowoczesny wielordzeniowy procesor.
- Chipy Apple z serii M charakteryzują się doskonałą wydajnością w przypadku LLM dzięki ujednoliconej pamięci i silnikowi neuronowemu.
---

## Kwantyzacja
Kwantyzacja zmniejsza precyzję numeryczną odważników, radykalnie ograniczając pamięć i zwiększając prędkość przy niewielkim koszcie dokładności.
### Popularne formaty
| Formatuj | Bity | Opis | Typowe zastosowanie |
|------------|------|------------|------------|
| **GGUF** | 4–8 | Format llama.cpp, zoptymalizowany pod kątem hybrydy CPU/GPU | Najlepsze do wnioskowania lokalnego |
| **GPTQ** | 4–8 | Tylko GPU, wydajny na CUDA | Najlepsze dla procesorów graficznych NVIDIA |
| **AWQ** | 4 | Obsługuje aktywację, tylko GPU | Dobre do wnioskowania wsadowego na procesorach graficznych |
| **ONNX** | zmienna | Standaryzowany, wieloplatformowy | Produkcja serwująca |
### Wybór poziomu kwantyzacji
- **Q8_0** (8-bit): minimalna utrata jakości, największy rozmiar.
- **Q6_K** (6-bit): dobra jakość, przyzwoita kompresja.
- **Q5_K_M** (5-bitowy): wspólny słodki punkt.
- **Q4_K_M** (4-bitowy): najmniejsza, akceptowalna jakość dla większości zadań.
- **IQ4_XS** / **IQ3_XS**: Ulepszona kwantyzacja z większą złożonością przy 4/3 bitach.
**Ogólna zasada:** Użyj Q4_K_M, aby uzyskać dobrą równowagę jakości i rozmiaru. Jeśli masz dodatkową pamięć VRAM, użyj Q5 lub Q6.
---

## Silniki wnioskowania (lokalne)
### lama.cpp
- Napisane w C++.
- Obsługuje format GGUF.
- Zoptymalizowany pod kątem procesora i karty graficznej (poprzez CUDA, Metal, OpenCL).
- Bardzo szybki, zwłaszcza na procesorze.
- Wiersz poleceń, tryb serwera i powiązania Python.
**Przykładowe polecenie:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Opakowuje plik llama.cpp za pomocą prostego interfejsu CLI i interfejsu API REST.
- Automatyczne pobieranie modeli i zarządzanie nimi.
- Świetne do prototypowania i aplikacji komputerowych.
— Obsługuje niestandardowe pliki modeli dla monitów systemowych.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Graficzna aplikacja komputerowa dla systemów Windows, macOS i Linux.
- Interfejs pobierania i czatu jednym kliknięciem.
- Wbudowany serwer lokalny z API kompatybilnym z OpenAI.
- Dobre dla użytkowników nietechnicznych i szybkiego testowania.
### Transformatory z przytulną twarzą + bitsandbytes
- Standardowa biblioteka Pythona dla modeli HF.
- Użyj`bitsandbytes`do 4-bitowej kwantyzacji (`load_in_4bit=True`).
- Bardziej elastyczny do dostrajania, ale wolniejszy niż llama.cpp do wnioskowania.
### ExLlamaV2
- Bardzo szybkie wnioskowanie GPU dla GPTQ i AWQ.
- Najlepsza wydajność na procesorach graficznych NVIDIA.
- Obsługuje generowanie wsadowe.
### mlx (Jabłko)
- Framework Apple dla chipów z serii M.
- Wysoce zoptymalizowany dla Apple Silicon.
- API Pythona.
---

## Zarządzanie pamięcią
### Okno kontekstowe i pamięć podręczna KV
Pamięć podręczna KV przechowuje pary klucz-wartość dla każdej warstwy i każdego tokena w kontekście. Rośnie liniowo wraz z długością kontekstu.
Koszt pamięci ≈ 2 × warstwy × (głowice KV × przyciemnienie głowicy) × tokeny × bajty na wartość
W przypadku modelu 32-warstwowego z 8 głowicami KV i 128 przyciemnieniami głowicy każdy token kosztuje ~32 × 8 × 128 × 2 bajty = 65 KB na token. W przypadku tokenów 128 tys. To ~ 8 GB tylko na pamięć podręczną.
### Strategie odciążania
- **Odciążanie warstw**: Umieść niektóre warstwy na GPU, inne na CPU. Szybszy niż czysty procesor, mniejsze wymagania dotyczące pamięci VRAM.
- **Przesyłanie tokenów**: Przetwarzaj tokeny stopniowo, a nie wszystkie na raz.
### Natychmiastowe buforowanie
Użyj ponownie pamięci podręcznej KV w podobnych monitach, aby uniknąć ponownego obliczania fazy wstępnego napełniania. Niektóre frameworki to obsługują (np. vLLM, llama.cpp z`--prompt-cache`).
### Pliki mapowane w pamięci
Załaduj wagi modeli bezpośrednio z dysku, bez ładowania ich całkowicie do pamięci RAM (przydatne w przypadku dużych modeli w systemach o ograniczonej pamięci). llama.cpp domyślnie używa mapowania pamięci.
---

## Architektury wdrożeń
### Tryb jednego urządzenia
Jeden model działa na jednym komputerze (laptopie, smartfonie, urządzeniu brzegowym). Używany w przypadku asystentów osobistych, aplikacji do robienia notatek i uzupełniania kodu.
### Hybrydowa chmura krawędziowa
Model lokalny obsługuje typowe zapytania; w przypadku złożonych pytań powrót do modelu chmury. Daje to to, co najlepsze z obu światów — w większości przypadków szybkość/prywatność i możliwości w przypadkach brzegowych.
### Distributed Inference (Multi-GPU)
W przypadku większych modeli podziel warstwy na wiele procesorów graficznych (równoległość tensorów) lub podziel kontekst na urządzenia (równoległość potoku). Użyj pliku llama.cpp z`-ngl`lub ExLlamaV2 z`--num-gpu-layers`.
### Wdrożenie mobilne
- **Android**: Użyj pliku llama.cpp poprzez powiązania JNI lub zestaw ML.
- **iOS**: Użyj pliku llama.cpp poprzez powiązania Swift lub mlx.
- **Web**: Użyj WebLLM (działa na WebGPU w środowisku wykonawczym ONNX) lub transformators.js.
---

## Optymalizacja wydajności
### Błysk Uwaga
Przyspiesza obliczenia uwagi i zmniejsza zużycie pamięci. Dostępne w bibliotekach llama.cpp, ExLlamaV2 i nowoczesnych transformatorach.
### Wnioskowanie wsadowe
Przetwarzaj wiele monitów w jednym przebiegu do przodu. Znacząco zwiększa przepustowość. Użyj`llama-batch`lub vLLM.
### Wcześniejsze zatrzymanie / budżetowanie tokenów
Ustaw maksymalny budżet tokenu, aby zapobiec nieograniczonemu generowaniu.
### Dekodowanie spekulatywne
Użyj małego, szybkiego modelu (wersja robocza), aby przewidzieć tokeny, a następnie sprawdź równolegle z dużym modelem. Może zapewnić 2–3-krotne przyspieszenie.
---

## Praktyczny przewodnik konfiguracji
### 1. Zainstaluj Ollamę
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Wyciągnij model
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Uruchom z API
```bash
ollama serve
```

Następnie wyślij żądania do`http://localhost:11434/api/generate`.
### 4. Integracja z Pythonem
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternatywa) Użyj bezpośrednio pliku llama.cpp
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Monitorowanie i obserwowalność
- Śledź wykorzystanie procesora graficznego (`nvidia-smi` w systemie Linux, Monitor aktywności w systemie macOS).
- Śledź wykorzystanie pamięci (RAM i VRAM).
- Śledź tokeny na sekundę (przepustowość).
- Śledź czas do pierwszego tokena (opóźnienie).
- Użyj wbudowanego logowania z llama.cpp lub Ollama.
---

## Ograniczenia i kompromisy
- **Luka w jakości**: Małe modele lokalne (3.8B–7B) na ogół radzą sobie gorzej z modelami dużych chmur (GPT-4, Claude 3.5) przy złożonym rozumowaniu.
- **Granica wiedzy**: wiedza o modelu jest zamrażana w czasie szkolenia; użyj RAG, aby wprowadzić aktualne informacje.
- **Wielojęzyczny**: Mniejsze modele mogą obsługiwać mniej języków.
- **Wykorzystanie narzędzia**: Przepływy pracy agenta (wywoływanie funkcji) mogą być mniej niezawodne w małych modelach.
W przypadku wielu codziennych zadań (podsumowanie, pytania i odpowiedzi, uzupełnianie kodu, klasyfikacja) modele lokalne są już wystarczające i szybko się udoskonalają.