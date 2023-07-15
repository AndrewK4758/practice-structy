def moveZeros(nums: list[int]) -> None:
    notZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[notZero], nums[i] = nums[i], nums[notZero]
            notZero+=1

    print(nums)
    

moveZeros([0,1,0,3,12])