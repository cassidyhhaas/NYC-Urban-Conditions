import pandas as pandas
import json
import pymongo
import argparse
from pymongo import MongoClient
import pprint

settings = {
    'mongo_db_name': '311',
    'chunk_size': 100000,
    'drop_collections_on_load': True,
    'mongo_collection_name': '311',
}

def write_to_mongo_db(destination, data):
    if (settings['drop_collections_on_load']):
        destination.drop()
    for chunk in data:
        destination.insert(json.loads(chunk.to_json(orient='records')))

if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Pymongo import')
	parser.add_argument('--data',
						type=str,
						help='csv data file',
						required=True)
	args = parser.parse_args()
	
	mongo_client = MongoClient()
	mongo_db = mongo_client[settings['mongo_db_name']]
	mongo_collection = mongo_db[settings['mongo_collection_name']]

	documents = pandas.read_csv(args.data,
							chunksize=settings['chunk_size'])
							
	write_to_mongo_db(mongo_collection, documents)
	
	pprint.pprint(mongo_collection.count())