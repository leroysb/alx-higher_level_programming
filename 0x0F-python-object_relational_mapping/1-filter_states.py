#!/usr/bin/python3
"""
module 1-filter_states: filters the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(
        host="localhost",
        port=3360,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * \
        FROM states \
        WHERE CONVERT(`name` USING Latin1) \
        COLLATE Latin1_General_CS \
        LIKE 'N%' \
        ORDER BY id ASC"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
