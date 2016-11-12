from osmread import parse_file, Way, Node

class MapNode:
    def __init__(self, id, lat, lon):
        self.id = id
        self.lat = lat
        self.lon = lon

class Edge:
    def __init__(self, node_from, node_to, risk=0):
        self.node_from = node_from
        self.node_to = node_to
        self.risk = risk
    def setRisk(self, risk):
        self.risk = risk


def main():
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
                edge = Edge(nodes[path[i]], nodes[path[i + 1]])
                if path[i] in edges:
                    edges[path[i]].append(edge)
                else:
                    edges[path[i]] = [edge]
    return (nodes, edges)

if __name__ == "main":
    main()



