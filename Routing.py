from MapDataParser import euclid
import MapDataParser, math, sys
import heapq

distWeight = 1
riskWeight = 1

data = MapDataParser.getNodesAndEdges()
nodes = data[0]
edges = data[1]

class SearchNode:
    def __init__(self, node, end, prev=None):
        self.node = node
        self.toEnd = MapDataParser.euclid(node.point, end)
        self.prev = prev

    # BELOW IS ALL HEURISTICS HANDLING
    def __lt__(self, other):
        return
    def __gt__(self, other):
        return
    def __eq__(self, other):
        return
    def __ne__(self, other):
        return

def route(p1, p2):
    startNode, endNode = None, None
    bestDistFromStart, bestDistFromEnd = sys.maxint, sys.maxint
    for node in nodes:
        distFromStart = euclid(p1, nodes[node].point)
        distFromEnd = euclid(p2, nodes[node].point)
        if distFromStart < bestDistFromStart:
            startNode = node
            bestDistFromStart = distFromStart
        if distFromEnd < bestDistFromEnd:
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

