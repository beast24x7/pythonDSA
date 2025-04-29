"""
You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself.
371 is an Armstrong number since 33 + 73 + 13 = 371. 
"""

class Solution:
    def armstrongNumber (self, n):
        n1 = n
        sum = 0
        while n1 > 0:
            unitDigit = n1 % 10
            sum = sum + unitDigit ** 3
            n1 = n1 // 10
        
        if sum == n:
            return True
        else:
            return False


print(Solution.armstrongNumber(Solution,31))