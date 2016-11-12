from threading import Thread
import urllib 
import re 
import mysql.connector
import data


conn = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com", user="Admin", passwd="CalHacks2016!", db="berkeley_crimes")
x = conn.cursor()


def populate(): 
	query = "CREATE TABLE crimes (block_location_address offense eventtm eventdt block_location);"
	x.execute(query)
	for dct in data.filteredCalls: 
		for key in dct:
			qmarks = ', '.join('?' * len(dct))
			qry = "INSERT INTO Table (%s) Values (%s)" % (qmarks, qmarks)
			cursor.execute(qry, dct.keys() + dct.values())


def pull(): 
	"""return a list of tuples of lat long for each crime""

