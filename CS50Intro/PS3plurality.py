#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:40:48 2020

@author: user
"""


# First we init the variables
candidates={}  #this dictionary will store the name of the candidate and votes
voters=int #that is the count of voters that are elidgible to vote
names=str #name of the candidate to be input
c_quantity=int #number of candidates for the election compaign
voters=0
votes=str
c_quantity=0
broken_votes=int
broken_votes=0
alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
print('Welcome to the election compaign!')
print('')

while voters < 1:
    voters=int(input('Please enter the number of elidgible voters: '))
print('')
while c_quantity < 1:
    c_quantity=int(input('Please enter the number of participating candidates: '))
print('')

for i in range(0,c_quantity):
    names=str(input('Please enter the name of candidate '))
    x=names.upper()
    i+=1
    candidates.update({x:0})
print('')
for j in range(0,voters):
    votes=str(input('Enter the name of the candidate you are voting for: '))
    y=votes.upper()
    if y in candidates:
        candidates[y]+=1
    else:
        print('')
        print('Such candidate was not registered for the election!!!!!')
        broken_votes+=1
print('')
print('Election compaign results as follows:')
print('')
print('Registered candidates are: ')
for i in candidates:
    print(i)
print('')
print('Votes distribution:')
for key,value in candidates.items():
    print (key," => ",value)
print('Total votes considered invalid: ', broken_votes)
print('')
print('Election compaign results. The winner is:')
winner_names=[]
winner_scores=[]
winner_scores=list(candidates.values())
# print(winner_scores)
winner_names=list(candidates.keys())
# print(winner_names)
print('')
a=[2, 2, 1]
b=['bill','cathy','joe']    
x=winner_scores.index(max(winner_scores))
for i in range(len(winner_scores)):
    if winner_scores[i]==winner_scores[x]:
        print(winner_names[i])  


        
   
        
        
    