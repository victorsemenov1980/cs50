#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 00:57:18 2020

@author: user
"""


"""
Coleman-Liau index.
index = 0.0588 * L - 0.296 * S - 15.8

L is the average number of letters per 100 words in the text

S is the average number of sentences per 100 words in the text.
"""
alphabeth=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text=str()
text=input('Please enter text for evaluation: ')
x=text.split()
letters=int()
sentences=int()
for char in text:
    if char in alphabeth:
        letters+=1
    else:
        letters+=0
for char in text:
    if char=='.' or char=='!' or char=='?':
        sentences+=1
    else:
        sentences+=0
L=letters*100/len(x)
S=sentences*100/len(x)  
index=int()
index=0.0588 * L - 0.296 * S - 15.8
print('')
print('Number of words: ',len(x))
print('')
print('Number of letters in text: ',letters)
print('')
print('Number of sentences: ',sentences)
print('')
if index<1:
    print('Before Grade 1')
elif index>16:
    print('Grade 16+')
else:
    print('The reading Grade is: ',round(index))

