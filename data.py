import json
from pprint import pprint

def dataToDict(String url): 
	with open(url, 'r') as fp:
    #List of Dictionaries 
    data = json.load(fp)
    return data

callsForService = dataToDict("callsForService.json")
stopData = dataToDict("stopData.json")




