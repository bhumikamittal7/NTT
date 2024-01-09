import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from main.help import *

#============================ Recursive GS ====================================#
def recGS(f, w, q):
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
        r_1 = recGS(r_1, (w**2)%q, q)
        r_2 = recGS(r_2, (w**2)%q, q)
        r = r_1 + r_2
        return r
    
#============================ Iterative GS ====================================#
def iterGS(ntt, psi, q):
    n = len(ntt)
    ntt = bit_reversal(ntt)
    assert (q%(2*n))==1
    psiInverse = inverse(psi, q)
    psiInverse_table = generate_psi_table(q, n, psiInverse)
    psiInverse_table_rev = bit_reversal(psiInverse_table)

    t = 1
    m = n
    while m > 1:
        j1 = 0
        h = m//2
        for i in range (0, h):
            j2 = j1 + t - 1
            S = psiInverse_table_rev[h+i]
            for j in range(j1, j2+1):
                U = ntt[j]
                V = ntt[j+t]
                ntt[j] = (U + V)%q
                ntt[j+t] = ((U - V)*S)%q
            j1 = j1 + 2*t
        t = 2*t
        m = m//2
    for j in range(n):
        ntt[j] = (ntt[j]*inverse(n, q))%q
    return ntt
