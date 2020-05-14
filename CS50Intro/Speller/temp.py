#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:51:09 2020

@author: user
"""
import csv
import re

dna_temp={} #a temporary location for csv dict reader
dna_base=[] #list of dicts where for every person there is a dict with all values

with open('large.csv', newline='') as csvfile:
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
with open('5.txt','r') as file:
    c=file.read()
    test+=c
    
result=[] #here is the analysis of txt file

for i in range(1,len(dict_keys)):
    test_sub=dict_keys[i]
    res = [i.start() for i in re.finditer(test_sub, test)] 
    result.append(len(res))