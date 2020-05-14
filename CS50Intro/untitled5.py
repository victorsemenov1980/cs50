#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:05:49 2020

@author: user
"""


ballots=[['ALICE', 'CHARLIE', 'BOB'], ['ALICE', 'CHARLIE', 'BOB'], ['BOB', 'CHARLIE', 'ALICE'], ['BOB', 'CHARLIE', 'ALICE'], ['CHARLIE', 'ALICE', 'BOB']]
scores={('ALICE', 'BOB'): [0, 0], ('ALICE', 'CHARLIE'): [0, 0], ('BOB', 'CHARLIE'): [0, 0]}
# print(ballots[0][1])
# print(ballots[0].index('ALICE'))\
voters=5
# for k,v in scores.items():
#     print(v[0])

for i in range(0,voters):
    for k,v in scores.items():
        if ballots[i].index(k[0])<ballots[i].index(k[1]):
            v[0]+=1
        else:
            v[1]+=1
           
    i+=1

print(scores)
print('')
number_of_candidates=3
names=['ALICE','BOB','CHARLIE']








x=list(scores.values())
keys=list(scores.keys())
keys_list=[list(i) for i in keys]

for i in range(0,number_of_candidates):
    if x[i][0]<x[i][1]:
        x[i][0],x[i][1]=x[i][1],x[i][0]
        keys_list[i][0],keys_list[i][1]= keys_list[i][1],keys_list[i][0]
    
for i in range(0,number_of_candidates-1):
    if x[i][0]<x[i+1][0]:
        x[i],x[i+1]=x[i+1],x[i]
        keys_list[i],keys_list[i+1]=keys_list[i+1],keys_list[i]

for i in range(0,number_of_candidates-1):
    if keys_list[i][0]==keys_list[i+1][1]:
        x[i],x[i+1]=x[i+1],x[i]
        keys_list[i],keys_list[i+1]=keys_list[i+1],keys_list[i]       


print(keys_list[0][0])




















