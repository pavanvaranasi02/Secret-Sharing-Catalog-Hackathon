from random import randint
from math import ceil
import sys
# from support import *
import json

sys.setrecursionlimit((10000000)) 

# Print the values for each distinct index
shares = [-1, 111898491473545177384928253740829263784, 80936128512288804002949965084853625989, 83128464517013186486437147951121697361, 14234972942152512503595714586795948218, 152417740372945552911018640409491185480, 121013049146002010465532607028277923401, 64663069104074844924146108908685177580, 125560438894246244703291038216368250530, 91358754874688794145918088714166671802, 65454884932347995054882497291972821299]
# print(shares)
n = len(shares)
xs = []
for i in range(1, n):
    xs.append((i, shares[i]))
    

def lagrange_interpolation(xs, PRIME):
    result = 0
    x=0
    x_values, y_values = [], []
    for ls in xs:
        x_values.append(ls[0])
        y_values.append(ls[1])
    
    for i, x_i in enumerate(x_values):
        numerator, denominator = 1, 1
        for j, x_j in enumerate(x_values):
            if i != j:
                numerator = (numerator * (x - x_j)) % PRIME
                denominator = (denominator * (x_i - x_j)) % PRIME
        result = (result + (numerator * pow(denominator, -1, PRIME) * y_values[i])) % PRIME
    return result


def take_shares(shares, prime):
    val=lagrange_interpolation(shares,prime)
    print(val)

prime = (1<<127)-1
# print(prime)

take_shares(xs, prime)