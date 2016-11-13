# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import cm
# import numpy as np
import Utils
import MySQLMap
import Routing
import MapDataParser

# Gaussian Blur test
# def blur():
#     class Crime:
#         def __init__(self, lat, lon):
#             self.location = (lat, lon)

#     crimes = []

#     for i in range(10):
#         crimes.append(Crime(5, 5))

#     for i in range(5):
#         crimes.append(Crime(15, 15))

#     for i in range(10):
#         crimes.append(Crime(0, 5))

#     X = []
#     Y = []
#     Z = []
#     n = 0
#     for i in range(15):
#         for j in range(15):
#             crime = Utils.CrimeDensity((i, j), crimes)
#             X.append(i)
#             Y.append(j)
#             Z.append(crime)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.scatter(X, Y, Z, c='r', marker='o')
#     plt.show()
nodes, nodeEdges, edges = MapDataParser.getNodesAndEdges()
risk = MySQLMap.pull()
def route(a, b, c):
    # print(Routing.route((37.862075, -122.262564), (37.8762594, -122.258591), nodes, nodeEdges, risk))
    for (x, y) in Routing.route((37.865766, -122.267594), (37.872186, -122.268399), nodes, nodeEdges, risk, a, b, c)[0]:
        print (str(x) + ", " + str(y))
