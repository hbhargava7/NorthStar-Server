from threading import Thread
import urllib 
import re 
import MySQLdb 
import data


conn = mySQLdb.connect(host="ec2-54-218-21-50.us-west-2.compute.amazonaws.com:3306", user="root", passwd="adhksADHKS123!@#", db="world")

query = "INSERT INTO table_name (field) values ('value')" 
x = conn.cursor()
x.execute(query)

for dct in filteredCalls: 
	for key in dct:
		query = "INSERT INTO hello (" + str(key) + ") values (" + str(dct[key])
		x = conn.cursor()
		x.execute(query)




