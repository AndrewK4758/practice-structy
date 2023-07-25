import functools

def set_reducer(inp):
    
    for i in range(len(inp)):
        inp[i] = inp.count(inp[i])
    print(inp)
    # res = []
    # if len(inp) == 1:
        # return res
    # for i in range(2, len(inp)):
        # if inp[i-1] != inp[i] and inp[i-2] != inp[i-1]:
            # res.append(1)
        # else:
            # res.append(inp.count(inp[i-1]))
    # for idx, num in enumerate(res):
        # if res[idx] > 1:
            # res.remove(res[idx])
    # return set_reducer(res)
    
print(set_reducer([0, 4, 6, 8, 8, 8, 5, 5, 7]))