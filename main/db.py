import ssl

from main.config import MONGO_URL, MONGO_DB
from pymongo import MongoClient

client = MongoClient(MONGO_URL, ssl_cert_reqs=ssl.CERT_NONE)

def get_users_collection():
    return client[MONGO_DB]["users"]
