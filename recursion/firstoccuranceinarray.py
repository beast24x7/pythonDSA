"""
Search First Occurrence of a Number
"""
def firstIndex(arr, testVariable, currentIndex) :
    if len(arr) == currentIndex:
        return -1
    elif arr[currentIndex] == testVariable:
        return currentIndex
    else:
        return firstIndex(arr,testVariable,currentIndex+1)
    
