import pymongo
from pymongo import MongoClient

#This is for 311 complaint data
settings = {
    'mongo_db_name': '311',
    'mongo_collection_name': '311',
}

if __name__ == "__main__":

	mongo_client = MongoClient()
	mongo_db = mongo_client[settings['mongo_db_name']]
	mongo_collection = mongo_db[settings['mongo_collection_name']]

    #this uses update to remove the attribute add multi is how you tell it to remove all, not just the first instance of tht attribute
	mongo_collection.update({}, {'$unset': {'Taxi Company Borough':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'X Coordinate (state Plane)':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'Y Coordinate (state Plane)':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'Agency':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'City':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'Ferry Direction':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'Bridge Highway Direction':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'Bridge Highway Segment':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'Community Board':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'School Code':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'School Address':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'School Number':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'School Not Found':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'School Phone Number':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'Road Ramp':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'Vehicle Type':1}}, multi=True)
	
	mongo_collection.update({}, {'$unset': {'School City':1}}, multi=True)
	mongo_collection.update({}, {'$unset': {'School State':1}}, multi=True)