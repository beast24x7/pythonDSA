from  typing import *
i = 0
list = []
def printNtimes(n: int) -> List[str]:
    if n <= 0:
        return []
    else:
        return ["Coding Ninjas"] + printNtimes(n -1) 
    

print(printNtimes(5))
