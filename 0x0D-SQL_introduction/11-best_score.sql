-- List all records with score >= 10 in a table ordered by score(top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESCENDING
