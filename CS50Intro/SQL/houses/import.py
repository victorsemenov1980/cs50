import csv
import re
import sys
from sys import argv, exit
import itertools
import sqlite3

# if len(argv) != 2:
#     print("Usage: python dna.py data.csv")
#     exit(1)

# with open(sys.argv[1], newline='') as csvfile:
conn = sqlite3.connect('students.db')
c=conn.cursor()
with open('characters.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        names=row['name']
        x = names.split(" ")
        if len(x)==2:
            middle='NULL'
            first=x[0]
            last=x[1]
        else:
            middle=x[1]
            first=x[0]
            last=x[2]
        c.execute("INSERT INTO students(first,middle,last,house,birth) VALUES (?,?,?,?,?)",(first,middle,last,row['house'],row['birth']))
       

    conn.commit()
    conn.close()