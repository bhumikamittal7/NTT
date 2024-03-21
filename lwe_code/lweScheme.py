from petlib.bn import Bn
import numpy as np
import math
from normalDist import dist

n=2**8
q=n**2
alpha =1/(math.sqrt(2*math.pi*n)*(math.log2(n))**2)
m=2*n
ksd=25

#### bits required to represent 'num'. Note that 'num' starts from 1 and not 0 in our case.
def bit_extract(num):
    return int(math.log2(num))

### initialize Zq
Zq=int(Bn.get_prime(bit_extract(q),safe=0))

### matrix multiplication over Zq
def mtxmult_Zq(a,b):
    return np.mod(np.matmul(a,b),Zq)

### matrix addition over Zq
def mtxadd_Zq(a,b):
    return np.mod(np.add(a,b),Zq)
    
A = np.random.randint(0,Zq, (n,m),dtype=int)
s = np.random.randint(0,Zq, (n,),dtype=int)
e = np.array(dist(alpha*q,m))

b=mtxadd_Zq(mtxmult_Zq(np.transpose(A),s),e)

print(A,b)
