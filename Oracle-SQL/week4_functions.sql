SELECT * FROM Posts;

SELECT username, TO_CHAR(created_at, 'DD "of" Month YYYY HH:MI:SS') AS created_date FROM Users;
SELECT first_name, TO_CHAR(hire_date, 'DD "of" Month MONTH mon yyyy DY DAY DD HH:MI:SS') AS created_date FROM Employees;

SELECT TO_CHAR(created_at, '$99,999.00') FROM Users

SELECT username, TO_CHAR(created_at, 'DD-Mon-YYYY') FROM Users
WHERE TO_DATE(TO_CHAR(created_at, 'DD-Mon-RR'), 'DD-Mon-RR') < '01-Jan-25';

SELECT UPPER(CONCAT(SUBSTR(username, 1, 7), '_KOTOK')) FROM Users;

SELECT TO_NUMBER(12312) FROM DUAL

SELECT TO_CHAR('HELLO') FROM DUAL

SELECT NVL(image_url, 'Пошел нахуй!') FROM Posts

SELECT ('hoho' * 3) FROM DUAL

SELECT NVL2('Пошел нахуЙ', NVL2('ШЛА НАХУЙ', 809, 999), 321) FROM DUAL // it is like ternary operation [ condition ? ho : jo ]
SELECT NVL2(image_url, 'Пошел нахуй!', TO_DATE('03-JAN-2025')) FROM Posts

SELECT NULLIF(123, 'DSAD') FROM DUAL 

SELECT COALESCE(NULL, NULL, NULL, 'HOHOHO', NULL, NULL, NULL, 123, NULL, NULL, NULL, NULL) FROM DUAL
SELECT COALESCE(NULL, NULL, NULL, 'HOHOHO', NULL, NULL, NULL, 'HOHOHO123', NULL, NULL, NULL, NULL) FROM DUAL
SELECT COALESCE('hello mother fucker', NULL, NULL, 'HOHOHO', NULL, NULL, NULL, 'jooj', NULL, NULL, NULL, NULL) FROM DUAL
SELECT COALESCE('HOHOHO', '123', '567') FROM DUAL


SELECT 
    CASE 123 
        WHEN LENTH('hoho') > 3 THEN 10
        ELSE 3
    END AS jpjp
FROM DUAL
// CONDITIONS AND RETURN TYPES SHOULD BE SIMILAR TO EACH OTHERS


// DEFINITION: there two type of data conversion Implicit(automatically will be converted with SQL) and Explicit(we need make data conversion)
SELECT first_name, hire_date, TO_CHAR(hire_date, 'YYYY-YEAR') FROM Employee
SELECT first_name, hire_date FROM Employees
WHERE hire_date > '01^Jan^5'


