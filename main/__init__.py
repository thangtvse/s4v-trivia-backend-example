import logging

from flask import Flask
from flask_cors import CORS

from main.config import config
from main.error_handlers import register_error_handlers

app = Flask(__name__)
app.config.from_object(config)
CORS(app)

logging.basicConfig(
    format="%(asctime)s %(levelname)-5s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)


# Register these in their own function so they don't pollute
# the main namespace
# Loading these here lets sqlalchemy know about the models
# and allows the controllers/errors to execute their hooks to
# create the routes
def _register_subpackages():
    import main.controllers


_register_subpackages()

register_error_handlers(app)