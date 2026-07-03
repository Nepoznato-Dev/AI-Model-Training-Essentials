# Sistemas de Banco de Dados

## Fundamentos de Banco de Dados

### O que é um Banco de Dados?
Um banco de dados é uma coleção organizada de informações estruturadas armazenadas eletronicamente, projetada para recuperação, inserção, atualização e exclusão eficientes de dados.

### Sistemas de Gerenciamento de Banco de Dados (DBMS)
Software que interage com usuários finais, aplicações e o próprio banco de dados para capturar e analisar dados. Exemplos: MySQL, PostgreSQL, Oracle, MongoDB.

### Conceitos-Chave
- **Schema**: Estrutura/organização do banco de dados (tabelas, campos, relacionamentos)
- **Instância**: Dados reais armazenados em um determinado momento
- **Propriedades ACID**: Atomicidade, Consistência, Isolamento, Durabilidade
- **Teorema CAP**: Consistência, Disponibilidade, Tolerância a Partições (escolha 2)
- **Normalização**: Organização dos dados para reduzir redundância
- **Desnormalização**: Adição de redundância para melhorar o desempenho de leitura

## Bancos de Dados Relacionais (SQL)

### Conceitos Fundamentais
- **Tabelas**: Linhas (registros) e colunas (campos)
- **Chave Primária**: Identificador único para cada linha
- **Chave Estrangeira**: Referência à chave primária em outra tabela
- **Índices**: Estruturas de dados que melhoram a velocidade das consultas
- **Views**: Tabelas virtuais baseadas em resultados de consulta
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
- **LEFT JOIN**: Todas as linhas da tabela da esquerda, correspondências da direita
- **RIGHT JOIN**: Todas as linhas da tabela da direita, correspondências da esquerda
- **FULL OUTER JOIN**: Todas as linhas de ambas as tabelas
- **CROSS JOIN**: Produto cartesiano das duas tabelas
- **SELF JOIN**: Tabela unida a ela mesma

### Formas Normais
- **1NF**: Valores atômicos, sem grupos repetidos
- **2NF**: 1NF + sem dependências parciais (todos os atributos não chave dependem da chave primária completa)
- **3NF**: 2NF + sem dependências transitivas (atributos não chave não dependem de outros atributos não chave)
- **BCNF**: 3NF mais forte, todo determinante é uma chave candidata
- **4NF**: Sem dependências multivaloradas
- **5NF**: Sem dependências de junção

### SGBDs Populares
- **PostgreSQL**: Recursos avançados, extensível, compatível com ACID
- **MySQL**: Amplamente usado, leituras rápidas, aplicações web
- **Oracle**: Recursos corporativos, escalabilidade, caro
- **SQL Server**: Ecossistema Microsoft, ferramentas integradas
- **SQLite**: Embarcado, serverless, leve
- **MariaDB**: Fork do MySQL, open-source

## Bancos de Dados NoSQL

### Tipos de Bancos de Dados NoSQL

#### Armazenamentos de Documentos
- **Estrutura**: Documentos semelhantes a JSON (BSON)
- **Casos de Uso**: Gestão de conteúdo, catálogos, perfis de usuário
- **Exemplos**: MongoDB, CouchDB, DocumentDB
- **Exemplo de Consulta** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Armazenamentos Chave-Valor
- **Estrutura**: Pares simples de chave e valor
- **Casos de Uso**: Cache, sessões, carrinhos de compra
- **Exemplos**: Redis, DynamoDB, Riak
- **Características**: Rápidos, simples, com consultas limitadas

#### Bancos Column-Family
- **Estrutura**: Colunas agrupadas em famílias
- **Casos de Uso**: Big data, analytics, séries temporais
- **Exemplos**: Cassandra, HBase, ScyllaDB
- **Características**: Otimizados para escrita, distribuídos, escaláveis

#### Bancos de Dados em Grafo
- **Estrutura**: Nós, arestas, propriedades
- **Casos de Uso**: Redes sociais, detecção de fraude, recomendações
- **Exemplos**: Neo4j, Amazon Neptune, ArangoDB
- **Linguagem de Consulta**: Cypher (Neo4j), Gremlin

