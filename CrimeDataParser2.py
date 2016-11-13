import json

#Converts the json data into a dictionary. 
def dataToDict(url):
    with open(url) as data:
        data = json.load(data)
    return data

crimes = dataToDict("data/crimes2.json")['data']
CRIMETYPES = ["ASSAULT/BATTERY FEL.","ASSAULT/BATTERY MISD.", "BRANDISHING", "BURGLARY RESIDENTIAL", "GUN/WEAPON", \
			"ROBBERY", "SEXUAL ASSAULT FEL.", "SEXUAL ASSAULT MISD.", "THEFT FELONY (OVER $950)", "THEFT FROM PERSON", \
			"THEFT MISD. (UNDER $950)"]

def parseData(): 
	filtered = []
	for crime in crimes:
		if crime[9] and crime[11] and crime[10] and crime[15][2] and crime[15][1] and crime[9] in CRIMETYPES:
			temp = {}
			temp['offense'] = crime[9]
			temp['eventtm'] = crime[11]
			temp['eventdt'] = crime[10]
			temp['longitude'] = crime[15][2]
			temp['latitude'] = crime[15][1]
			filtered.append(temp)
	return filtered

filteredCalls = parseData() 







