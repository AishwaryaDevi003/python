# Create a class AccessControl that parses a text-based permission list and organizes it into a nested dictionary
# of {role: {user: [permissions]}}. Use regex to extract fields.

# Example Input:

# data = """
# Role: Admin | User: Alice | Permissions: Read, Write, Delete
# Role: User | User: Bob | Permissions: Read
# Role: Moderator | User: Charlie | Permissions: Read, Write
# Role: Admin | User: Dave | Permissions: Write, Delete
# """

# Expected Output:

# {
#   'Admin': {
#     'Alice': ['Read', 'Write', 'Delete'],
#     'Dave': ['Write', 'Delete']
#   },
#   'User': {'Bob': ['Read']},
#   'Moderator': {'Charlie': ['Read', 'Write']}
# }
# import re
# class AccessControl:
#     def parse(self, data):
#         d={}
#         l=re.findall(r"Role:\s*(.*?)\s*\|\s*User:\s*(.*?)\s*\|\s*Permissions:\s*(.*)", data)
#         print(l)
#         for r,u,p in l:
#             part = p .split(',')
#             l=[]
#             for i in part:
#                 l.append(i.strip())
#             if r not in d:
#                 d[r]={}
#             d[r][u]=l
#         return d
# data = """Role: Admin | User: Alice | Permissions: Read, Write, Delete
# Role: User | User: Bob | Permissions: Read
# Role: Moderator | User: Charlie | Permissions: Read, Write
# Role: Admin | User: Dave | Permissions: Write, Delete
# """
# ac = AccessControl()
# result = ac.parse(data)
# print(result)

# Hard Question 2 — Class + Regex + Dynamic Grouping (Invoice Summarizer)

# You are given invoice details in text format.
# Build a class InvoiceSummarizer that:

# 1. Extracts Invoice ID, Customer Name, and Amount using regex.


# 2. Groups all invoices by Customer Name in a dictionary.


# 3. Provides a method total_by_customer() that returns each customer’s total billed amount.



# Example Input:

# data = """
# Invoice: INV001 | Name: John | Amount: $250.50
# Invoice: INV002 | Name: Alice | Amount: $300.00
# Invoice: INV003 | Name: John | Amount: $120.75
# """

# Expected Output:

# {
#   'John': {'invoices': ['INV001', 'INV003'], 'total': 371.25},
#   'Alice': {'invoices': ['INV002'], 'total': 300.00}
# }

# import re
# class InoviceSummarizer:
#     def parse(self, data):
#         d={}
#         l=re.findall(r"Invoice:\s*(.*?)\s*\|\s*Name:\s*(.*?)\s*\|\s*Amount:\s*\$(.*)", data)
#         for inv,name,amt in l:
#             amt=float(amt)
#             if name not in d:
#                 d[name]={'invoices':[],'total':0.0}
#             d[name]['invoices'].append(inv)
#             d[name]['total']+=amt
#         return d
# data = """Invoice: INV001 | Name: John | Amount: $250.50
# Invoice: INV002 | Name: Alice | Amount: $300.00
# Invoice: INV003 | Name: John | Amount: $120.75
# """
# ac = InoviceSummarizer()
# result = ac.parse(data)
# print(result)


# Hard Question 3 — Class + Regex Pattern Dispatcher (Custom Command Interpreter)

# Create a class CommandInterpreter that reads input lines representing shell-like commands
# and uses regex to identify command types and store execution metadata in a dictionary.

# Each command has one of these forms:

# COPY source.txt destination/

# MOVE file1.txt folderA/

# DELETE temp.log


# The class should categorize commands by action and record their arguments.

# Expected Output:

# {
#   'COPY': [{'src': 'source.txt', 'dest': 'destination/'}],
#   'MOVE': [{'src': 'file1.txt', 'dest': 'folderA/'}],
#   'DELETE': [{'file': 'temp.log'}]
# }

