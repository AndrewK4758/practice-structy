from collections import deque
def closest_carrot(grid, starting_row, starting_col):
    
    visited = set([(starting_row,starting_col)])
    queue = deque([(starting_row, starting_col, 0)])
    
    while queue:
        
        row, col, dist = queue.popleft()

        if grid[row][col] == 'C':
            return dist
        
        deltas = [(1,0),(-1,0),(0,1),(0,-1)]

        for delta in deltas:
            d_row, d_col = delta
            nxt_row = row + d_row
            nxt_col = col + d_col
            pos = (nxt_row, nxt_col)
            row_bound = 0 <= nxt_row < len(grid)
            col_bound = 0 <= nxt_col < len(grid[0])
            if row_bound and col_bound and pos not in visited and grid[nxt_row][nxt_col] != 'X':
                visited.add(pos)
                queue.append((nxt_row, nxt_col, dist + 1))
    return -1
    

grid = [
  ['O', 'O', 'O', 'O', 'O'],
  ['O', 'X', 'O', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['O', 'X', 'C', 'O', 'O'],
  ['O', 'X', 'X', 'O', 'O'],
  ['C', 'O', 'O', 'O', 'O'],
]

print(closest_carrot(grid, 1, 2)) # -> 4