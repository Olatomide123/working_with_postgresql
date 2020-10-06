import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine("postgres:///mydb")

db = scoped_session(sessionmaker(bind=engine))
def main():
    f = open("flights.csv") # open up the file containing the data and call it 'f'
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin": origin, "destination": destination, "duration": duration}) # fill in the place holders with values from the 'for loop'
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
        # :origin means a place holder for origin since we don't know the exact value of the origin yet
        # :destination means place holder for destination
        # :duration means place holder for duration
    db.commit() # save the changes

if __name__ == "__main__":
    main()
