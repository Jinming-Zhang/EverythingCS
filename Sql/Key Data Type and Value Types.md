## Data Type depends on the Database System
Supported data types are dependent on the database system.
We could look into the official document for supported data types of the database system that we are working on.

[MySql Supported Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)
[PostgreSql supported Data Types](https://www.postgresql.org/docs/current/datatype.html)

However, there are some core data types that most of database systems should support.
## Key Data Types
### Text
> **CHAR(X)**
>Store text up to X characters, **shorter text will be padded with space**

>**VARCHAR(X)**
Store text up to X characters, shorter strings will not be changed

> **TEXT**
> Text with no user-defined max length, max size denpends on database system

>**ENUM**
>Only values from a predefined set of allowed values are accepted
>
>ENUM is built-in for MySql:
>```sql
>CREATE TABLE enum_example(
>    gender ENUM('male', 'wolf')
>);
>``` 
>
>For PostgreSql, we need to create a custom type first
>```sql
>CREATE TYPE gender_type AS ENUM('male', 'wolf');
>CREATE TABLE enum_example(
>    gender gender_type
>);
>```

^691b84

### Numeric
>**INT**
>Integer numbers (between min and max boundaries) are allowed

>**DECIMAL** / **NUMERIC**
> Decimal numbers with a fixed precision (exact values are stored)
> Will have more performance cost comparing to floating point numbers.

> **FLOAT** / **REAL**
> Decimal numbers with floating points (the approximated values are stored, based on the precision)
### Date
Many database system will store the time in UTC timezone, and when queried, it will return the translated time based on the client that sent the query.
For details check the database system's official document.

>**DATE**
>A value like 1995-12-05
>Just the date, no times like hours

>**DATETIME** / **TIMESTAMP**
>A value like 1995-12-05 12:34:21
>With time

### Others
> **BOOLEAN**
> True/false

>**JSON**
> A special kind of text

### How to store files
Usually do not store files in database, instead, store them on a file server/ hard drive, then store the path in the database.
