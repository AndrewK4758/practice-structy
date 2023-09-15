def knightly_number(n, m, kr, kc, pr, pc, memo={}):
	key = (m, kr, kc)
	if key in memo:
		return memo[key]
	
	if kr < 0 or kr >= n or kc < 0 or kc >= n:
		return 0
	
	knight_pos = (kr, kc)
	pawn_pos = (pr, pc)

	if m == 0:
		if knight_pos == pawn_pos:
			return 1
		else:
			return 0
	
	deltas = [(2,1), (2,-1), (1,2), (1,-2), (-2,1), (-2,-1), (-1,2), (-1,-2)]

	count = 0
	for delta in deltas:
		a, b = delta
		nxt_row = kr + a
		nxt_col = kc + b
		count += knightly_number(n, m-1, nxt_row, nxt_col, pr, pc, memo)
		memo[key] = count
	return count
	

print(knightly_number(8, 2, 7, 1, 7, 1))



















'''
0|
1|              k
2|
3|
4|
5|
6|
7|________________
 0 1 2 3 4 5 6 7 8
'''