from pymongo import MongoClient
from project.config import Config
client=MongoClient(Config.MONGO_DATABASE_URI)
mongo_database=client.mongo_database
api_exception_collection=mongo_database["api_collection"]
application_exception_collection=mongo_database["application_collection"]