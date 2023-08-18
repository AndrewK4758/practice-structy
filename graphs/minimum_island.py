def minimum_island(grid):
    visited = set()
    min_size = float('inf')
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            size = dfs(grid, i, j, visited)
            if size > 0 and size < min_size:
                min_size = size
    return min_size

def dfs(grid, i, j, visited):
    row_bound = 0 <= i < len(grid)
    col_bound = 0 <= j < len(grid[0])

    if not row_bound or not col_bound:
        return 0
    if grid[i][j] == 'W':
        return 0
    pos = (i,j)
    if pos in visited:
        return 0
    visited.add(pos)
    
    size = 1
    size += dfs(grid, i-1, j, visited)
    size += dfs(grid, i+1, j, visited)
    size += dfs(grid, i, j-1, visited)
    size += dfs(grid, i, j+1, visited)
    return size
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2