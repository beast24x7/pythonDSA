"""
You are given two numbers, ‘X’ and ‘Y’. Your task is to find the greatest common divisor of the given two numbers.

The Greatest Common Divisor of any two integers is the largest number that divides both integers.

For Example:
You are given ‘X’ as 20 and ‘Y’ as 15. The greatest common divisor, which divides both 15 and 20, is 5. Hence the answer is 5.
"""
def findGcd(a, b):
    while(a > 0) and (b >0):
        if a>b:
            a = a % b
        else:
            b = b % a
    if a == 0:
         return b
    else:
         return a
    

print(findGcd(20,15))