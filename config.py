import os

class Config(object):
    NGINX_PATH = '/etc/nginx'
    CONFIG_PATH = os.path.join(NGINX_PATH, 'conf.d')
    SECRET_KEY = os.urandom(64).hex()
    DEBUG = os.environ['DEBUG']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )

    @staticmethod
    def init_app(app):  # do any data materialization here.
        pass

class DevConfig(Config):
    DEBUG = True

class WorkingConfig(Config):
    DEBUG = False

config = {
    'dev': DevConfig,
    'default': WorkingConfig
}
