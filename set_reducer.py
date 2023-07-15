import functools

def set_reducer(inp):
    res = []
    if len(inp) == 1:
        return functools.reduce(lambda x,y: x, inp)
    for i in range(len(inp)):
        if inp[i-1] != inp[i] and inp[i-2] != inp[i-1]:
            res.append(1)
        else:
            res.append(inp.count(inp[i-1]))
    for idx, num in enumerate(res):
        if res[idx] > 1:
            res.remove(res[idx])
    return set_reducer(res)
    
print(set_reducer([8, 1, 6, 1, 2, 7, 7, 7, 7, 6, 5, 3, 2, 1, 8]))