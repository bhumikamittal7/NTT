#THIS IS INCOMPLETE RN 

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from codes.help import *
#============================ take params ====================================#
k = int(input("Enter any number: "))
n = 2**k

q = take_q(n)
w = take_w(q,n)
f = take_f(n,q)

#============================ print params ====================================#
print ("n = ",n)
print ("q = ",q)
print ("w = ",w)
print ("f(x) = ",f)

#============================ Iterative GS implementation ====================================#
'''
Concept:
Define: phi_8 = w, phi_4 = w^2, phi_2 = w^4, phi_1 = w^8
    1. Bit reveral the input
    2. 
'''
