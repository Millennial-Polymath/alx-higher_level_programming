#!/usr/bin/python3
"""
lists all states with a name starting with N
"""
import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                     password=argv[2], database=argv[3])
cursor = db.cursor()
sql = "SELECT * FROM states ORDER BY id;"
cursor.execute(sql)
[print(state) for state in cursor.fetchall() if state[1].startswith('N')]
db.close()
