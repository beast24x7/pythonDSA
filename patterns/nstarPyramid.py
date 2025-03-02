"""
Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 

  *
 ***
*****
"""


def nStarTriangle(n: int) -> None:
    for i in range(0,n):
        for sp1 in range(0,n-i-1):
            print(end=" ")
        for star in range(0,2*i+1):
            print("*",end="")
        for sp2 in range(0,n-i-1):
            print(end=" ")
        print(end="\n")
        
"""Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 

*****
 ***
  *

"""

def nStarTriangleRev(n: int) -> None:
    for i in range(0,n):
        for sp1 in range(0,i):
            print(end=" ")
        for star in range(0,2*n-(2*i+1)):
            print("*",end="")
        for sp1 in range(0,i):
            print(end=" ")
        print(end="\n")
        

"""
Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Diamond.

Example:
Input: ‘N’ = 3

Output: 

  *
 ***
*****
*****
 ***
  *
"""
nStarTriangle(3)
nStarTriangleRev(3)
