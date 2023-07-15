def findTheDifference(s: str, t: str) -> str:

    s = ''.join(sorted(s))
    t = ''.join(sorted(t))    
    if len(s) == 0:
        return t

    for i in range(len(s)):
        if s[i] is not t[i]:
            return t[i]
    return t[len(t)-1]
print(findTheDifference('abcd', 'abcde'))