### Quando Usar NoSQL
- Schema flexível/em evolução
- Requisitos de escalabilidade horizontal
- Alta taxa de escrita
- Dados hierárquicos/aninhados
- Sistemas distribuídos
- Aplicações em tempo real

## Design de Banco de Dados

### Modelagem Entidade-Relacionamento
- **Entidades**: Objetos/conceitos (Cliente, Produto, Pedido)
- **Atributos**: Propriedades das entidades (nome, preço, data)
- **Relacionamentos**: Conexões entre entidades (um para um, um para muitos, muitos para muitos)
- **Cardinalidade**: Número de instâncias no relacionamento

### Padrões de Design de Schema
- **Single Table Inheritance**: Todos os tipos em uma tabela com discriminador de tipo
- **Class Table Inheritance**: Tabelas separadas para a base e para as subclasses
- **Concrete Table Inheritance**: Tabela separada para cada classe concreta
- **Junction Tables**: Resolvem relacionamentos muitos para muitos
- **Audit Tables**: Rastreiam alterações (created_at, updated_at, deleted_at)

### Estratégias de Indexação
- **B-Tree**: Padrão, consultas por intervalo, ordenação
- **Hash**: Buscas por correspondência exata
- **Bitmap**: Colunas com baixa cardinalidade (gênero, status)
- **Full-Text**: Capacidades de busca textual
- **Spatial**: Dados geográficos (GIS)
- **Composite**: Múltiplas colunas combinadas
- **Covering**: Inclui todas as colunas necessárias para a consulta

## Otimização de Consultas

### Planos de Execução
- Entender como o banco de dados executa consultas
- Identificar gargalos (full table scans, índices ausentes)
- Ferramentas: EXPLAIN, EXPLAIN ANALYZE

### Técnicas de Otimização
- **Uso de Índices**: Garantir que as consultas usem os índices adequados
- **Reescrita de Consultas**: Simplificar consultas complexas
- **Otimização de Joins**: Escolher os tipos e a ordem correta dos joins
- **Particionamento**: Dividir tabelas grandes (range, hash, list)
- **Views Materializadas**: Resultados de consulta pré-computados
- **Cache de Consultas**: Armazenar resultados frequentes de consultas

### Problemas Comuns de Desempenho
- **Problema de Consulta N+1**: Busca ineficiente de dados relacionados
- **Índices Ausentes**: Full table scans em tabelas grandes
- **Indexação Excessiva**: Escritas lentas devido a índices demais
- **Contenção de Locks**: Transações esperando por locks
- **Consultas Ineficientes**: SELECT *, joins desnecessários

## Transações e Concorrência

### Níveis de Isolamento de Transação
- **READ UNCOMMITTED**: Menor isolamento, leituras sujas possíveis
- **READ COMMITTED**: Apenas dados confirmados ficam visíveis (padrão na maioria dos DBs)
- **REPEATABLE READ**: A mesma consulta retorna os mesmos resultados dentro da transação
- **SERIALIZABLE**: Maior isolamento, transações executadas sequencialmente

### Controle de Concorrência
- **Pessimistic Locking**: Bloquear recursos antes do acesso
- **Optimistic Locking**: Verificar a versão antes do commit
- **MVCC (Multi-Version Concurrency Control)**: Manter múltiplas versões das linhas
- **Row-Level Locking**: Bloquear linhas específicas
- **Table-Level Locking**: Bloquear a tabela inteira

### Deadlocks
- Dependência circular em que as transações aguardam umas pelas outras
- Prevenção: Ordenação consistente de locks, timeouts, detecção de deadlock
- Resolução: Abortar uma transação

## Replicação e Escalabilidade

### Tipos de Replicação
- **Master-Slave**: Um primário, múltiplas réplicas de leitura
- **Master-Master**: Múltiplos primários, replicação bidirecional
- **Multi-Master**: N primários, requer resolução de conflitos
- **Chain Replication**: Replicação sequencial entre nós

### Abordagens de Escalabilidade
- **Escalabilidade Vertical**: Aumentar recursos do servidor (CPU, RAM, armazenamento)
- **Escalabilidade Horizontal**: Adicionar mais servidores (sharding, partitioning)
- **Read Replicas**: Descarregar o tráfego de leitura
- **Sharding**: Dividir dados entre servidores por chave/intervalo/hash
- **Federation**: Dividir por função/serviço

