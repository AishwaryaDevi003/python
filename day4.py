# you have a log file with multiple modules and their execution times per day.
# Extract data using regex and create a nested dictionary:
# Outer keys: dates
# Inner keys: module names
# Values: average execution time per module per date
# Example Input:
# log = """
# [2025-10-01] Module: auth Time: 2.5s
# [2025-10-01] Module: db Time: 1.8s
# [2025-10-01] Module: auth Time: 3.1s
# [2025-10-02] Module: db Time: 2.0s
# """
# Expected Output:
# {
#   '2025-10-01': {'auth': 2.8, 'db': 1.8},
#   '2025-10-02': {'db': 2.0}
# }

import re
log = """
[2025-10-01] Module: auth Time: 2.5s
[2025-10-01] Module: db Time: 1.8s
[2025-10-01] Module: auth Time: 3.1s
[2025-10-02] Module: db Time: 2.0s
"""
p=re.findall(r"\[(\d+-\d+-\d+)]\s\S+\s(\S+)\s\S+\s(\d.\d)",log)
print(p)
d={}
for i,j,k in p:
    if i not in d:
        d[i]={}
    if j not in d[i]:
        d[i][j]=[]
    d[i][j].append(float(k))
for i in d:
    for j in d[i]:
        d[i][j]=sum(d[i][j])/len(d[i][j])
print(d)

# Write a Python program that scans a document and extracts named entities (like Person, Organization, Location) using provided tags, and organizes them in a dictionary.
# Example Input:
# text = "Alice(PERSON) works at Google(ORG) in California(LOC). Bob(PERSON) joined Amazon(ORG)."
# Expected Output:
# {
#   'PERSON': ['Alice', 'Bob'],
#   'ORG': ['Google', 'Amazon'],
#   'LOC': ['California']
# }
import re
s="Alice(PERSON) works at Google(ORG) in California(LOC). Bob(PERSON) joined Amazon(ORG)."
p=re.findall(r"(\S+)\((\S+)\)",s)
print(p)
d={}
for i,j in p:
    if j not in d:
        d[j]=[]
    if i not in d[j]:
        d[j].append(i)
print(d)

# Given a system log file, extract all IP addresses and classify them as public or private, storing the results in a dictionary.
# Example Input:
# log = """
# Connected to 192.168.1.10
# Request from 8.8.8.8
# User 10.0.0.2 logged in
# Contacted 172.16.0.5 and 203.0.113.45
# """
# Expected Output:
# {
#   'private': ['192.168.1.10', '10.0.0.2', '172.16.0.5'],
#   'public': ['8.8.8.8', '203.0.113.45']
# } 
import re
log = """
Connected to 192.168.1.10
Request from 8.8.8.8
User 10.0.0.2 logged in
Contacted 172.16.0.5 and 203.0.113.45
"""
p=re.findall(r"(\d+\.\d+\.\d+\.\d+)",log)
print(p)
d={"private":[],"public":[]}
for i in p:
    print(i)
    if i[:3]=="192" or i[:2]=="10" or i[:3]=="172":
        if i not in d["private"]:
            d["private"].append(i)
    else:
        if i not in d["public"]:
            d["public"].append(i)
print(d)

# Given a text of product reviews like this:
# "Laptop: ⭐⭐⭐⭐, Phone: ⭐⭐⭐, Laptop: ⭐⭐⭐⭐⭐, Tablet: ⭐⭐",
# extract all product ratings, compute the average star rating per product,
# and store the result in a dictionary.
# Expected Output:
# {'Laptop': 4.5, 'Phone': 3.0, 'Tablet': 2.0}

import re
s="Laptop: ⭐⭐⭐⭐, Phone: ⭐⭐⭐, Laptop: ⭐⭐⭐⭐⭐, Tablet: ⭐⭐"
p=re.findall(r"(\S+):\s(⭐+)",s)
print(p)
d={}
for i,j in p:
    if i not in d:
        d[i]=[len(j)]
    else:
        d[i].append(len(j))
for i in d:
    d[i]=sum(d[i])/len(d[i])
print(d)