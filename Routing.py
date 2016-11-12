import MapDataParser, math, sys
import heapq

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
    heap = []
    n = 0
    for i in range(0, len(nodes)):
        if nodes[i] == start:
            n = i
            break
    for edge in edges[n]:
        heapq.heappush(heap, edge)
    while heap != [] or path[len(path) - 1] != end:
        toAdd = (heapq.heappop(heap))
        path.append(toAdd)
        for edge in edges[findChildren(toAdd.node_to)]:
            heapq.heappush(heap, edge)

    return path

def findChildren(node):
    for i in range(0, len(nodes)):
        if nodes[i] == node:
            return i

def euclid(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt(x*x + y*y)