def solve(s):
    vowels = 'aeiou'
    for letter in s:
        if letter in vowels:
            s = s.replace(letter, '*')
    consts = s.split('*')
    

    def counts(ele):
        total = 0
        max = 0
        for letter in ele:
            total += ord(letter) - 96
            if total > max:
                max = total
        return max
    
    return max(list(map(counts, consts)))
print(solve("chruschtschov"))