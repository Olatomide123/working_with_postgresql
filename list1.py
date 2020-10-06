import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL")) # The engine is just an object created  by SQL alchemy. It is used to manage connections to the database.
                                                    # the engine will help us with talking to the datatype and making sure that python is able to send commands to the database
                                                    # and get results from the database
engine = create_engine("postgres:///mydb")

db = scoped_session(sessionmaker(bind=engine))  # when we have multiple people simultaneously trying to use our website
                                                # at the same time, we want to make sure that the stuff that person A is doing
                                                # with the database is kept separate from the stuff that person B is doing with the
                                                # database. That is, creating different sessions for different people.

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    main()
