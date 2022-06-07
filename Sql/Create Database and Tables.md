## Data Definition Operations

## Creating Databases
```sql
CREATE DATABASE "database_name";
```


## Creating Tables
```sql
CREATE TABLE "table_name"
(
	"id" int PRIMARY KEY AUTO_INCREMENT,
	"col_name_1" INT NOT NULL UNIQUE,
	"col_name_2" VARCHAR(256) NOT NULL,
	"col_name_3" DECIMAL(9,2),
	"col_name_4" ENUM('v1', 'v2', 'v3'),
	"col_name_5" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	"col_name_6" VARCHAR(256) GENERATED ALWAYS AS (CONCAT("col_name_2","something"))
);
```

```sql
-- create table from other table
CREATE TEMPORARY TABLE "table_name" AS SELECT * FROM "other_table_name";
```

- When creating a table, we also need to declare the data type for each colume that will be in the table. [[Key Data Type and Value Types | note link]] 

- We can have a column dedicated as an [[Constraints| unique]] [[Primary Key Foreign Key|ID]], that guarantees it's value is unique among all entries.

- We can also specify the default value for columns when the column data isn't provided during insert, check official database system document for the supported default value for each data type (e.g: [Mysql](https://dev.mysql.com/doc/refman/8.0/en/timestamp-initialization.html#:~:text=TIMESTAMP%20has%20a%20default%20of,case%20the%20default%20is%20NULL%20.))

- We can also add [[Constraints]] for columns when creating a table.

-  [[Key Data Type and Value Types#^691b84 | See difference of ENUM between MySql and PostgreSql]].
 
 
 
 ## Create View
 A read-only table that shows commonly used query result.
 View is stored in database as a query instead of an actual table, whenever the View is needed, the query is ran.
 ```sql
 CREATE VIEW view_name AS
 SELECT * FROM employee
 WHERE salary > 1000;
 ```

## Updating Databases
ALTER DATABASE
## Updating Tables
Different database system have different syntax for altering tables, check their offical document for details.
- [MySql](https://dev.mysql.com/doc/refman/8.0/en/alter-table.html)
	```sql
	ALTER TABLE "table_name"
	MODIFY COLUMN "col_name"
	FLOAT(5,2) DEFAULT 0;
	```
- [PostgreSql](https://www.postgresql.org/docs/current/sql-altertable.html)
	```sql
	ALTER TABLE "table_name"
	ALTER COLUMN "col_name" 
		SET DATA TYPE
		TIMESTAMP 
		DEFAULT CURRENT_TIMESTAMP;
	```

## Deleting Database
```sql
DROP DATABASE "database_name";
```

## Deleting Table
```sql
DROP TABLE "table_name";
```