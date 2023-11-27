import random
#=========== helper functions =================================================#
def is_prime(p):
    if p==1:
        return False
    for i in range(2,p):
        if p%i==0:
            return False
    return True

def generate_random_prime():
    while True:
        p = random.randint(1,500)
        if is_prime(p):
            return p

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def Z_q_star(q):
    Z_q_star_list = []
    for i in range(1,q):
        if gcd(i,q)==1:
            Z_q_star_list.append(i)
    return Z_q_star_list

#find all w such that order of w is n  and w^j != 1 for any 1<=j < n
def primitive_roots(q,n):
    Z_q_star_list = Z_q_star(q)
    w_list = []
    for w in Z_q_star_list:
        if w**n % q == 1 and all(w**j % q != 1 for j in range(1, n)):
            w_list.append(w)
    return w_list

def random_poly(n,q):
    f = []
    for i in range(n):
        f.append(random.randint(0,q-1))
    return f

#============================ take params ====================================#

k = int(input("Enter any number: "))
n = 2**k

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

choice2 = input("Do you want to enter a w? (1/0): ")
if choice2=='1':
    w = int(input("Enter w: "))
else:
    w_list = primitive_roots(q,n)
    w = random.choice(w_list)

assert (w**n)%q==1

choice3 = input("Do you want to enter a polynomial? (1/0): ")
if choice3=='1':
    f = []
    for i in range(n):
        f.append(int(input("Enter coefficient of x^"+str(i)+": ")))
else:
    f = random_poly(n,q)

#============================ print params ====================================#
print ("n = ",n)
print ("q = ",q)
print ("w = ",w)
print ("f(x) = ",f)

#============================ Normal NTT ====================================#
def convertToNTT(f, q, w):
    ntt = []
    for i in range(n):
        ntt.append(0)
        #we need to calculate f(w^i) for i = 0 to n-1 and store it in ntt[i]
        for j in range(n):
            ntt[i] += f[j]*(w**(i*j))
        ntt[i] = ntt[i]%q
    return ntt

#============================ Butterfly Implementation (Cooley Tukey) ====================================#
def convertToNTT_butterfly(f, w, q):
    n = len(f)
    if n == 1:
        return f
    else:
        r_1 = []
        r_2 = []
        for i in range(n//2):
            r_1.append((f[i] + f[i+n//2]) % q)
            r_2.append((f[i] - f[i+n//2]) * pow(w, i, q) % q)

        # print ("r_1 = ",r_1)
        # print ("r_2 = ",r_2)
        r_1 = convertToNTT_butterfly(r_1, (w**2)%q, q)
        r_2 = convertToNTT_butterfly(r_2, (w**2)%q, q)
        r = r_1 + r_2
        return r

#======================= Bit Reversal ==============================================#
def bit_reversal(f):
    n = len(f)
    f_rev = []
    for i in range(n):
        f_rev.append(0)
    for i in range(n):
        f_rev[i] = f[int(bin(i)[2:].zfill(k)[::-1],2)]
    return f_rev
#============================ print and compare ====================================#
ntt = convertToNTT(f,q,w)
print ("NTT(f(x)) = ",ntt)

ntt_butterfly = convertToNTT_butterfly(f,w,q)
print ("NTT(f(x)) using butterfly = ",ntt_butterfly)
ntt_butterfly = bit_reversal(ntt_butterfly)
print ("NTT(f(x)) after bit reversal = ",ntt_butterfly)

assert ntt==ntt_butterfly
print ("Lessgoo!")
