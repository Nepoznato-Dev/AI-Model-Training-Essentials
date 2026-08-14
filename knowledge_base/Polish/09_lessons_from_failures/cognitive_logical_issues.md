---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Błędy poznawcze i błędy logiczne
Dokument ten konsoliduje błędy poznawcze, błędy logiczne i błędy w rozumowaniu, które wpływają zarówno na proces podejmowania decyzji przez człowieka, jak i na wyniki systemów sztucznej inteligencji.
---

## Błędy poznawcze
Błędy poznawcze to systematyczne wzorce odchyleń od racjonalności w ocenie i podejmowaniu decyzji. W przypadku tworzenia oprogramowania i systemów AI może to prowadzić do błędnych decyzji projektowych, błędnych wymagań i stronniczego zachowania modelu.
### Błąd potwierdzenia
**Co to jest:** Tendencja do wyszukiwania, interpretowania i przypominania sobie informacji w sposób potwierdzający istniejące wcześniej przekonania.
**Zły przykład w rozwoju:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**W recenzjach kodu:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Łagodzenie:**
- Aktywnie szukaj niepotwierdzających dowodów
- Korzystaj z recenzji kodów ślepych
- Zachęcaj do wyrażania odmiennych opinii
- Wyraźnie dokumentuj założenia
### Stronniczość zakotwiczenia
**Co to jest:** Zbyt duże poleganie na pierwszej napotkanej informacji.
**Zły przykład:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Łagodzenie:**
- Uzyskaj wiele niezależnych szacunków
- Użyj pokera planowania do oszacowania
- Weź pod uwagę zakresy zamiast szacunków punktowych
- Referencyjne dane historyczne
### Błąd utopionych kosztów
**Co to jest:** Kontynuowanie przedsięwzięcia ze względu na wcześniej zainwestowane zasoby (czas, pieniądze, wysiłek), nawet jeśli lepiej będzie je porzucić.
**Zły przykład:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Łagodzenie:**
- Oceniaj decyzje w oparciu o przyszłą wartość, a nie przeszłe inwestycje
- Regularnie oceniaj wykonalność projektu
- Stwórz psychologiczne bezpieczeństwo podczas obracania się
- Stosuj obiektywne kryteria przy podejmowaniu decyzji o kontynuacji/zatrzymaniu
### Heurystyka dostępności
**Co to jest:** przecenianie znaczenia informacji, które są łatwo dostępne lub aktualne.
**Zły przykład:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Łagodzenie:**
- Korzystaj z podejmowania decyzji w oparciu o dane
- Skonsultuj kompleksowe modele zagrożeń
- Spójrz na stawki podstawowe i statystyki
- Unikaj stronniczości związanej z nieaktualnością w ustalaniu priorytetów
### Efekt Dunninga-Krugera
**Co to jest:** Osoby o niskich umiejętnościach w zadaniu przeceniają swoje możliwości; eksperci mogą ich nie doceniać.
**Zły przykład:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Łagodzenie:**
- Zachęcaj do ciągłego uczenia się
- Wdrożyć procesy wzajemnej oceny
- Tworzenie programów mentorskich
- Rozwijaj pokorę i ciekawość
---

## Błędy logiczne
Błędy logiczne to błędy w rozumowaniu, które podważają ważność argumentów. Modele AI mogą generować wyniki zawierające te błędy.
### Ad Hominem (atak na osobę)
**Co to jest:** Atakowanie osoby przedstawiającej argument, a nie samego argumentu.
**Zły przykład:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Dlaczego jest to złe:** Ważność opinii zależy od jej treści, a nie od stażu pracy recenzenta.
### Odwołaj się do władzy
**Co to jest:** twierdzenie, że coś jest prawdą, ponieważ twierdzi to autorytet bez dowodów.
**Zły przykład:**```markdown
"This architecture must be correct because Google uses it."
```

