from MapDataParser import euclid
import MapDataParser, math, sys
import Utils

distWeight = 1
riskWeight = 1

data = MapDataParser.getNodesAndEdges()
nodes = data[0]
edges = data[1]

class SearchNode:
    def __init__(self, node, goal, prev=None, cost=0):
        self.node = node
        self.cost = cost
        self.prev = prev
        self.goal = goal

    # BELOW IS ALL HEURISTICS HANDLING
    def isGoalState(self):
        return self.node.id == self.goal.id

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

def findPath(start, goal):
    visited = []
    curr = start
    fringe = util.PriorityQueue()
    fringe.push(curr, 0)
    while True:
        if fringe.isEmpty():
            return []
        curr = fringe.pop()
        if curr == goal:
            return createPath(curr)
        if curr.node not in visited:
            visited.append(curr.node)
            children = edges[node.id]
            if children:
                for e in children:
                    cost = e.dist + curr.cost
                    node = SearchNode(e.end, goal, curr, cost)
                    fringe.push(node, node.cost + Utils.euclid(curr.point, goal.point))

def createPath(node):
    path = []
    curr = node
    while curr.prev:
        path.append(curr.move)
        curr = curr.prev
    path.reverse()
    return path

start = (37.86979719999999, -122.2675821)
goal = (37.8760221, -122.2588018)

print (route(start, goal))