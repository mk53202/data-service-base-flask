import datetime
import io
import os
import flask

# from app.api import api
# from app.data import data


@api.route('/',  methods=['GET'])
def home():
    return "API default"


# @api.route("/days/<int:days>", methods=['GET'])
# def routeDays(days):
#     query = str(days) + " days"
#     # myData = jsonLoraMap(query)
#     return query


# @api.route("/test", methods=['GET'])
# def testdb():
#     try:
#         from sqlalchemy.sql import text
#         db.session.query("1").from_statement(text("SELECT 1")).all()
#     except:
#         return '<h1>Something is broken.</h1>'

# @api.route("/device/<int:device_id>", methods=['PUT'])
# def routeDays(days):
#     query = str(days) + " days"
#     # myData = jsonLoraMap(query)
#     return query

# @app.route("/weeks/<int:weeks>")
# def routeWeeks(weeks):
#     query = str(weeks) + " weeks"
#     myData = jsonLoraMap(query)
#     return myData

# @app.route("/hours/<int:hours>")
# def routeHours(hours):
#     query = str(hours) + " hours"
#     myData = jsonLoraMap(query)
#     return myData

# if __name__ == "__main__":
#     app.run(host='0.0.0.0')

# sql_command = queries.SQL_BASIC_SELECT_WITH_TIME
#geocoder = what3words.Geocoder(creds.WHAT3WORDS_API_KEY)

# def jsonLoraMap(query):

#     SQL_BASIC_SELECT_WITH_TIME='''
#     select id, received_at, device_name, application_name, data, rx_info, object
#     from device_up
#     where (received_at > now() - interval '{0}') and (device_name = 'lora-app-node');
#     '''.format(query)

#     data = {}               # Variables to hold JSON document we'll build below
#     data['geo_data'] = []   #

#     conn_string = "host={} port={} dbname={} user={} password={}".format(creds.PGHOST, creds.PGPORT, creds.PGDATABASE, creds.PGUSER, creds.PGPASSWORD)
#     conn=psycopg2.connect(conn_string)

#     cur = conn.cursor(cursor_factory=RealDictCursor)
#     cur.execute(SQL_BASIC_SELECT_WITH_TIME)
#     sql_results = cur.fetchall()

#     for sql_row in sql_results:     # Loop through result rows from query

#         data_payload = sql_row['data'].tobytes().decode('utf-8')    # Get and decode data_payload from lora receive column
#         if not re.match("^\d+(.)\d+,", data_payload):   # Match string from beginning of line (for example): 123.5678,
#             continue    # Go to next row in for loop

#         # Added in what3words integration
#         (lat, lon) = data_payload.split(',',1)  # Split latitude and longitude seperately by comma delimination
#         #what3words_results = geocoder.convert_to_3wa(what3words.Coordinates(lat, lon))  # Make api call to get what3words words for coord
#         #what3words_word = what3words_results['words'] # set variable for inclusion in JSON serialization below
#         what3words_word = 'matt.koster.me'

#         rx_info = sql_row['rx_info']    # Get formatted data in rx_infor
#         for item_rx_info in rx_info:    # and parse it out
#             rssi = item_rx_info['rssi']
#             snr = item_rx_info['loRaSNR']
#             received_at = item_rx_info['time']
#         #alt = ['altitude']
#         #
#         # Format the document outout
#         #
#         data['geo_data'].append({
#             'id': sql_row['id'],
#             'device_name': sql_row['device_name'],
#             'received_at': received_at,
#             'rssi': rssi,
#             'snr': snr,
#             'geo_coord': data_payload,
#             #'what3words': what3words_word
#         })

#     return data
