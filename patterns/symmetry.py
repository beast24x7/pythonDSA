def symmetry(n: int):
    spaceCounter = 0
    for i in range(1,n+1):
        for num in range(n+1,i,-1):
            print("*",end="")
        print(end=" "* spaceCounter)
        for num2 in range(n+1,i,-1):
            print("*",end="")
        print()
        spaceCounter +=2

    spaceCounter2 = spaceCounter - 2
    for j in range(1,n+1):
        for num1 in range(0,j):
            print("*",end="")
        print(end=" "*spaceCounter2)
        for num11 in range(0,j):
            print("*", end="")
        print()
        spaceCounter2 -=2

"""
Problem statement
Sam is curious about symmetric patterns, so he decided to create one.

For every value of ‘N’, return the symmetry as shown in the example.

Example:
Input: ‘N’ = 3

Output: 
*         *
* *     * *
* * * * * *
* *     * *
*         *

"""
def symmetry1(n: int):
    spacecounter = 2*n -2
    spacecounter1 = 2
    for i in range(1,n+1):
        for num in range(1,i+1):
            print("*",end="")
        print(end=" "*spacecounter)
        for num2 in range(1,i+1):
            print("*",end="")
        print()
        spacecounter -=2

    for j in range(1,n):
        for num1 in range(j,n):
            print("*",end="")
        print(end=" "*spacecounter1)
        for num1 in range(j,n):
            print("*",end="")
        print()
        spacecounter1 +=2

     