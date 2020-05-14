#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:32:57 2020

@author: user
"""
import csv
import re
import sys
from sys import argv, exit
import itertools

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

dna_temp={} #a temporary location for csv dict reader
dna_base=[] #list of dicts where for every person there is a dict with all values

with open(sys.argv[1], newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        dna_temp.update(line)
        dna_base.append(dna_temp)
        dna_temp={}
        
dict_keys=[] #Here we store the names of DNA sequences

for dic in dna_base:
    for key,value in dic.items():
        dict_keys=list(dic.keys())

# print(dict_keys)       
test=''
result=[] #here is the analysis of txt file

with open(sys.argv[2],'r') as file:
    c=file.read()
    test+=c
 
for i in range(1,len(dict_keys)):
    test_sub=dict_keys[i]
    res = [i.start() for i in re.finditer(test_sub, test)] 
    

    streak_count = []
    counter = 1
    for i in range(len(res)):
        if i != (len(res) - 1):
            diff = res[i+1] - res[i]
            if diff == len(test_sub):
                counter += 1
            else:
                streak_count.append(counter)
                counter = 1
        else:
            streak_count.append(counter)
    result.append(max(streak_count))


dict_result={}
result = list(map(str, result))
result.insert(0,'null')
dict_result=dict(zip(dict_keys,result))


for i in range(len(dna_base)):
    dict_result['name']=dna_base[i]['name']
    if dict_result==dna_base[i]:
        print(dna_base[i]['name'],end='.\n')
        x=1
        break
    else:
        x=0

if x==0:
    print('No match.')

      











    
    

