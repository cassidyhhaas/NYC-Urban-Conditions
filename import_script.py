#!/usr/bin/python3.5

import argparse
import pymongo;
import csv;

parser = argparse.ArgumentParser(description = 'Data Import Script');
parser.add_argument('-data', type = str, help = 'Data file. Expects a csv', required = True);
parser.add_argument('-db', type = str, help = 'Name of the database (if you don\'t have one for the provided name, one will be created)', required = True);
parser.add_argument('-c', type = str, help = 'Name of the collection (if you don\'t have one for the provided name, one will be created)', required = True);
parser.add_argument('-n', type = str, help = 'Number of rows to add', default = -1, required = False);
args = parser.parse_args();

print('Connecting to database...');
from pymongo import MongoClient;
client = MongoClient();
db = client[args.db];
collection = db[args.c];
startingSize = collection.count();

print('Copying file contents...')
datafile = args.data;
readRows = 0;
with open(datafile, encoding='utf-8') as csvfile:
	tupleReader = csv.reader(csvfile);
	titles = next(tupleReader);
	bufferCount = 0;
	documents = [];
	for row in tupleReader:
		document = {};
		for i in range(0, len(titles)):
			document[titles[i]] = row[i];
		
		documents.append(document);

		bufferCount += 1;
		readRows += 1;
		if(bufferCount >= 1000):
			collection.insert_many(documents);
			bufferCount = 0;
			del documents[:];

		if(readRows % 10000 == 0):
			print("{:.1f}%".format(100 * readRows / int(args.n)));

		if(readRows == int(args.n)):
			break;

	if(len(documents) > 0):
		collection.insert_many(documents);

print(str(collection.count() - startingSize) + ' documents were added (' + str(collection.count()) + ' total documents)');
