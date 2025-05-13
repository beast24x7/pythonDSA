from collections import defaultdict
def countOccurance(s: str):
    frequencyDict = defaultdict(lambda:0)
    for char in s:
        frequencyDict[char] +=1
    return frequencyDict

str = "hello World"

dict = countOccurance(str)


print(dict['l'])
print(dict['k'])


