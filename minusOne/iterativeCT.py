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
#bit reverse the input
f = bit_reversal(f)
print ("f(x) after bit reversal = ",f)
