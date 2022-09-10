-- A script that lists all cities in our db its state
-- Records are sorted in asc order using cities.id
SELECT c.id, c.name, s.name
	   FROM cities AS c
	   		INNER JOIN states AS s
			ON c.state_id = s.id
	ORDER BY c.id;
