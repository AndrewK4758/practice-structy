import pprint as pr
def counting_change(amount, coins, i=0, memo={}):
    keys = (amount, i)
    if keys in memo:
        return memo[keys]
    if amount == 0:
        return 1
    if i == len(coins):
        return 0
    
    coin = coins[i]
    possible_combos = 0
    for coin_count in range(0, (amount//coin)+1):
        next = amount - (coin * coin_count)
        possible_combos += counting_change(next, coins, i+1, memo)
    memo[keys] = possible_combos
    pr.pprint(memo)
    return memo[keys]

print(counting_change(24, [5, 7, 3]))