from help import *

#============================ INTT - Iterative Gentleman Sande====================================#
def inttGS(NTTf, q, w):
    a = bit_reversal(NTTf)
    

    return a


# #============================ take params ====================================#

# k = int(input("Enter any k such that n = 2^k: "))
# n = 2**k

# q = take_q(n)
# w = take_w(q,n)
# NTTf = take_poly(n,q)

# #============================ print params ====================================#
# print ("n = ",n)
# print ("q = ",q)
# print ("w = ",w)
# print ("NTT(f(x)) = ",NTTf)

# #============================ print and compare ====================================#
# f = inttGS(NTTf,w,q)
# print ("Original f = ",f)


#============================ NTT ====================================#
def NTT(f,q,w):
    if len(f) == 1:
        return f
    else:
        f_even = [f[i] for i in range(0,len(f),2)]
        f_odd = [f[i] for i in range(1,len(f),2)]
        f_even = NTT(f_even,q,w**2)
        f_odd = NTT(f_odd,q,w**2)
        f = [0]*len(f)
        for i in range(len(f)//2):
            f[i] = (f_even[i] + w**i*f_odd[i])%q
            f[i+len(f)//2] = (f_even[i] - w**i*f_odd[i])%q
        return f
    