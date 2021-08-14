import ssl

from main.config import config
from pymongo import MongoClient

print(config["MONGO_URL"])
client = MongoClient(config["MONGO_URL"], ssl_cert_reqs=ssl.CERT_NONE)

def get_users_collection():
    return client[config["MONGO_DB"]]["users"]
