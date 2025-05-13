from typing import List
from collections import defaultdict

def getFrequencies(v: List[int]) -> List[int]: 
    frequencyDict = defaultdict(int)
    for i in v:
        frequencyDict[i] += 1
    
    maxF,minF = max(frequencyDict.values()),min(frequencyDict.values())
    maxElement = [key for key, value in frequencyDict.items() if value == maxF]
    minElement = [key for key, value in frequencyDict.items() if value == minF]


    return([min(maxElement),min(minElement)])



print(getFrequencies([1,2,3,1,1,2]))