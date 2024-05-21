--Task1

SELECT name
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);

--Task2

SELECT department_id, 
       (SELECT name 
        FROM employees AS e2 
        WHERE e1.department_id = e2.department_id 
        ORDER BY salary DESC 
        LIMIT 1) AS highest_earner
FROM employees AS e1
GROUP BY department_id;

--Task3

SELECT name
FROM employees
WHERE department_id IN (1, 3);

--Task4

SELECT DISTINCT department_id
FROM employees AS e1
WHERE EXISTS (
    SELECT 1
    FROM employees AS e2
    WHERE e1.department_id = e2.department_id
      AND e2.salary > 5500
);

--Task5

SELECT DISTINCT department_id
FROM employees AS e1
WHERE NOT EXISTS (
    SELECT 1
    FROM employees AS e2
    WHERE e1.department_id = e2.department_id
      AND e2.salary < 4500
);


