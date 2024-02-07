from helper import *
#parameters
# q = 2**23 - 2**13 + 1
q =17
n = 5
k = 4
l = 4
eta = 2
d = 14
tau = 39
beta = 78
gamma_1 = 2**17
phi = 1753

#generate params
a = randomMatrix(k, l, q, n)
s1 = S_eta(eta, l)
s2 = S_eta(eta, k)
y = S_eta(gamma_1-1, l)

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

#calculate params
# t = modRq(matrixAdd(polyMultiply(a,s1), s2), q, n)
# w = modRq(a*y, q, n)

def printParams2():
    print("t = \n", t)
    print("===================================================")

    print("w = \n", w)
    print("===================================================")
    return

print("t = \n", s1)
print("===================================================")
# w_upper = 
# c = 
# z = y + c * s1

# #key gen

# #sign

# #verify

    

#============================================================================================================================================================
def randomMatrix(k, l, q, n):
    matrix = []
    for i in range(k):
        row = []
        for j in range(l):
            row.append(randomPolynomial(q, n))
        matrix.append(row)
    return matrix

def randomPolynomial(q, n):
    polynomial = []
    for i in range(n):
        polynomial.append(random.randint(0, q-1))
    return polynomial
#============================================================================================================================================================
# S_eta(eta, l) generates a vector of length l with entries which are polynomials in R with coefficients between -eta and eta
def ranPoly(eta, n):
    poly = []
    for i in range(n):
        poly.append(random.randint(-eta, eta))
    return poly

def S_eta(eta, l, n):
    return [[ranPoly(eta, n)] for _ in range(l)]