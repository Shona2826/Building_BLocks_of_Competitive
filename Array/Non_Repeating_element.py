def repeat(a):
	b =[]
	count = 0
	b = list.copy(a)
	for i in range(len(a)):
		b.remove(a[i])
		if a[i] not in b:
			count = 1
			return a[i]
	if count == 0:
		return -1

a = [1,5,3,4,3,5,6,1]
print(repeat(a))