s = "aacdbda"
def replace_and_remove(s):
	write_index,a_count = 0,0
	for i in range(len(s)):
		if s[i] != 'b':
			s[write_index] = s[i]
			write_index += 1
		if s[i] == 'a':
			a_count += 1
	cur_index = write_index - 1
	write_index += a_count - 1
	final_size = write_index + 1
	while cur_index >= 0:
		if s[cur_index] == 'a':
			s[write_index - 1:write_index+1] = 'dd'
			write_index -= 2
		else:
			s[write_index] = s[cur_index]
			write_index -= 1
		cur_index -= 1
	return s
print(replace_and_remove(s))