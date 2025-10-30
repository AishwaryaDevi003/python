# Very Hard Question 1 — Polymorphic Regex Parser Framework

# Design a class hierarchy for a log parser framework:

# Base class BaseParser defines an abstract method parse_line(line).

# Subclasses ApacheParser, NginxParser, and SystemParser each have different regex patterns.

# A LogManager class takes multiple parsers, feeds log lines to the correct parser,
# and builds a dictionary grouped by parser type.


# Example Input:

# logs = [
#     '127.0.0.1 - - [06/Oct/2025:10:00] "GET /index.html HTTP/1.1" 200 512',
#     '2025/10/06 10:01:23 [info] Connection established',
#     '[2025-10-06 10:02:10] SYSTEM: Reboot triggered'
# ]

# Expected Output:

# {
#   'ApacheParser': [{'ip': '127.0.0.1', 'endpoint': '/index.html', 'status': 200}],
#   'NginxParser': [{'time': '2025/10/06 10:01:23', 'level': 'info', 'msg': 'Connection established'}],
#   'SystemParser': [{'time': '2025-10-06 10:02:10', 'msg': 'Reboot triggered'}]
# }

# from abc import ABC, abstractmethod
# import re
# class BaseParser(ABC):
#     @abstractmethod
#     def parse(self, line):
#         pass
# class ApacheParser(BaseParser):
#     def parse(self,line):
#         p=re.search(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(GET|POST) (.*?) HTTP/1\.1" (\d{3}) (\d+)', line)
#         if p:
#             return {'ip': p.group(1), 'endpoint': p.group(4), 'status': int(p.group(5))}
# class NginxParser(BaseParser):
#     def parse(self,line):
#         p=re.search(r'(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}) \[(.*?)\] (.*)', line)
#         if p:
#             return {'time': p.group(1), 'level': p.group(2), 'msg': p.group(3)}
# class SystemParser(BaseParser):
#     def parse(self,line):
#         p=re.search(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] SYSTEM: (.*)', line)
#         if p:
#             return {'time': p.group(1), 'msg': p.group(2)}
# class LogManager:
#     def __init__(self,parsers):
#         self.parsers=parsers
#     def process_logs(self,logs):
#         r={}
#         for i in logs:
#             for parser in self.parsers:
#                 res=parser.parse(i)
#                 if res:
#                     k=type(parser).__name__
#                     if k not in r:
#                         r[k]=[]
#                     r[k].append(res)
#                     break
#         return r
# logs = [
#     '127.0.0.1 - - [06/Oct/2025:10:00] "GET /index.html HTTP/1.1" 200 512',
#     '2025/10/06 10:01:23 [info] Connection established',
#     '[2025-10-06 10:02:10] SYSTEM: Reboot triggered'
# ]

# parsers = [ApacheParser(), NginxParser(), SystemParser()]
# lm = LogManager(parsers)
# result = lm.process_logs(logs)
# print(result)

    
    
    
# Very Hard Question 2 — Dataclass + Regex AutoMapper

# Create a @dataclass model UserProfile with fields:
# id, name, email, phone, address.

# Write a class DataAutoMapper that:

# 1. Takes text input with inconsistent delimiters (:, =, |, ;)


# 2. Uses regex to normalize and extract key-value pairs.


# 3. Auto-populates the UserProfile dataclass and stores it in a dictionary {id: UserProfile}.



# Example Input:

# data = """
# id=101 | name:Ravi Kumar | email:ravi.k@example.com | phone:9876543210 | address=Bangalore
# id:102; name=Priya Sharma; email=priya.s@gmail.com; phone=9123456789; address=Chennai
# """

# Expected Output:

# {
#   '101': UserProfile(id='101', name='Ravi Kumar', email='ravi.k@example.com',
#                      phone='9876543210', address='Bangalore'),
#   '102': UserProfile(id='102', name='Priya Sharma', email='priya.s@gmail.com',
#                      phone='9123456789', address='Chennai')
# }

# import re
# from dataclasses import dataclass
# @dataclass
# class UserProfile:
#     id: str
#     name: str
#     email: str
#     phone: str
#     address: str

