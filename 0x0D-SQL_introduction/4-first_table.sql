-- Script that creates a table called first_table in current db
-- If table exists, script should not fail
CREATE TABLE IF NOT EXISTS first_table (
       id INT,
       name VARCHAR(256)
       );
