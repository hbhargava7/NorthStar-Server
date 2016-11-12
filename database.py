import mysql.connector

HOST = "ec2-54-218-21-50.us-west-2.compute.amazonaws.com:3306"
USER = "root"
PASSWORD = "adhksADHKS123!@#"
DB = "world"

db = MySQLdb.connect(host=HOST, user=ROOT, passwd=PASSWORD, db=DB)
cursor = cnx.cursor()

query = ("SELECT Name, Population FROM city "
         "WHERE Population BETWEEN %s AND %s")

lowerBound = 100000
upperBound = 100000000

cursor.execute(query, (hire_start, hire_end))

for (city, population) in cursor:
  print("{} has population {}".format(city, population))

cursor.close()
cnx.close()
