import datetime as dt
import numpy as np
import pandas as pd
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


##flask setup
from flask import Flask, jsonify

app = Flask(__name__)




#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`"
    )

##test comment
@app.route("/api/v1.0/precipitation<br/>")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp)


    return jsonify

@app.route("/api/v1.0/stations<br/>")
def stations():
querystations = session.query(station.station)
   
    return jsonify

@app.route("/api/v1.0/tobs<br/>")
def tobs():
   

   return jsonify
    


@app.route("/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`"")
def search():


    return jsonify
    
