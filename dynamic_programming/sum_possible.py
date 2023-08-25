# to find the sum of any number in numbers == amount. Numbers can be used as many times as necessary
# this is a recursive solution with memoization

def sum_possible(amount, numbers, memo={}):
    if amount in memo:
       return memo[amount] # check to see if the amount is logged in the memo and if so, return the T/F value
    if amount < 0:
       return False # base case 1
    if amount == 0:
        return True # base case 2
    for num in numbers: # loop to test all nums in numbers
      new_num = amount - num
      if sum_possible(new_num, numbers, memo): # if the call to the new number == True, assign the value to True of the key amount and return true for the function call
        memo[amount] = True
        return True
    memo[amount] = False
    return False 
    # if the num in nums and memo all return False, record False in the value of the memo for the key amount and return False for the function call
print(sum_possible(271, [10, 8, 265, 24]))