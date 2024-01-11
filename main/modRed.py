from help import *

def log2(x):
    return (x.bit_length() - 1)

#function k-RED
def kRED(C, n, q):
    m = log2(n)+1
    k = (q-1)//(2**m)
    C0 = C%(2**m)
    C1 = C//(2**m)
    x = k*C0 - C1
    return x


#function k-RED-2x
def kRED2x(C, n, q):
    m = log2(n)+1
    k = (q-1)//(2**m)
    C0 = C%(2**m)
    C1 = (C//(2**m))%(2**m)
    C2 = C//(2**(2*m))
    y = (((k**2)*C0) - (k*C1) + C2)
    return y
    
#modified ntt
def modifiedNTT(a, psi, q):
    f = a.copy()
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
                if m == 128:
                    U = kRED(U)
                    V = kRED2x(V)
                else:
                    V = kRED(V)
                f[j] = (U + V)
                f[j+t] = (U - V)
        m = 2*m
    f = bit_reversal(f)
    return f


#modified intt
def modifiedINTT(nttF, psi, q):
    ntt = nttF.copy()
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
                ntt[j] = (U + V)
                ntt[j+t] = ((U - V)*S)
                if m == 32:
                    ntt[j] = kRED(ntt[j])
                    ntt[j+t] = kRED2x(ntt[j+t])
                else:
                    ntt[j+t] = kRED(ntt[j+t])
            j1 = j1 + 2*t
        t = 2*t
        m = m//2
    for j in range(n):
        U = ntt[j]
        V = ntt[j+t]
        # ntt[j] = kRED((U + V), inverse(n, q))
        # ntt[j+t] = kRED((U - V), inverse(psi, q))
    return ntt
