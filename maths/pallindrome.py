"""Given an integer x, return true if x is a palindrome, and false otherwise."""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        copynum = x
        revnum = 0
        if x < 0:
            return False
        else: 
            while x > 0:
                lastDigit = x % 10
                x = x // 10
                revnum = (revnum * 10) + lastDigit
            return revnum == copynum
        
print(Solution.isPalindrome(Solution,1221))
print(Solution.isPalindrome(Solution,-1221))
        