from random import randint
from math import ceil
import sys
# from support import *
import json

sys.setrecursionlimit((10000000)) 

# Read the content from "data.json"
with open('dup_data.json', 'r') as file:
    json_content = file.read()

# Parse the JSON data
data = json.loads(json_content)

# Extract values of the "value" field for each distinct index
index_values = {}
prime = ""
for share in data["shares"]:
    index = share["index"]
    value = share["value"]["value"]
    prime = share["value"]["prime"]
    index_values[index] = value

# Print the values for each distinct index
shares = []
for index, value in index_values.items():
    shares.append((index, int(value, 16)))
    
# print(shares)

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

prime = int(prime, 16)
# print(prime)

take_shares(shares, prime)