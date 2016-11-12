import math

# Give a point (lat, lon), and a list of crimes,
# return the crime score for that point
def CrimeDensity(point, crimes):
    if not crimes:
        print ("no crimes")
        return 0
    # The bandwidth h dictates the spread of the Gaussian kernel 
    # that is centered at each datapoint and hence, it controls 
    # the smoothness of the estimated density. Small values of h 
    # can capture more detail while large values of h lead to smoother
    # estimation. In other words, it is the analogue of the bin width of
    # a histogram. AKA higher h means a crime will have a bigger effect area.
    h = 10
    # number of crimes
    n = len(crimes)
    score = 0
    for c in crimes:
        score += (math.e ** (- (euclid(c, point) ** 2) / (2 * h * h))) / math.sqrt(2*math.pi)
    return score / (n * h * h)

# # Find the euclidean distance between 2 points (lat, lon)
# def distance(p1, p2):
#     y = p1[0] - p2[0]
#     x = p1[1] - p2[1]
#     return math.sqrt(x*x + y*y)

# Haversine degree to meter conversion
def euclid(p1, p2):
    R = 6371 * 10e3 # km
    dlon = math.radians(p2[1] - p1[1])
    dlat = math.radians(p2[0] - p1[0])
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(p1[0])) * math.cos(math.radians(p2[0]))\
                                              * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c
