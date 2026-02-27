SELECT * FROM Employees

// QUESTIONS
// what is explicit and inplicit data type conversions
// how it is working data type conversions in NVL2(a, b, c) in the output
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