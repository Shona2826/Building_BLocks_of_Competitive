a = [2,1,4,3,5]
for i in range(1,len(a)):
	if a[i-1] < a[i]:
		continue
	elif i>=2 and a[i-1] > a[i]:
		if a[i-2] > a[i]:
			temp = a[i-2]
			a[i-2] = a[i]
			a[i] = temp
		temp = a[i-1]
		a[i-1] = a[i]
		a[i] = temp
	else:
		temp = a[i-1]
		a[i-1] = a[i]
		a[i] = temp
print(a)
