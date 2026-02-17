// if I have data in temporary table and when I remove data in actual table will that affect to temporary table
// ALTER TABLE statement to add, modify, or drop columns
// how does it look default in table alter
AFTER TABLE table 
ADD (column datatype, [DEFAULT expr]
    [, column_datatype]...);
    
ALTER TABLE table
MODIFY column datatype, [DEFAULT expr]
    [, column_datatype]...);
    
ALTER TABLE table
DROP (column, [, column,]...)

ALTER TABLE dept80
ADD (job_id VARCHAR(9)); // for adding new table, by default is can be null

// DEFINITION: what if we need add NOT NULL column -> we need make default balue

ALTER TABLE dept80
MODIFY (last_name VARCHAR(30)); // to change column datatype, default value, it will affect to future added columns ned default value, we can not decrease the size or if values null or size of specific rows not bigger of specified

ALTER TABLE dept80
DROP (job_id)  // to drop particular column, make contain a data or not, by using it we can remove only one column
// can we use DROP statement for more than 1 column
// if must be at least in table
// primary key can not be removed until cascade option
// it better when we made column 'unused' flag and remove column
// ROLLBACK can not be used

// how to set a unused?
ALTER TABLE <tabke_name
SET UNUSED (column, [, column, ]) // they are making same job

ALTER TABLE table
SET UNUSED column (column, [, column, ]) // they are making same job

ALTER TABLE <table_name>
DROP UNUSED COLUMNS // to remove unsued flag
// ROLLBACK can not be worked with DROP


// working with CONSTRAINTS
ALTER TABLE <TABLE>
ADD [CONSTRAINT <column>] // optional to a name, but by giving a contraint for name it is good
TYPE (<column_name>)

ALTER TABLE emp2
MODIFY employee_id, PRIMARY key

ALTER TABLE emp2
ADD CONSTRAINT emp_mgr_fk   
    FOREIGN KEY (manager_id)
    REFERENCES emp2(employee_id)
    
// WHAT the differences between ADD and MODIFY for contraints

ALTER TABLE emp2
ADD CONSTRAINT emp_dt_fk
FOREIGN KEY (Department_id)
REFERENCES departments(department_id) ON DELETE CASCADE; // departments is a parent, emp2 references to departments, delete them also means DELETE CASCADE

ALTER TABLE emp2 
ADD CONSTRAINT emp_dt_fK
FOREIGN KEY (Department_id)
REFERENCES departments(department_id) ON DELETE SET NULL; // ON DELETE SET NULL child rows value to make it null when parents removed

// if we ommit clauses, oracle does not allow to remove parent row

// differ = ertelemek
ALTER TABLE dept2
ADD CONSTRAINT dept2_id_pk
PRIMARY KEY (department_id)
DEFERRABLE INITIALLY DEFERRED

SET CONTRAINTS dept2_id_pk

ALTER SESSION
SET CONSTRAINTS IMMEDIATE


// page - 16
// difference between INITIALLY DEFERRED and INITIALLY IMMEDIATE
// contraints checked after DML operations
// deferred means like interpreter line by line checking contraints byt IMMEDIATE vise versa
// how does it work? on the end of DML statement 
// what does it mean DEFERRABLE 


// page - 17
// second example: why we need CASCADE? -> it will remove all associate ids to depaartment id, for example that primary key can be in another table as foreign key


// page - 18
ALTER TABLE mepl2
DISABLE CONSTRAINT emp_dt_fk // what does it do
// what if we enable PRIMARY KEY? CASCADE?

// page - 20
if we enable UNIQEU or PRIMARY KEY indexes will be automatically created we must have neccessary privileges 

// page - 21

// page - 23
ALTER TABLE emp2
DROP COLUMN employee_id CASCADE CONSTRAINTS // we are dropping employee_id column and any referenced to primary key will be dropped

ALTER TABLE test1
DROP (col1_pk, col2_fk, col1) CASCADE CONSTRAINT

// PAGE - 24 
ALTER TABLE marketing RENAME COLUMN team_id TO id; // change name of column
ALTER TABLE marketing RENAME CONSTRAINT mktg_pk TO new_mktg_pk; // ranaming name of contraints
// must not conflict new name with other existing ones


