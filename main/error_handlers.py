import traceback

from flask import jsonify
from werkzeug.exceptions import HTTPException

from .errors import Error, InternalServerError


def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_unauthorized(error: HTTPException):
        return jsonify({"error_message": error.description}), error.code

    @app.errorhandler(Error)
    def handle_error(error: Error):
        return error.to_response()

    @app.errorhandler(Exception)
    def handle_exception(error):
        print(str(error))
        traceback.print_exc()

        return InternalServerError().to_response()
