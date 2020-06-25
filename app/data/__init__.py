from flask import Blueprint

api = Blueprint('data', __name__)

from . import endpoints
