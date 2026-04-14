# MSSQL Security Checklist

## Authentication
- Use Windows Authentication where possible (more secure)
- For SQL Auth: enforce strong passwords, rotate regularly
- Never use `sa` account for applications

## Authorization
- Principle of least privilege — grant only required permissions
- Use roles, not direct user grants
- Separate application roles from admin roles

## Query Security

### Parameterization (prevent SQL injection)
```sql
-- ✅ SAFE: Parameterized
CREATE PROCEDURE GetCustomer @CustomerId INT
AS
    SELECT * FROM Customers WHERE Id = @CustomerId;

-- ❌ DANGEROUS: Concatenation
-- SELECT * FROM Customers WHERE Id = ' + @CustomerId + '
```

## Encryption
- Use `ENCRYPTBYPASSPHRASE` for quick obfuscation (not real encryption)
- Use `ENCRYPTBYKEY` / `DECRYPTBYKEY` for real column encryption
- Always use TLS for data in transit
- Enable `ALWAYS ENCRYPTED` for sensitive columns

## Sensitive Data
```sql
-- Dynamic data masking (SQL 2016+)
ALTER TABLE Customers
ADD EmailMask AS CONCAT(LEFT(Email, 2), '***', RIGHT(Email, 4));

ALTER TABLE Customers
ALTER COLUMN Email ADD MASKED WITH (FUNCTION = 'email()');
```

## Auditing
- Enable SQL Server Audit
- Monitor failed logins
- Track schema changes
- Review logs regularly

## Backup Security
- Encrypt backups: `BACKUP ... WITH COMPRESSION, ENCRYPTION`
- Store backups in secure locations
- Test restore procedures
