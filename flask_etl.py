## ---------------------------------------------------------------------
# 1. Import Flask
from flask import Flask,jsonify

## import packages for sql queries and etc.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import SingletonThreadPool
####-------------------------------------------------------------------------

### Create an engine to connect to the database.
engine = create_engine('postgresql://postgres:postgres@localhost:5432/us_dice_jobs')
# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
job_location=Base.classes.job_location

## -----------------------------------------------------------------------------------
###- open a session to the database.
session = Session(engine)

##### --------------------------------------------------------------------------------
# 2. Create an app
app = Flask(__name__)

### -----------------------------------------------------------------------------------
# 3. Define static routes
#### This is the home page of the site. It describes the usage with links
#### Displays a picture of ETL
@app.route("/")
def index():
    return '''<strong>Are you trying to switch jobs? Use this interface to get instant answers!</strong> <br> \
    <br>\
    <strong> \
    <a href="http://127.0.0.1:5000/api/v1.0/location" target="_blank">1. /api/v1.0/location</a><br> \
    <br><a href="http://127.0.0.1:5000/api/v1.0/travel" target="_blank">2. /api/v1.0/travel</a><br> \
    <br><a href="http://127.0.0.1:5000/api/v1.0/telecommute" target="_blank">3. /api/v1.0/telecommute</a><br>\
               
    </strong>\
    <br>\
    <img src="Architecture.png">
    
    '''

## -------------------------------------------------------------------------------------------
#### Code for precipitation 
@app.route("/api/v1.0/location")
def cal_prcp():
    """Display location for the all the jobs from the dataset.
    Args: None
    Returns:
    A jsonified dictionary with all the location readings.
    """
    
## -------------------------------------------------------------------------------------------------
## Code to list the stations
# @app.route("/api/v1.0/stations")
# def station_details():
#     """Display all the stations from the dataset.
#     Args: None
#     Returns:
#     Jsonified names of all the stations.
#     """
#     station_names=session.query(Measurement.station).group_by(Measurement.station).all()
#     jsonified_names=jsonify(station_names)
#     return(jsonified_names)    
## ---------------------------------------------------------------------------------------------------
### Code to display the temperature readings.
# @app.route("/api/v1.0/tobs")
# def tobs():
#     """ Query for the dates and temperature observations from a year from the last data point.
#     Args: None
#     Returns:
#     Return a JSON list of Temperature Observations (tobs) for the previous year.
#     """
#     import datetime
#     import timestring

#     latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
#     start_date=timestring.Date(latest_date).date
#     lasttwelve=start_date-datetime.timedelta(days=366)
#     getdata= session.query(Measurement.date, Measurement.tobs).filter(Measurement.date.between(lasttwelve,start_date))

## creating the dictionary for the display with temperature and dates
    # tobs_list={}
    # for row in getdata:
    #    tobs_list[row[0]]=row[1]
    # temp_twelvemonths=jsonify(tobs_list)
    # return (temp_twelvemonths)
## --------------------------------------------------------------------------------------------------------
# @app.route("/api/v1.0/<start date>")
# def tobs():
#getdata= session.query(Measurement.date, Measurement.tobs).filter(Measurement.date.between(lasttwelve,start_date))

##------------------------------------------------------------------------------------------------------------
# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)

### ------------------------------------------------------------------------------------------------------------
