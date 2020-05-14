#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:56:44 2020

@author: user
"""

#Problem set 0. Say Hello

# x=str(input('Please anter your name: '))
    
# print('Hello ',x)

"""Problem set 1-1 Mario"""

n=int()
while n<1:
    n=int(input('Enter the height of the Mario pyramid: '))

i=int()
j=int()
p=[]

for i in range(1,n+1,1):
    for j in range(n,i,-1):
        p.append(' ')
    for j in range(0,i,1):
        p.append('#')
    p.append(' ')
    for j in range(0,i,1):
        p.append('#')
    # print('')
    str1 = ''.join(p)
    print(str1)
    p=[]

"""Problem set 1-2 credit card"""

card_number=str()
cn=[]
cn2=[]
x=int()
cn3=[]
cn4=[]
x=[]
cn3_string=str()
card_number=str(input('Please enter your card number '))
cn=[int(i) for i in list(card_number)]

if len(cn) != 13 and len(cn) !=15 and len(cn) !=16:
    print('Invalid card number')
else:
    cn.reverse()
    for i in range(0,len(cn),2):      
        cn2.append(cn[i])
    for i in range(1,len(cn),2):      
        cn3.append(cn[i]*2)
    cn3_string = [str(integer) for integer in cn3]
    a_string = "".join(cn3_string)
    cn4=[int(i) for i in list(a_string)]
    y=sum(cn4)
    x=sum(cn2)
    z=(x+y)%10
    cn.reverse()
    if z==0:
        # print(cn)
        # print(len(cn))
        # print('Valid card')
        if cn[0]==4 and len(cn)==13:
            print('Visa')
        elif cn[0]==4 and len(cn)==16:
            print('Visa')
        elif cn[0]==3 and cn[1]==4 and len(cn)==15:
            print('AmEX')
        elif cn[0]==3 and cn[1]==7 and len(cn)==15:
            print('AmEX')
        elif cn[0]==5 and cn[1]==1 and len(cn)==16:
            print('MasterCard')
        elif cn[0]==5 and cn[1]==2 and len(cn)==16:
            print('MasterCard')
        elif cn[0]==5 and cn[1]==3 and len(cn)==16:
            print('MasterCard')
        elif cn[0]==5 and cn[1]==4 and len(cn)==16:
            print('MasterCard')
        elif cn[0]==5 and cn[1]==5 and len(cn)==16:
            print('MasterCard')
    else:
        print('Invalid card')
   
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
