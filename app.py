import json 
import Routing
import MySQLMap
import MapDataParser
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

nodes, nodeEdges, edges = MapDataParser.getNodesAndEdges()
risk = MySQLMap.pull()

def processRoute(origin, destination):
	routes = Routing.route(origin, destination, nodes, nodeEdges, risk)
	results = {}
	temp = {}
	temp['route'] = routes[0]
	temp['description'] = 'Shortest Path'
	temp['travelTime'] = ''
	temp['safetyScore'] = 0
	temp['originPlaceID'] = ''
	temp['destinationPlaceID'] = ''
	results['fastestRoute'] = temp

	temp = {}
	temp['route'] = routes[1]
	temp['description'] = 'Optimum Path'
	temp['travelTime'] = ''
	temp['safetyScore'] = 0
	temp['originPlaceID'] = ''
	temp['destinationPlaceID'] = ''
	results['optimalRoute'] = temp

	temp = {}
	temp['route'] = routes[2]
	temp['description'] = 'Safest Path'
	temp['travelTime'] = ''
	temp['safetyScore'] = 0
	temp['originPlaceID'] = ''
	temp['destinationPlaceID'] = ''
	results['safestRoute'] = temp
	return {"routes": results}

@app.route('/', methods=['POST'])
def process():
	data = request.get_data()
	dictionary = json.loads(data.decode('utf-8'))
	origin = (dictionary['originLatitude'], dictionary['originLongitude'])
	destination = (dictionary['destinationLatitude'], dictionary['destinationLongitude'])
	result = processRoute(origin, destination) 
	return jsonify(result)

app.run(host="0.0.0.0", port=int("80"))



