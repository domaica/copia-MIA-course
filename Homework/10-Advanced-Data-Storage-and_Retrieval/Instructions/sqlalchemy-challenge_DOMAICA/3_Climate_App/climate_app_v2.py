# Check powerpoint file in this same folder: 'screenshots of climate_app_v2.py running.pptx'
# to see results and screenshots

# Dependencies

import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database -----------------------------------------

# create engine with database file ---
engine = create_engine('sqlite:///../Resources/hawaii.sqlite')

# reflect database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# save references to tables
measurement = Base.classes.measurement
station = Base.classes.station

# Flask setup-----------------------------------------

app = Flask(__name__)

# Flask Routes --------------------------------
# Home page.
# List all routes that are available.

@app.route("/")
def home():
    return (
        f"</br>"
        f"This is Ignacio Domaica's climate app page<br/>"
        f"-----------------------------------------------<br/>"
        f"These are all available routes from this home page<br/>"
        f"To proceed, please copy any below route and paste above (After current url in web browser)<br/>"
        f"-----------------------------------------------<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"</br>"
        f"-----------------------------------------------<br/>"
        f"WARNING: For these following 2 routes you will have additional instructions in corresponding webpage</br>"
        f"</br>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
        f"<br>"

    )

################ ROUTE #########################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # create a session from Python to the database
    session = Session(engine)
    # perform a query to extract every date and precipitation values
    prcp_data = session.query(measurement.date, measurement.prcp).all()
    # close the session
    session.close()

    # Create a new empty dictionary
    prcp_dict = {} 
    # loop query and add required info into dictionary (date & precipitation inches observations)
    for date, prcp in prcp_data:
        prcp_dict[date] = prcp
    
    # jsonify dictionary as required
    return jsonify(prcp_dict)



################ ROUTE #########################
@app.route("/api/v1.0/stations")
def stations():
    # create a session from Python to the database
    session = Session(engine)
    # perform a query to retrieve all the station data
    results = session.query(station.station, station.name).all()
    # close the session 
    session.close()

    # create a list of dictionaries with station info using for loop
    list_stations = []

    for st in results:
        # empty dictionary
        station_dict = {}
        # retrieve fields of name and station
        station_dict["station"] = st[0]
        station_dict["name"] = st[1]
        # append dictionary values to list
        list_stations.append(station_dict)

    # jsonify list
    return jsonify(list_stations)


################ ROUTE #########################
@app.route("/api/v1.0/tobs")
def tobs():

    # create a session from Python to the database
    session = Session(engine)

    # Query the dates and temperature observations of the most active station for the last year of data.
    # Get most active station
    most_active_station = session.query(measurement.station, func.count(measurement.station)).\
                                        order_by(func.count(measurement.station).desc()).\
                                        group_by(measurement.station).first()[0]

    # To get last year of data proceed exactly as we did in the data analysis
    # convert to datetime and calculate the start date (12 months from the last date 
    # or 365 days using timelapse from datetime
    get_last_date = session.query(measurement.date).order_by(measurement.date.desc()).first()[0]
    format_str = '%Y-%m-%d'
    last_date = dt.datetime.strptime(get_last_date, format_str)
    query_date = last_date - dt.timedelta(days=365)

    # Query temperature observation from database with conditions:
    # most_active
    # one year back
    most_active_temps = session.query(measurement.date, measurement.tobs).\
                                    filter((measurement.station == most_active_station)\
                                            & (measurement.date >= query_date)\
                                            & (measurement.date <= last_date)).all()

    # close session
    session.close()

    # jsonify query results
    return jsonify(most_active_temps)


################ ROUTE #########################
@app.route("/api/v1.0/<start>")
def temps_from_start(start):
    # Return a JSON list of the minimum temperature, the average temperature, 
    # and the max temperature for a given start date.
    # Initial function to collect daily observations from start date 
    def collect_day_temp(start_date):

        # create a session from Python to the database
        session = Session(engine)   
        # collect date, temps from database and get max min and calculate averages for temperatures observed
        sel = [measurement.date, func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]
        # loop results selected (*sel) and group by date taking into account datetime formats
        return session.query(*sel).filter(func.strftime("%Y-%m-%d", measurement.date)\
            >= func.strftime("%Y-%m-%d", start_date)).group_by(measurement.date).all()

        # close session
        session.close()

    try:
        # convert string start date to a date format with datetime  
        start_date = dt.datetime.strptime(start, "%Y-%m-%d")

        # call previous function to get max min average from initial date
        collected_infos = collect_day_temp(start_date)
         # creat new dictionary empty needed to append later
        daily_stats=[]

        # create a "for" loop to append data 
        for temp_date, tmin, tmax, tavg in collected_infos:

            # new dictionary and collect results for rows with dates, min, max and average 
            # in that specific date for all stations
            dict_aux = {}
            # dict_aux = temp_date, tmin, tmax, tavg
            dict_aux = {}
            dict_aux["Observation Date"] = temp_date
            dict_aux["Temp-Min"] = tmin
            dict_aux["Temp-Max"] = tmax
            dict_aux["Temp-Avg"] = tavg

            # append results to daily stats list from dict_aux dictionary
            daily_stats.append(dict_aux)

        # jsonify dictionary with temperatures
        return jsonify(daily_stats)

    except ValueError:
        return "</br> Please substitute string 'start_date' in above url by a specific start date\
                </br> </br> with following format:'YYYY-MM-DD'  , for example: '2016-08-01'"
# --------------------------



############ ROUTE #########################
@app.route("/api/v1.0/<start>/<end>")
def temps_range(start, end):
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
    # Initial function to collect daily observations within a date range
    def collect_day_temp(start_date, end_date):

        # DB session call
        session = Session(engine)   

        sel = [measurement.date, func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
        return session.query(*sel).filter(func.strftime("%Y-%m-%d", measurement.date) >= func.strftime("%Y-%m-%d", start_date)).\
                                   filter(func.strftime("%Y-%m-%d", measurement.date) <= func.strftime("%Y-%m-%d", end_date)).\
                                    group_by(measurement.date).all()

        # DB session close
        session.close()

    try:
        # start date & end date transform to datetime format 
        start_date = dt.datetime.strptime(start, "%Y-%m-%d")
        end_date = dt.datetime.strptime(end, "%Y-%m-%d")

        # call above function to calculate max min avg for every station from start date to end
        collected_infos = collect_day_temp(start_date, end_date)
        daily_stats=[]

        # create a "for" loop to append data 
        for temp_date, tmin, tavg, tmax in collected_infos:

            # new dictionary and collect results for rows with dates, min, max and average 
            # in that specific date for all stations
            dict_aux = {}
            dict_aux["Observation Date"] = temp_date
            dict_aux["Temp-Min"] = tmin
            dict_aux["Temp-Max"] = tmax
            dict_aux["Temp-Avg"] = tavg

            # append row results to daily stats
            daily_stats.append(dict_aux)

        #after loop jsonify dictionary with temperatures
        return jsonify(daily_stats)

    except ValueError:
        return "</br> Change string 'start_date/end_date' in above url by a specific range of start and end dates\
                </br> </br> with this format: 'YYYY-MM-DD/YYYY-MM-DD'\
                </br> </br> For example: 2016-08-01/2016-12-31"

if __name__ == "__main__":
    app.run(debug=True)