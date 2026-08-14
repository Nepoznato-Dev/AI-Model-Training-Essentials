---
# Metadata
title: "Computer Vision Fundamentals"
description: "CNNs, object detection, segmentation, transfer learning"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [computer, vision, ai-and-machine-learning]
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
# Fundamentos da Visão Computacional
A visão computacional dá às máquinas a capacidade de interpretar e compreender informações visuais do mundo – imagens, vídeos e dados 3D. Ele potencializa tudo, desde reconhecimento facial em seu telefone até carros autônomos, análise de imagens médicas e controle de qualidade industrial. Este arquivo cobre os principais conceitos, arquiteturas e técnicas.
---

## Como os computadores veem as imagens
### Pixels e Canais
Uma imagem digital é uma grade de pixels. Cada pixel possui valores numéricos que representam a intensidade da cor.
| Tipo de imagem | Canais | Valores por Pixel | Exemplo |
|-----------|----------|-----------------|---------|
| **Tons de cinza** | 1 | 0 (preto) a 255 (branco) | Radiografias médicas |
| **RGB** | 3 | Vermelho, Verde, Azul (cada 0–255) | Fotos coloridas padrão |
| **RGBA** | 4 | RGB + Alfa (transparência) | Imagens com fundos transparentes |
| **HSV** | 3 | Matiz, Saturação, Valor | Segmentação baseada em cores |
Uma imagem RGB de 1920×1080 é um tensor de forma`(1080, 1920, 3)`– são 6,2 milhões de pixels, cada um com 3 valores.
### Principais operações
| Operação | Descrição |
|-----------|------------|
| **Redimensionando** | Dimensionar imagem para dimensões alvo (interpolação bilinear, vizinho mais próximo) |
| **Recorte** | Extraia uma região de interesse |
| **Normalização** | Dimensione os valores de pixel para [0,1] ou [-1,1] para redes neurais |
| **Aumento** | Expandir artificialmente os dados de treinamento (rotação, inversão, instabilidade de cor, corte) |
---

## Convolução: a operação central
Uma convolução desliza um pequeno filtro (kernel) pela imagem, calculando produtos escalares em cada posição. É assim que as CNNs detectam bordas, texturas e padrões.
### Parâmetros de Convolução
| Parâmetro | Efeito |
|-----------|--------|
| **Tamanho do kernel** | 3×3, 5×5, 7×7 – kernels maiores capturam padrões maiores |
| **Passo** | Tamanho do passo; stride=2 reduz pela metade as dimensões de saída |
| **Preenchimento** | Adicione zeros ao redor da borda para preservar as dimensões espaciais |
| **Número de filtros** | Cada filtro aprende um recurso diferente (borda, textura, padrão de cor) |
### O que as convoluções aprendem
| Profundidade da camada | Recursos detectados |
|------------|------------------|
| **Camadas iniciais** | Bordas, cantos, texturas simples |
| **Camadas intermediárias** | Formas, partes de objetos (rodas, olhos, folhas) |
| **Camadas profundas** | Conceitos de alto nível (rostos, carros, animais) |
---

## Arquiteturas CNN
A evolução das arquiteturas CNN conta a história do progresso do aprendizado profundo na visão computacional.
| Arquitetura | Ano | Inovação Chave |
|------------|------|---------------|
| **LeNet-5** | 1998 | Primeira CNN prática; reconhecimento de dígitos |
| **AlexNet** | 2012 | Deep CNN vence ImageNet; ReLU, abandono, treinamento de GPU |
| **VGGNet** | 2014 | Convoluções 3×3 empilhadas (mais profundas = melhor) |
| **GoogLeNet (Início)** | 2014 | Módulos de iniciação (tamanhos de filtros paralelos); 22 camadas |
| **ResNet** | 2015 | Pular conexões (aprendizagem residual); Mais de 152 camadas |
| **EficienteNet** | 2019 | Escala composta (profundidade + largura + resolução) |
| **ConvNeXt** | 2022 | ResNet modernizado; competitivo com Transformadores |
### Por que o ResNet mudou tudo
Antes do ResNet, treinar redes muito profundas era quase impossível devido ao problema do gradiente evanescente. A ResNet introduziu **conexões ignoradas** (também chamadas de conexões residuais): a entrada de uma camada é adicionada à sua saída.
```
output = F(x) + x    # Skip connection
```

Essa ideia simples permitiu que redes com mais de 152 camadas fossem treinadas de forma eficaz e agora é padrão em praticamente todas as arquiteturas profundas.
---

