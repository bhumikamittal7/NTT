from helper import *
#===============================================================================
q = 2**23 - 2**13 + 1
n = 5
k = 4
l = 4
eta = 2
d = 14
tau = 39
beta = 78
gamma_1 = 2**17
phi = 1753
#===============================================================================
a = generateMatrix(k, l, q, n)
s1 = S_eta(eta, l, n)
s2 = S_eta(eta, k, n)
y = S_eta(gamma_1-1, l, n)
#===============================================================================
def printParams1():
    print("Number of cols in A = k =", len(a))
    print("===================================================")

    print("A = \n", a)
    print("===================================================")

    print("s1 = \n",s1)
    print("===================================================")

    print("s2 = \n",s2)
    print("===================================================")

    print("y = \n",y)
    print("===================================================")
    return
# printParams1()
#===============================================================================
#multiply a by s1 (a is a matrix of polynomials, s1 is a vector of polynomials)
#dim of s1 = l x1
#dim of a = k x l
#dim of as1 = k x 1
def matrixVectorMult(a, s1, q, n):
    as1 = []
    for i in range(len(a)):
        row = PolynomialModRq([0], q, n)
        for j in range(len(a[0])):
            row.add(a[i][j].multiply(s1[j]))
        as1.append(row)
    return as1

as1 = matrixVectorMult(a, s1, q, n)

def addT(as1, s2, q, n):
    t = []
    for i in range(len(as1)):
        t.append(as1[i].add(s2[i]))
    return t

t = addT(as1, s2, q, n)

# print("t = \n", t)

w = matrixVectorMult(a, y, q, n)
# print("w = \n", w)
wCopy = w.copy()
w_dash = [pol.get_coefficients() for pol in wCopy]
print("w_dash = \n", w_dash)
#===============================================================================
#generate message msg such that msg \in {0,1}^*
def generateMsg():
    msg = []
    for i in range(2**d):
        msg.append(random.randint(0,1))
    return msg

msg = generateMsg()
# print("msg = \n", msg)
#===============================================================================
def w_upper(w, d):
    #each entry in w is a polynomial which can be represented as a list of coefficients
    #each coefficient is an integer between 0 and q-1
    #we want to convert each coefficient into a binary string
    #then divide each binary string a_0 = b_0 + c_0 where b_0 is the first d bits of a_0 and c_0 is the remaining bits
    #then we want to convert b_0 into an integer and c_0 into an integer

    pass
#===============================================================================
#concat w with msg and then hash it using SHA1-128 to get a scalar
import hashlib
def concat(w, msg):
    for i in range(len(w)):
        w[i] = w[i].to_bytes()
    msg = bytes(msg)
    ret = b''.join(w) + msg
    return ret

def hashMsg(w, msg):
    hash = hashlib.sha1(concat(w, msg))
    return hash

#hash the message to get a scalar
scalar = hashMsg(w, msg)
scalar = scalar.hexdigest()

# print("c = ", scalar)

#convert c into a binary string
def hexToBinary(c):
    binary = bin(int(c, 16))[2:]
    return binary

binary = hexToBinary(scalar)
# print("binary = ", binary)

#convert binary string into an integer
def binaryToInt(binary):
    return int(binary, 2)

c = binaryToInt(binary)
# print("binary = ", c)

#===============================================================================
def scalarVectorMult(scalar, s1, q, n):
    c = []
    for poly in s1:
        poly = poly.get_coefficients()
        c.append(poly)
    for i in range(len(c)):
        for j in range(len(c[0])):
            c[i][j] = (c[i][j] * scalar) % q
    return c

cs1 = scalarVectorMult(c, s1, q, n)
# print("cs1 = \n", cs1)
y_dash = [pol.get_coefficients() for pol in y]
# print("y_dash = \n", y_dash)

def addVectors(cs1, y_dash, q, n):
    row = []
    z = []
    for i in range(len(cs1)):
        for j in range(len(cs1[0])):
            row.append((cs1[i][j] + y_dash[i][j]) % q)
        z.append(row)
        row = []
    return z

z = addVectors(cs1, y_dash, q, n)
# print("z = \n", z)
#===============================================================================
