def isVowel(str) -> bool:
    vowel = "aeiou"
    str = str.lower()
    if str in vowel:
        return True
    else: 
        return False

def countVowelRecusrively(str,len) -> int:
    if len == 0:
        return
    elif len == 1:
        return isVowel(str[0])
    else:
        return countVowelRecusrively(str,len-1) + isVowel(str[len-1])
    

print(countVowelRecusrively("ravi",len("ravi")))