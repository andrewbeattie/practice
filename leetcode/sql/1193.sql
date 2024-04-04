/* Table: Transactions

https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

Return the result table in any order. */


SELECT
    /* Methods like MONTH_YEAR or SUBSTRING_INDEX or DATE_FORMAT will all work
    DATE_FORMAT AND SUBSTRING_INDEX offer the most flexibility
    SUBSTRING_INDEX will be faster but it could fail if the date is not in expected format
    depending upon use this could be beneficial however
    */
    SUBSTRING_INDEX(trans_date, '-', 2) AS month,
    country,
    COUNT(id) AS trans_count,
    -- Count will be slightly faster
    COUNT(CASE WHEN state = 'approved' THEN 1 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    -- Handling cases where the amount is 0 or null
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount 
FROM Transactions
GROUP BY month, country;  