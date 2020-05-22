s = "suman is a good girl"
def reverse_order(s):
	s= s[::-1]
	def reverse_range(s,start,end):
		while start < end:
			s[start],s[end] = s[end],s[start]
			start,end = start+1,end-1
	start = 0
	while True:
		end = s.find(' ',start)
		print(end)
		if end < 0:
			break
		reverse_range(s,start,end-1)
		start = end + 1
	reverse_range(s,start,len(s)-1)
	return s
print(reverse_order(s))