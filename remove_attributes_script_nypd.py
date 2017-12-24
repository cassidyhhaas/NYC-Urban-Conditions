import pymongo
from pymongo import MongoClient

#This is for nypd complaint data
settings = {
    'mongo_db_name': 'NYPDData',
    'mongo_collection_name': 'NYPDData',
}

if __name__ == "__main__":

    mongo_client = MongoClient()
    mongo_db = mongo_client[settings['mongo_db_name']]
    mongo_collection = mongo_db[settings['mongo_collection_name']]

    #this uses update to remove the attribute add multi is how you tell it to remove all, not just the first instance of tht attribute
    mongo_collection.update({},{'$unset': {'KY_CD':1}},multi=True);
    mongo_collection.update({},{'$unset': {'PD_CD':1}},multi=True);
    mongo_collection.update({},{'$unset': {'CMPLNT_TO_TM':1}},multi=True);
    mongo_collection.update({},{'$unset': {'CMPLNT_TO_DT':1}},multi=True);
    mongo_collection.update({},{'$unset': {'HADEVELOPT':1}},multi=True);
    mongo_collection.update({},{'$unset': {'JURIS_DESC':1}},multi=True);
    mongo_collection.update({},{'$unset': {'LOC_OF_OCCUR_DESC':1}},multi=True);
    mongo_collection.update({},{'$unset': {'X_COORD_CD':1}},multi=True);
    mongo_collection.update({},{'$unset': {'Y_COORD_CD':1}},multi=True);
    mongo_collection.update({},{'$unset': {'PD_DESC':1}},multi=True);

