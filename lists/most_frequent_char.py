def most_frequent_char(s):

    char_num = 0
    rpt_char = 0
    i = 0
    while i < len(s)-1:
        i+=1
        if s.count(s[i]) > char_num:
            char_num = s.count(s[i])
            rpt_char = s[i]
    return rpt_char


    # char_num = 0
    # rpt_char = ''
    # for char in s:
        # if s.count(char) > char_num:
            # char_num = s.count(char)
            # rpt_char = char
    # return rpt_char
print(most_frequent_char('riverbed'))