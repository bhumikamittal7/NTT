def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

#let's first define Z_q* as the set of all integers in the range [0,q-1] that are relatively prime to q
def Z_q_star(q):
    Z_q_star = []
    for i in range(1,q):
        if gcd(i,q)==1:
            Z_q_star.append(i)
    return Z_q_star

#take q as an input from the user
q = int(input("Enter a number q: "))
Z_q_star = Z_q_star(q)
print("Z_q_star = ",Z_q_star)

#take some n as an input from the user
n = int(input("Enter a number n: "))

def order(a):
    for i in range(1,q):
        if (a**i)%q==1:
            return i

#find all w in Z_q_star such that w^n=1
w_n_1 = []
for w in Z_q_star:
    if (w**n)%q==1:
        w_n_1.append(w)
print("w = ",w_n_1)

#chose a random w from the list w
import random
#remove first element from w_n_1 by list slicing
w = random.choice(w_n_1[1:])
print("Chosen w = ",w)
#verify that w^n=1 (we need to mod this by q and ensure that the result is 1)
assert (w**n)%q==1      #if this is not true, then the program should stop here -- but technically, this should never happen

#======================================================================================================================================================================

#now we need to generate a random polynomial f(x) of degree n-1 with coefficients in Z_q
def random_poly(n,q):
    f = []
    for i in range(n):
        f.append(random.randint(0,q-1))
    return f

#give user a choice to enter a polynomial or generate a random polynomial
choice = input("Do you want to enter a polynomial? (y/n): ")
if choice=='y':
    f = []
    for i in range(n):
        f.append(int(input("Enter coefficient of x^"+str(i)+": ")))
else:
    f = random_poly(n,q)

print("f(x) = ",f)

#======================================================================================================================================================================
#convert f(x) to NTT domain

def NTT(f,q,w):
    ntt_w = []
    for i in range(n):
        ntt_w.append(0)
        for j in range(n):
            ntt_w[i] += f[j]*(w**(i*j))
        ntt_w[i] = ntt_w[i]%q
    return ntt_w

ntt_w = NTT(f,q,w)
print("NTT(f(x)) = ",ntt_w)

#======================================================================================================================================================================
#convert NTT(f(x)) back to polynomial domain

def w_inverse(w):
    for i in range(1,q):
        if (w*i)%q==1:
            return i

def n_inverse(n):
    for i in range(1,q):
        if (n*i)%q==1:
            return i

def poly_ntt_inverse(ntt_w,q,w):
    w_inv = w_inverse(w)
    n_inv = n_inverse(n)
    f = []
    for i in range(n):
       f.append((ntt_w[i]*n_inv)%q)
    return f

g = poly_ntt_inverse(ntt_w,q,w)
print("g(x) = ",g)

ntt_inv = NTT(g,q,w_inverse(w))
print("f(x) = ",ntt_inv)

#ntt_inv and f should be the same
assert ntt_inv==f

print("Yayyy!")