**Dlaczego jest to złe:** To, co sprawdza się w przypadku Google na daną skalę, może nie działać w Twoim przypadku.
### Fałszywa dychotomia (myślenie czarno-białe)
**Co to jest:** Prezentujemy tylko dwie opcje, jeśli istnieje ich więcej.
**Zły przykład:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Rzeczywistość:** Istnieje wiele opcji pomiędzy tymi skrajnościami (optymalizuj gorące ścieżki, używaj Rusta dla określonych komponentów, ulepszaj kod Pythona itp.)
### Śliskie zbocze
**Co to jest:** Twierdzenie, że jedno wydarzenie nieuchronnie doprowadzi do łańcucha negatywnych konsekwencji.
**Zły przykład:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Dlaczego to jest złe:** Zakłada nieunikniony postęp bez dowodów; pomija czynniki łagodzące.
### Rozumowanie okrężne
**Co to jest:** Używanie wniosku jako przesłanki.
**Zły przykład:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (fałszywa przyczyna)
**Co to jest:** Zakładając, że ponieważ B nastąpiło po A, A spowodowało B.
**Zły przykład:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Rzeczywistość:** Korelacja nie oznacza związku przyczynowego. Inne czynniki mogą być odpowiedzialne.
### Słomiany Człowiek
**Co to jest:** fałszywe przedstawianie czyichś argumentów, aby ułatwić atak.
**Zły przykład:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Błędny pogląd na modę
**Co to jest:** Argumentowanie o czymś jest słuszne, ponieważ wiele osób w to wierzy.
**Zły przykład:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Dlaczego to jest złe:** Popularność nie gwarantuje przydatności do Twoich konkretnych potrzeb.
---

## Błędy w rozumowaniu w sztucznej inteligencji
### Wieloetapowe błędy logiczne
**Zły przykład:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Dlaczego to jest złe:**
- Popełnia błąd afirmacji następstwa
- Alicja potrafiła pisać kod, nie będąc programistą
- Struktura logiczna: (P → Q, Q) ⊬ P
**Prawidłowe rozumowanie:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Błędy w rozumowaniu matematycznym
**Zły przykład:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Rzeczywistość:** Jeśli piłka kosztuje 0,10 USD, a kij kosztuje o 1 USD więcej (1,10 USD), suma wyniesie 1,20 USD. Prawidłowa odpowiedź to 0,05 dolara za piłkę i 1,05 dolara za kij.
### Błędy w rozumowaniu przyczynowym
**Zły przykład:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Rzeczywistość:** Obydwa zjawiska są spowodowane trzecim czynnikiem (gorącą pogodą), a nie sobą nawzajem.
---

## Strategie doskonalenia
### Do podejmowania decyzji przez ludzi
1. **Trening świadomości**: Naucz się rozpoznawać powszechne uprzedzenia
2. **Wykorzystanie listy kontrolnej**: Użyj list kontrolnych decyzji, aby przeciwdziałać stronniczości
3. **Różne zespoły**: Włączaj ludzi o różnych perspektywach
4. **Badania przedśmiertne**: Wyobraź sobie porażkę i cofnij się, aby zidentyfikować przyczyny
5. **Dokumentacja**: Zapisz uzasadnienie do późniejszego przeglądu
### Dla systemów AI
1. **Podpowiedzi w ramach łańcucha myślowego**: Poproś model, aby pokazał kroki rozumowania
2. **Samokorekta**: Poproś model o przejrzenie i krytykę odpowiedzi
3. **Weryfikacja formalna**: Użyj symbolicznych narzędzi rozumowania dla logiki krytycznej
4. **Dekompozycja**: Podziel złożone problemy na mniejsze kroki
5. **Narzędzia zewnętrzne**: Używaj kalkulatorów i solwerów do zadań matematycznych
6. **Wiele próbek**: Wygeneruj wiele odpowiedzi i porównaj
---

## Powiązane tematy
- **Awarie AI/LLM**: Zobacz`ai_llm_failures.md`w przypadku halucynacji i problemów z rozumowaniem
- **Sprzeczne źródła**: Zobacz dokumentację dotyczącą oceny sprzecznych informacji
- **Krytyczne myślenie**: Zastosuj te koncepcje do oceny argumentów i dowodów
- **Szybka inżynieria**: Patrz `../02_artificial_intelligence/prompt_engineering.md`, aby zapoznać się z technikami ograniczania błędów w rozumowaniu
---

