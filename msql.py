from threading import Thread
import urllib 
import re 
import mysql.connector
import data


conn = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com", user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
x = conn.cursor()


def populate(): 
	x.execute("DROP TABLE crimes;")
	query = "CREATE TABLE crimes (block_location_address BLOB, offense BLOB, eventtm BLOB, eventdt BLOB, latitude BLOB, longitude BLOB);"
	x.execute(query)
	for dct in data.filteredCalls: 
		for key in dct:
			qmarks = ', '.join('?' * len(dct))
			qry = "INSERT INTO crimes (%s) VALUES (%s)" % (qmarks, qmarks)
			print(dct.keys())
			print(dct.values())
			x.execute(qry, dct.keys(), dct.values())


def pull(): 
	"""return a list of tuples of lat long for each crime"""

populate()