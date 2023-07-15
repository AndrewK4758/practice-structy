def repeatedSubstringPattern(s: str) -> bool:

    for i in range(1, len(s)):
        subStr = s[0:i]
        divideBy = len(s)//len(subStr)
        if subStr * divideBy == s:
            return True

    return False

print(repeatedSubstringPattern('abab'))