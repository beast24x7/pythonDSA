"""
Problem statement
Aryan and his friends are very fond of the pattern. They want to make the Reverse N-Number Crown for a given integer' N'.

Given 'N', print the corresponding pattern.

Example:
Input: ‘N’ = 3

Output: 

1         1
1 2     2 1
1 2 3 3 2 1
"""

def numberCrown(num: int) -> None:
    for i in range(1,num+1):

        for num0 in range(1,i+1):
            print(num0,end=" ")
        s = 2*(num-i)
        print(" "*s,end="")
        for num1 in range(i,0,-1):
            print(num1,end=" ")
        print()
