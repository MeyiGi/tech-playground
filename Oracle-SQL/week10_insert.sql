MERGE INTO copy_emp c
USING (SELECT * FROM Employees) e
ON (c.employee_id = e.employee_id)
WHEN MATCHED THEN
UPDATE SET
c.first_name = e.first_name
c.last_name = e.last_name
DELETE WHERE (commision_pct IS NOT NULL)
WHEN NOT MATCHED THEN
INSERT VALUES(e.employee_id, e.first_name...)

CREATE TABLE employees_5 (
  employee_id NUMBER,
  first_name  VARCHAR2(50),
  salary      NUMBER
);

DROP TABLE employees_3

INSERT INTO employees_5 (employee_id, first_name, salary)
    SELECT employee_id, first_name, salary FROM employees
    
UPDATE employees_3 SET salary = salary * 1.3
WHERE employee_id = 107

COMMIT;
SELECT * FROM employees_3
WHERE employee_id = 107

SELECT salary FROM employees_5
VERSIONS BETWEEN SCN MINVALUE AND MAXVALUE
WHERE employee_id = 107