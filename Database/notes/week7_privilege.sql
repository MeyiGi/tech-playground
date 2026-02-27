// database security can be classified in two system security and data security
// system securyty control access to data and use of data like username and password
// data security securing the data inside the table inside the database

// priviliges it means write in sql to particular ....
// system priviliges performing particular action in database
// object privilieges manipulate content of object in database
// database administrator have all priviligies, also can give priviligies to the user, user can give priviliges to another users and so on
// schemas is a collection of objects owned by database user

// there more than 200 privilieges are available system privilieges
// tasks such as creating, removing users removing backup tables

// SYSTEM_PROVILAGE_MAP we can see different types of privilieges

// creating user
CREATE USER user
IDENTIFIED BY password; 

CREATE USER demo
IDENTIFIED BY demo // this demo user do not have any priviligies, password is case sensitive
// TO GRANT priviliges
GRANT privilege [, privilege...]
TO USER [, user] role, PUBLIC...] // with PUBLIC we mean giving privilige to all users
// system privilege examples
CREATE SESSION
CREATE TABLE
CREATE SEQUENCE
CREATE VIEW
CREATE PROCEDURE

GRANT   create session, create table, 
        create sequence, create view 
TO demo
// DBA stands for database administrator
// difference between role and user 
// role is group of user for example "Manager" and we give privilige to manager all managers will grant privilege, we can use several roles users can be assigned to several roles

CREATE ROLE manager
GRANT create table, create view
TO MANAGER

GRANT MANAGER TO  demo // what if we make operation with manager but nobory is granted to manager role
SELECT * FROM dba_sys_privs
// Changing passowrd
ALTER USER demo
IDENTIFIED BY new_password // can I use numbers

// object privileges: ALTER, DELETE, INDEX, INSERT, REFERENCES(foreighn key, if we provide REFERENCES privilege it means user can work with FOREIGN KEY), SELECT, UPDATE


GRANT   object_priv[(columns)]
ON      ojbect // we are giving privelege to this object
TO      (user|role|PUBLIC)
[WITH GRANT OPTION]; // to grant a object to the other users

GRANT UPDATE (DEPARTMENT_NAME, location_id)
ON            departments
TO            demo, manager;

GRANT select, insert
ON departments
TO demo
WITH GRANT OPTION; // demo can give this privelege to other users

GRANT select
ON alice.departments // departments table in alice user
TO PUBLIC // all user can use select to alice.departments table, PUBLIC assess can give only DBA

REVOKE [privilege [, privilege...]|ALL]
ON object
FROM {user[, user...]|role|PUBLIC}
[CASCADE CONSTRAINTS] // when we remove grant from one user that granted users with this user will be revoked like CASCADE in foreigh key it is good when we use it
// maybe I am wrong I need research it

REVOKE select, insert
ON departments
FROM demo // we are removing select and insert privelegies from demo user
// WITH ADMIN OPTION --> if we use this clause we are giving system privelege we need to be very careful using it sooooooo in such case two DBA?

quiz a. true, b. false[because only DBA can create role], c. true, d. true 

