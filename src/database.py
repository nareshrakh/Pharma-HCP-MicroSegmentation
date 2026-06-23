import config
import pymongo

mongo_url = config.MONGODB_URL
mongo_client = pymongo.MongoClient(mongo_url)

def get_user_collection():
    db_name = config.MONGO_DB_NAME
    db = mongo_client[db_name]
    user_collection = db['user_details']
    return user_collection


def get_data_collection():
    db_name = config.MONGO_DB_NAME
    db = mongo_client[db_name]
    data_collection = db['input_data_details']
    return data_collection