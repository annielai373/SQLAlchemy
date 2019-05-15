import numpy as np
import sqlalchemy
import sqlite3
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


## Database Setup ##
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


## Flask Setup ##
app = Flask(__name__)


## Flask Routes ##

@app.route("/")
def home():
    print("Server received request for 'Home' page...")
#    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
#    """Return a list of all precipitation values"""
    # Query all 
    prcp = session.query(Measurement.date, Measurement.prcp)\
            .filter(Measurement.date >= prev_year)\
            .order_by(Measurement.date).all()

    # Convert list of tuples into normal list
    prcp = list(np.ravel(prcp))

    return jsonify(prcp)

@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'tobs' page...")
#    """Return a list of all tobs values"""
    # Query all 
    tobs = session.query(Measurement.date, Measurement.tobs)\
            .filter(Measurement.date >= prev_year)\
            .order_by(Measurement.date).all()

    # Convert list of tuples into normal list
    tobs = list(np.ravel(tobs))

    return jsonify(tobs)

@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    """Return a list of stations data"""
    # Query all stations
    stations = session.query(Station.stations).all()

    # Convert list of tuples into normal list
    stations = list(np.ravel(stations))

    return jsonify(stations)


if __name__ == '__main__':
    app.run(debug=True)
