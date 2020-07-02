import os
from app import create_app # imports web/app.py->create_app()

app = create_app(os.getenv('FLASK_CONFIG') or 'default') # create app and entrypoint