-- https://leetcode.com/problems/project-employees-i/

/* Table: Project

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
(project_id, employee_id) is the primary key of this table.
employee_id is a foreign key to Employee table.
Each row of this table indicates that the employee with employee_id is working on the project with project_id.
 

Table: Employee

+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
employee_id is the primary key of this table. It's guaranteed that experience_years is not NULL.
Each row of this table contains information about one employee. */


SELECT 
    -- project_id
    p.project_id as project_id,
    -- average experience years
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM 
    Project as p
LEFT JOIN Employee as e 
    ON p.employee_id = e.employee_id
-- all employees for each project
GROUP BY p.project_id
ORDER by p.project_id ASC;
