import json

#Converts the json data into a dictionary. 
def dataToDict(url):
    with open(url) as data:
        data = json.load(data)
    return data

crimes = dataToDict("crimes.json")

#Filters the dictionary so it only include releavent fields. 
def filterDict(data, keys):

	filtered = []

	for d in data: 
		temp = {}
		for key in keys:
			if key in d:
				value = d[key]
				if (key == "block_location"):
					longitude = value["coordinates"][0]
					latitude = value["coordinates"][1]
					temp["longitude"] = longitude
					temp["latitude"] = latitude
				else: 
					temp[key] = value
		if len(temp.keys()) == 6:
			filtered.append(temp)
		# else:
		# 	print (d["caseno"])
	return filtered


keyCalls = ["block_location_address", "offense", "eventtm", "eventdt", "block_location"]
filteredCalls = filterDict(crimes, keyCalls)

