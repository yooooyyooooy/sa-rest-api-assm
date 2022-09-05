from pymongo import MongoClient

from configs.config import settings

conn = MongoClient(settings.MONGO_CLUSTER)
db = conn[settings.DB_NAME]
