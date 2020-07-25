def sub(a):
	if 0 in a:
		return "YES"
	sums = 0
	s = set()
	for i in range(len(a)):
		sums += a[i]
		if sums == 0 or sums in s:
			return "YES"
		s.add(sums)
	return "NO"

a = [-3,2,1,1,6]
print(sub(a))


