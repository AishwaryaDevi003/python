# Write a Python program to count the frequency of each word in a given sentence using a dictionary.
# Example Input:
# "apple banana apple orange banana apple"
# Expected Output:
# {'apple': 3, 'banana': 2, 'orange': 1}

# s=input("Enter a string: ")
# words=s.split()
# print(words)
# d={}
# for word in words:
#     if word in d:
#         d[word]+=1
#     else:
#         d[word]=1
# print(d)

# Write a Python program that extracts all valid email addresses from a string using a regular expression, and then store them as keys in a dictionary.
# The value for each key should be the domain name (part after @).
# Example Input:
# text = "Contact us at support@example.com or sales@company.org for more info."
# Expected Output:
# {'support@example.com': 'example.com', 'sales@company.org': 'company.org'}

import re
t=input("Enter a string: ")
p=re.findall(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+",t)
d={}
for i in p:
    email=i.split('@')
    d[i]=email[1]
print(d)

# Given a text, find all words that start with a capital letter (like proper nouns) using regex,
# and create a dictionary where keys are the capitalized words and values are their count of occurrences.
# Ignore punctuation and case sensitivity.
# Example Input:
# text = "Alice met Bob. Alice and Bob went to Paris. Bob liked Paris."
# Expected Output:
# {'Alice': 2, 'Bob': 3, 'Paris': 2}

# import re
# s=input("Enter a string: ")
# p=re.findall(r"[A-Z][a-zA-Z]+",s)
# d={}
# for i in p:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)