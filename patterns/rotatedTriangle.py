"""
Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Rotated Triangle.

Example:
Input: ‘N’ = 3

Output: 

*
**
***
**
*
"""
def nStarTriangle(n: int) -> None:
    for i in range(1,n+1):
        print("*"*i,end="\n")
    for j in range(n-1,0,-1):
        print("*"*j,end="\n")


nStarTriangle(4)