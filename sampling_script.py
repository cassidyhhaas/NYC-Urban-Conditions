import argparse
import pymongo
from pymongo import MongoClient
import os

settings = {
    'mongo_db_name': '311_mongo_import',
    'mongo_collection_name': '311_mongo_import',
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bootstrapping script")
    parser.add_argument('--size',
                        type=int,
                        help='sample size',
                        default=100000,
                        required=False)
    parser.add_argument('--number',
                        type=int,
                        help='number of samples',
                        default=10,
                        required=False)
    args = parser.parse_args()

    mongo_client = MongoClient()
    mongo_db = mongo_client[settings['mongo_db_name']]
    mongo_collection = mongo_db[settings['mongo_collection_name']]

    print("Sampling from " + str(mongo_collection.count()) + " documents")

    for sample in range(args.number):
        mongo_sample_collection_name = "sample_" + str(sample)
		
        mongo_sample_collection = mongo_db[mongo_sample_collection_name]

        mongo_sample_collection.insert(mongo_collection.aggregate(
            [ { '$sample': { 'size': args.size } } ], allowDiskUse=True))

        #cursor = mongo_sample_collection.find({})
        #for document in cursor:
        #    print(document)
