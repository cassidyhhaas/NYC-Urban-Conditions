from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt


def main():
	client = MongoClient()

	db = client['311'] #change this to be whatever you called your 311 database
	collection = db['311']
	
	#dataset is huge so sample the collection MAKE THIS RANDOM SAMPLING
	sampled = collection.find().limit(100000)
	
	#category = 'PLUMBING'
	#category = 'GENERAL CONSTRUCTION'
	#category = 'NONCONST'
	#category = 'PAINT - PLASTER'
	category = 'HEATING'

	x, y = splitTypes(category, sampled)
	create_map(x, y, category)


#make separate heat maps for different complaint types
def splitTypes(type, sampled):
	locations = []
	x = []
	y = []
	for entry in sampled:
		if entry['Complaint Type'] == type and entry['Latitude'] is not u'':
			lat = entry['Latitude']
			lon = entry['Longitude']
			location = (lat, lon)
			locations.append(location)
			x.append(lat)
			y.append(lon)

	xnp = np.array(x).astype(np.float)
	ynp = np.array(y).astype(np.float)
	return xnp, ynp


#use this sample's lat and long to plot points on a heatmap
#TO-DO: OVERLAY OVER NYC MAP
def create_map(longs, lats, category):
	heatmap, xedges, yedges = np.histogram2d(longs, lats, bins=(64, 64))
	extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

	plt.clf()
	plt.title(category)
	plt.imshow(heatmap.T, extent=extent, origin='lower')
	plt.show()


if __name__ == '__main__':
	main()