---
name: mssql
description: "MSSQL (Microsoft SQL Server) development skill. Use when writing T-SQL queries, stored procedures, designing schemas, optimizing performance, managing indexes, working with Azure SQL, or any MSSQL-specific development task. Covers T-SQL syntax, best practices, common patterns, and anti-patterns."
---

# MSSQL / T-SQL Development Skill

Specialized knowledge for Microsoft SQL Server development. T-SQL specific patterns, performance optimization, and development workflows.

## Core Types

### T-SQL Query Patterns

```sql
-- Window functions (MSSQL 2012+)
SELECT 
    name,
    salary,
    SUM(salary) OVER (PARTITION BY dept ORDER BY hire_date) as running_total,
    LAG(name, 1) OVER (ORDER BY salary DESC) as prev_higher_paid
FROM employees;

-- Common Table Expressions (CTEs)
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) as rn
    FROM products
)
SELECT * FROM ranked WHERE rn <= 3;

-- CROSS APPLY for top-N per group
SELECT p.name, o.order_id, o.total
FROM products p
CROSS APPLY (SELECT TOP 5 order_id, total FROM orders WHERE product_id = p.id ORDER BY date DESC) o;
```

### Schema Design

```sql
-- Proper indexing
CREATE NONCLUSTERED INDEX IX_Orders_CustomerDate 
ON Orders(CustomerId, OrderDate) 
INCLUDE (TotalAmount)
WHERE IsDeleted = 0;

-- Filtered index
CREATE INDEX IX_Orders_Active 
ON Orders(CustomerId) 
WHERE OrderStatus = 'Active';

-- Columnstore for analytics (MSSQL 2012+)
CREATE COLUMNSTORE INDEX CSI_Sales ON Sales(ProductId, Date, Amount);
```

## Performance Optimization

### Query Analysis
```sql
-- Actual execution plan analysis
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
-- Your query here

-- Missing index detection
SELECT 
    migs.avg_total_user_cost * (migs.avg_user_impact / 100.0) * (migs.user_seeks + migs.user_scans) as impact,
    mid.statement as table_name,
    migs.avg_total_user_cost,
    migs.avg_user_impact,
    migs.user_seeks,
    migs.user_scans,
    mid.equality_columns,
    mid.included_columns
FROM sys.dm_db_missing_index_groups mig
JOIN sys.dm_db_missing_index_group_stats migs ON migs.group_handle = mig.index_group_handle
JOIN sys.dm_db_missing_index_details mid ON mid.index_handle = mig.index_handle
WHERE migs.avg_total_user_cost * migs.avg_user_impact > 100
ORDER BY migs.avg_total_user_cost * migs.avg_user_impact * (migs.user_seeks + migs.user_scans) DESC;
```

### Common Optimizations
- **Avoid** `SELECT *` — specify columns
- **Use** `SET NOCOUNT ON` in stored procedures
- **Use** `TRY...CATCH` for error handling
- **Avoid** `NOT IN` — use `NOT EXISTS` or `LEFT JOIN`
- **Use** `NVARCHAR(MAX)` instead of TEXT (deprecated)
- **Prefer** `COUNT_BIG(*)` for large tables
- **Use** `OUTPUT` clause instead of SCOPE_IDENTITY()

## Stored Procedures Best Practices

```sql
CREATE OR ALTER PROCEDURE dbo.InsertOrder
    @CustomerId INT,
    @OrderDate DATETIME2,
    @OrderId INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    
    BEGIN TRY
        BEGIN TRANSACTION;
        
        INSERT INTO Orders (CustomerId, OrderDate, Status)
        VALUES (@CustomerId, @OrderDate, 'Pending');
        
        SET @OrderId = SCOPE_IDENTITY();
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
        THROW;
    END CATCH
END
```

## Azure SQL Specific

```sql
-- Elastic queries for sharding
CREATE EXTERNAL DATA SOURCE MyShards
WITH (
    TYPE = SHARD_MAP_MANAGER,
    LOCATION = 'myserver.database.windows.net',
    DATABASE_NAME = 'ShardMapDb',
    CREDENTIAL = ElasticDBQueryCred
);

-- Intelligent performance
ALTER DATABASE CURRENT SET INTELLIGENT_SENSORY_QUERY_CORRELATION = ON;
```

## Development Workflow

### Schema Versioning
- Use migration scripts (Flyway, Liquibase, or custom)
- Never modify scripts that have been deployed
- Always wrap DDL in transactions for rollback capability

### Testing
```sql
-- Unit test pattern with tSQLt
EXEC tSQLt.NewTestClass 'TestOrderProc';
GO

CREATE OR ALTER PROCEDURE TestOrderProc.[Test insert order succeeds]
AS
BEGIN
    -- Arrange
    EXEC tSQLt.FakeTable 'dbo.Orders';
    
    -- Act
    DECLARE @OrderId INT;
    EXEC dbo.InsertOrder @CustomerId = 1, @OrderDate = GETDATE(), @OrderId = @OrderId OUTPUT;
    
    -- Assert
    EXEC tSQLt.AssertEquals 1, @OrderId;
END
```

## Quick Reference

| Pattern | Use INSTEAD of |
|---------|----------------|
| `NOT EXISTS` | `NOT IN` with subquery |
| `OUTER APPLY` | `LEFT JOIN` with subquery |
| `MERGE` | Multiple IF/ELSE INSERT/UPDATE |
| `INTO #temp` | `SELECT INTO` (for large) |
| `TRY_CAST/CONVERT` | Direct CAST (with error handling) |

## When to Use

- Writing or reviewing T-SQL queries
- Designing tables, indexes, constraints
- Creating/modifying stored procedures, functions, triggers
- Performance tuning and execution plan analysis
- Azure SQL Database or SQL Server on-premises
- Schema migrations and deployments
