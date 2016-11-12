from osmread import parse_file, Way, Node
import math

class MapNode:
    def __init__(self, id, lat, lon):
        self.id = id
        self.lat = lat
        self.lon = lon

class Edge:
    def __init__(self, node_from, node_to, dist, risk=0):
        self.node_from = node_from
        self.node_to = node_to
        self.dist = dist
        self.risk = risk
    def setRisk(self, risk):
        self.risk = risk

# Haversine degree to meter conversion
def euclid(p1, p2):
    R = 6371 * 10e3 # km
    dlon = math.radians(p2[0] - p1[0])
    dlat = math.radians(p2[1] - p1[1])
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(p1[1])) * math.cos(math.radians(p2[1]))\
                                            * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

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
                dist = euclid((nodes[path[i]].lon,nodes[path[i]].lat),(nodes[path[i+1]].lon,nodes[path[i+1]].lat))
                print(dist)
                edge = Edge(nodes[path[i]], nodes[path[i + 1]], dist)

                if path[i] in edges:
                    edges[path[i]].append(edge)
                else:
                    edges[path[i]] = [edge]
    return (nodes, edges)