## Principais tarefas de visão
### Classificação de imagens
Atribua um rótulo a uma imagem inteira.
| Modelo | Abordagem |
|-------|----------|
| CNNs (ResNet, EfficientNet) | Abordagem tradicional; excelente precisão |
| Transformadores de Visão (ViT) | Trate a imagem como uma sequência de patches; Codificador de transformador |
| Transferência de aprendizagem | Ajustar um modelo pré-treinado em seu conjunto de dados |
### Detecção de objetos
Encontre e classifique vários objetos em uma imagem, com caixas delimitadoras.
| Modelo | Tipo | Velocidade |
|-------|------|-------|
| **R-CNN** | Duas fases (proposta + classificação) | Lento |
| **R-CNN rápido** | Melhorado em dois estágios | Médio |
| **R-CNN mais rápido** | Região Proposta Rede + detector | Médio |
| **YOLO** (v1–v10) | Estágio único; prever caixas + classes em uma passagem | Muito rápido |
| **DETR** | Baseado em transformador; sem caixas de ancoragem | Médio |
**YOLO** (You Only Look Once) é a opção ideal para detecção em tempo real. **R-CNN mais rápido** é preferido quando a precisão é mais importante do que a velocidade.
### Segmentação de imagens
Classifique cada pixel de uma imagem.
| Tipo | Descrição | Caso de uso |
|------|-------------|----------|
| **Segmentação Semântica** | Cada pixel recebe um rótulo de classe | Condução autônoma (estrada, carro, pedestre) |
| **Segmentação de instâncias** | Cada ID de instância de pixel + objeto | Contagem de objetos, imagens médicas |
| **Segmentação Panóptica** | Semântica + instância combinada | Compreensão abrangente da cena |
Modelos principais: U-Net (imagem médica), Mask R-CNN (instância), DeepLab (semântica), Segment Anything Model (SAM — segmentação universal).
### Geração de imagem
| Abordagem | Descrição | Exemplos |
|----------|-------------|----------|
| **GANs** | Treinamento adversário gerador vs discriminador | EstiloGAN, CicloGAN |
| **VAE** | Aprenda distribuição latente; amostra para gerar | Autoencoders Variacionais |
| **Modelos de difusão** | Eliminar iterativamente o ruído aleatório | Difusão Estável, DALL-E, Midjourney |
Os modelos de difusão ultrapassaram amplamente os GANs em qualidade de geração de imagem.
---

## Transferir aprendizagem para visão
Treinar uma CNN do zero requer enormes dados e computação. O aprendizado por transferência permite começar com um modelo já treinado em milhões de imagens (ImageNet) e ajustá-lo para sua tarefa específica.
### Passos
1. **Escolha um modelo pré-treinado** (ResNet50, EfficientNet-B0, ViT).
2. **Substitua o cabeçalho de classificação** pelo seu próprio (correspondente ao seu número de turmas).
3. **Congelar camadas iniciais** (elas capturam recursos genéricos como bordas).
4. **Ajuste** seu conjunto de dados com uma baixa taxa de aprendizado.
5. **Descongele gradualmente** se precisar de mais adaptação.
Essa abordagem atinge rotineiramente alta precisão com apenas 1.000 a 10.000 imagens rotuladas.
---

## Aumento de dados
O aumento expande artificialmente seu conjunto de dados de treinamento aplicando transformações.
| Aumento | Efeito | Quando usar |
|------------|--------|-------------|
| **Corte aleatório** | Cortar em região aleatória | Quase sempre |
| **Inversão horizontal** | Imagem espelhada | Quando a orientação não importa |
| **Rotação** | Girar em ângulo aleatório | Quando os objetos aparecem em qualquer ângulo |
| **Jitter de cor** | Ajuste aleatoriamente brilho, contraste e saturação | Quando a iluminação varia |
| **Apagamento aleatório** | Mascarar regiões aleatórias | Melhora a robustez |
| **Mixup / CutMix** | Misture duas imagens e rótulos | Regularização |
Bibliotecas:`torchvision.transforms`,`albumentations`,`imgaug`,`tf.keras.preprocessing`.
---

## Ferramentas e Estruturas
| Ferramenta | Finalidade |
|------|---------|
| **CV aberto** | Operações clássicas de CV (filtragem, detecção de bordas, transformações geométricas) |
| **visão da tocha** | Modelos de visão, transformações e conjuntos de dados PyTorch |
| **tf.keras.applications** | Modelos pré-treinados em TensorFlow/Keras |
| **Ultralíticos (YOLOv8/v11)** | Detecção, segmentação e classificação de objetos |
| **Cara Abraçando (transformadores)** | Transformadores de visão, SegFormer, DETR |
| **Segmente qualquer coisa (SAM)** | Segmentação universal de imagens do Meta |
| **Albumentações** | Biblioteca de aumento de imagens rápida e flexível |
---

## Dicas Práticas
- **Comece com a aprendizagem por transferência.** O ajuste fino de um modelo pré-treinado supera o treinamento do zero em quase todos os casos.
- **Normalize suas entradas.** Combine a normalização que o modelo pré-treinado espera (geralmente média/padrão do ImageNet).
- **Use métricas apropriadas.** Precisão para conjuntos de dados balanceados; F1, mAP ou IoU para tarefas desequilibradas ou de detecção.
- **Visualize seus dados.** Veja imagens de amostra, verifique distribuições de classes, inspecione previsões de modelos.
- **Aumente com sabedoria.** Aplique apenas transformações que façam sentido para o seu domínio (não inverta imagens médicas verticalmente).
- **Monitore o overfitting.** Se a precisão do treinamento for alta, mas a validação for baixa, aumente o aumento ou adicione o abandono.