### Modelos de Consistência
- **Consistência Forte**: Todos os nós veem os mesmos dados ao mesmo tempo
- **Consistência Eventual**: Os nós convergem com o tempo
- **Consistência Causal**: Relações de causa e efeito preservadas
- **Read-Your-Writes**: O usuário vê suas próprias atualizações imediatamente

## Backup e Recuperação

### Estratégias de Backup
- **Full Backup**: Cópia completa do banco de dados
- **Incremental Backup**: Alterações desde o último backup
- **Differential Backup**: Alterações desde o último full backup
- **Point-in-Time Recovery**: Restaurar para um momento específico
- **Continuous Backup**: Replicação em tempo real para backup

### Procedimentos de Recuperação
- **RTO (Recovery Time Objective)**: Tempo máximo aceitável de indisponibilidade
- **RPO (Recovery Point Objective)**: Perda máxima aceitável de dados
- **Plano de Recuperação de Desastres**: Procedimentos documentados para falhas
- **Testes**: Exercícios regulares de recuperação

## Segurança

### Controle de Acesso
- **Autenticação**: Verificar a identidade do usuário
- **Autorização**: Conceder permissões (GRANT, REVOKE)
- **Roles**: Agrupar permissões para facilitar o gerenciamento
- **Princípio do Menor Privilégio**: Acesso mínimo necessário

### Proteção de Dados
- **Criptografia em Repouso**: Criptografar dados armazenados
- **Criptografia em Trânsito**: TLS/SSL para conexões
- **Mascaramento**: Ocultar dados sensíveis em ambientes não produtivos
- **Tokenização**: Substituir dados sensíveis por tokens

### Vulnerabilidades Comuns
- **SQL Injection**: SQL malicioso na entrada do usuário
- **Escalonamento de Privilégio**: Obter acesso não autorizado
- **Audit Logging**: Rastrear todas as atividades do banco de dados
- **Compliance**: Requisitos de GDPR, HIPAA e PCI-DSS

## Tecnologias Modernas de Banco de Dados

### Bancos de Dados em Nuvem
- **AWS**: RDS, Aurora, DynamoDB, Redshift
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: SQL Database, Cosmos DB, Synapse
- **Benefícios**: Serviço gerenciado, auto-scaling, backups incluídos

### Bancos de Dados NewSQL
- Combinam a consistência do SQL com a escalabilidade do NoSQL
- **Exemplos**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Recursos**: Distribuídos, transações ACID, escalabilidade horizontal

### Bancos de Dados de Séries Temporais
- Otimizados para dados com timestamp
- **Exemplos**: InfluxDB, TimescaleDB, Prometheus
- **Casos de Uso**: IoT, monitoramento, dados financeiros

### Bancos de Dados Vetoriais
- Armazenam e consultam vetores de embeddings
- **Exemplos**: Pinecone, Milvus, Weaviate, Qdrant
- **Casos de Uso**: Busca semântica, sistemas de recomendação, aplicações de AI

### Bancos de Dados Multi-Modelo
- Suportam múltiplos modelos de dados em um único sistema
- **Exemplos**: ArangoDB, OrientDB, Azure Cosmos DB
- **Benefício**: Flexibilidade sem múltiplos bancos de dados

## ORMs e Acesso a Dados

### Object-Relational Mapping
- **Objetivo**: Mapear tabelas do banco de dados para objetos de programação
- **ORMs Populares**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernate, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework

### Benefícios
- Abstração em relação ao SQL
- Segurança de tipos
- Gerenciamento de migrations
- APIs de construção de consultas

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
- Tempo de resposta de consultas
- Throughput (transações por segundo)
- Número de conexões
- Taxa de acerto de cache
- I/O de disco
- Tempo de espera por locks
- Atraso de replicação

### Tarefas de Manutenção
- **Vacuum/Analyze**: Atualizar estatísticas, recuperar espaço
- **Index Rebuilding**: Desfragmentar índices
- **Atualizações de Estatísticas**: Manter o otimizador de consultas informado
- **Rotação de Logs**: Gerenciar o tamanho dos arquivos de log
- **Planejamento de Capacidade**: Prever crescimento, planejar upgrades
