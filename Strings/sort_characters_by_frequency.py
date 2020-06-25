from collections import Counter
def characters(s):
	sol = Counter(s)
	res = ''
	sol = sol.most_common()
	for letter,count in sol:
		res += letter*count
	
	print(res)

a = "sumassaaaaaan"
characters(a)