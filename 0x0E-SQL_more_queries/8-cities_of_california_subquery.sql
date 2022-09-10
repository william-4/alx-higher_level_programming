-- A script that lists all cities of California in db hbtn_0d_usa
-- sort results in asc order by cities.id
SELECT `id`, `name`
	   FROM `cities`
	   WHERE `state_id` IN (
	   		 SELECT `id`
			 FROM `states`
			 WHERE `name` = "California")
		ORDER BY `id`;
