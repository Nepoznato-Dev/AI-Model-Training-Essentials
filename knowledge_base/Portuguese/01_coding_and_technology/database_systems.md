<!--
---
# Metadata
title: "Database Systems"
description: "SQL, NoSQL, design patterns, optimization"
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
tags: [database, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Sistemas de Banco de Dados
## Fundamentos de banco de dados
### O que é um banco de dados?
Um banco de dados é uma coleção organizada de informações estruturadas armazenadas eletronicamente, projetada para recuperação, inserção, atualização e exclusão eficiente de dados.
### Sistemas de gerenciamento de banco de dados (SGBD)
Software que interage com usuários finais, aplicativos e o próprio banco de dados para capturar e analisar dados. Exemplos: MySQL, PostgreSQL, Oracle, MongoDB.
### Conceitos-chave
- **Esquema**: Estrutura/organização do banco de dados (tabelas, campos, relacionamentos)
- **Instância**: dados reais armazenados em um determinado momento
- **Propriedades ACID**: Atomicidade, Consistência, Isolamento, Durabilidade
- **Teorema CAP**: Consistência, Disponibilidade, Tolerância de Partição (escolha 2)
- **Normalização**: organização de dados para reduzir redundância
- **Desnormalização**: adição de redundância para melhorar o desempenho de leitura
## Bancos de dados relacionais (SQL)
### Conceitos Básicos
- **Tabelas**: Linhas (registros) e colunas (campos)
- **Chave primária**: identificador exclusivo para cada linha
- **Chave Estrangeira**: Referência à chave primária em outra tabela
- **Índices**: estruturas de dados que melhoram a velocidade da consulta
- **Visualizações**: tabelas virtuais baseadas nos resultados da consulta
- **Procedimentos armazenados**: blocos de código SQL pré-compilados
- **Gatilhos**: ações automáticas em alterações de dados
### Operações SQL (CRUD)```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Junta-se
- **INNER JOIN**: Retorna linhas correspondentes de ambas as tabelas
- **LEFT JOIN**: Todas as linhas da tabela esquerda, correspondências da direita
- **RIGHT JOIN**: Todas as linhas da tabela direita, correspondências da esquerda
- **FULL OUTER JOIN**: Todas as linhas de ambas as tabelas
- **CROSS JOIN**: Produto cartesiano de ambas as tabelas
- **SELF JOIN**: Tabela unida a si mesma
### Formulários de Normalização
- **1NF**: Valores atômicos, sem grupos repetidos
- **2NF**: 1NF + sem dependências parciais (todos os atributos não-chave dependem de toda a chave primária)
- **3NF**: 2NF + sem dependências transitivas (atributos não-chave não dependem de outros atributos não-chave)
- **BCNF**: 3NF mais forte, todo determinante é uma chave candidata
- **4NF**: Sem dependências com vários valores
- **5NF**: Sem dependências de junção
### RDBMS populares
- **PostgreSQL**: recursos avançados, extensíveis, compatíveis com ACID
- **MySQL**: aplicações web amplamente utilizadas, leituras rápidas
- **Oracle**: recursos empresariais, escalabilidade, custos elevados
- **SQL Server**: ecossistema Microsoft, ferramentas integradas
- **SQLite**: incorporado, sem servidor, leve
- **MariaDB**: fork do MySQL, código aberto
## Bancos de dados NoSQL
### Tipos de bancos de dados NoSQL
#### Armazenamento de documentos
- **Estrutura**: documentos semelhantes a JSON (BSON)
- **Casos de uso**: gerenciamento de conteúdo, catálogos, perfis de usuário
- **Exemplos**: MongoDB, CouchDB, DocumentDB
- **Exemplo de consulta** (MongoDB):```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Armazenamentos de valor-chave
- **Estrutura**: pares simples de valores-chave
- **Casos de uso**: cache, sessões, carrinhos de compras
- **Exemplos**: Redis, DynamoDB, Riak
- **Características**: Consultas rápidas, simples e limitadas
#### Lojas Familiares de Coluna
- **Estrutura**: Colunas agrupadas em famílias
- **Casos de uso**: Big data, análises, séries temporais
- **Exemplos**: Cassandra, HBase, ScyllaDB
- **Características**: Otimizado para gravação, distribuído, escalonável
#### Bancos de dados gráficos
- **Estrutura**: Nós, arestas, propriedades
- **Casos de uso**: redes sociais, detecção de fraudes, recomendações
- **Exemplos**: Neo4j, Amazon Neptune, ArangoDB
- **Linguagem de consulta**: Cypher (Neo4j), Gremlin
### Quando usar NoSQL
- Esquema flexível/em evolução
- Requisitos de escala horizontal
- Alto rendimento de gravação
- Dados hierárquicos/aninhados
- Sistemas distribuídos
- Aplicações em tempo real
## Projeto de banco de dados
### Modelagem Entidade-Relacionamento
- **Entidades**: Objetos/conceitos (Cliente, Produto, Pedido)
- **Atributos**: Propriedades das entidades (nome, preço, data)
- **Relacionamentos**: conexões entre entidades (um para um, um para muitos, muitos para muitos)
- **Cardinalidade**: Número de instâncias em relacionamento
### Padrões de design de esquema
- **Herança de tabela única**: todos os tipos em uma tabela com discriminador de tipo
- **Herança de tabela de classe**: tabelas separadas para base e subclasses
- **Herança de tabela concreta**: tabela separada para cada classe concreta
- **Tabelas de junção**: resolva relacionamentos muitos para muitos
- **Tabelas de auditoria**: Rastreie alterações (created_at, Updated_at, Deleted_at)
### Estratégias de Indexação
- **B-Tree**: padrão, consultas de intervalo, classificação
- **Hash**: pesquisas de correspondência exata
- **Bitmap**: colunas de baixa cardinalidade (gênero, status)
- **Texto completo**: recursos de pesquisa de texto
- **Espacial**: dados geográficos (GIS)
- **Composto**: múltiplas colunas combinadas
- **Cobertura**: inclui todas as colunas necessárias para consulta
## Otimização de consulta
### Planos de Execução
- Compreender como o banco de dados executa consultas
- Identificação de gargalos (varreduras completas de tabelas, índices ausentes)
- Ferramentas: EXPLICAR, EXPLICAR ANALISAR
### Técnicas de otimização
- **Uso de índice**: certifique-se de que as consultas usem índices apropriados
- **Reescrita de consulta**: simplifique consultas complexas
- **Otimização de associação**: escolha os tipos e a ordem de associação corretos
- **Particionamento**: Divida tabelas grandes (intervalo, hash, lista)
- **Visualizações materializadas**: resultados de consulta pré-computados
- **Cache de consulta**: armazene resultados de consultas frequentes
### Problemas comuns de desempenho
- **Problema de consulta N+1**: busca ineficiente de dados relacionados
- **Índices ausentes**: verificações completas de tabelas em tabelas grandes
- **Excesso de indexação**: Gravações lentas devido a muitos índices
- **Contenção de bloqueio**: transações aguardando bloqueios
- **Consultas ineficientes**: SELECT *, junções desnecessárias
## Transações e simultaneidade
### Níveis de isolamento de transação
- **LEIA NÃO COMPROMETIDA**: Isolamento mais baixo, leituras sujas possíveis
- **READ COMMITTED**: Somente dados confirmados visíveis (padrão na maioria dos bancos de dados)
- **REPEATABLE READ**: A mesma consulta retorna os mesmos resultados na transação
- **SERIALIZÁVEL**: Maior isolamento, as transações são executadas sequencialmente
### Controle de simultaneidade
- **Bloqueio Pessimista**: Bloqueie recursos antes do acesso
- **Bloqueio Otimista**: Verifique a versão antes de confirmar
- **MVCC (controle de simultaneidade multiversão)**: mantém várias versões de linhas
- **Bloqueio em nível de linha**: bloqueia linhas específicas
- **Bloqueio em nível de tabela**: bloqueia a tabela inteira
### Impasses
- Dependência circular onde as transações esperam umas pelas outras
- Prevenção: ordenação consistente de bloqueios, tempos limite, detecção de deadlock
- Resolução: Abortar uma transação
## Replicação e dimensionamento
### Tipos de replicação
- **Master-Slave**: uma réplica primária de leitura múltipla
- **Master-Master**: múltiplas primárias, replicação bidirecional
- **Multi-Master**: N primárias, resolução de conflitos necessária
- **Replicação em cadeia**: replicação sequencial através de nós
### Abordagens de dimensionamento
- **Escalonamento vertical**: Aumente os recursos do servidor (CPU, RAM, armazenamento)
- **Escalonamento horizontal**: adicione mais servidores (fragmentação, particionamento)
- **Réplicas de leitura**: descarrega o tráfego de leitura
- **Fragmentação**: Divida os dados entre servidores por chave/intervalo/hash
- **Federação**: Divisão por função/serviço
### Modelos de Consistência
- **Forte consistência**: todos os nós veem os mesmos dados ao mesmo tempo
- **Consistência eventual**: os nós convergem ao longo do tempo
- **Consistência causal**: relações de causa-efeito preservadas
- **Read-Your-Writes**: o usuário vê suas próprias atualizações imediatamente
## Backup e recuperação
### Estratégias de backup
- **Backup completo**: cópia completa do banco de dados
- **Backup incremental**: alterações desde o último backup
- **Backup Diferencial**: alterações desde o último backup completo
- **Recuperação pontual**: Restaure para um momento específico
- **Backup contínuo**: replicação em tempo real para backup
### Procedimentos de recuperação
- **RTO (objetivo de tempo de recuperação)**: tempo de inatividade máximo aceitável
- **RPO (objetivo de ponto de recuperação)**: perda máxima de dados aceitável
- **Plano de recuperação de desastres**: procedimentos documentados para falhas
- **Testes**: exercícios regulares de recuperação
## Segurança
### Controle de acesso
- **Autenticação**: verifique a identidade do usuário
- **Autorização**: conceder permissões (GRANT, REVOKE)
- **Funções**: permissões de grupo para facilitar o gerenciamento
- **Princípio do Menor Privilégio**: Acesso mínimo necessário
### Proteção de Dados
- **Criptografia em repouso**: criptografa dados armazenados
- **Criptografia em trânsito**: TLS/SSL para conexões
- **Mascaramento**: ocultar dados confidenciais em ambientes não produtivos
- **Tokenização**: substitua dados confidenciais por tokens
### Vulnerabilidades Comuns
- **Injeção de SQL**: SQL malicioso na entrada do usuário
- **Escalonamento de privilégios**: obtenção de acesso não autorizado
- **Registro de auditoria**: rastreie todas as atividades do banco de dados
- **Conformidade**: requisitos GDPR, HIPAA, PCI-DSS
## Tecnologias modernas de banco de dados
### Bancos de dados em nuvem
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: Banco de dados SQL, Cosmos DB, Synapse
- **Benefícios**: serviço gerenciado, escalonamento automático, backups incluídos
### Bancos de dados NewSQL
- Combine consistência SQL com escalabilidade NoSQL
- **Exemplos**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Recursos**: Transações ACID distribuídas, escalonamento horizontal
### Bancos de dados de série temporal
- Otimizado para dados com carimbo de data/hora
- **Exemplos**: InfluxDB, TimescaleDB, Prometheus
- **Casos de uso**: IoT, monitoramento, dados financeiros
### Bancos de dados de vetores
- Armazenar e consultar vetores de incorporação
- **Exemplos**: Pinha, Milvus, Weaviate, Qdrant
- **Casos de uso**: pesquisa semântica, sistemas de recomendação, aplicações de IA
### Bancos de dados multimodelos
- Suporta vários modelos de dados em um único sistema
- **Exemplos**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefício**: Flexibilidade sem vários bancos de dados
## ORMs e acesso a dados
### Mapeamento Objeto-Relacional
- **Objetivo**: Mapear tabelas de banco de dados para objetos de programação
- **ORMs populares**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  -Java: Hibernate, JPA
  -Rubi: ActiveRecord
  - .NET: Entidade Framework
### Benefícios
- Abstração de SQL
- Digite segurança
- Gestão de migração
- APIs de construção de consultas
### Desvantagens
- Sobrecarga de desempenho
- Consultas complexas mais difíceis de escrever
- Problemas de consulta N+1
- Curva de aprendizagem
## Administração de banco de dados
### Responsabilidades do DBA
- Instalação e configuração
- Ajuste de desempenho
- Backup e recuperação
- Gestão de segurança
- Planejamento de capacidade
- Monitoramento e alertas
- Gerenciamento de patches
### Métricas de monitoramento
- Tempo de resposta da consulta
- Taxa de transferência (transações por segundo)
- Contagem de conexões
- Proporção de acertos de cache
- E/S de disco
- Bloquear tempo de espera
- Atraso na replicação
### Tarefas de Manutenção
- **Aspirar/Analisar**: Atualizar estatísticas, recuperar espaço
- **Reconstrução de índice**: desfragmentar índices
- **Atualizações de estatísticas**: mantenha o otimizador de consultas informado
- **Rotação de log**: Gerenciar tamanhos de arquivos de log
- **Planejamento de capacidade**: preveja o crescimento, planeje atualizações