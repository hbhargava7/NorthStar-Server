import json

#Converts the json data into a dictionary. 
def dataToDict(url):
    with open(url) as data:
        data = json.load(data)
    return data

callsForService = dataToDict("callsForService.json")
stopData = dataToDict("stopData.json")


#Filters the dictionary so it only include releavent fields. 
def filterDict(data, keys):

	filtered = []

	for dict in data: 
		temp = {k: v for k, v in dict.items() if k in keys}
		filtered.append(temp)

	return filtered


keyCalls = ["block_location_address", "offense", "eventtm", "eventdt", "block_location"]
filteredCalls = filterDict(callsForService, keyCalls)




