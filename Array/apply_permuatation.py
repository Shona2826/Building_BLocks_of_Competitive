a = [3,1,2,0]
perm = [3,1,2,0]
for i in range(len(a)):
	nexts = i
	while perm[nexts] >= 0:
		a[i] , a[perm[nexts]] = a[perm[nexts]],a[i]
		temp = perm[nexts]
		perm[nexts] -= len(perm)
		nexts = temp
perm[:] = [a + len(perm) for a in perm]
print(a)