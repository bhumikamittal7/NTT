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

# Create block matrix A
A = block_matrix(A1, A2)
print("Number of rows of A (n):", A.shape[0])
print("Number of columns of A (m):", A.shape[1])

# Calculate the inverse of A1
A1_inverse = matrix_inverse(A1, q)
# Print A1_inverse if needed
# print(A1_inverse)

# Calculate H1
H1 = -np.dot(A1_inverse, A2)
H1 = Matrix(H1).lift()

# Calculate H2
H2 = q * np.identity(n)
H2 = Matrix(H2).lift()

# Calculate H3
H3 = np.identity(m - n)
H3 = Matrix(H3).lift()

# Calculate H4
H4 = np.zeros((n, n), dtype=int)
H4 = Matrix(H4).lift()

# Augment matrices to form H_upper and H_lower
H_upper = H1.augment(H2)
H_lower = H3.augment(H4)

# Stack H_upper and H_lower to form H
H = H_upper.stack(H_lower)
print("Number of rows of H (m):", H.nrows())
print("Number of columns of H (m):", H.ncols())
# Print H if needed
# print(H)

# Convert H to a dense matrix
H_new = Matrix(H)

# Perform LLL reduction
reduced_H, _ = H_new.transpose().LLL()

# Print the results if needed
# print("Original H:")
# print(H_new)
# print('---------------------------')
# print("Reduced H:")
# print(reduced_H)
# print(reduced_H[0])
