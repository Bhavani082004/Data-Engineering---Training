CREATE DATABASE IF NOT EXISTS employee_tracker;
USE employee_tracker;
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    job_role VARCHAR(100),
    joining_date DATE
);
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    clock_in DATETIME,
    clock_out DATETIME,
    attendance_status VARCHAR(20) DEFAULT 'Present',
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);
CREATE TABLE tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    task_name VARCHAR(200) NOT NULL,
    task_date DATE NOT NULL,
    task_status VARCHAR(30) DEFAULT 'Pending',
    hours_spent DECIMAL(5,2) DEFAULT 0,
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);
INSERT INTO employees
(employee_name, department, job_role, joining_date)
VALUES
('Arun', 'IT', 'Developer', '2026-01-10'),
('Priya', 'HR', 'HR Executive', '2026-02-15'),
('Rahul', 'Finance', 'Analyst', '2026-03-01'),
('Meena', 'IT', 'Tester', '2026-04-05');
INSERT INTO attendance
(employee_id, attendance_date, clock_in, clock_out, attendance_status)
VALUES
(1, '2026-10-09', '2026-10-09 09:00:00', '2026-10-09 17:00:00', 'Present'),
(2, '2026-10-09', '2026-10-09 09:15:00', '2026-10-09 17:15:00', 'Present'),
(3, '2026-10-09', NULL, NULL, 'Absent'),
(4, '2026-10-09', '2026-10-09 09:05:00', '2026-10-09 17:05:00', 'Present');
INSERT INTO tasks
(employee_id, task_name, task_date, task_status, hours_spent)
VALUES
(1, 'Develop login page', '2026-10-09', 'Completed', 3.00),
(1, 'Fix application bugs', '2026-10-09', 'Completed', 2.00),
(2, 'Prepare HR report', '2026-10-09', 'Pending', 1.50),
(3, 'Review financial data', '2026-10-09', 'Completed', 2.00),
(4, 'Test application', '2026-10-09', 'In Progress', 4.00);
INSERT INTO attendance
(employee_id, attendance_date, clock_in, attendance_status)
VALUES
(1, CURDATE(), NOW(), 'Present');
UPDATE attendance
SET clock_out = NOW()
WHERE employee_id = 1
  AND attendance_date = CURDATE();
SELECT * FROM attendance;
SELECT
    e.employee_name,
    e.department,
    a.attendance_date,
    a.clock_in,
    a.clock_out,
    a.attendance_status
FROM employees e
JOIN attendance a
    ON e.employee_id = a.employee_id;
UPDATE tasks
SET task_status = 'Completed'
WHERE task_id = 2;  
DELETE FROM tasks
WHERE task_id = 5;  
DELIMITER //

CREATE PROCEDURE CalculateWorkingHours(
    IN p_employee_id INT
)
BEGIN
    SELECT
        e.employee_id,
        e.employee_name,
        COALESCE(
            SUM(
                TIMESTAMPDIFF(
                    MINUTE,
                    a.clock_in,
                    a.clock_out
                )
            ) / 60.0,
            0
        ) AS total_working_hours
    FROM employees e
    LEFT JOIN attendance a
        ON e.employee_id = a.employee_id
    WHERE e.employee_id = p_employee_id
    GROUP BY
        e.employee_id,
        e.employee_name;
END //

DELIMITER ;
CALL CalculateWorkingHours(1);
CREATE INDEX idx_employee_department
ON employees(department);
CREATE INDEX idx_attendance_employee
ON attendance(employee_id);
SHOW INDEX FROM employees;
SHOW INDEX FROM attendance;
SHOW INDEX FROM tasks;




