from typing import *

def reverseArray(n: int, nums: List[int],m:int=0) -> List[int]:
    if m >= n/2:
        return nums
    else:
        nums[m],nums[n] = nums[n],nums[m]
        return reverseArray(n-1,nums,m+1)

print(reverseArray(4,[1,2,3,5,4]))