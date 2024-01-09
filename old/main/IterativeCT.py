# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from help import *

#============================ Butterfly Implementation (Iterative Cooley Tukey) ====================================#
def iterativeCT(f, w, q):
    pass


# #============================ take params ====================================#

# k = int(input("Enter any k such that n = 2^k: "))
# n = 2**k

# q = take_q(n)
# w = take_w(q,n)
# f = take_poly(n,q)

# #============================ print params ====================================#
# print ("n = ",n)
# print ("q = ",q)
# print ("w = ",w)
# print ("f(x) = ",f)

# #============================ print and compare ====================================#
# ntt = convertToNTT(f,q,w, n)
# print ("NTT(f(x)) = ",ntt)

# ntt_butterfly = iterativeCT(f,w,q)
# print ("NTT(f(x)) using butterfly = ",ntt_butterfly)
# ntt_butterfly = bit_reversal(ntt_butterfly)
# print ("NTT(f(x)) after bit reversal = ",ntt_butterfly)

# assert ntt==ntt_butterfly
# print ("Lessgoo!")
