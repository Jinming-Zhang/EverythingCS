# Insert / Create entry
```sql
-- has to be the same order as in table
INSERT INTO "databse_name" VALUES (
	'col-1-value',
	'col-2-value',
	2
);
```
or
```sql
-- specify custom order of the data column
-- insert multiple entries at once, separated by comma
INSERT INTO "database_name" 
(col-3, col-2, col-1)
VALUES
('val-11', 'val-12', 'val-13'),
('val-21', 'val-22', 'val-23');
```
or
```sql
-- insert entry by querying from other table
(col-3, col-2, col-1)
VALUES
SELECT <query>;
```

# Select / Create Data
```sql
SELECT 
"column1",
"column2" AS "new_name"
FROM "table_name"
WHERE "conditions";

-- real example
SELECT
emp_no as dog_tag,
salary / 100 as salary, 
"hardcoded column"
FROM
salaries
WHERE
emp_no = 10069;
```

Avaiable Comparision for `WHERE` clause:
- `=, IS` (for checking against `NULL` / BOOL)
- `<>, !=, IS NOT`
- `>, >=, <, <=`
- `AND, OR`

```sql
SELECT
emp_no as dog_tag,
salary, 
from_date,
to_date,
"hardcoded column"
FROM
salaries
WHERE
(emp_no = 10069)
AND
from_date > '1999-12-31'
AND
(salary BETWEEN 85000 AND 90000);
-- BETWEEN queries values INCLUSIVELY for both sides
```

## Nested Queries
Since query returns a table, it can also be used to run `SELECT` query. But we can't alter the data in query because those only exist in memory
```sql
SELECT emp_no FROM
	(SELECT * FROM salaries
	WHERE salary > 12345)
AS rich_people;
```
# Update Data
```sql
-- based on the condition, this can update multiple entries at once
UPDATE "table_name"
SET "col-1-name" = "new value",
	"col-2-name" = "new value"
	...
WHERE "conditions";

-- real example
UPDATE employees_sample
SET 
	first_name = "wolfy",
	last_name = "furry"
WHERE emp_no = 10001;
```

# Delete Data
```sql
-- based on the condition, this can delete multiple entries
DELETE FROM "table_name"
WHERE "conditions";

-- real example
DELETE FROM employees_sample
WHERE
emp_no < 10069;
```

