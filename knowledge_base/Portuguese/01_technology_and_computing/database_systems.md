# Sistemas de Banco de Dados

## Fundamentos de Banco de Dados

### O que é um Banco de Dados?
Um banco de dados é uma coleção organizada de informações estruturadas armazenadas eletronicamente, projetada para a recuperação, inserção, atualização e exclusão eficientes de dados.

### Sistemas de Gerenciamento de Banco de Dados (DBMS)
Software que interage com usuários finais, aplicações e com o próprio banco de dados para capturar e analisar dados. Exemplos: MySQL, PostgreSQL, Oracle, MongoDB.

### Conceitos-Chave
- **Schema**: Estrutura/organização do banco de dados (tabelas, campos, relacionamentos)
- **Instance**: Dados reais armazenados em um determinado momento
- **ACID Properties**: Atomicidade, Consistência, Isolamento, Durabilidade
- **CAP Theorem**: Consistência, Disponibilidade, Tolerância a Partições (escolha 2)
- **Normalization**: Organização dos dados para reduzir redundância
- **Denormalization**: Adição de redundância para melhorar o desempenho de leitura

## Bancos de Dados Relacionais (SQL)

### Conceitos Fundamentais
- **Tables**: Linhas (registros) e colunas (campos)
- **Primary Key**: Identificador único para cada linha
- **Foreign Key**: Referência à chave primária em outra tabela
- **Indexes**: Estruturas de dados que melhoram a velocidade das consultas
- **Views**: Tabelas virtuais baseadas em resultados de consultas
- **Stored Procedures**: Blocos de código SQL pré-compilados
- **Triggers**: Ações automáticas em alterações de dados

