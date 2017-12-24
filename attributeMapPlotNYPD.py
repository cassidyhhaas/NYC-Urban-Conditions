from pymongo import MongoClient
import pandas as pd
import matplotlib  
import matplotlib.pyplot as plt  
#Inline Plotting for Ipython Notebook 
import matplotlib.cm
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from matplotlib.patches import Circle
from decimal import Decimal
import argparse

def main(category, value):
	client = MongoClient()

	db = client.NYPDData
	collection = db.NYPDData


	latitudeArray = []
	longitudeArray = []


	cursor = list(collection.find(
	{category: value}, {"Longitude": 1, "Latitude": 1, "_id": 0}).limit(1000))
	for obj in cursor:
		try:
			x = float(obj["Longitude"])
			y = float(obj["Latitude"])
			latitudeArray.append(y)
			longitudeArray.append(x)
		except ValueError:
			print("Value Error")

	create_map(latitudeArray, longitudeArray)


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
	parser = argparse.ArgumentParser(description='Data Mining HW2')
	parser.add_argument('-a', type=str,
							help="Attribute to Plot", 
							required=True)
	parser.add_argument("-v", type=str, 
							help="Desired Attribute Value", 
							required=True)

	args = parser.parse_args()

	main(args.a, args.v)