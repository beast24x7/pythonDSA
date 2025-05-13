"""
Corresponding Fibonacci Number
"""
def fibonacci(testVariable):
    # Base Case
    if testVariable <= 1 :
        return testVariable
    
    # Recursive Case
    return(fibonacci(testVariable - 2) + fibonacci(testVariable - 1))

testVariable = 7
print(fibonacci(testVariable))

for i in range(1,testVariable+1):
    print(fibonacci(i))


## 0, 1, 1, 2, 3, 5, 8
from typing import List
def generateFibonacci(num: int) -> List[int]:
    if num == 0:
        return [0]
    if num == 1:
        return [0,1]
    else:
       series = generateFibonacci(num-1)
       nextFib = series[-1] + series[-2]
       series.append(nextFib)

       return series

print(generateFibonacci(6))