from typing import List
def countOccurance(arr:List[int]):
    frequencyArray = [0] * 11

    for num in arr:
        frequencyArray[num] +=1

    return frequencyArray

array = [1,2,3,4,1,2,6,7]
counts = countOccurance(array)

for i in set(array):
    print("Occurance of {} in {} is {}".format(i,array,counts[i]))


import string 

def countAlphaOccurance(s: str):
    frequencyArray = [0]*26
    s = s.lower()  # convert to lowercase to handle case insensitivity

    for char in s:
        if char.isalpha():  # only process alphabetic characters
            index = ord(char) - ord('a')
            frequencyArray[index] += 1
    return frequencyArray

str_input = "helloworld"
counts = countAlphaOccurance(str_input)

unique_chars = set(str_input.lower())  # use a different variable name than 'set'

print("Unique characters:", unique_chars)

# Print counts for each unique character only once
for char in sorted(unique_chars):
    if char.isalpha():  # only print for alphabetic characters
        print(f"Occurrence of character '{char}' in '{str_input}' is {counts[ord(char) - ord('a')]}")