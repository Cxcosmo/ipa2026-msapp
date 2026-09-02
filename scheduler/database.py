import os

from pymongo import MongoClient

mongo_uri = os.environ.get("MONGO_URI")
db_name   = os.environ.get("DB_NAME")

client = MongoClient(mongo_uri)
db = client[db_name]
routers = db["routers"]


def get_router_info():
    return list(routers.find())


if __name__ == '__main__':
    print(get_router_info())