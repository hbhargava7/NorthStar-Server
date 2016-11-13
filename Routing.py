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
    bestDistFromStart, bestDistFromEnd = 999999999, 999999999
    for id in nodes.keys():
        distFromStart = Utils.euclid(p1, nodes[id].point)
        distFromEnd = Utils.euclid(p2, nodes[id].point)
        if distFromStart < bestDistFromStart:
            startNode = id
            bestDistFromStart = distFromStart
        if distFromEnd < bestDistFromEnd:
            endNode = id
            bestDistFromEnd = distFromEnd
    return findPath(nodes[startNode], nodes[endNode])

def findPath(start, goal):
    visited = []
    curr = SearchNode(start, goal)
    fringe = Utils.PriorityQueue()
    fringe.push(curr, 0)
    while True:
        if fringe.isEmpty():
            return []
        curr = fringe.pop()
        if curr.isGoalState():
            return createPath(curr)
        if curr.node not in visited:
            visited.append(curr.node)
            children = edges[curr.node.id]
            if children:
                for e in children:
                    d = e.dist
                    risk = e.calculateRisk()
                    print("distance: {}, risk: {}".format(d, risk))
                    cost = d + risk + curr.cost
                    node = SearchNode(e.end, goal, curr, cost)
                    fringe.push(node, node.cost + Utils.euclid(curr.node.point, goal.point))

def createPath(node):
    path = []
    curr = node
    print ("cost: " + str(node.cost))
    while curr:
        path.append(curr.node.point)
        curr = curr.prev
    path.reverse()
    return path


start = (37.86979719999999, -122.2675821)
goal = (37.8760221, -122.2588018)

for (x, y) in route(start, goal):
    print(str(x) + ", " + str(y))