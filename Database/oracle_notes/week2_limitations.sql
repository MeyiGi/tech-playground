SELECT  last_name FROM Employees
WHERE last_name = "Whalen"; // where clause can not use double quotation
SELECT * FROM Employees
SELECT  last_name FROM Employees
WHERE last_name = 'Whalen';
--
--1)Arithmetic operation
--2)Concatination operand
--3)compare operation
--4)IS [NOT] LIKE
--5)[NOT] BETWEEN ... AND ...
--6)not equal to
--7)NOT
--8)AND
--9)OR

SELECT &&name, &id FROM Employees


// DD-MON-RR -> you wonder why instead of YYYY there RR, it is automatically detect which current centure if it RR = 50 it means 1950 in contract RR = 23 means 2023
// DD-MON-YY -> here YY just truncating YYYY to last two digits if it is 80 it means 2080 year
SELECT last_name, employee_id FROM Employees
WHERE employee_id IN (100, 102, '103', 'huy') // implicit conversion is working but huy can not be converted to number

SELECT last_name FROM Employees
WHERE salary < 'h'; // implicitly conversion working in where clause but it is impossible convert h to number

SELECT last_name FROM Employees 
WHERE HIRE_DATE < 'h'; // same case

SELECT last_name FROM Employees
WHERE HIRE_DATE < 1000; // same case

SELECT last_name, salary FROM Employees
WHERE salary BETWEEN 2500 AND 3500  // it is basically 3500 <= salary <= 2500 working inclusively 

 
SELECT last_name, salary FROM Employees
WHERE salary BETWEEN 3500 AND 2500 // it is basically 3500 <= salary <= 2500 working inclusively 

SELECT employee_id, last_name, salary, manager_id FROM Employees
WHERE manager_id IN (100, 101, 201, 23849032, 24321.123) // can not be present another types it is not implicitly

SELECT first_name FROM Employees
WHERE first_name BETWEEN 'A' AND 'C' // they are case sensitive

SELECT first_name FROM Employees
WHERE first_name BETWEEN A AND C // have to be in in single quotation in order to make it workable

SELECT employee_id, last_name, job_id FROM Employees
WHERE job_id LIKE '%SA\_%' ESCAPE '\' //  we can use ESCAPE idetifier to search for the actual % and _ sybmbols

// NOT operator can be used in BETWEEN, IN, LIKE AND NULL

// DEFINITION: Rules of precedence
// 1 Arithmetic operation
// 2 Concatination operator
// 3 Comparison condition
// 4 IS [NOT] NULL, [NOT] NULL
// 5 [NOT ]BETWEEN 
// 6 not equal to
// 7 NOT
// 8 AND
// 9 OR

SELECT * FROM Employees
ORDER BY 2 // this number identify by which column to make order by

SELECT * FROM Employees
ORDER BY 0

SELECT * FROM Employees
ORDER BY 'kotokbas' // won't affect to the corresponding order think about it like nothing doing special

SELECT * FROM Employees
WHERE salary < &salary

SELECT * FROM Employees
WHERE salary + 20 < 10 - '123123'

SELECT &&column_name FROM Employees
WHERE salary < 10000 // it will save what kind of column name I chosen before

SELECT * FROM &Table
SELECT &column FROm Employees

DEFINE employee_num = 200 // like that we can create variable that we can use
SELECT employee_id, last_name, salary FROM Employees
WHERE employee_id = &employee_num
UNDEFINE employee_num // malloc for defining
// by using this we can see in the "Script Output" full query and what kind of substitutional variables was used
SET VERIFY ON 
SELECT employee_id, last_name, salary FROM Employees
WHERE employee_id = &employee_num