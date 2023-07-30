import json
from random import randint


H = []
prime = 23
n, k = 5, 3
g = 3
q = 43
Sigma = []
Commitments = []
vis=[0]*n
p = 119
error = 0

def get_hash(i, phi, gai0, Ri):
    return ((i)+((gai0)*p)+(Ri*p*p))%p
    

class Node:
    def __init__(self, id, secret_code) -> None:
        self.coeff = [secret_code]+[randint(1, prime-1) for i in range(k)]
        self.id = id
        self.k = randint(1, prime-1)
        self.Ri = pow(g, self.k, q)
        self.c = get_hash(id, "", pow(g, secret_code, q), self.Ri)
        self.sigma = [self.Ri, k+secret_code*self.c]
        self.commitments = [pow(g, coeff, q) for coeff in self.coeff]
    
    def broadcast(self):
        Sigma.append([self.id]+self.sigma)
        Commitments.append(self.commitments)
        
    def check(self, i, R, u, cl):
        u=pow(g,u,q)
        cl=pow(Commitments[i][0], -cl, q)
        return (u*cl)%q == R
    
    def verify(self):
        for ls in Sigma:
            if ls[0]!=self.id:
                cl = get_hash(ls[0], "", Commitments[ls[0]][0], ls[1])
                if(not self.check(ls[0], ls[1], ls[2], cl)):
                    global error 
                    error = 1
                    print(ls)
                    return False
                else:
                    print(ls)
                    # Sigma.remove(ls)
        return True
                
                    
    def __str__(self):
        return f'{self.coeff} \n{self.id} \n{self.k} \n{self.Ri} \n{self.c} \n{self.sigma} \n{self.commitments}'
    
nodes=[]
secret_codes=[1323,463,5425,9878,432]
for i in range(1,n+1):
    nodes.append(Node(i,secret_codes[i-1]))
for nd in nodes:
    nd.broadcast()
    # print(str(nd))
    

print((Sigma))

for nd in (nodes):
    nd.verify()

print((Sigma))
print(error)