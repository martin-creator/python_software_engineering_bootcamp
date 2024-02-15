# SQL and Relational Databases Crash Course
# SQL Overview
##  SQL is a language designed to work with databases
##  SQL stands for Structured Query Language
##  SQL allows you to access and manipulate databases
##  SQL is an ANSI (American National Standards Institute) standard
##  SQL can execute queries against a database
##  SQL can retrieve data from a database
##  SQL can insert records in a database
##  SQL can update records in a database
##  SQL can delete records from a database
##  SQL can create new databases
##  SQL can create new tables in a database

# SQL Syntax
##  SQL syntax is the set of rules that defines how SQL statements are constructed
##  SQL syntax is similar to English language
##  SQL syntax is case-insensitive
##  SQL syntax is divided into several categories:
###  Data Definition Language (DDL)
###  Data Manipulation Language (DML)
###  Data Query Language (DQL)
###  Transaction Control Language (TCL)
###  Data Control Language (DCL)

# Data Definition Language (DDL)
##  DDL is used to define the structure of the database
##  DDL commands include:
###  CREATE DATABASE
###  CREATE TABLE
###  ALTER TABLE
###  DROP TABLE
###  TRUNCATE TABLE
###  CREATE INDEX
###  DROP INDEX

# Data Manipulation Language (DML)
##  DML is used to manage data within the database
##  DML commands include:
###  INSERT
###  UPDATE
###  DELETE

# Data Query Language (DQL)
##  DQL is used to retrieve data from the database
##  DQL commands include:
###  SELECT
### FROM
### WHERE
### GROUP BY
### HAVING
### ORDER BY

# Transaction Control Language (TCL)
##  TCL is used to manage transactions within the database
##  TCL commands include:
###  COMMIT
###  ROLLBACK
###  SAVEPOINT
###  SET TRANSACTION

# Data Control Language (DCL)
##  DCL is used to manage permissions within the database
##  DCL commands include:
###  GRANT
###  REVOKE

# SQL Statements
##  SQL statements are used to perform tasks such as:
###  Create a database
###  Create a table
###  Insert records
###  Update records

# SQL Keywords
##  SQL keywords are reserved words that have special meaning in SQL
##  SQL keywords are case-insensitive
##  SQL keywords include:
###  SELECT
###  INSERT

# SQL Identifiers
##  SQL identifiers are used to name database objects such as tables and columns
##  SQL identifiers can be:
###  Table names
###  Column names
###  Index names
###  View names

# SQL Comments
##  SQL comments are used to document SQL code
##  SQL comments can be:
###  Single-line comments
###  Multi-line comments
###  Single-line comments start with --
###  Multi-line comments start with /* and end with */

# SQL Data Types
##  SQL data types are used to define the type of data that can be stored in a column
##  SQL data types include:
###  Numeric data types
###  Character data types
###  Date and time data types
###  Binary data types
###  Miscellaneous data types

# SQL Operators
##  SQL operators are used to perform operations on data
##  SQL operators include:
###  Arithmetic operators
###  Comparison operators
###  Logical operators
###  Bitwise operators
###  Assignment operators

# SQL Functions
##  SQL functions are used to perform operations on data
##  SQL functions include:
###  Aggregate functions
###  Scalar functions
###  String functions
###  Date and time functions
###  Mathematical functions
###  Miscellaneous functions

# SQL Constraints
##  SQL constraints are used to enforce rules on data
##  SQL constraints include:
###  NOT NULL
###  UNIQUE
###  PRIMARY KEY
###  FOREIGN KEY
###  CHECK
###  DEFAULT

# SQL Joins
##  SQL joins are used to combine rows from two or more tables
##  SQL joins include:
###  INNER JOIN
###  LEFT JOIN
###  RIGHT JOIN
###  FULL JOIN
###  CROSS JOIN
###  SELF JOIN

# SQL Subqueries
##  SQL subqueries are used to nest one query within another query
##  SQL subqueries include:
###  Single-row subqueries
###  Multiple-row subqueries
###  Multiple-column subqueries
###  Correlated subqueries

# SQL Views
##  SQL views are used to store a query as a virtual table
##  SQL views can be used to:
###  Simplify complex queries
###  Hide the complexity of the underlying database schema
###  Provide an additional layer of security

# SQL Indexes
##  SQL indexes are used to improve the performance of queries
##  SQL indexes include:
###  Single-column indexes
###  Composite indexes
###  Unique indexes
###  Clustered indexes
###  Non-clustered indexes
###  Bitmap indexes

# SQL Triggers
##  SQL triggers are used to automatically perform actions when certain events occur
##  SQL triggers include:
###  BEFORE triggers
###  AFTER triggers
###  INSTEAD OF triggers
###  Compound triggers

# SQL Transactions
##  SQL transactions are used to manage groups of SQL statements
##  SQL transactions include:
###  BEGIN TRANSACTION
###  COMMIT TRANSACTION
###  ROLLBACK TRANSACTION
###  SAVE TRANSACTION

