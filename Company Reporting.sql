CREATE TABLE staff_hierarchy (
 employee_id INT PRIMARY KEY,
 employee_name VARCHAR(100),
 manager_id INT,
 designation VARCHAR(100)
);
INSERT INTO staff_hierarchy VALUES
(1, 'Raj Malhotra', NULL, 'CEO'),
(2, 'Meera Shah', 1, 'CTO'),
(3, 'Vikram Rao', 1, 'Sales Director'),
(4, 'Aman Khan', 2, 'Engineering Manager'),
(5, 'Sara Ali', 2, 'Data Manager'),
(6, 'Rohit Das', 4, 'Developer'),
(7, 'Priya Singh', 4, 'Developer'),
(8, 'Kabir Ahmed', 5, 'Data Engineer'),
(9, 'Neha Rao', 5, 'Data Analyst'),
(10, 'Imran Sheikh', 3, 'Sales Manager'),
(11, 'Pooja Jain', 10, 'Sales Executive');
SELECT e.employee_name AS employee,
       m.employee_name AS manager
FROM staff_hierarchy e
LEFT JOIN staff_hierarchy m
ON e.manager_id = m.employee_id;
SELECT employee_name, designation
FROM staff_hierarchy
WHERE manager_id = 1;
SELECT employee_name, designation
FROM staff_hierarchy
WHERE manager_id = 2;
SELECT *
FROM staff_hierarchy
WHERE manager_id IS NULL;
SELECT e.employee_name,
       e.designation,
       m.employee_name AS manager_name
FROM staff_hierarchy e
LEFT JOIN staff_hierarchy m
ON e.manager_id = m.employee_id;
SELECT m.employee_name AS manager,
       COUNT(e.employee_id) AS total_reports
FROM staff_hierarchy m
JOIN staff_hierarchy e
ON m.employee_id = e.manager_id
GROUP BY m.employee_id, m.employee_name;
SELECT m.employee_name AS manager,
       COUNT(e.employee_id) AS total_reports
FROM staff_hierarchy m
JOIN staff_hierarchy e
ON m.employee_id = e.manager_id
GROUP BY m.employee_id, m.employee_name
HAVING COUNT(e.employee_id) > 1;
SELECT e.employee_name AS developer,
       m.employee_name AS manager
FROM staff_hierarchy e
LEFT JOIN staff_hierarchy m
ON e.manager_id = m.employee_id
WHERE e.designation = 'Developer';
SELECT e.employee_name,
       m.employee_name AS manager
FROM staff_hierarchy e
LEFT JOIN staff_hierarchy m
ON e.manager_id = m.employee_id
WHERE e.employee_name = 'Pooja Jain';
WITH RECURSIVE EmployeeHierarchy AS
(
    SELECT employee_id,
           employee_name,
           manager_id,
           designation,
           1 AS level
    FROM staff_hierarchy
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.employee_id,
           e.employee_name,
           e.manager_id,
           e.designation,
           h.level + 1
    FROM staff_hierarchy e
    JOIN EmployeeHierarchy h
    ON e.manager_id = h.employee_id
)
SELECT *
FROM EmployeeHierarchy;






