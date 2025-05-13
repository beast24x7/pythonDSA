def isPalindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    else:
        length = len(string)
        if string[0] == string[length-1]:
            return isPalindrome(string[1:length-1])
    return False


print(isPalindrome("madam"))