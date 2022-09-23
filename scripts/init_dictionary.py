# coding: utf-8
import os
import csv
import sqlite3

"""
Thanks `lordli`, for this repo helped me.
https://raw.githubusercontent.com/1eez/103976/master/EnWords.csv
"""

con = sqlite3.connect("dictionary.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS word(english, chinese);")
cur.execute("DELETE FROM  word;")

with open('{}/EnWords.csv'.format(os.path.dirname(__file__)), newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    counter = 0
    for row in spamreader:
        # print(row)
        # if counter > 10:
        #     break
        # counter += 1
        row = ', '.join(row)
        if 'NULL' in row:
            continue
        en = row.split('","')[0].replace('"', '')
        cn = row.split('","')[1].replace('"', '')
        # print(en)
        # print(cn)
        cur.execute("insert into word(english, chinese) values (?, ?)", (en, cn))

        cur.execute('select count(*) from word;')
        row = cur.fetchone()
        print("count:", row[0])

        # print(len(row))
        # raise