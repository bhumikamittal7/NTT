# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from help import *

#============================ Butterfly Implementation (Recursive GS) ====================================#
# Link (theorem 2) - https://people.scs.carleton.ca/~maheshwa/courses/5703COMP/16Fall/FFT_Report.pdf

def recursiveGS(f, w, q):
    n = len(f)
    if n == 1:
        return f
    else:        
        r_1 = []
        r_2 = []
        for i in range(n):
            if i%2 == 0:
                r_1.append(f[i])
            else:
                r_2.append(f[i])
        # print ("r_1 = ",r_1)
        # print ("r_2 = ",r_2)
        r_1 = recursiveGS(r_1, (w**2)%q, q)
        r_2 = recursiveGS(r_2, (w**2)%q, q)
        r = [0]*n
        for i in range(n//2):
           r[i] = (r_1[i] + w**i*r_2[i])%q
           r[i+n//2] = (r_1[i] - w**i*r_2[i])%q
        return r

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

# ntt_butterfly = recursiveGS(f,w,q)
# print ("NTT(f(x)) using butterfly = ",ntt_butterfly)

# assert ntt==ntt_butterfly
# print ("Lessgoo!")


#this doesn't need bit reversal?