---
# Metadata
title: "Database Design Skill"
description: "Create detailed data models with logical and physical design choices that ensure data integrity and optimize performance."
category: "Data Skills"
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
    date: "2026-01-15"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-01-15"
last_modified: "2026-01-15"
review_date: "2026-07-15"
reviewed_by: "Data Skills Team"
next_review: "2027-01-15"

# Classification
tags: [database-design, sql, data-modeling, normalization, performance]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Database Design Skill

## Overview

Database design is the process of creating a detailed data model of a database, including logical and physical design choices and physical storage parameters. A well-designed database ensures data integrity, minimizes redundancy, and optimizes query performance.

## When to Use

- Starting a new application that requires persistent data storage
- Migrating from legacy systems to modern databases
- Experiencing performance issues with existing database schemas
- Scaling applications to handle increased data volume
- Ensuring data consistency across multiple applications
- Planning data architecture for enterprise systems

## Core Competencies

### Schema Design
- Entity-Relationship (ER) modeling
- Table structure optimization
- Primary and foreign key strategies
- Index design and implementation
- Constraint definition (unique, check, not null)
- Partitioning and sharding strategies

### Normalization
- First Normal Form (1NF) - Eliminating repeating groups
- Second Normal Form (2NF) - Removing partial dependencies
- Third Normal Form (3NF) - Eliminating transitive dependencies
- Boyce-Codd Normal Form (BCNF) - Advanced normalization
- Denormalization for performance optimization
- Trade-offs between normalization and query performance

### Indexing Strategies
- B-tree indexes for range queries
- Hash indexes for equality lookups
- Composite indexes for multi-column queries
- Covering indexes to avoid table lookups
- Full-text indexes for text search
- Index maintenance and rebuilding

### Data Integrity
- Referential integrity constraints
- Check constraints for business rules
- Triggers for complex validation
- Transaction management
- ACID properties enforcement
- Data validation at application and database levels

## Design Principles

### CAP Theorem
Understanding the trade-offs between:
- **Consistency** - All nodes see the same data
- **Availability** - Every request receives a response
- **Partition Tolerance** - System continues despite network failures

### BASE Properties
For distributed systems:
- **Basically Available** - System guarantees availability
- **Soft State** - State may change over time
- **Eventual Consistency** - System becomes consistent over time

### Codd's Rules
Twelve rules for relational database management systems ensuring true relational behavior.

## Frameworks & Methods

### Database Design Process
1. **Requirements Analysis** - Gather data requirements from stakeholders
2. **Conceptual Design** - Create ER diagrams and data models
3. **Logical Design** - Map conceptual model to relational schema
4. **Physical Design** - Optimize for specific DBMS
5. **Implementation** - Create tables, indexes, and constraints
6. **Testing & Optimization** - Performance testing and tuning
7. **Maintenance** - Ongoing monitoring and optimization

### Modeling Approaches
- **Top-Down Design** - Start with high-level entities
- **Bottom-Up Design** - Start with attributes and group into entities
- **Inside-Out Design** - Start with known core entities

### Documentation Standards
- Data dictionaries
- ER diagrams with cardinality notation
- Schema migration scripts
- Change management logs

## Practical Templates

### Table Definition Template
```sql
CREATE TABLE table_name (
    id PRIMARY_KEY_TYPE GENERATED ALWAYS AS IDENTITY,
    column_name DATA_TYPE [CONSTRAINTS],
    -- Add audit columns
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(50),
    updated_by VARCHAR(50),
    
    CONSTRAINT pk_table_name PRIMARY KEY (id),
    CONSTRAINT fk_related_table FOREIGN KEY (column_name) 
        REFERENCES related_table(id)
);

-- Add indexes
CREATE INDEX idx_column_name ON table_name(column_name);

-- Add comments
COMMENT ON TABLE table_name IS 'Description of table purpose';
COMMENT ON COLUMN table_name.column_name IS 'Description of column';
```

