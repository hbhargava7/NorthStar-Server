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
        self.dist = Utils.euclid(self.start, self.end)
        self.risk = risk 
        self.calculateRisk()

    def norm(self):
        x = self.start.lat - self.end.lat
        y = self.end.lon - self.end.lon
        return (x / self.length, y / self.length)

    # Return array of segmented points between 2 end points
    def segmentize(self):
        (dx, dy) = self.norm()
        x = self.start.lat
        y = self.start.lon
        points = []
        for i in range(floor(self.length)):
            x += dx
            y += dy
            points.append(x, y)
        return points

    def calculateRisk(self):
        curr = (self.start.lat, self.start.lon)
        for (lat, lon) in self.segmentize:
            print (Utils.euclid(curr , (lat, lon)))
            curr = (lat, lon)

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
