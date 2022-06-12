# Constraints
Constraints can be set to a column when creating a table, different database systems can have different syntax, check official document for details.
## Constraint - NOT NULL 
```sql
CREATE TABLE "table_name"(
	full_name VARCHAR(256) NOT NULL
);
```
or altering a table:
```sql
-- for mysql
ALTER TABLE "table_name"(
	MODIFY COLUMN "col-1" VARCHAR(256) NOT NULL
);
```
```sql
-- for postgreSql
ALTER TABLE "table_name"(
	ALTER COLUMN "col-1" SET NOT NULL,
	ALTER COLUMN "col-2" SET NOT NULL
);
```

## Constraint - CHECK
On table creation:
```sql
-- column-wise CHECK
CREATE TABLE "table_name"(
	"col-1" INT CHECK(col-1 > 0 AND col-1 < 1000)
);

-- entry-wise CHECK
CREATE TABLE "table_name"(
	"col-1" INT CHECK(col-1 > 0 AND col-1 < 1000),
	"col-2" INT,
	CHECK (col-1 > col-2)
	
);
```
On altering table:
```sql
-- for mysql and postgres
ALTER TABLE "table_name"
ADD CONSTRAINT "constraint-name"
CHECK(col>0);

```

## Constraint - UNIQUE
```sql
CREATE TABLE "table_name"(
	"col-name" INT NOT NULL UNIQUE
);
```

## Constriant - PRIMARY/FOREIGN KEY
See [[Primary Key Foreign Key]]
Primary Key must be not null and unique, only one primary key column is allowed in a table.
