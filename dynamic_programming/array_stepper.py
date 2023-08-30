def array_stepper(numbers, i=0, memo={}):
    if i in memo:
        return memo[i]
    if i >= len(numbers)-1:
        return True
        
    idx_choice = numbers[i]
    for steps in range(1, idx_choice+1):
        if array_stepper(numbers, i + steps, memo):
            memo[i] = True
            return True
    memo[i] = False
    return False
print(array_stepper([2, 4, 2, 0, 0, 1]))