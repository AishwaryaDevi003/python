# Design a base class BaseLogParser that defines a method parse_line(line) (to be overridden).
# Create subclasses ErrorLogParser, InfoLogParser, and DebugLogParser — each uses a different regex to extract data.
# Finally, write a LogRouter class that routes each log line to the correct subclass based on the log level and returns a combined dictionary of parsed data.

# Example Input:
# logs = [
#     "[2025-10-06 09:10] ERROR Disk full at /var/log",
#     "[2025-10-06 09:12] INFO Backup started",
#     "[2025-10-06 09:14] DEBUG Checking permissions"
# ]
# Expected Output:
# {
#   'ERROR': [{'timestamp': '2025-10-06 09:10', 'msg': 'Disk full at /var/log'}],
#   'INFO': [{'timestamp': '2025-10-06 09:12', 'msg': 'Backup started'}],
#   'DEBUG': [{'timestamp': '2025-10-06 09:14', 'msg': 'Checking permissions'}]
# }

# import re
# class BaseLogParser:
#     def parse_line(self, a):
#         pass
# class ErrorLogParser(BaseLogParser):
#     def parse_line(self,a):
#         p=re.findall(r"\[(\d+-\d+-\d+\s\d+:\d+)\]\sERROR\s(.*)",a)
#         d=[]
#         for i in p:
#             d.append({'timestamp':i[0],'msg':i[1]})
#         return d
# class InfoLogParser(BaseLogParser):
#     def parse_line(self,a):
#         p=re.findall(r"\[(\d+-\d+-\d+\s\d+:\d+)\]\sINFO\s(.*)",a)
#         d=[]
#         for i in p:
#             d.append({'timestamp':i[0],'msg':i[1]})
#         return d
# class DebugLogParser(BaseLogParser):
#     def parse_line(self,a):
#         p=re.findall(r"\[(\d+-\d+-\d+\s\d+:\d+)\]\sDEBUG\s(.*)",a)
#         d=[]
#         for i in p:
#             d.append({'timestamp':i[0],'msg':i[1]})
#         return d
# class LogRouter:
#     def __init__(self,logs):
#         self.logs=logs
#     def route_logs(self):
#         d={'ERROR':[],'INFO':[],'DEBUG':[]}
#         for i in self.logs:
#             if 'ERROR' in i:
#                 pa=ErrorLogParser()
#                 d['ERROR'].extend(pa.parse_line(i))
#             elif 'INFO' in i:
#                 pa=InfoLogParser()
#                 d['INFO'].extend(pa.parse_line(i))
#             elif 'DEBUG' in i:
#                 pa=DebugLogParser()
#                 d['DEBUG'].extend(pa.parse_line(i))
#         return d
# logs = [
#     "[2025-10-06 09:10] ERROR Disk full at /var/log",
#     "[2025-10-06 09:12] INFO Backup started",
#     "[2025-10-06 09:14] DEBUG Checking permissions"
# ]
# a=LogRouter(logs)
# print(a.route_logs())

# Create a class TransactionAnalyzer that reads a multiline string of transactions with varying formats (use regex to normalize).
# Then aggregate them by user_id in a dictionary.

# Example Input:

# data = """
# user-101: paid $45.60 on 2025/10/06
# user=102 amount 120.00 date=2025-10-05
# user:103 paid 60.5 on 2025-10-04
# user=101 paid $10.40 on 2025-10-06
# """

# Expected Output:

# {
#   '101': {'total': 56.00, 'transactions': 2},
#   '102': {'total': 120.00, 'transactions': 1},
#   '103': {'total': 60.50, 'transactions': 1}
# }

# import re
# class TransactionAnalyzer:
#     def parse_trans(self,data):
#         p=re.findall(r"user[-=:](\d+).*?([\d.]+).*?(\d+[-/]\d+[-/]\d+)",data)
#         d={}
#         for i in p:
#             uid=i[0]
#             a=float(i[1])
#             if uid not in d:
#                 d[uid]={'total':a,'transactions':1}
#             else:
#                 d[uid]['total']+=a
#                 d[uid]['transactions']+=1
#         return d
# data = """
# user-101: paid $45.60 on 2025/10/06
# user=102 amount 120.00 date=2025-10-05
# user:103 paid 60.5 on 2025-10-04
# user=101 paid $10.40 on 2025-10-06
# """
# a=TransactionAnalyzer()
# print(a.parse_trans(data))

# Build a class hierarchy for input validation using regex:

# BaseValidator → defines an abstract method validate(value)

# EmailValidator, PhoneValidator, and PasswordValidator → each implements regex-based validation
# Then write a class UserInputChecker that takes a dictionary of inputs and validates each using the correct subclass.


# Example Input:

# inputs = {
#   "email": "user@example.com",
#   "phone": "+919876543210",
#   "password": "Pass@123"
# }

