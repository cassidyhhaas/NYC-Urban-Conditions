#DONE: if completed data is unknown, mean duration and fill in completed date
#DONE: if cross street is missing fill in intersection
#CANT: if there is an address -> extract zip code, street name... the fields are already filled if the information is available
from pymongo import MongoClient
from datetime import datetime, timedelta


client = MongoClient()
#change these to be whatever your 311 database is called
db = client['311'] 
collection = db['311new']


def main():
	#do a separate mean calculation for each category 
	categories = collection.distinct('Complaint Type')
	for category in categories:
		replace_completed_date(category)

	#fill intersection and cross street attributes
	replace_cross_street()


def replace_completed_date(category):
	#if completed data is unknown, find the mean duration and fill in completed date
	#get the average time for the category
	timedeltas = []
	sampled = collection.find({'Complaint Type': category})
	for entry in sampled:
		if entry['Created Date'] is not u'' and entry['Closed Date'] is not u'':
			datetime_created = datetime.strptime(entry['Created Date'], '%m/%d/%Y %I:%M:%S %p')
			datetime_closed = datetime.strptime(entry['Closed Date'], '%m/%d/%Y %I:%M:%S %p')
			timedeltas.append(datetime_closed - datetime_created)
	average_timedelta = sum(timedeltas, timedelta(0)) / len(timedeltas)
	
	#it doesnt work unless i redo the sample for some reason
	sampled = collection.find({'Complaint Type': category, 'Closed Date': ''})
	for entry in sampled:
		if entry['Created Date'] is not u'' and entry['Closed Date'] is u'': 
			new_closed = datetime.strptime(entry['Created Date'], '%m/%d/%Y %I:%M:%S %p') + average_timedelta
			new_closed = new_closed.strftime("%m/%d/%Y %I:%M:%S %p")
			collection.find_one_and_update({'_id': entry['_id']}, {'$set': {'Closed Date': new_closed}})


def replace_cross_street():
	no_cross = collection.find({'Cross Street 1': '', 'Cross Street 2': ''})
	for entry in no_cross:
		#if cross streets is empty and intersection is not
		if entry['Intersection Street 1'] is not u'' and entry['Intersection Street 2'] is not u'':
			collection.find_one_and_update({'_id': entry['_id']}, {'$set': {'Cross Street 1': entry['Intersection Street 1'], 'Cross Street 2': entry['Intersection Street 2']}})
	
	no_intersect = collection.find({'Intersection Street 1': '', 'Intersection Street 2': ''})
	for entry in no_intersect:
		#if intersection is empty and cross streets is not
		if entry['Cross Street 1'] is not u'' and entry['Cross Street 2'] is not u'':
			collection.find_one_and_update({'_id': entry['_id']}, {'$set': {'Intersection Street 1': entry['Cross Street 1'], 'Intersection Street 2': entry['Cross Street 2']}})


if __name__ == '__main__':
	main()