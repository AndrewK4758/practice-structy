def paired_parentheses(string):
	if string == '':
		return True
	if string.count('(') == string.count(')'):
		if string.index('(') < string.index(')'):
			return True
		else:
			return False
	else:
		return False	

print(paired_parentheses("(david)((abby))"))