# Medium (Level 1) — Regex + Dictionary Formatter

# Write a program that extracts name, age, and city from a messy multiline text and stores it in a list of dictionaries.

# Example Input:

# data = """
# Name: John, Age=25; City->London
# Name=Alice; Age:30 City:NewYork
# City:Paris Name=Mike Age=22
# """

# Expected Output:

# [
#   {'name': 'John', 'age': 25, 'city': 'London'},
#   {'name': 'Alice', 'age': 30, 'city': 'NewYork'},
#   {'name': 'Mike', 'age': 22, 'city': 'Paris'}
# ]


# ---
import re

data = """
Name: John, Age=25; City->London
Name=Alice; Age:30 City:NewYork
City:Paris Name=Mike Age=22
"""

result = []

lines = data.strip().split('\n')
for line in lines:
    name = re.findall(r'Name[:=]\s*(\w+)', line)
    age = re.findall(r'Age[:=]\s*(\d+)', line)
    city = re.findall(r'City[:=>\s]*([\w]+)', line)

    info = {}
    if name:
        info['name'] = name[0]
    else:
        info['name'] = ''

    if age:
        info['age'] = int(age[0])
    else:
        info['age'] = 0

    if city:
        info['city'] = city[0]
    else:
        info['city'] = ''

    result.append(info)

print(result)

# Hard (Level 2) — Class + Regex-Based Resume Parser

# Create a class ResumeParser that takes raw resume text and extracts:

# Name

# Email

# Phone number

# Skills list (comma-separated)


# Store each resume as a dictionary entry using the person’s name as the key.

# Example Input:

# data = """
# Name: Ravi Kumar
# Email: ravi.k@example.com
# Phone: +919876543210
# Skills: Python, Automation, Networking

# Name: Priya Sharma
# Email: priya.s@gmail.com
# Phone: 9123456789
# Skills: Data Analysis, SQL, Tableau
# """

# Expected Output:

# {
#   'Ravi Kumar': {
#       'email': 'ravi.k@example.com',
#       'phone': '+919876543210',
#       'skills': ['Python', 'Automation', 'Networking']
#   },
#   'Priya Sharma': {
#       'email': 'priya.s@gmail.com',
#       'phone': '9123456789',
#       'skills': ['Data Analysis', 'SQL', 'Tableau']
#   }
# }
import re

class ResumeParser:
    def __init__(self, text):
        self.text = text

    def parse(self):
        d = {}
        p=re.findall(r"Name:\s*(.*?)\s*Email:\s*(.*?)\s*Phone:\s*(.*?)\s*Skills:\s*(.*?)(?=Name:|$)", self.text, re.DOTALL)
        for i in p:
            skills_list = [skill.strip() for skill in i[3].split(',')]
            d[i[0].strip()] = {
                'email': i[1].strip(),
                'phone': i[2].strip(),
                'skills': skills_list
            }
        return d


data = """
Name: Ravi Kumar
Email: ravi.k@example.com
Phone: +919876543210
Skills: Python, Automation, Networking

Name: Priya Sharma
Email: priya.s@gmail.com
Phone: 9123456789
Skills: Data Analysis, SQL, Tableau
"""

a = ResumeParser(data)
print(a.parse())

# Very Hard (Level 3) — Inheritance + Regex + Dataclass Log Correlator

# Build a log correlation system using OOP and regex.

# Base class BaseLog defines structure using @dataclass with timestamp, level, and message.

# Subclasses SystemLog, AppLog, and SecurityLog each parse a different log format using regex.

# A LogCorrelator class merges parsed logs by timestamp into a dictionary timeline.


# Example Input:

# system_log = """
# [2025-10-06 09:10] SYSTEM: Boot completed
# [2025-10-06 09:12] SYSTEM: Network up
# """

# app_log = """
# 2025/10/06 09:10 - APP - Started main service
# 2025/10/06 09:13 - APP - Request received
# """

# security_log = """
# (2025-10-06 09:12) SECURITY ALERT: User login successful
# (2025-10-06 09:15) SECURITY ALERT: Unauthorized access attempt
# """

