def cubes(numRange):
    list = []
    for i in range(numRange):
        list.append(i**3)
    return list

print(cubes(10))

def generateCubes(numList):
    for i in range(numList):
        yield i**3

print(generateCubes(5))

l1 = list(generateCubes(10))
print(l1)


def fib(numRange):
    a = 1
    b = 1 
    list = []
    for i in range(numRange):
        list.append(a)
        a,b = b,a+b
    return list


print(fib(5))

def fibGenerator(numRange):
    a = 1
    b = 1
    for i in range(numRange):
        yield a
        a,b = b, a+b
print(list(fibGenerator(5)))


### Problem 2
'''
Create a generator that yields "n" random numbers between 
a low and high number (that are inputs).<br>Note: Use the random library. For example: '''

import random

def generateRandom(n,high,low):
    for i in range(n):
        yield random.randint(low,high) 


print(list(generateRandom(5,10,1)))


stringIterator = iter("MyString")
print(next(stringIterator))
print(list(stringIterator))