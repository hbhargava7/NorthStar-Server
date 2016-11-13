import mysql.connector 
import MapDataParser
from tqdm import tqdm

def populate():
    nodes, nodeEdges, edges = MapDataParser.getNodesAndEdges()

    db = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com", \
                                user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
    cursor = db.cursor()
    cursor.execute("DROP TABLE edges;")
    query = "CREATE TABLE edges (id BIGINT, risk DECIMAL(10, 4));"
    cursor.execute(query)
    for edgeID in tqdm(edges):
        risk = edges[edgeID].calculateRisk()
        qry = "INSERT INTO edges (id, risk) VALUES (%s, %s)"
        cursor.execute(qry, (edgeID, risk))

    db.commit()
    cursor.close()
    db.close()


def pull(): 
    """return a list of tuples of lat long for each crime"""
    db = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com",   
                                user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
    cursor = db.cursor()
    query = ("SELECT id, risk from edges")
    cursor.execute(query)
    toReturn = {}
    for (edgeID, risk) in cursor:
        # print("{}, {}".format(float(lat), float(lon)))
        toReturn[int(edgeID)] = float(risk)
    cursor.close()
    db.close()
    return toReturn

populate()
