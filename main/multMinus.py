from help import *
from main.RecursiveCooleyTukey import *
from inttGS import *

#============================ take params ====================================#
k = int(input("Enter any k such that n = 2^k: "))
n = 2**k

q = take_q(n)
w = take_w(q,n)

f = take_poly(n,q)
g = take_poly(n,q)

#============================ print params ====================================#
print ("n = ",n)
print ("q = ",q)
print ("w = ",w)

print ("f(x) = ",f)
print ("g(x) = ",g)

#================ normal multiplication ===================#
def normal_mult(f,g,q):
    fg = [0]*(2*len(f)-1)
    for i in range(len(f)):
        for j in range(len(g)):
            fg[i+j] += f[i]*g[j]
    for i in range(len(fg)):
        fg[i] = fg[i]%q
    return fg

#================ pointwise multiplication ===================#
def pointwise_mult(f,g,q):
    fg = [0]*(2*len(f)-1)
    for i in range(len(f)):
        fg[i] = f[i]*g[i]
    for i in range(len(fg)):
        fg[i] = fg[i]%q
    return fg

#============================ NTT TEST ====================================#
NTTf = nttCT(f,w,q)
NTTg = nttCT(g,w,q)

print ("NTT(f(x)) = ",NTTf)
print ("NTT(g(x)) = ",NTTg)

NTTfg = pointwise_mult(NTTf,NTTg,q)
print ("NTT(f(x))*NTT(g(x)) = ",NTTfg)

fg = inttGS(NTTfg,q,w)
print ("f(x)*g(x) = ",fg)

fg1 = normal_mult(f,g,q)
print ("f(x)*g(x) = ",fg1)

assert fg==fg1
print ("Lessgoo!")
