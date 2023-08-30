def non_adjacent_sum(nums, i=0, memo={}):
    
    if i in memo:
        return memo[i]
    
    if i >= len(nums):
        return 0
            
    with_first = nums[i] + non_adjacent_sum(nums, i+2, memo)
    without_first = non_adjacent_sum(nums, i+1, memo)
    memo[i] = max(with_first, without_first)
    print(memo[i])
    return memo[i]
nums = [
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
  61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  42
]

print(non_adjacent_sum(nums))