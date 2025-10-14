# You are given a list of temperatures in Celsius.
# Write a program to convert them to Fahrenheit and store the results in a dictionary where key = Celsius value and value = Fahrenheit value.

# Example Input:

# temps = [0, 20, 37, 100]

# Expected Output:

# {0: 32.0, 20: 68.0, 37: 98.6, 100: 212.0}

temps = [0, 20, 37, 100]
d={}
for i in temps:
    d[i]=f"{(i*1.8)+32:.1f}"
print(d)

# You are given a paragraph containing text-based emojis.
# Create a dictionary mapping each emoji symbol to its word meaning (like ":)" → "smile") using regex, then replace all emojis in the text with their meanings.

# Example Input:

# text = "Hey :) How are you :( I missed you <3"

# Expected Output:

# {':)': 'smile', ':(': 'sad', '<3': 'love'}
# # Modified text: "Hey smile How are you sad I missed you love"

import re
text = "Hey :) How are you :( I missed you <3"
e= {':)': 'smile', ':(': 'sad', '<3': 'love'}
p = re.findall(r'(:\)|:\(|<3)',text)
print(p)
d={}
for i in p:
    if i == ":)":
        d[i]="happy"
    elif i==":(":
        d[i]="sad"
    elif i=="<3":
        d[i]="love"
print(d)
for i in p:
    text=text.replace(i,d[i])
print(text)

# You are given a paragraph of text.
# Write a program to create a reverse index dictionary where:

# Each word (case-insensitive) is a key

# The value is a list of sentence numbers where the word appears


# Example Input:

# text = "Python is great. I love Python programming. Great tools exist for Python."

# Expected Output:

# {
#   'python': [1, 2, 3],
#   'is': [1],
#   'great': [1, 3],
#   'i': [2],
#   'love': [2],
#   'programming': [2],
#   'tools': [3],
#   'exist': [3],
#   'for': [3]
# }

import re
text = "Python is great. I love Python programming. Great tools exist for Python."
s=re.split(r'\.\s+',text)
print(s)
d={}
for i in range(len(s)):
    w=re.findall(r'\b\w+\b',s[i].lower())
    print(w)
    for j in w:
        if j not in d:
            d[j]=[i+1]
        else:
            if (i+1) not in d[j]:
                d[j].append(i+1)
print(d)

# Write a Python program that analyzes a server log file and categorizes log entries into a dictionary based on log level (INFO, ERROR, DEBUG, etc.).

# Example Input:

# log = """
# [INFO] System started
# [DEBUG] Loading configuration
# [ERROR] Connection failed
# [INFO] Retrying connection
# """

# Expected Output:

# {
#   'INFO': ['System started', 'Retrying connection'],
#   'DEBUG': ['Loading configuration'],
#   'ERROR': ['Connection failed']

import re
log = """[INFO] System started
[DEBUG] Loading configuration
[ERROR] Connection failed
[INFO] Retrying connection
"""
p=re.findall(r'\[(\S+)\]\s(.*)',log)
print(p)
d={}
for i in p:
    if i[0] not in d:
        d[i[0]]=[i[1]]
    else:
        d[i[0]].append(i[1])
print(d)

# Question 5:
# You are given two product data strings from different systems.
# Each contains product IDs and prices.
# Use regex to extract the data and merge into a single dictionary —
# if the same product appears in both, keep the average price.

# Example Input:

# data1 = "ID101: $50, ID102: $75, ID103: $100"
# data2 = "ID102: $65, ID104: $120, ID101: $55"

# Expected Output:

# {
#   'ID101': 52.5,
#   'ID102': 70.0,
#   'ID103': 100.0,
#   'ID104': 120.0
# }

import re
data1 = "ID101: $50, ID102: $75, ID103: $100"
data2 = "ID102: $65, ID104: $120, ID101: $55"
p1=re.findall(r'(ID\d+):\s\$(\d+)',data1)
p2=re.findall(r'(ID\d+):\s\$(\d+)',data2)
print(p1)
print(p2)
d={}
for i in p1:
    d[i[0]]=(int(i[1]))   
print(d) 
for i in p2:
    if i[0] in d:
        d[i[0]]=((d[i[0]])+int((i[1])))//2
    else:
        d[i[0]]=i[1]
print(d)


                

