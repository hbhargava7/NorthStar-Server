from osmread import parse_file, Way, Node
import math
import MySQLCrime
from Utils import euclid

CRIMES = MySQLCrime.pull()

class MapNode:
    def __init__(self, id, lat, lon):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.point = (lat, lon)

class Edge:
    def __init__(self, node_from, node_to, dist, risk=0):
        self.node_from = node_from
        self.node_to = node_to
        self.dist = dist
        self.risk = risk

def getNodesAndEdges():
    # nodes maps {ID:MapNode}
    nodes = dict()

    #edges maps {ID:[Edge....]}
    edges = dict()

    for entity in parse_file('map.osm'):
        if isinstance(entity, Node):
             node = MapNode(entity.id, entity.lat, entity.lon)
             nodes[entity.id] = node
        if isinstance(entity, Way):
            path = entity.nodes
            for i in range(len(path)-1):
                dist = euclid(nodes[path[i]].point, nodes[path[i+1]].point)
                edge = Edge(nodes[path[i]], nodes[path[i + 1]], dist)
                if path[i] in edges:
                    edges[path[i]].append(edge)
                else:
                    edges[path[i]] = [edge]
    return (nodes, edges)
