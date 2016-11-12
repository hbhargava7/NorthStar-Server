from osmread import parse_file, Way, Node
import math
import MySQLCrime
import Utils

CRIMES = MySQLCrime.pull()

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
        self.risk = Utils.CrimeDensity(self.start.point, self.closeCrimes())
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
        print ("calculateing risk")
        risk = 0
        for (lat, lon) in self.segmentize():
            risk += Utils.CrimeDensity((lat, lon), CRIMES)
        print (risk)

    def closeCrimes(self):
        close = []
        for c in CRIMES:
            if Utils.euclid(self.start.point, c) < 100 or Utils.euclid(self.end.point, c) < 100:
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
        if isinstance(entity, Way):
            path = entity.nodes
            for i in range(len(path)-1):
                # dist = Utils.euclid(nodes[path[i]].point, nodes[path[i+1]].point)
                edge = Edge(nodes[path[i]], nodes[path[i + 1]])
                if path[i] in edges:
                    edges[path[i]].append(edge)
                else:
                    edges[path[i]] = [edge]
    return (nodes, edges)

getNodesAndEdges()