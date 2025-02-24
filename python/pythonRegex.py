text = "my number is 456-098-987 call my!!"

print("my" in text)

import re
pattern = 'my' 

match = re.search(pattern,text) # neglects second occurance of my

print(match.span())
print(match.start())
print(match.end())


match = re.findall(pattern,text)

print(match)


for match in re.finditer("my",text):
    print(match.span())



match = re.search(r"\d\d\d-\d\d\d-\d\d\d",text)
print(match.group())

match = re.search(r"\d{3}-\d{3}-\d{3}",text)
print(match.group())
