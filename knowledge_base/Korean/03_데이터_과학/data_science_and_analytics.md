<!-- 
This file was automatically translated from English to Korean.
Source: data_science_and_analytics.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 데이터 과학과 분석

## 핵심 개념

### 데이터 과학이란?
데이터 과학은 구조화된 데이터와 비정형 데이터에서 지식과 인사이트를 추출하기 위해 과학적 방법, 프로세스, 알고리즘, 시스템을 활용하는 융합 분야입니다. 다음 요소가 결합됩니다:
- **통계**: 분석을 뒷받침하는 수학적 기반
- **컴퓨터 과학**: 프로그래밍, 알고리즘, 데이터 구조
- **도메인 전문성**: 해당 분야에 대한 지식
- **데이터 시각화**: 결과를 효과적으로 전달하는 방법

### 데이터 유형
- **정형 데이터**: 행과 열로 체계적으로 구성된 데이터(데이터베이스, 스프레드시트)
- **비정형 데이터**: 미리 정해진 형식이 없는 데이터(텍스트, 이미지, 오디오, 비디오)
- **반정형 데이터**: 어느 정도 구조는 있지만 엄격하지 않은 데이터(JSON, XML, HTML)
- **시계열 데이터**: 시간 순서에 따라 인덱싱된 연속적인 데이터 포인트
- **공간 데이터**: 지리 또는 위치 기반 정보
- **그래프 데이터**: 관계를 노드와 엣지로 표현한 데이터

### 데이터 과학 프로세스 (CRISP-DM)
1. **비즈니스 이해**: 목표와 요구사항을 정의합니다.
2. **데이터 이해**: 초기 데이터를 수집하고 탐색합니다.
3. **데이터 준비**: 데이터를 정제하고 변환하며 형식을 맞춥니다(전체 작업의 80%를 차지하는 경우가 많습니다).
4. **모델링**: 적절한 모델링 기법을 선택해 적용합니다.
5. **평가**: 목표 대비 모델 성능을 검토합니다.
6. **배포**: 모델을 운영 환경에 적용합니다.

## 통계 기초

### 기술 통계
- **중심 경향성 지표**: 평균, 중앙값, 최빈값
- **산포도 지표**: 범위, 분산, 표준편차, 사분위 범위
- **분포 형태**: 왜도(비대칭성), 첨도(꼬리의 두꺼움)
- **백분위수와 사분위수**: 분포 내 상대적 위치

### 추론 통계
- **가설 검정**: 귀무가설, 대립가설, p값
- **신뢰구간**: 모집단 모수를 포함할 가능성이 높은 값의 범위
- **통계적 유의성**: 결과가 우연히 발생했을 가능성의 정도
- **제1종 오류**: 참인 귀무가설을 기각하는 오류(false positive)
- **제2종 오류**: 거짓인 귀무가설을 기각하지 못하는 오류(false negative)
- **검정력**: 거짓인 귀무가설을 올바르게 기각할 확률

### 확률 분포
- **정규분포**: 종 모양 곡선으로, 평균 = 중앙값 = 최빈값입니다.
- **이항분포**: 성공/실패와 같은 이진 결과를 다룹니다.
- **포아송 분포**: 일정 구간에서 발생하는 이벤트 수를 모델링합니다.
- **균등분포**: 모든 결과가 동일한 확률을 가집니다.
- **지수분포**: 이벤트 사이의 시간을 나타냅니다.
- **t-분포**: 표본 수가 적고 모집단 분산을 모를 때 사용합니다.
- **카이제곱 분포**: 범주형 데이터 분석에 활용됩니다.

### 통계 검정
- **t-test**: 두 집단의 평균을 비교합니다.
- **ANOVA**: 여러 집단의 평균을 비교합니다.
- **Chi-Square Test**: 범주형 변수 간 독립성을 검정합니다.
- **Mann-Whitney U**: t-test의 비모수 대안입니다.
- **Pearson Correlation**: 연속형 변수 간 선형 관계를 측정합니다.
- **Spearman Correlation**: 순위 기반의 단조 관계를 측정합니다.
- **Kolmogorov-Smirnov**: 두 분포를 비교합니다.

## 데이터 수집과 저장

### 데이터 소스
- **데이터베이스**: SQL, NoSQL, 관계형 데이터베이스, 문서 저장소
- **APIs**: REST, GraphQL, 웹 스크래핑
- **파일**: CSV, JSON, XML, Parquet, Avro
- **스트리밍 데이터**: Kafka, Kinesis, 실시간 피드
- **설문과 실험**: 1차 데이터 수집 방식
- **공개 데이터셋**: 정부 데이터, Kaggle, 학술 저장소

