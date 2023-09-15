def can_concat(s, words, memo={}):
		if s in memo:
				return memo[s]
		if s == '':
				return True
		
		for word in words:
				s_start = s.startswith(word)
				if s_start:
						new_s = s.replace(word, '', 1)
						nxt_iter = can_concat(new_s, words, memo)
						if nxt_iter:
								memo[s] = True
								return True
		memo[s] = False
		return False
						

print(can_concat("oneisnone", ["on", "e", "is"]))