def pair_product(numbers, target_product):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] * numbers[j] == target_product and i != j:
                return (i,j)

print(pair_product([4, 7, 9, 2, 5, 1], 5))