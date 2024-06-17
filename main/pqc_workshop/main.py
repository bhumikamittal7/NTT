import sys, os, time
from help import *
from direct import *
from quasilinear import *

#====================== take input from user ======================#
# n = int(input("Enter n \in \mathbb{N}: "))

k = int(input("Enter any k such that n = 2^k: "))
n = 2**k

q = take_q(n)
w = take_w(q,n)
psi = take_psi(q,n, w)

f = take_poly(n,q)
g = take_poly(n,q)
print ("======================= Inputs =======================")
print ("n = ",n)
print ("q = ",q)
print ("w = ",w)
print ("psi = ",psi)
print ("f = ",f)
print ("g = ",g)
#====================== run all the algos ======================#
print("\n")
print ("======================= Direct Algorithms =======================")
print ("======================= Cyclic =======================")
print("NTT(f) = ",cycNTT(f, q, w, n))
print("NTT(g) = ",cycNTT(g, q, w, n))

start = time.time()
fg = cycCon(f, g, q, w, n)
end = time.time()

print("f*g = ", fg)
# print ("Time taken for cycCon = ", end-start)

print("\n")
print ("======================= Negacyclic =======================")
print("NTT(f) = ",negacycNTT(f, q, psi, n))
print("NTT(g) = ",negacycNTT(g, q, psi, n))

start = time.time()
fg = negacycCon(f, g, psi, q, n)
end = time.time()

print("f*g = ", fg)
# print ("Time taken for negacycCon = ", end-start)

print("\n")
print ("======================= Quasilinear Algorithms =======================")
print ("======================= CT =======================")
recCTF = recCT(f, w, q)
print("recCT = ",recCTF)
iterCTF = iterCT(f, psi, q)
print("iterCT = ",iterCTF)

print("\n")
print ("======================= GS =======================")
recGSF = recGS(f, w, q)
print("recGS = ",recGSF)
# iterGSF = iterGS(iterCTF, psi, q)
# print("iterGS = ",iterGSF)

# print("\n")
print ("======================= Multiplication =======================")
start = time.time()
fg = mult(f, g, q, psi, n)
end = time.time()

print("f*g = ", fg)
# print ("Time taken for mult = ", end-start)
print("\n")
print("======================= DONE =======================")
