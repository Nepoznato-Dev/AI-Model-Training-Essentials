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
# Arquitetura local de IA
Um guia prático para executar grandes modelos de linguagem inteiramente no dispositivo — considerações de hardware, mecanismos de inferência, otimização de memória e design de sistema para implantação na borda.
---

## Por que executar a IA localmente?
- **Privacidade**: Nenhum dado sai do dispositivo.
- **Custo**: Sem taxas de API por token.
- **Latência**: inferência previsível e sem rede.
- **Disponibilidade offline**: Funciona sem internet.
- **Controle**: Controle total sobre a versão do modelo, personalização e ajuste fino.
---

## Requisitos de hardware
### Memória GPU (VRAM)
O recurso mais crítico. Tamanho do modelo na memória ≈ **parâmetros × bytes por parâmetro**.
| Precisão | Bytes por parâmetro | Modelo 3.8B | Modelo 7B | Modelo 13B | Modelo 70B |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32 | 4 | ~15GB | ~28 GB | ~52GB | ~280GB |
| FP16 | 2 | ~7,6 GB | ~14GB | ~26 GB | ~140 GB |
| INT8 (8 bits) | 1 | ~3,8GB | ~7 GB | ~13 GB | ~70GB |
| INT4 (4 bits) | 0,5 | ~1,9GB | ~3,5 GB | ~6,5GB | ~35GB |
**Diretrizes práticas:**
- 8GB VRAM → modelos de até 7B em 4 bits.
- 12GB VRAM → modelos de até 13B em 4 bits.
- 24 GB VRAM → modelos de até 70B em 4 bits (ou 13B em 8 bits).
- Apple Silicon (memória unificada) pode executar modelos de 70B em sistemas com mais de 64 GB.
### RAM (memória do sistema)
- Para inferência de CPU, você precisa de RAM de sistema suficiente para carregar o modelo (semelhante aos números VRAM).
- Para inferência de GPU, a RAM do sistema é importante para carregar o modelo na memória antes de descarregar para VRAM.
### Armazenamento
- Os pesos dos modelos quantizados ocupam alguns GB (por exemplo, 7B de 4 bits ≈ 4 GB no disco). Garanta pelo menos 20–50 GB livres para vários modelos.
### CPU
- Para processamento imediato (pré-preenchimento) e descarregamento de CPU, uma CPU moderna com vários núcleos ajuda.
- Os chips Apple série M têm excelente desempenho para LLMs devido à memória unificada e ao Neural Engine.
---

## Quantização
A quantização reduz a precisão numérica dos pesos, reduzindo drasticamente a memória e aumentando a velocidade com um pequeno custo de precisão.
### Formatos Populares
| Formato | Pedaços | Descrição | Uso típico |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | formato llama.cpp, otimizado para híbrido CPU/GPU | Melhor para inferência local |
| **GPTQ** | 4–8 | Somente GPU, eficiente em CUDA | Melhor para GPUs NVIDIA |
| **AWQ** | 4 | Com reconhecimento de ativação, somente GPU | Bom para inferência em lote em GPUs |
| **ONNX** | variável | Padronizado, multiplataforma | Serviço de produção |
### Escolhendo um nível de quantização
- **Q8_0** (8 bits): perda mínima de qualidade, tamanho maior.
- **Q6_K** (6 bits): boa qualidade, compactação decente.
- **Q5_K_M** (5 bits): ponto ideal comum.
- **Q4_K_M** (4 bits): menor qualidade aceitável para a maioria das tarefas.
- **IQ4_XS** / **IQ3_XS**: quantização aprimorada com melhor perplexidade em 4/3 bits.
**Regra geral:** Use Q4_K_M para um bom equilíbrio entre qualidade e tamanho. Se você tiver VRAM extra, use Q5 ou Q6.
---

## Mecanismos de inferência (locais)
### lhama.cpp
- Escrito em C++.
- Suporta formato GGUF.
- Otimizado para CPU e GPU (via CUDA, Metal, OpenCL).
- Muito rápido, especialmente na CPU.
- Linha de comando, modo de servidor e ligações Python.
**Exemplo de comando:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Envolve llama.cpp com uma CLI simples e API REST.
- Baixa modelos automaticamente e os gerencia.
- Ótimo para prototipagem e aplicativos de desktop.
- Suporta Modelfiles personalizados para prompts do sistema.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### Estúdio LM
- Aplicativo gráfico de desktop para Windows, macOS, Linux.
- Interface de download e bate-papo com um clique.
- Servidor local integrado com API compatível com OpenAI.
- Bom para usuários não técnicos e testes rápidos.
### Abraçando Transformadores de Rosto + bits e bytes
- A biblioteca Python padrão para modelos HF.
- Use`bitsandbytes`para quantização de 4 bits (`load_in_4bit=True`).
- Mais flexível para ajuste fino, mas mais lento que llama.cpp para inferência.
###ExLlamaV2
- Inferência de GPU muito rápida para GPTQ e AWQ.
- Melhor desempenho em GPUs NVIDIA.
- Suporta geração em lote.
### mlx (maçã)
- Estrutura da Apple para chips da série M.
- Altamente otimizado para Apple Silicon.
-API Python.
---