# Expected Output:

# {
#   '2025-10-06 09:10': [
#       {'source': 'SYSTEM', 'msg': 'Boot completed'},
#       {'source': 'APP', 'msg': 'Started main service'}
#   ],
#   '2025-10-06 09:12': [
#       {'source': 'SYSTEM', 'msg': 'Network up'},
#       {'source': 'SECURITY', 'msg': 'User login successful'}
#   ],
#   '2025-10-06 09:13': [{'source': 'APP', 'msg': 'Request received'}],
#   '2025-10-06 09:15': [{'source': 'SECURITY', 'msg': 'Unauthorized access attempt'}]
# }



import re
def parse(log):
    p=re.findall(r"(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\]\sSYSTEM:\s(.*)",log)
    d={}
    for i in p:
        if i[0] not in d:
            d[i[0]]=[{'source':'SYSTEM','msg':i[1]}]
        else:
            d[i[0]].append({'source':'SYSTEM','msg':i[1]})
    return d

def parse1(log):
    p=re.findall(r"(\d{4}/\d{2}/\d{2}\s\d{2}:\d{2})\s-\sAPP\s-\s(.*)",log)
    d={}
    for i in p:
        timestamp=i[0].replace('/','-')
        if timestamp not in d:
            d[timestamp]=[{'source':'APP','msg':i[1]}]
        else:
            d[timestamp].append({'source':'APP','msg':i[1]})
    return d

def parse2(log):    
    p=re.findall(r"\((\d{4}-\d{2}-\d{2}\s\d{2}:\d{2})\)\sSECURITY ALERT:\s(.*)",log)
    d={}
    for i in p:
        if i[0] not in d:
            d[i[0]]=[{'source':'SECURITY','msg':i[1]}]
        else:
            d[i[0]].append({'source':'SECURITY','msg':i[1]})
    return d
system_log = """
[2025-10-06 09:10] SYSTEM: Boot completed
[2025-10-06 09:12] SYSTEM: Network up
"""

app_log = """
2025/10/06 09:10 - APP - Started main service
2025/10/06 09:13 - APP - Request received
"""

security_log = """
(2025-10-06 09:12) SECURITY ALERT: User login successful
(2025-10-06 09:15) SECURITY ALERT: Unauthorized access attempt
"""
d1=parse(system_log)
d2=parse1(app_log)
d3=parse2(security_log)
for i in d2:
    if i in d1:
        d1[i].extend(d2[i])
    else:
        d1[i]=d2[i]
for i in d3:
    if i in d1:
        d1[i].extend(d3[i])
    else:
        d1[i]=d3[i]
print(d1)

# Very Hard (Level 4) — Dynamic Regex Class Compiler

# Write a class PatternCompiler that:

# 1. Accepts a dictionary of pattern names → regex expressions.


# 2. Dynamically creates methods at runtime for each pattern name.


# 3. Each generated method should return all matches from a given text.



# Example Input:

# patterns = {
#   "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
#   "phones": r"\+?\d{10,12}",
#   "dates": r"\d{4}-\d{2}-\d{2}"
# }
# compiler = PatternCompiler(patterns)
# text = "Contact us at admin@mail.com or +919812345678 by 2025-10-06."

# Expected Output (when calling methods):

# compiler.emails(text) → ['admin@mail.com']
# compiler.phones(text) → ['+919812345678']
# compiler.dates(text) → ['2025-10-06']


# ---

import re
class PatternCompiler:
    def __init__(self, patterns):
        self.patterns = patterns
        for name, pattern in patterns.items():
            setattr(self, name, self.create_method(pattern))

    def create_method(self, pattern):
        def method(text):
            return re.findall(pattern, text)
        return method
patterns = {
  "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
  "phones": r"\+?\d{10,12}",
  "dates": r"\d{4}-\d{2}-\d{2}"
}
compiler = PatternCompiler(patterns)
text = "Contact us at admin@mail.com or +919812345678 by 2025-10-06."
print(compiler.emails(text)) 
print(compiler.phones(text)) 
print(compiler.dates(text))
