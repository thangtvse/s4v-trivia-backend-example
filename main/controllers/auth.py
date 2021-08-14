import bcrypt
from flask import jsonify

from main import app, jwttoken
from main.core import parse_args_with
from main.schemas.auth import LoginRequestSchema, SignupRequestSchema, AuthResponseSchema
from main.db import get_users_collection
from main.errors import BadRequest


@app.route('/auth/signup', methods=["POST"])
@parse_args_with(SignupRequestSchema())
def signup(args):
    username = args["username"]
    password = args["password"]

    users_collection = get_users_collection()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    existing_user = users_collection.find_one({
        "username": username
    })

    if existing_user:
        raise BadRequest(message="Username is already taken")

    res = users_collection.insert_one({
        "username": username,
        "password": hashed_password
    })

    return AuthResponseSchema().dump({
        "_id": str(res.inserted_id),
        "username": username,
        "access_token": jwttoken.encode({
            "_id": str(res.inserted_id),
            "username": username,
        })
    })


@app.route('/auth/login', methods=["POST"])
@parse_args_with(LoginRequestSchema())
def login(args):
    username = args["username"]
    password = args["password"]

    users_collection = get_users_collection()
    user = users_collection.find_one({
        "username": username
    })

    if not user:
        raise BadRequest(message="Incorrect username or password")

    matched = bcrypt.checkpw(password.encode('utf-8'), user["password"])

    if not matched:
        raise BadRequest(message="Incorrect username or password")

    return AuthResponseSchema().dump({
        "_id": str(user["_id"]),
        "username": username,
        "access_token": jwttoken.encode({
            "_id": str(user["_id"]),
            "username": username,
        })
    })
