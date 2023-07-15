def plusOne(digits):
    strDig = list(map(str, digits))
    strDig = ''.join(strDig)
    add1 = str(int(strDig)+1)
    return list(map(int, [*add1]))

print(plusOne([1,2,3]))