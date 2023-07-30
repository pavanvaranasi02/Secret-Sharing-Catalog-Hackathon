import sys

sys.setrecursionlimit((10000000)) 

def inverse(a,b,p):
    if(b==0): return 1
    val=inverse(a,b//2,p)
    val=(val*val)%p
    if b%2==0:
        return val
    return (val*a)%p



# def find(a, p):
#     if a < 0:
#         a = -a
#         return p - a % p
#     return a % p

def find(a, b, p):
    return (a*inverse(b,p-2,p))%p
    
# print(find(222, 11))
# print(find(22,1,11))
# print(find(-1,3,11))