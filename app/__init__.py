import logging
import logging.config
import logging.handlers
from flask import Flask
from werkzeug.utils import import_string
from app.models.base_models import MIGRATE, DB


def create_app(app_config):
    """
    Initialize the core application.
    """

    # Creating the app
    flask_app = Flask(__name__)
    cfg = import_string(app_config)()
    flask_app.config.from_object(cfg)
    DB.init_app(flask_app)
    MIGRATE.init_app(flask_app, DB)
    # Enable sqlalchemy logging
    if flask_app.config.get('ENV', 'dev') == 'dev':
        # set log level can be configure from env variable
        logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)

    return flask_app
