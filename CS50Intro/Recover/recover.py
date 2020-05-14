#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 16:39:49 2020

@author: user
"""


# def bytes_from_file(filename, chunksize=512):
#     with open(filename, "rb") as f:
#         while True:
#             chunk = f.read(chunksize)
#             if chunk:
#                 for b in chunk:
#                     yield b
#             else:
#                 break


# for b in bytes_from_file('card.raw'):
#     if b[1]==0xff and b[2]==0xd8 and b[3]==0xff
#         with open('01.jpeg', 'wb') as f:
#             f.write(chunk)
#     # byte_arr = [120, 3, 255, 0, 100]
#         binary_format = bytearray(byte_arr)
#         f.write(binary_format)
#         f.close()


    
    

# fin = open('card.raw', 'rb')
# # fout = open('file2.jpeg', 'w+b')
# while True:
#   b=fin.read(512)
#   i=0
#   if b=='0xff\0xd8\0xff':
#       fout=open('/JPEGFOUND/file'+i,'w+b')
#       n = fout.write(b)
#       i+=1    
#   else:
#     break

# with open("card.raw", "rb") as f:
#     while True:
#         chunk=f.read(512)
#         b=chunk[:3]
#         print(b)
#         # while b!='':
        #     print(b)
    
        
        # if b=='xff\xd8\xff':
            
        #     fout=open('/JPEGFOUND/file.jpeg','w+b')
        #     n = fout.write(chunk)
        # else:
        #     break


# with open('card.raw', 'rb') as file:
#     for byte in iter(lambda: file.read(1), b''):
 
# f = open("card.raw", "rb")
# try:
#     byte = f.read(512)
#     b=byte[:3]
#     print(b)
#     while b != "":
#         if b=='xff\xd8\xff':
#             f2=open('out.jpeg','wb')
#             f2.write(byte)
#         byte = f.read(512)
# finally:
#     f.close()

# f = open("card.raw", "rb")
# b=f.read()
# for i in b:
#     if i=='xff\xd8\xff':
#         print(i)
# with open('card.raw', 'rb') as f:
#     s = f.read()
# b=s.find('xff\xd8\xff')
# print(b)
"""
This is the working prototype
"""
f=open("jpg.jpg", 'rb')
# # chunk=f.read(512)
# # # b=chunk[:3]
# # # print(b)
# # if b'\xff\xd8\xff' in chunk:
# #     print('hooray')
# while True:
#         chunk=f.read()
#         if b'\xff\xd8\xff' in chunk:
#             print('hooray')
#             f2=open('jpegnew.jpg','w+b')
#             n=f2.write(chunk)
#         else:
#             break

"""
end
"""
# chunk=f.read()
# # b1=chunk[1]
# # b2=chunk[2]
# # b3=chunk[3]
# print(b1,'----',b2,'------',b3)
# if b1==216 and b2==255 and b3==224:
#     print('hooray')
    
"""
f=open("card.raw", 'rb')
chunk=f.read(512)
while chunk!=b'':
        chunk=f.read(512)
        b1=chunk[:1]
        b2=chunk[:2]
        b3=chunk[:3]
        if b1==b'\xff' and b2==b'\xff\xd8' and b3==b'\xff\xd8\xff':
            f2=open('rec02.jpg','w+b')
            n=f2.write(chunk)
        


"""
"""
f=open("card.raw", 'rb')
chunk=f.read(512)
while chunk!=b'':
        chunk=f.read(512)
        b1=chunk[1]
        b2=chunk[2]
        b3=chunk[3]
        if b1==216 and b2==255 and b3==224:
            f2=open('rec01.jpg','w+b')
            n=f2.write(chunk)
        # if chunk==b'':
        #     break

"""

f=open("card.raw", 'rb')
chunk=f.read(512)
i=0

while chunk!=b'':
        chunk=f.read(512)
        b1=chunk[:1]
        b2=chunk[:2]
        b3=chunk[:3]
        if b3==b'\xff\xd8\xff':
            
            i+=1
            f2=open("rec0%s.jpg" %i,'w+b')
            n=f2.write(chunk)
            while chunk!=b'':
                chunk=f.read(512)
                f2=open("rec0%s.jpg" %i,'a+b')
                n=f2.write(chunk)
        # chunk=f.read(512)
       
            
            
            
        
        


            











        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            


















