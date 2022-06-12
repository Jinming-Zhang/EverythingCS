# Primary Key
A primary key is used as an unique identifier for each entry inside a table.

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

# Foreign Key
`Foreign Key` is a constraint that can add to a column to indicate that the column is depending on another coulumn in a different table.
```sql
CREATE TABLE table_1(
	some_col INT,
	FOREIGN KEY (some_col) REFERENCE another_table (col_in_another_table) ON DELETE CASCADE );

-- example
CREATE TABLE table_1(
	address_id INT,
	FOREIGN KEY (address_id) REFERENCE address (id)
);
```
Add `Foreign Key` constraint with a name:
```sql
-- add foreign key constraint with a name
CREATE TABLE table_name (
col_name col_data_type,
CONSTRAINT c_name
FOREIGN KEY (col_name) REFERENCES other_table (other_col_name)
);
-- example
CREATE TABLE emp_private(
	id INT PRIMARY KEY AUTO_INCREMENT,
	emp_no INT ,
	CONSTRAINT emp_no_foreignKey FOREIGN KEY (emp_no) REFERENCES employees(emp_no), privacy TEXT
)
```
Avaiable actions:
![[SQL-TheCompleteDevelopersGuideMySQLPostgreSQLUdemy-5-26.jpg]]

## Add/Remove Foreign Key
To add a foreign key constraint to an existing table:
```sql
ALTER TABLE <table_name>
ADD FOREIGN KEY <column_name> REFERENCES <related_table> (<related_column>) ON DELETE ... ON UPDATE...
-- with name
ALTER TABLE <table_name>
ADD CONSTRAINT <constraint_name> FOREIGN KEY <column_name> REFERENCES ... (see above)
```
To delete a foreign key constraint to an existing table:
```sql
ALTER TABLE <table_name>
DROP FOREIGN KEY <constraint_name>;
```