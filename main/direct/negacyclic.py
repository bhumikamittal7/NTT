import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from main.help import *

#============================ Direct NTT ====================================#
#valdermonde matrix method
def negacycNTT(f, q, psi, n):
    ntt = []
    for j in range(n):
        ntt.append(0)
        for i in range(n):
            ntt[j] += f[i]*(psi**((2*i*j)+1))
        ntt[j] = ntt[j]%q
    return ntt

#============================ Inverse NTT ====================================#
def negacycINTT(ntt, q, psi, n):
    nInverse = inverse(n,q)
    print ("nInverse = ",nInverse)
    psiInverse = inverse(psi,q)
    print ("wInverse = ",psiInverse)

    intt = []
    for i in range(n):
        intt.append(0)
        for j in range(n):
            intt[i] += ntt[j]*(psiInverse**((2*i*j)+j))
        intt[i] = (intt[i]*nInverse)%q
    return intt

#============================ Multiplication ====================================#
def negacycCon(f,g, psi, q, n):
    fntt = negacycNTT(f,q,psi,n)
    gntt = negacycNTT(g,q,psi,n)
    hntt = []
    for i in range(n):
        hntt.append((fntt[i]*gntt[i])%q)
    h = negacycINTT(hntt,q,psi,n)
    return h
