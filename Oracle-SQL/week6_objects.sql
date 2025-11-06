// DEFINITION: views - is a logical table, logically repressents subsets logical table based on physical data, it doesn't contain data itself, it is stored as select select statement, it does not store data physically
// Advantages of views: restricting data access to physical table, to make complex queries easy, ... [another two ones] 
// simple views contain one, do not contain function, groups does not present, DML
// complext views, contain one or more, contain functionsm grups, do not contain DML
CREATE VIEW empvu80
AS  SELECT employee_id, last_name, salary FROM Employees
    WHERE department_id = 80;
DESCRIBE empvu80

CREATE OR REPLACE VIEW salvu50 (ID_NUMBER, NAME, ANN_SALARY)
AS  SELECT employee_id, last_name, salary * 12 FROM Employees
    WHERE department_id = 50
DESCRIBE salvu50

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
// can not be removed rows because it contain several tables, you can imagine it as trying remove from one physical table, it is impossible because data in another table do not present
// what if we add new rows will it show new rows in view?
// how we can remove VIEW?
CREATE OR REPLACE VIEW empvn1
AS  SELECT DISTINCT first_name, employee_id
    FROM employees // it is not simple VIEW because we have DISTINCT we can not determine particular row
// to serve the internet why we can not remove rows in complex VIEW

CREATE VIEW empvn2
AS  SELECT employee_id, last_name
    FROM employees
    WHERE ROWNUM <= 3 // ROWNUM counting as complext VIEW thereby we can not remove rows in VIEW, why? 


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
// can I use simultaneously WITH CHECK OPTION and READ ONLY in VIEW
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

