import numpy as np
from sympy import Matrix

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(np.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def next_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1

# Helper function to generate a random matrix over a given field
def random_matrix(modulus, rows, cols):
    return np.random.randint(0, modulus, size=(rows, cols), dtype=np.int64) % modulus

# Helper function to calculate the inverse of a matrix over a given field
def matrix_inverse(matrix, modulus):
    return np.linalg.inv(matrix) % modulus

# Helper function to create a block matrix from two matrices
def block_matrix(matrix1, matrix2):
    return np.block([[matrix1, matrix2]])

# Generate lattice parameters
n = 5
m = 2 * n   # take 2n
q = next_prime(n**2)  # take prime s.t. q ~ n^2
print("n =", n)
print("m =", m)
print("q =", q)

# Generate random matrices over the field Z_q
A1 = random_matrix(q, n, n)
A2 = random_matrix(q, n, m - n)

print ("A1 =")
print (A1)

print ("A2 =")
print (A2)
