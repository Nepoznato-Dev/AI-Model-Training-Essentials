---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
subcategory: "Life Sciences"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to life_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [genetics, genomics, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Genética e Genômica
A genética é o estudo da hereditariedade – como as características são transmitidas dos pais aos filhos através do DNA. A genômica é o estudo de genomas inteiros: todos os genes, as regiões não codificantes, como eles interagem e como variam entre indivíduos e populações. A transição da genética para a genómica foi impulsionada pela tecnologia de sequenciação – passámos do estudo de um gene de cada vez para a leitura de genomas inteiros em horas, gerando dados que estão a transformar a medicina, a agricultura, a ciência forense e a nossa compreensão da evolução.
---

## Fundamentos do DNA
### Estrutura do DNA
| Componente | Descrição |
|-----------|------------|
| **Nucleotídeo** | Bloco de construção do DNA; consiste em um açúcar (desoxirribose), um grupo fosfato e uma base nitrogenada |
| **Bases** | Adenina (A), Timina (T), Guanina (G), Citosina (C) |
| **Emparelhamento de bases** | A emparelha com T (2 ligações de hidrogênio); G emparelha com C (3 ligações de hidrogênio) |
| **Dupla hélice** | Duas fitas antiparalelas (5' para 3' e 3' para 5'); torcido em uma hélice |
| **Cromossomo** | Uma única e longa molécula de DNA enrolada em proteínas histonas; os humanos têm 46 (23 pares) |
| **Genoma** | O conjunto completo de DNA de um organismo; genoma humano é de aproximadamente 3,2 bilhões de pares de bases |
### Dogma Central da Biologia Molecular
| Etapa | Processo | Localização | Produto |
|------|---------|----------|---------|
| **Replicação** | ADN → ADN | Núcleo | Duas moléculas de DNA idênticas |
| **Transcrição** | DNA → mRNA | Núcleo | RNA Mensageiro |
| **Tradução** | mRNA → proteína | Ribossomo (citoplasma) | Cadeia polipeptídica (proteína) |
---

## Expressão Gênica
### Como os genes são regulados
| Nível | Mecanismo | Exemplo |
|-------|-----------|--------|
| **Epigenética** | Metilação do DNA; modificação de histonas; remodelação da cromatina | Silenciamento de um cromossomo X em mulheres |
| **Transcricional** | Fatores de transcrição ligam promotores/intensificadores; ativar ou reprimir | Operon Lac em bactérias; genes responsivos a hormônios |
| **Pós-transcricional** | Emenda alternativa; Estabilidade do ARNm; microRNAs | Um gene → múltiplas variantes de proteínas |
| **Tradução** | Disponibilidade de ribossomos; regulação do fator de iniciação | Regulação do ferro via mRNA da ferritina |
| **Pós-tradução** | Modificação de proteínas (fosforilação, ubiquitinação); degradação | Controle do ciclo celular |
---

## Padrões de herança
### Genética Mendeliana
| Padrão | Descrição | Exemplo |
|---------|-------------|---------|
| **Autossômico dominante** | Uma cópia do alelo é suficiente | doença de Huntington; acondroplasia |
| **Autossômico recessivo** | São necessárias duas cópias | Fibrose cística; anemia falciforme |
| **Dominante ligado ao X** | Gene no cromossomo X; uma cópia é suficiente | Síndrome de Rett |
| **Recessivo ligado ao X** | Gene no cromossomo X; homens mais afetados | Hemofilia; daltonismo |
| **Codominância** | Ambos os alelos expressaram-se igualmente | Grupos sanguíneos ABO (A e B) |
| **Dominância incompleta** | Heterozigoto é intermediário | Flores rosa de pais vermelhos e brancos |
| **Poligênico** | Vários genes contribuem para uma característica | Altura; cor da pele; inteligência |
| **Pleiotropia** | Um gene afeta múltiplas características | Síndrome de Marfan (tecido conjuntivo, olhos, coração) |
---

## Genômica
### Tipos de Genômica
| Tipo | Foco | Aplicação |
|------|-------|------------|
| **Genômica estrutural** | Estrutura 3D de todas as proteínas de um genoma | Desenho de medicamentos; engenharia de proteínas |
| **Genômica funcional** | O que os genes fazem; interações genéticas; padrões de expressão | Compreendendo os mecanismos das doenças |
| **Genômica comparativa** | Comparando genomas entre espécies | Relações evolutivas; identificando regiões conservadas |
| **Metagenômica** | ADN proveniente de amostras ambientais (não cultivadas) | Estudos de microbioma; descobrindo novos organismos |
| **Farmacogenômica** | Como os genes afetam a resposta aos medicamentos | Medicina personalizada; dosagem de medicamentos |
| **Epigenômica** | Modificações epigenéticas em todo o genoma | Diagnóstico de câncer; biologia do desenvolvimento |
### Tecnologias de sequenciamento de DNA
| Geração | Tecnologia | Comprimento da leitura | Rendimento | Recurso principal |
|-----------|-----------|-------------|------------|-------------|
| **Primeira geração** | Sequenciamento Sanger | ~1.000 pb | Baixo | Precisão padrão ouro; usado para validação |
| **Segunda geração** | Illumina (Solexa) | 50–300 pb | Muito alto | Leituras curtas; plataforma dominante; baixo custo por base |
| **Segunda geração** | Torrente de íons | 200–400 pb | Alto | Baseado em semicondutores; sem óptica |
| **Terceira geração** | PacBio (SMRT) | 10.000–100.000 pb | Moderado | Leituras longas; resolve regiões repetitivas |
| **Terceira geração** | Nanopore Oxford | Até milhões de bp | Moderado a elevado | Leituras ultralongas; portátil (MinION); em tempo real |
---

## Variação Genética
### Tipos de variação
| Tipo | Descrição | Frequência |
|------|-------------|-----------|
| **SNP** (polimorfismo de nucleotídeo único) | Alteração de base única | Mais comum; ~1 em 1.000 bases |
| **Inserção/Exclusão (indel)** | Adição ou remoção de bases | Pode causar mutações de frameshift |
| **CNV** (Variação do Número de Cópias) | Segmentos duplicados ou eliminados (1 kb – vários Mb) | Contribui para doenças e evolução |
| **Variação estrutural** | Inversões; translocações; grandes rearranjos | Menos comum; pode ser patogênico |
| **Microssatélite (STR)** | Repetições curtas em tandem (2–6 pb repetidas) | Forense; testes de paternidade |
### GWAS (estudos de associação genômica ampla)
| Etapa | Descrição |
|------|-------------|
| **1. Coletar amostras** | Casos (com doença) e controles (sem) |
| **2. Genótipo** | Use matrizes SNP para genotipar centenas de milhares de variantes |
| **3. Teste estatístico** | Teste cada SNP quanto à associação com a característica |
| **4. Lote de Manhattan** | Visualize resultados em todos os cromossomos |
| **5. Replicação** | Confirmar resultados em amostras independentes |
---

## Edição de genes
### CRISPR-Cas9
| Componente | Função |
|-----------|----------|
| **RNA guia (gRNA)** | ~20 nucleotídeos; corresponde à sequência de DNA alvo |
| **Proteína Cas9** | Tesouras moleculares; corta DNA no local alvo |
| **Sequência PAM** | Motivo curto (NGG) próximo ao alvo; necessário para ligação Cas9 |
| **HDR** (Reparo Dirigido por Homologia) | Edição precisa usando um modelo de doador |
| **NHEJ** (junção final não homóloga) | Reparo sujeito a erros; cria inserções/exclusões (knockout) |
### Aplicativos de edição de genes
| Aplicação | Descrição |
|------------|------------|
| **Terapêutico** | Corrigir mutações causadoras de doenças (falciformes; talassemia beta) |
| **Agricultura** | Culturas resistentes a doenças; pecuária melhorada |
| **Pesquisa** | Crie modelos arrasadores; estuda função genética |
| **Impulsão genética** | Disseminar uma modificação genética através de uma população (por exemplo, mosquitos resistentes à malária) |
---

## Considerações Éticas
| Edição | Preocupação |
|-------|---------|
| **Privacidade genética** | Quem é o proprietário dos dados do seu genoma? Os empregadores ou seguradoras podem usá-lo? |
| **Edição genética em embriões** | Mudanças hereditárias; bebês projetados; efeitos não intencionais fora do alvo |
| **Discriminação genética** | GINA (EUA) protege contra alguma discriminação, mas tem lacunas |
| **Consentimento informado** | Dados genômicos revelam informações sobre parentes que não consentiram |
| **Armazenamento de dados** | Os genomas são grandes (~200 GB brutos); desafios de segurança e armazenamento de longo prazo |
| **Patrimônio** | A medicina genômica corre o risco de aumentar as disparidades de saúde se estiver disponível apenas para populações ricas |
---

## Resumo
A genética estuda como os genes individuais funcionam e são herdados. A genômica estuda genomas inteiros – todos os genes, suas interações e suas variações. O DNA é transcrito em RNA, que é traduzido em proteínas. A expressão gênica é regulada em vários níveis: epigenético, transcricional, pós-transcricional, translacional e pós-traducional. A herança segue padrões (dominante, recessivo, poligênico) que determinam como as características passam entre as gerações. Tecnologias modernas de sequenciamento (Illumina, PacBio, Nanopore) podem ler genomas inteiros de forma rápida e barata. CRISPR-Cas9 permite a edição genética precisa com potencial transformador na medicina e na agricultura. Os maiores desafios são éticos: quem controla os dados genómicos, como regular a edição genética em embriões e como garantir que a medicina genómica beneficie todos, não apenas os privilegiados.