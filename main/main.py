#we will use this file to take bunch of inputs as required and choices from users to run the entire thing and maybe nicely format it and export it to an output file
#this will run all the algos and compare them run time probably?

import sys, os, time
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from help import *
from direct import *
from quasilinear import *

#====================== take input from user ======================#

k = int(input("Enter any k such that n = 2^k: "))
n = 2**k

q = take_q(n)
w = take_w(q,n)
psi = take_psi(q,n, w)

f = take_poly(n,q)
g = take_poly(n,q)

#====================== run all the algos ======================#

print ("======================= Direct Algorithms =======================")
print ("======================= Cyclic =======================")
print("NTT(f) = ",cycNTT(f, q, w, n))
print("NTT(g) = ",cycNTT(g, q, w, n))

start = time.time()
fg = cycCon(f, g, q, w, n)
end = time.time()

print("f*g = ", fg)
print ("Time taken for cycCon = ", end-start)

print ("======================= Negacyclic =======================")
print("NTT(f) = ",negacycNTT(f, q, psi, n))
print("NTT(g) = ",negacycNTT(g, q, psi, n))

start = time.time()
fg = negacycCon(f, g, psi, q, n)
end = time.time()

print("f*g = ", fg)
print ("Time taken for negacycCon = ", end-start)

# print ("======================= Quasilinear Algorithms =======================")
# print ("======================= CT =======================")





