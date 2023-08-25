import pprint

def tribonacci(n, memo={}):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n not in memo:
    	memo[n] = tribonacci(n-3, memo) + tribonacci(n-2, memo) + tribonacci(n-1, memo)
    pprint.pprint(memo)
    return memo[n]

print(tribonacci(373))