# import re
# class Command:
#     def parse(Self,data):
#         d={}
#         l=re.findall(r"(COPY|MOVE|DELETE)\s+([^\s]+)(?:\s+([^\s]+))?", data)
#         for cmd,src,dest in l:
#             if cmd not in d:
#                 d[cmd]=[]
#             if cmd in ['COPY','MOVE']:
#                 d[cmd].append({'src':src,'dest':dest})
#             elif cmd=='DELETE':
#                 d[cmd].append({'file':src})
#         return d
# data = """COPY source.txt destination/
# MOVE file1.txt folderA/
# DELETE temp.log
# """
# a=Command()
# r=a.parse(data)
# print(r)


# Hard Question 4 — Regex + Class + Data Linking (Employee Hierarchy Builder)

# Given a company hierarchy text, create a class HierarchyBuilder
# that uses regex to build a manager–employee dictionary tree.

# Example Input:

# data = """
# Manager: Alice -> Employees: Bob, Carol
# Manager: Bob -> Employees: David, Emma
# Manager: Carol -> Employees: Frank
# """

# Expected Output:

# {
#   'Alice': {
#     'Bob': {'David': {}, 'Emma': {}},
#     'Carol': {'Frank': {}}
#   }
# }

# (Nested structure: each manager key holds sub-dictionaries of their team.)
# import re
# class HierarchyBuild:
#     def parse(self,data):
#         d={}
#         l=re.findall(r"Manager:\s*(.*?)\s*->\s*Employees:\s*(.*)", data)
#         for m,e in l:
#             el=e.split(',')
#             lst=[]
#             for x in el:
#                 lst.append(x.strip())
#             d[m]=lst
#         all_m=set(d.keys())
#         all_e=set()
#         for v in d.values():
#             for emp in v:
#                 all_e.add(emp)
#         top=list(all_m - all_e)[0]
#         def tree(mgr):
#             team={}
#             if mgr in d:
#                 for emp in d[mgr]:
#                     team[emp]=tree(emp)
#             return team
#         r={top:tree(top)}
#         return r
    
# data = """Manager: Alice -> Employees: Bob, Carol
# Manager: Bob -> Employees: David, Emma
# Manager: Carol -> Employees: Frank
# """
# ac = HierarchyBuild()
# r = ac.parse(data)
# print(r)

# ⚔️ Hard Question 5 — Class + Regex Validation + Custom Exception Handling

# Create a class FormValidator that validates a set of form entries from text.
# Each entry includes name, email, and phone.
# Use regex validation and raise a custom InvalidDataError for incorrect records.
# Store valid entries in a dictionary {name: {'email': ..., 'phone': ...}}.

# Example Input:

# data = """
# Name: Ravi | Email: ravi@mail.com | Phone: 9876543210
# Name: Priya | Email: priya@@gmail | Phone: 99999
# Name: Arjun | Email: arjun.k@gmail.com | Phone: +919812345678
# """

# Expected Output:

# {
#   'Ravi': {'email': 'ravi@mail.com', 'phone': '9876543210'},
#   'Arjun': {'email': 'arjun.k@gmail.com', 'phone': '+919812345678'}
# }

# and raise an exception message for the invalid entry:

# InvalidDataError: Invalid email or phone for entry: Priya
    

import re
class InvalidDataError(Exception):
    pass
class formvalidat:
    def __init__ (self):
        self.d={}
    def parse(self,data):
        p=re.findall(r"Name:\s*(.*?)\s*\|\s*Email:\s*(.*?)\s*\|\s*Phone:\s*(.*)",data)
        print(p)
        for n,e,ph in p:
            email=re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",e)
            phone=re.match(r"^\+?\d{10,13}$", ph)
            if not email or not phone:
                print(f"InvalidDataError: Invalid email or phone for entry: {n}")
                continue
            self.d[n]={'email':e,'phone':ph}
        return self.d
data = """
Name: Ravi | Email: ravi@mail.com | Phone: 9876543210
Name: Priya | Email: priya@@gmail | Phone: 99999
Name: Arjun | Email: arjun.k@gmail.com | Phone: +919812345678
"""
ac = formvalidat()
r=ac.parse(data)
print(r)
    
