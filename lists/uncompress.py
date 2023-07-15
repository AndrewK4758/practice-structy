def uncompress(s):
    num_to_rpt = 0
    char_to_rpt = ' '
    res = []
    i = 0
    j = 0
    while j < len(s):
        if s[j].isnumeric() is True:
            j += 1
        else:
            num_to_rpt = int(s[i:j])
            char_to_rpt = s[j]
            j += 1
            i = j
            res.append(char_to_rpt * num_to_rpt)

    return ''.join(res)

print(uncompress("2c3a1t"))