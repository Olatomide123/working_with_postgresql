-- foreign key is a method for connecting multiple tables together

-- SQL is often called a relational database because one thing that makes it powerful
-- is the ability to take multiple different tables and relate them together in some way.

CREATE TABLE passengers(
  id SERIAL PRIMARY KEY,
  name VARCHAR NOT NULL,
  flight_id INTEGER REFERENCES flights -- flight_id is an integer that is going to reference the flights table.
);

INSERT INTO passengers (name, flight_id) VALUES('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES('Bob', 2);
INSERT INTO passengers (name, flight_id) VALUES('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES('Dave', 2);
INSERT INTO passengers (name, flight_id) VALUES('Erin', 4);
INSERT INTO passengers (name, flight_id) VALUES('Frank', 6);
INSERT INTO passengers (name, flight_id) VALUES('Grace', 6);


SELECT * FROM passengers WHERE name = 'Alice';

SELECT * FROM flights WHERE id = 1;

-- 'join' takes two different tables that are related in some way, and group them together into one
-- when you try to select them.
-- example:

SELECT origin, destination, name FROM flights join passengers ON passengers.flight_id = flights.id;

SELECT origin, destination, name FROM flights join passengers ON passengers.flight_id = flight_id WHERE name  = 'Alice';


-- There are different types of joins. The above example is an 'inner join'.
-- there is also left join. What left join is going to do is, it is going to take the table on the left
-- in ths case: flights table and it is going to make sure that all of the rows in the flights table
-- are included in the final result, even if they don't have a match.
-- example:


SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;

-- we also have 'right join'
-- we also have 'full outer join'


SELECT * FROM flights WHERE id IN (SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT (*) > 1);
--the line in bracket means get me all thw flight ids from passengers that have multiple passengers
--and the outer line means that select everything from flights as long as the ID of the flight is in the result of the bracket.
