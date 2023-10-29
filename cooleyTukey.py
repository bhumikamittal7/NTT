#cooley-tukey (basically we are using the divide and conquer approach)
#here q is a prime number and n is a power of 2 such that q = 1 mod n
import random

#take n from the user
k = int(input("Enter any number: "))
n = 2**k

choice = input("Do you want to enter a q? (y/n): ")
if choice=='y':
    q = int(input("Enter q: "))
    assert q%n==1
else:
    #generate q such that q = 1 mod n
    q = 1 + n*random.randint(1,10)

print("n = ",n)
print("q = ",q)

#input is a polynomial f(x) of degree n-1 in polynomial domain with coefficients in Zq and \omega is a primitive nth root of unity in Zq

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def Z_q_star(q):
    Z_q_star = []
    for i in range(1,q):
        if gcd(i,q)==1:
            Z_q_star.append(i)
    return Z_q_star
Z_q_star = Z_q_star(q)
print("Z_q_star = ",Z_q_star)

w_n_1 = []
for w in Z_q_star:
    if (w**n)%q==1:
        w_n_1.append(w)
print("w = ",w_n_1)

w = random.choice(w_n_1[1:])
print("Chosen w = ",w)
assert (w**n)%q==1    

def random_poly(n,q):
    f = []
    for i in range(n):
        f.append(random.randint(0,q-1))
    return f

choice = input("Do you want to enter a polynomial? (y/n): ")
if choice=='y':
    f = []
    for i in range(n):
        f.append(int(input("Enter coefficient of x^"+str(i)+": ")))
else:
    f = random_poly(n,q)
#======================================================================================================================================================================
#output: f(w^l) for l=0,1,...,n-1

