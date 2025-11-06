SELECT USER_ID, UPPER(FULL_NAME) god, BIO, CONCAT('HELLO', 'HELLO') AS "JOJOJO" FROM Users
WHERE LOWER(FULL_NAME) = LOWER('Kate Austen')

SELECT FULL_NAME FROM Users
WHERE INSTR(FULL_NAME, 'n') = LENGTH(FULL_NAME)

SELECT SYSDATE FROM dual
SELECT NEXT_DAY(SYSDATE, 'FRIDAY') FROM dual
SELECT ROUND(SYSDATE, 'DAY') FROM dual

SELECT FULL_NAME FROM Users
WHERE SUBSTR(FULL_NAME, LENGTH(FULL_NAME)) = 'n'

SELECT ROUND(5231235.51513, -1000000000000000) FROM DUAL

SELECT * FROM Users



// DEFINITION: there 2 types of functions: single row(return one result for one row) and multiple row(return one result per set of rows) functions
// DEFINITION: single row functions manipulate data return one result for one row, may convert data type, can be nested 
// DEFINITION: character function: there two types, case-conversion and character-manipulation
// DEFINITION: character function case conversion: LOWER, UPPER, INITCAP
// DEFINITION: character function character-manipulation:

SELECT CONCAT('HELLO', 'WORLD', 'HOHOHO') FROM dual // CONCAT can take only two arg
SELECT SUBSTR('HELLO WORLD!', 0, 4) FROM dual // There no difference between 0 and 1, 
SELECT SUBSTR('HELLO WORLD!', -13, 3) FROM dual // There no difference between 0 and 1,
SELECT INSTR('hehehel', 'elasd') FROM dual // it is like find index
SELECT LPAD('hello', 10, '&') FROM dual // there also another RPAD working logic almost similar
SELECT REPLACE('HELLO', 'H', 'porno') FROM dual
SELECT TRIM('H' FROM 'dHELLOH') FROM dual

// Numeric functions: 
// ROUND: round to a specified decimal
SELECT ROUND(75912047.719238) FROM Dual // by default ROUND 0
SELECT ROUND(75912047.719238, 2) FROM Dual
SELECT ROUND(75912047.719238, -1) FROM Dual // can be negative number in round
// TRUNC: truncates values to a specidied decimal
SELECT TRUNC(75912047.719238, 2) FROM Dual
SELECT TRUNC(75912047.719238, 2.6321) FROM Dual // when if float number it is taking number before 2. only
SELECT TRUNC(75912047.719238, -1) FROM Dual // can be negative number it is like making zero to decimal
// MOD: like % operation in programming language
SELECT 1000 % 100 FROM dual // as you can see % not working in SQL
SELECT MOD(1000, 100) FROM dual
SELECT MOD(1000, 100.5) FROM dual

// Default display dates in Oracle Database is DD-MON-RR
SELECT SYSDATE FROM DUAL
SELECT first_name, (SYSDATE - hire_date) FROM Employees // returning days
SELECT first_name, (SYSDATE - hire_date) / 365 FROM Employees // returning years

// Date Manipulation Functions
// MONTHS_BETWEEN(args1, args2)
// NEXT_DAY(args, day_of_week) like 'FRIDAY'
// LAST_DAY(args) returning date where day part is last of month
// ADD_MONTHS(arg1, num) adding num months to arg1
SELECT 
    employee_id , 
    hire_date, 
    ((SYSDATE - hire_date) / 365)  * 12,
    ADD_MONTHS(hire_date, 6),
    NEXT_DAY(hire_date, 'FRIDAY'),
    LAST_DAY(hire_date)
FROM Employees
WHERE ((SYSDATE - hire_date) / 365) * 12 > 150


// can I use alias in where from select place?
SELECT 20 AS Age FROM dual
WHERE Age = 20 // we can not
// but alias working in HAVING and ORDER BY

// when we ROUND or TRUNC the date day is always becoming 1 
SELECT SYSDATE, ROUND(SYSDATE, 'MONTH'), ROUND(SYSDATE, 'YEAR'), TRUNC(SYSDATE, 'MONTH'), TRUNC(SYSDATE, 'YEAR') FROM Dual

 
--1)arithmetic operation
--2)concatination operator
--3)comparison condition
--4)IS [NOT] NULL, [NOT] LIKE
--5)[NOT] BETWEEN
--6)not equal to
--7)NOT
--8)AND
--9)OR