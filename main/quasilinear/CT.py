import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from main.help import *

#============================ Recursive CT ====================================#
# Link (theorem 2) - https://people.scs.carleton.ca/~maheshwa/courses/5703COMP/16Fall/FFT_Report.pdf

def recCT(f, w, q):
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
        r_1 = recCT(r_1, (w**2)%q, q)
        r_2 = recCT(r_2, (w**2)%q, q)
        r = [0]*n
        for i in range(n//2):
           r[i] = (r_1[i] + w**i*r_2[i])%q
           r[i+n//2] = (r_1[i] - w**i*r_2[i])%q
        
        r = bit_reversal(r)
        return r
    
#============================ Iterative CT function ====================================#
def iterCT(f, psi, q):
    n = len(f)
    assert (q%(2*n))==1

    psi_table = generate_psi_table(q, n, psi)
    psi_table_rev = bit_reversal(psi_table)
    # print ("psi_table = ",psi_table)
    # print ("psi_table_rev = ",psi_table_rev)
        
    t = n
    m = 1
    while m < n:
        t = t//2
        for i in range (0, m):
            j1 = 2*i*t
            j2 = j1 + t - 1
            S = psi_table_rev[m+i]
            for j in range(j1, j2+1):
                U = f[j]
                V = (f[j+t]*S)
                f[j] = (U + V)%q
                f[j+t] = (U - V)%q
        m = 2*m
    f = bit_reversal(f)
    return f
