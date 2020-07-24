def missing(a):
	for i in range(1,len(a)+1):
		if i not in a:
			return i
a = [1,2,3,4,6,7,8,9]
print(missing(a))