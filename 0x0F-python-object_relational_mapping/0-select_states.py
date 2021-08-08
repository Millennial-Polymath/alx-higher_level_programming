#!/usr/bin/python3
"""
Module contains a script that lists all states from the db hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ =="__main__":
    db = MySQLdb.connect(host="localhot", port=3306, user=argv[1], password=argv[2],
                         database=argv[3])
    cursor = db.cursor()
    sql = "SELECT * FROM `states` ORDER BY `id` ASC;"

    cursor.execute(sql)
    [print(state) for state in cursor.fetchall()]
    db.close()