### Normalization Checklist
- [ ] All attributes are atomic (1NF)
- [ ] No partial dependencies (2NF)
- [ ] No transitive dependencies (3NF)
- [ ] All determinants are candidate keys (BCNF)
- [ ] Foreign keys properly defined
- [ ] Indexes created for frequently queried columns
- [ ] Appropriate data types selected
- [ ] Constraints added for data validation

### Index Selection Guide
| Query Pattern | Recommended Index Type |
|--------------|------------------------|
| Equality searches | Hash or B-tree |
| Range queries | B-tree |
| Multi-column WHERE | Composite B-tree |
| Text search | Full-text index |
| JSON queries | GIN/GiST (PostgreSQL) |
| Geospatial data | Spatial index |

## Common Pitfalls

### Over-Normalization
**Problem**: Excessive normalization leading to complex joins and poor performance.
**Solution**: Denormalize selectively for read-heavy operations while maintaining write integrity.

### Missing Indexes
**Problem**: Queries perform full table scans causing slow performance.
**Solution**: Analyze query patterns and create appropriate indexes; monitor slow query logs.

### Poor Data Types
**Problem**: Using inappropriate data types wasting storage and causing conversion overhead.
**Solution**: Choose precise data types (e.g., DECIMAL for money, DATE for dates).

### Lack of Documentation
**Problem**: Schema becomes unmaintainable without proper documentation.
**Solution**: Maintain data dictionaries and ER diagrams; use schema comment features.

### Ignoring Scalability
**Problem**: Database works initially but fails under load.
**Solution**: Plan for partitioning, replication, and read replicas from the start.

### N+1 Query Problem
**Problem**: Fetching related data in loops causing excessive queries.
**Solution**: Use JOINs or batch loading with proper indexing.

## Best Practices

### Do
- Use meaningful, consistent naming conventions
- Implement soft deletes when data history matters
- Add audit trails for critical data changes
- Regularly analyze and update statistics
- Use connection pooling
- Implement proper backup and recovery procedures
- Version control schema migrations
- Test queries with realistic data volumes

### Don't
- Store computed values that can be derived
- Use SELECT * in production code
- Ignore query execution plans
- Create too many indexes (slows writes)
- Mix OLTP and OLAP workloads on same database
- Hardcode database-specific features without abstraction

## Tools & Resources

### Design Tools
- **dbdiagram.io** - Online ER diagram tool
- **MySQL Workbench** - Visual database design
- **pgAdmin** - PostgreSQL administration
- **DBeaver** - Universal database tool
- **Lucidchart** - Collaborative diagramming

### Monitoring & Analysis
- **EXPLAIN/EXPLAIN ANALYZE** - Query plan analysis
- **Slow Query Log** - Identify problematic queries
- **pg_stat_statements** - PostgreSQL query statistics
- **Performance Schema** - MySQL performance monitoring

### Migration Tools
- **Flyway** - Database migration tool
- **Liquibase** - Schema change management
- **Alembic** - Python database migrations
- **DbUp** - .NET database deployments

## Real-World Examples

### E-commerce Database
```sql
-- Products with inventory tracking
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    cost DECIMAL(10,2) CHECK (cost >= 0),
    category_id INTEGER REFERENCES categories(category_id),
    stock_quantity INTEGER DEFAULT 0 CHECK (stock_quantity >= 0),
    reorder_level INTEGER DEFAULT 10,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders with proper relationships
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_number VARCHAR(50) UNIQUE NOT NULL,
    customer_id INTEGER REFERENCES customers(customer_id),
    status VARCHAR(20) DEFAULT 'pending',
    total_amount DECIMAL(12,2) NOT NULL,
    shipping_address_id INTEGER REFERENCES addresses(address_id),
    billing_address_id INTEGER REFERENCES addresses(address_id),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    shipped_date TIMESTAMP,
    delivered_date TIMESTAMP
);

-- Order items with referential integrity
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(12,2) GENERATED ALWAYS AS (quantity * unit_price) STORED
);
```

