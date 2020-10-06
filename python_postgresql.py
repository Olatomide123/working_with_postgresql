import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL")) # The engine is just an object created  by SQL alchemy. It is used to manage connections to the database.
                                                    # the engine will help us with talking to the datatype and making sure that python is able to send commands to the database
                                                    # and get results from the database
                                                    # note (os.getenv) did not work on my mac
engine = create_engine("postgres:///mydb")         # I had to create a new user and password on postgresql, then I aslo created a new db called mydb


db = scoped_session(sessionmaker(bind=engine))  # when we have multiple people simultaneously trying to use our website
                                                # at the same time, we want to make sure that the stuff that person A is doing
                                                # with the database is kept separate from the stuff that person B is doing with the
                                                # database. That is, creating different sessions for different people.

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall() # select/get the origin, destination and duration from the db.
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.") # python 2.7 will not run print(f"{})
                                                                                        # instead use python3 list.py on command terminal

if __name__ == "__main__":
    main()
