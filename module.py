import json

# This code takes a datafile (csv or json) and chunks it out by iterating through a stepped range iterator. This will take the chunk and write it to the given file in the directory.
def chunkData():	
	# open the file
	with open('locationData.json') as infile:
		# load the file
		o = json.load(infile)
		# what is the length of the file
		length = len(o['locations'])
		# chunk size
		chunkSize = 50000
		# iterator
		rangeValue = range(0, length, chunkSize)

		# loop through stepped iterator and create a new file bases on current step and dump json into file.
		for i in rangeValue:
			with open('file_' + str(i) + '.json','w') as outfile:
				json.dump(o['locations'][i:i+chunkSize], outfile)

geojson = {
	'type': 'featureCollection',
	'features':[]
}

feature = {
	'type': 'Feature',
	'properties': {
		'timeStamp':''
	},
	'geometry':{
		'type': 'Point',
		'coordinates':[]
	}
}

def sortData(dataChunk):
	data = json.load(chunk)

	for line in data:
		# print("line", line)
		# timeStamp = feature['properties']['timeStamp']
		# coordinates = feature['coordinates']
		feature = {
			'type': 'feature',
			'properties': {
				'timeStamp':''
			},
			'geometry':{
				'type': 'Point',
				'coordinates':''
			}
		}

		dataTimeStamp = line['timestampMs']
		# print("dataTimeStamp", dataTimeStamp)

		dataLongitude = line['longitudeE7']
		# print("dataLongitude", dataLongitude)

		dataLatitude = line['latitudeE7']
		# print("dataLatitude", dataLatitude)

		dataAccuracy = line['accuracy']

		lngLat = [dataLongitude,dataLatitude]

		feature['properties']['timeStamp'] = dataTimeStamp

		feature['geometry']['coordinates'] = lngLat

		feature['properties']['accuracy'] = dataAccuracy
		# print(feature)

		geojson['features'].append(feature)


for i in range(0,1113487,50000):
    # print("i", i)
	with open('file_' + str(i) + '.json',) as chunk:
		sortData(chunk)
		# if i == 0:
		# 	print(geojson)


with open('location_data_cleaned.geojson','w') as file:
	json.dump(geojson, file)
	print('done')
