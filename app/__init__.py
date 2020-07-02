from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
# from flask_moment import Moment # Extends the jinja templates with localized date/time functionality

# moment = Moment()   # Extends the jinja templates with localized date/time functionality

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(config[config_name])

    db.init_app(app)
    db.create_all(app=app)

    config[config_name].init_app(app)
    # moment.init_app(app)

    # Register the ui
    from app.ui import ui as ui_blueprint
    app.register_blueprint(ui_blueprint)

    # Register the api endpoints
    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