# Expected Output:

# {
#   'email': True,
#   'phone': True,
#   'password': True
# }

# import re
# class Validator:
#     def validate(self, v):
#         pass
# class Email(Validator):
#     def validate(self,v):
#         p=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",v)
#         return bool(p)
# class Phone(Validator):
#     def validate(self,v):
#         p=re.findall(r"\+?91\d{10}",v)
#         return bool(p)
# class Password(Validator):
#     def validate(self,v):
#         p=re.findall(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+",v)
#         return bool(p)
# class UserInputChecker:
#     def __init__(self,ipt):
#         self.ipt=ipt
#     def check(self):
#         d={}
#         for i in self.ipt:
#             if i=="email":
#                 va=Email()
#                 d[i]=va.validate(self.ipt[i])
#             elif i=="phone":
#                 va=Phone()
#                 d[i]=va.validate(self.ipt[i])
#             elif i=="password":
#                 va=Password()
#                 d[i]=va.validate(self.ipt[i])
#         return d
# inputs = {
#   "email": "user@example.com",
#   "phone": "+919876543210",
#   "password": "Pass@123"
# }
# a=UserInputChecker(inputs)
# print(a.check())




# Given a text describing module dependencies,
# use regex to extract relationships and build a dependency graph dictionary
# where keys are modules and values are lists of dependencies.

# Example Input:

# text = """
# ModuleA depends on ModuleB, ModuleC
# ModuleB depends on ModuleD
# ModuleC depends on ModuleE, ModuleF
# ModuleD depends on None
# ModuleE depends on None
# ModuleF depends on None
# """

# Expected Output:

# {
#   'ModuleA': ['ModuleB', 'ModuleC'],
#   'ModuleB': ['ModuleD'],
#   'ModuleC': ['ModuleE', 'ModuleF'],
#   'ModuleD': [],
#   'ModuleE': [],
#   'ModuleF': []
# }


# import re
# class graph:
#     def parse(self,text):
#         p=re.findall(r"(\w+)\sdepends\son\s(.*)",text)
#         d={}
#         for i in p:
#             if i[0] not in d:
#                 d[i[0]]=[]
#             if i[1]!="None":
#                 for j in i[1].split(","):
#                     d[i[0]].append(j)
#         return d
# text = """
# ModuleA depends on ModuleB, ModuleC
# ModuleB depends on ModuleD
# ModuleC depends on ModuleE, ModuleF
# ModuleD depends on None
# ModuleE depends on None
# ModuleF depends on None
# """
# a=graph()
# print(a.parse(text))

# Create a class ReportBuilder that uses composition with another class RegexExtractor.
# RegexExtractor extracts dates, amounts, and IDs from text using regex.
# ReportBuilder organizes the extracted info into a summary dictionary and generates a formatted string report.

# Example Input:

# data = """
# Transaction ID: TXN101 | Date: 2025-10-06 | Amount: $450.75
# Transaction ID: TXN102 | Date: 2025-10-07 | Amount: $320.00
# Transaction ID: TXN103 | Date: 2025-10-07 | Amount: $100.50
# """

# Expected Output:

# {
#   '2025-10-06': [{'id': 'TXN101', 'amount': 450.75}],
#   '2025-10-07': [
#       {'id': 'TXN102', 'amount': 320.00},
#       {'id': 'TXN103', 'amount': 100.50}
#   ]
# }

# and a report like:

# Date: 2025-10-06 → Total: 450.75
# Date: 2025-10-07 → Total: 420.50

import re
class RegexExtractor:
    def extract(self, data):
        p=re.findall(r"Transaction ID:\s(\w+)\s\|\sDate:\s(\d+-\d+-\d+)\s\|\sAmount:\s\$(\S+)",data)
        d={}
        for i in p:
            tid=i[0]
            date=i[1]
            a=float(i[2])
            if date not in d:
                d[date] = [{'id': tid, 'amount': a}]
            else:
                d[date].append({'id': tid, 'amount': a})
        return d
class ReportBuilder:
    def __init__ (self, data):
        self.data=data
        self.extractor=RegexExtractor()
    def summary(self):
        return self.extractor.extract(self.data)
    def report(self):
        s=self.summary()
        r=[]
        for date in s:
            items=s[date]
            t=0
            for i in items:
                t+=i['amount']
            r.append(f"Date: {date} -> Total: {t:.2f}")
        return "\n".join(r)
data = """
Transaction ID: TXN101 | Date: 2025-10-06 | Amount: $450.75
Transaction ID: TXN102 | Date: 2025-10-07 | Amount: $320.00
Transaction ID: TXN103 | Date: 2025-10-07 | Amount: $100.50
"""
a=ReportBuilder(data)
print(a.summary())
print(a.report())