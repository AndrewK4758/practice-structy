def nesting_score(string):
	stack = [0]
	
	for i in range(len(string)):
		if string[i] == '[':
			stack.append(0)
		else:
			score = stack.pop()
			if score == 0:
				stack[-1] += 1
			else:
				stack[-1] += 2 * score

	return stack[0]
		
print(nesting_score("[[][][]]"))