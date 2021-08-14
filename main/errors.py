from flask import jsonify
from marshmallow import Schema, fields


class Error(Exception):
    status_code = None

    def __init__(self, error_data=None):
        super().__init__()
        self.error_data = error_data or {}

    def to_response(self):
        resp = jsonify(ErrorSchema().dump(self))
        resp.status_code = self.status_code
        return resp


class ErrorSchema(Schema):
    error_code = fields.Int()
    error_message = fields.String()
    error_data = fields.Raw()


class StatusCode:
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    INTERNAL_SERVER_ERROR = 500


class ErrorCode:
    BAD_REQUEST = 40000
    VALIDATION_ERROR = 40001
    METHOD_NOT_ALLOWED = 40007
    UNAUTHORIZED = 40100
    NOT_FOUND = 40400
    INTERNAL_SERVER_ERROR = 50000


class BadRequest(Error):
    status_code = StatusCode.BAD_REQUEST
    error_code = ErrorCode.BAD_REQUEST
    error_message = "Bad request"

    def __init__(
            self, code=ErrorCode.BAD_REQUEST, message="Bad Request", error_data=None
    ):
        super().__init__(error_data)
        self.error_code = code
        self.error_message = message


class NotFound(Error):
    status_code = StatusCode.NOT_FOUND
    error_code = ErrorCode.NOT_FOUND
    error_message = "Not found"

    def __init__(self, code=ErrorCode.NOT_FOUND, message="Not found", error_data=None):
        super().__init__(error_data)
        self.error_code = code
        self.error_message = message


class MethodNotAllowed(Error):
    status_code = StatusCode.METHOD_NOT_ALLOWED
    error_code = ErrorCode.METHOD_NOT_ALLOWED
    error_message = "Method not allowed"


class ValidationError(Error):
    status_code = StatusCode.BAD_REQUEST
    error_code = ErrorCode.VALIDATION_ERROR
    error_message = "Validation error"

    def __init__(
            self,
            code=ErrorCode.VALIDATION_ERROR,
            message="Validation error",
            error_data=None,
    ):
        super().__init__(error_data)
        self.error_code = code
        self.error_message = message


class Unauthorized(Error):
    status_code = StatusCode.UNAUTHORIZED
    error_code = ErrorCode.UNAUTHORIZED
    error_message = "Unauthorized"


class InternalServerError(Error):
    status_code = StatusCode.INTERNAL_SERVER_ERROR
    error_code = ErrorCode.INTERNAL_SERVER_ERROR
    error_message = "Internal Server Error"

    def __init__(self, message="Internal Server Error", error_data=None):
        super().__init__(error_data)
        self.error_message = message
