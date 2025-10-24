# Create a class TemplateEngine that replaces placeholders in a text using a dictionary of variables.
# Placeholders are written in double curly braces {{variable_name}}.
# Use regex to identify and replace them dynamically.

# Example Input:

# text = "Hello {{name}}, your order {{order_id}} will be delivered by {{date}}."
# data = {"name": "Ravi", "order_id": "A1023", "date": "2025-10-06"}

# Expected Output:

# "Hello Ravi, your order A1023 will be delivered by 2025-10-06."

import re
class TempleteEngine:
    def render(self,text,data):
        p=re.findall(r"{{(.*?)}}",text)
        for i in p:
            if i in data:
                text=text.replace("{{"+i+"}}",data[i])
        return text
        
text = "Hello {{name}}, your order {{order_id}} will be delivered by {{date}}."
data = {"name": "Ravi", "order_id": "A1023", "date": "2025-10-06"}
a=TempleteEngine()
print(a.render(text,data))


# ou’re given multiple lines describing file details in a log.
# Each line contains a filename, extension, size (in KB), and modified date.
# Use regex to parse and store the data in a dictionary grouped by file extension.

# Example Input:

# data = """
# file1.txt size:12KB modified:2025-10-05
# report.pdf size:230KB modified:2025-09-30
# notes.txt size:8KB modified:2025-10-06
# image.png size:1024KB modified:2025-08-20
# """

# Expected Output:

# {
#   'txt': [{'name': 'file1', 'size': 12, 'modified': '2025-10-05'},
#           {'name': 'notes', 'size': 8, 'modified': '2025-10-06'}],
#   'pdf': [{'name': 'report', 'size': 230, 'modified': '2025-09-30'}],
#   'png': [{'name': 'image', 'size': 1024, 'modified': '2025-08-20'}]
# }

import re
data = """
file1.txt size:12KB modified:2025-10-05
report.pdf size:230KB modified:2025-09-30
notes.txt size:8KB modified:2025-10-06
image.png size:1024KB modified:2025-08-20
"""
p=re.findall(r"(\w+)\.(\w+)\ssize:(\d+)KB\smodified:(\d+-\d+-\d+)",data)
print(p)
d={}
for i in p:
    if i[1] not in d:
        d[i[1]]=[{"name":i[0],"size":int(i[2]),"modified":i[3]}]
    else:
        d[i[1]].append({"name":i[0],"size":int(i[2]),"modified":i[3]})
print(d)

# Write a class ConfigParser that reads configuration data formatted like:

# [Database]
# host=localhost
# port=5432
# [Server]
# debug=True
# port=8000

# Use regex to extract section headers ([Section]) and key-value pairs.
# Store the data as a nested dictionary, e.g.

# {
#   'Database': {'host': 'localhost', 'port': '5432'},
#   'Server': {'debug': 'True', 'port': '8000'}
# }

# Add a method get(section, key) that retrieves a specific configuration value.

import re


# Create two dictionaries from separate text logs using regex extraction,
# then merge them intelligently based on a shared key (user_id).
# The class DataMerger should handle conflicts by choosing the latest timestamp entry.

# Example Input:

# log1 = """
# user:101 name:Ravi time:10:00
# user:102 name:Kumar time:10:10
# """
# log2 = """
# user:101 age:30 time:10:05
# user:102 age:28 time:09:50
# """

# Expected Output:

# {
#   '101': {'name': 'Ravi', 'age': 30, 'time': '10:05'},
#   '102': {'name': 'Kumar', 'age': 28, 'time': '10:10'}
# }

import re
class DataMerger:
    def parse_log(self, log):
        p=re.findall(r"user:(\d+)\s(.*?)\stime:(\d+:\d+)",log)
        d={}
        for i in p:
            de=re.findall(r"(\w+):([\w\d]+)",i[1])
            e={"time":i[2]}
            for j in de:
                e[j[0]]=j[1]
            d[i[0]]=e
        return d
    def merge(self, log1, log2):
        d1=self.parse_log(log1)
        d2=self.parse_log(log2)
        for i in d2:
            if i in d1:
                for key,value in d2[i].items():
                    if key=="time":
                        if value>d1[i]["time"]:
                            d1[i][key]=value
                    else:
                        d1[i][key]=value
            else:
                d1[i]=d2[i]
        return d1
log1 = """
user:101 name:Ravi time:10:00
user:102 name:Kumar time:10:10
"""
log2 = """
user:101 age:30 time:10:05
user:102 age:28 time:09:50
"""
a=DataMerger()
print(a.merge(log1,log2))





# Write a class JSONSanitizer that takes a messy string containing pseudo-JSON data
# and uses regex to clean it up into a valid JSON-like dictionary.
# The input may contain extra spaces, single quotes, or trailing commas.

# Example Input:

# text = "{ 'name': 'Alice', 'age': 25, 'skills': ['Python', 'ML', ], }"

# Expected Output:

# {
#   'name': 'Alice',
#   'age': 25,
#   'skills': ['Python', 'ML']
# }

# import re
# class JSONSanitizer:
#     def clean(self,text):
#         text=text.replace("'",'"')
#         text=re.sub(r",\s*}","}",text)
#         text=re.sub(r",\s*]","]",text)
#         return text
# text = "{ 'name': 'Alice', 'age': 25, 'skills': ['Python', 'ML', ], }"
# a=JSONSanitizer()
# print(a.clean(text))
    