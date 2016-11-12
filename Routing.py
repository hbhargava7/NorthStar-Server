import MapDataParser, math, sys

data = MapDataParser.getNodesAndEdges()
nodes = data[0]
edges = data[1]

def route(p1, p2):
    startNode, endNode = None, None
    bestDistFromStart, bestDistFromEnd = sys.maxint, sys.maxint
    for node in nodes:
        distFromStart = euclid(p1, (nodes[node].lat, nodes[node].lon))
        distFromEnd = euclid(p2, (nodes[node].lat, nodes[node].lon))
        if startNode is None or distFromStart < bestDistFromStart:
            startNode = node
            bestDistFromStart = distFromStart
        if endNode is None or distFromEnd < bestDistFromEnd:
            endNode = node
            bestDistFromEnd = distFromEnd
    return findPath(startNode, endNode)

def findPath(start, end):
    path = []

    return path


def euclid(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(x*x + y*y)