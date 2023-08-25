import pprint as pr

def fib(n, memo={}):
    if n == 0:
      return 0
    if n == 1 or n == 2:
      return 1
    if n not in memo:
      memo[n] = fib(n-2, memo) + fib(n-1, memo)
    pr.pprint(memo)
    return memo[n]

print(fib(35))