// page - 27
// user_indexes - data dictianary


// we can not modify index or update we need make drop and create for that
DROP INDEX upper_dept_name_idx

// when we make drop it will go to recycle bin where it can be recovered later by using 
DROP TABLE dept80 PURGE // by using PURGE we are removing completly from recycle bin also permanently

// flashback table statement let us recover tables to a specific point in time with a single statemnt
// we can  recover table with DROP statement by using FLASHBACK TABLE
// what is SCN

DROP TABLE emp2
SELECT original_name, operation, droptime FROM recyclebin

FLASHBACK TABLE emp2 TO BEFORE DROP
PURGE RECYCLEBIN // cleaning the recyclebin

// temporary table used only in session or transaction after commit rollback is removing
// basket in online store is example for temporary table
// we can use indexes for temporary tables or views

CREATE GLOBAL TEMPORARY TABLE cart(n NUMBER, d DATE) 
ON COMMIT DELETE ROWS; // transaction based, after transaction it will be removed
// what the difference between CTE and these ones
// what does it mean preserve -> WHEN commit appers

CREATE GLOBLA TEMPORARY TABLE today_sales
ON COMMIT PRESERVE ROWS AS
    SELECT * FROM orders
            WHERE order_date = SYSDATE // after transaction it won't be removed it is denoted to the session (preserve), this statement looking interesting what does it mean?
            
// external table it is data is stored outside the database but metadata are storing in database, we can think it like view 
// difference between regular and external are only read only(externel)

CREATE OR REPLACE DIRECTORY emp_dir
AS '/../emp_dir';

GRANT READ ON DIRECTORY emp_dir TO ora_21;

// what if we do not specify ORGANIZATION EXTERNAL
// if we do not specify assess drive ??
// default directory 
// ACCESS OARANETERS how to access external source
// FIRST OF ALL WE NEED CREATE DIRECTORY AND NAME
// NOBADFILE do not create bad file 
// PARALLEL mean more than 1 can be access





////////////////////////////////////////////////////////////////////////////////////

// DEFINITION: ALTER TABLE used to add, modify, drop columns and add default value
CREATE TABLE dept80 AS
SELECT *
FROM employees 
WHERE department_id = 80; //  can not be executed twice or more

ALTER TABLE dept80
ADD (job_id_hoho_jojo VARCHAR2(9)); // can not be added existing columns
SELECT * FROM dept80

ALTER TABLE dept80
MODIFY (job_id VARCHAR(10))

ALTER TABLE dept80
DROP (job_id_hoho, job_id_hoho_jojo) // I can remove simultaneously several columns


// SET UNUSED in order to make a column like removed and later we can drop column
ALTER TABLE table_name
SET UNUSED job_id_hoho_jojo;

ALTER TABLE dept80
DROP UNUSED COLUMN job_id_hoho_jojo

ALTER TABLE dept80 DROP UNUSED COLUMNS;
DESCRIBE employees



ALTER TABLE emp2
MODIFY employee_id PRIMARY KEY


ALTER TABLE emp2
ADD CONSTRAINT manager_for_user
FOREIGN KEY(manager_id)
REFERENCES emp2(manager_id) // it is important can appear in test

ALTER TABLE emp2
ADD CONSTRAINT manager_for_user
FOREIGN KEY Department_id // department_id present in the emp2
REFERENCES Departments(department_id) ON DELETE CASCADE // emp2 is child table when in departments was removed for example "sales" also will be removed employees assigned to "sales" in the emp2

ALTER TABLE emp2
ADD CONSTRAINT manager_for_user
FOREIGN KEY Department_id
REFERENCES departments(department_id) ON DELETE SET NULL // setting null when department was removed in departments table


ALTER TABLE emp2
ADD CONSTRAINT pk2_key
PRIMARY KEY employee_id
// DEFERRABLE INITIALLY DEFERRED // means will check after a transaction
//DEFERRABLE INITIALLY IMMEDIATE // means will check right away after an operation

SET CONSTRAINTS pk2_key IMMEDIATE

