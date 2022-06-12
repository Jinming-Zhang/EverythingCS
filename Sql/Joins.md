# Inner Join
 `INNER JOIN` merges data from multiple tables into one result, which contains entries that satisfys the givin matching conditions.
 
 >Entries that don't satisfy matching condition will be ignored.
 
```sql
SELECT col_1, col_2
FROM
table_1 INNER JOIN table_2
ON
table_1.col_1 = table_2.col_1;
-- Example
SELECT 
e.emp_no as id, e.first_name as fname, s.salary as salary
FROM
employees as e 
INNER JOIN 
salaries as s
ON
e.emp_no = s.emp_no
LIMIT 50
```

# Left Join & Right Join
Similar to `INNER JOIN`, but it
- Includes all the entries on the left side of the `LEFT JOIN` even it doesn't satisfy the matching condition. 
- Only includes matching entries for the table on the right side of `LEFT JOIN`.
- Columns that don't have a matching entry for the right table will have NULL value.

# Cross Join

`CROSS JOIN` will result in all combinations of entries in two tables.
```sql
SELECT * FROM
table_1 CROSS JOIN table_2;
```

# Union
Appending multiple table entries with same number of coloumns, **can not** be used on entries with different number of columns.

Usually used on entires with same column definitions
```sql
SELECT * FROM table_1
WHERE id > 1
UNION
SELECT * FROM table_1
WHERE id < 100;
```

# Union vs Join
- `UNION` appending new entries of multiple queries, it adds rows.
- `JOIN` appending columns of multiple queries, it adds columns.


![[SQL-TheCompleteDevelopersGuideMySQLPostgreSQLUdemy-3-47.jpg]]
