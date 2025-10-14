# Create a dictionary that maps numbers (1–5) to their squares using a loop.
# Expected Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n=5
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)


# Write a Python program that takes a paragraph as input and counts how many numeric values (like 123, 4.5, etc.) appear in it using regular expressions.
# Store the unique numbers as keys in a dictionary and their count of occurrences as values.
# Example Input:
# text = "I bought 3 apples, 4.5 kg of mangoes, and 3 more oranges. Total: 7.5 kg."
# Expected Output:
# {'3': 2, '4.5': 1, '7.5': 1}

import re
s="I bought 3 apples, 4.5 kg of mangoes, and 3 more oranges. Total: 7.5 kg."
p=re.findall(r"\d+\.?\d*",s)
print(p)
d={}
for i in p:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


# You have a log text containing multiple user activities.
# Extract all usernames and their IP addresses using regex and store them in a dictionary,
# where each username maps to a list of unique IPs.

# Example Input:
# log = """
# User: alice IP: 192.168.1.10  
# User: bob IP: 10.0.0.2  
# User: alice IP: 192.168.1.11  
# User: bob IP: 10.0.0.2
# """
# Expected Output:
# {
#   'alice': ['192.168.1.10', '192.168.1.11'],
#   'bob': ['10.0.0.2']
# }

import re
l="""User: alice IP: 192.168.1.10  
User: bob IP: 10.0.0.2  
User: alice IP: 192.168.1.11  
User: bob IP: 10.0.0.2"""
p=re.findall(r"\S+\s(\S+)\s\S+:\s(\d+\.\d+.\d+\.\d+)",l)
print(p)
d={}
for k,v in p:
    if k in d:
        if v not in d[k]:
            d[k].append(v)
    else:
        d[k]=[v]
print(d)
