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
