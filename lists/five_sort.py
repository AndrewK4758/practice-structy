def five_sort(nums):
    i = 0
    j = len(nums)-1
    while i < j:
        if nums[j] == 5:
            j-=1
        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+=1
    return nums
print(five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5]))