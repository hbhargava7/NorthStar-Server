import MapDataParser, math, sys
import Utils
import MySQLMap

distWeight = 1
riskWeight = 1

class SearchNode:
    def __init__(self, node, goal, prev=None, cost=0):
        self.node = node
        self.cost = cost
        self.prev = prev
        self.goal = goal

    # BELOW IS ALL HEURISTICS HANDLING
    def isGoalState(self):
        return self.node.id == self.goal.id

    def __eq__(self, other):
        self.node.id == other.node.id

def route(p1, p2, nodes, nodeEdges, risk):
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
    paths = []
    paths.append(findPath(nodes[startNode], nodes[endNode], nodes, nodeEdges, risk, 1, 0, 1))
    paths.append(findPath(nodes[startNode], nodes[endNode], nodes, nodeEdges, risk, 1, 1, 1))
    paths.append(findPath(nodes[startNode], nodes[endNode], nodes, nodeEdges, risk, 0.1, 100, 0.5))
    return paths

def findPath(start, goal, nodes, nodeEdges, risk, a, b, c):
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
        if curr.node.id not in visited:
            visited.append(curr.node.id)
            children = nodeEdges[curr.node.id]
            if children:
                for e in children:
                    d = e.dist
                    r = risk[e.id]
                    # print("distance: {}, r: {}".format(d, r))
                    cost = a*d + b*r + curr.cost
                    node = SearchNode(e.other(curr.node), goal, curr, cost)
                    fringe.push(node, node.cost + c*Utils.euclid(curr.node.point, goal.point))

def createPath(node):
    path = []
    curr = node
    while curr:
        path.append([curr.node.point[0], curr.node.point[1]])
        curr = curr.prev
    path.reverse()
    return path
