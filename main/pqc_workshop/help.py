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

#find all w such that order of w is n and w^j != 1 for any 1<=j < n
def primitive_roots(q,n):
    Z_q_list = []
    for i in range(1,q):
        Z_q_list.append(i)
    w_list = []
    for w in Z_q_list:
        if w**n % q == 1 and all(w**j % q != 1 for j in range(1, n)):
            w_list.append(w)
    print ("w_list = ",w_list)
    return w_list

#find all \psi such that \psi^2 = w mod q and \psi^n = -1 mod q
def primitive_root_2n(q,n,w):
    Z_q_list = []
    for i in range(1,q):
        Z_q_list.append(i)
    psi_list = []
    for psi in Z_q_list:
        if psi**2 % q == w and psi**n % q == q-1:
            psi_list.append(psi)
    print ("psi_list = ",psi_list)
    return psi_list

#generates a random polynomial of degree n-1 with coefficients in Z_q
def random_poly(n,q):
    f = []
    for i in range(n):
        f.append(random.randint(0,q-1))
    return f

#find the inverse of an element in Z_q
def inverse(a,q):
    for i in range(1,q):
        if (a*i)%q==1:
            return i

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
        print("w = ",w)

    assert (w**n)%q==1

    return w

# take psi such that psi^2 = w mod q and psi^n = -1 mod q
def take_psi(q,n,w):
    choice2 = input("Do you want to enter a psi? (1/0): ")
    if choice2=='1':
        psi = int(input("Enter psi: "))
    else:
        psi_list = primitive_root_2n(q,n,w)
        psi = random.choice(psi_list)
        print("psi = ",psi)

    assert (psi**2)%q==w
    assert (psi**n)%q==q-1

    return psi

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

#============================ psi table ====================================#
#we generate a table of psi values for a given psi, q and n containing psi^i for i = 0 to n-1
def generate_psi_table(q, n, psi):
    psi_table = []
    psi_table.append(1)
    for i in range(1,n):
        psi_table.append((psi_table[i-1]*psi)%q)
    return psi_table
