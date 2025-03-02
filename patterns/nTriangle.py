"""
Problem statement
Sam is making a Triangular painting for a maths project.

An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers starting from 1.

For every value of ‘N’, help sam to print the corresponding N-dimensional Triangle.

Example:
Input: ‘N’ = 3

Output: 
1
1 2 
1 2 3
"""

def nTriangle(n:int) ->None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print(end="\n")

nTriangle(5)

"""
Problem statement
Sam is making a Triangular painting for a maths project.

An N-dimensional Triangle is represented by the lower triangle of the pattern filled with integers representing the row number.

For every value of ‘N’, help sam to print the corresponding Triangle.

Example:
Input: ‘N’ = 3

Output: 
1
2 2 
3 3 3
"""
def triangle( n:int) ->None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print(end="\n")

triangle(5)
