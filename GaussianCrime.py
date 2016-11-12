from math import sqrt, pi, e
# Give a point (lat, lon), and a list of crimes,
# return the crime score for that point
def CrimeDensity(point, crimes):
    # The bandwidth h dictates the spread of the Gaussian kernel 
    # that is centered at each datapoint and hence, it controls 
    # the smoothness of the estimated density. Small values of h 
    # can capture more detail while large values of h lead to smoother
    # estimation. In other words, it is the analogue of the bin width of
    # a histogram. AKA higher h means a crime will have a bigger effect area.
    h = 1
    # number of crimes
    n = len(crimes)
    score = 0
    for c in crimes:
        score += (e ** (- (distance(c.location, point) ** 2) / (2 * h * h))) / sqrt(2*pi)
    return score / (n * h * h)

# Find the euclidean distance between 2 points (lat, lon)
def distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return sqrt(x*x + y*y)


# Tests
class Crime:
    def __init__(self, lat, lon):
        self.location = (lat, lon)

crimes = []

for i in range(5, 10):
    for j in range(5, 10):
        crimes.append(Crime(i, j))

for i in range(15):
    for j in range(15):
        print(str(round(CrimeDensity((i, j), crimes), 3)) + " | ", end = "")
    print("")