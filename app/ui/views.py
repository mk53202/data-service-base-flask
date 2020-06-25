from app.ui import ui
import flask
import os

@ui.route('/',  methods=['GET'])
def index():
    return "No UI here, only API. Go to /api"
