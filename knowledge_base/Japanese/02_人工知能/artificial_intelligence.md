<!-- 
This file was automatically translated from English to Japanese.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 人工知能

## 人工知能とは何か

人工知能（AI）とは、人間の知能を機械上で模倣し、思考・学習・問題解決を行えるようにする技術を指します。AI システムは、音声認識、意思決定、言語翻訳、画像内の物体認識など、通常は人間の知能を必要とする作業を実行できます。AI という用語は 1956 年、Dartmouth Conference において John McCarthy によって提唱され、これが AI 分野の出発点と広く見なされています。

現代の AI は大きく、特定の課題に特化した Narrow AI（Weak AI）と、理論上あらゆる領域で人間に匹敵またはそれ以上の認知能力を持つ Artificial General Intelligence（AGI）に分けられます。現在実用化されている AI はすべて Narrow AI です。

## AI の歴史

AI の歴史はおよそ 80 年近くにわたります。理論的な基盤を築いた人物の一人が Alan Turing で、1950 年の論文 "Computing Machinery and Intelligence" では Turing Test を提案しました。これは、機械が人間と区別できない知的振る舞いを示せるかを測る考え方です。1956 年の Dartmouth Conference によって、AI は正式に学術分野として成立しました。

1950〜1970 年代には、ELIZA のような初期チャットボットや、AI 向けに設計されたプログラミング言語 LISP など、楽観的な初期プログラムが登場しました。一方で 1970 年代から 1980 年代には、期待に成果が追いつかず、資金や関心が低下した「AI 冬の時代」もありました。1980 年代には、人間の専門知識をルールとして表現する expert system の登場で再び注目が高まりました。2000 年代にはインターネットと大規模データセットを背景に機械学習が大きく進展し、2010 年代には deep learning が computer vision、natural language processing（NLP）、reinforcement learning を大きく変革しました。

## 機械学習

機械学習（ML）は AI の一分野であり、明示的にプログラムしなくてもデータから学べるようにする技術です。主な分類は次のとおりです。

**Supervised Learning**: ラベル付きの入力と出力の組で学習する方式です。例として、スパム検知や画像分類があります。代表的なアルゴリズムには linear regression、decision tree、support vector machine、neural network があります。

**Unsupervised Learning**: ラベルのないデータからパターンを見つける方式です。例として、顧客セグメンテーションや異常検知があります。代表的な手法には k-means clustering や principal component analysis（PCA）があります。

**Reinforcement Learning**: エージェントが環境と相互作用し、報酬や罰を受け取りながら学ぶ方式です。ゲーム AI（AlphaGo、AlphaZero）、ロボティクス、推薦システムなどで使われます。

**Semi-Supervised Learning と Self-Supervised Learning**: 少量のラベル付きデータと大量のラベルなしデータを組み合わせる、あるいは自己生成した教師信号で学ぶ方式です。GPT 系モデルの事前学習は self-supervised な手法です。

## 深層学習

深層学習は機械学習の一分野で、多数の層を持つ人工ニューラルネットワークを利用します。脳の神経構造に着想を得たこれらのネットワークは、データの階層的表現を学習します。深層学習は次のような分野を支えています。

- **Computer Vision**: 画像認識、物体検出、医用画像解析
- **Natural Language Processing**: 機械翻訳、感情分析、質問応答
- **Speech Recognition**: Siri、Alexa、Google Assistant などの音声認識
- **Generative AI**: 画像生成（DALL-E、Stable Diffusion）、文章生成（GPT）

代表的なアーキテクチャには、画像向けの convolutional neural network（CNN）、系列データ向けの recurrent neural network（RNN）や LSTM、言語向けの transformer、生成向けの generative adversarial network（GAN）があります。

## Large Language Models（LLMs）

Large Language Models（LLMs）は、膨大なテキストデータで学習され、人間の言語を理解・生成する AI システムです。基盤となるのは、2017 年の論文 "Attention is All You Need" で Vaswani らが提案した Transformer アーキテクチャです。LLM は系列中の次の token を予測することで、自然な文章生成、質問応答、コード生成、推論などを行います。

