s = "suman goel"
def snake_string(s):
	result = []
	for i in range(1,len(s),4):
		result.append(s[i])
	for i in range(0,len(s),2):
		result.append(s[i])
	for i in range(3,len(s),4):
		result.append(s[i])
	return ''.join(result)
print(snake_string(s))