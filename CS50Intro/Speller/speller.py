#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:57:37 2020

@author: user
"""

import re

dictionary='large'
words = set()
def check(word):
    """Return true if word is in dictionary else false""" 
    if word.lower() in words:
        return True 
    else:
        return False

def size():
    """Returns number of words in dictionary if loaded else 0 if not yet loaded""" 
    return len(words)

file = open(dictionary, "r")
words = set()
for line in file:
    words.add(line.rstrip("\n")) 
print("",len(words),' words loaded')
word=''
counter=0
misspelled=[]

# print(words)
with open('carroll.txt','r') as file_check:
    for line in file_check.readlines():
        for word in line.split():
            if word==re.sub(r'[^\w\s]','',word) and check(word)==False:
                counter+=1
                misspelled.append(word)


print('Misspelled=',counter)
print()
print('The misspelled words are:')
for i in misspelled:
    print(i)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            