# class DataAutoMapper:
#     def __init__(self):
#         self.r={}
#     def parse(self, data):
#         l=data.strip().split('\n')
#         for i in l:
#             i=re.sub(r'[:;=]', '|',i)
#             p=re.findall(r'(\w+)\s*\|\s*([^|]+)',i)
#             d={}
#             for k,v in p:
#                 d[k.strip()]=v.strip()
#             up=UserProfile(id=d['id'],name=d['name'],email=d['email'],phone=d['phone'],address=d['address'])
#             self.r[d['id']]=up
#         return self.r
# data = """
# id=101 | name:Ravi Kumar | email:ravi.k@example.com | phone:9876543210 | address=Bangalore
# id:102; name=Priya Sharma; email=priya.s@gmail.com; phone=9123456789; address=Chennai
# """
# ac = DataAutoMapper()
# r = ac.parse(data)
# print(r)
 
# Very Hard Question 3 — Recursive Regex Dictionary Expander

# Write a program that takes a text with nested key-value pairs and converts it into a nested dictionary,
# using regex recursively.

# Example Input:

# text = """
# person: {
#     name: John,
#     contact: {
#         email: john@example.com,
#         phone: 9876543210
#     },
#     address: {
#         city: London,
#         zip: 12001
#     }
# }
# """

# Expected Output:

# {
#   'person': {
#     'name': 'John',
#     'contact': {'email': 'john@example.com', 'phone': '9876543210'},
#     'address': {'city': 'London', 'zip': '12001'}
#   }
# }

# import re
# def parse(text):
#     t=text.strip().replace('\n','').replace(' ','')
#     r={}
#     p=re.findall(r'(\w+):\s*(\{[^{}]*\}|[^,{}]+)', t)
#     for k,v in p:
#         v=v.strip()
#         if v.startswith('{') and v.endswith('}'):
#             r[k]=parse(v[1:-1])
#         else:
#             r[k]=v
#     return r
# text = """
# person: {
#     name: John,
#     contact: {
#         email: john@example.com,
#         phone: 9876543210
#     },
#     address: {
#         city: London,
#         zip: 12001
#     }
# }
# """
# r=parse(text)
# print(r)


# Very Hard Question 4 — Class + Multi-Regex Correlation Engine

# Create a CorrelationEngine class that takes three sources of text —
# user logs, transaction logs, and error logs —
# and correlates them by user ID using regex extraction.

# Each source uses a different format, and the engine should produce a single merged dictionary:

# Example Input:

# user_logs = "UserID:101 Name:Ravi Login:2025-10-06 09:00"
# txn_logs = "TxnID:T2025-1 UID=101 Amount=$250.50 Time:2025-10-06 09:10"
# error_logs = "[2025-10-06 09:15] ERROR User 101: Connection lost"

# Expected Output:

# {
#   '101': {
#     'name': 'Ravi',
#     'login': '2025-10-06 09:00',
#     'transactions': [{'txn_id': 'T2025-1', 'amount': 250.50, 'time': '2025-10-06 09:10'}],
#     'errors': ['Connection lost']
#   }
# }

# (Tests your ability to coordinate multiple regex matches and aggregate data into one structure.)

import re
class controle:
    def __init__(self):
        self.d={}
    def log(self,log):
        m = re.search(r'UserID:(\d+)\s+Name:(\w+)\s+Login:([\d\-:\s]+)', log)
        if m:
            uid,name,login=m.groups()
            self.d[uid]={'name':name,'login':login,'transactions':[],'errors':[]}
            
    def txn(self,log):
        m=m = re.search(r'TxnID:(\w+)\s+UID=(\d+)\s+Amount:\$(\d+\.\d+)\s+Time:([\d\-:\s]+)', log)
        if m:
            txn,uid,amt,time = m.groups()
            amt=float(amt)
            if uid in self.d:
                self.d[uid]={'name':None,'login':None,'transactions':[],'errors':[]}
            self.d[uid]['transactions'].append({'txn_id':txn,'amount':amt,'time':time})
    def error(self,log):
        m = re.search(r'User\s+(\d+):\s+(.*)', log)
        if m:
            uid,msg=m.groups()
            if uid not in self.d:
                self.d[uid]={'name':None,'login':None,'transactions':[],'errors':[]}
            self.d[uid]['errors'].append(msg)
user_logs = "UserID:101 Name:Ravi Login:2025-10-06 09:00"
txn_logs = "TxnID:T2025-1 UID=101 Amount=$250.50 Time:2025-10-06 09:10"
error_logs = "[2025-10-06 09:15] ERROR User 101: Connection lost"

c=controle()
c.log(user_logs)
c.txn(txn_logs)
c.error(error_logs)
print(c.d)

