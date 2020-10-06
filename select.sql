SELECT * FROM flights;


SELECT * FROM flights LIMIT 2; -- meaning get all from flights but only give me back a maximum  of two rows.

SELECT * FROM flights ORDER BY duration ASC; -- ASC= asccending

SELECT * FROM flights ORDER BY duration ASC LIMIT 3;

SELECT * FROM flights ORDER BY duration DESC;

SELECT * FROM flights ORDER BY duration DESC LIMIT 3;

SELECT origin, COUNT(*) FROM flights GROUP BY origin;


--- below means: select origin, count star: how many flights are from that location from my flights, grouping
-- them by origin having the origin greater than one
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;
