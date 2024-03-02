/*
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| user_name   | varchar |
+-------------+---------+
user_id is the primary key (column with unique values) for this table.
Each row of this table contains the name and the id of a user.
 

Table: Register

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| contest_id  | int     |
| user_id     | int     |
+-------------+---------+
(contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id of a user and the contest they registered into.
 

Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

The result format is in the following example.
*/

SELECT
    contest_id,
    -- Create `percentage` which will be 
    -- users in contest / all users in Users table as percentage  round 2
    ROUND((COUNT(*) / (SELECT DISTINCT COUNT(*) FROM Users) * 100), 2) as percentage
FROM 
    Register
GROUP BY contest_id
-- order by percentage DESC, contest_id ASC
ORDER BY percentage DESC, contest_id ASC;
