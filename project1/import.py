#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:35:13 2020

@author: user
"""
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# import requests
# res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "LQ1D378SOCttnAhqzexeMA", "isbns": "9781632168146"})
# print(res.json())



engine = create_engine("postgres://iqcqqdbqmphuft:ca336b0adf47ff9393ef2e2d01b201d165cf80929c922c204d23bdfbcba36379@ec2-34-200-72-77.compute-1.amazonaws.com:5432/d328v5u9cu47oh")
db = scoped_session(sessionmaker(bind=engine))


file = open("books.csv")

reader = csv.reader(file)

for isbn, title, author, year in reader:

    db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                {"isbn": isbn, 
                  "title": title,
                  "author": author,
                  "year": year})

    print(f"Added book {title} to database.")

    db.commit()

# email='test6@yahoo.com'
# password='qwerty'
# db.execute("INSERT INTO users (email,password) VALUES (:a,:b)",{"a":email,"b":password})
# db.commit()

# email='test6@yahoo.com'
# password='qwerty'
# data=db.execute("SELECT * FROM users WHERE email = :a",{"a":email}).fetchone()
# if data==None:
#             print("can register.")
           
        
# else:
#             print('cannot register')
        
        
        

        
        
        
        
        
        
        
        