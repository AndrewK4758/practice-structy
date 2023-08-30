import math
def summing_squares(n, memo={}):
		if n in memo:
				return memo[n]
		if n == 0:
				return 0
		num_sqrs = float('inf')
		for i in range(1, math.floor(math.sqrt(n)+1)):
				sqr_val = i**2
				nxt_val = 1 + summing_squares(n - sqr_val, memo)
				num_sqrs = min(num_sqrs, nxt_val)
		memo[n] = num_sqrs
		return memo[n]
print(summing_squares(8))