from pymongo import MongoClient
import pandas as pd
import matplotlib  
import matplotlib.pyplot as plt  
import matplotlib.cm
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from matplotlib.patches import Circle
from decimal import Decimal
import argparse

def main(category, value, year):
	client = MongoClient()
	db = client.ThreeOneOneData 
	collection = db.sample0
	collection2 = db.sample1
	collection3 = db.sample2
	collection4 = db.sample3
	collection5 = db.sample4
	collection6 = db.sample5
	collection7 = db.sample6
	collection8 = db.sample7
	collection9 = db.sample8
	collection10 = db.sample9


	# category = 'LAW_CAT_CD'
	# value = 'FELONY'

	latitudeArray = []
	longitudeArray = []

	cursor = list(collection.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")

	cursor = list(collection2.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")

	cursor = list(collection3.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")

	cursor = list(collection4.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")


	cursor = list(collection5.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")

	cursor = list(collection6.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")

	cursor = list(collection7.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")


	cursor = list(collection8.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")


	cursor = list(collection9.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")


	cursor = list(collection9.find(
	{category: {'$regex': value}, "Closed Date": {'$regex' : year}}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")

	create_map(latitudeArray, longitudeArray)

#west limit and south are lower left corner, east and north are upper right corner
#westlimit=-74.25909; southlimit=40.477399; eastlimit=-73.700272; northlimit=40.917577
def create_map(latitudeArray, longitudeArray):

	LOW_LEFT_CORNR_LONGITUDE = -74.260380
	LOW_LEFT_CORNER_LATITUDE = 40.485808
	UP_RIGHT_CORNER_LONGITUDE = -73.699206
	UP_RIGHT_CORNER_LATITUDE = 40.917691


	MIN_NYC_ISLAND_TO_VISUALIZ = 0.6

	# Create the Basemap

	m = Basemap(llcrnrlon=LOW_LEFT_CORNR_LONGITUDE,
	            llcrnrlat=LOW_LEFT_CORNER_LATITUDE,
	            urcrnrlon=UP_RIGHT_CORNER_LONGITUDE,
	            urcrnrlat=UP_RIGHT_CORNER_LATITUDE,
	            ellps='WGS84',
	            resolution='h',
	            area_thresh=MIN_NYC_ISLAND_TO_VISUALIZ)

	m.drawcoastlines()
	m.fillcontinents(color="#ebebeb")
	m.drawcountries(linewidth=3)
	m.drawstates()
	m.drawrivers()

	m.drawmapboundary(fill_color='#ffffff')

	m.readshapefile('zipshape/cb_2016_us_zcta510_500k', 'zip')

	plt.scatter(longitudeArray, latitudeArray, marker='.', s=2, color="#006767", zorder=10)
	plt.show()
 

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Data Mining NYC')
	parser.add_argument('-a', type=str,
							help="Attribute to Plot", 
							required=True)
	parser.add_argument("-v", type=str, 
							help="Desired Attribute Value (As a Regular Expression)", 
							required=True)
	parser.add_argument("-y", type=str, 
							help="Year (As a Regular Expression)", 
							required=True)

	args = parser.parse_args()

	main(args.a, args.v, args.y)