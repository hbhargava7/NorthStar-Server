# Give a point (lat, long), and a list of crimes,
# return the crime score for that point
def CrimeDensity(point, crimes):
    # The bandwidth h dictates the spread of the Gaussian kernel 
    # that is centered at each datapoint and hence, it controls 
    # the smoothness of the estimated density. Small values of h 
    # can capture more detail while large values of h lead to smoother
    # estimation. In other words, it is the analogue of the bin width of
    # a histogram.
    h = 1
    # number of crimes
    n = len(crimes)
    score = 0
    for c in crimes:

# Find the euclidean distance between 2 points (lat, long)
def distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]