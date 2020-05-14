#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 01:45:38 2020

@author: user
"""
temp=[]
encrypted=str()
alphabeth_capitals=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabeth_small=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
substitution_dict={}
key=str()
plain_text=str()
while len(key)!=26:
    key=input('Please enter the 26 letters encryption key: ')
plain_text=input('Please enter the message to be enrypted: ')
key_lower=key.lower()
key_upper=key.upper()
for i,j in enumerate(key_lower):
    substitution_dict.update({alphabeth_small[i]:key_lower[i]})

for i,j in enumerate(key_upper):
    substitution_dict.update({alphabeth_capitals[i]:key_upper[i]})

for char in plain_text:
  
    if char in  substitution_dict:
        temp.append(substitution_dict[char])
    else:
        temp.append(char)
               
encrypted=''.join(temp)
print('')
print('The encrypted message is ready: ',encrypted)
       
