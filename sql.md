# SQL dolgozat

1. [DDL - Data Definition Language](#ddl---data-definition-language)
    - [Database](#database)
    - [Table](#table)
      - [Típusok](#tipusok)
      - [Megszoritások](#megszoritások)
      - [Index](#index)
      - [Alter table](#alter-table)
      - [View](#view)
1. [DML - Data Manipulation Language](#dml---data-manipulation-language)
    - [Insert](#insert)
    - [Update](#update)
    - [Delete](#delete)
1. [DQL - Data Query Language](#dql---data-query-language)
    - [Select](#select)
      - [Aggregáló függvények](#aggregáló-függvények)
      - [CASE](#case)
      - [TOP](#top-number)
      - [DISTINCT](#distinct)
    - [Rendezés - Order By](#rendezés)
    - [Szűrés - Where](#szűrés)
      - [Wildcards](#wildcards)
    - [Joins](#joins)
    - [Csoportosítás - Group By](#csoportosítás)
    - [Having](#újabb-feltétel---having)
    - [Halmazműveletek](#műveletek-select-ek-közt)
1. [Mentés - backup készítés](#backup)

## DDL - Data Definition Language

### Database

```sql
--create
CREATE DATABASE IF NOT EXISTS dbname;
--drop
DROP DATABASE IF EXISTS dbname;
```

### Table

```sql
--create
CREATE TABLE tablename(
    oszlopnev1 tipus megszoritasok,
    oszlopnev2 tipus megszoritasok,
    oszlopnev3 tipus megszoritasok,
}

--drop
DROP TABLE tablename;

-- truncate (tartalom törlése)
TRUNCATE TABLE tablename; 
```

#### Tipusok

(ennél több van, de elég csak ennyit tudni egyelőre)

- VARCHAR(size)
- BOOL
- INT
- FLOAT
- DOUBLE
- DATE
- DATETIME
- TIMESTAMP
- TIME
- YEAR

#### Megszoritások

- NOT NULL
  - nem lehet NULL
  - Ensures that a column cannot have a NULL value
- UNIQUE
  - egyediségi kényszer
  - Ensures that all values in a column are different

    ```sql
    create table dolgozok (
        az int not null primary key auto_increment,
        ig varchar(10) unique,
        nev varchar(50)
    );
    ```

- PRIMARY KEY
  - kulcs
  - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table

    ```sql
    create table osztalyok(
        az int not null primary key auto_increment,
        nev varchar(50)
    );
    ```

  - ez ugyanaz, viszont ha több mint 1 attributum van, csak igy lehet:

    ```sql
    create table osztalyok(
        az int not null auto_increment,
        nev varchar(50),
        primary key(az)
    );
    ```

- FOREIGN KEY
  - idegen kulcs
  - Prevents actions that would destroy links between tables

    ```sql
    create table osztalyok(
        az int not null primary key auto_increment,
        nev varchar(50)
    );

    create table dolgozok(
        az int not null primary key auto_increment,
        nev varchar(50),
        osztalyAz int,
        foreign key (osztalyAz) references osztalyok (az)
    );
    ```

- CHECK
  - ellenőrzés
  - Ensures that the values in a column satisfies a specific condition

    ```sql
    create table szamok (
        szam1 int check (szam1 >= 5),
        szam2 int check (szam2 >= 5),
        constraint nagyobb check (szam1>szam2)
    );
    ```

- DEFAULT
  - alapértelmezett érték
  - Sets a default value for a column if no value is specified

    ```sql
    CREATE TABLE Persons (
        ID int NOT NULL,
        LastName varchar(255) NOT NULL,
        FirstName varchar(255),
        Age int,
        City varchar(255) DEFAULT 'Sandnes'
    );
    ```

- CREATE INDEX
  - indexelje az értékeket
  - ez azt jelenti, hogy gyorsabban tudunk keresni a megadottak közt
  - Used to create and retrieve data from the database very quickly

#### Index

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

#### ALTER TABLE

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

#### View

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

## DML - Data Manipulation Language

### Insert

```sql
INSERT INTO `tablename`('oszlopnév1','oszlopnév2','oszlopnév3')
VALUES ('érték1','érték2','érték3');


INSERT INTO table2
SELECT * FROM table1
WHERE condition;

INSERT INTO table_name (column_list)
VALUES
    (value_list_1),
    (value_list_2),
    ...
    (value_list_n);
```

### Update

```sql
UPDATE tablename
SET mit=mire
WHERE szuresfelt;
```

### Delete

```sql
DELETE FROM tablename WHERE felt;
```

## DQL - Data Query Language

### Select

```sql
select oszloplista
from tablename;
```

oszloplista:

- vesszővel elválasztva felsorolásszerűen
- \* - minden oszlop
- oszlopnév **AS** ujnév - oszlopátnevezés a megjelenítéshez (*alias*)

```sql
select név AS nevek, kor
from adatok;

-- ekkor a két oszlop a megjelnítésben: nevek, kor
-- az első oszlop az adatok tábla név oszlop adatai
```

#### Aggregáló Függvények

```sql
--megszámolás
select count(*) AS 'db_adat'
from adatok;

-- átlagszámítás
select avg(kor)
from adatok;

-- összegzés
select sum(fizetések)
from adatok;

-- minimum
select min(kor)
from adatok;

-- összegzés
select max(kor)
from adatok;
```

#### CASE

Hajoosztályok tábla:
| osztály | tipus | ország | águkszáma |
| ---- | ---- | ---- | ----- |
| Bismark | bb | Németország | 8 |
| Iowa | bb | USA |9 |
| Kongo | bc | Japán | 8 |

```sql
select osztály,
CASE
    WHEN típus ="bb" THEN "csatahalyó"
    WHEN típus ="bc" THEN "cirkáló"
    ELSE "egyéb"
END AS tipus
FROM Hajoosztályok;
```

Eredmény:
| osztály | tipus |
| --- | --- |
| Bismark | csatahalyó |
| Iowa | csatahalyó |
| Kongo | cirkáló |

#### TOP NUMBER

Erre akkor van szükségünk, ha az első néhány találat kell nekünk:

```sql
select top 3 név, kor
from adatok;
-- az adatok táblábol a név, kor oszlopokat mutatja
-- de csak véletlenszerűen az első 3-at rekordot
-- megj: akkor lesz értelme, ha tudunk rendezni egy oszlop szerint:
select top 1 név
from adatok
order by kor;
-- Ez a legfiatalabb személy nevét írja ki
```

#### Distinct

Duplikátumok eltüntetése

adatok tábla:
| név | kor |
| --- | --- |
| János | 21 |
| Géza | 25 |
| János | 45 |
| Béla | 8 |
| István | 30 |

```sql
SELECT név
FROM table_name; 
```

A fenti lekérdezés eredményében a János név kétszer is szerepelni fog, de ennek semmi értelme

```sql
SELECT DISTINCT név
FROM adatok; 
```

Eredmény:
| név |
| --- |
| János |
| Géza |
| Béla |
| István |

### Rendezés

```sql
SELECT név
FROM adatok
ORDER BY név; -- abc szerinti sorrend 

SELECT név
FROM adatok
ORDER BY név desc; -- abc szerint visszafele
```

### Szűrés

```sql
SELECT név
FROM adatok
Where kor>5;
```

Feltételben operátorok:

- \=
- \> \< \>= \<=
- \<\>
- [NOT] BETWEEN 50 AND 60
- [NOT] LIKE
- [NOT] IN
  - column_name IN (val1, val2, val3)
  - column_name IN (SELECT .... )
- AND, OR, NOT
- IS NULL
- IS NOT NULL

#### Wildcards

| MYSQL | magyarázat |
| --- | --- |
| WHERE CustomerName LIKE 'a%' | Finds any values that start with "a" |
| WHERE CustomerName LIKE '%a' | Finds any values that end with "a" |
| WHERE CustomerName LIKE '%or%' | Finds any values that have "or" in any position |
| WHERE CustomerName LIKE '_r%' | Finds any values that have "r" in the second position |
| WHERE CustomerName LIKE 'a_%' | Finds any values that start with "a" and are at least 2 characters in length |
| WHERE CustomerName LIKE 'a__%' | Finds any values that start with "a" and are at least 3 characters in length |
| WHERE ContactName LIKE 'a%o' | Finds any values that start with "a" and ends with "o" |

### Joins

![kép](https://www.codeproject.com/KB/database/Visual_SQL_Joins/Visual_SQL_JOINS_orig.jpg)

[w3school](https://www.w3schools.com/sql/sql_join.asp)
[részletesen](https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins)

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN

### Csoportosítás

Hajoosztalyok:

| Osztály | típus | Ország | ágyúkSzáma | kaliber | vízkiszorítás |
| --- | --- | --- | --- | --- | --- |
| Bismark. | bb | Németország | 8 | 15 | 42000 |
| Iowa | bb | USA | 9 | 16 | 46000 |
| Kongo | bc | Japán | 8 | 14 | 32000 |
| North Carolina | bb | USA | 9 | 16 | 37000 |
| Renown | bc | Nagy Britannia | 6 | 15 | 32000 |
| Revenge | bb | Nagy Britannia | 8 | 15 | 29000 |
| Tennessee | bb | USA | 12 | 14 | 32000 |
| Yamato | bb | Japán | 9 | 18 | 65000 |

```sql
select típus, count(Osztály) AS "darab"
from Hajoosztalyok
group by típus;
```

| típus | darab |
| --- | --- |
| bb | 6 |
| bc | 2 |

Akkor most ezt szépítsük a korábbiak alapján:

```sql
select 
    CASE
        WHEN típus ="bb" THEN "csatahalyó"
        WHEN típus ="bc" THEN "cirkáló"
        ELSE "egyéb"
    END AS hajótípus, count(Osztály) AS "darab"
from Hajoosztalyok
group by típus
order by hajótípus;
```

| hajótípus | darab |
| --- | --- |
| cirkáló | 2 |
| csatahalyó | 6 |

### Újabb feltétel - HAVING

Miben más mint a where?
Tudja használni az aggregáló függvényeket a feltételben.

Hajoosztalyok:

| Osztály | típus | Ország | ágyúkSzáma | kaliber | vízkiszorítás |
| --- | --- | --- | --- | --- | --- |
| Bismark. | bb | Németország | 8 | 15 | 42000 |
| Iowa | bb | USA | 9 | 16 | 46000 |
| Kongo | bc | Japán | 8 | 14 | 32000 |
| North Carolina | bb | USA | 9 | 16 | 37000 |
| Renown | bc | Nagy Britannia | 6 | 15 | 32000 |
| Revenge | bb | Nagy Britannia | 8 | 15 | 29000 |
| Tennessee | bb | USA | 12 | 14 | 32000 |
| Yamato | bb | Japán | 9 | 18 | 65000 |

```sql
select 
    CASE
        WHEN típus ="bb" THEN "csatahalyó"
        WHEN típus ="bc" THEN "cirkáló"
        ELSE "egyéb"
    END AS "Amiből 5-nél több van"
from Hajoosztalyok
group by típus
HAVING count(Osztály) > 5
order by hajótípus;
```

| Amiből 5-nél több van |
| --- |
| csatahalyó |

### Műveletek Select-ek közt

(relációs algebrából ismertek)

- Unió
  - **UNION** - duplikátumok nélkül
  - **UNION ALL** - duplikátumokkal
- Különbség
  - **MINUS**
- metszet
  - **INTERSECT**

## Backup

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
