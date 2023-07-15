  
def perimeter(n):
    res = [1,1]
    if n <= 0:
        return 0
    while len(res) <= n:
        next_val = res[len(res)-1] + res[len(res)-2]
        res.append(next_val)
            
    return sum(res) *4
        
        

print(perimeter(5))