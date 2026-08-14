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
# 인지적 편견과 논리적 오류
이 문서는 인간의 의사 결정과 AI 시스템 출력 모두에 영향을 미치는 인지 편향, 논리적 오류 및 추론 오류를 통합합니다.
---

## 인지 편향
인지 편향은 판단과 의사 결정에서 합리성에서 벗어나는 체계적인 패턴입니다. 소프트웨어 개발 및 AI 시스템에서 이는 잘못된 설계 결정, 결함 있는 요구 사항 및 편향된 모델 동작으로 이어질 수 있습니다.
### 확증편향
**정의:** 기존 믿음을 확인하는 방식으로 정보를 검색하고 해석하고 기억하는 경향입니다.
**개발 중 나쁜 예:**```python
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

**코드 리뷰에서:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**완화:**
- 반증적인 증거를 적극적으로 찾으십시오.
- 블라인드 코드 리뷰를 활용하세요
- 반대 의견을 장려
- 가정을 명시적으로 문서화하세요.
### 고정 편견
**정의:** 처음 접한 정보에 너무 많이 의존합니다.
**나쁜 예:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**완화:**
- 여러 개의 독립적인 견적을 받아보세요
- 추정을 위해 플래닝 포커를 사용하세요.
- 점 추정 대신 범위 고려
- 참고 역사적 데이터
### 매몰 비용 오류
**정의:** 이전에 투자한 리소스(시간, 돈, 노력) 때문에 포기하더라도 계속해서 노력하는 것이 더 좋습니다.
**나쁜 예:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**완화:**
- 과거의 투자가 아닌 미래의 가치를 기준으로 의사결정을 평가합니다.
- 프로젝트 실행 가능성을 정기적으로 재평가
- 피봇팅에 대한 심리적 안정감을 조성합니다.
- 계속/중지 결정을 위해 객관적인 기준을 사용합니다.
### 가용성 휴리스틱
**정의:** 쉽게 이용할 수 있거나 최신 정보의 중요성을 과대평가합니다.
**나쁜 예:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**완화:**
- 데이터 기반 의사 결정을 사용합니다.
- 포괄적인 위협 모델을 참조하세요.
- 기본요금과 통계를 살펴보세요
- 우선순위에 있어서 최신 편향을 피하세요.
### 더닝-크루거 효과
**정의:** 업무 능력이 낮은 사람들은 자신의 능력을 과대평가합니다. 전문가들은 자신의 의견을 과소평가할 수 있습니다.
**나쁜 예:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**완화:**
- 지속적인 학습을 장려합니다.
- 동료 검토 프로세스 구현
- 멘토링 프로그램 만들기
- 겸손함과 호기심을 키워주세요.
---

## 논리적 오류
논리적 오류는 논증의 타당성을 훼손하는 추론의 오류입니다. AI 모델은 이러한 오류가 포함된 출력을 생성할 수 있습니다.
### Ad Hominem(사람에 대한 공격)
**정의:** 논쟁 자체보다는 논쟁을 벌이는 사람을 공격합니다.
**나쁜 예:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**나쁜 이유:** 피드백의 유효성은 리뷰어의 직위가 아닌 내용에 따라 달라집니다.
### 권위에 호소
**정의:** 권위 있는 인물이 증거 없이 그렇게 말했기 때문에 무언가를 주장하는 것이 사실입니다.
**나쁜 예:**```markdown
"This architecture must be correct because Google uses it."
```

**나쁜 이유:** 규모에 따라 Google에 적합한 것이 귀하의 사용 사례에는 적합하지 않을 수 있습니다.
### 잘못된 이분법(흑백 사고)
**정의:** 더 많은 옵션이 있는 경우 두 가지 옵션만 제시합니다.
**나쁜 예:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**현실:** 이러한 극단 사이에는 많은 옵션이 존재합니다(핫 경로 최적화, 특정 구성 요소에 Rust 사용, Python 코드 개선 등).
### 미끄러운 경사면
**정의:** 하나의 사건이 필연적으로 일련의 부정적인 결과를 초래할 것이라고 주장합니다.
**나쁜 예:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**나쁜 이유:** 증거 없이 진행이 불가피하다고 가정합니다. 완화 요인을 무시합니다.
### 순환논리
**정의:** 결론을 전제로 사용합니다.
**나쁜 예:**```markdown
"Our code is high quality because we write good code."
```

### 사후 Ergo Propter Hoc(거짓 원인)
**정의:** B가 A를 따랐기 때문에 A가 B를 발생시켰다고 가정합니다.
**나쁜 예:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**현실:** 상관관계는 인과관계를 의미하지 않습니다. 다른 요인이 원인일 수 있습니다.
### 밀짚맨
**정의:** 공격하기 쉽도록 누군가의 주장을 허위로 표현하는 것입니다.
**나쁜 예:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### 악대왜건 오류
**정의:** 많은 사람들이 그것을 믿기 때문에 어떤 것이 옳다고 주장하는 것입니다.
**나쁜 예:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**나쁜 이유:** 인기가 귀하의 특정 요구에 대한 적합성을 보장하지는 않습니다.
---

## AI의 추론 실패
### 다단계 논리 오류
**나쁜 예:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**나쁜 이유:**
- 결과를 긍정하는 오류를 범한다.
- 앨리스는 프로그래머가 아니어도 코드를 작성할 수 있었습니다
- 논리 구조: (P→Q, Q) ⊬ P
**올바른 추론:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### 수학적 추론 실패
**나쁜 예:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**현실:** 공 가격이 $0.10이고 배트 가격이 $1 더 비싸다면($1.10) 총액은 $1.20가 됩니다. 정답은 공의 경우 $0.05, 배트의 경우 $1.05입니다.
### 인과 추론 오류
**나쁜 예:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**현실:** 둘 다 서로에 의한 것이 아니라 세 번째 요인(더운 날씨)에 의해 발생합니다.
---

## 개선 전략
### 인간의 의사결정을 위해
1. **인식 교육**: 일반적인 편견을 인식하는 방법을 배웁니다.
2. **체크리스트 사용**: 편견에 대응하기 위해 의사결정 체크리스트를 사용하세요.
3. **다양한 팀**: 다양한 관점을 가진 사람들을 포함하세요
4. **사전 분석**: 실패를 상상하고 거꾸로 작업하여 원인을 파악합니다.
5. **문서화**: 추후 검토를 위한 추론 기록
### AI 시스템용
1. **사고 사슬 프롬프트**: 모델에게 추론 단계를 보여달라고 요청합니다.
2. **자기 수정**: 모델이 답변을 검토하고 비평하도록 합니다.
3. **형식적 검증**: 중요한 논리를 위해 상징적 추론 도구를 사용합니다.
4. **분해**: 복잡한 문제를 더 작은 단계로 나누기
5. **외부 도구**: 수학 작업에 계산기와 솔버를 사용하세요.
6. **다중 표본**: 다중 응답 생성 및 비교
---

## 관련 주제
- **AI/LLM 오류**: 환각 및 추론 문제는 `ai_llm_failures.md`를 참조하세요.
- **모순되는 소스**: 상충되는 정보 평가에 대한 문서를 참조하세요.
- **비판적 사고**: 이러한 개념을 적용하여 주장과 증거를 평가합니다.
- **신속한 엔지니어링**: 추론 오류를 줄이는 기술은 `../02_artificial_intelligence/prompt_engineering.md`를 참조하세요.
---

## 소프트웨어 개발의 추가적인 인지 편향
### 현상 유지 편향
**정의:** 현재 상태 유지를 선호합니다. 모든 변화는 손실로 인식됩니다.
**나쁜 예:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**완화:**
- 변경하지 않는 데 드는 비용을 정량화합니다.
- 정기적인 업그레이드 일정 설정
- 안전한 실험 환경 조성
- 변화를 위협이 아닌 기회로 프레임화
### 낙관주의 편향
**정의:** 시간, 비용, 위험은 과소평가하면서 이점은 과대평가합니다.
**나쁜 예:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**완화:**
- 참조 클래스 예측 사용(유사한 과거 프로젝트와 비교)
- 비상 버퍼 추가(20-50%)
- 사전부검 실시
- 시간 경과에 따른 추정 정확도 추적
### 생존 편향
**정의:** 실패를 무시하고 성공적인 사례에 집중합니다.
**나쁜 예:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**완화:**
- 성공과 실패를 모두 연구하세요.
- 기본 요율 및 통계를 찾아보세요
- 눈에 보이지 않는 데이터를 고려
- 체리 따기 예시를 피하세요
### 기본 귀속 오류
**정의:** 다른 사람의 행동을 상황이 아닌 성격에 귀인시키는 것입니다.
**나쁜 예:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**완화:**
- 상황적 요인을 고려하라
- 공감을 실천하라
- 개인이 아닌 시스템에 집중
- 비난 없는 사후 부검을 사용하세요.
### 사후 판단 편향
**정의:** 사건이 발생한 후에는 그것이 내내 예측 가능했다고 믿습니다.
**나쁜 예:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**완화:**
- 결과 전 예측 문서화
- 단순한 결과가 아닌 의사결정 맥락 검토
- '내가 그랬다'는 문화를 피하세요
- 책임을 전가하지 않고 프로세스 개선에 집중
---

## 더 많은 논리적 오류
### 참신함에 대한 호소
**정의:** 새로운 것이기 때문에 더 좋다고 가정하는 것입니다.
**나쁜 예:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### 전통에 대한 호소
**정의:** 항상 그렇게 해왔기 때문에 뭔가가 옳다고 주장하는 것입니다.
**나쁜 예:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque(위선에 대한 호소)
**정의:** 비평가의 불일치를 지적하여 비판을 일축합니다.
**나쁜 예:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### 로드된 질문
**정의:** 가정이 포함된 질문입니다.
**나쁜 예:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### 진정한 스코틀랜드 사람은 없습니다
**정의:** 이의제기 시 보편적 주장에 예외를 적용합니다.
**나쁜 예:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### 유전적 오류
**정의:** 현재의 장점보다는 출처를 기준으로 무언가를 판단합니다.
**나쁜 예:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### 중간지대 오류
**정의:** 진실을 가정하는 것은 항상 두 극단의 중간에 있습니다.
**나쁜 예:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## AI 시스템의 인지 편향
### 훈련 데이터 편향
AI 모델은 훈련 데이터에 존재하는 편향을 상속합니다.
**예:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**완화:**
- 편향에 대한 훈련 데이터 감사
- 편견 제거 기술을 사용하세요.
- 편향된 출력 테스트
- 다양한 데이터 수집
### 자동화 편향
**정의:** 자동화된 시스템이 잘못된 경우에도 지나치게 의존합니다.
**예:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**완화:**
- 인간의 감독을 유지
- AI 결과물에 대한 비판적 평가를 장려합니다.
- AI를 오류가 없는 것으로 취급하지 마세요.
- 검토 프로세스 구현
### 이해의 환상
**정의:** AI가 작동하지 않는데도 AI가 어떻게 작동하는지 이해하고 있다고 믿습니다.
**예:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**완화:**
- AI 한계에 대해 사용자 교육
- 시스템 작동 방식을 투명하게 공개하세요.
- AI를 의인화하지 마세요.
- 적절한 기대치를 설정하십시오.
---

## 사례 연구
### 사례 연구 1: 아키텍처 선택의 확증 편향
**사건:** 한 팀은 소규모 애플리케이션을 위해 마이크로서비스 아키텍처를 선택했습니다.
**근본 원인:** 팀 리더는 마이크로서비스를 칭찬하는 여러 기사를 읽었으며 
복잡성에 대한 경고를 무시하고 이 선택을 확인하는 정보만 찾았습니다.
**영향:**
- 3명의 개발자로 구성된 팀의 막대한 오버헤드
- 배포 복잡성이 10배 증가했습니다.
- 네트워크 호출로 인해 성능 저하
- 프로젝트가 6개월 지연되었습니다.
**강의:** 단순한 상황이 아닌 특정 상황을 기반으로 아키텍처를 평가하세요. 
긍정적인 평가. 명시적으로 절충점을 고려하십시오.
### 사례 연구 2: 레거시 시스템의 매몰 비용
**사고:** 회사는 5년 동안 맞춤형 CRM을 계속 유지했습니다. 
더 나은 대안에도 불구하고.
**근본 원인:** "이미 200만 달러를 투자했는데 지금은 버릴 수 없습니다."
**영향:**
- 연간 유지관리 비용: $500,000
- 기회비용: 최신 기능을 사용할 수 없음
- 인재 유지 문제(개발자는 최신 기술로 작업하기를 원함)
- 총 5년 비용: $450만 대 SaaS 대안의 경우 $150만
** 교훈: ** 과거 투자는 매몰되었습니다. 미래 가치를 기반으로 의사 결정을 내립니다.
### 사례 연구 3: 보안의 가용성 휴리스틱
**사건:** 팀은 최근 공개된 공격에 대한 방어를 최우선으로 생각했습니다. 
가능성이 더 높은 위협은 무시하면서 벡터를 공격합니다.
**근본 원인:** 최근 뉴스 보도에 따르면 하나의 위협 유형에 대한 가용성이 높아졌습니다. 
메모리에 위험 평가가 왜곡되어 있습니다.
**영향:**
- 확률이 낮은 위협을 완화하는 데 10만 달러 지출
- 방치된 벡터로 인해 실제 침해가 발생함
- 복구 비용: $500K+
**교훈:** 최근성 기반 우선순위 지정이 아닌 데이터 기반 위협 모델링을 사용하십시오.
---

## 실습
### 편향 탐지 연습
최근 결정을 검토하고 질문하십시오.
1. 우리는 어떤 가정을 했나요?
2. 우리의 결론과 모순되는 증거는 무엇입니까?
3. 여러 옵션을 고려했거나 첫 번째 아이디어를 기준으로 삼았나요?
4. 우리는 미래가치 때문에 계속되는 걸까요, 아니면 과거의 투자 때문에 계속되는 걸까요?
5. 다른 사람이 우리에게 묻는다면 무엇을 추천하시겠습니까?
### 논리적 오류 발견
일상적인 토론에서 오류를 식별하는 연습을 해보세요.
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### 사전 부검 기법
프로젝트를 시작하기 전에:
1. 6개월 후의 미래를 상상해 보세요
2. 프로젝트는 눈에 띄게 실패했습니다
3. 실패한 이유에 대한 이야기를 쓰세요
4. 이러한 실패 모드를 방지하기 위해 역방향 작업
이는 낙관주의 편향과 가용성 휴리스틱에 대응합니다.
---

## 도구 및 프레임워크
### 의사결정 일지 템플릿
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

### 편견 체크리스트
중요한 결정을 내리기 전에:
- [ ] 반증적인 증거를 찾았습니까?
- [ ] 초기 정보에 기반을 두고 있습니까?
- [ ] 매몰비용이 우리에게 영향을 미치나요?
- [ ] 우리는 우리의 추정치를 과신하고 있습니까?
- [ ] 기본 요율을 고려했습니까?
- [ ] 가용성/최근성 편향에 빠지고 있습니까?
- [ ] 처음부터 다시 시작해도 같은 선택을 하게 될까요?
### 레드팀 훈련
제안된 결정에 반대할 사람을 지정하십시오.
- 그들의 역할은 결함을 찾는 것입니다.
- 대안적인 관점을 제시해야 합니다.
- 비판에 건설적으로 대응하는 팀 실천
- 제기된 문제 및 해결된 문제를 문서화합니다.
이는 확증 편향과 집단 사고에 대응합니다.