## Gerenciamento de memória
### Janela de contexto e cache KV
O cache KV armazena pares de valores-chave para cada camada e cada token no contexto. Ele cresce linearmente com o comprimento do contexto.
Custo de memória ≈ 2 × camadas × (cabeças KV × cabeça dim) × tokens × bytes por valor
Para um modelo de 32 camadas com cabeçotes de 8 KV e dim de 128 cabeçotes, cada token custa ~32 × 8 × 128 × 2 bytes = 65 KB por token. Para tokens de 128 mil, são aproximadamente 8 GB apenas para o cache.
### Estratégias de descarregamento
- **Descarregamento de camadas**: Coloque algumas camadas na GPU, outras na CPU. Mais rápido que CPU pura, menor necessidade de VRAM.
- **Streaming de tokens**: processe tokens de forma incremental, em vez de todos de uma vez.
### Cache de prompt
Reutilize caches KV em prompts semelhantes para evitar o recálculo da fase de pré-preenchimento. Algumas estruturas suportam isso (por exemplo, vLLM, llama.cpp com`--prompt-cache`).
### Arquivos mapeados na memória
Carregue pesos de modelos diretamente do disco sem carregá-los inteiramente na RAM (útil para modelos enormes em sistemas com memória limitada). llama.cpp usa mapeamento de memória por padrão.
---

## Arquiteturas de implantação
### Modo de dispositivo único
Um modelo funciona em uma máquina (laptop, smartphone, dispositivo de ponta). Usado para assistentes pessoais, aplicativos de anotações e preenchimento de código.
### Híbrida Edge-Cloud
O modelo local lida com consultas comuns; fallback para um modelo de nuvem para questões complexas. Isso oferece o melhor dos dois mundos: velocidade/privacidade para a maioria e capacidade para casos extremos.
### Inferência Distribuída (Multi-GPU)
Para modelos maiores, divida camadas em várias GPUs (paralelismo de tensor) ou divida o contexto entre dispositivos (paralelismo de pipeline). Use llama.cpp com`-ngl`ou ExLlamaV2 com`--num-gpu-layers`.
### Implantação móvel
- **Android**: use llama.cpp por meio de ligações JNI ou kit de ML.
- **iOS**: Use llama.cpp por meio de ligações Swift ou mlx.
- **Web**: Use WebLLM (executado em WebGPU via tempo de execução ONNX) ou transformers.js.
---

## Otimização de desempenho
### Atenção Flash
Acelera o cálculo da atenção e reduz o uso de memória. Disponível em llama.cpp, ExLlamaV2 e bibliotecas de transformadores modernos.
### Inferência em lote
Processe vários prompts em uma única passagem de encaminhamento. Aumenta drasticamente o rendimento. Use`llama-batch`ou vLLM.
### Parada Antecipada / Orçamento de Token
Defina um orçamento máximo de tokens para evitar a geração ilimitada.
### Decodificação Especulativa
Use um modelo pequeno e rápido (rascunho) para prever tokens e, em seguida, verifique com o modelo grande em paralelo. Pode gerar aceleração de 2–3×.
---

## Guia Prático de Configuração
### 1. Instale o Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Puxe um modelo
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Execute com API
```bash
ollama serve
```

Em seguida, envie solicitações para`http://localhost:11434/api/generate`.
### 4. Integração Python
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternativa) Use llama.cpp diretamente
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Monitoramento e Observabilidade
- Rastreie a utilização da GPU (`nvidia-smi` no Linux, Activity Monitor no macOS).
- Acompanhe o uso de memória (RAM e VRAM).
- Rastreie tokens por segundo (taxa de transferência).
- Acompanhe o tempo até o primeiro token (latência).
- Use o registro integrado de llama.cpp ou Ollama.
---

## Limitações e compensações
- **Lacuna de qualidade**: Pequenos modelos locais (3,8B–7B) geralmente apresentam desempenho inferior aos grandes modelos de nuvem (GPT-4, Claude 3.5) em raciocínio complexo.
- **Corte de conhecimento**: o conhecimento do modelo é congelado no momento do treinamento; use RAG para injetar informações atuais.
- **Multilíngue**: modelos menores podem ter menos capacidade multilíngue.
- **Uso de ferramentas**: fluxos de trabalho de agente (chamada de função) podem ser menos confiáveis ​​em modelos pequenos.
Para muitas tarefas diárias (resumo, perguntas e respostas, conclusão de código, classificação), os modelos locais já são suficientes e estão melhorando rapidamente.