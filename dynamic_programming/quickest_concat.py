def quickest_concat(s, words):
	res = _quickest_concat(s, words, memo={})
	if res == float('inf'):
		return -1
	else:
		return res

def _quickest_concat(s, words, memo):
	if s in memo:
		return memo[s]
	if s == '':
		return 0
	
	min_concat = float('inf')
	for word in words:
		s_start = s.startswith(word)
		if s_start:
			next_s = s.replace(word, '', 1)
			concat_num = _quickest_concat(next_s, words, memo) +1
			min_concat = min(min_concat, concat_num)
	
	memo[s] = min_concat
	return memo[s]
print(quickest_concat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']))