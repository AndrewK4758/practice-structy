def pair_sum(numbers, target_sum):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target_sum and i != j:
                return (i,j)

print(pair_sum([9, 9], 18))