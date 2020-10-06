-- The idea of sql injection and race condition are just for good security considerations to be taken in
-- mind as we start to approach designing databses that are ultimately going to go into web applications.

-- SQL transactions have 'begin' and 'commit'

-- To bridge the gap between Python and SQL, to allow our python code to be able to run SQL commands on databases
-- And so what we'll be using for that is a popular library called SQL ALCHEMY
-- SQL ALCHEMY is a python library that is used to connect Python and SQL and to allow Python code
-- to be able to run SQL queries.

-- Example: if I want a python programn that prints out all of the flights that are currently in my flights table.
-- Check list.py file