### Operações SQL (CRUD)
```sql
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

### Joins
- **INNER JOIN**: Retorna linhas correspondentes de ambas as tabelas
- **LEFT JOIN**: Todas as linhas da tabela da esquerda e correspondências da direita
- **RIGHT JOIN**: Todas as linhas da tabela da direita e correspondências da esquerda
- **FULL OUTER JOIN**: Todas as linhas de ambas as tabelas
- **CROSS JOIN**: Produto cartesiano de ambas as tabelas
- **SELF JOIN**: Tabela associada a ela mesma

### Formas Normais
- **1NF**: Valores atômicos, sem grupos repetidos
- **2NF**: 1NF + sem dependências parciais (todos os atributos não-chave dependem da chave primária inteira)
- **3NF**: 2NF + sem dependências transitivas (atributos não-chave não dependem de outros atributos não-chave)
- **BCNF**: 3NF mais forte, todo determinante é uma chave candidata
- **4NF**: Sem dependências multivaloradas
- **5NF**: Sem dependências de junção

### SGBDRs Populares
- **PostgreSQL**: Recursos avançados, extensível, compatível com ACID
- **MySQL**: Amplamente usado, leituras rápidas, aplicações web
- **Oracle**: Recursos corporativos, escalabilidade, custo elevado
- **SQL Server**: Ecossistema Microsoft, ferramentas integradas
- **SQLite**: Embarcado, sem servidor, leve
- **MariaDB**: Fork do MySQL, código aberto

## Bancos de Dados NoSQL

### Tipos de Bancos de Dados NoSQL

#### Bancos de Documentos
- **Structure**: Documentos semelhantes a JSON (BSON)
- **Use Cases**: Gerenciamento de conteúdo, catálogos, perfis de usuários
- **Examples**: MongoDB, CouchDB, DocumentDB
- **Query Example** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Bancos Chave-Valor
- **Structure**: Pares simples de chave-valor
- **Use Cases**: Cache, sessões, carrinhos de compras
- **Examples**: Redis, DynamoDB, Riak
- **Characteristics**: Rápidos, simples, consultas limitadas

#### Bancos Orientados a Famílias de Colunas
- **Structure**: Colunas agrupadas em famílias
- **Use Cases**: Big data, análises, séries temporais
- **Examples**: Cassandra, HBase, ScyllaDB
- **Characteristics**: Otimizados para escrita, distribuídos, escaláveis

#### Bancos de Grafos
- **Structure**: Nós, arestas, propriedades
- **Use Cases**: Redes sociais, detecção de fraudes, recomendações
- **Examples**: Neo4j, Amazon Neptune, ArangoDB
- **Query Language**: Cypher (Neo4j), Gremlin

### Quando Usar NoSQL
- Esquema flexível/em evolução
- Requisitos de escalabilidade horizontal
- Alta taxa de escrita
- Dados hierárquicos/aninhados
- Sistemas distribuídos
- Aplicações em tempo real

## Projeto de Banco de Dados

### Modelagem Entidade-Relacionamento
- **Entities**: Objetos/conceitos (Cliente, Produto, Pedido)
- **Attributes**: Propriedades das entidades (nome, preço, data)
- **Relationships**: Conexões entre entidades (um para um, um para muitos, muitos para muitos)
- **Cardinality**: Número de instâncias em um relacionamento

### Padrões de Projeto de Esquema
- **Single Table Inheritance**: Todos os tipos em uma tabela com discriminador de tipo
- **Class Table Inheritance**: Tabelas separadas para a base e para as subclasses
- **Concrete Table Inheritance**: Tabela separada para cada classe concreta
- **Junction Tables**: Resolvem relacionamentos muitos para muitos
- **Audit Tables**: Rastreiam alterações (created_at, updated_at, deleted_at)

### Estratégias de Indexação
- **B-Tree**: Padrão, consultas por intervalo, ordenação
- **Hash**: Buscas por correspondência exata
- **Bitmap**: Colunas de baixa cardinalidade (gênero, status)
- **Full-Text**: Recursos de busca textual
- **Spatial**: Dados geográficos (GIS)
- **Composite**: Combinação de múltiplas colunas
- **Covering**: Inclui todas as colunas necessárias para a consulta

## Otimização de Consultas

### Planos de Execução
- Entender como o banco de dados executa consultas
- Identificar gargalos (varreduras completas de tabela, índices ausentes)
- Ferramentas: EXPLAIN, EXPLAIN ANALYZE

### Técnicas de Otimização
- **Index Usage**: Garantir que as consultas usem índices apropriados
- **Query Rewriting**: Simplificar consultas complexas
- **Join Optimization**: Escolher os tipos e a ordem corretos dos joins
- **Partitioning**: Dividir tabelas grandes (range, hash, list)
- **Materialized Views**: Resultados de consultas pré-computados
- **Query Caching**: Armazenar resultados de consultas frequentes

### Problemas Comuns de Desempenho
- **N+1 Query Problem**: Busca ineficiente de dados relacionados
- **Missing Indexes**: Varreduras completas em tabelas grandes
- **Over-indexing**: Escritas lentas devido a índices em excesso
- **Lock Contention**: Transações aguardando locks
- **Inefficient Queries**: SELECT *, joins desnecessários

## Transações e Concorrência

### Níveis de Isolamento de Transações
- **READ UNCOMMITTED**: Menor isolamento, leituras sujas possíveis
- **READ COMMITTED**: Apenas dados confirmados ficam visíveis (padrão na maioria dos bancos)
- **REPEATABLE READ**: A mesma consulta retorna os mesmos resultados dentro da transação
- **SERIALIZABLE**: Maior isolamento, transações executadas sequencialmente

### Controle de Concorrência
- **Pessimistic Locking**: Bloqueia recursos antes do acesso
- **Optimistic Locking**: Verifica a versão antes do commit
- **MVCC (Multi-Version Concurrency Control)**: Mantém múltiplas versões das linhas
- **Row-Level Locking**: Bloqueia linhas específicas
- **Table-Level Locking**: Bloqueia a tabela inteira

### Deadlocks
- Dependência circular em que transações esperam umas pelas outras
- Prevenção: Ordenação consistente de locks, timeouts, detecção de deadlock
- Resolução: Abortamento de uma transação

## Replicação e Escalabilidade

### Tipos de Replicação
- **Master-Slave**: Um primário, múltiplas réplicas de leitura
- **Master-Master**: Múltiplos primários, replicação bidirecional
- **Multi-Master**: N primários, com necessidade de resolução de conflitos
- **Chain Replication**: Replicação sequencial entre nós

### Abordagens de Escalabilidade
- **Vertical Scaling**: Aumentar os recursos do servidor (CPU, RAM, armazenamento)
- **Horizontal Scaling**: Adicionar mais servidores (sharding, particionamento)
- **Read Replicas**: Descarregar tráfego de leitura
- **Sharding**: Dividir dados entre servidores por chave/faixa/hash
- **Federation**: Divisão por função/serviço

### Modelos de Consistência
- **Strong Consistency**: Todos os nós veem os mesmos dados ao mesmo tempo
- **Eventual Consistency**: Os nós convergem ao longo do tempo
- **Causal Consistency**: Relações de causa e efeito são preservadas
- **Read-Your-Writes**: O usuário vê imediatamente suas próprias atualizações

## Backup e Recuperação

### Estratégias de Backup
- **Full Backup**: Cópia completa do banco de dados
- **Incremental Backup**: Alterações desde o último backup
- **Differential Backup**: Alterações desde o último backup completo
- **Point-in-Time Recovery**: Restauração para um momento específico
- **Continuous Backup**: Replicação em tempo real para backup

### Procedimentos de Recuperação
- **RTO (Recovery Time Objective)**: Tempo máximo aceitável de indisponibilidade
- **RPO (Recovery Point Objective)**: Perda máxima aceitável de dados
- **Disaster Recovery Plan**: Procedimentos documentados para falhas
- **Testing**: Simulações regulares de recuperação

## Segurança

### Controle de Acesso
- **Authentication**: Verificação da identidade do usuário
- **Authorization**: Concessão de permissões (GRANT, REVOKE)
- **Roles**: Agrupamento de permissões para facilitar o gerenciamento
- **Principle of Least Privilege**: Mínimo acesso necessário

### Proteção de Dados
- **Encryption at Rest**: Criptografia dos dados armazenados
- **Encryption in Transit**: TLS/SSL para conexões
- **Masking**: Ocultação de dados sensíveis fora de produção
- **Tokenization**: Substituição de dados sensíveis por tokens

### Vulnerabilidades Comuns
- **SQL Injection**: SQL malicioso na entrada do usuário
- **Privilege Escalation**: Obtenção de acesso não autorizado
- **Audit Logging**: Rastreamento de todas as atividades do banco de dados
- **Compliance**: Requisitos de GDPR, HIPAA, PCI-DSS

## Tecnologias Modernas de Banco de Dados

### Bancos de Dados em Nuvem
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Benefits**: Serviço gerenciado, escalabilidade automática, backups incluídos

### Bancos de Dados NewSQL
- Combinam a consistência do SQL com a escalabilidade do NoSQL
- **Examples**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Features**: Distribuídos, transações ACID, escalabilidade horizontal

### Bancos de Dados de Séries Temporais
- Otimizados para dados com timestamp
- **Examples**: InfluxDB, TimescaleDB, Prometheus
- **Use Cases**: IoT, monitoramento, dados financeiros

### Bancos de Dados Vetoriais
- Armazenam e consultam vetores de embeddings
- **Examples**: Pinecone, Milvus, Weaviate, Qdrant
- **Use Cases**: Busca semântica, sistemas de recomendação, aplicações de IA

### Bancos de Dados Multimodelo
- Suportam múltiplos modelos de dados em um único sistema
- **Examples**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefit**: Flexibilidade sem necessidade de múltiplos bancos de dados

## ORMs e Acesso a Dados

### Mapeamento Objeto-Relacional
- **Purpose**: Mapear tabelas do banco de dados para objetos de programação
- **Popular ORMs**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefícios
- Abstração do SQL
- Segurança de tipos
- Gerenciamento de migrações
- APIs para construção de consultas

### Desvantagens
- Sobrecarga de desempenho
- Consultas complexas mais difíceis de escrever
- Problemas de consulta N+1
- Curva de aprendizado

## Administração de Banco de Dados

### Responsabilidades do DBA
- Instalação e configuração
- Ajuste de desempenho
- Backup e recuperação
- Gerenciamento de segurança
- Planejamento de capacidade
- Monitoramento e alertas
- Gerenciamento de patches

### Métricas de Monitoramento
- Tempo de resposta das consultas
- Throughput (transações por segundo)
- Número de conexões
- Taxa de acerto do cache
- I/O de disco
- Tempo de espera por locks
- Atraso de replicação

### Tarefas de Manutenção
- **Vacuum/Analyze**: Atualizar estatísticas, recuperar espaço
- **Index Rebuilding**: Desfragmentar índices
- **Statistics Updates**: Manter o otimizador de consultas informado
- **Log Rotation**: Gerenciar o tamanho dos arquivos de log
- **Capacity Planning**: Prever crescimento, planejar upgrades
