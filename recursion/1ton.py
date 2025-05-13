
from typing import List
def printNos(x: int,arr: List = None) -> List[int]:
    if arr is None:
        arr = []
    if x > 0: 
        printNos(x-1,arr)
        arr.append(x)
    return arr
        
    
print(printNos(9))


"""
N to 1 
"""

def printNto1(x: int) -> List[int]:
    if x == 0:
        return []
    else:
        return [x] + printNto1(x-1)
    
print(printNto1(5))


"""
SUM OF 1toN
"""
def printSum1toN(x: int) -> int:
    if x == 0:
        return 0
    else:
        return x + printSum1toN(x-1)
    
print(printSum1toN(10))


"""
1 To N
"""
def printBacktracking(x: int):
    if x < 1:
        return 
    else:
        printBacktracking(x-1)
        print(x)

printBacktracking(5)