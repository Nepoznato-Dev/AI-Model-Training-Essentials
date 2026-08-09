---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
category: "AI and Machine Learning"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [model, optimization, deployment, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Otimização e implantação de modelo
Treinar um grande modelo de IA é impressionante, mas implantá-lo com eficiência é onde acontece a maior parte da engenharia. Um modelo que leva 10 segundos para responder ou requer oito GPUs A100 é inútil para a maioria das aplicações reais. A otimização de modelos é a arte e a ciência de tornar modelos menores, mais rápidos e mais baratos — sem sacrificar muita qualidade. Este arquivo cobre quantização, poda, destilação e as ferramentas práticas para colocar modelos em produção.
---

## Por que otimizar?
| Preocupação | Impacto |
|--------|--------|
| **Latência** | Os usuários esperam respostas em menos de 1 segundo; cada 100ms extras perde engajamento |
| **Custo** | A inferência de GPU é cara; um modelo 70B custa aproximadamente US$ 0,05-0,15 por 1 milhão de tokens em hardware em nuvem |
| **Memória** | Um modelo 7B no FP32 precisa de 28 GB de VRAM; a maioria das GPUs de consumo tem 8-24 GB |
| **Energia** | A operação de modelos grandes consome eletricidade significativa; assuntos para dispositivos móveis e edge |
| **Escala** | Atender milhões de usuários requer modelos que caibam no hardware disponível |
---

## Quantização
A quantização reduz a precisão dos pesos do modelo de ponto flutuante de 32 bits (FP32) para formatos menores como INT8, INT4 ou até inferiores.
### Formatos de precisão
| Formato | Bits por Peso | Memória para modelo 7B | Qualidade |
|--------|----------------|--------------------|---------|
| **FP32** | 32 | 28 GB | Linha de base (precisão total) |
| **FP16/BF16** | 16 | 14 GB | Quase idêntico ao FP32 |
| **INT8** | 8 | 7 GB | Perda de qualidade muito pequena |
| **INT4** | 4 | 3,5GB | Perda moderada de qualidade; ainda utilizável |
| **INT3/INT2** | 3-2 | 2,6-1,75 GB | Perda significativa de qualidade; fase de investigação |
### Métodos de Quantização
| Método | Quando isso acontece | Como funciona | Qualidade |
|--------|----------------|--------------|---------|
| **Quantização Pós-Treinamento (PTQ)** | Após a conclusão do treinamento | Calibre o modelo em um pequeno conjunto de dados; encontrar escalas ótimas | Bom para INT8; degrada em INT4 |
| **GPTQ** | Após o treinamento | Quantização INT4 compatível com GPU usando informações aproximadas de segunda ordem | Boa qualidade em INT4 |
| **AWQ** (quantização de peso com reconhecimento de ativação) | Após o treinamento | Proteger os pesos salientes com base nas magnitudes de ativação | Melhor que GPTQ em INT4 |
| **GGUF** (formato lhama.cpp) | Após o treinamento | Quantização amigável à CPU; precisão mista por camada | Otimizado para inferência de CPU |
| **Treinamento com reconhecimento de quantização (QAT)** | Durante o treinamento | Simule a quantização durante o treinamento para que o modelo aprenda a lidar | Melhor qualidade; requer reciclagem |
### Impacto prático
| Modelo | Tamanho FP16 | Tamanho INT4 | Aceleração | Perda de qualidade |
|-------|-----------|-----------|---------|-------------|
| **LAMA 7B** | 14 GB | 3,5GB | 2-4x | ~1-2% em benchmarks |
| **LAMA 70B** | 140 GB | 35 GB | 2-3x | ~2-3% em benchmarks |
---

## Poda
A poda remove pesos ou neurônios desnecessários de um modelo treinado.
| Tipo | Descrição | Vantagem | Desafio |
|------|------------|-----------|-----------|
| **Não estruturado** | Remover pesos individuais (definido como zero) | Taxas de compressão mais altas | Requer suporte de hardware esparso |
| **Estruturado** | Remova neurônios inteiros, cabeças de atenção ou camadas | Reduz diretamente o tamanho do modelo | Pode perder mais qualidade |
| **Com base na magnitude** | Remover pesos com menores valores absolutos | Simples; funciona bem | Pode perder pequenos pesos importantes |
| **Com base na importância** | Remover pesos com base na sua contribuição para a produção | Preservação de melhor qualidade | Mais caro para calcular |
### Pipeline de poda
| Etapa | Descrição |
|------|-------------|
| 1. Treinar | Treine o modelo completo normalmente |
| 2. Pontuação | Calcular pontuações de importância para cada peso/neurônio |
| 3. Podar | Remova os elementos menos importantes |
| 4. Ajuste fino | Treine novamente para recuperar a precisão perdida |
| 5. Repita | Iterar a poda e o ajuste fino para maior compactação |
---

## Destilação de Conhecimento
Treinar um modelo pequeno de “aluno” para imitar um modelo grande de “professor”.
| Componente | Função |
|-----------|------|
| **Professor** | Modelo grande e de alta qualidade |
| **Estudante** | Modelo pequeno que aprende com o professor |
| **Perda de destilação** | Aluno tenta igualar a distribuição de produção do professor (rótulos suaves) |
### Tipos de Destilação
| Tipo | Descrição | Exemplo |
|------|-------------|---------|
| **Baseado em Logit** | Aluno corresponde às probabilidades de produção do professor | Destilação original de Hinton |
| **Baseado em recursos** | Aluno corresponde às representações intermediárias do professor | FitNets |
| **Baseado em relacionamento** | Aluno compara relações entre amostras | RKD (Destilação de Conhecimento Relacional) |
| **Sem dados** | Não são necessários dados de treinamento originais; usar a geração do professor | DAFL, DeepInversion |
### Exemplos notáveis ​​de destilação
| Professor | Estudante | Resultado |
|--------|---------|--------|
| **GPT-4** | GPT-3.5-turbo (rumores) | Modelo menor com muita qualidade do GPT-4 |
| **BERT-Grande** | DestilBERT | 40% menor, 60% mais rápido, 97% do desempenho do BERT |
| **LAMA 70B** | LLaMA 7B (via destilação) | Modelo pequeno de código aberto aproximando-se da qualidade de modelo grande |
---

## Otimizações específicas do LLM
### Otimização de cache KV
Grandes modelos de linguagem armazenam em cache pares de valores-chave de tokens anteriores para evitar recomputação.
| Técnica | Descrição | Impacto |
|-----------|-------------|--------|
| **Atenção multiconsulta (MQA)** | Todas as cabeças de atenção compartilham um par KV | Reduz a memória; ligeira perda de qualidade |
| **Atenção de consulta agrupada (GQA)** | Grupos de cabeças compartilham pares KV | Equilíbrio entre MQA e atenção padrão |
| **Atenção à janela deslizante** | Atenda apenas aos últimos tokens W | Reduz o tamanho do cache KV para contextos longos |
### Decodificação Especulativa
| Etapa | Descrição |
|------|-------------|
| 1 | Um pequeno modelo de “rascunho” gera K tokens rapidamente |
| 2 | O modelo grande verifica todos os tokens K em uma passagem direta |
| 3 | Os tokens aceitos são mantidos; os rejeitados são regenerados |
Resultado: aceleração de 2 a 3x na geração sem perda de qualidade (o modelo grande sempre tem a palavra final).
### Atenção Flash
| Recurso | Descrição |
|--------|-------------|
| **Problema** | A atenção padrão requer memória O(n²) para a matriz de atenção |
| **Solução** | Calcule a atenção em blocos; nunca materialize a matriz completa na memória |
| **Resultado** | 2 a 4x mais rápido; permite janelas de contexto muito mais longas |
| **Variantes** | Flash Attention 2 (mais rápido), FlashDecoding (otimizado para inferência) |
---

## Servindo Estruturas
| Estrutura | Melhor para | Recurso principal |
|-----------|----------|------------|
| **vLLM** | Serviço LLM | PagedAtenção; dosagem contínua; alto rendimento |
| **TensorRT-LLM** | Inferência de GPU NVIDIA | Desempenho máximo em hardware NVIDIA |
| **lhama.cpp** | Inferência de CPU e GPU de consumidor | Executa modelos quantizados em laptops e telefones |
| **Olhama** | Modelo local em execução | Wrapper amigável em torno de llama.cpp |
| **Servidor de Inferência Triton** | Serviço multi-estrutura | Suporta TensorFlow, PyTorch, ONNX, TensorRT |
| **TorchServe** | Servindo modelo PyTorch | Integração nativa do PyTorch |
| **Tempo de execução ONNX** | Inferência entre plataformas | Execução otimizada em hardware |
| **BentoML** | Implantação de produção | Agnóstico em termos de estrutura; trata de embalar e servir |
---

## Padrões de implantação
| Padrão | Descrição | Quando usar |
|---------|-------------|-------------|
| **Implantação de borda** | Execute modelos em telefones, dispositivos IoT ou hardware incorporado | Baixa latência; off-line; privacidade |
| **API de nuvem** | Modelos de hospedagem em GPUs em nuvem; servir via API | Computação máxima; pagamento por uso |
| **Híbrido** | Modelo pequeno no dispositivo; grande modelo em nuvem | O melhor dos dois mundos |
| **Sem servidor** | Escalar para zero; pague apenas quando usado | Tráfego esporádico; sensível aos custos |
| **Inferência em lote** | Processar dados em massa de acordo com uma programação | Quando o tempo real não é necessário |
---

## Comparativo de mercado
| Métrica | O que mede |
|--------|-----------------|
| **Tokens por segundo** | Capacidade de geração (quanto maior, melhor) |
| **Tempo para o primeiro token (TTFT)** | Latência antes do aparecimento do primeiro token de saída |
| **Latência por solicitação** | Tempo total desde a entrada até à saída completa |
| **Uso de memória** | VRAM ou RAM consumida durante a inferência |
| **Rendimento** | Solicitações atendidas por segundo |
| **Custo por 1 milhão de tokens** | Custo em dólares para processar 1 milhão de tokens |
---

## Dicas Práticas
- **Comece com a quantização.** A quantização INT4 (AWQ ou GPTQ) oferece a melhor compensação entre qualidade e tamanho. A maioria dos modelos 7B roda confortavelmente em uma única GPU de consumidor no INT4.
- **Use vLLM para veiculação de LLM.** É a opção de código aberto mais rápida para inferência de LLM de alto rendimento.
- **Perfil antes de otimizar.** Meça onde o tempo é realmente gasto. Muitas vezes é a largura de banda da memória, e não a computação, que é o gargalo.
- **Corresponda o modelo à tarefa.** Um modelo 7B é adequado para a maioria das tarefas. Não use 70B quando 7B servir.
- **Considere a destilação.** Se você precisar de um modelo pequeno e rápido para produção, destile a partir de um modelo maior em vez de treinar do zero.
- **Monitore continuamente.** O desempenho do modelo pode diminuir com o tempo, à medida que as distribuições de dados mudam. Rastreie métricas de latência, rendimento e qualidade.
---

## Resumo
A otimização do modelo é a ponte entre pesquisa e produção. A quantização reduz os modelos em 4 a 8x com perda mínima de qualidade. A poda remove o peso morto. A destilação transfere conhecimento de modelos grandes para modelos pequenos. Os truques de Flash Attention e KV-cache tornam a inferência mais rápida. Juntas, essas técnicas transformam um modelo que requer um data center em um modelo que funciona em um laptop ou telefone. O campo está avançando rapidamente – o que exigiu oito A100 no ano passado roda em uma GPU de consumo hoje.