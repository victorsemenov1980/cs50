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

# if len(argv) != 3:
#     print("Usage: python dna.py data.csv sequence.txt")
#     exit(1)

dna_temp={} #a temporary location for csv dict reader
dna_base=[] #list of dicts where for every person there is a dict with all values

with open('small.csv', newline='') as csvfile:
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

with open('1.txt','r') as file:
    c=file.read()
    test+=c

dict_result={}
dict_keys.pop(0)
dict_result = dict.fromkeys(dict_keys, 0)

for key in dict_result:
    l = len(key)
    tempMax = 0
    temp = 0
    for i in range(len(test)):
        # after having counted a sequence it skips at the end of it to avoid counting again
        while temp > 0:
            temp -= 1
            continue

        # if the segment of dna corresponds to the key and there is a repetition of it we start counting
        if test[i: i + l] == key:
            while test[i - l: i] == test[i: i + l]:
                temp += 1
                i += l

            # it compares the value to the previous longest sequence and if it is longer it overrides it
            if temp > tempMax:
                tempMax = temp

    # store the longest sequences in the dictionary using the correspondent key
    dict_result[key] += tempMax
print(dict_result)
for i in range(len(dna_base)):
    dict_result['name']=dna_base[i]['name']
    # print(i)
    # print(dict_result)
    # print(dna_base[i])
    if dict_result==dna_base[i]:
        print(dna_base[i]['name'],end='.\n')
        x=1
        break
    else:
        x=0

if x==0:
    print('No match.')

      











    
    

