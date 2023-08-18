from collections import deque

def best_bridge(graph):
		# visited = set()
		cur_island = None
		for i in range(len(graph)):
			for j in range(len(graph[0])):
					islands = dfs(graph, i, j, visited=set())
					if len(islands) > 0:
						cur_island = islands
						
		island_set = set(cur_island)		
		queue = deque([])
		for pos in cur_island:
			row, col = pos
			queue.append((row, col, 0))
		while queue:
			row, col, dist = queue.popleft()
			
			if graph[row][col] == 'L' and (row, col) not in cur_island:
				return dist - 1
			
			deltas = [(1,0),(-1,0),(0,1),(0,-1)]
			
			for delta in deltas:
				d_row, d_col = delta 
				nei_row = row + d_row
				nei_col = col + d_col
				nei_pos = (nei_row, nei_col)
				row_bound = 0 <= nei_row < len(graph)
				col_bound = 0 <= nei_col < len(graph[0])
				if row_bound and col_bound and nei_pos not in island_set:
					island_set.add(graph[nei_row][nei_col])
					queue.append((nei_row, nei_col, dist + 1))
		return -1

				
def dfs(graph, row, col, visited):
	row_bound = 0 <= row < len(graph)
	col_bound = 0 <= col < len(graph[0])

	if not row_bound or not col_bound or graph[row][col] == 'W':
		return visited

	pos = (row, col)
	if pos in visited:
		return visited

	visited.add(pos)

	dfs(graph, row-1, col, visited)
	dfs(graph, row+1, col, visited)
	dfs(graph, row, col-1, visited)
	dfs(graph, row, col+1, visited)

	return visited

grid = [
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "L", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "W", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "W"],
  ["W", "W", "W", "W", "W", "W", "L", "L"],
  ["W", "W", "W", "W", "W", "W", "W", "L"],
]
print(best_bridge(grid))