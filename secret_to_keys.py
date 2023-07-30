from random import randint
from math import ceil
import sys
import json
from field_math import *

sys.setrecursionlimit((10000000)) 

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

def func(rndm_D, i, prime_num):
    val=0
    x=1
    for el in rndm_D:
        val=(val+(el*x)%prime_num)%prime_num
        x=(x*i)%prime_num
    return val
    

# Takes highest possible prime.
prime_num = 8417601304505654543
n = int(input('Shares: '))

# Secret is given by the user
D = int(input('Enter a secret key: '))

# Minimum number of keys to get Secret back by using lagrange Coeeficient
k = int(input('Threshold: '))

# Random Values for Coefficients of the polynomial equation.
rndm_D = [D]
print('Commitment Values:',hex(inverse(2, rndm_D[-1], prime_num)).replace('0x', ''))
for i in range(k-1):
    rndm_D.append(randint(1, (prime_num-1)))
    print('Commitment Values:',hex(inverse(2, rndm_D[-1], prime_num)).replace('0x', ''))
    
print(hex(prime_num).replace('0x', ''))
# print("Coefficients:", rndm_D)


# Values Distributed to the users.
keys = [-1]
hex_keys = []
for i in range(n):
    keys.append(func(rndm_D, i+1, prime_num))
    hex_keys.append(hex(keys[-1]).replace('0x', ''))
    
print('hex Keys:', hex_keys)
print('Keys: ', keys)

# R
# x=[i for i in range(1, k+1)]
# ys=[keys[i] for i in xs]
# xs = []
# for i in range(1, k+1):
#     xs.append((i, keys[i]))
    
# print(xs)
# val=lagrange_interpolation(xs,prime_num)
# # val=interpolation(x,keys,prime_num)
# print('Original Secret: ', D%prime_num)
# print('Calculated Secret: ', val)
