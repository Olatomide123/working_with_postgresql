from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine("postgres:///mydb")
db = scoped_session(sessionmaker(bind=engine))




app = Flask(__name__) # meaning I want to create a new web application and I want this web application to be a web application and (__name__) represent this current file

@app.route("/")
def index():
        flights = db.execute("SELECT * FROM flights").fetchall()
        return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():

    """Book a flight."""

        # Get form information.
    name = request.form.get("name") # get the name from the form submitted by thr user

    try:
        flight_id = int(request.form.get("flight_id"))

    except ValueError:
        return render_template("error.html", message="Invalid flight number.")


    # Make sure the flight exists.
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0: # means mo flight
        return render_template("error.html", message="No such flight with that id.")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",{"name": name, "flight_id": flight_id})

    db.commit()
    return render_template("success.html")
