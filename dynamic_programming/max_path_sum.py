def max_path_sum(grid):
	return _max_path_sum(grid, 0, 0, {})

def _max_path_sum(grid, r, c, memo):
	pos = (r,c)
	if pos in memo:
		return memo[pos]
	if r == len(grid) or c == len(grid[0]):
		return float('-inf')
	if r == len(grid) -1 and c == len(grid[0]) -1:
		print(grid[r][c], 'start')
		return grid[r][c]
	move_down = _max_path_sum(grid, r+1, c, memo)
	move_right = _max_path_sum(grid, r, c+1, memo)
	memo[pos] = grid[r][c] + max(move_down, move_right)
	print(move_down, 'md', move_right, 'mr', memo[pos], pos)

	return memo[pos]

grid =   [
  [1, 2, 8, 1],
  [3, 10, 12, 10],
  [4, 0, 6, 3],
]
print(max_path_sum(grid)) 