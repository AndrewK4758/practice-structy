def max_palin_sequence(string):
		return _max_palin_sequence(string, 0, len(string)-1, memo={})

def _max_palin_sequence(string, i, j, memo={}):
	
		if string[i:j] in memo:
				return memo[string[i:j]]
			
		if i == j:
				return 1
		if i > j:
				return 0
			
		if string[i] == string[j]:
				memo[string[i:j]] = _max_palin_sequence(string, i+1, j-1, memo) + 2
		else:
				memo[string[i:j]] = max(
						_max_palin_sequence(string, i+1, j, memo),
						_max_palin_sequence(string, i, j-1, memo)
				)
	
		return memo[string[i:j]]
					
print(max_palin_sequence("luwxult"))