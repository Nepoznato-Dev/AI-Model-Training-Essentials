<!-- 
이 파일은 영어에서 한국어로 자동 번역되었습니다.
원본: prompt_engineering.md
참고: 기술 용어, 코드 예시, 고유 명사는 영어로 남아 있을 수 있습니다.
정확성 개선을 위해 풀 리퀘스트를 통해 기여해 주세요.
-->

# 프롬프트 엔지니어링

프롬프트 엔지니어링은 언어 모델로부터 최상의 결과를 얻기 위해 입력 프롬프트를 설계, 정제, 최적화하는 실천법입니다. 이는 예술이자 과학이며, 파인튜닝 없이 LLM 동작을 제어하는 주요 인터페이스입니다.

---

## 핵심 원칙

### 명확성과 구체성
명확한 프롬프트는 모호함의 여지를 남기지 않습니다. 형식, 길이, 관점을 포함하여 원하는 것을 정확히 명시하세요.

**모호함:**
> "Python 에 대해 알려주세요."

**구체적:**
> "Python 의 Global Interpreter Lock (GIL) 을 설명하세요. 멀티스레딩에 미치는 영향을 설명하고, 하나의 우회 방법을 제시하며, 답변을 200 단어 이내로 유지하세요."

### 컨텍스트 제공
모델은 역할, 대상, 목표를 알 때 더 잘 수행합니다.

**컨텍스트 없음:**
> "리스트를 정렬하는 함수를 작성하세요."

**컨텍스트 있음:**
> "당신은 시니어 Python 개발자입니다. 주어진 키를 기준으로 딕셔너리 리스트를 정렬하는 함수를 작성하세요. 타입 힌트를 사용하고 엣지 케이스를 처리하세요. 대상은 주니어 개발자입니다."

### 긍정적인 지시 사용
모델에게 무엇을 해야 하는지 말하지, 무엇을 피해야 하는지 말하지 마세요. "전문 용어를 포함하지 마세요"보다 "10 세도 이해할 수 있는 간단한 언어를 사용하세요"가 더 효과적입니다.

---

## 프롬프트 구조

### 시스템 / 사용자 / 어시스턴트 역할
대부분의 LLM API 는 다회전 구조를 지원합니다:

- **시스템 메시지**: 모델의 동작, 페르소나, 제약 조건을 설정합니다 (세션 전체에 지속됨).
- **사용자 메시지**: 현재 쿼리 또는 지시사항.
- **어시스턴트 메시지**: 모델의 이전 응답 (연속성을 위해 사용).

**예시 (OpenAI API 스타일):**
시스템: 당신은 도움이 되는 코딩 어시스턴트입니다. 간결한 코드 예시와 짧은 설명으로 답변합니다. 안전하지 않은 코드는 절대 제공하지 않습니다.
사용자: URL 에서 파일을 다운로드하는 Python 함수를 작성하세요.

### Few-Shot 프롬프팅
모델에게 작업을 수행하도록 요청하기 전에 2-3 개의 원하는 입력 - 출력 형식 예시를 제공하세요. 이렇게 하면 패턴을 학습할 수 있습니다.

**예시:**
사용자: 다음 문장을 수동태로 변환하세요:
입력: 그 고양이가 쥐를 쫓았다.
출력: 쥐가 고양이에게 쫓겼다.
입력: 그 셰프가 식사를 준비했다.
출력: 식사가 셰프에 의해 준비되었다.
입력: 그 폭풍이 집을 파괴했다.
출력: (모델이 완성)

### Chain-of-Thought (CoT, 연쇄 사고)
모델에게 단계별로 추론 과정을 보여주도록 유도하세요. 이는 산수, 논리, 다단계 작업의 정확도를 향상시킵니다.

**CoT 없음:**
> "24 × 37 은 얼마인가요?"

**CoT 있음:**
> "24 × 37 을 계산하세요. 추론 과정을 단계별로 보여주세요."

모델은 중간 단계를 생성하여 산수 오류를 줄입니다.

### 구조화된 출력
JSON, YAML 또는 마크다운 테이블과 같은 특정 형식을 요청하여 파싱을 신뢰할 수 있게 만드세요.
사용자: 마이크로서비스의 장단점을 각각 세 개씩 나열하세요. "pros" 와 "cons" 키를 가진 유효한 JSON 객체만 반환하세요. 각 키는 문자열 배열이어야 합니다.

---

## 고급 기법

