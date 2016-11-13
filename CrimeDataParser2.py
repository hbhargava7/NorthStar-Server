import json

#Converts the json data into a dictionary. 
def dataToDict(url):
    with open(url) as data:
        data = json.load(data)
    return data

crimes = dataToDict("data/crimes2.json")['data']

keyCalls = ["block_location_address", "offense", "eventtm", "eventdt", "block_location"]

def parseData(): 
	filtered = []
	for crime in crimes: 
		temp = {}
		temp['offense'] = crime[9]
		temp['eventtm'] = crime[11]
		temp['eventdt'] = crime[10]
		temp['longitude'] = crime[15][2]
		temp['latitude'] = crime[15][1]
		filtered.append(temp)
	return filtered

filteredCalls = parseData() 







