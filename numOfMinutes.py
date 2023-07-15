def numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
    total = 0
    minusVal = manager[headID]
    for i in range(n):
        if manager[i] > 0 and informTime[i] > 0:
            total += informTime[i]
    return total

print(numOfMinutes(15, 0, [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]))