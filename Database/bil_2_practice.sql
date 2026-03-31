-- practice bil 1
-- 1) Department таблицасынан Фирмалар жайгашкан шаарлардын коддорун чыгаргыла. 
SELECT location_id FROM DEPARTMENT;

-- 2) Баардык кызматчылардын тизмесин төмөнкүдөй түрдө чыгаргыла:    W. J. Smith  (substring функциясы колдонулат)
SELECT SUBSTR(last_name, 1, 1) || '. '|| SUBSTR(middle_initial, 1, 1) || '. ' || INITCAP(LAST_NAME) FROM EMPLOYEE;

-- 3) Employee таблицасындагы комиссиялык көрсөткүч айлыктын канча пайызын түзөт.
SELECT 
    last_name, 
    CASE
        WHEN commission IS NOT NULL THEN
            TO_CHAR(ROUND(commission / salary, 4) * 100, 'FM00.00') || '%'
        ELSE '00.00%'
    END AS commission_pct
FROM EMPLOYEE 
ORDER BY commission_pct DESC;

-- 4) Комиссиялык корсөткучү айлыгынан жогору болгон кызматчылардын тизмесин чыгаргыла
SELECT last_name, salary, commission FROM EMPLOYEE
WHERE commission > salary;

-- 5) 'S'тамгасынан башталган кызматчылардын тизмесин чыгаргыла
SELECT last_name FROM EMPLOYEE
WHERE UPPER(last_name) LIKE 'S%'