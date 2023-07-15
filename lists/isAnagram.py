def isAnagram(s: str, t: str) -> bool:
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))
    res = True
    if len(s) != len(t):
        return False
    for i in range(len(t)):
        if s[i] != t[i]:
            res = False
    return res
print(isAnagram('rat', 'car'))