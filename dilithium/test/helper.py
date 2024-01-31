import random
#============================================================================================================================================================
class PolynomialModRq:
    def __init__(self, coefficients, q, n):
        self.coefficients = coefficients
        self.q = q
        self.n = n

    def add(self, other):
        result_coeffs = [(a + b) % self.q for a, b in zip(self.coefficients, other.coefficients)]
        return PolynomialModRq(result_coeffs, self.q, self.n)

    def subtract(self, other):
        result_coeffs = [(a - b) % self.q for a, b in zip(self.coefficients, other.coefficients)]
        return PolynomialModRq(result_coeffs, self.q, self.n)
    
    def divide_polynomials(self, dividend, divisor):
        dividend.reverse()
        if not isinstance(dividend, list) or not isinstance(divisor, list):
            raise ValueError("Both dividend and divisor must be lists")

        if not all(isinstance(x, (int, float)) for x in dividend) or not all(isinstance(x, (int, float)) for x in divisor):
            raise ValueError("Both dividend and divisor must contain numerical elements")

        if not divisor:
            raise ValueError("Divisor list cannot be empty")

        if len(divisor) > len(dividend):
            raise ValueError("Degree of divisor must be less than or equal to the degree of dividend")

        result = list(dividend)

        for i in range(len(dividend) - len(divisor) + 1):
            factor = result[i] // divisor[0]

            for j in range(1, len(divisor)):
                result[i + j] -= factor * divisor[j]

        remainder = result[-len(divisor) + 1:]
        return remainder


    def multiply(self, other):
        result_coeffs = [0] * (self.n * 2 - 1)
        for i in range(self.n):
            for j in range(self.n):
                result_coeffs[i + j] = (result_coeffs[i + j] + self.coefficients[i] * other.coefficients[j]) % self.q

        remainder_coeffs = self.divide_polynomials(result_coeffs, [1] + [0] * (self.n - 2) + [1])

        return PolynomialModRq(remainder_coeffs, self.q, self.n)

    def get_coefficients(self):
        return self.coefficients

    def __str__(self):
        return " + ".join(f"{coeff}x^{i}" for i, coeff in enumerate(self.coefficients) if coeff != 0)
#============================================================================================================================================================

# q = 17
# n = 4
# poly1 = PolynomialModRq([1, 2, 3, 4], q, n)
# poly2 = PolynomialModRq([1, 2, 0, 1], q, n)
# poly3 = PolynomialModRq([1, 0, 0, 1], q, n)

# result_add = poly1.add(poly2)
# result_subtract = poly1.subtract(poly2)
# result_multiply = poly1.multiply(poly2)

# print(f"Poly1: {poly1}")
# print(f"Poly2: {poly2}")
# print(f"Add: {result_add.get_coefficients()}")
# print(f"Subtract: {result_subtract.get_coefficients()}")
# print(f"Multiply: {result_multiply.get_coefficients()}")
    
#============================================================================================================================================================

#now i want to define a matrix A with k rows and l columns where each entry is a polynomial in Rq
#polynomials can be generated using the PolynomialModRq class
import random
def generatePoly(q, n):
    coefficients = []
    for i in range(n):
        coefficients.append(random.randint(0, q-1))
    return PolynomialModRq(coefficients, q, n)

def generateMatrix(k, l, q, n):
    matrix = []
    for i in range(k):
        row = []
        for j in range(l):
            row.append(generatePoly(q, n))
        matrix.append(row)
    return matrix

#now we will generate a vector of length l with entries which are polynomials in R with coefficients between -eta and eta
def generateEtaPoly(q, n):
    coefficients = []
    for i in range(n):
        coefficients.append(random.randint(-q, q))
    return PolynomialModRq(coefficients, q, n)

def S_eta(eta, l, n):
    vector = []
    for i in range(l):
        vector.append(generateEtaPoly(eta, n))
    return vector
