import random
import math
#=========== helper functions =================================================#
#checks if the number is prime or not
def is_prime(p):
    if p==1:
        return False
    for i in range(2,p):
        if p%i==0:
            return False
    return True

#generates a random prime number between 1 and 500
def generate_random_prime():
    while True:
        p = random.randint(1,500)
        if is_prime(p):
            return p

#finds the gcd of two numbers
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

#gives the list of all elements in Z_q_star  
def Z_q_star(q):
    Z_q_star_list = []
    for i in range(1,q):
        if gcd(i,q)==1:
            Z_q_star_list.append(i)
    return Z_q_star_list

#find all w such that order of w is n and w^j != 1 for any 1<=j < n
def primitive_roots(q,n):
    Z_q_star_list = Z_q_star(q)
    w_list = []
    for w in Z_q_star_list:
        if w**n % q == 1 and all(w**j % q != 1 for j in range(1, n)):
            w_list.append(w)
    return w_list

#generates a random polynomial of degree n-1 with coefficients in Z_q
def random_poly(n,q):
    f = []
    for i in range(n):
        f.append(random.randint(0,q-1))
    return f

#============================ Taking Params ====================================#
#take q such that q = 1 mod n and q is a prime number
def take_q(n):
    n = 2*n
    choice = input("Do you want to enter a q? (1/0): ")
    if choice=='1':
        q = int(input("Enter q: "))
    else:
        #generate q such that q = 1 mod n and q is a prime number
        while True:
            q = generate_random_prime()
            if q%n==1:
                break

    assert is_prime(q)
    assert q%n==1
    return q

#take w such that w^n = 1 mod q and w is a primitive root of q
def take_w(q,n):
    choice2 = input("Do you want to enter a w? (1/0): ")
    if choice2=='1':
        w = int(input("Enter w: "))
    else:
        w_list = primitive_roots(q,n)
        w = random.choice(w_list)

    assert (w**n)%q==1

    return w

#take f such that f is a polynomial of degree n-1 with coefficients in Z_q
def take_poly(n,q):
    choice3 = input("Do you want to enter a polynomial? (1/0): ")
    if choice3=='1':
        f = []
        for i in range(n):
            f.append(int(input("Enter coefficient of x^"+str(i)+": ")))
    else:
        f = random_poly(n,q)
    return f

#======================= Bit Reversal ==============================================#
#bit reversal - takes a list f and returns a list f_rev such that f_rev[i] = f[bit_reversal(i)]
def bit_reversal(f):
    #k should be such that 2^k = n
    # print ("f = ",f)
    n = len(f)
    k = int(math.log(n,2))
    # print ("n = ",n)
    f_rev = []
    for i in range(n):
        f_rev.append(0)
    for i in range(n):
        # print("k = ",k)
        f_rev[i] = f[int(bin(i)[2:].zfill(k)[::-1],2)]
        # print ("i", i,"reversed i", int(bin(i)[2:].zfill(k)[::-1],2), "f_rev[i] = ",f_rev[i])
    return f_rev

#============================ Normal NTT ====================================#
#valdermonde matrix method
def convertToNTT(f, q, w, n):
    ntt = []
    for i in range(n):
        ntt.append(0)
        #we need to calculate f(w^i) for i = 0 to n-1 and store it in ntt[i]
        for j in range(n):
            ntt[i] += f[j]*(w**(i*j))
        ntt[i] = ntt[i]%q
    return ntt
