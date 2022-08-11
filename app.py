# Import Dependencies:
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set-up:
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

# Add code to reflect the database:
Base.prepare(engine, reflect=True)

# Create our references for each table in the database; We checked these in VS Code:
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session to link from python to our database:
session = Session(engine)

# Create App and define routes:
app = Flask(__name__)

# Define the welcome route:
@app.route('/')

def welcome():
    return(
    '''
    <b>Welcome to the Climate Analysis API!<b><br/>
    <br/>
    <b>Available Routes:</b><br/>
    <br/>
    <mark>/api/v1.0/precipitation<mark><br/>
    <mark>/api/v1.0/stations<mark><br/>
    <mark>/api/v1.0/tobs<mark><br/>
    <mark>/api/v1.0/temp/start/end<mark><br/>
    <br/>
    <b>Thank You for using the Climate Analysis API!<b>

    ''')



# Create precipitation route:
@app.route("/api/v1.0/precipitation")

def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Create stations route:
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# Create the temperature observations route for the recorded temperatures of the previous year:
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create a route to report on the minimum, average, and maximum temperatures.
# This route is different and will include both a starting and ending date:
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)