CREATE TABLE flights(
  id SERIAL PRIMARY KEY, -- serial is a datatype similar to integer but it increments automatically
                          -- primary means this is the way i want to reference all flights or a table
  origin VARCHAR NOT NULL, -- VARCHAR = text, NOT NULL: means it can't be empty
  destination VARCHAR NOT NULL,
  duration INTEGER NOT NULL
);