### 자기 일관성 (Self-Consistency)
동일한 프롬프트에 대해 여러 응답을 생성하고 (temperature > 0 사용) 최종 답변에 대해 다수결 투표를 진행하세요. 이는 추론 작업에 특히 효과적입니다.

### Tree-of-Thoughts (사고 나무)
여러 추론 경로를 병렬로 탐색하고, 각각을 평가한 후 최상의 것을 선택하세요. 이는 연구 수준의 기법이지만, 모델에게 "대안적 솔루션을 탐색하라"고 요청하여 근사할 수 있습니다.

### ReAct (추론 + 행동)
모델이 추론과 도구 호출을 교차하게 하세요. 생각한 후 행동하고 (예: 웹 검색, 코드 실행), 그 결과를 바탕으로 다시 생각할 수 있습니다.

**프롬프트 구조:**
당신은 계산기와 검색 엔진을 사용할 수 있습니다. 각 단계에서 다음을 출력하세요:
Thought: (당신의 추론)
Action: (도구 이름, 입력)
Observation: (도구 출력)
... 최종 답을 얻을 때까지 계속합니다.

### 페르소나 할당
응답의 틀을 잡기 위해 특정 페르소나를 할당하세요.

**예시:**
- "당신은 신입 졸업생에게 메모리 관리를 설명하는 리눅스 커널 개발자입니다."
- "당신은 클라이언트에게 일반적인 조언을 제공하는 친절한 영양학자입니다."
- "당신은 새로운 가제트를 검토하는 냉소적인 기술 비평가입니다."

**예시:**
- "You are a Linux kernel developer explaining memory 관리 to a new graduate."
- "You are a friendly nutritionist giving general advice to a client."
- "You are a cynical tech critic reviewing a new gadget."

---

## Parameter Tuning

- **Temperature** (0.0 – 1.0+): Controls randomness. Lower = more deterministic, higher = more creative. Use 0.0–0.3 위한 factual answers; 0.7–1.0 위한 creative writing.
- **Top-p** (nucleus sampling): Cuts off 그 probability mass at a certain cumulative threshold. 0.9 means 그 model samples from 그 top 90% 의 likely tokens. Usually adjust either temperature or top-p, not both.
- **Max tokens**: Sets 그 maximum output length. Remember to reserve space 위한 그 response within 그 context window.
- **Frequency penalty**: Reduces repetition 의 그 same tokens.
- **Presence penalty**: Encourages 그 model to introduce new topics.

---

## Common Pitfalls 와 Fixes

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Model ignores parts 의 prompt | Prompt too long or overloaded | Shorten; put 그 most important instruction at 그 end |
| Output is too verbose | No length constraint | Add "Limit to 3 sentences" or set max_tokens |
| Output is too terse | Overly restrictive | Add "Explain 에서 detail" or lower temperature |
| Factual hallucinations | Insufficient context or ambiguous question | Add "If you are unsure, say 'I don't know'" 와 provide a RAG context |
| Inconsistent formatting | No explicit format instruction | Ask 위한 JSON, markdown table, or bullet list |
| Model answers 에서 wrong 언어 | No 언어 instruction | Explicitly state "Respond 에서 영어" (or your target 언어) |

---

## Prompt Templates 위한 Common Tasks

### Summarisation
Summarise 그 following text 에서 3 bullet points. Focus on 그 main arguments 와 avoid details.

Text: [insert text]


### Code Generation
Write a [언어] function that [does X].
Requirements:

Use type hints.

Include a docstring.

Handle edge cases: [list].

Do not use external libraries unless specified.


### Explanation
Explain [concept] to a [non-expert / university student / child]. Use an analogy where appropriate.

### Brainstorming
Generate 10 ideas 위한 [topic]. 위한 each idea, give a one-sentence description 와 one potential challenge.

text

### Classification
Classify 그 following customer 피드백 as [positive, neutral, negative].
Provide a confidence score (0-100) 와 a brief reason.

피드백: [insert text]

### Translation 와 함께 Style
Translate 그 following 영어 text to Spanish. Use an informal tone suitable 위한 a social media post.
Text: [insert text]

---

## Evaluation 의 Prompts

Treat prompts as code: version them, test them, 와 iterate.

- **A/B test** different prompt variants on a held-out set 의 queries.
- **Measure success** via human evaluation or automated metrics (e.g., exact match, BLEU, custom scoring).
- **Keep a prompt registry** (a simple text file or spreadsheet) 와 함께 그 prompt, version, 와 observed 성능.

---