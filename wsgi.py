import os
from app import create_app # imports app/__init__.py->create_app()

app = create_app(os.getenv('FLASK_CONFIG') or 'default') # create app and entrypoint

