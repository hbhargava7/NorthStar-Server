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
    def __init__(self, id, n1, n2):
        self.id = id
        self.n1 = n1
        self.n2 = n2
        self.dist = Utils.euclid(self.n1.point, self.n2.point)
        # self.risk = Utils.CrimeDensity(self.n1.point, self.closeCrimes())
        # print (self.risk)
        # self.risk = 0

    def norm(self):
        x = self.n2.lat - self.n1.lat
        y = self.n2.lon - self.n1.lon
        return (x / self.dist, y / self.dist)

    # Return array of segmented points between 2 n2 points
    def segmentize(self):
        (dx, dy) = self.norm()
        (x, y) = self.n1.point
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
            if Utils.euclid(self.n1.point, c) < 1000 or Utils.euclid(self.n2.point, c) < 1000:
                close.append(c)
        return close

    def other(self, curr):
        if curr.id == self.n1.id:
            return self.n2
        return self.n1

def getNodesAndEdges():
    # nodes maps {ID:MapNode}
    nodes = dict()

    #edges maps {ID:[Edge....]}
    nodeEdges = dict()

    #edges {ID: Edge}
    edges = dict()

    for entity in parse_file('map.osm'):
        if isinstance(entity, Node):
             node = MapNode(entity.id, entity.lat, entity.lon)
             nodes[entity.id] = node
        if isinstance(entity, Way) and 'highway' in entity.tags:
            path = entity.nodes
            edgeID = entity.id
            for i in range(len(path)-1):
                # dist = Utils.euclid(nodes[path[i]].point, nodes[path[i+1]].point)
                n1ID = path[i]
                n2ID = path[i + 1]
                edge = Edge(edgeID, nodes[n1ID], nodes[n2ID])
                edges[edgeID] = edge
                if n1ID in nodeEdges:
                    nodeEdges[n1ID].append(edge)
                else:
                    nodeEdges[n1ID] = [edge]
                if n2ID in nodeEdges:
                    nodeEdges[n2ID].append(edge)
                else:
                    nodeEdges[n2ID] = [edge]
    prunedNodes = dict()
    for nID in nodes.keys():
        if nID in nodeEdges:
            prunedNodes[nID] = nodes[nID]
    return (prunedNodes, nodeEdges, edges)