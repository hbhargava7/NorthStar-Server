import mysql.connector 
import CrimeDataParser
import datetime

def populate(): 
	db = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com", \
								user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
	cursor = db.cursor()
	cursor.execute("DROP TABLE crimes;")
	query = "CREATE TABLE crimes (block_location_address BLOB, offense BLOB, eventtm TIME, \
											eventdt DATE, latitude DECIMAL(10, 8) NOT NULL, longitude DECIMAL(11, 8) NOT NULL);"
	cursor.execute(query)
	for dct in CrimeDataParser.filteredCalls: 
		qry = "INSERT INTO crimes (block_location_address, offense, eventtm, eventdt, latitude, longitude) \
				VALUES (%(block_location_address)s, %(offense)s, %(eventtm)s, %(eventdt)s, %(latitude)s, %(longitude)s)"
		cursor.execute(qry, dct)
	db.commit()
	cursor.close()
	db.close()


def pull(): 
	"""return a list of tuples of lat long for each crime"""
	db = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com", 	
								user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
	cursor = db.cursor()
	# start1 = datetime.time(20,0,0)
	# end1 = datetime.time(23,59,59)
	# start2 = datetime.time(0,0,0)
	# end2 = datetime.time(6,0,0)
	# query = ("SELECT latitude, longitude from crimes WHERE eventtm BETWEEN %s AND %s OR eventtm BETWEEN %s AND %s")
	# cursor.execute(query, (start1, end1, start2, end2))
	query = ("select latitude, longitude from crimes")
	cursor.execute(query)
	toReturn = []
	for (lat, lon) in cursor:
		# print("{}, {}".format(float(lat), float(lon)))
		toReturn.append((float(lat), float(lon)))
	cursor.close()
	db.close()
	return toReturn

populate()
