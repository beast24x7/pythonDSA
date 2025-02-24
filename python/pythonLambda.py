def square(num):
    return num ** 2

squared = list(map(square,[1,2,3,4,5]))

print(squared)

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

print(isPrime(9))

print(list(filter(isPrime,[1,2,3,4,5]))) ## filter returns iterator for True values

square = lambda num: num ** 2
print(square(6))

print(list(map(square,[1,2,3,4])))

even = lambda num:num % 2 == 0
print(list(filter(even,[1,2,3,4])))


print(list(map(lambda str: str[::-1],['apple','grapes'])))

"""
**Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.**

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output : 
    No. of Upper case characters : 4
    No. of Lower case Characters : 33
"""

def CaseChecker(string):
    ucounter = 0
    lcounter = 0

    for i in string.strip(" "):
        if i.isupper():
            ucounter +=1
        elif i.islower():
            lcounter +=1
        else :
            pass
    return(f"No. of Upper case characters : {ucounter}\nNo. of Lower case Characters : {lcounter}")

print(CaseChecker("Hello Mr. Rogers, how are you this fine Tuesday?"))

'''
**Write a Python function that takes a list and returns a new list with unique elements of the first list.**

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]
'''

def unq(list):
    u = []
    for i in list:
        if i not in u:
            u.append(i)
        else:
            pass
    return(u)

print(unq([1,1,1,1,2,2,3,3,3,3,4,5]))

'''
**Write a Python function to multiply all the numbers in a list.**

    Sample List : [1, 2, 3, -4]
    Expected Output : -24
'''
def mul(list):
    num = 1 
    for i in list:
        num *= i
    return num

print(mul([1, 2, 3, -4]))

#**Write a Python function that checks whether a word or phrase is palindrome or not.**

def palindrome(string):
    string = string.replace(' ','')
    return(string == string[::-1])

print(palindrome("nurses run"))

#**Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)**
import string
print(string.ascii_lowercase)

def pangram(s):
    s = set(s.lower().replace(' ',''))
    return(s == set(string.ascii_lowercase))

print(pangram("The quick brown fox jumps over the lazy dog"))
