from petlib.bn import Bn
import numpy as np
import math
from normalDist import dist

n=2**8
q=n**2
alpha =1/(math.sqrt(2*math.pi*n)*(math.log2(n))**2)
m=2*n

#### bits required to represent 'num'. Note that 'num' starts from 1 and not 0 in our case.
def bit_extract(num):
    return int(math.log2(num))

#### initialize Zq
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

## public key and secret key
pk=(A,b)
sk=s

## encrypt a plaintext
def enc(ptxt,pk):
    if ptxt == 0 or ptxt == 1:
        A,b = pk
        r = np.random.randint(0,2,(m,),dtype=int)
        c1 = mtxmult_Zq(np.transpose(r),np.transpose(A))
        c2 = (mtxmult_Zq(np.transpose(r),b) + (ptxt*math.floor(Zq/2))) % Zq
        return (c1,c2)
    else: 
        return -1

## decrypt a ciphertext
def dec(ctxt,sk):
    if ctxt != -1:
        s = sk
        c1, c2 = ctxt
        ptxt = (c2 - mtxmult_Zq(c1,s)) % Zq
        if math.floor(Zq/4) < ptxt < math.floor(3*Zq/4):
            print("Plaintext is", 1)
        else:
            print("Plaintext is", 0)
    else:
        print("Error! -- Plaintext needs to a bit: 0 or 1")

## encryting "0" using pk and then decrypting the resultant ciphertext using sk.
dec(enc(0,pk),sk)