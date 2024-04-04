/*
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, 
rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days 
starting from their first login date, then divide that number by the total number of players.
*/

-- get the first event_date for each player_id

SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id

-- get the fraction
-- count of players that meet the condition

-- find condition where player_id = player_id and event_date - 1= first_login + 1
WHERE   
    (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN (
        ...
    )

-- approach 1 
-- create a sub query with the first login date for each player id
-- join the sub query then use CASE statement to get the counts
-- being the players for which the event_date = first_login + 1
-- divide by the total player ids

SUM(CASE WHEN event_date = first_login + 1 THEN 1 ELSE 0 END) / COUNT(DISTINCT player_id)

-- put together

# Write your MySQL query statement below
WITH FirstEvent AS (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
)
SELECT 
    ROUND(SUM(CASE WHEN a.event_date = DATE_ADD(f.first_login INTERVAL 1 DAY) THEN 1 ELSE 0 END) / COUNT(DISTINCT f.player_id), 2) AS fraction
FROM Activity AS a
LEFT JOIN FirstEvent AS f
    ON a.player_id = f.player_id

/*
DATE_ADD(val INTERVAL 1 DAY) -- add 1 day
DATE_SUB(val INTERVAL 1 DAY) -- sub 1 day
DATE_ADD(val INTERVAL 1 MONTH) -- add 1 month
DATE_SUB(val INTERVAL 1 MONTH) -- sub 1 month
DATE_FORMAT(val, '%Y-%m-%d')
DATE_FORMAT(val, '%Y-%m-%d %H:%i:%s')
*/
