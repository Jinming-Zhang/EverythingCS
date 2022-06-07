# WHERE
Filter result to only show those satisfy the given conditions.
```sql
SELECT
emp_no as dog_tag,
salary / 100 as salary, 
"hardcoded column"
FROM
salaries
WHERE
emp_no = 10069;
```

# ORDER BY
Order the result by the givin attribute/column
```sql
SELECT * FROM salaries
ORDER BY salary;

-- order in descending order
SELECT * FROM salaries
ORDER BY salary DESC;
```

 When multiple columns is used for ordering, when a column has the same value, it will be ordered by the following column given.
```sql
SELECT * FROM salaries
ORDER BY salary, emp_no DESC;
```

# LIMIT
Limit the result to show.
```sql
SELECT * FROM salaries
LIMIT 50;
```

# OFFSET
Skip given number of entries of queried result.
```sql
SELECT * FROM salaries
OFFSET 10;
```

# DISTINCT
Only shows distinct result, duplicates will be omitted.
```sql
SELECT DISTINCT * FROM salaries;
```