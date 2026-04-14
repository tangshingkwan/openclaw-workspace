# MSSQL Quick Reference Card

## Data Types

| Type | Use For | Notes |
|------|---------|-------|
| `INT/BIGINT` | Primary keys, FKs | Use `BIGINT` for large tables |
| `DECIMAL(p,s)` | Money | Never use FLOAT for money |
| `DATETIME2` | Dates | Preferred over DATETIME |
| `NVARCHAR(MAX)` | Large text | Replaces deprecated TEXT |
| `BIT` | Booleans | 0/1 values |
| `UNIQUEIDENTIFIER` | UUIDs | Use `NEWSEQUENTIALID()` for performance |

## Index Types

```
Clustered      — Orders data physically (1 per table)
Nonclustered   — Separate structure (249 per table)
Columnstore    — Compression for analytics (1 per table)
Filtered       — Partial index with WHERE clause
```

## Common T-SQL Functions

```sql
-- Date functions
DATEADD(day, 7, GETDATE())
DATEDIFF(day, start, end)
EOMONTH(date)  -- Last day of month

-- String
CONCAT_WS('-', col1, col2)
STRING_SPLIT(col, ',')
TRIM/LTRIM/RTRIM

-- Conditional
IIF(condition, true, false)        -- SQL 2012+
CHOOSE(index, val1, val2, ...)      -- SQL 2012+
```

## Query Performance Checklist

- [ ] `SELECT` only needed columns
- [ ] `WHERE` clause is sargable (no functions on indexed columns)
- [ ] Proper indexes exist (not too many — writes suffer)
- [ ] No implicit conversions (types must match)
- [ ] `SET NOCOUNT ON` in procedures
- [ ] `TRY...CATCH` for error handling
- [ ] `SET XACT_ABORT ON` for distributed transactions

## Anti-Patterns to Avoid

❌ `SELECT *` — retrieves unnecessary data
❌ `NOT IN (SELECT...)` — use `NOT EXISTS`
❌ `OR` in JOIN — split into UNION
❌ `CURSOR` — use set-based operations
❌ `sp_` prefix — reserved for system procs
❌ `WITH (NOLOCK)` — use RCSI instead
❌ `FLOAT/REAL` for money — rounding errors
❌ `DATETIME` — use `DATETIME2` for precision

## Azure SQL Tiers

| Tier | Use Case |
|------|----------|
| Basic | Dev/test, small DBs (<2GB) |
| Standard | Production, moderate workloads |
| Premium/HS | High performance, large OLTP |
| Hyperscale | Very large, auto-scaling |
