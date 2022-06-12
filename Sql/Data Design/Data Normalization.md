
# Data Normalization
A concept to reduce data redundancy.


# Six Forms of Normalization
1. Each table cell (column + row) should contain a single value.
	1. Each row (record/entry) should be unique
2. There are no duplicate row values because of multi-column keys (composite keys/a combination of columns as a key)
3. All column values in a row are dependent on only the primary key.
4. There must be no conflicting unique identification criterial (i.e. column value combinations). Avoid multiple entities in one table.
5. All combinations of all (non-key) cell values should be possible.
6. There are no clashing column values because of implicit column dependencies.

# Easier-to-Understand-Rules
1. Avoid mixing data entities in the same table.
2. Avoid multiple values in a single table cell. (i.e. avoid "name_add", a column for both name and address).
3. Avoid splitting basic data across a lots of tables.
4. One Table = One Data Entity / One Type of Object
5. One Cell = One Value