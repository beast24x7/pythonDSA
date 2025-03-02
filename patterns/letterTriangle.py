"""
Problem statement
Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Increasing Letter Triangle.

Example:
Input: ‘N’ = 3

Output: 

A
A B
A B C
"""
def nLetterTriangle(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(j+64),end=" ")
        print()

"""
Problem statement
Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Reverse Letter Triangle.

You must print a matrix corresponding to the given Reverse Letter Triangle.

Example:
Input: ‘N’ = 3

Output: 

A B C
A B
A
"""

def nLetterTriangle(n: int):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(chr(j+64),end=" ")
        print()


"""

Problem statement
Sam is curious about Alpha-Ramp, so he decided to create Alpha-Ramp of different sizes.

An Alpha-Ramp is represented by a triangle, where alphabets are filled from the top in order.

For every value of ‘N’, help sam to return the corresponding Alpha-Ramp.

Example:
Input: ‘N’ = 3

Output: 
A
B B
C C C
"""
def alphaRamp(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(i+64),end=" ")
        print()

"""
Problem statement
Sam is curious about Alpha-Hills, so he decided to create Alpha-Hills of different sizes.

An Alpha-hill is represented by a triangle, where alphabets are filled in palindromic order.

For every value of ‘N’, help sam to return the corresponding Alpha-Hill.

Example:
Input: ‘N’ = 3

Output: 
    A
  A B A
A B C B A

"""
def alphaHill(n: int):
    for i in range(1,n+1):
        for space in range(i,n):
            print(end=" ")
        for num in range(1,i+1):
            print(chr(num+64),end=" ")
        for num1 in range(i-1,0,-1):
            print(chr(num1+64),end=" ")
        print()


n = 3

for i in range(n,0,-1):
    for j in range(i,n+1):
        print(chr(j+64),end=" ")
    print()


for i in range(1,n+1):
    for j in range(n,n-i,-1):
        print(chr(j+64),end="")
    print()

