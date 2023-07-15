# return masked string
def maskify(cc):
    res = ''
    for index, letter in enumerate(cc):
        if index < len(cc)-4:
            letter = '#'
            res += letter
        else:
            res+=letter
    return res
print(maskify('SF$SDfgsd2eA'))