### User Management System
Design considerations:
- Separate authentication from profile data
- Implement role-based access control tables
- Track login history for security
- Support soft deletes for GDPR compliance
- Use UUIDs for public-facing identifiers

## Metrics for Success

### Performance Metrics
- Query response time < 100ms for 95th percentile
- Index hit ratio > 95%
- Buffer cache hit ratio > 90%
- Transaction throughput meets SLA requirements

### Quality Metrics
- Zero referential integrity violations
- < 1% null values in required fields
- Schema documentation completeness > 95%
- Migration success rate = 100%

### Maintenance Metrics
- Backup completion rate = 100%
- Recovery time objective (RTO) met
- Recovery point objective (RPO) met
- Schema change deployment time < 30 minutes

## Practice Exercises

### Beginner
1. Design a library management system with books, members, and loans
2. Normalize an unnormalized spreadsheet of customer orders
3. Create appropriate indexes for common query patterns
4. Write DDL scripts with proper constraints

### Intermediate
1. Design a multi-tenant SaaS database schema
2. Optimize a poorly performing database with 10M+ records
3. Implement audit logging using triggers
4. Create partitioning strategy for time-series data

### Advanced
1. Design a globally distributed database with eventual consistency
2. Migrate a monolithic database to microservices architecture
3. Implement row-level security for multi-tenant isolation
4. Design a data warehouse schema with star/snowflake patterns

## Getting Started

### Learning Path
1. **Fundamentals**: Learn SQL basics and relational theory
2. **Modeling**: Practice ER diagram creation
3. **Normalization**: Master normal forms through exercises
4. **Indexing**: Understand how indexes work internally
5. **Optimization**: Learn query tuning techniques
6. **Advanced Topics**: Study replication, sharding, and distributed databases

### Recommended Resources
- Books: "Database Design for Mere Mortals" by Michael J. Hernandez
- Courses: Coursera "Database Management Essentials"
- Practice: LeetCode database problems
- Documentation: Official docs for your chosen RDBMS

### First Project
Design a blog platform database:
- Users, posts, comments, tags
- Implement proper relationships
- Add indexes for common queries
- Write migration scripts

## Quick Reference Card

### Normal Forms Quick Guide
- **1NF**: Atomic values, no repeating groups
- **2NF**: 1NF + no partial dependencies
- **3NF**: 2NF + no transitive dependencies
- **BCNF**: 3NF + every determinant is a candidate key

### Index Types
- **B-tree**: Default, good for ranges and sorting
- **Hash**: Fast equality lookups only
- **GIN**: Multi-value fields (arrays, JSON)
- **GiST**: Geospatial and full-text search
- **BRIN**: Large tables with natural ordering

### Common Constraints
```sql
PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, 
CHECK (condition), DEFAULT value, 
CONSTRAINT name_type CHECK (expression)
```

### Performance Tips
- Use EXPLAIN to analyze queries
- Index columns in WHERE, JOIN, ORDER BY
- Avoid functions on indexed columns in WHERE
- Use covering indexes when possible
- Regularly UPDATE STATISTICS

## Mastery Tips

1. **Think in Sets**: Embrace set-based operations over procedural thinking
2. **Understand Execution Plans**: Learn to read and optimize query plans
3. **Profile Before Optimizing**: Measure actual performance before making changes
4. **Design for Growth**: Consider future scale from the beginning
5. **Automate Everything**: Use migration tools and CI/CD for schema changes
6. **Stay Current**: Keep up with new database features and best practices
7. **Learn Multiple RDBMS**: Different databases have different strengths
8. **Understand Trade-offs**: Every design decision has pros and cons

## Related Skills

- [Data Analysis](data_analysis.md) - Extracting insights from data
- [System Architecture](../designing-skills/system_architecture.md) - Overall system design including data layer
- [API Design](../designing-skills/api_design.md) - Designing data access interfaces

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Data Skills Team
next_review: 2026-07-15
---
