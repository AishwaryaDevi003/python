# Write a Python program that takes a list of names and creates a dictionary where each name is the key and the length of the name is the value.

# Example Input:

# names = ["Tom", "Jennifer", "Ali", "Chris"]

# Expected Output:
# {'Tom': 3, 'Jennifer': 8, 'Ali': 3, 'Chris': 5}

s=["Tom", "Jennifer", "Ali", "Chris"]
d={}
for i in s:
    d[i]=len(i)
print(d)



# Question:
# You are given a messy text containing phone numbers in different formats.
# Extract all valid 10-digit phone numbers and store them in a dictionary with the last 4 digits as the key and the full number as the value.
# Example Input:
# text = "Call 9876543210 or 987-654-3210. Alternate: (91234 56780)"
# Expected Output:
# {'3210': '9876543210', '6780': '9123456780'}

import re
text = "Call 9876543210 or 987-654-3210. Alternate: (91234 56780)"
p=re.findall(r"\d+-?\d+-?\d+\s?\d+",text)
print(p)
d={}
for i in p:
    n=i.replace("-"," ").replace("","")
    print(n)
    d[n[-4:]]=n
print(d)

# Example Input:

# log = """
# [2025-10-05] User: alice Action: login
# [2025-10-05] User: bob Action: upload
# [2025-10-06] User: alice Action: logout
# """

# Expected Output:

# {
#   'alice': {'2025-10-05': 'login', '2025-10-06': 'logout'},
#   'bob': {'2025-10-05': 'upload'}
# }

import re
log = """
[2025-10-05] User: alice Action: login
[2025-10-05] User: bob Action: upload
[2025-10-06] User: alice Action: logout
"""
p=re.findall(r"\[(\d+-\d+-\d+)]\s\S+:\s(\S+)\s\S+\s(\S+)",log)
print(p)
d={}
for i,j,k in p:
    print(i,j,k)
    if j not in d:
        d[j]={}
    d[j][i]=k
print(d)

# Question:
# Given a text of student marks in this format:
# "Alice: 89, Bob: 76, Charlie: 92, Alice: 95, Bob: 82",
# write a program to create a dictionary where each student's name is the key, and the average mark is the value.
# Expected Output:
# {'Alice': 92.0, 'Bob': 79.0, 'Charlie': 92.0}

import re
s="Alice: 89, Bob: 76, Charlie: 92, Alice: 95, Bob: 82"
p=re.findall(r"(\S+):\s(\d+)",s)
print(p)
d={}
for i,j in p:
    print(i,j)
    if i not in d:
        d[i]=[int(j)]
    else:
        d[i].append(int(j))
for i in d:
    d[i]=sum(d[i])/2
print(d)