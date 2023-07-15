def intersection(a, b):
    res = []
    if a == b:
        return a
    for i in range(len(a)):
        for j in range(len(b)):
           if a[i] == b[j]:
               res.append(a[i])
    return res
    

print(intersection([ i for i in range(0, 50000) ], [ i for i in range(0, 50000) ]))