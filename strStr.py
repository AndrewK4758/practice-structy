def strStr(haystack: str, needle: str) -> int:

    try:
        return haystack.index(needle)
    except:
        return -1
    

print(strStr("sadbutsad", "sad"))