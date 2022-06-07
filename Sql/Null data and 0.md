# Null
If a column is omitted during insertion, and there are no default value or constraint set, then the value of that coloumn will be `null`.
# Null vs 0/''
Null and 0 are different 
Null values will be ignored for a lot of Sql operations.
0 will effect Sql operations.
eg: AVG()