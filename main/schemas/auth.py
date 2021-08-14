import numbers

from marshmallow import (
    INCLUDE,
    Schema,
    ValidationError,
    fields,
    post_load,
    pre_load,
    validate,
    validates_schema,
)

from main.schemas import BaseSchema


class SignupRequestSchema(BaseSchema):
    username = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8))


class LoginRequestSchema(BaseSchema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class AuthResponseSchema(BaseSchema):
    _id = fields.String(required=True)
    username = fields.String(required=True)
    access_token = fields.String(required=True)
