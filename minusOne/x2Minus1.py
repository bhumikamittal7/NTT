import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from codes.help import *
from recursiveCT import *
#============================ take params ====================================#

k = int(input("Enter any number: "))
n = 2**k

q = take_q(n)
w = take_w(q,n)
f = take_f(n,q)
g = take_f(n,q)

#============================ print params ====================================#
print ("n = ",n)
print ("q = ",q)
print ("w = ",w)
print ("f(x) = ",f)
print ("g(x) = ",g)

#======================= multiply f(x) and g(x) ====================================#
def multiply(f,g,q):
    h = [0]*(2*len(f)-1)
    for i in range(len(f)):
        for j in range(len(g)):
            h[i+j] += (f[i]*g[j]) % q
    return h

h = multiply(f,g,q)
print ("Without NTT Product ",h)
#============================ Pointwise multiplication function ====================================#
def pointwiseMultiply(f,g,q):
    n = len(f)
    h = []
    for i in range(n):
        h.append((f[i]*g[i]) % q)
    return h
#============ convert to NTT using Cooley Tukey ====================================#
nttF = convertToNTT(f,q,w, n)
nttG = convertToNTT(g,q,w, n)


nttFG = pointwiseMultiply(nttF,nttG,q)
print ("NTT Product ",nttFG)
