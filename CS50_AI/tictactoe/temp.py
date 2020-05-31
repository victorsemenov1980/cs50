#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:55:35 2020

@author: user
"""
import random
X = "X"
O = "O"
EMPTY=None
board= [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def count_values(iterable):
     
    if iterable.count(iterable[0])==len(iterable):
        return True
    else:
        return False

win_list=[]
check=[]
win_list.append([board[0][0],board[0][1],board[0][2]])
win_list.append([board[1][0],board[1][1],board[1][2]])
win_list.append([board[2][0],board[2][1],board[2][2]])
win_list.append([board[0][0],board[1][0],board[2][0]])
win_list.append([board[0][1],board[1][1],board[2][1]])
win_list.append([board[0][2],board[1][2],board[2][2]])
win_list.append([board[0][0],board[1][1],board[2][2]])
win_list.append([board[0][2],board[1][1],board[2][0]])
for i in win_list:
        if count_values(i)==True and i[0]!=None:
            check.append(i)
if len(check)>0:           
    if len(check)!=1:
        print('impossible board')
    if check[0][0]==X:
        print(X)
    elif check[0][0]==O:
        print(O)
    elif len(check)==0:
        print( None)

        