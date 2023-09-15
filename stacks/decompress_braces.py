def decompress_braces(string):
	stack = []

	for ele in string:
		if ele in '123456789':
			stack.append(int(ele))
		else:
			if ele == '}':
				group = ''
				while isinstance(stack[-1], str):
					chars = stack.pop()
					group = chars + group
					print(group)
				mult = stack.pop()
				stack.append(group * mult)
			elif ele != '{':
				stack.append(ele)
	return ''.join(stack)

			

print(decompress_braces("2{q}3{tu}v"))