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
	results = []
	for route in routes:
		temp = {}
		temp['route'] = route
		temp['description'] = ''
		temp['traveTime'] = ''
		temp['safetyScore'] = 0
		temp['originPlaceID'] = ''
		temp['destinationPlaceID'] = ''
		results.append(temp)
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



