from osmread import parse_file, Way, Node
import math
# import MySQLCrime
import Utils
from crimes import CRIMES

ALLOWED = ["motorway", "trunk", "primary", "secondary", "tertiary", "unclassified",\
                    "residential", "living_street", "motorway_link", "trunk_link", "primary_link",\
                    "secondary_link", "tertiary_link"]

class MapNode:
    def __init__(self, id, lat, lon):
        self.id = id
        self.lat = lat
        self.lon = lon
        self.point = (lat, lon)

class Edge:
    def __init__(self, node_from, node_to, risk=0):
        self.start = node_from
        self.end = node_to
        self.dist = Utils.euclid(self.start.point, self.end.point)
        # self.risk = Utils.CrimeDensity(self.start.point, self.closeCrimes())
        # print (self.risk)
        # self.risk = 0

    def norm(self):
        x = self.end.lat - self.start.lat
        y = self.end.lon - self.start.lon
        return (x / self.dist, y / self.dist)

    # Return array of segmented points between 2 end points
    def segmentize(self):
        (dx, dy) = self.norm()
        x = self.start.lat
        y = self.start.lon
        points = []
        for i in range(math.floor(self.dist)):
            x += dx
            y += dy
            points.append((x, y))
        return points

    def calculateRisk(self):
        risk = 0
        close = self.closeCrimes()
        if close:
            for (lat, lon) in self.segmentize():
                risk += Utils.CrimeDensity((lat, lon), close)
        return risk

    def closeCrimes(self):
        close = []
        for c in CRIMES:
            if Utils.euclid(self.start.point, c) < 1000 or Utils.euclid(self.end.point, c) < 1000:
                close.append(c)
        return close

def getNodesAndEdges():
    # nodes maps {ID:MapNode}
    nodes = dict()

    #edges maps {ID:[Edge....]}
    edges = dict()

    for entity in parse_file('map.osm'):
        if isinstance(entity, Node):
             node = MapNode(entity.id, entity.lat, entity.lon)
             nodes[entity.id] = node
        if isinstance(entity, Way) and 'highway' in entity.tags:
            path = entity.nodes
            for i in range(len(path)-1):
                # dist = Utils.euclid(nodes[path[i]].point, nodes[path[i+1]].point)
                edge = Edge(nodes[path[i]], nodes[path[i + 1]])
                backEdge = Edge(nodes[path[i + 1]], nodes[path[i]])
                if path[i] in edges:
                    edges[path[i]].append(edge)
                else:
                    edges[path[i]] = [edge]
                if path[i + 1] in edges:
                    edges[path[i + 1]].append(backEdge)
                else:
                    edges[path[i + 1]] = [backEdge]
    prunedNodes = dict()
    for id in nodes.keys():
        if id in edges:
            prunedNodes[id] = nodes[id]
    return (prunedNodes, edges)