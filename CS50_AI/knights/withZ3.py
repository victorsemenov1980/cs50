#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:43:04 2020

@author: user
"""


from z3 import *

# True = Knight, False = Knave
A, B,C = Bools("A B C")
s = Solver()

# Puzzle 1
# "A says: "Both of us are Knaves"
#B says nothing
# s.add((A == True) == And(A == False, B == False))

# if s.check() != sat:
#     print("No solution")
# else:
#     print(s.model())
    
# Puzzle 0
# A says "I am both a knight and a knave."
# s.add((A == True) == And(A == False, A == True))

# if s.check() != sat:
#     print("No solution")
# else:
#     print(s.model())  


# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# s.add((A == True) == Or(And(A == False, B == False),And(A==True,B==True)))
# s.add((B == True) == Or(And(A == False, B == True),And(A==True,B==False)))

# if s.check() != sat:
#     print("No solution")
# else:
#     print(s.model())

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
s.add((B == True) == ((A == True) == (A == False)))
s.add((B == True) == (C==False))
s.add((C == True) == (A==True))

if s.check() != sat:
    print("No solution")
else:
    while s.check() == sat:
            model = s.model()
            print(model)
            # Exclude current solution
            s.add(Or([d() != model[d] for d in model]))