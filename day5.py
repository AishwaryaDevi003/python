# 

s="code"
d={}
for i in s:
    if i in d:
        continue
    else:
        d[i]=ord(i)
print(d)

# You are given a text that contains dates in various formats.
# Extract all valid dates and store them in a dictionary with their index as the key and the date string as the value.

# Example Input:

# text = "Meetings are on 2025-10-06, 10/07/2025, and 08-Nov-2025."

# Expected Output:

# {0: '2025-10-06', 1: '10/07/2025', 2: '08-Nov-2025'}

import re
text="Meetings are on 2025-10-06, 10/07/2025, and 08-Nov-2025."
p=re.findall(r"(\d+-?/?\S+?\d+-?\d+)",text)
print(p)
d={}
for i in range(len(p)):
    d[i]=p[i]
print(d)

# Extract domain names from a text of email addresses and count how many times each domain appears.

# Example Input:

# text = "mike@gmail.com, anna@yahoo.com, bob@gmail.com, tom@outlook.com, jane@yahoo.com"

# Expected Output:

# {'gmail.com': 2, 'yahoo.com': 2, 'outlook.com': 1}
import re
text = "mike@gmail.com, anna@yahoo.com, bob@gmail.com, tom@outlook.com, jane@yahoo.com"
p=re.findall(r"@(\S+.com)",text)
print (p)
d={}
for i in p:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

# You are given logs of students and their scores in various subjects.
# Extract data and store it in a nested dictionary where the key is the student name and the value is another dictionary of subject: score.

# Example Input:

# log = """
# Student: Alice Subject: Math Score: 89
# Student: Bob Subject: Physics Score: 76
# Student: Alice Subject: English Score: 92
# """

# Expected Output:

# {
#   'Alice': {'Math': 89, 'English': 92},
#   'Bob': {'Physics': 76}
# }

import re
log = """
Student: Alice Subject: Math Score: 89
Student: Bob Subject: Physics Score: 76
Student: Alice Subject: English Score: 92
"""
p=re.findall(r"\S+:\s(\S+)\s\S+:\s(\S+)\s\S+:\s(\S+)",log)
print(p)
d={}
for i,j,k in p:
    if i not in d:
        d[i]={}
    d[i][j]=int(k)
print(d)

# Given a chat log containing messages with usernames and timestamps, extract each user and the messages they sent in a dictionary format.

# Example Input:

# chat = """
# [10:01] Alice: Hi Bob!
# [10:02] Bob: Hey Alice!
# [10:03] Alice: How are you?
# """

# Expected Output:

# {
#   'Alice': ['Hi Bob!', 'How are you?'],
#   'Bob': ['Hey Alice!']
# }
import re
chat = """
[10:01] Alice: Hi Bob!
[10:02] Bob: Hey Alice!
[10:03] Alice: How are you?
"""
p=re.findall(r"\S+\s(\S+):(.+)",chat)
print(p)
d={}
for i,j in p:
    if i not in d:
        d[i]=[]
    d[i].append(j)
print(d)