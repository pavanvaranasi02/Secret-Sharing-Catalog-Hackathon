import json
import sys
from field_math import *

sys.setrecursionlimit((10000000)) 

# Read the content from "data.json"
with open('vss_valid2.json', 'r') as file:
    json_content = file.read()

# Parse the JSON data
data = json.loads(json_content)

index = int(data["share"]["index"])
index_values = int(data["share"]["value"]["value"], 16)

prime = int(data["share"]["value"]["prime"], 16)
commitment_values = []
group_data = data["group"]
generator_value = int(group_data["generator"]["data"]["value"])
generator_prime = int(group_data["generator"]["data"]["prime"], 16)
commitment_prime = ""



C = 1
j = index
for cmt in data["commitments"]:
    commitment_prime = int(cmt["data"]["prime"], 16)
    commitment_values.append(int(cmt["data"]["value"], 16))

q = commitment_prime
p = prime
# print(q%(q)," jndijsd")

count=0
for i in (range(len(commitment_values))):
    y=inverse(j,count,p)%p
    C = (C*(inverse(commitment_values[i], y, q)))%q # C = ci%cp
    count+=1
    
# print(index, index_values, prime)
# print(commitment_prime, commitment_values)
# print(generator_prime, generator_value)
v = (inverse(generator_value, index_values%p, q))%q   # v = (g^f(i))%q
print('v:', v)
C = C%q            # C = C%q
print('C:', C)
print(v == C)
# val = inverse(generator_value, C, q)
# print('val:', val)