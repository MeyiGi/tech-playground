// DEFINITION: views - is a logical table, logically repressents subsets logical table based on physical data, it doesn't contain data itself, it is stored as select select statement, it does not store data physically
// Advantages of views: restricting data access to physical table, to make complex queries easy, ... [another two ones] 
// simple views contain one, do not contain function, groups does not present, DML
// complext views, contain one or more, contain functionsm grups, do not contain DML
CREATE OR REPLACE VIEW empvu80
AS  SELECT employee_id, last_name, salary FROM Employees
    WHERE department_id = 80;

    
    
DESCRIBE empvu80
SELECT COUNT(*) FROM empvu80 // inserted or removed in physical table will affect view

INSERT INTO Employees

CREATE OR REPLACE VIEW empvu80 (id_number, hoho, hokotok, dsa) // if number of alias more than SELECT columns it will cause an error
AS  SELECT employee_id, last_name, salary FROM Employees
    WHERE department_id = 80;
CREATE OR REPLACE VIEW empvu80 (id_number, hoho) // same as before it will cause an error
AS  SELECT employee_id, last_name, salary FROM Employees
    WHERE department_id = 80;
DESCRIBE empvu80

UPDATE empvu80
SET salary = salary + 5000 // can be modified because empvu80 is simple view

// name of columnns, CREATE OR REPLACE allows us to recreate view if it hadn't be there it would cause an error
CREATE OR REPLACE VIEW salvu50 (ID_NUMBER, NAME, ANN_SALARY) 
AS  SELECT employee_id, last_name, salary * 12 FROM Employees
    WHERE department_id = 50;
DESCRIBE salvu50    

UPDATE salvu50
SET salary = salary / 12 // it won't work because there expression salary * 12



SELECT * FROM salvu50 // to retrieve data from VIEWS
// in order to modify view we need add "CREATE OR REPLACE" to the VIEW
// make modifications using UPDATE or INSERT
// what will happen if we remove row from 
// make updating all cols in the home
// AVG similar statements leading to complex VIEW
// add another columns with MIN, MAX, AVG without grouping by

CREATE OR REPLACE VIEW dept_sum_vu
(NAME, MINSAL, MAXSAL, AVGSAL)
AS SELECT 
    d.department_name, 
    MIN(e.salary),
    MAX(e.salary),
    AVG(e.salary)
FROM Employees e 
LEFT JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name

// this was in blackboard in the classroom 
CREATE OR REPLACE VIEW empvn (department, min_salary)
AS  SELECT department_id, MIN(salary)
    FROM Employees
    GROUP BY department_id
    
DELETE FROM empvn
WHERE department_id = 100 // why not department???

CREATE OR REPLACE VIEW empv AS
SELECT DISTINCT(department_id), first_name FROM Employees
CREATE OR REPLACE VIEW empv (hoho, kotok) AS 
SELECT first_name, salary * 12 FROM Employees
SELECT * FROM empv
DELETE FROM empv
WHERE department_id = 90 // not working
// we can not use remove DML operation on JOIN, GROUP, ROWNUM and AGGREGATE FUNCTIONS
// can not be removed rows because it contain several tables, you can imagine it as trying remove from one physical table, it is impossible because data in another table do not present
// what if we add new rows will it show new rows in view? yes
// how we can remove VIEW? DROP view view
CREATE OR REPLACE VIEW empvn1
AS  SELECT DISTINCT first_name, employee_id
    FROM employees // it is not simple VIEW because we have DISTINCT we can not determine particular row
// to serve the internet why we can not remove rows in complex VIEW

CREATE VIEW empvn2
AS  SELECT employee_id, last_name
    FROM employees
    WHERE ROWNUM <= 3 // ROWNUM counting as complext VIEW thereby we can not remove rows in VIEW, why? 


// group functions, GROUP BY, JOIN, DISTINCT, ROWNUM --> Can not be implemented REMOVE
// group functions, GROUP BY, JOIN, DISTINCT, ROWNUM, expression --> Can not be implemented MODIFY
// group functions, GROUP BY, JOIN, DISTINCT, ROWNUM, expression, NOT NULL in TABLE --> Can not be implemented ADD

SELECT employee_id, last_name
FROM employees
WHERE ROWNUM <= 3 
ORDER BY salary DESC; // ordering will work only after WHERE ROWNUM <= 3 so it do not guarantee will take data in sorted order
// we can use DML operations on simple views
// we can not remove rows in VIEW if contains: group functions, GROUP BY, DISTINCT, ROWNUM
// when we remove row or data in view we are removing data also in physical table
// what if instead of ROWNUM we will use LIMIT statement will it allow to remove row?
// can I use VIEW to the CTE?
// defined by expression cols can not modified in VIEW (salary * 12) but can be removed
// NOT NULL I fucking didn't understand what does it mean can not be modified
CREATE OR REPLACE VIEW empvu20
AS  SELECT
    FROM employees
    WHERE department_id = 20;
    WITH CHECK OPTION CONTRAINT empvu20 ck; // whenever we UPDATE or INSERT it will every time check WHERE department_id = 20;
