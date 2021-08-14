import datetime
import os

import jwt

from main.config import JWT_SECRET


def encode(audience):
    iat = datetime.datetime.utcnow()
    return jwt.encode(
        {
            "sub": audience,
            "iat": iat,
            "exp": iat + datetime.timedelta(days=365),
        },
        JWT_SECRET,
    )


def decode(access_token, audience):
    try:
        token = jwt.decode(
            access_token,
            config.JWT_SECRET,
            leeway=10,
            algorithms="HS256",
            audience=audience,
        )
    except jwt.InvalidTokenError:
        return None
    return token


def generate_access_token_nonce():
    return os.urandom(4).hex()
