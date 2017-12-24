import pymongo
from pymongo import MongoClient


settings = {
    'mongo_db_name': '311',
    'mongo_collection_name': '311',
}

if __name__ == "__main__":

    mongo_client = MongoClient()
    mongo_db = mongo_client[settings['mongo_db_name']]
    mongo_collection = mongo_db[settings['mongo_collection_name']]

    print("Searching for tuples with missing values ...")

    # Checks attributes for missing values; uses logical AND operator
    count = mongo_collection.delete_many({"Complaint Type":""})

    print("Deleted " + str(count.deleted_count) + " documents")