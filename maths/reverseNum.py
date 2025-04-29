"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
 the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverse(self, x: int) -> int:
        revNum = 0
        signCheck = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            lastDigit = x % 10
            x = x // 10
            if revNum > (2**31 - 1) // 10 or (revNum == (2**31 - 1) // 10 and lastDigit > 7):
                return 0
            else :
                revNum = (revNum * 10) + lastDigit
        return signCheck * revNum
        

print(Solution.reverse(Solution,1010))