ALTER SESSION
SET CONSTRAINTS = DEFERRED

CREATE TABLE emp_new (
    salary NUMBER
    CONSTRAINT sal_ck
    CHECK(salary > 1000)
    DEFERRABLE INITIALLY IMMEDIATE
    bonus NUMBER
    CONSTRAINT bonus_ck
    CHECK (bonus > 0)
    DEFERRABLE INITIALLY DEFERRED
)

ALTER TABLE emp_new
DROP PRIMARY KEY CASCADE

ALTER TABLE emp_new
DISABLE CONSTRAINT bonus_ck
ENABLE CONSTRAINT bonus_ck

ALTER TABLE emp_new
DROP COLUMN employee_id CASCADE CONSTRAINT // linked to the employee_id constraints will be removed

ALTER TABLE emp_new
DROP (col1, col2, col3) CASCADE CONSTRAINT 

ALTER TABLE emp_new
RENAME employee_id TO id

ALTER TABLE emp_new
RENAME CONSTRAINT sal_ck TO huy

FLASHBACK TABLE [table]
TO [SCN_ID]

FLASHBACK TABLE [table]
TO TIMESTAMP(SYS_DATE - INTERVAL '5' MINUTE)

FLASHBACK TABLE [table]
TO BEFORE DROP

// FLASHBACK allow to recover to specific time point restores table with constraint 

CREATE GLOBAL TEMPORARY TABLE cart(n NUMBER, d DATE)
ON COMMIT DELETE ROWS

CREATE GLOBLA TEMPORARY TABLE today_session
ON COMMIT PRESERVE ROWS AS 
    SELECT * FROM employees
    WHERE order_date = SYSDATE
    
    

CREATE OR REPLACE DIRECTORY emp_dir
AS '/.../emp_dir'

GRANT READ ONLY ON DIRECTORY emp_dir TO huy


CREATE TABLE oldemp (
    fname CHAR(25), lname CHAR(25)
)
ORGANIZATION EXTERNAL(
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY emp_dir
    ACCESS PARAMETERS(
        RECORDS DELIMITED BY NEWLINE 
        NOBADFILE
        NOLOGFILE
        FIELDS TERMINATED BY ','
        (
            fname POSITION (1:20) CHAR,
            lname POSITION (21:40) CHAR 
        )
    )
    LOCATION ('emp.dat')
)
PARALLEL 5
REJECT LIMIT 200

CREATE TABLE oldemp (
    employee_id, first_name, last_name
)
ORGANIZATION EXTERNAL (
    TYPE DATAPUMP
    DEFAULT DIRECTORY emp_dir
    LOCATION ('expr1.exp', 'expr2.exp')
)
PARALLEL AS
SELECT employee_id, first_name, last_name FROM Employees




ALTER TABLE emp80
ADD (job_id VARCHAR(8))

ALTER TABLE emp80
MODIFY (job_id VARCHAR(100))


ALTER TABLE emp80
SET UNUSED (job_id)

ALTER TABLE emp80
SET UNUSED COLUMN job_id, job_reference

ALTER TABLE emp80
DROP UNUSED COLUMNS

ALTER TABLE emp80
ADD CONSTRAINT hohohoo
FOREIGN KEY(manager_id)
REFERENCES emp80(employee_id)
ON DELETE CASCADE
ON DELETE SET NULL



ALTER TABLE emp80
ADD CONSTRAINT kokoko
FOREIGN KEY(Department_id)
REFERENCES departments(department_id)








ALTER TABLE emp20
ADD CONSTRAINT kokoko
FOREIGN KEY (Department_id)
REFERENCES department(department_id) ON DELETE CASCADE 
DEFERRABLE INITIALLY DEFERRED
DEFERRABLE INITIALLY IMMEDIATE

SET CONSTRAINTS kokoko IMMEDIATE

AFTER SESSION 
SET CONSTRAINTS kokoko = IMMEDAITE

CREATE TABLE emp80 (
    salary NUMBER
    CONSTRAINT sal_ck
    CHECK(salary > 1000)
    DEFERRABLE INITIALLY IMMEDIATE
    bonus NUMBER
    CONSTRAINT bonus_ck
    CHECK (bonus > 0)
    DEFERRABLE INITIALLY DEFERRED
)

