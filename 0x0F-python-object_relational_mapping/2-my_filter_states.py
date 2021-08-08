#!/usr/bin/python3
"""
Takes an argument and displays all values in the states table of a database
where name matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cursor = db.cursor()
    sql = "SELECT * FROM `states` WHERE `name` = '{}'".format(argv[4])
    cursor.execute(sql)

    [print(state) for state in cursor.fetchall()]
