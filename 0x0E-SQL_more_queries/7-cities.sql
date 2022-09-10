-- A script that creates a database and a table
-- id is unique, auto generated, can't benull and is a primary key
-- state_id can't be null, is a foreign key that references id of states table
-- name can't be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	   id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	   state_id INT NOT NULL,
	   name VARCHAR(256) NOT NULL,
	   FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
