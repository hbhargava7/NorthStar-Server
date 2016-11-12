import json

def dataToDict(url):
    with open(url) as data:
        data = json.load(data)
    return data

callsForService = dataToDict("callsForService.json")
stopData = dataToDict("stopData.json")





