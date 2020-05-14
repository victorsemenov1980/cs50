#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:41:25 2020

@author: user
"""
import itertools
names=[]
print('Welcome to Tideman election!')
print('')
number_of_candidates=0
while number_of_candidates<2:
    number_of_candidates=int(input('Enter the number of elidgible candidates: '))
candidate_name=str
num2=number_of_candidates
while number_of_candidates!=0:
    candidate_name=str(input('Enter candidate name: '))
    number_of_candidates-=1
    x=candidate_name.upper()
    names.append(x)
number_of_candidates=num2
print('')
print('List of registered candidates:')
for i in names:
    print(i)    
x=list(itertools.combinations(names, 2))
scores={}
for i in x:
    scores.update({i:[0,0]})
# print(scores)
voters=0
while voters<2:
    voters=int(input('Enter quantity of elidgible voters '))
ballot=[]
ballots=[]
num=number_of_candidates
z=1
v=voters
for voters in range(0,voters):
    print('')
    print('Voter #',z)
    for number_of_candidates in range(0,number_of_candidates):
        candidate=str(input('Enter candidates in descending order of you personal rating: '))
        f=candidate.upper()
        ballot.append(f)
        number_of_candidates-=1
    ballots.append(ballot) 
    ballot=[]
    z+=1
    voters-=1
    number_of_candidates=num
voters=v  
for i in range(0,voters):
    for k,v in scores.items():
        if ballots[i].index(k[0])<ballots[i].index(k[1]):
            v[0]+=1
        else:
            v[1]+=1
           
    i+=1
print('')
print('Election summary:')
for k,v in scores.items():
    print('')
    print(k,' FINAL SCORE ',v)
print('')
print('The winner is:')
x=list(scores.values())
keys=list(scores.keys())
keys_list=[list(i) for i in keys]

#sorting and sorting

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


