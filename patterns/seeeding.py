"""
Problem statement
Sam is planting trees on the upper half region (separated by the left diagonal) of the square shared field.
For every value of ‘N’, print the field if the trees are represented by ‘*’.

Example:
Input: ‘N’ = 3

Output: 
* * *
* *
*
***    1 3*
**     2 2*
*      3 1*

n-row+1

"""

def seeding(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print("*", end=" ")
        print(end="\n")

seeding(3)
"""
Problem statement
Aryan and his friends are very fond of the pattern. For a given integer ‘N’, they want to make the Reverse N-Number Triangle.

Example:
Input: ‘N’ = 3

Output: 

1 2 3
1 2
1
logic
1  3  (n-row+1)
2  2
3  1
"""

def nNumberTriangle(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j,end=' ')
        print(end="\n")