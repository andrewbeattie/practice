# Note that we need to delete the columns not select...
# So we need to use a subquery to get the id of the rows that have the same email.
# Then we can use that id to delete the rows that have the same id but different emails.



DELETE FROM Person
WHERE id NOT IN (
    SELECT id
    FROM (
        SELECT id,
               ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS row_num
        FROM Person
    ) AS RankedRows
    WHERE row_num = 1
);