代表的な LLM には次のようなものがあります。
- **GPT series**（OpenAI）: GPT-3、GPT-4 以降のモデル群。対話やコード生成で広く利用される。
- **Claude**（Anthropic）: 安全性と有用性を重視したモデル。
- **Gemini**（Google DeepMind）: テキスト、画像、コードを統合するマルチモーダルモデル。
- **LLaMA / Llama 3**（Meta）: 研究用途やローカル実行向けの open-weight モデル。
- **Mistral**（Mistral AI）: より大きな LLM に匹敵する効率的な open model。

LLM の学習は通常 2 段階で行われます。まず大規模テキストコーパスによる pre-training を行い、その後 supervised fine-tuning や reinforcement learning from human feedback（RLHF）で対話向けに調整します。context window はモデルが一度に扱える文脈量を表し、初期の GPT-3 の 4K tokens から、2024 年の高度なモデルでは 100 万 tokens 超まで拡大しています。

## AI 倫理と安全性

AI は、バイアス、プライバシー、雇用への影響、悪用リスクなど、重要な倫理的課題を伴います。学習データが歴史的な不平等を含んでいる場合、AI システムは差別的な出力を生み得ます。顔認識システムでは肌の色が濃い人への誤り率が高い例が報告されており、採用アルゴリズムが男性候補者を有利に扱った事例もあります。

AI safety は、AI システムが意図どおりに振る舞い、意図しない害を生まないようにするための分野です。主な関心事は次のとおりです。
- **Alignment**: AI の目標が人間の価値観と一致していること
- **Interpretability / Explainability**: AI がなぜその判断をしたのか理解できること（医療、法律、金融で特に重要）
- **Misuse**: AI による deepfake、偽情報、サイバー攻撃
- **Existential risk**: 将来の AGI が人類の存続と整合しない目標を追うかもしれないという理論的懸念

AI safety に取り組む組織としては、OpenAI の Safety チーム、Anthropic、DeepMind の safety チーム、MIRI や ARC のような独立研究機関があります。

## 社会における AI

AI はほぼすべての産業を変えつつあります。

- **医療**: 医用画像からのがん診断支援、患者転帰予測、創薬の加速（AlphaFold はタンパク質構造予測で大きな成果を出した）、治療計画の個別最適化
- **金融**: 不正検知、アルゴリズム取引、信用スコアリング、robo-advisor などに ML が使われる
- **Transportation**: 自動運転車は computer vision、lidar、reinforcement learning を活用する。Tesla Autopilot、Waymo、Cruise が代表例
- **Education**: 個々の学習速度や学習スタイルに合わせて教材を調整する個別学習プラットフォーム
- **Creative fields**: 音楽、アート、文章の生成。Midjourney、DALL-E、GitHub Copilot などが制作ワークフローを変えている
- **Cybersecurity**: 異常検知や脅威分析を強化する一方、攻撃側にも防御側にも利用される

## ロボティクスと Embodied AI

ロボティクスは AI と物理的な機械を組み合わせる分野です。現代のロボットは、知覚（camera、lidar）、計画、制御によって移動や操作を行います。Boston Dynamics の Atlas は高度な二足歩行の例として知られています。ABB や FANUC の産業ロボットは製造業を自動化し、Roomba のような家庭用ロボットや da Vinci System のような手術支援ロボットも広く使われています。Embodied AI は、エージェントが環境との相互作用を通じて身体的スキルを学ぶ研究領域であり、シミュレーションと現実世界の橋渡しを目指します。

## 現在の AI トレンド（2020 年代）

- **Multimodal AI**: テキスト、画像、音声、動画を統合的に扱うシステム（GPT-4V、Gemini）
- **Agents と agentic AI**: ツール使用、ウェブ閲覧、コード生成、多段階行動ができる LLM（OpenAI Operator、Anthropic Computer Use）
- **Open-weight models**: Meta の LLaMA により、研究者が大規模モデルへアクセスしやすくなった
- **On-device AI**: クラウド接続なしで、スマートフォンやノート PC 上で AI モデルを動かす流れ（Apple Intelligence、Qualcomm NPU）
- **AI regulation**: EU AI Act（2024）は、リスク水準ごとに AI システムを分類する包括的な AI 法規制として注目されている
