<!--
---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [blockchain, distributed, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Blockchain e sistemas distribuídos
Blockchain é um tipo específico de sistema distribuído – um livro-razão descentralizado e somente anexado, onde os registros (blocos) são vinculados por hashes criptográficos. Sistemas distribuídos são o campo mais amplo de fazer com que vários computadores trabalhem juntos como um só. Ambos os conceitos são importantes para a compreensão da infraestrutura moderna, desde criptomoedas até bancos de dados distribuídos e algoritmos de consenso que alimentam serviços globais.
---

## Fundamentos de Sistemas Distribuídos
### Por que sistemas distribuídos?
| Motivação | Descrição |
|-----------|------------|
| **Escalabilidade** | Adicionar mais máquinas para lidar com mais carga |
| **Tolerância a falhas** | Sistema continua funcionando mesmo que algumas máquinas falhem |
| **Distribuição geográfica** | Atender usuários de data centers próximos |
| **Especialização** | Máquinas diferentes realizam tarefas diferentes |
### Conceitos-chave
| Conceito | Descrição | Desafio |
|--------|-------------|-----------|
| **Consenso** | Fazer com que todos os nós concordem com um valor | Partições de rede; Falhas bizantinas |
| **Replicação** | Copiando dados em vários nós | Consistência vs disponibilidade |
| **Particionamento (fragmentação)** | Dividindo dados entre nós | Pontos quentes; consultas entre fragmentos |
| **Modelos de consistência** | Garantias sobre o que os diferentes leitores veem | A consistência forte é lenta; eventual consistência pode surpreender usuários |
| **Teorema CAP** | Você só pode ter 2 de: Consistência, Disponibilidade, Tolerância de partição | Na prática, é necessária tolerância à partição; escolha C ou A |
### O Teorema CAP
| Escolha | O que você ganha | Do que você desiste | Exemplo |
|--------|-------------|-------|---------|
| **CP** | Consistente + tolerante a partições | Alguns nós podem estar indisponíveis durante partições | HBase, MongoDB, Redis |
| **PA** | Disponível + tolerante a partição | As leituras podem retornar dados obsoletos | Cassandra, DynamoDB, CouchDB |
| **CA** | Consistente + disponível | Não é possível tolerar partições de rede | Bancos de dados de nó único (não verdadeiramente distribuídos) |
---

## Algoritmos de consenso
Como os nós distribuídos concordam com o estado do sistema?
| Algoritmo | Tipo | Tolerância a Falhas | Usado em |
|-----------|------|----------------|--------|
| **Paxos** | Tolerante a falhas de colisão | Até f falhas com nós 2f+1 | Google Gordinho; teoria fundamental |
| **Jangada** | Tolerante a falhas de colisão | Até f falhas com nós 2f+1 | etcd, Cônsul, TiKV |
| **PBFT** | Tolerante a falhas bizantinas | Até f falhas com nós 3f+1 | Tecido Hyperledger |
| **Comprovante de Trabalho** | Tolerante a falhas bizantinas | Depende do poder de hash | Bitcoin |
| **Prova de Participação** | Tolerante a falhas bizantinas | Depende da aposta | Ethereum 2.0, Cardano |
### Jangada (simplificada)
| Função | Responsabilidade |
|------|---------------|
| **Líder** | Lida com todas as solicitações do cliente; envia entradas de log para seguidores |
| **Seguidor** | Responde às solicitações do líder; votos nas eleições |
| **Candidato** | Solicita votos para se tornar líder |
1. Todos os nós começam como seguidores
2. Se um seguidor não receber notícias do líder durante o tempo limite da eleição, ele se tornará um candidato
3. Os candidatos solicitam votos; aquele com mais votos torna-se líder
4. O líder replica as entradas de log para os seguidores
5. Quando a maioria confirma, a inscrição está comprometida
---

##Blockchain
### Como funciona um Blockchain
| Componente | Descrição |
|-----------|------------|
| **Bloquear** | Um lote de transações + metadados + hash do bloco anterior |
| **Hash** | Impressão digital criptográfica do conteúdo do bloco |
| **Corrente** | Cada bloco faz referência ao hash do bloco anterior, criando uma cadeia imutável |
| **Consenso** | Os participantes da rede concordam sobre quais blocos adicionar |
| **Árvore Merkle** | Árvore de hashes que resume todas as transações em um bloco |
### Por que o Blockchain é difícil de adulterar
1. Cada bloco contém o hash do bloco anterior
2. Alterar qualquer transação altera o hash do bloco
3. O hash alterado quebra a cadeia – todos os blocos subsequentes tornam-se inválidos
4. Um invasor precisaria minerar novamente todos os blocos subsequentes E controlar >50% da rede
### Tipos de Blockchain
| Tipo | Acesso | Validador | Exemplo |
|------|--------|-----------|---------|
| **Público (sem permissão)** | Qualquer pessoa pode ler e escrever | Consenso aberto (PoW, PoS) | Bitcoin, Ethereum |
| **Privado (permitido)** | Acesso restrito | Validadores conhecidos | Hyperledger, Corda |
| **Consórcio** | Governado por um grupo de organizações | Validadores selecionados | R3 Corda para serviços bancários |
### Contratos Inteligentes
Código autoexecutável armazenado no blockchain que é executado quando condições predeterminadas são atendidas.
| Plataforma | Idioma | Recurso notável |
|----------|----------|-----------------|
| **Etéreo** | Solidez, Vyper | Maior ecossistema de contratos inteligentes |
| **Solana** | Ferrugem, C | Alto rendimento; taxas baixas |
| **Cardano** | Haskell (Plutus) | Revisado por pares; verificação formal |
| **Hiperledger** | Vá, Java, JavaScript | Empresa; autorizado |
---

## Criptomoeda
| Moeda | Consenso | Fornecimento | Uso primário |
|----------|-----------|--------|------------|
| **Bitcoins** | Prova de Trabalho | 21 milhões (limitado) | Reserva de valor; ouro digital |
| **Etéreo** | Prova de Participação | Sem limite rígido | Contratos inteligentes; DeFi; NFTs |
| **Solana** | Prova de Participação + Prova de História | Sem limite rígido | Transações de alta velocidade |
| **Cardano** | Prova de Participação (Ouroboros) | 45 mil milhões (limitado) | Abordagem acadêmica; sustentabilidade |
---

## Bancos de dados distribuídos
| Banco de dados | Arquitetura | Consistência | Melhor para |
|----------|------------|-------------|----------|
| **Cassandra** | Coluna larga; ponto a ponto | Ajustável (eventual para quórum) | Alto rendimento de gravação; série temporal |
| **MongoDB** | Documento; conjuntos de réplicas | Eventual (com opção de consistência causal) | Esquema flexível; rápido desenvolvimento |
| **BarataDB** | SQL Distribuído; Consenso de jangada | Forte | SQL Distribuído; implantação global |
| **TiDB** | SQL Distribuído; Jangada (via TiKV) | Forte | Compatível com MySQL; dimensionamento horizontal |
| **DynamoDB** | Valor-chave; gerenciado | Eventual (ou forte com leituras consistentes) | Sem servidor; Integrado à AWS |
| **Chave inglesa** | SQL Distribuído; Paxos | Forte | Google Nuvem; consistência global |
---

## Padrões de sistema distribuído
| Padrão | Descrição | Caso de uso |
|--------|-------------|----------|
| **Eleição de líder** | Escolha um nó para coordenar | Líder da jangada; Guardião do Zoológico |
| **Replicação** | Copie dados para redundância e escalonamento de leitura | Réplicas de banco de dados; CDN |
| **Fragmentação** | Particionar dados por intervalo de chaves ou hash | Bancos de dados em grande escala |
| **MapaReduce** | Divida a computação entre nós; resultados agregados | Grande processamento de dados |
| **Protocolo de fofoca** | Os nós compartilham periodicamente o estado com pares aleatórios | Associação ao cluster; detecção de falhas |
| **Commit de duas fases** | Coordenar transações em vários nós | Bancos de dados distribuídos |
| **Padrão Saga** | Série de transações locais com ações compensatórias | Transações de microsserviços |
| **Disjuntor** | Pare de ligar para um serviço com falha; falhar rapidamente | Resiliência; evitar falhas em cascata |
---

## Desafios em Sistemas Distribuídos
| Desafio | Descrição | Mitigação |
|-----------|-------------|------------|
| **Partições de rede** | Os nós não conseguem se comunicar | trade-off da PAC; tente novamente com espera |
| **Inclinação do relógio** | Nós diferentes têm relógios diferentes | Utilize relógios lógicos; NTP; evite depender do horário do relógio de parede |
| **Falhas Bizantinas** | Nós que mentem ou se comportam arbitrariamente | Consenso BFT; blockchain |
| **Cérebro dividido** | Dois nós pensam que são os líderes | Esgrima; decisões baseadas em quórum |
| **Falhas em cascata** | Uma falha desencadeia outras | Disjuntores; anteparas; degradação graciosa |
| **Consistência de dados** | Mantendo réplicas sincronizadas | Modelos de consistência; resolução de conflitos |
---

## Resumo
Os sistemas distribuídos são a forma como o software moderno é dimensionado, sobrevive a falhas e atende usuários globalmente. Algoritmos de consenso (Raft, Paxos) garantem que os nós concordem. Blockchains adicionam verificação criptográfica e descentralização para criar livros contábeis sem confiança. Bancos de dados distribuídos (Cassandra, CockroachDB, DynamoDB) lidam com dados em escala. O compromisso fundamental — captado pelo teorema CAP — é entre consistência e disponibilidade quando a rede não é fiável. Compreender esses conceitos é essencial para construir sistemas que funcionem em escala de internet.