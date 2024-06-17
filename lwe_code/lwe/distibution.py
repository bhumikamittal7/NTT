import random

def bernoulli(p):
    return random.random() < p

def uniform_sampling(number_of_bits):
    p = 0.5
    result = 0
    for _ in range(number_of_bits):
        result <<= 1
        result |= bernoulli(p)
    return result

