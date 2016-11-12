from threading import Thread
import urllib 
import re 
import MySQLdb 
import data


conn = mySQLdb.connect(host="host", user="user",password="password", db="dbname")

query = "INSERT INTO table_name (field) values ('value')" 
x = conn.cursor()
x.execute(query)

for dct in filteredCalls: 
	for key in dct:
		query = "INSERT INTO hello (" + str(key) + ") values (" + str(dct[key])
		x = conn.cursor()
		x.execute(query)




