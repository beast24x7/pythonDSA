"""
Problem statement
Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the N-Binary Number Triangle.

You are required to print the pattern as shown in the examples below.

Example:
Input: ‘N’ = 3

Output: 

1
0 1
1 0 1
"""
def nBinaryTriangle(n: int) -> None:
    for i in range(0,n):
        start = 1 if i % 2 == 0 else 0
        for j in range(0,i+1):
            print(start,end=" ")
            start = 1 - start
        print(end="\n")