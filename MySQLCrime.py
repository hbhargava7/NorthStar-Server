import mysql.connector 
import CrimeDataParser2

def populate(): 
	db = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com", \
								user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
	cursor = db.cursor()
	cursor.execute("DROP TABLE crimes2;")
	query = "CREATE TABLE crimes2 (offense BLOB, eventtm TIME, \
											eventdt DATE, latitude DECIMAL(10, 8) NOT NULL, longitude DECIMAL(11, 8) NOT NULL);"
	cursor.execute(query)
	for dct in CrimeDataParser2.filteredCalls: 
		qry = "INSERT INTO crimes2 (offense, eventtm, eventdt, latitude, longitude) \
				VALUES (%(offense)s, %(eventtm)s, %(eventdt)s, %(latitude)s, %(longitude)s)"
		cursor.execute(qry, dct)
	db.commit()
	cursor.close()
	db.close()


def pull(): 
	"""return a list of tuples of lat long for each crime"""
	db = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com", 	
								user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
	cursor = db.cursor()
	query = ("select latitude, longitude from crimes2")
	cursor.execute(query)
	toReturn = []
	for (lat, lon) in cursor:
		# print("{}, {}".format(float(lat), float(lon)))
		toReturn.append((float(lat), float(lon)))
	cursor.close()
	db.close()
	return toReturn

def heatmap():
    db = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com",   
                                user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
    cursor = db.cursor()
    query = ("SELECT id, risk from edges2")
    cursor.execute(query)
    toReturn = {}
    for (edgeID, risk) in cursor:
        # print("{}, {}".format(float(lat), float(lon)))
        toReturn[int(edgeID)] = float(risk)
    cursor.close()
    db.close()
    return toReturn
