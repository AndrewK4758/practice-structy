def island_count(grid):
    visited = set()
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(grid, i, j, visited) == True:
              count+=1
    return count

def dfs(grid, i, j, visited):

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False
    if grid[i][j] == 'W':
        return False
    pos = (i,j)

    if pos in visited:
        return False
    visited.add(pos)

    dfs(grid, i-1, j, visited)
    dfs(grid, i+1, j, visited)
    dfs(grid, i, j-1, visited)
    dfs(grid, i, j+1, visited)
    return True        
    
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) 