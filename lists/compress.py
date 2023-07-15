def compress(s):
    s += '!'
    num_to_rpt = 0
    char_to_rpt = ''
    res = []
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            j+=1
        else:
            num_to_rpt = j - i
            char_to_rpt = s[i]
            i = j
            if num_to_rpt == 1:
                res.append(char_to_rpt)
            else:
                res.append(str(num_to_rpt))
                res.append(char_to_rpt)
        
    return ''.join(res)
            
    
print(compress('ccaaatsss'))