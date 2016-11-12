from threading import Thread
import urllib 
import re 
import mysql.connector
import data


conn = mysql.connector.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com", user="Admin", passwd="CalHacks2016!", db="world")

x = conn.cursor()
query = "CREATE TABLE crimes (block_location_address offense eventtm eventdt block_location);"

for dct in data.filteredCalls: 
	for key in dct:
		query = "INSERT INTO crimes (" + str(key) + ") values (" + str(dct[key]) + ")"
		print (query)
		x.execute(query)