## Dodatkowe błędy poznawcze w tworzeniu oprogramowania
### Stronniczość dotycząca status quo
**Co to jest:** Preferencja utrzymania obecnego stanu; każda zmiana jest postrzegana jako strata.
**Zły przykład:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Łagodzenie:**
- Określ ilościowo koszty braku zmian
- Ustaw regularne harmonogramy aktualizacji
- Tworzenie bezpiecznych środowisk eksperymentalnych
- Przedstawiaj zmiany jako możliwości, a nie zagrożenia
### Stronnictwo optymizmu
**Co to jest:** Niedocenianie czasu, kosztów i ryzyka przy jednoczesnym przecenianiu korzyści.
**Zły przykład:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Łagodzenie:**
- Użyj prognozowania klasy referencyjnej (porównaj z podobnymi projektami z przeszłości)
- Dodaj bufory awaryjne (20-50%)
- Przeprowadzić sekcję zwłok
- Śledź dokładność szacunków w czasie
### Błąd w przetrwaniu
**Co to jest:** Koncentrowanie się na udanych przykładach i ignorowanie porażek.
**Zły przykład:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Łagodzenie:**
- Studiuj zarówno sukcesy, jak i porażki
- Poszukaj stawek podstawowych i statystyk
- Weź pod uwagę niewidoczne dane
- Unikaj wybierania przykładów
### Podstawowy błąd atrybucji
**Co to jest:** Przypisywanie zachowań innych charakterowi, a nie okolicznościom.
**Zły przykład:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Łagodzenie:**
- Weź pod uwagę czynniki sytuacyjne
- Ćwicz empatię
- Skoncentruj się na systemach, a nie na osobach
- Użyj nienagannej sekcji zwłok
### Stronniczość wynikająca z perspektywy czasu
**Co to jest:** po wystąpieniu zdarzenia, wierząc, że było ono przez cały czas przewidywalne.
**Zły przykład:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Łagodzenie:**
- Dokumentuj prognozy przed wynikami
- Przejrzyj kontekst decyzji, a nie tylko wyniki
- Unikaj kultury „a nie mówiłem”.
- Skoncentruj się na doskonaleniu procesów, a nie na przypisywaniu winy
---

## Więcej błędów logicznych
### Odwołanie do nowości
**Co to jest:** Zakładanie, że coś jest lepsze, ponieważ jest nowsze.
**Zły przykład:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Odwołanie do tradycji
**Co to jest:** Argumentowanie za czymś jest prawidłowe, ponieważ zawsze tak było.
**Zły przykład:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (odwołanie do hipokryzji)
**Co to jest:** Odrzucanie krytyki poprzez wskazanie niekonsekwencji krytyka.
**Zły przykład:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Załadowane pytanie
**Co to jest:** Zadawanie pytania zawierającego założenia.
**Zły przykład:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Żaden prawdziwy Szkot
**Co to jest:** Robienie wyjątku od uniwersalnego roszczenia w przypadku jego zakwestionowania.
**Zły przykład:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Błąd genetyczny
**Co to jest:** ocenianie czegoś na podstawie jego pochodzenia, a nie aktualnych zalet.
**Zły przykład:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Błąd środka
**Co to jest:** Zakładając, że prawda zawsze leży pośrodku dwóch skrajności.
**Zły przykład:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Błędy poznawcze w systemach AI
### Błąd danych treningowych
Modele AI dziedziczą błędy obecne w danych szkoleniowych.
**Przykład:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Łagodzenie:**
- Audyt danych szkoleniowych pod kątem błędów
- Stosuj techniki uprzedzające
- Test na stronnicze wyjścia
- Zróżnicowane gromadzenie danych
### Stronniczość automatyzacji
**Co to jest:** nadmierne poleganie na zautomatyzowanych systemach, nawet jeśli się mylą.
**Przykład:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Łagodzenie:**
- Utrzymuj nadzór ludzki
- Zachęcaj do krytycznej oceny wyników sztucznej inteligencji
- Nie traktuj sztucznej inteligencji jako nieomylnej
- Wdrożyć procesy przeglądu
### Iluzja zrozumienia
**Co to jest:** wiara, że ​​rozumiesz, jak działa sztuczna inteligencja, choć tak nie jest.
**Przykład:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Łagodzenie:**
- Edukuj użytkowników na temat ograniczeń AI
- Bądź przejrzysty w kwestii działania systemów
- Unikaj antropomorfizacji sztucznej inteligencji
- Ustaw odpowiednie oczekiwania
---

