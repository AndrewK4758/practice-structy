def mergeAlternately(word1: str, word2: str) -> str:
    res = ''
    end = ''
    wordLen = 0

    if len(word1) > len(word2):
        wordLen = len(word2)
        end = word1[wordLen:]

    if len(word2) > len(word1):
        wordLen = len(word1)
        end = word2[wordLen:]
        
    for i in range(wordLen):
        res+=word1[i]
        res+=word2[i]

    return res+end



print(mergeAlternately('abcdef', 'pqr'))