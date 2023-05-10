# SQL dolgozat

1. DDL - Data Definition Language:
    - create database
    - drop database
    - create table
        - megszorítások is
        - create index
    - drop table
    - truncate table
    - alter table
    - view-k
1. DML - Data Manipulation Language:
    - insert
    - update
    - delete
1. DQL - Data Query Language - select lekérdezések
1. Mentés - backup készítés

## index

```sql
-- duplicate values are allowed
CREATE INDEX index_name
ON table_name (column1, column2, ...);

-- not allowed
CREATE UNIQUE INDEX index_name
ON table_name (column1, column2, ...);

-- példa:
CREATE INDEX idx_pname
ON Persons (LastName, FirstName);
```

Drop index:

```sql
--MS Access
DROP INDEX index_name ON table_name;
--SQL Server
DROP INDEX table_name.index_name;
--Oracle
DROP INDEX index_name;
--MySQL
ALTER TABLE table_name
DROP INDEX index_name;
```

## View

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;

--példa:
CREATE VIEW Brazil_Customers AS
SELECT CustomerName, ContactName
FROM Customers
WHERE Country = 'Brazil';

-- drop:
DROP VIEW view_name;
```

## Alter Table

```sql
ALTER TABLE table_name
ADD column_name datatype;
--példa:
ALTER TABLE Customers
ADD Email varchar(255);

ALTER TABLE table_name
DROP COLUMN column_name;
--példa
ALTER TABLE Customers
DROP COLUMN Email;

ALTER TABLE table_name
RENAME COLUMN old_name to new_name;

ALTER TABLE table_name
MODIFY COLUMN column_name datatype;
```

## backup

```sql
BACKUP DATABASE databasename
TO DISK = 'filepath';
```

A differential back up only backs up the parts of the database that have changed since the last full database backup.

```sql
BACKUP DATABASE databasename
TO DISK = 'filepath'
WITH DIFFERENTIAL;
```

Példa:

```sql
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak';

BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak'
WITH DIFFERENTIAL;
```