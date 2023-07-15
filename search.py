def search(nums: list[int], target: int) -> int:
    end = len(nums)-1
    start = 0
    while nums[middle] != target:
        middle = (start + end)//2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle
    
    return -1

print(search([-1,0,3,5,9,12], 9))