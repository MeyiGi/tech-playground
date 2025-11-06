SELECT * FROM Employees

// QUESTIONS
// what is explicit and inplicit data type conversions
// how it is working data type conversions in NVL2(a, b, c) in the output [implicit]
// what is DML, DCL and DDL
// what is transaction
// containing of transactions ?
// what is commit and rollback keywords
// what is permanent in SQL
// what if I don't define values in insert into where can be null or not etc
// what is read Consistency
// kilitlemek ne demek
// FOR UPDATE Clause in a SELECT Statement

// DEFINITION
// Transaciton - is premise of one or more database operations (such as INSERT, UPDATE or DELETE) treated as single, indivisable unit of work

// <<INSERT statement>>
INSERT INTO Users (user_id, username, email, password_hash, full_name, bio, created_at)
VALUES (
    1002, -- new unique user_id
    'knitas_kate2',
    'kate@exasdampled2.com',
    'hash571mnasdo',
    'Kate Austenasd',
    'Knitting sweatasders, scarves, and everything in between.',
    SYSDATE
);

INSERT INTO Users (user_id, username, email, password_hash, full_name, bio, created_at)
VALUES (
    &user_id, -- new unique user_id
    '&username',
    '&email',
    '&hashpass',
    '&full_name',
    '&description',
    SYSDATE
);

INSERT INTO Users (user_id, username, email, password_hash, full_name, bio, created_at)
SELECT 1004, 'kotokbas', 'kotokbas@gmail.com', 'dasd', full_name, bio, created_at FROM Users
WHERE user_id = 37
// make inserting bunch with select
// take a look at another inserts
// how I can copy table to another one


SELECT * FROM Employees
// update
UPDATE Employees
SET HIRE_DATE = 124
WHERE employee_id = 1

UPDATE Employees
SET HIRE_DATE = 124, DEPARTMENT_ID = 10000
WHERE employee_id = 1

UPDATE Employees e
SET (job_id, salary) = (
    SELECT job_id, salary FROM Employees
    WHERE employee_id = 10
)
WHERE e.employee_id = 1
// what if select statement returning more than one record
// how to make bunch updating in SQL


SELECT * FROM Employees
// DELETE stament
DELETE FROM Employees
WHERE employee_id = 8

DELETE FROM Employees
WHERE employee_id = 12412u4

DELETE FROM Employees
WHERE JOB_ID IN (
    SELECT JOB_ID FROM Employees
    WHERE JOB_ID LIKE 'HR%'
)

// TRUNCATE - removes all rows from a table <--- (DDL)


// database transactions: start and end
// DDL is autocommit
// commit is basically saving the updated, added, removed results and can not be backup
// rollback you can imagine as "goto" in c++ undertand it as savepoint if code crush or power off laptop etc
// when we made commit all savepoints are erased

DELETE FROM Employees;
ROLLBACK;

SELECT COUNT(*) FROM Employees; // why fucking rollback not working



///////////////////////////////////////////////////////////



// DEFINITION: DML stands for Data Manupulation Language in SQL commands that used to manipulate the data stored in database tables [inserting, updating, deleting or [retrieving]]
// DEFINITION: Transaction is a single or more sql operations that are executed as one single unit

// INSERT used to add new row(s) to the table
INSERT INTO departments(department_id, department_name, manager_id, location_id)
VALUES (280, 'Public Relations', 100, 1700);
INSERT INTO departments(department_id, department_name, manager_id, location_id)
VALUES (281, 'Public Relations', 100, '1700'); // implicit conversion working in INSERT operation
INSERT INTO departments(department_id, department_name, manager_id, location_id)
VALUES (281, 'Public Relations', 100, '1700', 123); // number or args have to be equal

// UPDATE used to change particular informations about row(s), col(s)
UPDATE employees 
SET department_id = 50 
WHERE employee_id = 113; // if we remove WHERE clause change will be implemented to all cols

SELECT * FROM Employees

UPDATE Employees
SET (job_id, salary) = (
    SELECT job_id, salary FROM Employees
    WHERE employee_id = 205
)
WHERE employee_id = 113 // it have to been worked but because of contraints it won't work in my case

// DELETE used to removing row(s)
DELETE FROM Departments 
WHERE department_name = 'Finance'; 

DELETE FROM Departments // will remove all data from table

// TRUNCATE is autocommit, in contrast, DELETE is not autocommit so we can not use TRUNCATE with ROLLBACK etc

// DEFINITION: DCL stands for Data controlling language in sql which controll access in the database
// DEFINITION: TRANSACTION consist with one of constitute DML statementor DDL statement or with one DCL statement
// with COMMIT and ROLLBACK we can ensure data consistency 
// ROLLBACK used to make undo all changes in transaction 
// autocommits occur in DDL, DCL and when we are leaving sql workspace, while ROLLBACK occurs in system failer etc
// Before COMMIT or ROLLBACK data can be recovered, previewed but won't affect to another peoples viewing it is changed only your session
// DEFINITION: is a single DML statement fails during execution, only that statement will be rolled back
// Read Consistency means when changes was made with one user won't confict with changes made by another user, with another words when one user making SELECT * FROM ... and it is taking around 2 minutes and within 2 minutes was made changes with another user it will not affect to already started SELECT statement
