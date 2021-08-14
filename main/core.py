from functools import wraps

from flask import request
from marshmallow import ValidationError
from main import errors


# A convenient decorator to parse input with the specified schema and raise a bad request error if there are validation
# errors when parsing
def parse_args_with(schema):
    def parse_args_with_decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            request_args = request.get_json() or {}
            if request.method == "GET":
                request_args = request.args.to_dict()
            try:
                result = schema.load(request_args)
            except ValidationError as err:
                raise errors.BadRequest(error_data=err.messages)

            kwargs["args"] = result
            return f(*args, **kwargs)

        return decorated_function

    return parse_args_with_decorator
