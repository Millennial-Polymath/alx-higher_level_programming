#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of the state
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cursor = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities INNER \
    JOIN states on cities.state_id = states.id"
    cursor.execute(sql)
    print(", ".join([city[1] for city in cursor.fetchall()
                     if city[2] == argv[4]]))
