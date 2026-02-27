// DEFINITION: relational database is a collection of relation or two dimensional tables
// DEFINITION: primary key columns that main purpos is identifing each row in table
// DEFINITION: foreighn key is a column that creates a link between two tables
// DEFINITION: query is a question of requests for information
// DEFINITION: SQL is ansi standard language for operational relational databases is efficient easy to learn and use with sql we can do everything needed to work with databases, it is query, declarative language, it is designed to only interact with databases
// DEFINITION: DML stands for data manipulation language [update, delete, merge, insert]
// DEFINITION: DDL stands for data definitoin language it is autocommit language
// DEFINITION: projections is when we are retrieving precise columns retrieve specific columns in contract selection retrieving all rows that satisfy condition
// DEFINIITON: writing sql statements: sql statements are not case sensitive, can not be abbreviated, can be in multiple lines, indentation or placing in separate lines are optional used for readibility, sql statement can be terminated with ';' enabling execution of several sql statements 
// DEFINITION: arithmetic expression that was applied at null rows in result will be also null value regardless how many operation was made
SELECT * FROM Employees;

SELECT FIRST_NAME, "hohoho" FROM EMPLOYEES;
SELECT FIRST_NAME, 'hohoho' FROM EMPLOYEES;
SELECT FIRST_NAME AS 'HOHOHO' FROM EMPLOYEES; // why we need AS if we can do everying wihtout them? answer: for readibility
SELECT FIRST_NAME JFKDSLFJDSK from EMPLOYEES;
SELECT first_name || last_name FROM Employees;
SELECT hire_date || comission_pct FROM Employees;
SELECT hire_date || first_name FROM Employees:
SELECT hire_date || hire_date FROM Employees:
SELECT phone_number || salary FROM Employees;
SELECT salary || phone_number FROM Employees; // why it is worked? because of implicit conversion number to string
SELECT hire_date || salary FROM Employees
SELECT 'salary' FROM Employees
SELECT 'hello ' || 'you're pretty' FROM dual
SELECT 'hello ' || q'[you're pretty]' FROM dual 
// DEFINITION: literal character strings can not be with double quates
// DEFINITOIN: alias can not be with single quotes

SELECT first_name || ' ' || last_name || ' ' || hire_date FROM Employees 
SELECT first_name + last_name FROM Employees 

// why in this code one is causing error while another working fine?
SELECT first_name || hire_date FROM Employees;
SELECT hire_date || first_name FROM Employees:
SELECT salary || first_name FROM Employees
SELECT salary || hire_date FROM Employees
SELECT hire_date || salary FROM Employees
SELECT salary huy hoho FROM Employees

DESCRIBE Employees // letting use to know structure of table


--1) arithmetic operations
--2) concatination operator
--3) comparison condition
--4) IS [NOT] NULL, [NOT] LIKE
--5) [NOT] BETWEEN arg1 AND arg2
--6) not equal to
--7) NOT
--8) AND
--9) OR 

