-- Script that lists the number of records with the same score
-- result should display score and number of records for this score as number
-- list should be sorted by the number of records descending
-- Db name is passed as an argument to the mysql command, as all the others
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
