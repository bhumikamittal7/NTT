from helper import *
#===============================================================================
q = 2**23 - 2**13 + 1
n = 256
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
printParams1()
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
#===============================================================================

#generate message msg such that msg \in {0,1}^*
def generateMsg():
    msg = []
    for i in range(2**d):
        msg.append(random.randint(0,1))
    return msg

msg = generateMsg()
# print("msg = \n", msg)

#concat w with msg and then hash it using SHA1-128 to get a scalar
import hashlib
def concat(w, msg):
    # concat = w + msg #can i do this?
    concat = byte(w) + byte(msg)
    return concat

def hashMsg(w, msg):
    hash = hashlib.sha1(concat(w, msg))
    return hash

#hash the message to get a scalar
scalar = hashMsg(w, msg)
print("scalar = \n", scalar)