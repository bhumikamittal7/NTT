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

#============================ Butterfly Implementation (Cooley Tukey) ====================================#
def convertToNTT_butterfly(f, w, q):
    n = len(f)
    if n == 1:
        return f
    else:
        r_1 = []
        r_2 = []
        for i in range(n//2):
            r_1.append((f[i] + f[i+n//2]) % q)
            r_2.append((f[i] - f[i+n//2]) * pow(w, i, q) % q)

        # print ("r_1 = ",r_1)
        # print ("r_2 = ",r_2)
        r_1 = convertToNTT_butterfly(r_1, (w**2)%q, q)
        r_2 = convertToNTT_butterfly(r_2, (w**2)%q, q)
        r = r_1 + r_2
        return r


#============================ print and compare ====================================#
ntt = convertToNTT(f,q,w, n)
print ("NTT(f(x)) = ",ntt)

ntt_butterfly = convertToNTT_butterfly(f,w,q)
print ("NTT(f(x)) using butterfly = ",ntt_butterfly)
ntt_butterfly = bit_reversal(ntt_butterfly)
print ("NTT(f(x)) after bit reversal = ",ntt_butterfly)

assert ntt==ntt_butterfly
print ("Lessgoo!")
