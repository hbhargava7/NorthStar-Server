import MySQLdb
import datetime

THEHOST="localhost"
THEUSER="user"
THEPASSWD="passwd"
THEDB="database"

connection=MySQLdb.connect(
    host=THEHOST,user=THEUSER,passwd=THEPASSWD,db=THEDB)
cursor=connection.cursor()

abc,efg,ijk=1,2,3

data={'1': ['1', 'K', abc, 'xyz', None, None, None, datetime.date(2009, 6, 18)],
      '2': ['2', 'K', efg, 'xyz', None, None, None, None],
      '3': ['3', 'K', ijk, 'xyz', None, None, None,
            datetime.datetime(2010, 2, 5, 16, 31, 2)]}

sql='''\
CREATE TABLE IF NOT EXISTS temp (id int auto_increment primary key,
    field1 varchar(8),
    field2 int,
    field3 varchar(8),
    field4 bool,
    field5 varchar(8),
    field6 varchar(8),
    field7 datetime )'''

cursor.execute(sql)

sql='''\
INSERT INTO temp (id, field1, field2, field3, field4, field5, field6, field7)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
'''
cursor.executemany(sql, data.values())