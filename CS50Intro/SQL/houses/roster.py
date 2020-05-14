import csv
import re
import sys
from sys import argv, exit
import itertools

# if len(argv) != 2:
#     print("Usage: python dna.py data.csv")
#     exit(1)
# house=argv[1]

house='Slytherin'

import sqlite3
conn = sqlite3.connect('students.db')
c = conn.cursor()

for row in c.execute('SELECT first,middle,last,house,birth FROM students WHERE house=? ORDER BY last,first',(house,)):
        if row[1]=='NULL':
            print(row[0],row[2],', born',row[4])
        else:
            print(row[0],row[1],row[2],', born',row[4])
            

