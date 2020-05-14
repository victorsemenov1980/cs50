#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:08:14 2020

@author: user
"""


list1=[1,5,6,7,12,78,99,23,11,34,3,2,9,99,124,567,321,88]
print('')
print('Bubble sort')
print('')
print('Unsorted')
print(list1)
print('')
print('Sorted')
for i in range(len(list1)):
    for j in range(0,len(list1)-i-1):       
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            # print('J=',j)
            print(list1)
    # print('I=',i)
   
print(list1)

print('')
print('Selection sort')
print('')
print('Unsorted')
list1=[1,5,6,7,12,78,99,23,11,34,3,2,9,99,124,567,321,88]
print(list1)
print('')
print('Sorted')
sorted1=[]
for i in range(len(list1)):
    x=min(list1)
    sorted1.append(x)
    print(sorted1)
    list1.remove(x)
   
   
print(sorted1)

print('')
print('Merge sort')
print('')
print('Unsorted')
list1=[1,5,6,7,12,78,99,23,11,34,3,2,9,99,124,567,321,88]
print(list1)
def merge_sort(iterable):
    left=[]
    right=[]
    
    if len(iterable)>1:
        x=len(iterable)//2
        left=iterable[:x]
        right=iterable[x:]
        
        merge_sort(left)
        merge_sort(right)
        i=0
        j=0
        k=0
       
        while i<len(left) and j < len(right):
     
            
            if left[i]<right[j]:
                
                iterable[k]=left[i]
                i+=1
                
                
               
            else:
                iterable[k]=right[j]
                # sorted2.append(left[i])
                
                j+=1
            
            k+=1
            
        while i < len(left):
            iterable[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            iterable[k]=right[j]
            j += 1
            k += 1
               
            
       
    return iterable
    
  
print('')
print('Sorted')
print(merge_sort(list1))

print('')
print('Binary recursive search')
print('')
print('Search array:')
print(merge_sort(list1))
search_list=merge_sort(list1)
print('')
num_search=int(input('Which number you want to search for: '))
def binary(iterable,num_search):
    middle=int
    middle=len(iterable)//2
    left=iterable[:middle]
    right=iterable[middle:]
    if iterable[middle]==num_search:
        print('FOUND')
    else:
        if iterable[middle]>num_search:
            binary(left,num_search)
            
        else:
            iterable[middle]<num_search
            binary(right,num_search)
        

print(binary(search_list,num_search))
        





























