# Write a Python program that takes a list of fruits and their prices in two separate lists and combines them into a dictionary mapping fruit → price.

# Example Input:
# fruits = ["apple", "banana", "cherry"]
# prices = [100, 40, 150]
# Expected Output:
# {'apple': 100, 'banana': 40, 'cherry': 150}

fruits = ["apple", "banana", "cherry"]
prices = [100, 40, 150]
d={}
for i in fruits:
    for j in prices:
        d[i]=j
        prices.remove(j)
        break
print(d)

# Given a paragraph containing product names followed by IDs in brackets, extract all pairs and store them in a dictionary with product name as key and ID as value.

 

# Example Input:

 

# text = "Laptop (P123), Mouse (P456), Keyboard (P789)"

 

# Expected Output:

 

# {'Laptop': 'P123', 'Mouse': 'P456', 'Keyboard': 'P789'}

import re
text = "Laptop (P123), Mouse (P456), Keyboard (P789)"
p=re.findall(r'(\w+)\s\((\w+)\)',text)
print(p)
d={}
for i in p:
    d[i[0]]=i[1]
print(d)

# You have a set of system event logs.

# Extract all timestamps, usernames, and actions, and create a dictionary where each username maps to a list of tuples — each tuple containing timestamp and action.

 

# Example Input:

 

# log = """

# [2025-10-06 10:00] user=alice action=login

# [2025-10-06 10:05] user=bob action=upload

# [2025-10-06 10:15] user=alice action=logout

# """

 

# Expected Output:

 

# {

#   'alice': [('2025-10-06 10:00', 'login'), ('2025-10-06 10:15', 'logout')],

#   'bob': [('2025-10-06 10:05', 'upload')]

# }

 
import re
log = """

[2025-10-06 10:00] user=alice action=login

[2025-10-06 10:05] user=bob action=upload

[2025-10-06 10:15] user=alice action=logout

"""
p=re.findall(r"\[(\S+\s\S+)\]\suser=(\w+)\saction=(\w+)",log)
print(p)
d={}
for i in p:
    if i[1] not in d:
        d[i[1]]=[(i[0],i[2])]
    else:
        d[i[1]].append((i[0],i[2]))
print(d)

# You are given survey results containing ratings per department.

# Extract each department and its numeric ratings, and compute the average rating per department using a dictionary.

 

# Example Input:

 

# text = "HR: 4, IT: 5, HR: 3, Finance: 4, IT: 4"

 

# Expected Output:

 

# {'HR': 3.5, 'IT': 4.5, 'Finance': 4.0
import re
text = "HR: 4, IT: 5, HR: 3, Finance: 4, IT: 4"
p=re.findall(r"(\S+):\s(\d+)",text)
print(p)
d={}
for i in p:
    if i[0] not in d:
        d[i[0]]=[int(i[1])]
    else:
        d[i[0]].append(int(i[1]))
print(d)
for i in d:
    d[i]=sum(d[i])/len(d[i])
print(d)
 
# Given a text containing employee details, extract the department, employee name, and salary, and store the information in a nested dictionary grouped by department.

 

# Example Input:

 

# data = """

# Dept: HR Name: Alice Salary: 50000

# Dept: IT Name: Bob Salary: 60000

# Dept: HR Name: Carol Salary: 52000

# """

 

# Expected Output:

 

# {

#   'HR': {'Alice': 50000, 'Carol': 52000},

#   'IT': {'Bob': 60000}

# }
import re
data = """

Dept: HR Name: Alice Salary: 50000

Dept: IT Name: Bob Salary: 60000

Dept: HR Name: Carol Salary: 52000

"""
import re
p=re.findall(r"Dept:\s(\w+)\sName:\s(\w+)\sSalary:\s(\d+)",data)
print(p)
d={}
for i in p:
    print(i[0])
    if i[0] not in d:
        d[i[0]]=[{i[1],i[2]}]
    else:
        d[i[0]].append({i[1],i[2]})
print(d)

