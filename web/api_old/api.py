import datetime
import io
import os
import flask
# import pg_simple
import sys
sys.path.append("..")

# from web.api import api
# from app.data import data

from app import api

@api.route('/',  methods=['GET'])
def home():
    return "API default"

@api.route("/days/<int:days>", methods=['GET'])
def routeDays(days):
    query = str(days) + " days"
    # myData = jsonLoraMap(query)
    return query

@api.route("/test", methods=['GET'])
def testdb():
    try:
        from sqlalchemy.sql import text
        db.session.query("1").from_statement(text("SELECT 1")).all()
    except:
        return '<h1>Something is broken.</h1>'
