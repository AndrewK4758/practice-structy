def primeFactors(n):
    i = 2
    res = []
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            res.append(i)
    res.append(n)
    return res

print(primeFactors(12))        