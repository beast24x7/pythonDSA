from collections import Counter

list = [1,2,3,4,1,2,3,1,2]

print(Counter(list))
print(Counter('ababababadbcdbc'))

sentence = "How many times is enough times is enough"

sentenceList = sentence.split(" ")
print(Counter(sentenceList))



print(Counter(sentenceList).most_common(2))

from collections import defaultdict

d = defaultdict(lambda: 0)
print(d)
d['a'] = 1
d['b'] = 2

print(d['c'])

