#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:16:59 2020

@author: user
"""


from PIL import Image, ImageOps,ImageFilter
import os

def make_linear_ramp(white):
    # putpalette expects [r,g,b,r,g,b,...]
    ramp = []
    r, g, b = white
    for i in range(255):
        ramp.extend((r*i/255, g*i/255, b*i/255))
    return ramp

files = os.listdir(os.curdir)
print(files)
name=input('Enter file name to alter: ')
image = Image.open(name)
image.show()
print()
methods=['Rotate','Blur','Sharpen','Greyscale','Detail','Edge','Emboss','Smooth','Sepia']
for i in methods:
    print(i)
print()
name_out=input('Enter new file name: ')
print()
method=input('Enter method you want to apply: ')
print()

if 'rotate' in method.lower():
    n=int(input('Enter the turn: '))
    rotated = image.rotate(n)
    rotated.save(name_out)
    rotated.show()

if 'blur' in method.lower():
    blurred = image.filter(ImageFilter.BLUR)
    blurred.save(name_out)
    blurred.show()

if 'sharpen' in method.lower():
    sharpened = image.filter(ImageFilter.SHARPEN)
    sharpened.save(name_out)
    sharpened.show()

if 'greyscale' in method.lower():
    blackwhite = image.convert('L')
    blackwhite.save(name_out)
    blackwhite.show()

if 'detail' in method.lower():
    detailed = image.filter(ImageFilter.DETAIL)
    detailed.save(name_out)
    detailed.show()

if 'endge' in method.lower():
    edged = image.filter(ImageFilter.EDGE_ENHANCE)
    edged.save(name_out)
    edged.show()

if 'emboss' in method.lower():
    embossed = image.filter(ImageFilter.EMBOSS)
    embossed.save(name_out)
    embossed.show()
    
if 'smooth' in method.lower():
    smoothed = image.filter(ImageFilter.SMOOTH)
    smoothed.save(name_out)
    smoothed.show()

if 'sepia' in method.lower():
    sepia = make_linear_ramp((255, 240, 192))
    old=image.putpalette(sepia)
    old.save(name_out)
    old.show()

