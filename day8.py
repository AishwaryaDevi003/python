# Create a class StudentRecord that takes a block of text containing student details.
# Use regex to extract student name, ID, and marks and store them in a dictionary as:
# {student_id: {"name": name, "marks": marks}}

# Example Input:

# data = """
# ID: S101 Name: Alice Marks: 89
# ID: S102 Name: Bob Marks: 76
# ID: S103 Name: Carol Marks: 91
# """
# record = StudentRecord(data)
# record.get_all()

# Expected Output:

# {
#   'S101': {'name': 'Alice', 'marks': 89},
#   'S102': {'name': 'Bob', 'marks': 76},
#   'S103': {'name': 'Carol', 'marks': 91}
# }

import re
data = """ID: S101 Name: Alice Marks: 89
ID: S102 Name: Bob Marks: 76
ID: S103 Name: Carol Marks: 91
"""
p=re.findall(r"ID:\s(\w+)\sName:\s(\w+)\sMarks:\s(\d+)",data)
print(p)
d={}
for i in p:
    if i[0] not in d:
        d[i[0]]={"name":i[1],"marks":int(i[2])}
    else:
        d[i[0]].append(int(i[1]))
print(d)

# Create a class LogAnalyzer that can parse a log file using regex.
# Each log entry contains a timestamp, level, and message.
# The class should store logs in a dictionary grouped by log level and provide methods:

# get_errors() → returns all error messages

# count_by_level() → returns a dictionary of how many logs per level


# Example Input:

# log = """
# [2025-10-06 10:00] INFO Server started
# [2025-10-06 10:05] ERROR Connection failed
# [2025-10-06 10:10] INFO Retrying connection
# [2025-10-06 10:12] DEBUG Retrying sequence
# """

# Expected Output:

# {
#   'INFO': 2,
#   'ERROR': 1,
#   'DEBUG': 1
# }

import re
class logAnalyzer:
    def __init__(self, log):
        self.log = log
        self.logs_by_level = self.parse_logs()
    def parse_logs(self):
        p=re.findall(r"\[\d+-\d+-\d+\s\d+:\d+\]\s(\w+)\s(.*)",self.log)
        d={}
        for i in p:
            if i[0] not in d:
                d[i[0]]=[i[1]]
            else:
                d[i[0]].append(i[1])
        return d
    def get_errors(self):
        
        if 'ERROR' in self.logs_by_level:
            return self.logs_by_level['ERROR']
        else:
            return []
    def count_by_level(self):
        d={}
        for i in self.logs_by_level:
            d[i]=len(self.logs_by_level[i])
        return d
log="""
[2025-10-06 10:00] INFO Server started
[2025-10-06 10:05] ERROR Connection failed
[2025-10-06 10:10] INFO Retrying connection
[2025-10-06 10:12] DEBUG Retrying sequence
"""
a=logAnalyzer(log)
print(a.count_by_level())



# Create a class UserValidator that reads user registration data from text and validates using regex.
# Each user record contains a username, email, and phone.
# The class should store valid users in a dictionary with username as key and (email, phone) as value.
# Invalid entries should be ignored.

# Example Input:

# data = """
# Username: john Email: john@example.com Phone: 9876543210
# Username: anna Email: anna@@example Phone: 12345
# Username: mark Email: mark@gmail.com Phone: 9123456789
# """

# Expected Output:

# {
#   'john': ('john@example.com', '9876543210'),
#   'mark': ('mark@gmail.com', '9123456789')
# }

import re

class UserValidator:
    def __init__(self, data):
        self.data = data
        self.user = self.user()
    def user(self):
        p=re.findall(r"Username:\s(\w+)\sEmail:\s([\w\.-]+@[\w\.-]+)\sPhone:\s(\d{10})",self.data)
        d={}
        for i in p:
            d[i[0]]=(i[1],i[2])
        return d
data = """
Username: john Email: john@example.com Phone: 9876543210
Username: anna Email: anna@@example Phone: 12345
Username: mark Email: mark@gmail.com Phone: 9123456789
"""
a=UserValidator(data)
print(a.user)


# You are given a text that represents a warehouse stock log.
# Each entry includes a category, item name, and quantity.
# Write a program (or class) to extract this information using regex and store it as a nested dictionary in the form {category: {item: quantity}}.

# Example Input:

# data = """
# Category: Electronics Item: Laptop Qty: 10
# Category: Electronics Item: Phone Qty: 25
# Category: Furniture Item: Chair Qty: 15
# Category: Furniture Item: Table Qty: 5
# """

# Expected Output:

# {
#   'Electronics': {'Laptop': 10, 'Phone': 25},
#   'Furniture': {'Chair': 15, 'Table': 5}
# }

import re
class log:
    def __init__ (self, data):
        self.data=data
        self.logs=self.logs()
    def logs(self):
        p=re.findall(r"Category:\s(\w+)\sItem:\s(\w+)\sQty:\s(\d+)",self.data)
        d={}
        for i in p:
            if i[0] not in d:
                d[i[0]]={i[1]:int(i[2])}
            else:
                d[i[0]][i[1]]=int(i[2])
        return d
    
data = """Category: Electronics Item: Laptop Qty: 10
Category: Electronics Item: Phone Qty: 25
Category: Furniture Item: Chair Qty: 15
Category: Furniture Item: Table Qty: 5
"""
a=log(data)
print(a.logs)

# Create a class AccessLog that takes in a server access log text.
# Use regex to extract IP addresses, endpoints, and status codes, then:

# Store the results in a dictionary grouped by IP address.

# Add a method summary() that prints the count of requests per IP and the most common status code for that IP.


# Example Input:

# log = """
# 192.168.1.10 - GET /home 200
# 192.168.1.10 - POST /login 403
# 10.0.0.2 - GET /home 200
# 192.168.1.10 - GET /dashboard 200
# """

# Expected Output:

# {
#   '192.168.1.10': [
#       {'endpoint': '/home', 'status': 200},
#       {'endpoint': '/login', 'status': 403},
#       {'endpoint': '/dashboard', 'status': 200}
#   ],
#   '10.0.0.2': [
#       {'endpoint': '/home', 'status': 200}
#   ]
# }

# and

# Summary:
# 192.168.1.10 → 3 requests, Most common status: 200  
# 10.0.0.2 → 1 request, Most common status: 200


import re
class vlog:
    def __init__(self, log):
        self.log=log
        self.logs=self.logs()
    def logs(self):
        p=re.findall(r"(\d+\.\d+\.\d+\.\d+)\s-\s(\w+)\s(\/\w+)\s(\d+)",self.log)
        d={}
        for i in p:
            if i[0] not in d:
                d[i[0]]=[{"endpoint":i[2],"status":int(i[3])}]
            else:
                d[i[0]].append({"endpoint":i[2],"status":int(i[3])})
        return d    
    def summary(self):
        for i in self.logs:
            c=len(self.logs[i])
            s={}
            for j in self.logs[i]:
                if j['status'] not in s:
                    s[j['status']]=1
                else:
                    s[j['status']]+=1
            m=max(s,key=s.get)
            print(f"{i} - {c} requests, Most common status: {m}")
log = """
192.168.1.10 - GET /home 200
192.168.1.10 - POST /login 403
10.0.0.2 - GET /home 200
192.168.1.10 - GET /dashboard 200
"""
a=vlog(log)
print(a.logs)
a.summary()

