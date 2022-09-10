-- A script that creates a table
-- name field can't be null
CREATE TABLE IF NOT EXISTS `force_name`(
	   `id` INT,
	   `name` VARCHAR(256) NOT NULL
);