ALTER TABLE emp80
DISABLE CONSTRAINT kokoko CASCADE

ALTER TABLE emp80
DROP COLUMN kokoko CASCADE CONSTRAINTS

ALTER TABLE emp80
DROP (col1, col2, col3) CASCADE CONSTRAINTS

ALTER TABLE emp80 RENAME CONSTRAINT kokoko TO huy


CREATE TABLE emp80 (
    employee_id NUMBER(6) PRIMARY KEY
    USING INDEX (
        CREATE INDEX index_idx_id ON
        emp80(employee_id)
    )
)


CREATE INDEX kojpo
ON departments(UPPER(first_name))

FLASHBACK TABLE employees
TO TIMESTAMP(SYSDATE - INVERVAL '5' MINUTE)
FLASHBACK TABLE employees
TO [SCN_NUMBER]
FLASHBACK TABLE employees
TO BEFORE DROP


CREATE GLOBLA TEMPORARY TABLE hohoho(
    first_name VARCHAR(20), last_name VARCHAR(20)
)
ON COMMIT DELETE ROWS
ON COMMIT PRESERVE ROWS

CREATE GLOBAL TEMPORARY TABLE jojojo
ON COMMIT PRESERVE AS
SELECT employee_id, first_name, last_name FROM employees


CREATE OR REPLACE DIRECTORY emp_dir
AS '/.../hoy'

GRANT READ ONLY ON emp_dir TO alex


CREATE TABLE emp80 (
    fname VARCHAR(25), lname VARCHAR(25)
)
ORGANIZATION EXTERNAL(
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY emp_dir
    ACCESS PARAMETERS(
        RECORDS DELIMITED BY NEWLINE
        NOBADFILE
        NOLOGFILE
        FIELDS TERMINATED BY ', ' (
            fname POSITION(1:20),
            rname POSITION(21:40)
        )
    )
    LOCATION 'emp.dat'

)
PARALLEL 5
REJECT LIMIT 200

CREATE TABLE emp80(
    TYPE DATAPUMP
    DEFAULT DIRECTORY emp_dir
    LOCATION ('hoho1.exp', 'hoho2.exp')
)
PARALLEL AS
SELECT employee_id, first_name, last_name FROM emploees
WHERE department_id = 80




ALTER TALBE employees
DROP PRIMARY KEY CASCADE


CREATE GLOBAL TEMPORARY TABLE emp80(
    fname VARCHAR(25), lname(VARCHAR(25))
)
ON COMMIT DELETE ROWS
ON COMMIT PRESERVE ROWS

ALTER TABLE employees
ADD CONSTRAINT fk_emp
FOREIGN KEY (department_id)
REFERENCES DEPARTMENTS(id) 
ON DELETE SET NULL


CREATE INDEX upper_emp_idx
ON CUSTOMERS(UPPER(last_name))



ALTER TABLE employees
ADD COLUMNS (huy VARCHAR(20))
ALTER RABLE employees
DROP COLUMN huy

ALTER TABLE employees
SET UNUSED (huy)

ALTER TABLE employees
DROP UNUSED

ALTER TABLE employees
ADD CONSTRAINT fk_manager
FOREIGN KEY (manager_id)
REFERENCES employees(employee_id)
ON DELETE CASCADE
ON DELETE SET NULL

ALTER TABLE employees
ADD CONSTRAINT pk_department
PRIMARY KEY (department_id)
DEFERRABLE INITIALLY DEFERRED'
DEFERRABLE INITIALLY IMMEDIATE

SET CONSTRAINTS pk_department IMMEDIATE

ALTER SESSION
SET CONTRAINTS = IMMEDIATE

CREATE TABLE emp80(
    salary NUMBER
    CONSTRAINT sal_ck
    CHECK(salary > 1000)
    DEFERRABLE INITIALLY IMMEDIATE,
    bonus NUMBER
    CONSTRAINT bonus_ck
    CHECK(bonus > 0)
    DEFERRABLE INITIALLY DEFERRED
)


