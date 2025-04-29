from typing import List
import math
def printDivisors(n: int):
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            print(i)
            if ( n / i != i):
                print(int(n/i))


printDivisors(36)


def printDivisorsOptimized(n: int) -> List[int]:
    numList = []
    for i in range(1,int(math.sqrt(n))+1):
        if ( n % i == 0):
            print(i)
            numList.append(i)
            if int(n/i) != i:
                numList.append(int(n/i))

    return sorted(numList)

print(printDivisorsOptimized(36))