## Studia przypadków
### Studium przypadku 1: Błąd potwierdzenia w wyborze architektury
**Incydent:** zespół wybrał architekturę mikrousług dla małej aplikacji.
**Główna przyczyna:** Lider zespołu przeczytał kilka artykułów wychwalających mikrousługi i 
szukał jedynie informacji potwierdzających ten wybór, ignorując ostrzeżenia o złożoności.
**Wpływ:**
- Ogromne koszty ogólne dla zespołu 3 programistów
- Złożoność wdrożenia wzrosła 10-krotnie
- Wydajność spadła z powodu połączeń sieciowych
- Projekt opóźniony o 6 miesięcy
**Lekcja:** Oceniaj architektury na podstawie konkretnego kontekstu, a nie tylko 
pozytywne referencje. Należy wyraźnie rozważyć kompromisy.
### Studium przypadku 2: Koszty utopione w starszym systemie
**Incydent:** Firma kontynuowała utrzymywanie niestandardowego systemu CRM przez 5 lat 
pomimo lepszych alternatyw.
**Podstawowa przyczyna:** „Zainwestowaliśmy już 2 miliony dolarów, nie możemy teraz tego porzucić”.
**Wpływ:**
- Roczny koszt utrzymania: 500 tys. dolarów
- Koszt alternatywny: brak możliwości korzystania z nowoczesnych funkcji
- Problemy z utrzymaniem talentów (programiści chcieli pracować z nowoczesnymi technologiami)
- Całkowity koszt 5-letni: 4,5 mln USD w porównaniu z 1,5 mln USD w przypadku alternatywy SaaS
**Lekcja:** Wcześniejsze inwestycje zostały utopione. Podejmuj decyzje w oparciu o przyszłą wartość.
### Studium przypadku 3: Heurystyka dostępności w zabezpieczeniach
**Incydent:** Zespół uznał za priorytet obronę przed niedawno nagłośnionym atakiem 
wektor, ignorując bardziej prawdopodobne zagrożenia.
**Główna przyczyna:** Najnowsze doniesienia sprawiły, że jeden typ zagrożenia stał się wysoce dostępny 
w pamięci, wypaczając ocenę ryzyka.
**Wpływ:**
- Wydano 100 tys. dolarów na łagodzenie zagrożeń o niskim prawdopodobieństwie
- Rzeczywiste naruszenie nastąpiło poprzez zaniedbany wektor
- Koszt odzyskiwania: ponad 500 tys. dolarów
**Lekcja:** Stosuj modelowanie zagrożeń oparte na danych, a nie ustalanie priorytetów na podstawie aktualności.
---

## Ćwiczenia praktyczne
### Ćwiczenie wykrywania stronniczości
Przejrzyj ostatnie decyzje i zapytaj:
1. Jakie przyjęliśmy założenia?
2. Jakie dowody zaprzeczyłyby naszemu wnioskowi?
3. Czy rozważyliśmy wiele opcji, czy zakotwiczyliśmy się w pierwszym pomyśle?
4. Czy kontynuujemy ze względu na przyszłą wartość czy przeszłe inwestycje?
5. Co polecilibyśmy, gdyby ktoś nas o to zapytał?
### Wykrywanie błędów logicznych
Przećwicz rozpoznawanie błędów w codziennych dyskusjach:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Technika przedśmiertna
Przed rozpoczęciem projektu:
1. Wyobraź sobie, że jest to za 6 miesięcy
2. Projekt poniósł spektakularną porażkę
3. Napisz historię, dlaczego się nie udało
4. Cofnij się, aby zapobiec tym trybom awarii
Przeciwdziała to stronniczości optymizmu i heurystyce dostępności.
---

## Narzędzia i struktury
### Szablon dziennika decyzji
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Lista kontrolna stronniczości
Przed podjęciem ważnych decyzji:
- [ ] Czy szukaliśmy niepotwierdzających dowodów?
- [ ] Czy jesteśmy zakotwiczeni w informacjach początkowych?
- [ ] Czy koszty utopione mają na nas wpływ?
- [ ] Czy jesteśmy zbyt pewni naszych szacunków?
- [ ] Czy uwzględniliśmy stawki podstawowe?
- [ ] Czy mamy do czynienia z błędem dostępności/aktualności?
- [ ] Czy dokonalibyśmy tego samego wyboru, zaczynając od nowa?
### Ćwiczenie drużyny czerwonej
Wyznacz osobę, która będzie sprzeciwiać się proponowanej decyzji:
- Ich rolą jest znajdowanie wad
- Muszą przedstawiać alternatywne punkty widzenia
- Praktyki zespołowe w zakresie konstruktywnego reagowania na krytykę
- Zgłoszono i rozwiązano wątpliwości dotyczące dokumentów
Przeciwdziała to stronniczości potwierdzenia i myśleniu grupowemu.