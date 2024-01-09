import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from main.help import *

#============================ Direct NTT ====================================#
#valdermonde matrix method
def cycNTT(f, q, w, n):
    ntt = []
    for i in range(n):
        ntt.append(0)
        #we need to calculate f(w^i) for i = 0 to n-1 and store it in ntt[i]
        for j in range(n):
            ntt[i] += f[j]*(w**(i*j))
        ntt[i] = ntt[i]%q
    return ntt

#============================ Inverse NTT ====================================#
def cycINTT(ntt, q, w, n):
    nInverse = inverse(n,q)
    print ("nInverse = ",nInverse)
    wInverse = inverse(w,q)
    print ("wInverse = ",wInverse)
    intt = [0]*n
    for i in range(n):
        intt[i] = nInverse*ntt[i] % q
    # print ("intt = ",intt)
    intt = cycNTT(intt,q,wInverse,n)
    return intt

#============================ Multiplication ====================================#
def cycCon(f, g, q, w, n):
    fntt = cycNTT(f,q,w,n)
    gntt = cycNTT(g,q,w,n)
    hntt = [0]*n
    for i in range(n):
        hntt[i] = fntt[i]*gntt[i] % q
    h = cycINTT(hntt,q,w,n)
    return h