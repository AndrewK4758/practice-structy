from collections import deque

def knight_attack(n, kr, kc, pr, pc):
		# visited set tracks which positions we already searched
		visited = set([(kr, kc)])
		# queue for bfs data structure
		queue = deque([(kr, kc, 0)])
		# deltas are the possible changes in position for any given space
		
		while queue:
				row, col, move_count = queue.popleft()
				if (row, col) == (pr, pc):
						return move_count
				
				next_possible_moves = new_knight_positions(n, row, col)
				for next_pos in next_possible_moves:
						next_row, next_col = next_pos
						if next_pos not in visited:
							visited.add(next_pos)
							queue.append((next_row, next_col, move_count + 1))
						
# find all legal moves for any given position
def new_knight_positions(n, kr, kc):
		deltas = [(2,1), (2,-1), (1,2), (1,-2), (-2,1), (-2,-1), (-1,2), (-1,-2)]
		legal_moves = []
		for a, b in deltas: 
				row_pos = kr + a
				col_pos = kc + b
				if 0 <= row_pos < n and 0 <= col_pos < n:
						legal_moves.append((row_pos, col_pos))
		
		return legal_moves
				
print(knight_attack(24, 4, 7, 19, 20))
'''
7|
6|
5|
4|
3|
2|    p
1|  k
0|_____________________
 0  1  2  3  4  5  6  7







'''