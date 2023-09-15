def befitting_brackets(string):
	stack = []

	brackets = {
		'(' : ')',
		'{' : '}',
		'[' : ']'
	}
	for bracket in string:
		if bracket in brackets:
			print(brackets[bracket])
			stack.append(brackets[bracket])
		else:
			if stack and stack[-1] == bracket:
				stack.pop()
			else:
				return False
	return len(stack) == 0

print(befitting_brackets('(){}[](())'))