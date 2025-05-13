"""
Sum of Integers from 1 to n
"""

def sumTill(targetNumber) :
    if targetNumber == 1:
        return 1
    else:
        return targetNumber + sumTill(targetNumber-1)
    
print(sumTill(5))