### 데이터 웨어하우징
- **ETL**: Extract, Transform, Load 프로세스
- **데이터 레이크**: 원시 데이터를 원래 형식 그대로 저장하는 저장소
- **데이터 웨어하우스**: 분석용으로 구조화·가공된 데이터를 저장하는 시스템
- **데이터 마트**: 특정 부서를 위한 웨어하우스의 부분 집합
- **OLAP**: 다차원 질의를 수행하는 Online Analytical Processing
- **스타 스키마**: 차원 테이블이 사실 테이블을 둘러싼 구조
- **스노우플레이크 스키마**: 정규화된 차원 테이블 구조

### 데이터베이스 유형
- **관계형 (SQL)**: MySQL, PostgreSQL, Oracle, SQL Server
- **문서형**: MongoDB, CouchDB (JSON 유사 문서)
- **키-값**: Redis, DynamoDB (단순한 키-값 쌍)
- **컬럼 패밀리**: Cassandra, HBase (열 단위 처리에 최적화)
- **그래프형**: Neo4j, Amazon Neptune (노드와 관계 중심)
- **시계열**: InfluxDB, TimescaleDB (타임스탬프 기반 데이터)
- **벡터**: Pinecone, Milvus (ML용 임베딩 저장)

## 데이터 전처리

### 데이터 정제
- **결측값**: 대치(평균, 중앙값, 최빈값, 예측) 또는 삭제
- **이상치**: 탐지(IQR, Z-score)와 처리(상한/하한 설정, 변환)
- **중복값**: 식별과 제거
- **불일치**: 형식 표준화, 오탈자 수정
- **데이터 검증**: 제약 조건, 범위, 데이터 타입 확인

### 데이터 변환
- **정규화**: 값을 0-1 범위로 스케일링
- **표준화**: Z-score 정규화(평균=0, 표준편차=1)
- **인코딩**: One-hot, label, ordinal, target encoding
- **구간화**: 연속형 값을 범주로 묶기
- **로그 변환**: 왜도 완화
- **특성 스케일링**: 특성 간 비교 가능성 확보

### 특성 공학
- **특성 생성**: 기존 특성에서 새로운 특성 도출
- **특성 선택**: 가장 관련성이 높은 특성 선택
  - Filter methods (correlation, chi-square)
  - Wrapper methods (recursive feature elimination)
  - Embedded methods (LASSO, tree-based importance)
- **차원 축소**: PCA, t-SNE, UMAP
- **상호작용항**: 특성을 곱해 결합한 상호작용항 생성
- **다항 특성**: 고차항 생성

## 탐색적 데이터 분석 (EDA)

### EDA 기법
- **요약 통계**: 중심 경향, 퍼짐, 분포 형태 설명
- **단변량 분석**: 단일 변수의 분포 확인
- **이변량 분석**: 두 변수 간 관계 분석
- **다변량 분석**: 여러 변수 간 상호작용 분석
- **상관관계 분석**: 변수 간 관계와 다중공선성 파악
- **세분화**: 유사한 관측치끼리 그룹화

### 시각화 도구
- **히스토그램**: 단일 변수의 분포를 보여 줍니다.
- **박스 플롯**: 5수치 요약과 이상치 탐지에 유용합니다.
- **산점도**: 두 연속형 변수의 관계를 보여 줍니다.
- **히트맵**: 상관행렬이나 밀도를 시각화합니다.
- **막대그래프**: 범주형 비교에 적합합니다.
- **선 그래프**: 시간에 따른 추세를 보여 줍니다.
- **바이올린 플롯**: 분포 밀도와 box plot 요소를 함께 보여 줍니다.
- **페어 플롯**: 변수 쌍별 산점도를 한꺼번에 살펴봅니다.

### EDA를 위한 Python 라이브러리
- **pandas**: 데이터 조작과 분석
- **numpy**: 수치 계산
- **matplotlib**: 기본 시각화
- **seaborn**: 통계 시각화
- **plotly**: 인터랙티브 시각화
- **scipy**: 과학 계산과 통계

## 데이터 과학의 기계 학습

