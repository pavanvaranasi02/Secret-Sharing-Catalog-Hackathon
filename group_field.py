from field_math import *

def field(q,p):
    set1 = set()
    k=0
    for i in range(1,p*2+1):
        temp = (pow(q, i, p))%p
        # print(temp,q**i)
        if(temp in set1):
            k+=1
        else:
            set1.add(temp)
        if(k==p//2):
            break
    ans = list(set1)
    print(ans)

def field(g, a, b, p):
    val = find(a, b, p)
    print(inverse(g, val, p))
    
    
g=int(input("Enter g:"))
a=int(input("Enter a:"))
b=int(input("Enter b:"))
p=int(input("Enter p:"))
field(g, a, b, p)