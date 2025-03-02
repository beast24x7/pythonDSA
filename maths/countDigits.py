"""
Problem statement
You are given a number ’n’.
Find the number of digits of ‘n’ that evenly divide ‘n’.
Note:
A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.

Example:
Input: ‘n’ = 336

Output: 3

Explanation:
336 is divisible by both ‘3’ and ‘6’. Since ‘3’ occurs twice it is counted two times.
Note:
You don’t need to print anything. Just implement the given function.
"""

def countDigits(n: int) -> int:
    num = n
    counter = 0
    while n > 0:
        units = n % 10
        if units == 0:
            pass
        elif num % units == 0:
            counter +=1
    
        n = n // 10
    return counter

def countDigits1(n: int) -> int:
    counter = 0
    for i in str(n):
        if i != '0' and n % int(i) == 0:
            counter +=1 
    return counter

import math
def count(n: int) -> int:
    return int(math.log10(n) + 1)


print(count(5564))

print(len(str(-123)))