### 지도 학습
- **회귀**: 연속값 예측
  - Linear Regression
  - Polynomial Regression
  - Ridge/LASSO/Elastic Net
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **분류**: 범주형 레이블 예측
  - Logistic Regression
  - k-Nearest Neighbors
  - Naive Bayes
  - Support Vector Machines
  - Decision Trees
  - Random Forest
  - Gradient Boosting
  - 신경망

### 비지도 학습
- **군집화**: 유사한 관측치를 그룹화
  - k-Means
  - Hierarchical Clustering
  - DBSCAN (density-based)
  - Gaussian Mixture Models
  - Spectral Clustering
  
- **차원 축소**: 특성 수 축소
  - Principal Component Analysis (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencoders
  
- **연관 규칙**: 함께 자주 나타나는 항목 발견
  - Apriori Algorithm
  - FP-Growth

### 모델 평가
- **분류 지표**: 정확도, 정밀도, 재현율, F1-score, ROC-AUC, 혼동 행렬
- **회귀 지표**: MAE, MSE, RMSE, R², Adjusted R²
- **교차 검증**: k-fold, stratified, leave-one-out, time series split
- **하이퍼파라미터 튜닝**: grid search, random search, Bayesian optimization
- **학습 곡선**: 편향-분산 절충 관계 진단

## 빅데이터 기술

### 분산 컴퓨팅 프레임워크
- **Apache Hadoop**: MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark**: 메모리 내 처리 기반으로 Hadoop보다 빠릅니다.
  - Spark SQL: 구조화된 데이터 처리
  - Spark Streaming: 실시간 데이터 처리
  - MLlib: 기계 학습 라이브러리
  - GraphX: 그래프 처리
- **Apache Flink**: 낮은 지연 시간을 갖는 스트림 처리
- **Apache Beam**: 배치와 스트리밍을 아우르는 통합 모델

### 클라우드 플랫폼
- **AWS**: S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud**: BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure**: Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake**: 클라우드 데이터 웨어하우스

### 데이터 파이프라인 도구
- **Apache Airflow**: 워크플로 오케스트레이션
- **Luigi**: 데이터 파이프라인 관리(Spotify)
- **Prefect**: 현대적인 워크플로 오케스트레이션
- **Dagster**: 데이터 자산 중심의 오케스트레이터
- **dbt**: 웨어하우스 내 데이터 변환 도구

## 비즈니스 인텔리전스와 분석

### BI 도구
- **Tableau**: 시각적 분석 플랫폼
- **Power BI**: Microsoft의 비즈니스 분석 도구
- **Looker**: 데이터 탐색과 인사이트 도출 도구(Google)
- **Qlik Sense**: 연관형 분석 플랫폼
- **Metabase**: 오픈소스 BI 도구
- **Superset**: Apache 오픈소스 BI 도구

### 대시보드 설계 원칙
- **사용자 이해**: 사용자 요구에 맞게 설계합니다.
- **적절한 시각화 선택**: 데이터 유형에 맞는 차트를 사용합니다.
- **전략적인 색상 사용**: 중요한 정보를 눈에 띄게 강조합니다.
- **일관성 유지**: 형식과 축 스케일을 표준화합니다.
- **상호작용 지원**: 필터, 드릴다운, 툴팁을 제공합니다.
- **성능 최적화**: 빠른 로딩과 효율적인 쿼리를 보장합니다.
- **모바일 고려**: 반응형 디자인을 적용합니다.

### 핵심 성과 지표 (KPIs)
- **재무**: 매출, 이익률, ROI, 고객생애가치
- **고객**: 획득 비용, 이탈률, 만족도 점수, NPS
- **운영**: 효율성 지표, 사이클 타임, 결함률
- **마케팅**: 전환율, 클릭률, 기여도 분석
- **제품**: 활성 사용자, 참여도, 유지율, 기능 채택률

## 고급 분석

### 예측 분석
- **시계열 예측**: 시계열 예측 (ARIMA, Prophet, LSTM)
- **위험 모델링**: 신용평가, 사기 탐지, 보험 모델링
- **고객 분석**: 이탈 예측, 성향 모델링
- **수요 예측**: 재고 최적화, 공급망 예측
- **정비 예측**: 장비 고장 사전 예측

### 처방적 분석
- **Optimization**: 선형 계획법, 정수 계획법
- **Simulation**: Monte Carlo methods, discrete event simulation
- **Decision Analysis**: 의사결정 트리, 영향도 다이어그램
- **A/B 테스트**: 실험 설계, 통계적 유의성
- **Multi-Armed Bandits**: 적응형 실험

### 텍스트 분석 (NLP)
- **텍스트 전처리**: 토큰화, 어간 추출, 표제어 추출
- **감성 분석**: 긍정/부정/중립 분류
- **토픽 모델링**: LDA, NMF를 활용한 주제 발견
- **개체명 인식**: 사람, 장소, 조직 등의 개체 식별
- **텍스트 분류**: 스팸 탐지, 문서 분류
- **단어 임베딩**: Word2Vec, GloVe, BERT

## 데이터 윤리와 거버넌스

### 데이터 프라이버시
- **GDPR**: EU General Data Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **HIPAA**: Health Insurance Portability and Accountability Act (미국 의료)
- **Anonymization**: 개인 식별 정보를 제거하는 작업
- **Differential Privacy**: 개인을 보호하기 위해 노이즈를 추가하는 기법
- **동의 관리**: Opt-in/opt-out 메커니즘

### 데이터 품질
- **정확성**: 데이터가 올바른 정도
- **완전성**: 필요한 데이터가 모두 존재하는 정도
- **일관성**: 출처 간 모순이 없는 상태
- **적시성**: 필요한 시점에 데이터를 사용할 수 있는 상태
- **유효성**: 정의된 규칙을 충족하는 상태
- **고유성**: 중복이 없는 상태

### 편향과 공정성
- **표본추출 편향**: 대표성이 없는 데이터 수집
- **측정 편향**: 결함 있는 데이터 수집 도구로 인한 편향
- **알고리즘 편향**: 차별적인 모델 예측으로 이어지는 편향
- **공정성 지표**: demographic parity, equal opportunity
- **편향 완화**: 전처리, 학습 중 처리, 후처리 방식으로 편향 완화

### 데이터 거버넌스 프레임워크
- **데이터 스튜어드십**: 데이터 자산에 대한 책임 체계
- **메타데이터 관리**: 데이터를 설명하는 데이터 문서화
- **데이터 계보**: 데이터 흐름과 변환 이력 추적
- **접근 제어**: 역할 기반 권한 관리
- **감사 추적**: 데이터 접근과 변경 기록
- **규정 준수**: 규제 준수

## 데이터 과학 커리어 경로

### 역할
- **데이터 분석가**: 기술 통계, 대시보드, 리포팅 중심 역할
- **데이터 과학자**: 통계 모델링, 기계 학습, 고급 분석 수행
- **ML 엔지니어**: 운영 환경의 ML 시스템, 모델 배포, MLOps 담당
- **데이터 엔지니어**: 데이터 파이프라인, 인프라, ETL 프로세스 구축
- **분석 관리자**: 팀 리더십, 전략 수립, 이해관계자 관리
- **BI 개발자**: 대시보드와 보고서 개발
- **연구 과학자**: 새로운 알고리즘, 논문, 고급 연구 수행

### 역량 매트릭스
- **기술 역량**: Python/R, SQL, 통계, ML 프레임워크, 클라우드 플랫폼
- **분석 역량**: 문제 해결, 비판적 사고, 실험 설계
- **의사소통 역량**: 스토리텔링, 시각화, 발표 능력
- **비즈니스 역량**: 도메인 지식, 이해관계자 관리, ROI 분석
- **도구**: Git, Jupyter, Docker, CI/CD, 모델 버전 관리

## 새로운 트렌드

### 현재 동향
- **AutoML**: 기계 학습 파이프라인의 자동 생성
- **MLOps**: 기계 학습을 위한 DevOps 실천 방식
- **Feature Stores**: 중앙집중식 특성 관리 저장소
- **데이터 Mesh**: 분산형 데이터 아키텍처
- **LLMs와 생성형 AI**: 대규모 언어 모델과 콘텐츠 생성
- **Edge Analytics**: 데이터 발생 지점에서 수행하는 분석
- **Real-Time Analytics**: 스트리밍 데이터 분석
- **Augmented Analytics**: AI가 돕는 데이터 준비와 인사이트 도출

### 미래 방향
- **양자 기계 학습**: 양자 컴퓨팅을 활용한 ML
- **Federated Learning**: 분산된 데이터 전반에서 모델 학습
- **Causal Inference**: 상관관계를 넘어 인과관계를 파악하는 접근
- **Responsible AI**: 윤리, 설명 가능성, 투명성 중시
- **데이터 Fabric**: 환경 전반에 걸친 통합 데이터 관리
