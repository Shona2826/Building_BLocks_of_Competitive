def rotate(a):
	last = len(a)-1
	for i in range(len(a)):
		a[i],a[last] = a[last],a[i]

	return a

a = [1,2,3,4,5]
print(rotate(a))
