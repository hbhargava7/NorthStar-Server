import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import Utils

# Gaussian Blur test
def blur():
    class Crime:
        def __init__(self, lat, lon):
            self.location = (lat, lon)

    crimes = []

    for i in range(10):
        crimes.append(Crime(5, 5))

    for i in range(5):
        crimes.append(Crime(15, 15))

    for i in range(10):
        crimes.append(Crime(0, 5))

    X = []
    Y = []
    Z = []
    n = 0
    for i in range(15):
        for j in range(15):
            crime = Utils.CrimeDensity((i, j), crimes)
            X.append(i)
            Y.append(j)
            Z.append(crime)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z, c='r', marker='o')
    plt.show()

def pq():
    q = Utils.PriorityQueue()
    q.push(7, 1)
    q.push(6, 2)
    q.push(3, 5)
    q.push(4, 4)
    q.push(5, 3)
    q.push(1, 7)
    q.push(2, 6)
    for i in range(6):
        print(q.pop())