// how I can add another type of CONTRAINT???

// when we add READ_ONLY it will forbid using DML statements but it is saying in presenations SELECT in DML operations ???? -> it turns out to lie SELECT statement is DQL statement (data querying language)
// can I use simultaneously WITH CHECK OPTION and READ ONLY in VIEW --> No
// fucking FORCE and NOFORCE what does it mean in VIEW?





WITH names AS (
    SELECT first_name FROM Employees
)
SELECT * FROM names // what the difference between WITH and VIEWS?
// difference between CTE and VIEWS is CTE storing temporarily in contrast VIEWS permanent
// DEFINITION: table - is a basic unit of storage
// DEFINITION: sequence - ????
// DEFINITION: index - to improve performance data retrieval process
// DEFINITION: synonym - gives alternative name to objects
// DEFINITION: sequence is like automatic generator of nubmers unique primary key


// 
CREATE SEQUENCE sequence
    [INCREMENT BY N]
    [START WITH N]
    [(MAXVALUE N | NOMAXVALUE)] // 10^26
    [(MINVALUE N | NOMINVALUE)] // if we do not use minvalue it is nominvalue by default
    [(CYCLE | NOCYCLE)] // it enables generation process even if all used it is like circular array
    [(CACHE N | NOCACHE)]; // cache mean how many can be saved in cache N quantity
    
CREATE SEQUENCE dept_deptid_seq 
    INCREMENT BY 10
    START WITH 120
    MAXVALUE 9999 // WHAT IF WE DIDN'T SPECIFY? it will be 10^26
    NOCACHE
    NOCYCLE // Why we need use this? we must to keep all parameters
    
// how to use sequence?? By using Pseudocolumns
// NEXTVAL -> returns the next available sequence value
// CURRVAL -> returns the current value

INSERT INTO departments(department_id, departent_name, location_id) 
VALUES (dept_deptid_seq.nextval, 'support', 2500)
    
// if we want to insert a row but max length is less? what will happen? it will cause error in such case we need modify sequence MAXVALUE
// if system crases or rollback occurs in sequence, that sequence will be lost [rollback if there was 100 at the currval it will be removed and nextval will be 101 not optimal]
// they are like pointers
// what if we use sequence in two or more tables what will happen? it is bad but applicable

// to modify sequence we are using ALTER

ALTER SEQUENCE dept_deptid_seq
    INCREMENT BY 20
    MAXVALUE 999999
    NOCACHE
    NOCYCLE // what if I change positions NOCACHE <-> NOCYCLE what happens? we must ensure all values in right places

// we can not change START WITH part by using ALTER SEQUENCE statement we have only recreating sequence option for that
// what if we update MAXVALUE to less one? error 100 -> 99 
// here is dropping statemtn
DROP SEQUENCE dept_deptid_seq;

// DEFINITION: index object - is database object to improve performance some queries is a schema object can be used by Oracle BY using pointer dependent on a table, can be maintenad automatically by Oracle or by User end
// how oracle table does the search -> with index and without: by using index it will find wor_id and directly retrieve data in contrast when we retriving value without index it will look at them one by one, so indexes much better by using binary search etc directly retrieving data
// we can imagine it as book pages with their page numbers or without them
// it can be created or dropped in any time and will not affect table, we are adding indexes to specific column we are not creating new column
// we can create it with two way implicitly or explicitly 
// implicitly unique index created automatically when we define PRIMARY KEY or UNIQUE
CREATE [UNIQUE][BITMAP]INDEX index // unique means uniques, bitmap used for low unique values count like gender
ON table (column[, column]...);

CREATE INDEX emp_last_name_idx
ON employees(last_name);


// must we put index to each columns if it is so useful?
// we need use index if contains large range of value or a lot null values or one or more columns used frequently on WJERE claue or a join

// we do not need use INDEX for column that a little bit used
// table is small or updated frequently or the indexed columns are referenced as part of an expression[like expressions salary * 12 / 23 + 2134]
// in order to remove index we are using our loving DROP
DROP INDEX index
DROP INDEX emp_last_name_idx; // to drop an index we must be the owner of the index or have the DROP ANY INDEX privilage, we can not update indexes
// when we made DML operation we have to make updating table it is bad situationship for table


// DEFINITION: synonym - in order to give alternative name to the object
// why we need it? we know in sql there can be different users,i want retrieve data for different users table for example we wanna retrieve Employees with another user
// it creates another name for an object 
CREATE [PUBLIC] SYNONYM synonym // PUBLIC means assecible to all users
FOR object; 
// instead os saying Bob.departments we can create a synonym bdep also it will hep shorten lenghy object names

CREATE SYNONYM d_sum
FOR dept_sum_vu; // we are renaming dept_sum_vu and can use it, can be used for all objects

CREATE SYNINYM a_dept
FOR alice.departments

// quiz 1. False

// 





