def min_change(amount, coins):
    res = _min_change(amount, coins, memo={})
    if res == float('inf'):
        return -1
    else:
        return res

def _min_change(amount, coins, memo):
    if amount in memo:
       return memo[amount]
    if amount == 0:
       return 0
    if amount < 0:
       return float('inf')
    
    min_coins = float('inf')
    for coin in coins:
      num_coins = _min_change(amount - coin, coins, memo) + 1 # sets a variable named num_coins to keep track of the "count" of the number of function calls + 1
      min_coins = min(min_coins, num_coins)
    
    memo[amount] = min_coins
    return min_coins

print(min_change(13, [1, 9, 5, 14, 30]))