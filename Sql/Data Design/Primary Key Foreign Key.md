Automatic incremented primary key:
```sql
-- mysql
CREATE TABLE "table_name"(
	"col-name" INT PRIMARY KEY AUTO_INCREMENT
);
```

```sql
-- postgre
CREATE TABLE "table_name"(
	"col-name" INT SERIAL PRIMARY KEY
);
```
- Primary key is used by database, it's guaranteed to be `NOT NULL` and `UNIQUE`. 
- It's the primary identification column for the entries of the table.
- Only one PRIMARY KEY per table is allowed.