# SQL Best Practices
##  SQL best practices include:
###  Use consistent naming conventions
###  Use comments to document SQL code
###  Use transactions to ensure data consistency
###  Use constraints to enforce data integrity
###  Use indexes to improve query performance
###  Use views to simplify complex queries
###  Use triggers to automate actions
###  Use stored procedures to encapsulate business logic
###  Use subqueries to simplify complex queries

# SQL Injection
##  SQL injection is a security vulnerability that occurs when an attacker is able to execute malicious SQL statements
##  SQL injection can be prevented by:
###  Using parameterized queries
###  Using stored procedures
###  Using input validation
###  Using least privilege access
###  Using web application firewalls

# SQL vs NoSQL
##  SQL and NoSQL are two types of database management systems
##  SQL databases are relational databases
##  NoSQL databases are non-relational databases
##  SQL databases use a schema
##  NoSQL databases do not use a schema
##  SQL databases use structured query language
##  NoSQL databases use different query languages
##  SQL databases are suitable for complex queries
##  NoSQL databases are suitable for unstructured data
##  SQL databases are suitable for transactional applications
##  NoSQL databases are suitable for analytical applications
##  SQL databases are suitable for structured data
##  NoSQL databases are suitable for unstructured data

# Examples of using SQL in various real work scenarios of a devloper and data scientist


# Example 1: Create a database
# The following example creates a new database using the CREATE DATABASE command.   
# SQL
# CREATE DATABASE database_name;

# Example 2: Create a table
# The following example creates a new table using the CREATE TABLE command.
# SQL
# CREATE TABLE table_name (
#     column1 datatype,
#     column2 datatype,
#     column3 datatype
# );

# Example 3: Insert records
# The following example inserts records into a table using the INSERT command.
# SQL
# INSERT INTO table_name (column1, column2, column3)
# VALUES (value1, value2, value3);

# Example 4: Update records
# The following example updates records in a table using the UPDATE command.
# SQL
# UPDATE table_name
# SET column1 = value1, column2 = value2
# WHERE condition;

# Example 5: Delete records
# The following example deletes records from a table using the DELETE command.
# SQL
# DELETE FROM table_name
# WHERE condition;

# Example 6: Select records
# The following example selects records from a table using the SELECT command.
# SQL
# SELECT column1, column2
# FROM table_name
# WHERE condition;

# Example 7: Create an index
# The following example creates a new index using the CREATE INDEX command.
# SQL
# CREATE INDEX index_name
# ON table_name (column1, column2);

# Example 8: Create a view
# The following example creates a new view using the CREATE VIEW command.
# SQL
# CREATE VIEW view_name AS
# SELECT column1, column2
# FROM table_name
# WHERE condition;

# Example 9: Create a trigger
# The following example creates a new trigger using the CREATE TRIGGER command.
# SQL
# CREATE TRIGGER trigger_name
# BEFORE INSERT ON table_name
# FOR EACH ROW
# BEGIN
#     -- trigger logic goes here
# END;

# Example 10: Create a stored procedure
# The following example creates a new stored procedure using the CREATE PROCEDURE command.
# SQL
# CREATE PROCEDURE procedure_name
# AS
# BEGIN
#     -- procedure logic goes here
# END;

# Example 11: Create a user
# The following example creates a new user using the CREATE USER command.
# SQL
# CREATE USER user_name
# IDENTIFIED BY password;

# Example 12: Grant permissions
# The following example grants permissions to a user using the GRANT command.
# SQL
# GRANT permission1, permission2

# Example 13: Revoke permissions
# The following example revokes permissions from a user using the REVOKE command.
# SQL
# REVOKE permission1, permission2

# Example 14: Commit a transaction
# The following example commits a transaction using the COMMIT command.
# SQL
# COMMIT;

# Example 15: Rollback a transaction
# The following example rolls back a transaction using the ROLLBACK command.
# SQL
# ROLLBACK;

# Example 16: Save a transaction
# The following example saves a transaction using the SAVEPOINT command.
# SQL
# SAVEPOINT savepoint_name;

# Example 17: Create schema
# The following example creates a new schema using the CREATE SCHEMA command.
# SQL
# CREATE SCHEMA schema_name;

# Example 18: Alter table
# The following example alters a table using the ALTER TABLE command.
# SQL
# ALTER TABLE table_name
# ADD column_name datatype;

# Example 19: Drop table
# The following example drops a table using the DROP TABLE command.
# SQL
# DROP TABLE table_name;

# Example 20: Truncate table
# The following example truncates a table using the TRUNCATE TABLE command.
# SQL
# TRUNCATE TABLE table_name;

# Example 21: Create sequence
# The following example creates a new sequence using the CREATE SEQUENCE command.
# SQL
# CREATE SEQUENCE sequence_name
# START WITH 1
# INCREMENT BY 1;

# Example 22: Drop sequence
# The following example drops a sequence using the DROP SEQUENCE command.
# SQL
# DROP SEQUENCE sequence_name;

# Example 23: Create synonym
# The following example creates a new synonym using the CREATE SYNONYM command.
# SQL
# CREATE SYNONYM synonym_name
# FOR table_name;

# Example 24: Drop synonym

