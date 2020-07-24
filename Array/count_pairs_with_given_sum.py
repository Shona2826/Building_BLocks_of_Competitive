def pairs(a,k):
	res = 0
	count = 0
	for i in range(len(a)):
		res = k-a[i]
		for j in range(len(a)):
			if i != j and res == a[j]:
				count += 1
		j = 0
	return count//2

a = [1,1,1,1]
k = 2
print(pairs(a,k))