ALTER TABLE employees
DROP PRIMARY KEY CASCADE 


CREATE TABLE emp80(
    employee_id NUMBER PRIMARY KEY
    USING INDEX (
        CREATE INDEX emp_idx_id
        ON emp80(employee_id)
    )
)

CREATE INDEX upper_func
ON departments(UPPER(first_name))


CREATE GLOBAL TEMPORARY TABLE emp80(
    fname VARCHAR(25), lname VARCHAR(25)
)
ON COMMIT DELETE ROWS
ON COMMIT PRESERVE ROWS

CREATE GLOBAL TEMPORARY TABLE emp80(
    employee_id, first_name, last_name
)
ON COMMIT DELETE ROWS AS
SELECT employee_id, first_name, last_name FROM employees    

CREATE OR REPLACE DIRECTORY emp_dir
AS '/.../emp'

CREATE TABLE emp80(
    fname VARCHAR(25), lname VARCHAR(25)
)
ORGANIZATION EXTERNAL(
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY emp_dir
    ACCESS PARAMETERS(
        RECORDS DELIMITED BY NEWLINE
        NOBADFILE
        NOLOGFILE
        FIELDS TERMINATED BY ',' (
            fname POSITION(1:20) CHAR,
            rname POSITION(21: 40) CHAR
        )
    )
    LOCATION('jo.dat')
)
PARALLEL 5
REJECT LIMIT 200

CREATE TABLE emp80 (
    employee_id, first_name, last_name
)
ORGANIZATION EXTERNAL(
    TYPE DATAPUMP
    DEFAULT DIRECTORY emp_dir
    LOCATION('hoho1.exp', 'hoho2.exp')
)
PARALLEL AS
SELECT employee_id, first_name, last_name FROM Employees






ALTER TABLE employees
ADD CONSTRAINT fk_id
FOREIGN KEY(manager_id)
REFERENCES employees(manager_id)
ON DELETE CASCADE
ON DELETE SET NULL


ALTER TABLE employees
ADD CONSTRAINT pk_id
PRIMARY KEY(manager_id)
DEFERRABLE INITIALLY DEFERRED
DEFERRABLE INITIALLY IMMEDIATE

SET CONSTRAINTS pk_id IMMEDIATE
ALTER SESSION
SET CONSTRAINTS pk_id = IMMEDIATE

CREATE TABLE employees (
    salary NUMBER
    CONSTRAINT sal_ck
    CHECK (salary > 1000)
    DEFERRABLE INITIALLY IMMEDIATE,
    bonus NUMBER
    CONSTRAINT bonus_ck
    CHECK (bonus > 0)
    DEFERRABLE INITIALLY DEFERRED
)

ALTER TABLE emp
DROP CONSTRAINT pk_id 
ALTER TABLE emp
DROP PRIMARY KEY CASCADE

ALTER TABLE emp2
DISABLE CONSTRAINT pk_id

ALTER TABLE emp2
ENABLE CONSTRAINT pk_id

ALTER TABLE emp2
DROP COLUMN employee_id CASCADE CONSTRAINTS

ALTER TABLE emp2
RENAME COLUMN|CONSTRAINT pk_id TO new_name


CREATE TABLE employees(
    employee_id NUMBER PRIMARY KEY
    USING INDEX(
        CREATE INDEX hohoho
        ON employees(employee_id)
    )
)

CREATE INDEX upper_func
ON department(UPPER(first_name))

CREATE GLOBAL TEMPORARY TABLE emp(
    fname VARCHAR(25), lname VARCHAR(25)
)
ON COMMIT DELETE ROWS
ON COMMIT PRESERVE ROWS

CREATE GLOBAL TEMPORARY TABLE 

CREATE TABLE expr (
    fname VARCHAR(25), lname VARCHAR(25)
)
ORGANIZATION EXTERNAL(
    TYPE ORACLE_LOADER
    DEFAULT DIRECTORY emp_dir
    ACCESS PARAMETERS(...)
    LOCATION('hoho.dat')
)
PARALLEL 5
REJECT LIMIT 200