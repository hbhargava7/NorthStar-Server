import json 
import Routing
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def processRoute(origin, destination): 
	result = {}
	myRoute = route(origin, destination)
	result['route'] = ''
	result['description'] = ''
	result['traveTime'] = ''
	result['safetyScore'] = 0
	result['originPlaceID'] = ''
	result['destinationPlaceID'] = ''
	return result 

@app.route('/', methods=['POST'])
def process():
	data = request.get_data()
	dictionary = json.load(data)
	origin = (dictionary['originLatitude'], dictionary['originLongitude'])
	destination = (dictionary['destinationLatitude'], dictionary['destinationLongitude'])
	result = processRoute(origin, destination)
	return flask.jsonify(result) 

app.run(host="0.0.0.0", port=int("80"))
hello()



# JSON INPUT
# {
#   "originPlaceID" : "ChIJ_TFLOS98hYARwTgvAjYUpjI",
#   "originLongitude" : -122.258655,
#   "destinationLatitude" : 37.8632322,
#   "destinationLongitude" : -122.255017,
#   "destinationPlaceID" : "ChIJcQI-nC18hYAROYFsz3rwV98",
#   "originLatitude" : 37.867621
# }

# {
# 	routes : [
# 		{
# 			description : string,
# 			travelTime : string,
# 			safetyScore : float,
# 			timeScore : float,
# 			originPlaceID : string,
# 			destinationPlaceID : string,
# 			route : [
# 				[lat, long],
# 				[lat, long],
# 				[lat, long],
# 				etc.
# 			]
# 		},
# 		etc.
# 	]
# }




